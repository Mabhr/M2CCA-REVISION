"""Nettoie inge_fi : supprime les extras restants (Greeks, Black-Scholes, duration modifiée)
+ ajoute le contenu Robin manquant (NEU CP, modes de remboursement obligataire,
Théorie du Donut détaillée, Scopes 1/2/3, Directive Omnibus 2025, 12 ESRS).
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JSON = ROOT / 'data' / 'inge_fi.json'
HTML = ROOT / 'inge_fi.html'


def remove_extras(d):
    """Supprime les flashcards/quiz extras (Greeks, Black-Scholes, duration modifiée)."""
    BAD_KEYWORDS = ['greeks', 'black-scholes', 'black scholes', 'duration modifiée',
                    'parité call-put', 'parite call-put', 'delta', 'gamma', 'theta', 'vega', 'rhô',
                    'protective put', 'covered call', 'straddle', 'bull spread']

    def is_bad(text):
        t = text.lower()
        return any(k in t for k in BAD_KEYWORDS)

    new_fc = [fc for fc in d['flashcards']
              if not is_bad(fc.get('q', '') + ' ' + fc.get('a', ''))]
    new_q = [q for q in d['quizQuestions']
             if not is_bad(q.get('q', '') + ' ' + q.get('e', '') + str(q.get('o', '')))]
    removed_fc = len(d['flashcards']) - len(new_fc)
    removed_q = len(d['quizQuestions']) - len(new_q)
    d['flashcards'] = new_fc
    d['quizQuestions'] = new_q
    return removed_fc, removed_q


def add_missing(d):
    """Ajoute les flashcards et quiz manquants depuis les sources Robin."""
    new_fc = [
        # ─── Marché monétaire / NEU CP ───
        {
            "q": "Le marché monétaire — NEU CP (Negotiable European Commercial Paper)",
            "a": (
                "Le NEU CP (anciennement billet de trésorerie) est un titre de créance négociable "
                "à court terme émis sur le marché monétaire par les entreprises pour se financer.\n\n"
                "Caractéristiques :\n"
                "• Maturité : 1 jour à 1 an\n"
                "• Marché : monétaire français (Banque de France)\n"
                "• Intérêts PRÉ-COMPTÉS : les intérêts sont retenus à l'émission\n"
                "  → l'émetteur reçoit le montant nominal − intérêts\n"
                "  → à l'échéance, il rembourse le nominal\n\n"
                "Formule des intérêts pré-comptés :\n"
                "  Montant reçu = Nominal × [ 1 − (t × n / 36 000) ]\n"
                "  où t = taux nominal (%), n = nombre de jours\n\n"
                "À COMPARER avec les intérêts POST-COMPTÉS (cas classique d'un placement bancaire) :\n"
                "  Montant final = Nominal × [ 1 + (t × n / 36 000) ]"
            ),
            "theme": "marches_fi"
        },
        {
            "q": "NEU CP — calcul du rendement en cas de cession avant échéance",
            "a": (
                "Si le détenteur d'un NEU CP souhaite céder son titre avant l'échéance, il doit "
                "trouver un repreneur et négocier un nouveau taux selon les conditions de marché.\n\n"
                "Méthode :\n"
                "① Calculer la valeur du NEU CP au moment de la cession en actualisant le nominal "
                "au nouveau taux de marché sur la durée restante :\n"
                "    Valeur cession = Nominal × [ 1 − (t_marché × n_reste / 36 000) ]\n"
                "② Comparer avec le montant initialement déboursé :\n"
                "    Rendement effectif = (Valeur cession − Montant initial) / Montant initial × (365 / n_détenu)\n\n"
                "Risque : si les taux ont monté, la valeur de cession baisse → moins-value possible.\n"
                "Exemple type DSCG : NEU CP Abys / ADP avec calcul du rendement à la sortie anticipée."
            ),
            "theme": "marches_fi"
        },

        # ─── Modes de remboursement obligataire ───
        {
            "q": "Les 3 modes de remboursement d'un emprunt obligataire",
            "a": (
                "Un emprunt obligataire peut être remboursé selon 3 modalités :\n\n"
                "① IN FINE (mode le plus courant)\n"
                "  • L'émetteur verse uniquement les coupons (intérêts) périodiques\n"
                "  • Le capital (nominal) est remboursé en totalité à l'échéance\n"
                "  • Avantage émetteur : trésorerie préservée pendant la durée\n\n"
                "② ANNUITÉS CONSTANTES\n"
                "  • Chaque annuité comporte une part d'intérêts et une part de capital\n"
                "  • Le total versé chaque année est constant\n"
                "  • La part de capital augmente, la part d'intérêts diminue\n"
                "  Formule de l'annuité constante :\n"
                "    a = C × i / [ 1 − (1 + i)⁻ⁿ ]\n"
                "  où C = capital emprunté, i = taux annuel, n = durée\n\n"
                "③ AMORTISSEMENT CONSTANT (séries égales)\n"
                "  • Chaque année, l'émetteur rembourse la même fraction de capital (C / n)\n"
                "  • Les intérêts diminuent (calculés sur le capital restant dû)\n"
                "  • Les annuités sont donc dégressives"
            ),
            "theme": "marches_fi"
        },
        {
            "q": "Comparaison des 3 modes de remboursement — impact sur l'émetteur et l'investisseur",
            "a": (
                "                          IN FINE       ANNUITÉS CST       AMORT. CST\n"
                "Annuité initiale            Coupon         a (constant)      Plus élevée\n"
                "Annuité finale              Coupon + K     a (constant)      Plus faible\n"
                "Trésorerie émetteur         Préservée      Régulière         Dégressive\n"
                "Risque de défaut final      Maximal        Modéré            Minimal\n"
                "Coût total intérêts         Maximal        Intermédiaire     Minimal\n\n"
                "Choix selon le profil :\n"
                "• Entreprise en croissance avec flux montants → IN FINE (paie au moment où elle pourra)\n"
                "• Entreprise stable cherchant régularité → ANNUITÉS CONSTANTES\n"
                "• Entreprise voulant minimiser le coût total et le risque de défaut → AMORTISSEMENT CONSTANT"
            ),
            "theme": "marches_fi"
        },

        # ─── Formules dérivés ───
        {
            "q": "Formule du différentiel FRA (Forward Rate Agreement) actualisé",
            "a": (
                "Le FRA permet de fixer aujourd'hui un taux futur. Seul le DIFFÉRENTIEL d'intérêts "
                "est échangé, et il est ACTUALISÉ pour être versé en DÉBUT de période.\n\n"
                "Formule du différentiel actualisé :\n"
                "  Di = [ (Tm − Tg) × C × n / 36 000 ]  ÷  [ 1 + (Tm × n / 36 000) ]\n\n"
                "où :\n"
                "  • Tm = taux de marché à l'échéance\n"
                "  • Tg = taux garanti par le contrat\n"
                "  • C = nominal du contrat\n"
                "  • n = durée de la période d'intérêt (jours)\n\n"
                "Logique :\n"
                "• Si Tm > Tg : l'emprunteur (acheteur de FRA) reçoit le différentiel (il aurait dû "
                "payer plus cher sans la couverture)\n"
                "• Si Tm < Tg : c'est l'emprunteur qui verse le différentiel\n\n"
                "Actualisation : le différentiel est calculé en fin de période mais versé en début "
                "de période, d'où la division par (1 + Tm × n / 36 000)."
            ),
            "theme": "derives"
        },
        {
            "q": "Formule du taux Forward/Forward",
            "a": (
                "Le contrat Forward/Forward (F/F) fixe AUJOURD'HUI un taux d'emprunt (ou de placement) "
                "FUTUR, avec mise en place EFFECTIVE du prêt (contrairement au FRA).\n\n"
                "La banque garantit le taux en réalisant 3 opérations :\n"
                "① Aujourd'hui : emprunte sur les marchés pour la durée totale (attente + garantie)\n"
                "② Aujourd'hui : place ce montant sur les marchés pendant la période d'attente\n"
                "③ Au démarrage : récupère le placement et prête à l'entreprise pour la durée garantie\n\n"
                "FORMULE du taux Forward/Forward :\n"
                "  T F/F = [ (T_emp × durée_emp) − (T_pl × durée_pl) ]\n"
                "          ÷  [ durée_prêt × ( 1 + (T_pl × durée_pl / 36 000) ) ]\n\n"
                "où :\n"
                "  • T_emp = taux d'emprunt sur la durée totale\n"
                "  • T_pl  = taux de placement sur la période d'attente\n"
                "  • durée_emp = durée totale (attente + garantie), en jours\n"
                "  • durée_pl  = période d'attente, en jours\n"
                "  • durée_prêt = durée du prêt garanti, en jours\n\n"
                "Différence FRA vs F/F :\n"
                "  • FRA : option / pas d'obligation d'emprunter\n"
                "  • Forward/Forward : engagement ferme — l'entreprise DOIT emprunter"
            ),
            "theme": "derives"
        },

        # ─── ESG : Donut détaillé ───
        {
            "q": "Théorie du Donut (Kate Raworth, 2010) — les 7 principes",
            "a": (
                "L'économiste britannique Kate Raworth a développé la Théorie du Donut pour penser "
                "une économie qui réponde aux besoins humains SANS dépasser les limites planétaires.\n\n"
                "Visuellement : un anneau (donut) entre 2 cercles :\n"
                "• CERCLE INTÉRIEUR (plancher social) — les besoins humains essentiels :\n"
                "  santé, éducation, eau, alimentation, énergie, revenu, logement, justice, "
                "égalité genres, expression politique, paix, accès aux réseaux\n"
                "• CERCLE EXTÉRIEUR (plafond environnemental) — les 9 limites planétaires de "
                "Rockström : changement climatique, biodiversité, cycle de l'azote, cycle du phosphore, "
                "acidification océans, pollution chimique, ozone, eau douce, occupation des sols\n\n"
                "LES 7 PRINCIPES DU DONUT :\n"
                "① Changer de but : remplacer le PIB par la prospérité humaine\n"
                "② Voir l'ensemble : économie intégrée à la société et à la nature\n"
                "③ Cultiver la nature humaine : revaloriser réciprocité et coopération\n"
                "④ Penser systémique : raisonner en boucles de rétroaction\n"
                "⑤ Distribuer dès la conception : équité intégrée au modèle\n"
                "⑥ Régénérer dès la conception : économie circulaire et restauratrice\n"
                "⑦ Être agnostique sur la croissance : ne pas en faire un objectif en soi"
            ),
            "theme": "esg"
        },

        # ─── Scopes GES détaillés ───
        {
            "q": "Les 3 Scopes d'émissions GES (GHG Protocol) — vue d'ensemble",
            "a": (
                "Le GHG Protocol structure les émissions de gaz à effet de serre en 3 catégories :\n\n"
                "SCOPE 1 — Émissions DIRECTES (sous contrôle opérationnel de l'entreprise)\n"
                "  • Combustion de carburants dans les sources fixes (chaudières) et mobiles (flotte)\n"
                "  • Émissions de procédés (réactions chimiques, par ex. ciment)\n"
                "  • Émissions fugitives (fuites de gaz frigorigènes, méthane)\n"
                "  • Émissions biogéniques liées aux terres et changements d'affectation\n\n"
                "SCOPE 2 — Émissions INDIRECTES liées à l'énergie achetée\n"
                "  • Émissions de la production d'électricité consommée\n"
                "  • Émissions liées aux réseaux de chaleur/froid (vapeur, eau chaude)\n\n"
                "SCOPE 3 — Émissions INDIRECTES AUTRES (chaîne de valeur)\n"
                "  • En amont : achats biens & services, immobilisations, déchets, transport amont, "
                "    déplacements professionnels, leasing amont\n"
                "  • En aval : transport aval, distribution, utilisation des produits vendus, "
                "    fin de vie des produits, leasing aval, franchises, investissements\n\n"
                "Le Bilan Carbone® distingue ~23 sous-postes au total. Le Scope 3 représente "
                "souvent 70-90 % des émissions totales."
            ),
            "theme": "esg"
        },

        # ─── Liste exhaustive des 12 ESRS ───
        {
            "q": "Les 12 normes ESRS — liste exhaustive",
            "a": (
                "Les European Sustainability Reporting Standards (ESRS) sont organisées en 12 normes :\n\n"
                "TRANSVERSALES (2) :\n"
                "• ESRS 1 — Exigences générales (4 piliers : GOV / SBM / IRO / MT)\n"
                "• ESRS 2 — Disclosures généraux (BP, GOV, SBM, IRO)\n\n"
                "ENVIRONNEMENTALES — E (5) :\n"
                "• E1 — Changement climatique (atténuation + adaptation + énergie)\n"
                "• E2 — Pollution (air, eau, sols, substances préoccupantes)\n"
                "• E3 — Eau et ressources marines\n"
                "• E4 — Biodiversité et écosystèmes\n"
                "• E5 — Économie circulaire (ressources, déchets)\n\n"
                "SOCIALES — S (4) :\n"
                "• S1 — Effectifs propres (employés)\n"
                "• S2 — Travailleurs de la chaîne de valeur\n"
                "• S3 — Communautés affectées\n"
                "• S4 — Consommateurs et utilisateurs finaux\n\n"
                "GOUVERNANCE — G (1) :\n"
                "• G1 — Conduite des affaires (anti-corruption, lobbying, paiements fournisseurs)\n\n"
                "Spécificité : E1 (climat) est QUASI-INCONTOURNABLE — charge de la preuve inversée."
            ),
            "theme": "esg"
        },

        # ─── Directive Omnibus ───
        {
            "q": "Directive Omnibus 2025 — simplification du cadre CSRD/Taxonomie/CS3D",
            "a": (
                "Proposition législative européenne de février 2025 — paquet de simplification "
                "déclenché par le rapport Draghi sur la compétitivité européenne (sept. 2024).\n\n"
                "OBJECTIF : alléger la charge réglementaire des entreprises tout en maintenant "
                "le cap de la transition écologique.\n\n"
                "CSRD — modifications :\n"
                "• Report d'application : 2026 → 2028\n"
                "• Relèvement des seuils : 1 000 salariés / 50 M€ CA / 25 M€ bilan\n"
                "  → réduction d'environ 80 % du nombre d'entreprises concernées\n"
                "• Refonte / allègement des 12 ESRS\n"
                "• Abandon des standards sectoriels\n"
                "• Fin de la collecte d'informations auprès des fournisseurs non soumis\n\n"
                "TAXONOMIE :\n"
                "• Réduction d'environ 70 % des obligations de reporting\n"
                "• Seuil de matérialité financière introduit\n"
                "• Création du Green Asset Ratio pour les banques\n\n"
                "CS3D (devoir de vigilance) :\n"
                "• Limitation aux partenaires DIRECTS de la chaîne de valeur\n"
                "• Évaluations tous les 5 ANS (vs annuel)\n"
                "• Suppression des sanctions financières proportionnelles au CA\n\n"
                "MAINTIEN : la double matérialité reste un principe fondamental."
            ),
            "theme": "esg"
        },
    ]
    d['flashcards'].extend(new_fc)

    # Quiz correspondants
    new_quiz = [
        {
            "q": "Le NEU CP (Negotiable European Commercial Paper) se caractérise par :",
            "o": [
                "Des intérêts post-comptés versés à l'échéance",
                "Des intérêts PRÉ-comptés retenus à l'émission",
                "Une maturité minimale de 5 ans",
                "Une cotation obligatoire sur Euronext"
            ],
            "c": 1,
            "e": "Le NEU CP est un titre de créance négociable à court terme (1 jour à 1 an) émis sur le marché monétaire. Particularité : intérêts PRÉ-comptés → l'émetteur reçoit le nominal − intérêts à l'émission, et rembourse le nominal à l'échéance.",
            "theme": "marches_fi"
        },
        {
            "q": "Quels sont les 3 modes de remboursement d'un emprunt obligataire ?",
            "o": [
                "Linéaire / Exponentiel / Logarithmique",
                "In fine / Annuités constantes / Amortissement constant",
                "Trimestriel / Semestriel / Annuel",
                "Public / Privé / Hybride"
            ],
            "c": 1,
            "e": "Les 3 modes : ① IN FINE (capital remboursé en bloc à l'échéance) ② ANNUITÉS CONSTANTES (annuité fixe, formule a = C × i / [1 − (1+i)⁻ⁿ]) ③ AMORTISSEMENT CONSTANT (mêmes parts de capital, annuités dégressives).",
            "theme": "marches_fi"
        },
        {
            "q": "Quelle est la formule de l'annuité constante d'un emprunt obligataire ?",
            "o": [
                "a = C × i × n",
                "a = C / n",
                "a = C × i / [ 1 − (1 + i)⁻ⁿ ]",
                "a = C × (1 + i)ⁿ"
            ],
            "c": 2,
            "e": "L'annuité constante (méthode des intérêts composés sur le capital restant dû) est donnée par a = C × i / [1 − (1+i)⁻ⁿ], où C = capital, i = taux annuel, n = durée. Chaque annuité contient une part d'intérêts (décroissante) et une part de capital (croissante).",
            "theme": "marches_fi"
        },
        {
            "q": "Quelle est la différence entre un FRA et un contrat Forward/Forward ?",
            "o": [
                "FRA pour les actions, Forward/Forward pour les obligations",
                "FRA = option, Forward/Forward = engagement ferme de mise en place du prêt",
                "FRA sur le marché organisé, Forward/Forward en OTC",
                "FRA sans intérêts, Forward/Forward avec intérêts"
            ],
            "c": 1,
            "e": "FRA : seul le différentiel d'intérêts (actualisé) est échangé — pas d'obligation de mettre en place le prêt. Forward/Forward : engagement ferme et définitif de l'emprunteur, qui DOIT effectivement emprunter au taux garanti.",
            "theme": "derives"
        },
        {
            "q": "Combien de principes structurent la Théorie du Donut de Kate Raworth ?",
            "o": ["3 principes", "5 principes", "7 principes", "10 principes"],
            "c": 2,
            "e": "Kate Raworth (2010) propose 7 principes : ① Changer de but (au-delà du PIB) ② Voir l'ensemble ③ Cultiver la nature humaine ④ Penser systémique ⑤ Distribuer dès la conception ⑥ Régénérer dès la conception ⑦ Être agnostique sur la croissance.",
            "theme": "esg"
        },
        {
            "q": "Selon le GHG Protocol, à quel Scope correspondent les émissions liées à l'électricité achetée ?",
            "o": ["Scope 1", "Scope 2", "Scope 3 amont", "Scope 3 aval"],
            "c": 1,
            "e": "Scope 1 = directes (combustion sous contrôle, procédés, fugitives). Scope 2 = indirectes liées à l'énergie achetée (électricité, chaleur/froid). Scope 3 = autres indirectes amont + aval (chaîne de valeur), souvent 70-90 % du total.",
            "theme": "esg"
        },
        {
            "q": "Combien de normes ESRS au total ?",
            "o": ["8 normes", "10 normes", "12 normes", "16 normes"],
            "c": 2,
            "e": "12 ESRS : 2 transversales (ESRS 1 Exigences générales, ESRS 2 Disclosures généraux) + 5 environnementales (E1-E5) + 4 sociales (S1-S4) + 1 gouvernance (G1).",
            "theme": "esg"
        },
        {
            "q": "Selon l'Omnibus 2025, à quel niveau les seuils CSRD sont-ils relevés ?",
            "o": [
                "250 salariés / 25 M€ CA",
                "500 salariés / 40 M€ CA",
                "1 000 salariés / 50 M€ CA / 25 M€ bilan",
                "5 000 salariés / 100 M€ CA"
            ],
            "c": 2,
            "e": "Omnibus relève les seuils à 1 000 salariés / 50 M€ CA / 25 M€ bilan → réduction d'environ 80 % du nombre d'entreprises soumises. Report d'application à 2028. Cette simplification a été déclenchée par le rapport Draghi sur la compétitivité européenne.",
            "theme": "esg"
        },
    ]
    d['quizQuestions'].extend(new_quiz)

    # Checklist
    new_cl = [
        {"id": "if-neucp", "label": "NEU CP — intérêts pré-comptés + cession avant échéance"},
        {"id": "if-rembobli", "label": "3 modes de remboursement obligataire (in fine / annuités constantes / amortissement constant)"},
        {"id": "if-anncst", "label": "Formule annuité constante : a = C × i / [ 1 − (1+i)⁻ⁿ ]"},
        {"id": "if-fra-formule", "label": "Formule FRA actualisée : Di = (Tm−Tg) × C × n / 36 000  ÷  (1 + Tm × n / 36 000)"},
        {"id": "if-ff-formule", "label": "Formule Forward/Forward développée (3 opérations bancaires)"},
        {"id": "if-donut-7", "label": "Théorie du Donut Raworth (2010) — 7 principes + 2 cercles (planète × social)"},
        {"id": "if-scopes123", "label": "Scopes 1/2/3 GES (GHG Protocol) — sources + amont/aval"},
        {"id": "if-12esrs", "label": "Liste exhaustive des 12 ESRS (ESRS 1/2 + E1-E5 + S1-S4 + G1)"},
        {"id": "if-omnibus", "label": "Directive Omnibus 2025 — CSRD/Taxonomie/CS3D allégées"},
    ]
    d['checklistItems'].extend(new_cl)


def main():
    d = json.loads(JSON.read_text())
    before_fc = len(d['flashcards'])
    before_q = len(d['quizQuestions'])
    before_cl = len(d['checklistItems'])

    removed_fc, removed_q = remove_extras(d)
    add_missing(d)

    JSON.write_text(json.dumps(d, ensure_ascii=False, indent=2))
    print(f'✓ inge_fi.json mis à jour :')
    print(f'   flashcards    : {before_fc} → {len(d["flashcards"])} ({-removed_fc} extras retirés, {len(d["flashcards"]) - before_fc + removed_fc} ajoutés)')
    print(f'   quizQuestions : {before_q} → {len(d["quizQuestions"])} ({-removed_q} extras retirés, {len(d["quizQuestions"]) - before_q + removed_q} ajoutés)')
    print(f'   checklistItems: {before_cl} → {len(d["checklistItems"])}')


if __name__ == '__main__':
    main()
