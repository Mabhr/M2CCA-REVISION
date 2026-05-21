"""Réécrit l'annale 2024-2025 d'inge_fi en transcrivant verbatim le sujet (UE 5 - Finance.pdf)
et le corrigé (Corrigé Ingénierie financière 2024-2025 M2 CCA.pdf).

Nouveau schéma :
    annales[].dossiers[] = { label, context, items[{ q, correction }] }
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JSON_PATH = ROOT / 'data' / 'inge_fi.json'

# ──────────────────────────────────────────────────────────────────────────
# Nouvelle annale (mot pour mot depuis les PDFs)
# ──────────────────────────────────────────────────────────────────────────
NEW_ANNALE = {
    "id": "if_2024_2025",
    "year": "2024-2025",
    "name": "Session 1 — Vendredi 13 juin 2025",
    "duration": "2h00",
    "format": "Écrit · Plan comptable autorisé · Calculatrice non programmable",
    "professor": "P. Robin",
    "subject": (
        "M2 Comptabilité Contrôle Audit — Formation apprentissage & Formation continue.\n"
        "UE5 – FINANCE.\n"
        "Date : Vendredi 13 juin 2025 — 9h00 à 11h00. Semestre 2, session 1. Durée : 2h00.\n"
        "Plan comptable autorisé, aucun autre document autorisé. "
        "Calculatrice non programmable autorisée.\n"
        "Trésorerie, ingénierie financière et marchés financiers — P. Robin — 2h00.\n\n"
        "Consigne (Annexe 2) : Toujours arrondir à 2 chiffres après la virgule au SUPÉRIEUR, "
        "exemple : 0,21034 = 0,22."
    ),
    "dossiers": [
        {
            "label": "Premier dossier — Contrat Forward/Forward (4 points)",
            "context": (
                "Fin 3e trimestre N, le trésorier de la société Passflux constate au regard de ses prévisions "
                "un déficit de trésorerie de 200 000 € pour toute l'année N+1. Craignant une remontée des taux "
                "futurs il contracte avec sa banque un contrat Forward/Forward sur la base des conditions suivantes :\n\n"
                "|                  | Placement | Emprunt |\n"
                "| Taux à 3 mois    |  0,50 %   |   1 %   |\n"
                "| Taux à 12-18 mois|  1,25 %   |   2 %   |\n\n"
                "Formule donnée :\n"
                "T F/F = [ (Temprunt × durée emprunt) − (Tplacement × durée placement) ] "
                "÷ [ Durée du prêt (ou garantie) × ( 1 + (Tplacement × durée placement) / 36000 ) ]"
            ),
            "items": [
                {
                    "q": "a) Expliquer (rédaction ou graphique) la succession des opérations menées par la banque dans le cadre de ce contrat.",
                    "correction": (
                        "Le 30/09/N la Banque accepte de prêter à la société Passflux la somme de 200 000 € pour une "
                        "durée de 1 an soit du 01/01/N+1 au 31/12/N+1.\n\n"
                        "Dans ces conditions la banque va réaliser une triple opération :\n"
                        "• Emprunter ce jour pour 15 mois la somme sur les marchés (du 01/10/N au 31/12/N+1)\n"
                        "• Placer cette même somme sur les marchés pendant 3 mois (du 01/10/N au 31/12/N)\n"
                        "• Récupérer la somme placée et la Prêter pendant 12 mois à la société Passflux (01/01/N+1 au 31/12/N+1)\n\n"
                        "Schéma :\n"
                        "    01/10/N ────────► 31/12/N ────────────────────► 31/12/N+1\n"
                        "    │── Placement par la banque sur les Marchés (0,50 %) ──│\n"
                        "                              │── Période de prêt à Passflux ──│\n"
                        "    │────── Emprunt sur les marchés par la banque (2 %) ──────│\n\n"
                        "(Explication : 2 points)"
                    ),
                },
                {
                    "q": "b) Quel est le taux garanti dans le cadre de ce contrat entre la société Passflux et sa banque.",
                    "correction": (
                        "Somme à emprunter le 01/10/N par la banque pour disposer de 200 000 € le 01/01/N+1 :\n"
                        "    X + (X × 0,005 × 92/360) = 200 000  →  X = 199 744,77 €   (0,5 point)\n\n"
                        "À la fin du contrat la banque devra rembourser :\n"
                        "    199 744,77 + (199 744,77 × 0,02 × 457/360) = 204 816,07 €   (1 point)\n\n"
                        "Le taux garanti est donc :\n"
                        "    200 000 + (200 000 × X × 365/360) = 204 816,07  →  X = 2,375 %   (0,5 point)\n\n"
                        "Ou selon la formule :\n"
                        "    T F/F = (0,02 × 457 − 0,005 × 92) / [ 365 × (1 + 0,005 × 92 / 360) ]\n"
                        "    T F/F = 2,375 %   (ou 2 points)"
                    ),
                },
            ],
        },
        {
            "label": "Deuxième dossier — Contrat Collar (4 points)",
            "context": (
                "L'entreprise Carrousel veut réaliser un Emprunt de 300 000 € sur 4 ans au taux Tam + 0,5 %.\n"
                "Pour se protéger contre une éventuelle évolution défavorable des taux le trésorier a décidé "
                "de se pencher sur un instrument lui permettant de se prémunir contre ce risque : le Collar.\n\n"
                "Annexe 1 — Évolution du Tam sur les périodes :\n"
                "|     | N    | N+1 | N+2  | N+3 |\n"
                "| Tam | 1,5% | 2 % | 2,5% | 3 % |"
            ),
            "items": [
                {
                    "q": "a) Quelle est la nature du risque contre lequel le trésorier cherche à se préserver ?",
                    "correction": "Le trésorier cherche à se prémunir contre une hausse du taux d'intérêts. (0,5)",
                },
                {
                    "q": (
                        "b) Dans ces conditions doit-il :\n"
                        "    – acheter un collar emprunteur ?\n"
                        "    – vendre un collar emprunteur ?\n"
                        "    – acheter un collar prêteur ?\n"
                        "    – vendre un collar prêteur ?"
                    ),
                    "correction": "Dans ces conditions il va acheter un collar emprunteur. (0,5)",
                },
                {
                    "q": (
                        "c) Son banquier lui propose le collar suivant :\n"
                        "    – achat d'un Cap 3 % contre Tam + 0,5 %, prime 0,40 %\n"
                        "    – vente d'un Floor 2 % contre Tam + 0,5 %, prime 0,20 %\n"
                        "Remplissez en annexe 1 le tableau selon les évolutions du Tam proposées."
                    ),
                    "correction": (
                        "Évolution du Tam :\n"
                        "|                                |   N    |  N+1   |  N+2  |   N+3   |\n"
                        "| Tam                            | 1,5 %  | 2 %    | 2,5 % | 3 %     |\n"
                        "| Tam + 0,5 %  (0,5)             | 2 %    | 2,5 %  | 3 %   | 3,5 %   |\n"
                        "| Prime versée sur le Cap  (0,5) | 0,4 %  | 0,4 %  | 0,4 % | 0,4 %   |\n"
                        "| Différentiel reçu sur le Cap (0,5) | 2%<3% = 0 | 2,5%<3% = 0 | 3%=3% = 0 | 3,5%>3% = −0,5 % |\n"
                        "| Prime reçue sur le Floor  (0,5)| −0,20 %| −0,20 %| −0,20 %| −0,20 % |\n"
                        "| Différentiel versé sur le Floor (0,5) | 2%=2% = 0 | 2,5%>2% = 0 | 3%>2% = 0 | 3,5%>2% = 0 |\n"
                        "| Coût réel de l'endettement (0,5) | 2,20 % | 2,70 % | 3,20 % | 3,20 % |\n\n"
                        "Vérification : différentiel prime 0,4 − 0,20 = 0,20 %.\n"
                        "Soit 2 + 0,20 % = 2,20 % et 3 % + 0,20 % = 3,20 %."
                    ),
                },
            ],
        },
        {
            "label": "Troisième dossier — Les Options (4 points)",
            "context": (
                "Un exportateur va recevoir dans 90 jours 3 000 000 yens sur la base d'un cours actuel de "
                "1 € = 161,964 JPY.\n"
                "Craignant une évolution défavorable du change il cherche à prendre position sur le marché des options."
            ),
            "items": [
                {
                    "q": "a) Quelle position doit-il prendre ?",
                    "correction": (
                        "Il doit acheter un Put qui lui procurera le droit, mais non l'obligation, "
                        "de vendre ses Yens à un prix fixé d'avance. (0,75)"
                    ),
                },
                {
                    "q": (
                        "Il décide donc de se couvrir sur le marché des options moyennant une prime de 2 % "
                        "et un prix d'exercice de 160,85 JPY.\n"
                        "b) Quel sera le montant de la prime versée pour se couvrir ?"
                    ),
                    "correction": "La prime s'élève à : (3 000 000 / 160,85) × 0,02 = 373,02 €. (0,75)",
                },
                {
                    "q": (
                        "c) Quel sera le montant net obtenu par notre exportateur 90 jours plus tard "
                        "si le cours du yen est de 1 € = 159,25 JPY et 1 € = 162,50 JPY ?"
                    ),
                    "correction": (
                        "Hypothèse de 1 € = 159,25 JPY :\n"
                        "Dans ce cas le change s'élève à 3 000 000 / 159,25 = 18 838,30 € sur le marché comptant "
                        "alors que l'option lui permet d'obtenir 3 000 000 / 160,85 = 18 650,92 €.\n"
                        "Dans ces conditions le montant sur le marché comptant est supérieur à ce que garantit l'option "
                        "d'où abandon de celle-ci et vente sur le marché comptant.\n"
                        "Le résultat net est de : 18 838,30 − 373,02 = 18 465,28 €. (1,25)\n\n"
                        "Hypothèse de 1 € = 162,50 JPY :\n"
                        "Dans ce cas le change s'élève à 3 000 000 / 162,50 = 18 461,54 € ce qui est inférieur à ce que "
                        "garantit l'option (18 650,92 €).\n"
                        "Dans ces conditions on lève l'option pour un résultat net de : "
                        "18 650,92 − 373,02 = 18 277,90 €. (1,25)\n\n"
                        "(Attention si on ne levait pas l'option on obtiendrait un résultat net de "
                        "18 461,54 − 373,02 = 18 088,52 € ce qui est moindre !!)"
                    ),
                },
            ],
        },
        {
            "label": "Quatrième Dossier — Le Béta (4 points)",
            "context": (
                "Vous disposez des rentabilités moyennes du Titre Choups et de celles du CAC pour 5 périodes :\n\n"
                "| Périodes | Rentabilité moyenne du titre Choups en % | Rentabilité moyenne du CAC en % |\n"
                "|    1     |              1,05 %                       |             1,70 %               |\n"
                "|    2     |              0,95 %                       |             0,55 %               |\n"
                "|    3     |             −0,65 %                       |            −1,05 %               |\n"
                "|    4     |              0,30 %                       |             0,40 %               |\n"
                "|    5     |              1,95 %                       |             2,30 %               |"
            ),
            "items": [
                {
                    "q": "a) Déterminer le Bêta de Choups selon la formule β = COV (RCAC ; RAC) / V(RCAC). Annexe 2.",
                    "correction": (
                        "| Périodes | R Choups | R CAC  | RC − RMC | RCAC − RMCAC | (RCAC − RMCAC)² | (RC − RMC) × (RCAC − RMCAC) |\n"
                        "|    1     |  1,05 %  | 1,70 % |   0,33   |     0,92     |       0,85       |             0,31             |\n"
                        "|    2     |  0,95 %  | 0,55 % |   0,23   |    −0,55     |       0,31       |            −0,13             |\n"
                        "|    3     | −0,65 %  |−1,05 % |  −1,37   |    −1,83     |       3,35       |             2,51             |\n"
                        "|    4     |  0,30 %  | 0,40 % |  −0,42   |    −0,38     |       0,15       |             0,16             |\n"
                        "|    5     |  1,95 %  | 2,30 % |   1,23   |     1,52     |       2,31       |             1,87             |\n"
                        "| Moyennes |  0,72    | 0,78   |          |              |       6,97       |             4,98             |\n"
                        "(Tableau : 1 point)\n\n"
                        "Béta : (1/4 × 4,98) / (1/4 × 6,97) = 1,245 / 1,743 = 0,72. (1 point)"
                    ),
                },
                {
                    "q": (
                        "b) En supposant un Béta de 0,8, déterminer le coût des fonds propres de Choups sur la base "
                        "d'un taux sans risque de 1,15 % et d'une prime de risque du marché de 2 %."
                    ),
                    "correction": "Coût des fonds propres : Rcp = 1,15 % + (0,80 × 2 %) = 2,75 %. (0,5 point)",
                },
                {
                    "q": (
                        "c) Calculer le coût du capital sur la base d'un coût des capitaux propres de Choups de 3 %, "
                        "un taux d'endettement net d'IS de 2 %, la valeur de marché des capitaux propres de 4 800 000 € "
                        "représente 40 % de la valeur globale."
                    ),
                    "correction": (
                        "VGE = 4 800 000 / 0,40 = 12 000 000.\n"
                        "VD = VGE − VCP = 12 000 000 − 4 800 000 = 7 200 000. (0,5 point)\n\n"
                        "CMPC = (3 % × 4 800 / 12 000) + (2 % × 7 200 / 12 000) = 1,2 % + 1,2 % = 2,40 %. (1 point)"
                    ),
                },
            ],
        },
        {
            "label": "Cinquième dossier — L'introduction en bourse (4 points)",
            "context": "",
            "items": [
                {
                    "q": (
                        "Dans un développement structuré vous rappellerez les enjeux en termes d'avantages "
                        "et d'inconvénients d'une introduction en bourse pour une entreprise."
                    ),
                    "correction": (
                        "Barème : Introduction/conclusion = 1 point. Développement : Avantages : 3 propositions = 3 × 0,5 = 1,5 point. "
                        "Inconvénients : 3 propositions = 3 × 0,5 = 1,5 point.\n\n"
                        "─── AVANTAGES ───\n\n"
                        "1. L'accès au marché : la bourse offre une source de financement alternative pour déployer sa stratégie, "
                        "réaliser des opérations de croissance externe, procéder à des investissements. C'est souvent la première des motivations.\n\n"
                        "2. Un facteur de notoriété : Elle met un coup de projecteur sur des compétences, des équipes, des savoir-faire. "
                        "L'introduction en bourse a été pour nous une étape qui nous a permis de mieux nous faire connaître auprès d'un plus large public.\n\n"
                        "3. Une plus grande transparence : la bourse contraint les entreprises à plus de clarté dans la stratégie, "
                        "les publications périodiques des résultats, les échanges avec la communauté financière… J'ai la conviction que cet exercice "
                        "peut constituer un vecteur de croissance.\n\n"
                        "4. L'introduction en bourse permet d'apporter les fonds nécessaires à la croissance : au-delà d'un certain besoin "
                        "de financement, le recours aux investisseurs de type business angels ou fonds d'investissement ne suffit plus.\n\n"
                        "5. Fluidifier le marché : cela permet également aux investisseurs de départ, business angels, fonds d'investissement, "
                        "entrepreneurs, collaborateurs rémunérés par des actions… de réaliser une plus-value en revendant tout ou partie de leurs parts.\n\n"
                        "6. Gagner en crédibilité sur son marché : entrer en bourse, c'est pour beaucoup d'entrepreneurs une forme de consécration, "
                        "c'est acquérir une crédibilité supérieure : devenir une société cotée, c'est faire partie de l'aristocratie des start-ups.\n\n"
                        "7. Lever des fonds plus rapidement qu'auprès des acteurs du capital-investissement : une entrée en bourse permet pour une société "
                        "de lever de l'argent. Il est probable que la création du PEA-PME créera une demande à Paris et qu'une telle levée de fonds soit "
                        "dans certains cas plus facile (ou moins dilutive) qu'une levée réalisée auprès des fonds de capital investissement.\n\n"
                        "─── INCONVÉNIENTS ───\n\n"
                        "1. La complexité : l'introduction en bourse est un processus complexe, coûteux et risqué : il faut généralement faire appel "
                        "à une banque spécialisée, qui achète les titres avant de les revendre au marché. Or, ces intermédiaires réclament une rémunération "
                        "conséquente, et de temps à autre — comme cela a été le cas pour Facebook — ils se trompent dans leur estimation de cours d'introduction, "
                        "ce qui nuit à l'image de l'entreprise.\n\n"
                        "2. Une exposition qui requiert une très grande discipline : être une société cotée entraîne une série d'obligations d'information "
                        "auprès du marché boursier : il faut détailler précisément tous les éléments de l'activité dans des communications financières régulières, "
                        "ce qui impose une grande discipline de gestion et des systèmes d'information exhaustifs. Une société cotée est beaucoup plus exposée "
                        "et doit être beaucoup plus transparente.\n\n"
                        "3. Être soumis à « la loi du marché » : être coté, c'est aussi devoir se soumettre aux exigences des analystes, qui peuvent contraindre "
                        "l'entreprise à changer de stratégie lorsqu'ils estiment que cela leur sera plus profitable. Paradoxalement, alors que l'introduction "
                        "en bourse permet de lever des fonds supplémentaires, elle peut donc se traduire par une perte d'indépendance stratégique. "
                        "C'est pour regagner cette indépendance que Dell cherche actuellement à se retirer de la bourse.\n\n"
                        "4. Une plus grande vulnérabilité face aux OPA : être côté, c'est s'exposer au risque d'OPA. Pour éviter ce risque, "
                        "l'exigence de performance devient incontournable.\n\n"
                        "5. Une opération qui requiert beaucoup de temps et de ressources : il faut être conscient qu'une introduction en bourse "
                        "est un processus qui mobilise beaucoup d'énergie et prend du temps. L'équipe dirigeante est très sollicitée et il faut une "
                        "organisation particulièrement efficace pour gérer, en plus d'une activité en croissance, les relations avec les partenaires "
                        "qui vous accompagnent. Je me souviens par exemple avoir passé quelques nuits au bureau sur notre document de référence.\n\n"
                        "6. Une opération coûteuse : l'entrée en bourse a également un coût en termes de cotation, tenu de compte, honoraires de conseil, "
                        "recrutement le cas échéant. C'est un point qu'il ne faut surtout pas négliger au moment de se lancer dans l'aventure."
                    ),
                },
            ],
        },
    ],
    "tips": [
        "Le DOSSIER 5 (IPO) est une question rédactionnelle de 4 pts : intro/conclusion (1 pt) + 3 avantages développés (1,5 pt) + 3 inconvénients développés (1,5 pt). Ne pas faire l'impasse !",
        "TOUJOURS ARRONDIR À 2 DÉCIMALES AU SUPÉRIEUR (exemple 0,21034 → 0,22). Consigne explicite de l'énoncé.",
        "Pour le Forward/Forward : décomposer en 3 opérations (emprunt long, placement court, prêt à Passflux) avant de calculer.",
        "Pour le Collar emprunteur : achat Cap (plafond) + vente Floor (plancher) → on tunnelise le coût d'endettement.",
        "Pour les options : comparer systématiquement marché comptant vs exercice de l'option pour décider de lever ou abandonner.",
    ],
}


def main() -> None:
    d = json.loads(JSON_PATH.read_text())
    d['annales'] = [NEW_ANNALE]
    JSON_PATH.write_text(json.dumps(d, ensure_ascii=False, indent=2))
    print(f'✓ inge_fi.json mis à jour — annale 2024-2025 réécrite verbatim')
    print(f'  Dossiers : {len(NEW_ANNALE["dossiers"])}')
    print(f'  Sous-questions : {sum(len(ds["items"]) for ds in NEW_ANNALE["dossiers"])}')


if __name__ == '__main__':
    main()
