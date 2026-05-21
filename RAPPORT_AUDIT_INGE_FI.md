# Rapport d'audit de couverture - M2 CCA Ingénierie Financière

Date : 2026-05-21

## Sources auditées (dossier « Ingénierie Financière », périmètre validé : tout le dossier)

Cours et supports du professeur :
- `Chapitre 1 le Béta.pptx` (slides à dominante formules, peu de texte)
- `chapitre 1 Madeline .pdf` (prise de notes rédigée du chapitre 1, 11 pages)
- `Chapitre 2 Les Marchés de Capitaux.pptx` (monétaire, obligataire, actions, dérivés)
- `Chapitre 7 Critères extra financiers .pptx` (ESG, Donut, Scopes, ESRS)
- `Applications Chap1 Béta.docx` (7 applications, extraits DSCG 2009 à 2025)
- `Applications Marché Capitaux.docx` (19 applications)
- `Directive Omnibus.docx`
- `CSRD _ Checklist des ESRS.xlsx` (82 Disclosure Requirements détaillés)
- `Exemple Béta étudiant.xlsx` (2 feuilles, exemples de calcul de béta)
- `ordres de bourse.docx` (contient uniquement un lien YouTube, aucun texte exploitable)
- `infographie_circuit_ordre_bourse.png`, `marches_financiers_panorama...png` (visuels)
- `UE 5 - Finance.pdf` (sujet d'examen, vendredi 13 juin 2025, P. Robin)

Prises de notes antérieures (fiabilité variable, voir remarque liminaire) :
- `Ancien Prise de note Ingénierie Financière.docx`
- `Ancien Claude prise de note .docx`
- `cours_ingenierie_financiere_REDESIGN.docx`

Travail étudiant appliqué :
- `Dossier Renault` (`Dossier_RSE_Renault.docx`, `Presentation_RSE_Renault.pptx`, `script_oral...`)

## Plateforme auditée

- `data/inge_fi.json` : 4 thèmes, 36 items de checklist, 41 flashcards, 49 questions de quiz, 1 annale.
- `inge_fi.html` : un cours rédigé en 7 chapitres (fonction `getCoursHTML`).

## Remarque liminaire

1. La consigne initiale parlait de sources « au format PDF ». Le dossier ne contient que 2 PDF ; l'essentiel du cours est en PowerPoint et Word. Le périmètre retenu est l'intégralité du dossier.

2. Trois fichiers sont des prises de notes antérieures ou retravaillées (`Ancien Prise de note`, `Ancien Claude prise de note`, `cours_ingenierie_financiere_REDESIGN`). Leur contenu recoupe fidèlement les PPTX et le PDF Madeline ; ils sont utilisés comme sources de second rang (confirmation), jamais comme source unique d'une notion. Plusieurs y signalent eux-mêmes des trous (« demander à Albane », « section à compléter »).

3. Le `Dossier Renault` est un livrable étudiant (étude de cas RSE appliquée). Il mobilise les notions du chapitre 7 mais n'introduit aucune notion de cours normative. Il n'est pas retenu comme corpus de notions à auditer.

4. Diagnostic central : la plateforme `inge_fi` est globalement bien structurée et couvre les grands thèmes, mais le cours rédigé de `inge_fi.html` a été en grande partie enrichi avec des connaissances de finance générale externes aux supports du professeur. La part « intrus » est importante, surtout sur les chapitres Obligations, Coût du capital et ESG. Symétriquement, plusieurs notions explicitement traitées en cours (méthode d'interpolation du coût de la dette, prix d'équilibre en cotation, OPM, exposition au risque de taux, chronologie RSE) sont absentes.

---

# THÈME 1 - COÛT DU CAPITAL

## 1.1 OK (présent dans les sources ET dans la plateforme)

| Notion | Source | Trace plateforme |
|---|---|---|
| Définition du coût du capital (coût des ressources, rentabilité exigée par les apporteurs) | Madeline p.1 ; Ancien notes | HTML chap.4 ; fc1 |
| Formule du CMPC = Rcp×Vcp/(Vcp+Vd) + Rd×(1-IS)×Vd/(Vcp+Vd) | Chap.1 pptx ; Madeline p.1 | fc1, HTML chap.4, if1, if26 |
| Coût de la dette Rd : rentabilité attendue par les créanciers, future et non passée | Madeline p.1 | fc2 (concept), if2 |
| Rd = taux sans risque (OAT) + spread | Madeline p.1 ; Ancien Claude | HTML chap.4 (mentionné en approximation) |
| Coût net d'IS = Rd×(1-IS), déductibilité des intérêts | Chap.1 pptx ; Madeline | Q2, fc2, fc28 |
| Gordon-Shapiro : Rcp = D1/V0 + g (dividendes croissants) | Madeline p.2 | fc3, fc29, Q3, Q39, if3 |
| MEDAF : Rcp = Rf + βcp×(E(Rm)-Rf) = Rf + βcp×prime de risque | Chap.1 pptx ; Madeline p.2 | fc4, fc27, Q4, Q35, if4, if25 |
| Béta : sensibilité du titre au marché ; β>1 amplifie, β=1 réplique, β<1 défensif | Madeline p.3 | fc5, Q5, if4 |
| Béta endetté (béta des CP) vs béta désendetté (béta de l'actif économique / de l'activité) | Madeline p.3-4 | fc6, fc30, if5 |
| Formules désendettement / réendettement : β = β/[1+(D/CP)(1-IS)] et inverse | Chap.1 pptx ; Madeline p.4 | fc6, fc30, Q6, Q38, if5 |
| Méthode société non cotée : comparable coté, désendetter, moyenner, réendetter | Madeline p.4-5 | fc7, fc30, if6 |
| β = Covariance(Rtitre, Rmarché) / Variance(Rmarché) | Madeline p.3 | fc26, Q34, if24 |
| Méthode de calcul du béta par tableau (espérances, écarts, covariance, variance) | Applications 2, 3, 7 ; Madeline p.5-7 | fc26 |
| Prime d'illiquidité ajoutée au Rcp d'une société non cotée | Madeline p.9 (Application 4) | fc7, HTML chap.4, if6 |
| Règle d'arrondi (2 décimales, au supérieur) | UE5 PDF annexe 2 | fc31, Q41, if28 |

## 1.2 À AJOUTER (présent dans les sources, ABSENT ou insuffisant dans la plateforme)

- **Les 4 facteurs qui influencent le béta** (Madeline p.3) : A) la structure des coûts (charges fixes / charges variables) ; B) la sensibilité du secteur d'activité à la conjoncture ; C) la capacité à déterminer des flux futurs de trésorerie ; D) la structure financière (endettement). Notion centrale et examinable, totalement absente.
- **Distinction risque systémique / risque spécifique** (Madeline p.2 ; Ancien notes) : risque systémique (de marché, non diversifiable, donc rémunéré) vs risque spécifique (sectoriel, diversifiable, donc non rémunéré). C'est le fondement théorique du MEDAF ; absent de la plateforme.
- **Détermination du coût de la dette par interpolation linéaire** (Madeline p.5, Application 1) : encadrement du taux, calcul du TRI qui actualise les flux de la dette, puis passage net d'IS. Méthode de calcul effectivement enseignée et appliquée ; absente.
- **Béta comme pente de la droite de régression** Y = Ax + B, et **coefficient de détermination R²** (poids de la variable explicative) (Madeline p.3-4). La plateforme donne la formule Cov/Var mais n'explique pas la régression ni le R².
- **Formule du béta de la dette** : βd = (coût de la dette - taux sans risque) / (E(Rm) - taux sans risque) (Applications, cas GLI). Absente.
- **Rcp attendu ≠ rentabilité financière réellement versée** (Madeline p.2) : nuance soulignée en cours, à expliciter.
- **CMPC = taux d'actualisation de la VAN ; décision : VAN positive donc projet retenu** (Madeline p.1 et p.11). Lien évoqué mais à formaliser.
- **Remarque du professeur : « Gordon-Shapiro ne sera pas demandé à l'épreuve car trop simple »** (Ancien Prise de note ; Ancien Claude). Information de cadrage d'examen utile ; à signaler.
- **Couverture chiffrée des applications** : 7 applications corrigées existent (Innovis, Easy Sell Immo, Phone Solving, Peletier, Transvert, GLI, LVMH), extraits DSCG 2009 à 2025. La plateforme n'en exploite aucune en exercice dédié.

## 1.3 INTRUS (présent dans la plateforme, ABSENT des sources)

- **Coût de la dette « Rd ≈ charges financières / dette financière moyenne »** (fc2 et HTML chap.4). Les sources ne donnent jamais cette formule : elles enseignent Rd = OAT + spread et la détermination par interpolation (TRI). Formule de finance générale, à retirer ou à remplacer par la méthode du cours.
- **« Bouclier fiscal », CICE, ATAD, plafonnement des charges financières, hiérarchie créanciers seniors / juniors / actionnaires** (fc28, Q36, Q37). Aucune source ne mentionne ces éléments. Seule la déductibilité via (1-IS) est sourcée.
- **Effet de levier financier** : Rcp = Re + (Re-Rd)×D/CP, rentabilité économique = EBIT/Actif économique, levier positif/négatif (HTML chap.4). Notion absente des supports.
- **Structure optimale du capital, théorie du trade-off** : « valeur de l'entreprise endettée = valeur non endettée + économies fiscales - coûts de faillite » (HTML chap.4). Hors corpus.
- **Datations et attributions externes** : « Gordon-Shapiro (1956) », « Hamada (1972) », « Sharpe, Lintner, 1964 ». Le nom **« Hamada »** lui-même n'apparaît dans aucune source : le cours parle de désendettement/réendettement du béta. Les formules sont justes, mais l'habillage (noms propres, dates) est ajouté.
- **Prime d'illiquidité « de 2 à 5 % »** (fc7, Q7, HTML chap.4). La seule valeur sourcée est **4 points** (Application 4 du chapitre 1). La fourchette 2-5 % est externe.
- **Valeurs numériques illustratives non sourcées** : « OAT 10 ans ≈ 3 % en 2024 », « prime de risque ≈ 5-6 % en France » (HTML chap.4). À retirer ou marquer comme purement illustratif.
- **Anglicismes** : « WACC », « CAPM », « asset/equity beta ». Les sources n'emploient que CMPC, MEDAF. Tolérable mais à signaler.

---

# THÈME 2 - MARCHÉS FINANCIERS

## 2.1 OK (présent dans les sources ET dans la plateforme)

| Notion | Source | Trace plateforme |
|---|---|---|
| Marché organisé vs marché de gré à gré (OTC) | Chap.2 pptx ; Ancien notes | fc8, Q8, HTML chap.1, if7 |
| NEU CP : titre de créance court terme, intérêts précomptés | Chap.2 pptx slides 5-7 ; Applications 1-2 | fc32, Q42, if-neucp |
| NEU CP : calcul du rendement réel en cas de cession avant échéance | Chap.2 pptx slides 5, 7 ; Application 2 | fc33, if-neucp |
| Distinction intérêts précomptés / post-comptés | Chap.2 pptx slides 4-6 | fc32 |
| Valorisation d'une obligation = somme des flux actualisés | Chap.2 pptx slides 12-13 ; Ancien notes | fc11, Q13, HTML chap.3, if10 |
| Taux actuariel : taux qui égalise prix et flux actualisés ; > taux nominal si prime d'émission | Chap.2 pptx slide 9 ; Applications 3-8 | Q13, HTML chap.3, if10 |
| Relation inverse prix / taux d'une obligation | Chap.2 pptx slide 12 ; Ancien notes | Q10, HTML chap.3 |
| Coupon couru, cours pied de coupon vs plein coupon | Chap.2 pptx slide 13 ; Madeline ; Applications | fc12, Q12, HTML chap.3, if12 |
| Duration : durée de détention pour immuniser le portefeuille | Chap.2 pptx slide 14 ; Ancien notes | Q11, HTML chap.3, if11 |
| 3 modes de remboursement : in fine, annuités constantes, amortissement constant | Chap.1 pptx slides 10-11 ; Application 7 | fc34, fc35, Q43, if-rembobli |
| Formule de l'annuité constante a = C×i/[1-(1+i)^-n] | Chap.1 pptx slide 10 | fc34, Q44, if-anncst |
| IPO : définition, objectifs (lever des fonds, sortie des actionnaires, notoriété) | Ancien notes ; Ancien Claude | fc9, HTML chap.2, if8 |
| IPO : avantages et inconvénients (coût 3 à 7 %, transparence, perte de contrôle, pression) | Ancien notes ; Ancien Claude ; UE5 dossier 5 | Q40, HTML chap.2, if27 |
| Procédures OPO, OPF, cotation directe | Ancien notes ; Ancien Claude ; Applications 10-11 | fc9, HTML chap.2 |
| Ordres de bourse : règle du prix puis règle de chronologie | Ancien notes ; Ancien Claude | fc10, Q9, HTML chap.2, if9 |
| LCH ClearNet : chambre de compensation, contrepartie unique | Chap.2 pptx ; Ancien notes | fc20, Q20, HTML chap.1, if16 |
| Dépôt de garantie et appel de marge | Chap.2 pptx slides 38-39 ; Ancien notes | Q25, HTML chap.1 |
| AMF : autorité de tutelle des marchés ; Euronext : entreprise de marché | Chap.2 pptx ; Ancien notes | HTML chap.1 |

## 2.2 À AJOUTER (présent dans les sources, ABSENT ou insuffisant dans la plateforme)

- **OPM (Offre à Prix Minimal)** : procédure d'introduction par enchères sur la base d'un prix minimum. Enseignée et illustrée par l'Application 11 (cas Xprix). **Totalement absente de la plateforme**, qui ne cite que OPO, OPF, cotation directe.
- **Placement garanti (diffusion directe)** : un établissement financier diffuse les titres auprès d'investisseurs restreints et doit les acheter s'il ne trouve pas preneur (Ancien notes ; Ancien Claude ; Application 10 Essai One). Procédure source, absente de la liste de la plateforme.
- **Détermination du prix d'équilibre lors d'une cotation** : construction du carnet d'ordres (demande par prix décroissant, offre par prix croissant), prix d'équilibre = volume d'échange maximum (Chap.2 pptx slides 18-19, exemple chiffré Blanca). Absent ; notion examinable.
- **Cotation en continu** : horaires des phases (pré-ouverture 7h15, ouverture 9h00, pré-clôture 17h30, clôture 17h35) (Chap.2 pptx slide 20). Absent.
- **Cotation au fixing** : fixing A (deux plages, matin et après-midi) vs fixing B (une seule séance l'après-midi) (Ancien notes). Absent.
- **Mentions obligatoires d'un ordre de bourse** : sens (achat/vente), codification du titre, nombre de titres, durée de validité, conditions de prix ; nécessité d'un compte chez un PSI (établissement de crédit ou société d'investissement) (Ancien notes ; Ancien Claude). Partiellement absent.
- **Durée de validité d'un ordre** : à la journée, durée fixée (10-15 jours), ou à révocation (Ancien notes). Absent.
- **Taux actuariel : méthode de calcul détaillée** par égalisation du prix d'émission et de la somme des flux ; formule du prix d'émission Pe = Vn×i×((1-(1+i)^-n)/i) + Pr×(1+i)^-n (Chap.2 pptx slide 9 ; Madeline ; Applications). La plateforme énonce le concept mais pas la méthode de résolution.
- **Les 3 déterminants du prix d'une obligation** : influence du taux d'intérêt, valeur du coupon (plus le coupon est faible, plus le titre est sensible aux variations de taux), durée de l'emprunt (Ancien notes ; Ancien Claude). Absent.
- **Effet coupon** : hausse des taux donc surenchérissement du replacement des coupons et baisse de la valeur intrinsèque, et inversement (Ancien notes). Absent.
- **Taux facial / nominal, prix d'émission, prix de remboursement, « au pair »** : vocabulaire de base de l'emprunt obligataire (Chap.1 pptx slide 8 ; Chap.2 pptx). À expliciter.
- **Circuit d'un ordre de bourse** illustré par l'infographie source. À reconstituer a minima en texte.
- **Couverture chiffrée des applications** : 11 applications de marchés (monétaire, obligataire, actions) restent inexploitées en exercices.

## 2.3 INTRUS (présent dans la plateforme, ABSENT des sources)

- **Placement privé (PP)** présenté comme procédure d'introduction (fc9, HTML chap.2). Aucune source ne mentionne le placement privé ; il se substitue à tort à l'OPM.
- **Catégories d'obligations** : Investment grade, High yield (junk), notations BBB-/Baa3, S&P, Moody's, obligations convertibles, green bonds, ICMA Green Bond Principles (HTML chap.3). Section entièrement externe.
- **Duration de Macaulay, duration modifiée = Duration/(1+r), sensibilité ΔP/P ≈ -Duration modifiée × Δr, « bps »** (HTML chap.3). La duration comme concept est sourcée, mais sa déclinaison « Macaulay / modifiée / sensibilité » et la formule d'approximation sont externes.
- **Green shoe (option de surallocation), 15 % de titres supplémentaires** (HTML chap.2). Hors corpus.
- **Étapes de l'IPO en jargon anglo-saxon** : due diligence, book runners, roadshow, book building (HTML chap.2). Les sources décrivent le processus en termes plus simples (rôle de l'AMF, choix des intermédiaires, communication).
- **Compartiments Euronext avec seuils chiffrés** : A > 1 Md€, B 150 M-1 Md€, C < 150 M€ (HTML chap.1, fc9). Les sources évoquent l'existence de compartiments et le « compartiment C » mais ne donnent pas ces seuils.
- **Acteurs et cadres externes** : EMIR, ESMA, SEC, CME, Eurex, Euroclear, « market makers », « novation » (HTML chap.1, fc8, fc20). Les sources ne citent qu'Euronext, l'AMF et LCH ClearNet.
- **Anglicisme** « yield to maturity » (HTML chap.3). Les sources disent taux actuariel brut.

---

# THÈME 3 - PRODUITS DÉRIVÉS

## 3.1 OK (présent dans les sources ET dans la plateforme)

| Notion | Source | Trace plateforme |
|---|---|---|
| FRA : contrat de gré à gré fixant un taux futur, règlement du seul différentiel | Chap.2 pptx slides 26-27 ; Ancien Claude ; Application 14 | fc13, fc14, Q14, HTML chap.5, if13 |
| FRA : acheteur = emprunteur (couverture hausse), vendeur = prêteur (couverture baisse) | Ancien Claude | fc13, HTML chap.5 |
| Formule du différentiel FRA actualisé : Di = (Tm-Tg)×C×n/36000 ÷ (1+Tm×n/36000) | REDESIGN ; cohérent Chap.2 pptx slide 26 | fc36, if-fra-formule |
| Forward/Forward : taux futur garanti avec mise en place effective du prêt | Chap.2 pptx slide 28 ; Ancien Claude ; UE5 dossier 1 ; Application 15 | fc14, fc21, fc37, Q29, HTML chap.5, if13 |
| Forward/Forward : triple opération de la banque (emprunt, placement, prêt) | Chap.2 pptx slide 28 ; UE5 corrigé Passflux | fc21, fc37, HTML chap.5, if-ff-formule |
| Formule du taux Forward/Forward | UE5 PDF dossier 1 ; REDESIGN | fc21, fc37, if21, if-ff-formule |
| Différence FRA / Forward Forward (différentiel hors-bilan vs prêt réel) | Ancien Claude ; REDESIGN | fc14, Q15, Q45 |
| CAP : taux plafond, protection de l'emprunteur, prime | Chap.2 pptx slide 29 ; Ancien Claude | fc15, Q16, HTML chap.5, if14 |
| FLOOR : taux plancher, protection du prêteur, prime | Chap.2 pptx slide 30 ; Ancien Claude | fc16, Q17, HTML chap.5, if14 |
| COLLAR : tunnel, combinaison CAP + FLOOR ; emprunteur (achat CAP + vente FLOOR), prêteur (inverse) | Chap.2 pptx slides 31-32 ; Ancien Claude ; UE5 dossier 2 | fc17, fc22, Q18, Q31, HTML chap.5, if14, if22 |
| Collar emprunteur : calcul du coût réel borné entre plancher et plafond | Chap.2 pptx slide 31 ; UE5 dossier 2 (Carrousel) | fc23, if22 |
| Option : droit non obligation d'acheter (call) ou vendre (put), prime | Chap.2 pptx slides 33-36 ; Ancien Claude | fc18, fc19, Q19, HTML chap.6, if15 |
| Option européenne (échéance) vs américaine (tout moment) | Ancien Claude ; REDESIGN | HTML chap.6 |
| Déterminants de la valeur d'une option : cours du sous-jacent, prix d'exercice, volatilité, durée de vie, niveau des taux | Chap.2 pptx slide 36 | HTML chap.6 |
| Valeur d'une option = valeur intrinsèque + valeur temps | Chap.2 pptx slide 35 | fc18, Q19, HTML chap.6 |
| Options de change : exportateur achète un put, importateur achète un call | UE5 dossier 3 ; Application 19 | fc24, Q32, Q33, if23 |
| Options de change : calcul de la prime et du résultat net | UE5 dossier 3 ; Application 19 | fc25, if23 |
| Swap de taux : échange de flux d'intérêts, conversion fixe/variable | Chap.2 pptx slides 23-25 ; Ancien Claude ; Applications 12-13 | fc28 (mention), Q22, HTML chap.5 |

## 3.2 À AJOUTER (présent dans les sources, ABSENT ou insuffisant dans la plateforme)

- **Tableau d'exposition au risque de taux** : position emprunteuse / prêteuse croisée avec hausse / baisse des taux et taux fixe / variable, avec le caractère favorable ou défavorable (Chap.2 pptx slide 22). Grille de raisonnement examinable, absente.
- **Les 3 familles d'instruments** (contrat d'échange, contrat à terme, contrat d'option) et **les 5 sous-jacents** (matières premières et marchandises, taux d'intérêt, devises, actions, indices boursiers) (Chap.2 pptx slide 3). Absent.
- **Tableau gré à gré vs marché organisé par instrument** : swap, forward/forward, FRA, cap, floor, collar côté gré à gré ; futures et options sur futures côté organisé (Chap.2 pptx slide 23). Absent.
- **Contrat à terme ferme** : définition (engagement ferme et définitif des deux parties de livrer/payer à l'échéance quelles que soient les conditions de marché) (Ancien Claude). À expliciter.
- **Swap : mécanisme détaillé** : calcul du différentiel de taux entre les deux entreprises, partage équitable, détermination du taux du swap (Chap.2 pptx slides 24-25, exemple chiffré ; Applications 12-13). La plateforme ne traite le swap que comme concept.
- **Basis swap** (échange de taux variables sur références différentes : EURIBOR, LIBOR, TME, TMO, TMB) et **coupon swap** (conversion fixe/variable) (Ancien Claude). Cités en source, absents de la plateforme. Caractéristiques d'un swap : durée 3 mois à 10 ans, montants 1 à 10 M€.
- **Marché organisé : exemple de contrat à terme (futures) sur indice CAC 40** : valeur nominale du contrat, dépôt de garantie, cours de compensation, appels de marge quotidiens, calcul du gain (Chap.2 pptx slides 38-39, deux exemples chiffrés). Mécanisme du futures absent en tant qu'instrument.
- **Stratégies de base d'options** (profil de gain de l'acheteur et du vendeur, prime, prix d'exercice) et **catégories d'options** (Chap.2 pptx slides 33-34). À expliciter.
- **Représentations graphiques** du FRA, du Forward/Forward, du CAP, du FLOOR, du COLLAR (zones d'exercice et de non-exercice) (Chap.2 pptx slides 26 à 32). Support visuel du cours à reconstituer a minima en description.
- **Limitation des variations de cours** : au-delà d'un certain seuil de variation, la cotation est stoppée (Ancien Claude). Absent.
- **Couverture chiffrée des applications** : 8 applications de dérivés (swaps, FRA, Forward/Forward, collar, options de taux et de change) inexploitées.

## 3.3 INTRUS (présent dans la plateforme, ABSENT des sources)

- **Notation FRA « 3×6 », « 3×9 »** (HTML chap.5). Convention de marché non employée dans les sources.
- **Jargon d'options anglo-saxon** : ITM / ATM / OTM (in / at / out of the money), « thêta négatif » (HTML chap.6). Les sources parlent de zone d'exercice et de non-exercice.
- **Formules Max(S-K,0) et Max(K-S,0)** données comme définitions formelles de la valeur intrinsèque (fc18, fc19, Q19, HTML chap.6). Les sources traitent la valeur intrinsèque qualitativement, sans cette écriture formelle.
- **Collar à prime nulle « zero-cost collar »** (HTML chap.5). L'idée d'un coût réduit par compensation des primes est sourcée, mais pas l'expression ni le cas de prime strictement nulle.
- Remarque : la correction chiffrée de la flashcard fc23 (collar emprunteur Carrousel) et celle de l'annale Forward/Forward Passflux ne figurent pas telles quelles dans les PDF (l'annexe de l'UE5 est vierge). Ce sont des corrigés produits par la plateforme. Ils sont cohérents avec la méthode du cours, mais doivent être présentés comme corrigés de la plateforme et non comme contenu de la source.

---

# THÈME 4 - ESG ET FINANCE DURABLE

## 4.1 OK (présent dans les sources ET dans la plateforme)

| Notion | Source | Trace plateforme |
|---|---|---|
| Critères ESG : Environnemental, Social, Gouvernance | Chap.7 pptx ; Ancien Claude | fc20 (esg), Q21, Q27, HTML chap.7, if17 |
| Théorie du Donut, Kate Raworth, économiste, 2010 | Chap.7 pptx slide 4 ; Ancien Claude | fc38, Q46, if-donut-7 |
| Donut : deux limites (plancher social, plafond planétaire) et espace entre les deux | Ancien Claude ; REDESIGN | fc38, if-donut-7 |
| Les 7 principes de la théorie du Donut | Chap.7 pptx slide 4 | fc38, Q46, if-donut-7 |
| Les 3 Scopes d'émissions de GES (GHG Protocol / Bilan Carbone) | Chap.7 pptx slides 6-10 ; Ancien Claude | fc39, Q47, if-scopes123 |
| Scope 1 directes, Scope 2 énergie achetée, Scope 3 chaîne de valeur amont/aval | Chap.7 pptx slides 8-10 | fc39, Q47, if-scopes123 |
| 23 sous-catégories d'émissions | Chap.7 pptx slide 7 | fc39 |
| Les 12 normes ESRS (ESRS 1, ESRS 2, E1-E5, S1-S4, G1) | Chap.7 pptx slides 11-12 ; CSRD checklist | fc40, Q48, if-12esrs |
| ESRS 1 : 4 piliers GOV, SBM, IRO, MT ; E1 charge de la preuve inversée | CSRD checklist xlsx | fc40 |
| CSRD, ESRS, NFRD : sigles | Chap.7 pptx slide 11 | fc40, HTML chap.7 |
| Directive Omnibus : simplification de CSRD, Taxonomie, CS3D | Directive Omnibus.docx | fc41, if-omnibus |
| Omnibus : report 2026 vers 2028, seuils relevés (1000 salariés / 50 M€ CA / 25 M€ bilan), -80 % d'entreprises | Directive Omnibus.docx | fc41, Q49, if-omnibus |
| Omnibus : maintien de la double matérialité, rapport Draghi, Green Asset Ratio, allègements CS3D et Taxonomie | Directive Omnibus.docx | fc41, if-omnibus |

## 4.2 À AJOUTER (présent dans les sources, ABSENT ou insuffisant dans la plateforme)

- **Chronologie de la RSE et du développement durable** (Chap.7 pptx slide 5) : 1953 Howard Bowen, 1970 Club de Rome, 1987 Rapport Brundtland, 1992 Conférence de Rio, 2000 Pacte Global de l'ONU, 2009/2010 lois Grenelle I et II, 2010 norme ISO 26000, 2014 puis 2017 directive NFRD, 2015 ODD de l'ONU, 2016 loi Sapin II, 2017 loi sur le devoir de vigilance, 2019 loi PACTE, 2021 puis 2024 CSRD. Suite de dates très examinable, totalement absente.
- **Définition du développement durable** (Brundtland) : répondre aux besoins actuels sans compromettre la capacité des générations futures à répondre aux leurs (Ancien Claude ; Chap.7). Absent.
- **Définition de la RSE** : intégration des enjeux sociaux et climatiques dans la politique de l'entreprise, respect de la législation et des parties prenantes (Ancien Claude). Absent.
- **Performance financière vs performance RSE : un faux débat** ; la RSE comme créatrice de valeur (croissance du chiffre d'affaires par l'attractivité client, optimisation des investissements durables) (Ancien Claude ; REDESIGN). Absent.
- **Le GIEC** alerte sur le lien entre activités financières et changement climatique ; **définition de l'économie verte** (concept multidimensionnel, société en harmonie avec la nature) (Ancien Claude). Absent.
- **Les lois Grenelle** imposent pour la première fois aux entreprises cotées la publication d'un rapport RSE avec les comptes annuels (REDESIGN). Absent.
- **Sigles DPEF (Déclaration de Performance Extra-Financière) et KPI** (Chap.7 pptx slide 11). Absent.
- **Les postes d'émission détaillés des Scopes 1, 2 et 3** (Bilan Carbone : sources fixes et mobiles de combustion, procédés, émissions fugitives, émissions issues des terres pour le Scope 1 ; électricité et énergie de réseau pour le Scope 2 ; les 16 postes du Scope 3) (Chap.7 pptx slides 8-10). La plateforme résume ; le détail des postes, examinable, peut être ajouté.
- **CS3D : définition** (devoir de vigilance et de prévention sur les impacts droits humains et environnement dans la chaîne de valeur, sanctions financières et responsabilité civile) ; **règlement Taxonomie : définition** (classification des activités durables pour orienter la finance durable) (Directive Omnibus.docx). À expliciter, en restant strictement sur le contenu du document source.
- **Détail des Disclosure Requirements (DR)** par ESRS et règles de phase-in (CSRD checklist xlsx, 82 DR) : matière disponible si un approfondissement CSRD est souhaité.

## 4.3 INTRUS (présent dans la plateforme, ABSENT des sources)

- **Règlement Taxonomie : « 6 objectifs » et critère DNSH (Do No Significant Harm)** (HTML chap.7). Le document Omnibus mentionne la Taxonomie mais ne liste pas les 6 objectifs ni le DNSH.
- **SFDR (Sustainable Finance Disclosure Regulation), classification des fonds en articles 6, 8, 9** (HTML chap.7). Aucune source.
- **Agences de notation extra-financière nommées** : MSCI ESG, Sustainalytics, ISS ESG, Moody's ESG (HTML chap.7). Aucune source.
- **Sustainability-linked bonds (SLB), coupon « step-up »** (HTML chap.7). Aucune source.
- **Green bonds, ICMA Green Bond Principles, EU Green Bond Standard** (HTML chap.7 et chap.3). Aucune source.
- **Section « Impact sur l'ingénierie financière »** : DCF avec scénarios climatiques, stress tests réglementaires, prime de risque ESG, shareholder activism, CMPC ajusté ESG (HTML chap.7). Entièrement externe.
- **Donut : « 9 limites planétaires de Rockström »** détaillées et **liste des 12 besoins du plancher social** (fc38). Les sources évoquent « les limites planétaires » et « les limites sociales » sans cette double liste détaillée.
- **« Scope 3 = 70 à 90 % des émissions »** (fc39, HTML). Ordre de grandeur non chiffré dans les sources.

---

# THÈME TRANSVERSAL - « ÉVALUATION D'ENTREPRISE »

- **Checklist if19 « Évaluation d'entreprise - méthodes DCF & comparables »** et le thème orphelin `evaluation_ma` (référencé par fc29 et Q39 mais absent de la liste des 4 thèmes). L'évaluation d'entreprise par DCF et multiples comparables, en tant que chapitre autonome, n'est traitée par aucune source. Les sources n'abordent l'actualisation des flux que comme application du CMPC à la VAN d'un projet. **Intrus** : à supprimer ou à requalifier strictement comme « le CMPC comme taux d'actualisation de la VAN ».
- Le sous-titre de la plateforme annonce « Évaluation » comme pilier ; il conviendrait de l'aligner sur le périmètre réel des sources.

---

# SYNTHÈSE GLOBALE

## Volume estimé

| Thème | Notions OK | À ajouter | Intrus à retirer ou requalifier |
|---|---|---|---|
| Coût du capital | 14 | 9 | 8 |
| Marchés financiers | 18 | 12 | 8 |
| Produits dérivés | 20 | 11 | 4 |
| ESG et finance durable | 14 | 11 | 8 |
| Évaluation (transversal) | 0 | 0 | 1 |

## Diagnostic principal

1. **Bonne ossature, mais cours rédigé contaminé par de la finance générale.** Les 4 thèmes et la majorité des flashcards correspondent bien aux supports. En revanche, le cours de `inge_fi.html` (7 chapitres) ajoute de nombreuses notions externes : catégories d'obligations et notations, effet de levier, théorie du trade-off, SFDR, agences ESG, green bonds, green shoe, EMIR/ESMA. Ces ajouts sont du hors-programme au regard des supports du professeur.

2. **Erreurs de méthode à corriger en priorité.** Le coût de la dette est présenté avec une formule (charges financières / dette) qui n'est pas celle du cours (OAT + spread, puis interpolation linéaire du TRI). La formule du NEU CP précompté de la flashcard fc32 (« Nominal × [1 - t×n/36000] ») diffère de celle des supports, qui actualisent par division (« Nominal / [1 + t×n/36000] »).

3. **Lacunes sur des notions examinables.** Manquent notamment : les 4 facteurs du béta, la distinction risque systémique / spécifique, l'interpolation linéaire du coût de la dette, l'OPM, la détermination du prix d'équilibre en cotation, le tableau d'exposition au risque de taux, le swap chiffré, l'exemple de futures CAC 40, la chronologie RSE (1953-2024).

4. **Référencement des sources peu fiable.** De nombreuses flashcards portent un champ `src` / `srcChap` erroné : la flashcard ESG des Scopes est étiquetée « Chap 5 Dérivés », la flashcard du coût de la dette « Chap 5 Dérivés », l'Omnibus « Chap 2 », le calcul du béta « Chap 7 ». À reprendre intégralement.

5. **Numérotation des chapitres divergente.** Le professeur structure son cours en Chapitre 1 (le Béta / coût du capital), Chapitre 2 (les Marchés de capitaux, qui englobe monétaire, obligataire, actions et dérivés) et Chapitre 7 (critères extra-financiers). La plateforme réorganise en 7 chapitres et invente une numérotation (chap. 3 Obligations, chap. 5 Dérivés, chap. 6 Options) sans correspondance avec les supports.

6. **Richesse non exploitée.** 26 applications corrigées (7 béta, 11 marchés, 8 dérivés), extraites de sujets DSCG 2009 à 2025, ne sont pas mobilisées comme exercices. C'est le gisement le plus précieux pour la révision et l'entraînement.

## Recommandations pour la Tâche 2

- Réécrire le cours en respectant la structure du professeur : Coût du capital, Marchés de capitaux (monétaire, obligataire, actions, dérivés), Critères extra-financiers. Un fichier thématique par grand bloc.
- Retirer ou isoler clairement tous les éléments « intrus » listés ci-dessus. Aucune notion ne sera conservée si elle n'est pas traçable à un support.
- Combler les lacunes de la colonne « à ajouter », en restant au plus près de la formulation des sources.
- Corriger les deux erreurs de méthode (coût de la dette, formule NEU CP précompté).
- Intégrer les 26 applications comme exercices corrigés, fidèles aux corrigés des PDF et des notes (Madeline pour le chapitre 1).
- Reprendre le référencement source de chaque élément.
- Signaler explicitement, là où c'est le cas, qu'une notion provient d'une prise de notes de second rang ou que les notes elles-mêmes la signalent comme incomplète.
