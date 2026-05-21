"""Nettoie rse : corrige l'erreur CS3D + supprime les extras non sourcés
+ ajoute le contenu manquant (4 piliers ESRS 1, 82 DR, chiffres Omnibus, etc.).
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JSON = ROOT / 'data' / 'rse.json'


def fix_existing(d):
    """Corrige les flashcards existantes qui ont des erreurs ou des extras non sourcés."""

    # fc[3] Green Deal : retire SFDR + CBAM (non sourcés)
    for fc in d['flashcards']:
        if 'Green Deal' in fc.get('q', '') and 'CSRD' in fc.get('a', ''):
            fc['a'] = (
                "Ensemble de politiques européennes visant à rendre l'Europe climatiquement neutre d'ici 2050.\n\n"
                "Objectifs :\n"
                "• -55 % d'émissions de CO₂ en 2030 par rapport à 1990 (objectif « Fit for 55»)\n"
                "• Neutralité carbone en 2050\n"
                "• Économie circulaire, biodiversité, alimentation durable\n\n"
                "Instruments majeurs :\n"
                "• CSRD (Corporate Sustainability Reporting Directive)\n"
                "• Taxonomie européenne des activités durables\n"
                "• CS3D (Corporate Sustainability Due Diligence Directive)"
            )
            break

    # fc[16] Taxonomie : simplifier en retirant les 3 ratios précis et DNSH OCDE non sourcés
    for fc in d['flashcards']:
        if "Taxonomie" in fc.get('q', '') and "activités durables" in fc.get('q', ''):
            fc['a'] = (
                "Système de classification européen permettant d'identifier les activités économiques "
                "considérées comme durables sur le plan environnemental.\n\n"
                "Objectif : flécher les financements vers les activités vertes en donnant un "
                "langage commun aux investisseurs.\n\n"
                "Concept clé : une activité est dite « alignée à la Taxonomie » si elle contribue "
                "substantiellement à un objectif environnemental et ne nuit pas significativement "
                "aux autres.\n\n"
                "Évolution Omnibus (2025) : réduction d'environ 70 % des obligations de reporting "
                "Taxonomie + introduction d'un seuil de matérialité financière + Green Asset Ratio "
                "pour les banques."
            )
            break

    # fc[28] CS3D : ERREUR FACTUELLE — sanctions 5% CA contredites par l'Omnibus
    for fc in d['flashcards']:
        if 'devoir de vigilance' in fc.get('q', '').lower() and 'CS3D' in fc.get('q', ''):
            fc['q'] = "Le devoir de vigilance — Directive CS3D et impacts Omnibus 2025"
            fc['a'] = (
                "DIRECTIVE CS3D (Corporate Sustainability Due Diligence Directive)\n"
                "• Adoptée par l'UE en mai 2024\n"
                "• Étend l'obligation de vigilance à toutes les grandes entreprises de l'UE\n"
                "• Calendrier d'application graduel à partir de 2027\n"
                "• Couvre : droits humains, libertés fondamentales, santé/sécurité, environnement\n"
                "• Articulation avec la CSRD (le rapport CSRD inclut le devoir de vigilance)\n\n"
                "MODIFICATIONS OMNIBUS (2025) — la CS3D est ALLÉGÉE :\n"
                "• Vigilance limitée aux PARTENAIRES DIRECTS de la chaîne de valeur (vs ensemble auparavant)\n"
                "• Évaluations tous les 5 ANS (vs annuel auparavant)\n"
                "• SUPPRESSION des sanctions financières proportionnelles au chiffre d'affaires mondial\n"
                "• Suppression de la responsabilité civile européenne harmonisée\n\n"
                "IMPLICATIONS PROFESSION : audit des plans de vigilance, accompagnement des entreprises."
            )
            break

    # fc[19] Omnibus : enrichir avec les chiffres précis
    for fc in d['flashcards']:
        if 'Omnibus' in fc.get('q', '') and 'évolution' in fc.get('q', '').lower():
            fc['a'] = (
                "Proposition législative européenne (février 2025) — paquet de simplification "
                "déclenché en réaction au rapport Draghi sur la compétitivité européenne.\n\n"
                "CSRD — modifications majeures :\n"
                "• Report de l'application : 2026 → 2028\n"
                "• Relèvement des seuils : 1 000 salariés / 50 M€ CA / 25 M€ bilan\n"
                "• → diminution d'environ 80 % du nombre d'entreprises soumises\n"
                "• Refonte (allègement) des 12 thématiques ESRS\n"
                "• Abandon des standards sectoriels (initialement prévus)\n"
                "• Fin de la collecte d'informations auprès des fournisseurs non soumis\n\n"
                "TAXONOMIE :\n"
                "• Réduction d'environ 70 % des obligations de reporting\n"
                "• Introduction d'un seuil de matérialité financière\n"
                "• Création du Green Asset Ratio (bancaire)\n\n"
                "CS3D :\n"
                "• Limitation aux partenaires directs\n"
                "• Évaluations tous les 5 ans\n"
                "• Suppression des sanctions proportionnelles au CA\n\n"
                "MAINTIEN : double matérialité conservée comme principe."
            )
            break


def remove_extras(d):
    """Supprime les flashcards/quiz extras non sourcés (SBTi, 15 catégories Scope 3, etc.)."""
    KILL_FLASHCARD_INDICES = [
        29,  # Calcul du Scope 3 (15 catégories, méthode monétaire/physique — non sourcé)
        30,  # Taxonomie alignement (3 ratios CapEx/OpEx — non sourcé)
        32,  # Greenwashing — Climat Résilience 2021, Green Claims 2024, ARPP — non sourcé
    ]
    d['flashcards'] = [fc for i, fc in enumerate(d['flashcards']) if i not in KILL_FLASHCARD_INDICES]

    # Quiz : retirer ceux qui parlent de SFDR uniquement, CBAM, SBTi
    new_quiz = []
    for q in d['quizQuestions']:
        text = (q.get('q', '') + q.get('e', '') + str(q.get('o', '')) + str(q.get('choices', ''))).lower()
        if 'sfdr' in text or 'cbam' in text or 'sbti' in text or 'green claims' in text:
            continue
        new_quiz.append(q)
    d['quizQuestions'] = new_quiz


def add_missing(d):
    """Ajoute les flashcards/quiz manquants : 4 piliers ESRS 1, 82 DR, charge preuve E1, phase-ins, etc."""
    new_fc = [
        {
            "q": "Structure de l'ESRS 1 — les 4 piliers (GOV / SBM / IRO / MT)",
            "a": (
                "L'ESRS 1 (Exigences générales) organise l'information de durabilité autour de "
                "4 piliers transversaux qui structurent tous les rapports CSRD :\n\n"
                "① GOV — GOUVERNANCE\n"
                "  Rôle des organes d'administration, contrôle interne, gestion des risques, "
                "intégration de la durabilité dans les rémunérations.\n\n"
                "② SBM — STRATÉGIE & BUSINESS MODEL\n"
                "  Modèle d'affaire, chaîne de valeur, intégration de la durabilité dans la "
                "stratégie, parties prenantes, IRO matériels identifiés.\n\n"
                "③ IRO — IMPACTS, RISQUES & OPPORTUNITÉS\n"
                "  Processus d'identification et d'évaluation des IRO ; double matérialité.\n\n"
                "④ MT — MESURES & CIBLES (Metrics & Targets)\n"
                "  Politiques, actions, objectifs chiffrés, indicateurs de suivi.\n\n"
                "Cette grille s'applique à TOUTES les ESRS thématiques (E, S, G) qui détaillent "
                "les disclosures requirements (DR) selon ces 4 piliers."
            ),
            "theme": "csrd_esrs"
        },
        {
            "q": "Les 82 Disclosure Requirements (DR) de la CSRD",
            "a": (
                "La CSRD impose 82 Disclosure Requirements répartis comme suit :\n\n"
                "ESRS 2 (transversal) — 12 DR :\n"
                "  • BP-1, BP-2 (Bases de préparation)\n"
                "  • GOV-1 à GOV-5 (Gouvernance)\n"
                "  • SBM-1 à SBM-3 (Stratégie & Business Model)\n"
                "  • IRO-1, IRO-2 (Impacts, Risques, Opportunités)\n\n"
                "ESRS Environnementaux — 32 DR :\n"
                "  • E1 — Changement climatique : 9 DR\n"
                "  • E2 — Pollution : 6 DR\n"
                "  • E3 — Eau et ressources marines : 5 DR\n"
                "  • E4 — Biodiversité et écosystèmes : 6 DR\n"
                "  • E5 — Économie circulaire : 6 DR\n\n"
                "ESRS Sociaux — 32 DR :\n"
                "  • S1 — Effectifs propres : 17 DR\n"
                "  • S2 — Travailleurs chaîne de valeur : 5 DR\n"
                "  • S3 — Communautés affectées : 5 DR\n"
                "  • S4 — Consommateurs et utilisateurs finaux : 5 DR\n\n"
                "ESRS Gouvernance — 6 DR :\n"
                "  • G1 — Conduite des affaires : 6 DR (corruption, lobbying, pratiques de paiement…)"
            ),
            "theme": "csrd_esrs"
        },
        {
            "q": "ESRS E1 — les 9 Disclosure Requirements clés",
            "a": (
                "E1 (Changement climatique) regroupe 9 DR :\n\n"
                "• E1-1 — Plan de transition climat\n"
                "• E1-2 — Politiques relatives au climat\n"
                "• E1-3 — Actions et ressources\n"
                "• E1-4 — Objectifs (climate targets)\n"
                "• E1-5 — Consommation d'énergie et mix énergétique\n"
                "• E1-6 — Émissions GES brutes (Scopes 1, 2, 3) et totaux\n"
                "• E1-7 — Absorptions GES et projets crédits carbone\n"
                "• E1-8 — Tarification interne du carbone\n"
                "• E1-9 — Effets financiers anticipés des risques physiques et de transition\n\n"
                "Spécificité E1 : CHARGE DE LA PREUVE INVERSÉE — si l'entreprise n'a PAS de plan "
                "de transition climat, elle doit expliquer pourquoi (par défaut on considère qu'elle "
                "devrait en avoir un, sauf justification)."
            ),
            "theme": "csrd_esrs"
        },
        {
            "q": "Dispositifs transitoires (phase-ins) de la CSRD",
            "a": (
                "La CSRD prévoit des phase-ins pour faciliter la mise en conformité :\n\n"
                "1ÈRE ANNÉE — omissions autorisées :\n"
                "  • Effets financiers anticipés des risques (E1-9, E2-6, E3-5, E4-6, E5-6)\n"
                "  • Plan de transition s'il n'est pas encore formalisé\n\n"
                "3 PREMIÈRES ANNÉES — omissions qualitatives :\n"
                "  • Indicateurs détaillés sur S1-15 (équilibre vie pro/perso), S2-3, S3-3, S4-3\n\n"
                "ENTREPRISES < 750 SALARIÉS — exemptions spécifiques :\n"
                "  • Pas d'obligation immédiate sur le Scope 3 et les GES totaux\n"
                "  • Pas d'obligation sur certains DR S et E\n\n"
                "Objectif : étalement dans le temps pour permettre la montée en compétence des "
                "entreprises et la collecte des données nécessaires."
            ),
            "theme": "csrd_esrs"
        },
        {
            "q": "Rapport Draghi (2024) — déclencheur de l'Omnibus",
            "a": (
                "Rapport « The future of European competitiveness » de Mario Draghi (septembre 2024).\n\n"
                "Constat central : l'Europe perd en compétitivité face aux États-Unis et à la Chine, "
                "notamment à cause d'une réglementation jugée trop lourde sur les entreprises.\n\n"
                "Conséquence directe : la Commission européenne lance le paquet OMNIBUS (février 2025) "
                "visant à simplifier le cadre réglementaire :\n"
                "• CSRD : report 2028, seuils relevés (1000 / 50 M€ / 25 M€), -80 % d'entreprises\n"
                "• Taxonomie : -70 % obligations\n"
                "• CS3D : limitation aux partenaires directs, allègement des sanctions\n\n"
                "C'est l'élément contextuel à mobiliser pour expliquer pourquoi le cadre RSE européen "
                "a été révisé en 2025."
            ),
            "theme": "csrd_esrs"
        },
        {
            "q": "Sommet de Johannesburg 2002 et les 3 piliers du développement durable",
            "a": (
                "Sommet mondial du Développement durable, Johannesburg, août-septembre 2002 (10 ans "
                "après Rio 1992).\n\n"
                "Confirme la définition du développement durable selon les 3 PILIERS / SPHÈRES :\n\n"
                "① SPHÈRE ÉCONOMIQUE — viabilité, performance financière, création de valeur durable\n"
                "② SPHÈRE SOCIALE — équité, conditions de travail, droits humains, parties prenantes\n"
                "③ SPHÈRE ENVIRONNEMENTALE — préservation des ressources, climat, biodiversité\n\n"
                "Le développement durable s'inscrit à l'intersection de ces 3 sphères. Toute "
                "démarche RSE devra équilibrer ces 3 dimensions, et non se concentrer sur l'une au "
                "détriment des autres."
            ),
            "theme": "fondamentaux"
        },
        {
            "q": "Global Compact / Pacte mondial des Nations Unies",
            "a": (
                "Initiative lancée par Kofi Annan en 2000 — engagement volontaire pour les "
                "entreprises et organisations à respecter 10 principes universels structurés en "
                "4 piliers :\n\n"
                "① DROITS DE L'HOMME (2 principes)\n"
                "  • Promouvoir et respecter les droits de l'homme\n"
                "  • Ne pas se rendre complice de violations\n\n"
                "② NORMES INTERNATIONALES DU TRAVAIL (4 principes)\n"
                "  • Liberté d'association et négociation collective\n"
                "  • Élimination du travail forcé\n"
                "  • Abolition du travail des enfants\n"
                "  • Élimination des discriminations\n\n"
                "③ ENVIRONNEMENT (3 principes)\n"
                "  • Précaution face aux problèmes environnementaux\n"
                "  • Initiatives plus de responsabilité environnementale\n"
                "  • Favoriser la mise au point de technologies respectueuses\n\n"
                "④ LUTTE CONTRE LA CORRUPTION (1 principe)\n"
                "  • Agir contre la corruption sous toutes ses formes\n\n"
                "Plus de 20 000 entreprises adhérentes dans le monde."
            ),
            "theme": "fondamentaux"
        },
        {
            "q": "Matrice de matérialité — analyse des enjeux RSE",
            "a": (
                "Outil graphique pour identifier et hiérarchiser les enjeux RSE pertinents pour "
                "une entreprise.\n\n"
                "STRUCTURE — 2 axes :\n"
                "• Axe horizontal : Importance de l'enjeu pour L'ENTREPRISE (impact sur la création "
                "de valeur, modèle économique, performance financière)\n"
                "• Axe vertical : Importance de l'enjeu pour les PARTIES PRENANTES (attentes des "
                "clients, salariés, ONG, investisseurs, autorités…)\n\n"
                "ZONES :\n"
                "• Quadrant supérieur droit (importance HAUTE sur les 2 axes) → ENJEUX MATÉRIELS "
                "à intégrer dans la stratégie et le reporting\n"
                "• Autres quadrants → enjeux secondaires à surveiller\n\n"
                "ÉVOLUTION CSRD : passage de la matérialité SIMPLE à la DOUBLE MATÉRIALITÉ :\n"
                "• Matérialité d'impact : impact de l'entreprise sur la société/environnement\n"
                "• Matérialité financière : impact de l'environnement sur la performance financière\n\n"
                "La matrice classique reste un outil de communication, mais la démarche d'identification "
                "des IRO (Impacts/Risques/Opportunités) est plus rigoureuse."
            ),
            "theme": "materialite"
        },
        {
            "q": "Le concept d'IRO (Impacts, Risques, Opportunités) — démarche CSRD",
            "a": (
                "L'IRO est la mécanique opératoire de la double matérialité dans les ESRS.\n\n"
                "DÉFINITIONS :\n"
                "• IMPACTS — effets de l'entreprise sur l'environnement et la société (positifs ou "
                "négatifs, réels ou potentiels)\n"
                "• RISQUES — événements ESG pouvant affecter négativement la performance financière "
                "ou la situation de l'entreprise\n"
                "• OPPORTUNITÉS — événements ESG pouvant créer de la valeur financière\n\n"
                "PROCESSUS EN 3 ÉTAPES (ESRS 1) :\n"
                "① Identification des IRO sur l'ENSEMBLE de la chaîne de valeur (amont + propre + "
                "aval)\n"
                "② Évaluation de leur matérialité selon des critères de gravité, probabilité, "
                "ampleur, irréversibilité, étendue\n"
                "③ Détermination de l'information à publier sur les IRO matériels\n\n"
                "Concept structurant à mobiliser dans toute analyse de double matérialité — "
                "« la trinité » de l'analyse CSRD."
            ),
            "theme": "materialite"
        },
    ]
    d['flashcards'].extend(new_fc)

    # Ajouter des quiz correspondants
    new_quiz = [
        {
            "q": "Combien de Disclosure Requirements (DR) compte la CSRD au total ?",
            "o": ["12 DR", "32 DR", "82 DR", "150 DR"],
            "c": 2,
            "e": "La CSRD impose 82 DR : 12 transversaux (ESRS 2) + 32 environnementaux (E1-E5) + 32 sociaux (S1-S4) + 6 gouvernance (G1).",
            "theme": "csrd_esrs"
        },
        {
            "q": "Quels sont les 4 piliers transversaux de l'ESRS 1 ?",
            "o": [
                "GOV / SBM / IRO / MT",
                "E / S / G / Climat",
                "Plan / Actions / Mesures / Reporting",
                "Investir / Mesurer / Reporter / Auditer"
            ],
            "c": 0,
            "e": "L'ESRS 1 organise l'information autour de 4 piliers : GOV (Gouvernance), SBM (Stratégie & Business Model), IRO (Impacts/Risques/Opportunités), MT (Metrics & Targets).",
            "theme": "csrd_esrs"
        },
        {
            "q": "Selon l'Omnibus 2025, à quel niveau les seuils CSRD sont-ils relevés ?",
            "o": [
                "500 salariés / 25 M€ CA",
                "750 salariés / 40 M€ CA",
                "1 000 salariés / 50 M€ CA / 25 M€ bilan",
                "5 000 salariés / 100 M€ CA"
            ],
            "c": 2,
            "e": "Omnibus relève les seuils à 1 000 salariés / 50 M€ CA / 25 M€ bilan, ce qui réduit d'environ 80 % le nombre d'entreprises concernées. Report d'application à 2028.",
            "theme": "csrd_esrs"
        },
        {
            "q": "Selon l'Omnibus 2025, qu'en est-il des sanctions financières CS3D proportionnelles au chiffre d'affaires ?",
            "o": [
                "Confirmées à 5 % du CA mondial",
                "Relevées à 10 % du CA mondial",
                "Supprimées par l'Omnibus",
                "Maintenues mais plafonnées à 1 M€"
            ],
            "c": 2,
            "e": "L'Omnibus 2025 SUPPRIME les sanctions financières proportionnelles au CA mondial initialement prévues dans la CS3D, dans une logique d'allègement réglementaire suite au rapport Draghi.",
            "theme": "csrd_esrs"
        },
        {
            "q": "Quel rapport européen a déclenché la proposition Omnibus de 2025 ?",
            "o": [
                "Rapport Letta (2024) sur le marché unique",
                "Rapport Draghi (2024) sur la compétitivité européenne",
                "Rapport Stern (2006) sur le climat",
                "Rapport Macron (2024) sur l'industrie"
            ],
            "c": 1,
            "e": "Le rapport Draghi de septembre 2024 sur la compétitivité européenne a alerté sur la perte de compétitivité face aux USA/Chine. La Commission a réagi en lançant le paquet Omnibus en février 2025 pour simplifier le cadre réglementaire (CSRD/Taxonomie/CS3D).",
            "theme": "csrd_esrs"
        },
        {
            "q": "Qu'est-ce que la « charge de la preuve inversée » dans l'ESRS E1 ?",
            "o": [
                "L'entreprise doit prouver qu'elle pollue moins que la moyenne",
                "L'entreprise n'ayant pas de plan de transition climat doit expliquer pourquoi",
                "Les CAC doivent prouver leur indépendance",
                "Les fournisseurs doivent prouver leur conformité ESG"
            ],
            "c": 1,
            "e": "Pour E1 (Changement climatique), la charge de la preuve est inversée : par défaut on considère que toute entreprise devrait avoir un plan de transition climat. Si elle n'en a pas, elle doit le justifier explicitement dans son rapport.",
            "theme": "csrd_esrs"
        },
        {
            "q": "L'IRO dans la démarche CSRD signifie :",
            "o": [
                "Indicateurs / Reporting / Objectifs",
                "Impacts / Risques / Opportunités",
                "Initiatives / Résultats / Outcomes",
                "Information / Reporting / Organisation"
            ],
            "c": 1,
            "e": "IRO = Impacts (effets de l'entreprise sur environnement/société) + Risques (événements ESG affectant la performance) + Opportunités (événements ESG créateurs de valeur). Mécanique opératoire de la double matérialité, à appliquer sur l'ENSEMBLE de la chaîne de valeur.",
            "theme": "materialite"
        },
    ]
    d['quizQuestions'].extend(new_quiz)

    # Ajouter quelques items checklist
    new_checklist = [
        {"id": "r-esrs1-4p", "label": "ESRS 1 — 4 piliers transversaux : GOV / SBM / IRO / MT"},
        {"id": "r-82dr", "label": "82 Disclosure Requirements (12 + 32E + 32S + 6G) — répartition"},
        {"id": "r-e1-9dr", "label": "ESRS E1 — 9 DR détaillés (E1-1 à E1-9)"},
        {"id": "r-e1-preuve", "label": "Charge de la preuve inversée pour E1 (climat)"},
        {"id": "r-phase-in", "label": "Phase-ins CSRD — 1ère année, 3 premières années, < 750 salariés"},
        {"id": "r-omnibus-chiffres", "label": "Chiffres Omnibus : 1000 salariés / 50 M€ / 25 M€ / -80 % entreprises / -70 % Taxonomie"},
        {"id": "r-draghi", "label": "Rapport Draghi (sept. 2024) déclencheur de l'Omnibus"},
        {"id": "r-cs3d-omnibus", "label": "CS3D allégée par Omnibus : partenaires directs, évaluations 5 ans, suppression sanctions % CA"},
        {"id": "r-johannesburg", "label": "Sommet Johannesburg 2002 + 3 piliers DD (économique/social/environnement)"},
        {"id": "r-global-compact", "label": "Global Compact (Kofi Annan 2000) — 10 principes / 4 piliers"},
        {"id": "r-matrice-mat", "label": "Matrice de matérialité (entreprise × parties prenantes) → simple vs double"},
        {"id": "r-iro", "label": "Concept IRO (Impacts / Risques / Opportunités) sur chaîne de valeur"},
    ]
    d['checklistItems'].extend(new_checklist)


def main():
    d = json.loads(JSON.read_text())
    before_fc = len(d['flashcards'])
    before_qz = len(d['quizQuestions'])
    before_cl = len(d['checklistItems'])

    fix_existing(d)
    remove_extras(d)
    add_missing(d)

    JSON.write_text(json.dumps(d, ensure_ascii=False, indent=2))
    print(f'✓ rse.json mis à jour :')
    print(f'   flashcards    : {before_fc} → {len(d["flashcards"])}')
    print(f'   quizQuestions : {before_qz} → {len(d["quizQuestions"])}')
    print(f'   checklistItems: {before_cl} → {len(d["checklistItems"])}')


if __name__ == '__main__':
    main()
