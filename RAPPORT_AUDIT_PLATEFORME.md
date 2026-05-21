# Rapport d'audit — Plateforme de révision M2 CCA

Audit réalisé le 2026-05-21. Périmètre : architecture, code, performance, UI/design,
expérience d'apprentissage, accessibilité, maintenabilité.

> **Rappel de contrainte.** Le contenu rédigé des leçons (`getCoursHTML`, `getSynthHTML`)
> est traité comme intouchable et n'a pas été évalué sur le fond. Seuls les énoncés de
> quiz, les flashcards, le code et l'UI sont jugés modifiables. Aucun correctif n'est
> appliqué : ce document est une proposition à valider.

---

## 1. Synthèse exécutive — les 5 points prioritaires

1. **Collision d'identifiants de checklist entre cours (bug de données utilisateur).**
   `inge_fi.html` et `conduite_chgt.html` utilisent tous deux des ids `cc1`, `cc2`, …
   stockés dans la même clé `localStorage` (`m2cca_state`). Cocher « CMPC » en
   Ingénierie financière coche aussi « Définition du changement » en Conduite du
   changement. **Impact : élevé. Effort : moyen.**

2. **Les anneaux de progression de l'accueil sont faux.** `data/courses.json` référence
   des ids (`if1…if20`, `r1…r20`) qui ne sont jamais cochés par les pages de cours
   (`cc*`, `rf*`). Résultat : Ingénierie financière et RSE affichent **toujours 0 %** ;
   les 4 autres cours n'affichent que la progression des 8 à 25 premiers items sur
   33 à 127. **Impact : élevé. Effort : moyen.**

3. **Duplication massive du code.** ~530 lignes de JavaScript quasi identiques
   (navigation, flashcards, quiz, checklist, deep-link) sont copiées-collées dans les
   6 fichiers de cours, soit ~3 000 lignes redondantes. Toute correction de bug doit
   être faite 6 fois. **Impact : élevé. Effort : élevé.**

4. **Mécanique de quiz perfectible.** Les options de réponse ne sont **jamais
   mélangées** : la position de la bonne réponse se mémorise au fil des tentatives.
   La reprise des erreurs n'affiche ni la réponse donnée ni l'explication, et il n'y
   a pas de mode « rejouer mes erreurs ». **Impact : élevé. Effort : faible.**

5. **Sourçage incomplet sur les gros cours.** Sur `gouv` (le plus volumineux), les
   115 flashcards et 75 questions de quiz n'ont **aucun lien vers le chapitre source** ;
   sur `strat`, 31 quiz et 16 flashcards sont concernés. La fonctionnalité « ouvrir le
   chapitre » est donc morte là où elle serait la plus utile. **Impact : moyen-élevé.
   Effort : moyen** (travail de données).

---

## 2. Cartographie du projet (Phase 1)

### 2.1 Arborescence et rôle des fichiers

```
Plateforme révision/
├── index.html            Accueil : liste des UE/cours, progression globale, recherche
├── engine.js             Moteur partagé : state, SRS, rendus partiels, export PDF
├── shared.css            Feuille de style unique (1 222 lignes)
├── <cours>.html  (×6)    Une page complète par cours (coquille + contenu + JS + données)
│     inge_fi · gouv · strat · rse · evo_orga · conduite_chgt
├── data/
│     courses.json        Catalogue : semestres, UE, coefficients, checklists d'accueil
│     <cours>.json (×6)   Données d'un cours : checklist, flashcards, quiz, annales, thèmes
├── tools/
│     sync_data.py        Synchronise data/*.json vers les objets FALLBACK inline
├── .claude/
│     build_search_index.py   Régénère l'index de recherche embarqué dans index.html
│     sync_fallback.py        Variante de synchronisation
│     server.py                Petit serveur de dev (12 lignes)
│     + ~20 scripts one-shot   Migrations historiques (rewrite_*, patch_*, fix_*, tag_*…)
├── RAPPORT_AUDIT_COUVERTURE.md   Audit de couverture (cours SI) — antérieur
├── RAPPORT_AUDIT_INGE_FI.md      Audit de couverture (Ingénierie financière) — antérieur
└── .evo_pdf_extract.txt          Extraction PDF brute (résidu de travail)
```

### 2.2 Stack technique réelle

- **Site statique pur** : HTML + CSS + JavaScript vanilla (ES2017+). Aucun framework,
  aucun bundler, aucune dépendance npm, aucune étape de build pour le front.
- **Persistance** : `localStorage` uniquement (progression, scores, SRS, streak).
- **Polices** : Google Fonts en CDN (Playfair Display, Inter, JetBrains Mono).
- **Outillage** : scripts Python utilitaires (synchronisation données ↔ FALLBACK,
  génération de l'index de recherche). Non requis à l'exécution.
- **Hébergement** : conçu pour fonctionner aussi bien servi en HTTP qu'ouvert en
  `file://` (d'où les objets `FALLBACK` inline et l'index de recherche embarqué).

### 2.3 Architecture d'un fichier de cours

Chaque `<cours>.html` est autoportant et contient, dans cet ordre :

1. **Coquille HTML** : `<head>`, nav, conteneur `#appRoot`.
2. **`const FALLBACK = {…}`** : copie intégrale du `data/<cours>.json` (utilisée si le
   `fetch` échoue, typiquement en `file://`).
3. **Contenu rédigé** : `getCoursHTML()` (les chapitres `div.course-chapter`) et
   `getSynthHTML()` (la fiche de synthèse). **→ contenu de cours, intouchable.**
4. **~530 lignes de logique applicative** : navigation par onglets, checklist,
   flashcards, quiz, deep-link, filtre par thème. **→ identique d'un cours à l'autre.**
5. **Module « examen blanc »** : spécifique au cours (voir 2.5).
6. **Boot** : `loadJSON('data/<cours>.json', FALLBACK)` puis `renderNav()`.

`engine.js` regroupe ce qui est *déjà* mutualisé : `state`/`localStorage`, l'algorithme
SRS (SM-2 simplifié), les rendus partiels flashcard/quiz, le quiz Vrai/Faux, les
confettis, le ripple et l'export PDF.

### 2.4 Frontière contenu de cours / contenu modifiable

| Élément | Emplacement | Statut |
|---|---|---|
| Leçons rédigées | `getCoursHTML()` dans chaque HTML | **Intouchable** |
| Fiche de synthèse | `getSynthHTML()` dans chaque HTML | **Intouchable** |
| Annales (sujets réels + corrigés) | `data/<cours>.json` → `annales` | Sources — fidélité stricte |
| Énoncés de quiz | `data/<cours>.json` → `quizQuestions` | **Modifiable** (forme) |
| Flashcards | `data/<cours>.json` → `flashcards` | **Modifiable** (forme) |
| Checklist | `data/<cours>.json` → `checklistItems` | **Modifiable** |
| Examen blanc (générateurs) | dans chaque HTML | **Modifiable** |
| Code, UI, styles, navigation | `engine.js`, `shared.css`, HTML | **Modifiable** |

### 2.5 Fonctionnalités existantes

- **Accueil** : cartes UE par semestre, coefficients, anneaux de progression,
  3 statistiques animées, barre de streak, **recherche plein texte** sur le contenu
  de tous les cours (index pré-calculé embarqué).
- **Par cours**, 5 onglets : Checklist · Cours (avec filtre par axe + deep-link) ·
  Synthèse · Flashcards · Quiz · Annales · Examen blanc.
- **Flashcards** : carte recto/verso, **répétition espacée SM-2** (modes « SRS » et
  « mélangé »), aperçu des intervalles, raccourcis clavier, badge source cliquable.
- **Quiz** : QCM tirés au sort (20 max), timer optionnel 30 s/question, explication
  par question, score, historique des 5 dernières parties, liste des erreurs.
  Un type **Vrai/Faux multiple** est codé dans `engine.js` mais **jamais utilisé**.
- **Examen blanc** : 3 implémentations distinctes selon le cours —
  dossiers paramétrés à valeurs aléatoires (`inge_fi`, `strat`),
  dossiers/QCM (`gouv`, `rse`), sujets-types rédactionnels (`evo_orga`, `conduite_chgt`).
- **Annales** : sujets réels d'examen + corrigés dépliables, onglets multi-annales.
- **Export PDF** transversal (cours, annales, examen) via impression navigateur.

### 2.6 Volumétrie des contenus

| Cours | Checklist | Flashcards | Quiz | Annales | Thèmes |
|---|---|---|---|---|---|
| conduite_chgt | 40 | 46 | 29 | 2 | 6 |
| evo_orga | 33 | 41 | 25 | 1 | 5 |
| gouv | 127 | 115 | 75 | 2 | 3 |
| inge_fi | 56 | 67 | 61 | 1 | 4 |
| rse | 41 | 40 | 33 | 1 | 4 |
| strat | 38 | 49 | 68 | 3 | 4 |

### 2.7 Éléments dupliqués, morts ou incohérents (relevé)

- **Code dupliqué** : ~530 lignes JS identiques × 6 fichiers (vérifié par `diff` :
  le bloc `switchTab → toggleErrors` de `inge_fi.html` et de `strat.html` est
  rigoureusement identique).
- **Données dupliquées** : chaque `data/<cours>.json` existe aussi en copie inline
  (`FALLBACK`). Aujourd'hui synchronisées (vérifié), mais via un script manuel.
- **Fonctionnalité morte** : le quiz Vrai/Faux (`renderTFQuestionInline`,
  `selectTFAnswer`, `finalizeTFAnswer` dans `engine.js`) — 0 question `type:"tf"`
  dans les 6 fichiers de données.
- **Artefact de copier-coller** : `inge_fi.html:4325` journalise `console.error('[gouv] boot error'…)` — étiquette du mauvais cours.
- **Incohérence d'ids** : checklist `cc*` partagée par 2 cours ; ids d'accueil
  (`courses.json`) ≠ ids des pages de cours (voir §3.1).
- **Scripts one-shot** : `.claude/` contient une vingtaine de scripts de migration
  historiques (`rewrite_*`, `patch_*`, `fix_*`, `insert_*`, `clean_*`, `tag_*`) —
  inertes mais encombrants.
- **Résidu** : `.evo_pdf_extract.txt` à la racine, sans rôle applicatif.
- **`flashcards` sans `id`** dans `strat` (et 1 doublon : « Stratégie adaptative vs
  stratégie intentionnelle » apparaît deux fois).

---

## 3. Audit par axe (Phase 2)

### 3.1 Technique / Architecture

**Constat A — Collision d'ids de checklist.**
`engine.js:26` stocke la progression dans un dictionnaire global `state.checked`
indexé par `id` d'item. `inge_fi.html` (checklist `cc1…cc56`) et `conduite_chgt.html`
(checklist `cc1…cc40`) partagent donc les clés `cc1…cc40`.
*Impact :* progression faussée entre deux cours, line-through visible sur des items
non révisés, ressenti « plateforme buguée ».
*Recommandation :* préfixer tout id par la clé de cours (`inge_fi:cc1`,
`conduite_chgt:cc1`…), ou générer les ids à partir de `quizKey`. Migration douce :
lire l'ancienne clé si la nouvelle est absente.

**Constat B — Anneaux de progression de l'accueil non fonctionnels.**
`index.html:252` calcule `getProgress(c.checklistItems)` sur les `checklistItems` de
`data/courses.json`. Or ces ids (`if1…if20` pour inge_fi, `r1…r20` pour rse) ne
correspondent jamais aux ids cochés dans les pages de cours.
*Impact :* inge_fi et rse affichent toujours 0 % ; les autres cours sous-représentent
leur avancement (l'accueil ne voit que 8 à 25 items sur 33 à 127).
*Recommandation :* une seule source de vérité pour la checklist. Faire pointer
l'accueil sur les vraies données de cours (`data/<cours>.json`), ou exposer un agrégat
de progression dans `localStorage` que l'accueil relit.

**Constat C — Duplication de ~530 lignes JS × 6.**
Les fonctions `switchTab`, `renderNav`, `renderChecklist`, `initFlashcards`,
`renderQuizQuestion`, `parseDeepLink`, etc. sont identiques d'un cours à l'autre.
*Impact :* tout bug se corrige 6 fois ; tout oubli crée une divergence silencieuse.
C'est l'origine probable des constats A, B et de l'artefact `[gouv]`.
*Recommandation :* déplacer ce bloc dans `engine.js`. Le cours ne garderait que ses
données + son module examen. Gain estimé : ~3 000 lignes supprimées, fichiers de
cours allégés de 30 à 40 %.

**Constat D — Double source de données (JSON + FALLBACK inline).**
Le besoin (`file://`) est légitime, mais la duplication est maintenue à la main via
`tools/sync_data.py`. Un oubli de synchronisation = données différentes selon le mode
d'ouverture, sans alerte.
*Recommandation :* à conserver tant que l'usage `file://` est requis, mais y ajouter
un garde-fou : un test de cohérence (ou un en-tête de version `data-rev` comparé au
chargement) qui signale toute divergence. Si l'usage `file://` disparaît, supprimer
purement les `FALLBACK`.

**Constat E — Gestion d'erreurs correcte mais perfectible.**
Bon : garde d'erreur globale (`engine.js:8`), `loadJSON` avec timeout 4 s et fallback,
`try/catch` au boot. À corriger : `inge_fi.html:4325` logge `[gouv]` ; le boot ne
vérifie pas que `flashcards`/`quizQuestions` existent (un JSON tronqué planterait le
rendu du quiz plus loin, hors du `try`).

**Constat F — Découplage contenu / logique / présentation.**
La présentation (`shared.css`) est bien séparée. En revanche le **contenu rédigé** est
inséré en dur dans `getCoursHTML()` au sein du `<script>` — il n'est ni dans le DOM ni
dans le JSON. C'est ce qui oblige la recherche globale à ré-extraire les chapitres en
équilibrant les `<div>` à la main (`index.html:408-425`), solution fragile.
*Recommandation (à moyen terme) :* externaliser le contenu de cours en données
structurées (chapitres en JSON ou HTML statique réellement dans le DOM). À ne faire
que si la contrainte de fidélité peut être garantie par une migration automatisée.

**Ce qui est bien vu.** Le choix « site statique sans build » est cohérent avec un
projet personnel mono-utilisateur : zéro install, ouvrable partout, pérenne. L'algo
SRS et les rendus partiels (`updateFlashCardPartial`) sont propres et bien commentés.
L'export PDF par iframe d'impression est une solution simple et robuste.

### 3.2 Performance

**Constat A — Poids des pages de cours.**
Les fichiers font de 162 à 370 Ko (`gouv.html` : 370 Ko). Le contenu rédigé est
incompressible (c'est le cours), mais ~530 lignes de JS dupliqué + le `FALLBACK`
inline gonflent inutilement chaque page.
*Recommandation :* mutualiser le JS (constat C) le rend cacheable une seule fois via
`engine.js`. Gain réseau réel dès la 2ᵉ page de cours visitée.

**Constat B — Index de recherche embarqué de 225 Ko.**
`index.html:377` est une seule ligne de 225 Ko (l'index pré-calculé). L'accueil pèse
260 Ko surtout à cause d'elle. C'est le prix du fonctionnement `file://`.
*Impact :* modéré (statique, gzippé en HTTP ≈ 60-70 Ko ; en `file://` non compressé).
*Recommandation :* acceptable si `file://` est un vrai besoin. Sinon, charger l'index
en `fetch` paresseux au premier focus du champ de recherche.

**Constat C — Polices Google Fonts en CDN.**
3 familles, ~10 graisses. Le motif `preload + onload` évite le blocage du rendu, mais
il reste une dépendance réseau externe et un risque de FOUT.
*Recommandation :* réduire aux graisses réellement utilisées ; envisager l'auto-
hébergement des `.woff2` (cohérent avec un site « tout local »).

**Constat D — Rendu par `innerHTML` massif.**
Chaque changement d'onglet reconstruit `#appRoot` entièrement. Acceptable vu la taille
des écrans, et les rendus partiels flashcard/quiz limitent déjà la casse là où ça
compte. Pas d'action prioritaire.

*Bilan : la performance n'est pas un problème ressenti pour un usage mono-utilisateur.
Les gains viennent surtout, gratuitement, de la déduplication du code.*

### 3.3 Style / UI / Design

**Constat A — Deux couleurs d'accent, pas une.**
`shared.css:7-34` définit un accent bleu (`--accent #3d72b4`) **et** un accent cuivre
(`--copper #c88346`), utilisés ensemble dans presque tous les dégradés (titres, barres
de progression, anneaux). L'objectif « une seule couleur d'accent » n'est pas tenu.
*Impact :* identité visuelle correcte mais moins nette qu'un système strict.
*Recommandation :* choisir UN accent (le bleu acier est le plus lisible sur fond
sombre), reléguer le cuivre au rang de couleur sémantique ponctuelle (streak, alertes).
Remplacer les dégradés bi-teintes par des aplats ou des dégradés mono-teinte.

**Constat B — Alias de couleur trompeur.**
`--pink` existe encore (`shared.css:23`) et vaut `#c88346` (du cuivre). Vestige d'une
ancienne palette rose. Utilisé tel quel dans `renderChecklist` (`stop-color="var(--pink)"`).
*Recommandation :* supprimer `--pink`, renommer en `--copper` partout (quick win).

**Constat C — Cohérence et hiérarchie typographiques.**
Bon : 3 polices à rôle clair (Playfair = titres, Inter = corps, JetBrains Mono =
chiffres/labels). Échelle de tailles cohérente, `clamp()` pour le responsive.
À surveiller : beaucoup de styles en ligne (`style="font-size:0.7rem;color:…"`)
dispersés dans le JS — la hiérarchie est dupliquée plutôt que centralisée en classes.

**Constat D — Qualité perçue.**
La plateforme fait **soignée**, pas amateur : fond texturé, blobs, anneaux SVG,
animations de compteur, confettis, micro-interactions (ripple). Le risque inverse
existe : un léger excès d'effets. Rien de bloquant.

**Constat E — Responsive.**
Points de rupture présents (768 / 720 / 640 / 480 px), nav-tabs scrollable,
tableaux d'examen réduits sur mobile, `prefers-reduced-motion` respecté. Globalement
bon. À vérifier sur petit écran : les `.fc-actions` à 3 boutons et les tableaux
comparatifs denses du contenu de cours.

### 3.4 Expérience d'apprentissage

**Constat A — Quiz : options jamais mélangées.**
`renderQuizQuestion` (`inge_fi.html:3010`) rend `q.o` dans l'ordre stocké ; la bonne
réponse `q.c` est toujours au même indice. Les questions sont tirées au sort, mais pas
les propositions.
*Impact :* à la 2ᵉ ou 3ᵉ tentative, l'étudiant mémorise « la réponse est en C » au
lieu du savoir. C'est contraire à l'objectif de révision.
*Recommandation :* mélanger les options au moment du rendu et recalculer l'indice
correct. Effort faible, impact élevé.

**Constat B — Reprise des erreurs trop pauvre.**
`showQuizResult` (`inge_fi.html:3097-3105`) liste les erreurs avec seulement
l'énoncé + la bonne réponse. Manquent : la réponse donnée par l'étudiant et
l'explication `q.e` (pourtant disponible). Aucun mode « rejouer uniquement mes
erreurs ».
*Recommandation :* enrichir la fiche d'erreur (réponse donnée en rouge + bonne
réponse + explication) et ajouter un bouton « Rejouer mes N erreurs ». Effort faible.

**Constat C — Flashcards trop longues.**
Longueur moyenne de réponse : 369 (inge_fi) à 422 (strat) caractères, avec des cartes
jusqu'à 800 caractères (ex. strat « L'avantage parental »). Une flashcard efficace
teste **un** fait ; ici plusieurs cartes sont des mini-leçons à puces.
*Impact :* le rappel actif fonctionne mal sur un bloc dense — on « relit » au lieu de
« se tester ».
*Recommandation :* scinder les cartes multi-puces en cartes atomiques, **sans
modifier le savoir** (juste la granularité). Voir §6 pour un exemple.

**Constat D — SRS sans plafond de session.**
`initFlashcards` (`inge_fi.html:2773`) appelle `srsBuildQueue(fcSRS, total)` sans
`maxSize`. Au premier usage, toutes les cartes sont « nouvelles » → la session = le
paquet entier (jusqu'à 115 cartes pour gouv).
*Impact :* session ingérable, abandon probable, le bénéfice du SRS (petites doses
quotidiennes) est perdu.
*Recommandation :* plafonner (ex. 15-20 nouvelles + toutes les dues) via le 3ᵉ
argument déjà prévu par `srsBuildQueue`.

**Constat E — Type Vrai/Faux codé mais inutilisé.**
Tout le rendu Vrai/Faux multiple existe dans `engine.js` (corrections détaillées,
scoring) mais aucun cours n'a de question `type:"tf"`.
*Recommandation :* soit créer quelques questions V/F par cours (le format est
excellent pour traquer les confusions), soit retirer le code mort. À décider.

**Constat F — Parcours de révision.**
Bon : streak, checklist par cours, historique des scores, badge source cliquable
reliant flashcard/quiz au chapitre. Manques : aucune vue « que réviser aujourd'hui »
(cartes dues tous cours confondus), aucune reprise du quiz là où on s'est arrêté,
pas de bilan de progression dans le temps.
*Recommandation :* à terme, un tableau de bord d'accueil « X cartes dues, Y quiz à
refaire » par cours.

**Constat G — Simulateur de notes.**
Il n'existe pas de « simulateur de notes » global (calcul de moyenne pondérée par
coefficient d'UE) ; `courses.json` contient pourtant les coefficients. Ce qui existe
est l'**examen blanc** par cours, qui rend une note /20 bien construite (notamment
les dossiers à valeurs aléatoires de `inge_fi`/`strat`, où la correction est
recalculée par formule — robuste). Si un simulateur de moyenne générale est souhaité,
c'est une fonctionnalité à créer.

### 3.5 Accessibilité

**Constat A — Sémantique et clavier.**
Les items de checklist (`inge_fi.html:2752`), la carte flashcard et les pills de
thème sont des `<div onclick>` : non focусables, non activables au clavier, sans
`role`/`aria`. Les onglets de nav, eux, sont bien des `<button>` (bon point).
*Recommandation :* convertir en `<button>` ou ajouter `role`, `tabindex="0"`,
gestion `Enter`/`Espace` et `aria-checked` pour la checklist.

**Constat B — Très peu d'ARIA.**
~1 attribut `aria-*` par page de cours, aucun `role`. Les anneaux SVG ont un
`aria-label`, c'est à peu près tout. Les zones mises à jour dynamiquement (résultat
de quiz, correction) ne sont pas annoncées (`aria-live`).
*Recommandation :* `aria-live="polite"` sur `#appRoot` ou les zones de feedback ;
labels sur les champs ; `lang="fr"` est déjà présent (bon).

**Constat C — Contrastes.**
Fond très sombre, texte clair : globalement bon. À vérifier : `--text3 #5e6a7c` sur
`--bg #0a0e15` pour les libellés secondaires (ratio limite ~4.5:1) et le texte sur
les badges colorés translucides.
*Recommandation :* audit de contraste ciblé sur les textes `--text3` et les pills.

**Constat D — Focus visible.**
`:focus-visible` est stylé globalement (`shared.css:72`) — bon point. Le problème est
qu'il ne sert à rien sur les éléments non focusables (constat A).

### 3.6 Maintenabilité / Évolutivité

**Constat A — Ajouter un cours est lourd.**
Il faut : créer `data/<cours>.json`, dupliquer un HTML de cours entier, y réécrire
`getCoursHTML`/`getSynthHTML`/`FALLBACK`/le module examen, ajouter l'entrée dans
`courses.json`, régénérer l'index de recherche. Beaucoup d'étapes, beaucoup de copier-
coller. C'est exactement le terreau des bugs A et B du §3.1.
*Recommandation :* après mutualisation (constat C du §3.1), un nouveau cours = un
template HTML mince + un JSON. Idéalement une page de cours générique unique
paramétrée par `?cours=xxx`.

**Constat B — Conventions de nommage incohérentes.**
Ids de checklist : `cc*` (inge_fi & conduite_chgt), `g*`, `s*`, `eo*`, `rf*`,
`r*`, `if*` selon l'endroit. Préfixes flashcards : `fc*` ici, absent là (strat).
*Recommandation :* convention unique documentée (`<cours>:<type><n>`).

**Constat C — Dossier `.claude/` encombré.**
~20 scripts de migration one-shot mêlés aux 2-3 scripts réellement utiles.
*Recommandation :* archiver les scripts one-shot (sous-dossier `archive/` ou
suppression), garder `sync_data.py` et `build_search_index.py` documentés dans un
court `README`/`CLAUDE.md`.

**Constat D — Pas de documentation projet.**
Aucun `README`/`CLAUDE.md` ne décrit le processus « modifier un cours = éditer JSON +
HTML + relancer les scripts ». Cette connaissance n'existe aujourd'hui qu'en mémoire.
*Recommandation :* un court `CLAUDE.md` à la racine décrivant l'architecture et le
flux de mise à jour.

**Constat E — Versionnement.**
Le projet n'est pas un dépôt git. Vu la quantité de contenu sensible et irремplaçable
(les cours), c'est un risque réel de perte.
*Recommandation :* `git init` + commits réguliers. Quick win à fort filet de sécurité.

---

## 4. Tableau de priorisation

Trié par rapport impact / effort décroissant.

| # | Recommandation | Axe | Impact | Effort | Priorité |
|---|---|---|---|---|---|
| 1 | Mélanger les options de quiz au rendu | Apprentissage | Élevé | Faible | ★★★★★ |
| 2 | Enrichir la reprise des erreurs (réponse donnée + explication) | Apprentissage | Élevé | Faible | ★★★★★ |
| 3 | `git init` + commits | Maintenabilité | Élevé | Faible | ★★★★★ |
| 4 | Supprimer `--pink`, renommer en `--copper` | Style | Faible | Faible | ★★★★ |
| 5 | Corriger l'artefact `[gouv]` (`inge_fi.html:4325`) | Technique | Faible | Faible | ★★★★ |
| 6 | Plafonner la session SRS (maxSize) | Apprentissage | Élevé | Faible | ★★★★★ |
| 7 | Préfixer les ids de checklist par cours | Technique | Élevé | Moyen | ★★★★★ |
| 8 | Réparer les anneaux de progression de l'accueil | Technique | Élevé | Moyen | ★★★★★ |
| 9 | Bouton « Rejouer mes erreurs » | Apprentissage | Élevé | Moyen | ★★★★ |
| 10 | Passer à un seul accent couleur | Style | Moyen | Moyen | ★★★★ |
| 11 | Checklist/flashcard/pills accessibles au clavier | Accessibilité | Moyen | Moyen | ★★★★ |
| 12 | Compléter `src`/`srcChap` sur gouv et strat | Apprentissage | Moyen-élevé | Moyen | ★★★★ |
| 13 | Scinder les flashcards trop longues | Apprentissage | Moyen | Moyen | ★★★ |
| 14 | `aria-live` + ARIA sur zones dynamiques | Accessibilité | Moyen | Moyen | ★★★ |
| 15 | Archiver les scripts one-shot de `.claude/` | Maintenabilité | Faible | Faible | ★★★ |
| 16 | Ajouter un `CLAUDE.md` d'architecture | Maintenabilité | Moyen | Faible | ★★★★ |
| 17 | Mutualiser les ~530 lignes JS dans `engine.js` | Technique | Élevé | Élevé | ★★★★ |
| 18 | Décider du sort du quiz Vrai/Faux (créer ou supprimer) | Apprentissage | Moyen | Moyen | ★★★ |
| 19 | Garde-fou de cohérence JSON ↔ FALLBACK | Technique | Moyen | Faible | ★★★ |
| 20 | Réduire les graisses de police / auto-héberger | Performance | Faible | Moyen | ★★ |

---

## 5. Quick wins (fort impact, faible effort)

À traiter en premier, chacun isolément, sans risque pour le contenu de cours :

1. **Mélanger les options de quiz** (#1) — quelques lignes dans `renderQuizQuestion` /
   `updateQuizQuestionPartial` : permuter `q.o` et suivre le nouvel indice correct.
2. **Reprise des erreurs enrichie** (#2) — afficher dans `showQuizResult` la réponse
   choisie + `q.e`. Données déjà disponibles.
3. **Plafond de session SRS** (#6) — passer un 3ᵉ argument à `srsBuildQueue`
   (le paramètre `maxSize` existe déjà).
4. **`git init`** (#3) — filet de sécurité immédiat sur un contenu irremplaçable.
5. **Nettoyer la couleur `--pink`** (#4) — suppression de l'alias, renommage.
6. **Corriger le log `[gouv]`** (#5) dans `inge_fi.html:4325`.
7. **`CLAUDE.md` d'architecture** (#16) — fige le processus de mise à jour.
8. **Archiver `.claude/*` one-shot** (#15) — clarifie le dépôt.

Effet combiné : le quiz redevient un vrai outil d'entraînement, le SRS devient
utilisable au quotidien, et le projet est sécurisé — le tout sans toucher une ligne
de cours.

---

## 6. Quiz & flashcards — exemples concrets de reformulation

> Section à relire et valider avant toute intégration. Les propositions reformulent
> **la forme** ; le fond pédagogique (le savoir des cours) reste identique.

### 6.1 Flashcard trop dense → cartes atomiques

**Actuel** (`data/inge_fi.json`, carte « Formule du CMPC », réponse de 587 caractères :
formule + 5 puces de définition + rôle du CMPC).

**Proposition — scinder en 3 cartes** (même savoir, granularité testable) :

- *Carte A* — Q : « Formule du CMPC » → R : `CMPC = Rcp × Vcp/(Vcp+Vd) + Rd × (1−IS) × Vd/(Vcp+Vd)`.
- *Carte B* — Q : « Que désignent Rcp et Rd dans le CMPC ? » → R : Rcp = rentabilité
  exigée par les actionnaires (coût des fonds propres) ; Rd = rentabilité attendue
  par les prêteurs (coût de la dette).
- *Carte C* — Q : « À quoi sert le CMPC ? » → R : c'est le taux d'actualisation de la
  VAN ; si la VAN est positive, le projet est retenu.

La carte « formule » seule permet un vrai test de mémoire ; les définitions et le
rôle deviennent des cartes distinctes plutôt qu'un pavé relu passivement.

### 6.2 Question de comptage → question de compréhension

**Actuel** (`data/conduite_chgt.json`) : « Combien de résistances classiques au
changement sont identifiées par Besombes ? »

**Limite :** teste un nombre, pas la compréhension.
**Proposition** (si le cours le permet) : conserver cette question **et** ajouter une
question sœur de type « laquelle n'est PAS une résistance identifiée par Besombes ? »,
avec 3 résistances réelles + 1 distracteur plausible — ce qui force à connaître la
liste, pas seulement son cardinal.

### 6.3 Vrai/Faux multiple — activer un format déjà codé

Le moteur sait déjà afficher des questions `type:"tf"` (4 affirmations V/F + correction
détaillée par affirmation). Exemple de question à créer pour `inge_fi`, thème
« Coût du capital » (à valider sur le cours P. Robin) :

```
Sur le coût de la dette Rd :
 - Rd se construit à partir du taux sans risque (OAT) augmenté d'un spread.   [V]
 - Rd est la moyenne des taux des emprunts passés de l'entreprise.            [F]
 - Le coût de la dette retenu dans le CMPC est net d'impôt : Rd × (1 − IS).   [V]
 - Rd se calcule avec le modèle de Gordon-Shapiro.                            [F]
```

Ce format est très efficace pour traquer les confusions classiques. **À ne créer que
si chaque affirmation est traçable au cours.**

### 6.4 Sourçage manquant (gouv, strat)

Ce n'est pas une reformulation mais un enrichissement : ajouter `src` (libellé) et
`srcChap` (n° de chapitre) aux 75 quiz et 115 flashcards de `gouv`, et aux items
concernés de `strat`, pour réactiver le badge « ouvrir le chapitre ». Travail de
données à faire en relisant le contenu — à cadrer avec toi chapitre par chapitre.

### 6.5 Reformulations de pure forme (exemples)

Les énoncés actuels sont globalement bons. Quelques resserrages possibles :

- « Selon le cours, le coût de la dette Rd se construit à partir : » →
  « Le coût de la dette Rd se construit à partir : » (« selon le cours » est
  implicite et alourdit).
- Uniformiser la ponctuation des énoncés (certains finissent par « : », d'autres
  par « ? », d'autres sans rien) — cohérence de forme.

> Aucune de ces reformulations ne change une définition, une formule ou un fait.
> Le détail item par item sera fourni sous forme de liste à cocher si tu valides
> le principe.

---

## 7. Roadmap proposée

### Phase 1 — Sécuriser et corriger (rapide, sans risque contenu)

- `git init` + premier commit.
- Quick wins quiz : mélange des options, reprise des erreurs enrichie.
- Plafond de session SRS.
- Correctifs cosmétiques : `--pink`, log `[gouv]`.
- `CLAUDE.md` d'architecture + archivage des scripts `.claude/` one-shot.

*Objectif : la plateforme devient fiable comme outil d'entraînement, et le contenu
est sauvegardé.*

### Phase 2 — Fiabiliser les données et l'apprentissage

- Préfixer les ids de checklist par cours (avec migration localStorage).
- Réparer les anneaux de progression de l'accueil (source de vérité unique).
- Bouton « Rejouer mes erreurs ».
- Compléter le sourçage `src`/`srcChap` sur gouv et strat.
- Scinder les flashcards les plus denses (validation au cas par cas).
- Accessibilité clavier sur checklist / flashcard / pills.
- Décision sur le quiz Vrai/Faux (créer un jeu de questions ou retirer le code).

*Objectif : progression juste, navigation cours ↔ révision complète, cartes efficaces.*

### Phase 3 — Refondre l'architecture et finir l'UI

- Mutualiser les ~530 lignes JS dans `engine.js` ; alléger les fichiers de cours.
- À terme : page de cours générique unique paramétrée (`?cours=xxx`).
- Garde-fou de cohérence JSON ↔ FALLBACK, voire suppression des FALLBACK si
  l'usage `file://` est abandonné.
- Système de couleurs à un seul accent.
- `aria-live` et finitions d'accessibilité.
- Éventuel tableau de bord « à réviser aujourd'hui » et/ou simulateur de moyenne
  générale pondérée par coefficient d'UE.

*Objectif : ajouter un cours devient trivial, l'identité visuelle est nette,
la plateforme passe de « très bonne » à « exemplaire ».*

---

## Annexe — Ce qui est déjà bien

Pour équilibrer : plusieurs choix sont justifiés et à conserver.

- **Site statique sans build** : adapté à un projet personnel, pérenne, ouvrable
  partout. Ne pas « moderniser » avec un framework sans raison.
- **Algorithme SRS** propre, commenté, avec aperçu des intervalles — c'est le cœur
  d'une bonne plateforme de révision et il est bien fait.
- **Examen blanc à valeurs aléatoires** (`inge_fi`, `strat`) : la correction est
  recalculée par formule, donc toujours cohérente avec l'énoncé tiré. Excellent.
- **Rendus partiels** flashcard/quiz : évitent les reconstructions DOM coûteuses.
- **Export PDF** par iframe d'impression : simple, robuste, transversal.
- **Garde d'erreur globale** + fallback de données : la plateforme ne tombe pas en
  écran noir silencieux.
- **Recherche globale** plein texte fonctionnelle même en `file://`.
- **Qualité visuelle** : la plateforme fait soignée, cohérente, agréable.

Les contraintes `file://` (FALLBACK inline, index embarqué) sont des réponses
légitimes à un vrai besoin — à ne remettre en cause que si cet usage disparaît.
