# Plateforme de révision M2 CCA

Site statique de révision (HTML + CSS + JavaScript vanilla, sans framework ni build).
Un fichier HTML par cours + un accueil. Fonctionne servi en HTTP comme ouvert en `file://`.

## Architecture

- `index.html` — accueil : catalogue des UE/cours, progression globale, recherche plein texte.
- `engine.js` — moteur partagé : persistance (`localStorage`), SRS, helpers de quiz,
  rendus partiels flashcard/quiz, export PDF.
- `shared.css` — feuille de style unique.
- `<cours>.html` (×6 : `inge_fi`, `gouv`, `strat`, `rse`, `evo_orga`, `conduite_chgt`) —
  chaque page contient : la coquille, un objet `FALLBACK` (copie des données pour `file://`),
  le contenu rédigé (`getCoursHTML`, `getSynthHTML`), la logique applicative et un module
  « examen blanc » propre au cours.
- `data/courses.json` — catalogue (semestres, UE, coefficients).
- `data/<cours>.json` — données d'un cours : `checklistItems`, `flashcards`,
  `quizQuestions`, `annales`, `themes`.
- `tools/sync_data.py` — synchronise `data/*.json` vers les objets `FALLBACK` inline.
- `.claude/build_search_index.py` — régénère l'index de recherche embarqué dans `index.html`.

## Contenu intouchable

Le contenu rédigé des leçons (`getCoursHTML`, `getSynthHTML`) et les annales (vrais
sujets d'examen) ne doivent pas être modifiés sur le fond. Les énoncés de quiz et les
flashcards sont modifiables sur la forme, en restant fidèles au savoir enseigné.

## Mettre à jour un cours

1. Éditer `data/<cours>.json`.
2. Lancer `python3 tools/sync_data.py` pour répercuter dans les objets `FALLBACK` inline.
3. Si le contenu rédigé des chapitres a changé : `python3 .claude/build_search_index.py`.

## Persistance (clés localStorage)

- `m2cca_state` — items de checklist cochés, **namespacés par cours** (`inge_fi:cc1`).
- `m2cca_progress` — agrégat `{done,total}` par cours, lu par l'accueil.
- `m2cca_quiz_<cours>` — historique des scores de quiz.
- `m2cca_srs_<...>` — état de répétition espacée des flashcards.
- `m2cca_examen_<cours>` — scores d'examen blanc.
- `m2cca_streak` — série de jours consécutifs.

`COURSE_KEY` (dans `engine.js`) est dérivé du nom de fichier et sert à namespacer la
persistance pour éviter les collisions d'identifiants entre cours.

## Prévisualisation locale

Le chemin du projet contient un espace et un accent. Pour servir le site en local,
copier les fichiers vers un dossier sans caractère spécial puis lancer un serveur HTTP
depuis cette copie.
