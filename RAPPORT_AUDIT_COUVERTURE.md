# Rapport d'audit de couverture - M2 CCA Systèmes d'information

Date : 2026-05-20
Sources auditées :
- `13_01_2026_support_Sécurité_SI_etudiants.pdf` (205 pages, N. Lebey)
- `Gouvernance_des_systèmes_d_information_05_02_2025.pdf` (70 pages, N. Lebey)
- `Audit des SI.pdf` (134 pages, N. Lebey)
- `UE 7 - Management des SI.pdf` (sujet d'examen 11/06/2025)
- `30012026_sujet_M2_2024_2025.pdf` (sujet d'examen 30/01/2026)
- `UE5-Sujet-2024.pdf` (sujet DSCG UE5 2024, cas AMDM)

Plateforme auditée : `data/gouv.json` (course unique « gouv » mélangeant les 3 thèmes), `gouv.html`.

Remarque liminaire : la plateforme actuelle ne distingue pas les trois thèmes demandés. Tout est regroupé dans un seul cours « Système d'information » dont la checklist mélange gouvernance, audit et sécurité. La refonte (Tâche 2) imposera donc une réorganisation en trois fichiers thématiques.

---

## 1. SÉCURITÉ DES SI

### 1.1 OK (présent dans PDF ET plateforme)

| Notion | Source PDF | Trace plateforme |
|---|---|---|
| Définition sécurité informatique | Sécurité p.20 | flashcard PSSI |
| PSSI - définition | Sécurité p.50 | g29, flashcard PSSI |
| Étapes PSSI (Audit, Élaboration des règles, Surveillance, Actions) | Sécurité p.56-60 | g29, flashcards |
| ISO 27001 / 27002 (133 mesures, SMSI) | Sécurité + Gouv | g6, g20, quiz |
| Équation du risque (Menace × Vulnérabilité × Impact) | Sécurité p.44 | flashcard sécurité |
| Notion d'audit de sécurité | Sécurité p.67 | g41 |
| BYOD - définition, risques employeur | Sécurité p.165 + UE5 | g22, quiz |
| Shadow IT / SI fantômes | UE5 sujet | g22, quiz |
| Sauvegardes / sécurité physique | Audit p.112-117 | g42, g43 |
| Plan de continuité d'activité (PCA) | Sécurité p.203 | flashcards |
| Plan de reprise d'activité (PRA) + RPO + RTO | Sécurité p.205 | flashcards |
| 5 objectifs sécurité (DICAN : Disp, Int, Conf, Auth, Non-rép) | Sécurité p.33 | partiel |

### 1.2 À AJOUTER (présent dans PDF, ABSENT de la plateforme)

Liste exhaustive des notions du PDF Sécurité qui n'apparaissent pas (ou de façon trop superficielle) dans `gouv.json` :

**Fondamentaux**
- Historique cryptographie (Cesar, Vernam, Enigma/Scherbius, Turing, DES, Diffie-Hellman 1976, RSA 1978)
- Critères DIC (Disponibilité, Intégrité, Confidentialité) + extension à la Preuve (Authentification + Non-répudiation)
- Distinction Sûreté de fonctionnement vs Sécurité
- Évolution des risques (Internet, attaques, failles tech/config/politique, profil pirates)
- État actif vs passif d'insécurité
- Principaux défauts de sécurité (les 10 défauts listés p.65)

**Référentiels et méthodes**
- Norme ISO 9000, 14001, 17799, 19001, 27001, 27002, 27004, 27005 (présentation détaillée)
- SMSI (Système de Management de la Sécurité de l'Information) - buts
- Méthodes : COBIT (côté sécurité), EBIOS (5 étapes : contexte, besoins, menaces, objectifs, exigences), MARION, MEHARI (PSS, POS, POE)
- ISMS et roue de Deming (PDCA appliqué à la sécurité)

**Cryptographie**
- Vocabulaire (crypter, décrypter, clair, chiffré)
- Stéganographie : watermarking, canal caché (cover channel), exemples
- Principe de Kerckhoff (1883)
- Chiffrement symétrique : avantages, limites (multiplication des clés, pas d'intégrité)
- Chiffrement asymétrique : clé publique/privée, propriétés, inconvénients (1000× plus lent, attaques force brute)
- Hashage : déterministe, irréversible, empreinte digitale, fonctions MD5/SHA1/SHA256
- Algorithme RSA (formule c = m^e mod n, m = c^d mod n, création paire de clés)

**Confiance numérique**
- 4 piliers de la confiance numérique
- Signature électronique : enjeux, propriétés (identification + intégrité), effets juridiques (Directive 1999, Code civil 2000)
- Certificat électronique : double rôle, 3 classes (I, II, III, 3Plus)
- Autorité de certification : clé racine, chaîne de confiance
- Archivage électronique : SAE, lois (13/03/2000 art.1316-1, L134-2, Code commerce/CGI)
- Normes archivage : NF Z42-013, modèle OAIS
- ICP / PKI : composants, services (VPN, courriers, déclarations fiscales, horodatage)

**Réseau et architecture technique**
- Clé WEP (faille vecteur d'initialisation)
- WPA / WPA2 (TKIP, PSK)
- Firewall / pare-feu (restrictions, blocage)
- Proxy, SAS applicatifs (FTP/Telnet)
- SSL/TLS, SSH : protections assurées / non assurées

**Blockchain**
- Définition, 3 composants (blocs, nœuds, mineurs)
- Fonction de hash et exemples
- Processus de validation (mining)
- Caractéristiques (chronologique, immuable, infalsifiable)
- Types : blockchain publique vs privée
- Atouts (traçabilité, sécurité, efficacité 24/24, coûts réduits)
- Limites (impact environnemental, stockage, adaptation, cadre réglementaire)
- Domaines d'application : logistique, santé, assurance, administratif
- Cas Bitcoin : origine 2008 Nakamoto, fonctionnement, limites (volatilité, 7 tx/s)
- Règlement européen MiCA (02/08/2024)

**Cadre juridique des SI**
- Responsabilité civile chef d'entreprise (art. 1384 C.civ.)
- Responsabilité pénale chef d'entreprise
- Loi Informatique et Libertés (6 janvier 1978, modifiée 6 août 2004)
- CNIL (rôle, missions)
- Droits des personnes : information, accès, rectification, opposition
- Article 34 loi 1978 - sécurité des données personnelles
- Articles 323-1 à 323-3-1 Code pénal - intrusion SI
- Reproductions non autorisées (logiciels piratés, charte utilisation)
- Secret des correspondances privées
- Identification de l'entreprise sur son site Internet (mentions obligatoires)
- Publicité électronique - consentement préalable
- Conclusion contrats en ligne (art. 1369-1, double clic, signature électronique)
- Loi 85-660 du 3/7/1985 (contrefaçons, droit d'auteur)
- Loi 88-19 du 5/1/1988 (fraude informatique)
- Loi 19/03/99 sur la cryptographie (clés < 40 bits libres, 40-128 bits déclaration, > 128 bits autorisation, SCSSI)

**Piratage et acteurs**
- Origine du mot hacker (MIT, IBM 704)
- Hacker, Hacktivisme, Cracker - distinctions
- Cas Kevin Mitnick
- Cas DDoS février 2000

**Menaces / typologie des attaques**
- Virus : furtif, polymorphe, macros (VBA), composite
- Vers (worms) - propagation réseau
- Spyware (logiciel espion)
- Hijackers (pirates de navigateur)
- Troyens / Cheval de Troie + Backdoor
- Bombe logique (ex. Tchernobyl 1999)
- Cryptolocker / Ransomware (2013)
- Hoax (canular) : viroax, chaînes solidarité, fausses infos, arnaques
- Spam / pourriel
- Mailbombing
- Phishing (mécanisme, protection)
- Denial of Service (DoS)
- Sniffing (reniflage) + détecteur de sniffer + switch vs hub
- Scanning + IDS / IPS
- Social Engineering
- Cracking de mots de passe : attaque par dictionnaire, hybride, brute-force (John the Ripper, L0phtCrack)
- Spoofing : usurpation IP, e-mail, web
- Man in the Middle
- Hijacking (détournement de session)
- Buffer overflow

**Continuité d'activité - détails**
- Obligations légales PCA : CRBF 2004-02 (Bâle II), Code commerce L.123-22 (10 ans), décret 24/03/2006 (journalisation hébergeurs)
- Politique de continuité d'activité (4 actions, 3 objectifs)
- Solutions PRA : hébergeur externe, Cloud (EC2…), sauvegardes en ligne, virtualisation, NAS/SAN/RAID, image disque (Clonezilla, Ghost), applications web (Google Docs, O365), télétravail

### 1.3 INTRUS (présent dans la plateforme, ABSENT des PDF)

À supprimer car non traçable à une source autorisée :

- « Règle 3-2-1 pour les sauvegardes » (quiz item) - n'apparaît dans aucun PDF
- « Coffre-fort numérique - 3 critères / caractéristiques techniques détaillées » - les PDF (UE 7, 30/01/2026) mentionnent l'outil mais ne détaillent pas ses critères techniques
- Détails fins sur le RGPD : DPO, registre, AIPD/PIA, analyse d'impact, seuils, sanctions précises - le RGPD n'est pas couvert par les PDF de cours ; seule la loi Informatique et Libertés 1978 + CNIL est dans le PDF Sécurité

---

## 2. GOUVERNANCE DES SI

### 2.1 OK (présent dans PDF ET plateforme)

| Notion | Source PDF | Trace plateforme |
|---|---|---|
| Définition SI (données + ressources matérielles/logicielles) | Sécurité p.7, Gouv p.7 | g1, flashcard |
| Définition gouvernance des SI | Gouv p.4-7 | g1 |
| « Gouverner c'est » : connaître/anticiper, décider, communiquer/suivre, adapter | Gouv p.9 | flashcard |
| Évolution historique des SI 1960-2000 (tableau Lebey) | Gouv p.6 | g2 |
| 5 fondements ISACA (alignement, valeur, risques, ressources, performance) | Gouv p.10-15 | g3, flashcards, quiz |
| Modèle Henderson-Venkatraman (4 formes d'alignement) | Gouv p.11 | g4 |
| Création de valeur par le SI | Gouv p.12 | g5 |
| Balanced Scorecard - 4 axes | Gouv p.15 | g7 |
| Gouvernance d'entreprise vs gouvernance SI | Gouv p.20-21, 38-39 | g8 |
| SOX (2002), NRE (2001), LSF (2003), loi Breton (2005) | Gouv p.38 + Audit p.53 | g20 |
| DSI - 3 pôles (production, support, développement) | Gouv p.41 | g9 |
| Rôle du DSI (technicien → manager) | Gouv p.40 | g10 |
| Sous-traitance, externalisation, infogérance | Gouv p.24-37 | g11 |
| Infogérance globale, sélective, parc, production | Gouv p.29-31 | g11 |
| TMA - 3 domaines (assistance, curative, évolutive) | Gouv p.32 | g12 |
| Convention de service, Help Desk (critères qualité) | Gouv p.33-34 | flashcard Help Desk |
| Réversibilité / Transférabilité | Gouv p.36 | g13 |
| Offshore / Nearshore / Onshore | Gouv p.37 | g13 |
| Mouroir / fin de vie (infogérance) | Gouv p.26 | flashcard |
| SLA / OLA - définition, intérêts, limites | Gouv p.56-59 | g13 |
| COBIT - définition, 4 domaines (PO, AI, DS, SE), 7 critères | Gouv p.45-50 | g14 |
| ITIL - processus Support et Production | Gouv p.54 | g15 |
| ISO 9000, 9001, 9004 + 8 principes qualité | Gouv p.68-69 | partiel |
| ISO 20000, 27000 | Gouv p.61-62 | g6 |
| CMMI - 5 niveaux (Initial, Discipliné, Ajusté, Géré quantitativement, Optimisation) + domaines de processus | Gouv p.64-67 | g16 |
| Val IT - création de valeur, cycle de vie projets | Gouv p.45 | g18 |
| Risk IT - 3 volets (Gouvernance, Évaluation, Réponse) + processus RG/RE/RR | Gouv p.45, 63 | g18 |
| COSO - origine, cadre | Gouv p.70, Audit p.65 | g17 |
| Orientations stratégiques SI - curseurs | Gouv p.23 | flashcard |
| Adéquation fondements/pratiques (10 pratiques) | Gouv p.43-44 | partiel |

### 2.2 À AJOUTER (présent dans PDF, ABSENT de la plateforme)

- Statistique d'introduction : 80 % des DSI ne mesurent pas l'impact IT (ACADYS) ; 1 projet sur 2 abandonné (Gouv p.3) - le « 1 sur 2 » est dans quiz mais pas la source ACADYS
- 70-80 % du budget IT consacré au fonctionnement (Gouv p.11) - présent en quiz mais pas en flashcard
- Étapes démarche alignement stratégique (5 étapes : communication, définir stratégie, alliances, visibilité, prioriser) - Gouv p.22
- Apports du modèle de gouvernance SI (enjeux, bénéfices) - Gouv p.17-18
- Les 7 questions auxquelles la gouvernance répond - Gouv p.17
- Décalque gouvernance SI / gouvernance d'entreprise : séparation propriétaires/gestionnaires + gestion des risques - Gouv p.39
- Activités de la DSI (4 activités) - Gouv p.41
- Relations DSI / métiers (5 dimensions) - Gouv p.42
- Référentiels listés par finalité : COBIT (gouv), ITIL (services), CMM (solutions), ISO 9001 (qualité), ISO 17799 (sécurité), PRINCE2 (projets) - Gouv p.46
- Cube COBIT (3 dimensions : processus, segmentation info, ressources) - Gouv p.50
- Détail des 7 critères d'information COBIT (Efficacité, Efficience, Confidentialité, Intégrité, Disponibilité, Conformité, Fiabilité) - Gouv p.49 - existe en quiz mais à enrichir
- Démarche PDCA appliquée à ISO 27002 (Plan, Do, Check, Act détaillés) - Gouv p.62
- Les 10 pratiques de gouvernance (IGSI) - Gouv p.53
- 8 principes de management de la qualité ISO 9000:2000 (orientation client, leadership, implication, processus, système, amélioration continue, factuelle, fournisseurs) - Gouv p.69
- BPO (Business Process Outsourcing), BTO (Business Transformation Outsourcing) - Gouv p.26
- ASP (Application Service Provider) - Gouv p.29
- GIE comme solution partenariale - Gouv p.24
- Outsourcing - définition Commission ministérielle terminologie - Gouv p.27
- Phases d'un service : Prise en charge, Récurrence/Production, Réversibilité - Gouv p.35-36
- Norme ISO 20000 (deux parties, processus listés) - Gouv p.61
- Différence SLS (Service Level Specification) vs SLO (Service Level Objectives) - Gouv p.56
- Citation Churchill (introductive p.16) - non essentielle

### 2.3 INTRUS (présent dans la plateforme, ABSENT des PDF)

- **« PDP et PPF — facturation électronique 2026 »** : Aucun des PDF ne mentionne « Plateforme de Dématérialisation Partenaire », « Portail Public de Facturation », « Factur-X », ni le calendrier précis 2026 ; seuls les sujets d'examen UE7/30-01 posent la question sans fournir le contenu de réponse
- **« Calendrier 2026 de la facturation électronique »** : idem
- **« Format Factur-X »** : aucun PDF
- **« IA Act européen »** : aucun PDF
- **« FEC (Fichier des Écritures Comptables) obligatoire depuis... »** : aucun PDF
- **« AIPD / PIA (Privacy Impact Assessment) »** : aucun PDF
- **« DPO obligatoire pour... »** : aucun PDF
- **« RGPD - sanctions, principes détaillés, registre »** : RGPD n'est pas dans les PDF (seule la loi 1978 et la CNIL le sont) ; à conserver uniquement à un niveau très général sans détails non sourcés
- **« Audit des systèmes d'IA - nouvelle mission de l'expert-comptable »** : non sourcé
- **« IA et profession comptable - opportunités/menaces détaillées »** : pose la question en exam mais le contenu de réponse n'est pas dans les PDF
- **« Cas AMDM - Top 10 des erreurs de gestion de projet »** : le cas AMDM existe (UE5-Sujet-2024) mais aucune liste « Top 10 » n'y figure ; à reformuler comme étude de cas exemplative et non comme contenu normatif
- **« MOE / MOA, comité de pilotage, contrat régie vs forfait »** : le cas AMDM mentionne MOE, COPIL, contrat en régie mais sans définition systématique ; à conserver uniquement comme vocabulaire issu du cas, sans extrapolation
- **« Indicateurs de PERFORMANCE vs QUALITÉ du SI - listes types »** : le sujet UE5 pose la question mais ne fournit pas la grille ; à supprimer ou signaler comme attente d'examen sans corpus
- **« Strates du SI - métier, applicative, infrastructure »** : la notion de « strate » est citée dans UE5 (Q1.1) mais sans définition ni typologie ; à conserver à minima, en signalant le caractère implicite

---

## 3. AUDIT DES SI

### 3.1 OK (présent dans PDF ET plateforme)

| Notion | Source PDF | Trace plateforme |
|---|---|---|
| Définition audit (ISO 9000) | Audit p.7 | g19 |
| Audit informatique vs audit des SI | Audit p.6-8 | g19, flashcard |
| Objectifs audit SI (efficacité, performance, pérennité, sécurité) | Audit p.4 | g19 |
| Quand un audit SI est utile (cas) | Audit p.5 | quiz |
| Guide d'audit gouvernance SI - 12 vecteurs | Audit p.10 | g21, flashcard détaillée |
| Audit fonction informatique - objectifs, COBIT PO4 | Audit p.38 | g37 |
| Audit de l'exploitation - outils (Openview, Tivoli, Nagios), COBIT DS | Audit p.39 | g38 |
| Audit projets info - modèles cascade/V/W/spirale | Audit p.40 | g39 |
| Audit applications opérationnelles | Audit p.41 | g40 |
| Audit sécurité informatique - 4 notions (menaces, vulnérabilité, manifestation, maîtrise) | Audit p.42 | g41 |
| Typologie missions audit (interne, externe, stratégique) | Audit p.43-44 | flashcard |
| Caractéristiques démarche (Progressive, Modulaire, Universelle, Opérationnelle) | Audit p.49 | flashcard |
| Rapport d'audit - exigences ISACA | Audit p.52 | flashcard |
| Cadre légal et normatif | Audit p.53 | g20 |
| Référentiel COBIT - usage, opportunités, limites | Audit p.55-57 | g14 |
| Normes ISA (315, 330) + ISCQ1 + AFAI/IFAC | Audit p.60-61 | partiel |
| Normes professionnelles CNCC : 2-301, 2-302 → NEP 315, NEP 330 | Audit p.62 | g45 |
| Contrôle interne (définition AFAI, 3 objectifs) | Audit p.63 | g17 |
| Cadre AMF 2010 | Audit p.65-66 | g46 |
| Référence COSO II, ISO 31000 | Audit p.66 | g46 |
| Démarches contrôle interne (7 démarches AFAI) | Audit p.67 | flashcard |
| Contrôle comptes entités informatisées (CAC, expert-comptable) | Audit p.68 | g48 |
| SIC - autonome, semi-intégré, intégré | Audit p.68 | g48 |
| Norme CNCC 2-302 - principes | Audit p.69 | g45 |
| Risques en environnement informatique (6 risques) | Audit p.70-71 | g47 |
| Risque d'audit ISACA - inhérent + contrôle + non-détection | Audit p.72-74 | flashcard |
| Cartographie des applications - travaux à réaliser | Audit p.125-127 | g36 |
| Appréciation complexité SI | Audit p.129-131 | g36 |
| Identification des processus à analyser | Audit p.132-134 | flashcard |
| Management des risques (démarche générale) | Audit p.98-102 | g44 |
| Stratégie d'audit (charte, responsabilités, ressources) | Audit p.99 | g44 |
| Évaluation des vulnérabilités, cartographie risque résiduel | Audit p.100 | g44 |
| Structures de gestion des risques (Niveau 1/2/3) | Audit p.104 | flashcard |
| Schéma directeur sécurité, TdB sécurité | Audit p.106-109 | g42 |
| Sécurité physique des sites | Audit p.112-116 | g43 |
| Présentation démarche : prise de connaissance, évaluation enjeux/fonctionnelle/technique/financière/projet/sécurité/support | Audit p.82-91 | g35 |

### 3.2 À AJOUTER (présent dans PDF, ABSENT de la plateforme)

- Le concept d'audit des SI date des années 1970 - existe partiel en quiz, à expliciter
- Les 4 notions sur l'audit informatique : faits, entretiens, évaluation, recommandations + lettre de mission - Audit p.9
- Liste des référentiels mobilisés par l'auditeur : COBIT, ISO 27002, CMMi, ITIL, Val IT, Risk IT - Audit p.9
- Loi Breton (26/07/2005) - mentionnée mais non détaillée
- 12 vecteurs détaillés : leurs intitulés exacts (stratégie, innovation, risques, données, architecture, portefeuille, projets, RH, prestataires, services, budget&perf, marketing&com) - présent
- 4 caractéristiques de la démarche - existe
- Règles d'audit des SI : jugement + recommandation, comparaison observation/référence, tâche définie, finalité non remise en cause, faisabilité - Audit p.47-48
- Normes d'audit interne IIA : normes qualification, fonctionnement, mise en œuvre + norme 1210.A3 - Audit p.58-59
- Audit interne vs audit externe - définitions précises AFAI - Audit p.44
- Lien CAC / expert spécialiste informatique - Audit p.71
- Exemples incidence sur risque inhérent / lié au contrôle (achats, interfaces) - Audit p.74
- Notion de processus - définition « enchaînement de tâches » et liste des processus types (achats, ventes, stocks, règlements, paie) - Audit p.132
- Tableau croisé Applications × Processus pour sélection d'audit - Audit p.134
- Définition Risque (Larousse + équation) + composantes méthode d'attaque / éléments menaçants / vulnérabilités - Audit p.95
- Évolution des enjeux et objectifs : développement durable, éthique, nouvelles technologies, certification - Audit p.103
- Risques liés au SI : fonction transversale, à hauts risques (techno, ouverture, inhérents) - Audit p.105
- Exemple contenu Schéma Directeur Sécurité - Audit p.107-108
- Points à examiner (sécurité, sauvegardes) - Audit p.110-111
- Système d'assurance : mesurer conformité, programme d'audit, pérenniser - Audit p.102

### 3.3 INTRUS (présent dans la plateforme, ABSENT des PDF)

- **« Démarche d'audit SI en 7 étapes »** : le PDF Audit liste plutôt 7 phases d'évaluation (prise de connaissance, enjeux, fonctionnelle, technique, financière, projet, sécurité, support = 8) ; vérifier que la numérotation « 7 étapes » utilisée dans la plateforme correspond bien à celles du PDF, sinon recaler
- **« Gestion de projet informatique - 5 phases canoniques »** : la plateforme propose une liste « cadrage → clôture » qui n'est pas dans les PDF tels quels ; les PDF mentionnent cascade/V/W/spirale et étapes générales (étude faisabilité, analyse fonctionnelle, tests) mais pas une liste normative à 5 phases
- **« MOE / MOA - définitions et responsabilités »** : seul UE5 utilise les acronymes sans les définir
- **« Cahier des charges - contenu et bonnes pratiques »** : non détaillé dans les PDF
- **« Comité de pilotage (COPIL) - composition et missions »** : COBIT mentionne un « comité de pilotage de l'informatique » (Audit p.38) sans en détailler la composition
- **« Contrat régie vs forfait »** : UE5 emploie le terme « contrat en régie » sans définition comparative
- **« Cas AMDM Top 10 erreurs »** : non sourcé
- **« Indicateurs PERFORMANCE vs QUALITÉ du SI »** : sujet posé par UE5 sans corpus de réponse

---

## 4. SYNTHÈSE GLOBALE

### 4.1 Volume estimé

| Thème | Notions OK | À ajouter | Intrus à supprimer |
|---|---|---|---|
| Sécurité | ~12 (partiel) | ~80 | ~3 |
| Gouvernance | ~30 | ~20 | ~12 |
| Audit | ~25 | ~20 | ~7 |

### 4.2 Diagnostic principal

1. **La plateforme actuelle est gravement sous-dimensionnée sur la Sécurité.** Le PDF de Sécurité fait 205 pages et couvre cryptographie, lois, menaces, méthodes (EBIOS, MEHARI), blockchain, MiCA, archivage, etc. La plateforme n'aborde qu'environ 10 % de ce contenu.

2. **La plateforme contient beaucoup de contenu non sourcé** lié à la facturation électronique 2026, au RGPD, à l'IA Act, qui répond aux questions d'examen UE7/30-01 mais en s'appuyant sur des connaissances externes. Ce contenu doit être retiré ou explicitement marqué « hors PDF ».

3. **La structure mono-cours « gouv » mélange les 3 thèmes.** La refonte (Tâche 2) imposera de produire 3 fichiers JSON/HTML séparés : `securite.html/json`, `gouvernance.html/json`, `audit.html/json`, en utilisant `gouv.html` comme template.

4. **Couverture acceptable** sur Audit (le PDF est en grande partie composé de slides visuelles sans texte exploitable ; le texte capturé représente l'essentiel du fond).

5. **Couverture bonne** sur Gouvernance, mais à enrichir sur quelques notions (10 pratiques IGSI, 8 principes ISO 9000, BPO/BTO/ASP, phases d'un service).

### 4.3 Recommandation pour la Tâche 2

Réorganiser en :
- `securite.html/json` - reconstruit quasi intégralement à partir du PDF Sécurité
- `gouvernance.html/json` - enrichissement du contenu existant + suppression intrus
- `audit.html/json` - extraction du contenu Audit actuellement mélangé + ajout des notions manquantes
- Conserver `gouv.html` comme page d'index ou redirection

Aucune notion ne sera ajoutée hors PDF. Les questions d'examen (UE7, 30-01, UE5) seront traitées comme exercices, avec une mention explicite quand la réponse complète n'est pas dans le corpus des PDF de cours.
