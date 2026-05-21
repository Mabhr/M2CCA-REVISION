"""Met à jour les annales 2024-2025 des 5 cours restants (evo_orga, strat, gouv,
conduite_chgt, rse) en transcrivant verbatim les sujets (Annales 2024/UE X.pdf) et
les meilleures copies (Annales 2024/Meilleure copie ....pdf).

Les annales plus anciennes (Étude de cas, Janvier 2026, 2023-2024, 2022-2023) sont
conservées telles quelles — pas de sources verbatim à disposition.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / 'data'


# ═══════════════════════════════════════════════════════════════════════════
# EVO_ORGA — 2024-2025 (Évolution des modèles d'organisation, F. BESOMBES, 1h)
# Sujet : UE 6 - Management stratégique_Evolution des modèles.pdf p.1
# Meilleure copie : note 17/20, n° 2112
# ═══════════════════════════════════════════════════════════════════════════
EVO_ORGA_2024 = {
    "id": "eo_2024_2025",
    "year": "2024-2025",
    "name": "Session 1 — Mercredi 11 juin 2025",
    "duration": "1h00",
    "format": "Écrit · Aucun document autorisé",
    "professor": "F. Besombes",
    "subject": "",
    "dossiers": [
        {
            "label": "Question (20 points)",
            "context": (
                "La contingence organisationnelle (ou structurelle) est une constante dans toutes "
                "les organisations. Alors que ces dernières, connaissent sous l'impulsion des "
                "mutations économiques, technologiques, sociales, des changements majeurs."
            ),
            "items": [
                {
                    "q": (
                        "Vous indiquerez comment les dirigeants peuvent améliorer la performance de "
                        "l'organisation en veillant à l'équilibre entre l'ambition stratégique et la "
                        "capacité organisationnelle de leur structure.\n\n"
                        "Préalablement vous présenterez les concepts mobilisés par le postulat ci-dessus."
                    ),
                    "correction": (
                        "[Meilleure copie — note 17/20]\n\n"
                        "Depuis longtemps, les théories classiques de management, comme celle de Taylor "
                        "ou de Fayol, ont affirmé qu'il existait un modèle unique de gestion dit "
                        "« one best way ». La théorie de la contingence a évolué dans un contexte où "
                        "l'efficacité d'une organisation dépend de son habilité à s'adapter à son "
                        "environnement.\n\n"
                        "En effet, la théorie de la contingence rejette l'idée qu'il existe un modèle "
                        "de gestion unique mais que ce modèle de gestion doit s'adapter à son "
                        "environnement, par des facteurs de contingence.\n\n"
                        "Plusieurs auteurs ont pu participer à cette réflexion et l'un des premiers à "
                        "poser la pierre à l'édifice est Woodward en 1958. Pour cet auteur, le type "
                        "de gestion d'une entreprise doit s'adapter à son mode de production. Il en "
                        "existe 3 :\n"
                        "  • production unitaire : la structure de l'entreprise peut être flexible, "
                        "décentralisée ;\n"
                        "  • production en masse : à l'inverse, la structure doit être rigide ;\n"
                        "  • production en continu : complexe et comme celle en masse, la structure "
                        "doit être rigide.\n\n"
                        "Ensuite, les auteurs Burns et Stalker en 1961 ont affirmé que la structure de "
                        "l'entreprise dépend de son environnement. Effectivement, si l'entreprise "
                        "évolue dans un environnement stable (mécanique) alors la structure sera "
                        "centralisée avec une hiérarchie forte, rigide où toutes les informations "
                        "nécessaires à la prise de décision sont envoyées au top management, le "
                        "dirigeant. Tandis qu'un environnement instable comme l'innovation va préférer "
                        "une structure organique (décentralisée) où cette fois-ci les ordres sont émis "
                        "par plusieurs personnes, adaptée à la réalité du terrain.\n\n"
                        "Lawrence et Lorsch ont théorisé en 1967 qu'il peut exister plusieurs types de "
                        "gestion en fonction du marché de l'entreprise, et donc en fonction du produit "
                        "vendu, il peut exister plusieurs gestions dans une seule et même entreprise.\n\n"
                        "Ensuite Fielder en 1967 classe deux types de leadership en fonction de la "
                        "nature, culture et taille de l'entreprise :\n"
                        "  • le leadership orienté tâche où seul l'objectif rentre en jeu ;\n"
                        "  • le leadership orienté relation où les parties prenantes comme les "
                        "salariés sont importantes pour une bonne gestion.\n\n"
                        "Enfin, l'un des derniers auteurs que l'on peut rajouter, c'est Mintzberg en "
                        "1973 qui vient valider la théorie où il existe plusieurs types de structure :\n"
                        "  • Structure simple : un seul gérant et c'est tout.\n"
                        "  • Structure fonctionnelle : plusieurs pôles de fonction (GRH, logistique, "
                        "production…) ;\n"
                        "  • Structure divisionnelle : divisée par produit, marché ;\n"
                        "  • Structure bureaucratique : forte hiérarchie ;\n"
                        "  • Structure adhocratique : flexible.\n\n"
                        "Pour illustrer nos propos, prenons l'exemple d'une startup comme "
                        "Blackmarket : cette entité repose sur une structure adhocratique car tout le "
                        "temps en évolution. À l'inverse, les entités stables comme la Poste ou EDF "
                        "ont plus une structure bureaucratique, où la forte hiérarchie se fait sentir. "
                        "Michelin ou Airbus auront plus une structure divisionnelle catégorisée par "
                        "type de production ou lieu géographique.\n\n"
                        "Tous ces auteurs convergent vers l'idée qu'il existe non pas un modèle "
                        "unique de gestion mais que cela dépend de son environnement.\n\n"
                        "Pour résumer, les facteurs de contingence sont nombreux mais les principaux "
                        "peuvent ressortir comme :\n"
                        "  • La technologie (production)\n"
                        "  • La taille de l'entreprise\n"
                        "  • La culture\n"
                        "  • L'environnement\n"
                        "  • L'histoire du groupe\n"
                        "  • La stratégie globale de l'entreprise\n\n"
                        "C'est sur ce dernier facteur que repose la question : « Comment les "
                        "dirigeants peuvent améliorer la performance de l'organisation en veillant à "
                        "l'équilibre entre l'ambition stratégique et la capacité organisationnelle ? »\n\n"
                        "Tout d'abord, la stratégie c'est l'ensemble des actions mises en œuvre ou à "
                        "mettre en œuvre pour atteindre un objectif MT ou LT en utilisant différentes "
                        "ressources comme les compétences qui peuvent donner un avantage concurrentiel.\n\n"
                        "Cependant, nous avons pu voir que l'organisation est étroitement liée avec la "
                        "stratégie de l'entreprise. Si les dirigeants veulent améliorer la performance "
                        "de l'organisation, ce n'est pas seulement la structure à faire évoluer mais "
                        "tous les autres facteurs de contingences. Pour évoluer avec les mutations "
                        "économiques, technologiques, sociales alors il faudrait tendre vers une "
                        "structure flexible, décentralisée, orientée relation, afin de prendre en "
                        "compte tous les différents aspects. Cela affecterait inévitablement la "
                        "performance de l'organisation car les parties prenantes plus impliquées dans "
                        "un projet de changement ont plus de chance d'aboutir.\n\n"
                        "Selon Forbes, 30 % des projets échouent si les entreprises impliquent les "
                        "parties prenantes comme les salariés contre 60 % si elles ne le font pas. Ce "
                        "qui pourrait augmenter la création de valeur pour l'entreprise (Résultat) "
                        "comme pour les clients (utilité du produit).\n\n"
                        "En conclusion, la théorie de la contingence vient bousculer les théories "
                        "classiques du management afin de prendre en compte l'environnement dans "
                        "lequel une entreprise évolue afin de faire face aux différentes mutations "
                        "actuelles."
                    ),
                }
            ],
        }
    ],
    "tips": [
        "Structure académique attendue : intro → théories classiques (Taylor, Fayol) → théorie de la contingence → auteurs clés (Woodward, Burns & Stalker, Lawrence & Lorsch, Mintzberg) → application → conclusion.",
        "Mobiliser au moins 4-5 auteurs avec leurs dates et apports précis (Woodward 1958, Burns & Stalker 1961, Lawrence & Lorsch 1967, Fielder 1967, Mintzberg 1973).",
        "Donner des exemples concrets d'entreprises pour chaque type de structure (startup → adhocratique, Poste/EDF → bureaucratique, Michelin/Airbus → divisionnelle).",
        "Lister les 6 principaux facteurs de contingence (technologie, taille, culture, environnement, histoire, stratégie).",
        "Conclure en montrant que la stratégie ne se limite pas à la structure : tous les facteurs doivent évoluer ensemble.",
    ],
}


# ═══════════════════════════════════════════════════════════════════════════
# STRAT — 2024-2025 (Management Stratégique, A. TELLIER, 1h)
# Sujet : UE 6 - Management stratégique_Evolution des modèles.pdf p.2-4
# Meilleure copie : note 17/20, n° 2607891 — Sujet n°1 traité (plateformes)
# ═══════════════════════════════════════════════════════════════════════════
STRAT_2024 = {
    "id": "strat_2024_2025",
    "year": "2024-2025",
    "name": "Session 1 — Mercredi 11 juin 2025",
    "duration": "1h00",
    "format": "Écrit · Aucun document autorisé · 2 sujets au choix",
    "professor": "A. Tellier",
    "subject": "VOUS TRAITEREZ AU CHOIX LE SUJET 1 OU LE SUJET 2.",
    "dossiers": [
        {
            "label": "Sujet n°1 — Question de cours (20 points)",
            "context": (
                "Vous êtes contacté par un ami qui veut créer une plateforme. Son idée est de "
                "lancer une application pour smartphone qui permettrait de mettre en relation des "
                "personnes âgées et des personnes prêtes à rendre des services de proximité. Grâce "
                "à cette application, la personne âgée aurait accès à un réseau d'entraide. Elle "
                "pourrait échanger et envoyer une alerte aux personnes de sa communauté virtuelle "
                "pour demander de l'aide ou des services (ménage, bricolage…) à d'autres "
                "« aidants ». À l'inverse, la personne pourrait se proposer d'être « aidant » pour "
                "d'autres qui ont besoin d'une aide.\n\n"
                "Votre ami souhaite des conseils sur la stratégie qu'il pourrait déployer.\n\n"
                "N.B. Aucune connaissance sur le projet de votre ami n'est nécessaire pour "
                "répondre à la question. Vous pouvez appuyer votre réflexion sur des exemples "
                "variés."
            ),
            "items": [
                {
                    "q": (
                        "Après avoir rappelé ce qu'est une plateforme, vous détaillerez les "
                        "mécanismes sur lesquels il est possible de s'appuyer pour réussir à "
                        "développer ce type de structure."
                    ),
                    "correction": (
                        "[Meilleure copie — note 17/20 — Sujet n°1 traité]\n\n"
                        "Les plateformes sont des dispositifs de coordination de ressources et "
                        "d'actions, contrôlés par un opérateur privé qui en est le chef d'orchestre. "
                        "Ces nouveaux modèles d'entreprise sont apparus ces vingt dernières années, "
                        "avec l'émergence des nouvelles technologies et plus particulièrement "
                        "d'internet, qui permet de connecter entre elles des individus qui ne se "
                        "connaissent pas. Pour être qualifié de plateforme, un dispositif doit avoir "
                        "deux caractéristiques :\n"
                        "  • Chaque groupe (offreur et demandeur) peut être client de la plateforme\n"
                        "  • Il permet une mise en relation directe entre les offreurs et les "
                        "demandeurs\n\n"
                        "Pour mener à bien un projet de développement de plateforme, l'opérateur de "
                        "la plateforme doit réussir à rendre la plateforme la plus attractive "
                        "possible, pour inciter les demandeurs à se connecter dessus, mettre en place "
                        "les conditions nécessaires pour que les offreurs produisent du contenu et "
                        "que les demandeurs puissent trouver une offre satisfaisante, et enfin "
                        "définir un business model, c'est-à-dire un ensemble de paramètres permettant "
                        "de créer, délivrer et capturer de la valeur, pour permettre de rendre le "
                        "projet de plateforme rentable.\n\n"
                        "Pour atteindre ces objectifs, l'opérateur de la plateforme doit s'appuyer "
                        "sur 6 mécanismes, décrits par Christophe Benavent en 2016.\n\n"
                        "─── 1er mécanisme : les externalités de réseau et de standard ───\n\n"
                        "La valeur d'une plateforme est surtout liée à son nombre d'usagers. En "
                        "effet, une plateforme ne comprenant que peu d'usagers, même si elle est "
                        "très utile, ne sera que très peu utilisée et aura du mal à se développer. "
                        "C'est sur le principe de la loi de Metcalfe que Benavent fait cette "
                        "analyse, considérant que la valeur de la plateforme augmente au carré pour "
                        "chaque nouvel utilisateur. Il s'agira donc, pour une plateforme, de réussir "
                        "à avoir le plus d'utilisateurs possible pour rendre la plateforme la plus "
                        "attractive possible.\n\n"
                        "Concernant les externalités de standard, celles-ci sont liées à un possible "
                        "changement de plateforme : en effet, il peut être « coûteux » pour un "
                        "utilisateur utilisant déjà une plateforme de changer pour une nouvelle. Le "
                        "fait d'être le premier sur un marché peut donc être déterminant pour garder "
                        "les utilisateurs.\n\n"
                        "─── 2e mécanisme : le crowdsourcing ───\n\n"
                        "Le crowdsourcing va consister à faire porter le capital productif et le "
                        "travail de production sur les usagers. En effet, le modèle de plateforme "
                        "permet à l'opérateur d'avoir des apports en capital assez faibles, puisque "
                        "ce sont les offreurs qui vont produire son offre. Pour garder cette "
                        "dynamique, il faut également inciter les demandeurs à faire des retours, via "
                        "notamment des systèmes de notation des offreurs, qui permettront aux autres "
                        "utilisateurs de pouvoir avoir plus de confiance dans les offreurs.\n\n"
                        "─── 3e mécanisme : les marchés de réputation ───\n\n"
                        "Le troisième mécanisme est en lien avec le système de notation, car les "
                        "plateformes sont des marchés de réputation. La plupart des utilisateurs ne "
                        "se connaissent pas, et donc la confiance entre les utilisateurs, souvent "
                        "nécessaire pour effectuer un acte d'achat, doit pouvoir être créée. "
                        "L'opérateur de la plateforme va donc devoir permettre de créer ces "
                        "conditions, notamment donc par un système de notation et de commentaires.\n\n"
                        "─── 4e mécanisme : la logique de la longue traîne (économie de la variété) ───\n\n"
                        "Le modèle des plateformes permet aujourd'hui de ne pas avoir de stocks et "
                        "donc de proposer une variété de produits beaucoup plus importante qu'un "
                        "opérateur traditionnel. Dans le cas du sujet, la plateforme va pouvoir "
                        "proposer une multitude de services, certainement plus que ce que pourrait "
                        "le faire par exemple une entreprise d'aide à domicile. Toutefois, la "
                        "multitude des offres impose également de mettre en place des dispositifs "
                        "pour pouvoir retrouver celle qui correspond au besoin du demandeur. Il peut "
                        "s'agir de filtres, de moteurs de recherche, qui doivent permettre de faire "
                        "correspondre une offre spécifique à une demande singulière.\n\n"
                        "─── 5e mécanisme : la science de l'appariement ───\n\n"
                        "Elle reprend en partie les mécanismes de la logique de la longue traîne, "
                        "puisqu'il s'agit d'arriver à mettre en relation deux choses qui vont "
                        "naturellement de pair. La science de l'appariement va donc consister à "
                        "s'assurer que les offres et les demandes qui vont ensemble puissent se "
                        "« rencontrer » sur la plateforme.\n\n"
                        "─── 6e mécanisme : les marchés bifaces voire multifaces ───\n\n"
                        "Cela va consister à trouver les moyens de s'assurer des revenus par "
                        "plusieurs moyens, et de réussir à faire payer les deux faces du marché, à "
                        "savoir les offreurs et les demandeurs. Mais il peut être également "
                        "intéressant d'inviter d'autres types d'acteurs à proposer des offres sur la "
                        "plateforme (par exemple de la publicité) pour augmenter le nombre de sources "
                        "de revenus. Pour réussir à attirer à la fois offreurs et demandeurs, "
                        "l'opérateur de la plateforme peut mettre en place des dispositifs pour "
                        "attirer une des faces, comme par exemple prendre à sa charge les coûts "
                        "relatifs à une des faces au démarrage pour les inciter à venir sur la "
                        "plateforme, ou mettre en place des systèmes freemium, c'est-à-dire gratuit "
                        "au début puis payant pour avoir plus de fonctionnalités.\n\n"
                        "─── Les 4 risques majeurs ───\n\n"
                        "1. Le pricing : la prise en charge des coûts liés à une des faces du marché "
                        "peut présenter un risque pour l'opérateur. Il faut faire attention à ce que "
                        "ce mécanisme ne tue pas le business model imaginé au départ.\n\n"
                        "2. La méfiance entre les utilisateurs : il faudra donc pour l'opérateur "
                        "mettre en place les conditions de confiance pour éviter ce risque.\n\n"
                        "3. Le timing : le premier arrivé, si sa plateforme répond parfaitement aux "
                        "besoins des utilisateurs, aura un avantage considérable par rapport à ses "
                        "concurrents, notamment à cause des externalités de standard évoquées "
                        "précédemment. Mais il faut également que le marché soit prêt lors du "
                        "lancement d'une plateforme, pour que celle-ci ne soit pas délaissée. Un "
                        "mécanisme important pour se lancer rapidement est le MVP (minimum viable "
                        "product), qui est un produit ne présentant pas encore toutes les "
                        "caractéristiques du produit final mais qui permet déjà de faire du chiffre "
                        "d'affaires et d'avoir des retours utilisateurs pour améliorer son produit.\n\n"
                        "4. L'orgueil, notamment pour les plateformes déjà installées : comme dans "
                        "un secteur traditionnel, une entreprise leader sur son marché ne doit pas "
                        "croire que la bataille est gagnée et qu'elle va le rester toute sa vie. "
                        "Elle doit donc continuer à innover pour se prémunir d'entrants potentiels "
                        "et garder à tout prix son avantage concurrentiel.\n\n"
                        "Les plateformes répondent donc à d'autres logiques que des activités "
                        "« physiques » que nous avions l'habitude de côtoyer et s'appuient donc sur "
                        "des mécanismes différents pour garantir à l'opérateur de la plateforme un "
                        "succès. Ces mécanismes doivent donc être pris en compte pour éviter les "
                        "quatre risques majeurs que comporte le lancement d'une plateforme."
                    ),
                }
            ],
        },
        {
            "label": "Sujet n°2 — Étude de cas : « La nouvelle stratégie de Bic » (20 points, 5 pts/question)",
            "context": (
                "BIC est un des leaders mondiaux des articles de papeterie, des briquets et des "
                "rasoirs. Depuis plus de 75 ans, l'entreprise fabrique des produits de grande "
                "qualité accessibles à tous, partout dans le monde. Cette vocation a permis au "
                "Groupe de faire de sa marque, enregistrée dans le monde entier, l'une des plus "
                "reconnues.\n\n"
                "À partir des deux articles suivants, présentés par ordre chronologique, vous "
                "répondrez aux questions suivantes.\n\n"
                "━━━ TEXTE 1 — « Bic contraint de se réinventer pour affronter l'avenir », Le Figaro "
                "Économie, 3 janvier 2020 ━━━\n\n"
                "Le groupe a finalisé la cession de sa filiale de sport. Il se concentre désormais "
                "sur les stylos, rasoirs et briquets.\n\n"
                "Bic tire un trait sur ses planches à voile et paddles. Le groupe a finalisé la "
                "vente à l'estonien Tahe Outdoors de sa filiale Bic Sport, spécialisée dans les "
                "sports de glisse nautique. Il en obtiendra de 6 à 9 millions d'euros en fonction "
                "des résultats futurs de son ex-filiale. Avec cette cession, mise en œuvre par "
                "Gonzalve Bich, investi il y a un an par son père à la tête du groupe, Bic revient "
                "à ses activités historiques : stylos, briquets et rasoirs. Le groupe français, "
                "détenu à 44 % par la famille fondatrice, tire un trait final sur ses "
                "diversifications. Oubliée l'époque où l'entreprise vendait des téléphones portables "
                "dans les bureaux de tabac ; Bic a surtout renoncé à faire des produits "
                "promotionnels son quatrième pilier : il a cédé mi-2017 les activités "
                "nord-américaines de son ex-division Bic Graphic au fonds américain HIG pour 71 "
                "millions d'euros.\n\n"
                "Un choix imposé par la force des choses. Depuis deux ans, la croissance de Bic a "
                "marqué le pas, notamment dans l'activité rasoirs, bouleversée par la montée en "
                "puissance des acteurs en ligne comme Dollar Shave Club (Unilever) qui tirent les "
                "prix du marché à la baisse, surtout aux États-Unis. La rentabilité a par ailleurs "
                "été affectée par la hausse du coût des matières premières. À cela s'ajoute "
                "l'intensification de la concurrence des pays à bas coût. En tant que fabricant de "
                "biens de consommation (stylos, briquets, rasoirs), Bic est aussi confronté à un "
                "environnement de plus en plus compétitif. Les distributeurs sont aujourd'hui "
                "concurrencés par Amazon. Le digital a aussi donné naissance à de nouveaux acteurs, "
                "comme les « pure players » du rasage aux États-Unis. De plus, le comportement des "
                "consommateurs change, sans parler de la volatilité des matières premières.\n\n"
                "Le groupe septuagénaire, qui a réalisé l'an passé 2 milliards d'euros de chiffre "
                "d'affaires, est confronté à une triple contrainte : la baisse du nombre de fumeurs "
                "dans les pays occidentaux, la mode de la barbe qui incite les hommes à bouder leur "
                "rasoir et la désaffection à l'égard de l'écriture manuscrite. Si Bic peut compter "
                "sur une marque forte et reconnue mondialement, un puissant réseau de distribution "
                "et son intégration industrielle (26 usines), il est en fait à la croisée des "
                "chemins. Certes, les pays émergents représentent un tiers de son activité. Mais la "
                "volatilité de certaines économies, à l'image du Brésil, a fragilisé le groupe. Bic "
                "doit s'atteler à trouver de nouveaux relais de croissance pour l'avenir. « Afin de "
                "faire face aux défis et opportunités d'aujourd'hui et de demain, nous devons "
                "réinventer Bic », reconnaît aujourd'hui Gonzalve Bich, 40 ans, qui veut imprimer "
                "sa marque en modernisant le groupe. Une équipe a été chargée de définir un plan "
                "stratégique qui devrait être présenté fin 2020.\n\n"
                "━━━ TEXTE 2 — « Le plan stratégique de Gonzalve Bich », Les Echos, 12 novembre 2020 ━━━\n\n"
                "À la tête de Bic depuis deux ans et demi, Gonzalve Bich, le petit-fils du "
                "fondateur, veut relancer la croissance du champion mondial des biens de "
                "consommation. À l'occasion de la journée investisseurs mardi, il a présenté les "
                "points clés de son plan stratégique baptisé « Horizon ». Le groupe veut atteindre "
                "une croissance annuelle du chiffre d'affaires d'environ 5 %. Et de générer, grâce "
                "aux économies, « au moins 200 millions d'euros de flux nets de trésorerie par an "
                "jusqu'en 2022 ». Le montant des investissements sera en moyenne de 100 millions "
                "d'euros par an.\n\n"
                "« Monsieur Gonzalve Bich, parlez-nous du plan Horizon… »\n"
                "« Afin de faire face aux défis et opportunités d'aujourd'hui et de demain, nous "
                "devons réinventer Bic pour redevenir en 2022 un champion mondial des produits de "
                "consommation courante, plus agile et plus innovant. C'est l'ambition de ce plan "
                "stratégique. Ce projet « Horizon » s'inscrit dans la continuité du plan précédent et "
                "ouvre un nouveau chapitre, celui de la croissance, afin de voir comment nous allons "
                "élargir le périmètre de nos activités, en allant vers des segments de marché "
                "proches des nôtres et en forte croissance. Par exemple dans l'écriture, nous allons "
                "continuer à produire et fournir aux consommateurs des stylos de haute qualité à un "
                "prix abordable, avec une marque qu'ils connaissent, mais nous allons aussi leur "
                "apporter de nouveaux produits et de nouveaux usages. »\n\n"
                "« C'est le sens du rachat de Rocketbook, la marque américaine de carnets "
                "intelligents ? »\n"
                "« Rocketbook s'inscrit dans notre ADN. Ses cahiers, qui s'utilisent avec un stylo "
                "effaçable et dont le contenu peut être téléchargé via une application sur "
                "smartphone, sont proposés à un prix inférieur à 40 dollars. Et le consommateur fait "
                "un achat qui conserve l'aspect manuscrit de l'écriture. Ces cahiers présentent "
                "aussi un avantage environnemental car ils sont réutilisables. Ce sont nos premiers "
                "pas dans l'écriture digitale. Cette acquisition renforce l'activité Papeterie de "
                "BIC avec l'ajout d'un segment de marché très porteur. Les co-fondateurs de "
                "Rocketbook, Joe Lemay et Jake Epstein, l'ont reconnu, il y a une grande "
                "complémentarité entre BIC et Rocketbook. Nous sommes convaincus que Rocketbook "
                "pourra atteindre des niveaux de performances plus élevés en profitant de "
                "l'avantage parental offert par le groupe BIC. »\n\n"
                "« Sur chaque pilier du groupe, vous allez donc aller sur de nouveaux territoires ? »\n"
                "« Nous n'abandonnons pas ce qui a fait la force de notre marque. Nous allons "
                "continuer à fabriquer des stylos, des briquets et des rasoirs, mais nous allons "
                "étendre notre champ d'action tout en rationalisant nos gammes. Par exemple, dans "
                "l'écriture, nous constatons depuis une dizaine d'années que les gens ont envie de "
                "déconnecter et de se détendre à travers différentes formes d'activités créatives. "
                "Le coloriage pour adultes ou encore les marqueurs de tatouage éphémères Bodymark "
                "que nous avons lancé aux États-Unis et en Europe sont un succès. Il y a donc plein "
                "d'autres façons d'innover, d'amener de nouvelles solutions pour égayer le "
                "quotidien. »"
            ),
            "items": [
                {
                    "q": (
                        "1. À partir du premier texte qui présente les décisions prises sur le "
                        "portefeuille d'activités, comment peut-on qualifier la stratégie actuelle "
                        "du groupe Bic ? Justifiez vos propos."
                    ),
                    "correction": "[Pas de meilleure copie pour le Sujet n°2 — le candidat a traité le Sujet n°1]",
                },
                {
                    "q": "2. Selon vous, s'agit-il d'une stratégie « adaptative » ou « intentionnelle » ? Justifiez vos propos.",
                    "correction": "[Pas de meilleure copie pour le Sujet n°2 — le candidat a traité le Sujet n°1]",
                },
                {
                    "q": (
                        "3. Quel est d'après vous le mode de gouvernance en vigueur chez Bic ? "
                        "Justifiez vos propos. En quoi peut-il avoir une influence sur la stratégie ?"
                    ),
                    "correction": "[Pas de meilleure copie pour le Sujet n°2 — le candidat a traité le Sujet n°1]",
                },
                {
                    "q": (
                        "4. Le dirigeant du groupe BIC déclare dans le texte 2 : « Nous sommes "
                        "convaincus que Rocketbook pourra atteindre des niveaux de performances plus "
                        "élevés en profitant de l'avantage parental offert par le groupe BIC. » "
                        "Qu'est-ce qu'un avantage parental ? Quelles sont les sources d'un tel "
                        "avantage ? En quoi cette notion permet-elle de justifier le rachat de "
                        "Rocketbook ?"
                    ),
                    "correction": "[Pas de meilleure copie pour le Sujet n°2 — le candidat a traité le Sujet n°1]",
                },
            ],
        },
    ],
    "tips": [
        "Choix de sujet : la majorité des candidats traite le Sujet n°1 (question de cours sur les plateformes) — il est plus structurable. Le Sujet n°2 (étude de cas BIC) demande de mobiliser plusieurs concepts (stratégie adaptative/intentionnelle, gouvernance, avantage parental).",
        "Pour le Sujet n°1 : structurer autour de Benavent (2016) et ses 6 mécanismes + 4 risques. Mobiliser la loi de Metcalfe, le MVP, l'économie de la variété, les marchés bifaces.",
        "Définir précisément ce qu'est une plateforme (2 caractéristiques) avant de dérouler les mécanismes.",
        "Pour le Sujet n°2 (BIC) : qualifier la stratégie de recentrage / focalisation sur métier historique. Le mode de gouvernance familial (44 % par la famille fondatrice) influence la stratégie de long terme.",
        "Avantage parental (notion de corporate strategy) : valeur ajoutée que le groupe apporte à sa filiale (savoir-faire industriel, réseau de distribution, marque, complémentarités).",
    ],
}


# ═══════════════════════════════════════════════════════════════════════════
# GOUV — 2024-2025 (Management des Systèmes d'Information, N. LEBEY, 2h)
# Sujet : UE 7 - Management des SI.pdf
# Meilleure copie : note 16/20, n° 112516 — 5 questions
# ═══════════════════════════════════════════════════════════════════════════
GOUV_2024 = {
    "id": "gouv_2024_2025",
    "year": "2024-2025",
    "name": "Session 1 — Mercredi 11 juin 2025",
    "duration": "2h00",
    "format": "Écrit · Aucun document autorisé",
    "professor": "N. Lebey",
    "subject": "",
    "dossiers": [
        {
            "label": "Question 1 — Dématérialisation des bulletins de paie",
            "context": (
                "Dématérialisation des bulletins de paie : un nouveau standard en entreprise ?\n\n"
                "Article de Bertrand Dolbeau.\n"
                "Selon le Baromètre 2024 de la dématérialisation des documents RH mené par Digiposte "
                "et OpinionWay, 63 % des travailleurs reçoivent aujourd'hui leur fiche de paie au "
                "format numérique contre seulement 42 % en 2020. Cette transition vers un "
                "environnement professionnel toujours plus digital, loin d'être anodin, témoigne "
                "d'un bouleversement profond des usages et des mentalités, même si des inquiétudes "
                "persistent.\n\n"
                "Le coffre-fort numérique, outil plébiscité par les salariés, s'impose comme une "
                "réponse adaptée aux besoins de sécurité et d'accessibilité. Il permet non "
                "seulement un stockage sûr et durable des bulletins de paie, mais ouvre aussi la "
                "voie à une centralisation plus large des documents RH.\n\n"
                "La praticité de conservation (58 %) et l'accès facilité (51 %) restent les deux "
                "principaux leviers de la dématérialisation du bulletin de paie et les salariés "
                "recevant leurs bulletins de paie dans un coffre-fort numérique sont très "
                "confiants, à 90 %, par rapport au stockage de ce type de document.\n\n"
                "Pourtant, cette transformation n'est pas exempte de résistances. Près de 80 % des "
                "salariés expriment encore des préoccupations face aux risques numériques, "
                "notamment le vol de données personnelles ou l'utilisation frauduleuse de leurs "
                "documents. Un sentiment de vulnérabilité qui n'est pas à prendre à la légère et "
                "qui impose aux entreprises et aux acteurs de la dématérialisation un effort "
                "constant en matière de transparence et de pédagogie. Car si la technologie est "
                "prête, les esprits, eux, ont encore besoin d'être rassurés. Dans ce contexte, "
                "l'hébergement des données en France ou en Europe émerge comme une solution "
                "rassurante, souhaitée par 72 % des répondants.\n\n"
                "Des solutions de confiance peuvent apporter une réponse sécurisée et pédagogique "
                "pour accompagner les entreprises dans cette transition numérique, au bénéfice des "
                "employeurs comme des salariés."
            ),
            "items": [
                {
                    "q": "Expliquez quelles sont les obligations et les risques liés à la dématérialisation des bulletins de salaire.",
                    "correction": (
                        "[Meilleure copie — note 16/20]\n\n"
                        "La dématérialisation des bulletins de salaire implique les obligations et "
                        "les risques suivants.\n\n"
                        "━━━ OBLIGATIONS ━━━\n\n"
                        "Au niveau des obligations, la dématérialisation impose à l'entreprise de "
                        "garantir aux salariés :\n"
                        "  • La sécurité de leurs données à caractère personnel (DCP) par la mise en "
                        "place d'un certain nombre de moyens, mesures, ressources ainsi que de leurs "
                        "données sensibles comme le coffre-fort numérique\n"
                        "  • La disponibilité de ces données pendant 50 ans (accès numérique)\n"
                        "  • L'intégrité de celles-ci\n"
                        "  • L'authenticité et l'identification de celles-ci ainsi que de son "
                        "émetteur et de celui qui y accède\n"
                        "  • La non-répudiation\n"
                        "  • L'inaltérabilité\n\n"
                        "Cette dématérialisation impose également aux entreprises de se conformer au "
                        "RGPD (Règlement Général sur la Protection des Données) et à la loi "
                        "Informatique et Libertés de 1978.\n\n"
                        "L'entreprise est tenue de nommer un DPO (Délégué à la Protection des "
                        "Données) chargé du respect du traitement de ces données au RGPD.\n\n"
                        "Elle doit tenir un registre des traitements des données à caractère "
                        "personnel.\n"
                        "Elle doit informer la CNIL (Commission Nationale Informatique et Libertés) "
                        "de toute perte de données dans les 72h.\n"
                        "Elle doit garantir les droits des salariés en ce qui concerne le droit à la "
                        "consultation de leurs DCP, le droit à la rectification / suppression de "
                        "leurs données, le droit à la portabilité.\n"
                        "Elle doit informer les salariés des finalités du traitement de la collecte "
                        "de leurs données à caractère personnel et obtenir leurs consentements si "
                        "elles souhaitent commercialiser celles-ci.\n"
                        "Elle doit stocker ces données sur des serveurs hébergés en France et/ou en "
                        "Europe.\n"
                        "Elle doit mettre en place une PSSI (Politique de Sécurité des Systèmes "
                        "d'Information) et un PCA (Plan de Continuité d'Activité).\n"
                        "Elle doit nommer un RCCI (Responsable Conformité et Contrôle Interne) et "
                        "mettre en place une procédure de contrôle interne.\n\n"
                        "━━━ RISQUES ━━━\n\n"
                        "Au niveau des risques, la dématérialisation engendre les risques suivants :\n\n"
                        "  • Risques financiers en cas de perte / vol de données : cela peut "
                        "engendrer des coûts pour l'entreprise, d'une part pour indemniser les "
                        "salariés du préjudice subi, et d'autre part, en cas de rançons demandées "
                        "par les assaillants.\n\n"
                        "  • Risques d'image liés également à la perte / fuite des données qui "
                        "aurait pour conséquence de faire perdre la confiance des salariés dans la "
                        "capacité à protéger leurs données et par la même occasion celles de leurs "
                        "clients.\n\n"
                        "  • Risques organisationnels liés à la nécessité de cartographier les "
                        "risques, d'élaborer une stratégie et une méthode de projet pour mettre en "
                        "place cette dématérialisation, ainsi que l'établissement de procédures.\n\n"
                        "  • Risques humains liés à la résistance au changement, par exemple 37 % "
                        "selon le baromètre 2024 de la dématérialisation des documents RH mené par "
                        "Digiposte et OpinionWay.\n\n"
                        "  • Risques techniques et informatiques liés à la mise en œuvre de cette "
                        "dématérialisation et la nécessité d'avoir du matériel permettant celle-ci, "
                        "de répondre à ses obligations vues précédemment ; la nécessité d'avoir les "
                        "compétences techniques ou informatiques… et/ou encore la perte de réseaux "
                        "de communication."
                    ),
                }
            ],
        },
        {
            "label": "Question 2 — IA et usages : 3 risques + pistes pour les diminuer",
            "context": (
                "IA et usages : la confiance, pierre angulaire de son adoption durable.\n\n"
                "Une étude mondiale KPMG-Université de Melbourne révèle une adoption croissante de "
                "l'IA, mais pointe un manque de formation, une confiance encore limitée et la "
                "nécessité d'un cadre réglementaire renforcé. En France, malgré des usages en "
                "progression, les risques associés demeurent encore des freins importants notamment "
                "en entreprise."
            ),
            "items": [
                {
                    "q": "Donnez et expliquez trois risques, proposez des pistes pour les diminuer.",
                    "correction": (
                        "[Meilleure copie — note 16/20]\n\n"
                        "─── 1. Le risque de résistance au changement ───\n\n"
                        "La crainte de voir l'IA remplacer les tâches réalisées par l'Homme pousse "
                        "celui-ci à refuser parfois son adoption par ses détracteurs.\n\n"
                        "Afin de diminuer ce risque, il convient d'étudier les possibilités offertes "
                        "par l'IA afin d'aider l'Homme dans son quotidien, développer les formations "
                        "et intégrer et développer la culture du numérique dans les usages du "
                        "quotidien aussi bien professionnel que personnel.\n\n"
                        "Il faut également renforcer la confiance des ménages et des entreprises "
                        "dans l'IA par l'adoption d'un cadre réglementaire renforcé. Pour cela, "
                        "l'UE envisage d'établir, on a déjà établi ce qu'on appelle l'IA Act afin de "
                        "protéger le citoyen européen.\n\n"
                        "─── 2. Le risque de dépendance, de perte de compétences et/ou de savoir-faire ───\n\n"
                        "En effet, l'accroissement de l'IA dans nos usages, et l'avancée "
                        "technologique des américains dans ce domaine bouleverse les entreprises. "
                        "Ainsi, cela provoque ou peut provoquer une dépendance à l'égard de pays "
                        "disposant d'avancées technologiques dans ce domaine si l'UE ne suit pas.\n\n"
                        "Ainsi pour diminuer ce risque, il convient de rechercher un équilibre entre "
                        "réglementation afin de protéger / sécuriser et performance / création de "
                        "valeur. Il faut donc mettre en place une stratégie visant à garder une "
                        "autonomie stratégique par l'allocation de moyens / ressources au niveau "
                        "européen mais également des mesures de contrôles, d'audit afin d'assurer "
                        "la conformité et la pérennité de l'entreprise et de l'adoption de l'IA dans "
                        "nos usages.\n\n"
                        "Enfin, il faut également développer la formation continue et accompagner la "
                        "montée en compétences des salariés dans l'usage de l'IA au quotidien. Cela "
                        "nécessite donc la mise en place d'une gouvernance du système d'information "
                        "au sein de l'entreprise, d'audit de sécurité, d'audit IT, de comités "
                        "d'audit… Cela peut également être l'adoption de référentiels de bonnes "
                        "pratiques.\n\n"
                        "─── 3. Le risque de sécurité ───\n\n"
                        "En effet, l'utilisation de l'IA dans nos usages amène la question du risque "
                        "de sécurité lié aux données intégrées dans cet outil. À qui appartiennent "
                        "les données, comment garantir le droit à la propriété intellectuelle, les "
                        "droits d'auteurs…\n\n"
                        "Ainsi, afin de diminuer ce risque, les entreprises peuvent développer des "
                        "IA spécifiques à leur profession, telle que l'IA Francis Lefebvre basée sur "
                        "la base de données des éditions Francis Lefebvre. Elles peuvent également "
                        "former les collaborateurs, souscrire des cyber-assurances, étudier les "
                        "contrats de services avec leurs fournisseurs tout en prévoyant des clauses "
                        "de réversibilité, des niveaux de services (SLA / SLR)…"
                    ),
                }
            ],
        },
        {
            "label": "Question 3 — Facturation électronique : un chantier triple",
            "context": (
                "La mise en place de la facturation électronique est un chantier à la fois "
                "informatique, financier et managérial. Mais il ne faut pas oublier les "
                "obligations qui s'imposent aux entreprises, notamment en matière de traitement des "
                "données personnelles."
            ),
            "items": [
                {
                    "q": "Expliquez « un chantier à la fois informatique, financier et managérial ».",
                    "correction": (
                        "[Meilleure copie — note 16/20]\n\n"
                        "La facturation électronique est un chantier à la fois informatique, "
                        "financier et managérial car elle nécessite la mise en place d'un ensemble "
                        "de mesures regroupant à la fois la sécurité des systèmes d'informations, "
                        "l'allocation de ressources financières pour accompagner cette "
                        "transformation ainsi que la mise en place d'une gouvernance des systèmes "
                        "d'information afin de réduire les risques pour les organisations tout en "
                        "leur permettant d'être performantes et créer de la valeur. C'est donc la "
                        "recherche d'un équilibre entre risques et création de valeur."
                    ),
                },
                {
                    "q": "Quelles sont les obligations qui s'imposent aux entreprises, notamment en matière de traitement des données personnelles.",
                    "correction": (
                        "[Meilleure copie — note 16/20]\n\n"
                        "En ce qui concerne les obligations qui s'imposent aux entreprises, je vous "
                        "invite à consulter la réponse à la question 1, faisant référence à "
                        "celles-ci en ce qui concerne le traitement des données à caractère "
                        "personnelles (RGPD, loi Informatique et Libertés de 1978, nomination DPO, "
                        "registre des traitements, information CNIL sous 72h, droits des salariés, "
                        "stockage en France/Europe, PSSI, PCA, RCCI…)."
                    ),
                },
            ],
        },
        {
            "label": "Question 4 — Politique de sécurité des SI",
            "context": "",
            "items": [
                {
                    "q": "Décrivez les différentes étapes pour construire une politique de sécurité SI.",
                    "correction": (
                        "[Meilleure copie — note 16/20]\n\n"
                        "Pour construire une politique de sécurité des SI, on peut se référer aux "
                        "référentiels ISO 17799 et ISO 27000 et suivants. On peut également se "
                        "référer à la méthodologie MARION pour la mise en place de celle-ci.\n\n"
                        "1) Nommer un DPO (Délégué à la Protection des Données).\n"
                        "2) Établir un audit du SI afin d'identifier les risques et les menaces "
                        "pesant sur le SI.\n"
                        "3) Évaluer les risques pour l'entreprise. Risque = Impact × Menace × "
                        "Vulnérabilité.\n"
                        "4) Effectuer une analyse d'impact de ces risques et définir les mesures "
                        "correctives à mettre en place.\n"
                        "5) Mettre en place les mesures correctives.\n"
                        "6) Vérifier et contrôler régulièrement le niveau de sécurité attendu du SI "
                        "par des indicateurs clés.\n\n"
                        "La mise en place d'une politique SI passe également par la mise en place "
                        "d'un Plan de Continuité d'Activité (PCA) et d'un Plan de Sécurité du "
                        "Système d'Information (PSSI)."
                    ),
                },
                {
                    "q": (
                        "Donnez 3 problèmes ou difficultés que l'on peut rencontrer lors de la mise "
                        "en œuvre d'une politique de sécurité, proposez pour chaque problème des "
                        "pistes pour les diminuer."
                    ),
                    "correction": (
                        "[Meilleure copie — note 16/20]\n\n"
                        "Voici 3 problèmes ou difficultés que l'on peut rencontrer lors de la mise "
                        "en œuvre d'une politique de sécurité :\n\n"
                        "─── Problème 1 : Moyens / ressources financières ───\n\n"
                        "Solution : lever des fonds auprès des actionnaires, négocier le budget SI, "
                        "emprunter auprès de sa banque OU prioriser les risques et mettre en place "
                        "les mesures de sécurité en priorité sur les risques les plus significatifs "
                        "(démarche d'approche par les risques).\n\n"
                        "─── Problème 2 : Compétences techniques en interne ───\n\n"
                        "Solution : Externaliser la fonction SI, mettre en place des contrats de "
                        "services, d'infogérance avec des clauses de réversibilité et/ou "
                        "transférabilité. Il convient également de prévoir les niveaux de services "
                        "attendus (SLA / SLR) ainsi que la mise en place d'une TMA (Tierce "
                        "Maintenance Applicative) pour déterminer si l'on souhaite une maintenance "
                        "adaptative, évolutive, ainsi que le cahier des charges et le niveau "
                        "d'exigences attendus vis-à-vis du prestataire de services qui est souvent "
                        "une ESN (Entreprise de Services Numériques).\n\n"
                        "─── Problème 3 : Difficulté dans la construction même de cette politique de SI ───\n\n"
                        "Et manque de connaissances / compétences pour construire cette politique.\n\n"
                        "Solution : Utiliser les référentiels et guides de bonnes pratiques "
                        "permettant à quiconque de construire cette politique tels que les normes "
                        "ISO 17799, 27000 et suivants mais également les référentiels Val IT, "
                        "Risk IT, COBIT."
                    ),
                },
            ],
        },
        {
            "label": "Question 5 — Facturation électronique & IA : menace ou opportunité ?",
            "context": "Facture électronique et intelligence artificielle : menace ou opportunité pour les experts-comptables ?",
            "items": [
                {
                    "q": "Présentez 3 opportunités / 3 menaces en les développant.",
                    "correction": (
                        "[Meilleure copie — note 16/20]\n\n"
                        "Je réponds à cette question par les deux à la fois. Certains s'adapteront, "
                        "d'autres disparaîtront. On peut résumer cela par « le phénomène de "
                        "sélection naturelle ».\n\n"
                        "━━━ OPPORTUNITÉS ━━━\n\n"
                        "• L'expert-comptable, et au notamment, au travers l'action menée par "
                        "l'ordre des experts-comptables envisage de devenir un tiers de confiance "
                        "numérique pour le chef d'entreprise. Cela lui permettra donc d'être « au "
                        "centre du jeu », de la donnée, d'avoir accès à des informations "
                        "privilégiées en temps réel, perfectionner la connaissance de ses clients et "
                        "développer des missions à plus forte valeur ajoutée.\n\n"
                        "• La facturation électronique et l'intelligence artificielle permettront "
                        "également à l'EC (expert-comptable) de gagner un temps considérable. Fini "
                        "de scanner, photocopier, trier, ranger, archiver les factures. Fini la "
                        "saisie comptable. Fini de passer des coups de téléphone aux chefs "
                        "d'entreprise pour récupérer telle ou telle pièce comptable ! Tout sera "
                        "centralisé, implémenté directement en comptabilité automatiquement. Cela "
                        "lui permettra ainsi de réduire ses coûts, ses charges et dégager des "
                        "marges et une rentabilité supérieure.\n\n"
                        "• La facturation électronique et l'intelligence artificielle va permettre "
                        "de réduire les risques d'erreurs (erreur de saisie par exemple), lutter "
                        "contre la fraude, détecter les anomalies, éviter les doublons de facture, "
                        "les ruptures de séquences, supprimer le manquement des mentions "
                        "obligatoires sur celles-ci, éviter des sanctions financières, avoir une "
                        "visibilité et connaître les délais de paiement de ses clients / "
                        "fournisseurs, envoyer des relances automatiques.\n\n"
                        "━━━ MENACES ━━━\n\n"
                        "• Risques de perte de données liés à l'accroissement des cyberattaques, "
                        "attaques par rançongiciels, déni de service…\n\n"
                        "• Risques financiers en cas de perte, vol des données, fuite… mais "
                        "également hausse des coûts de cyber-assurance, de coûts de stockage, "
                        "maintenance des serveurs et SI.\n\n"
                        "• Risques sociaux liés à la suppression des emplois, mais également risque "
                        "de remplacement de l'EC par l'IA à terme."
                    ),
                }
            ],
        },
    ],
    "tips": [
        "5 questions à traiter en 2h → ~24 min/question. Bien gérer le temps : il ne faut pas faire l'impasse sur la dernière question (souvent rédactionnelle).",
        "Structure attendue pour chaque question : annoncer le plan (obligations / risques / opportunités / menaces) puis dérouler en parties claires.",
        "Mobiliser les acronymes du cours : DPO, RGPD, CNIL, PSSI, PCA, PRA, SLA, SLR, TMA, ESN, ISO 27000, COBIT, Val IT, Risk IT, MARION, IA Act.",
        "Pour Q1 et Q3 : la dématérialisation et la facturation électronique partagent les mêmes obligations RGPD — on peut renvoyer d'une question à l'autre (gain de temps).",
        "Pour Q5 : structurer en 3 opportunités + 3 menaces, bien équilibrer. Possibilité de conclure avec une métaphore (« sélection naturelle »).",
    ],
}


# ═══════════════════════════════════════════════════════════════════════════
# CONDUITE_CHGT — 2024-2025 (Conduite du changement et gestion des compétences,
# F. BESOMBES, 1h)
# Sujet : UE 9 - Conduite de changement et RSE.pdf p.1
# Meilleure copie : note 17/20, n° 081962
# ═══════════════════════════════════════════════════════════════════════════
CONDUITE_2024 = {
    "id": "cc_2024_2025",
    "year": "2024-2025",
    "name": "Session 1 — Jeudi 12 juin 2025",
    "duration": "1h00",
    "format": "Écrit · Aucun document autorisé",
    "professor": "F. Besombes",
    "subject": "",
    "dossiers": [
        {
            "label": "Question (20 points)",
            "context": "",
            "items": [
                {
                    "q": (
                        "Après avoir rappelé ce qu'est la compétence, la GPEC et la GEPP, vous "
                        "expliquerez en quoi la compétence est devenue un enjeu clé pour l'avenir "
                        "des organisations.\n\n"
                        "Puis, vous expliquerez en quoi une bonne gestion des compétences favorise "
                        "l'autonomie des personnes dans un contexte de changement."
                    ),
                    "correction": (
                        "[Meilleure copie — note 17/20 — « Très bon travail »]\n\n"
                        "─── Définitions et introduction ───\n\n"
                        "La compétence est une disposition à combiner, à moduler et à mettre en "
                        "œuvre des ressources. Elle représente le savoir-faire, les connaissances, "
                        "l'expérience de chacun. Elle est nécessaire pour tel ou tel métier et doit "
                        "être en adéquation avec le poste pour que la personne puisse être "
                        "efficiente.\n\n"
                        "La GEPP est la gestion de l'emploi et du parcours professionnel. Elle a été "
                        "mise en place en 2017 par Macron par le biais d'une ordonnance. Elle "
                        "concerne toutes les entreprises qui ont plus de 300 salariés. Il s'agit "
                        "d'une négociation auprès des salariés pour évaluer leurs compétences, voir "
                        "les évolutions des métiers et l'amélioration des compétences. Cette "
                        "négociation a lieu tous les trois ans.\n\n"
                        "De cette manière, on peut constater que la compétence est un enjeu crucial, "
                        "obsolète dans la pérennité de l'entreprise. Dans un premier temps, il sera "
                        "question de voir que la compétence est devenue un enjeu clé pour l'avenir "
                        "des organisations. Ensuite, il sera pertinent de voir que la bonne gestion "
                        "des compétences favorise l'autonomie des personnes dans un contexte de "
                        "changement.\n\n"
                        "─── I. La compétence : un enjeu clé pour l'avenir des organisations ───\n\n"
                        "Pour commencer, lors du recrutement, l'accent est mis sur l'adéquation des "
                        "compétences réelles du candidat et les compétences requises pour le métier. "
                        "Le système d'information est notamment utilisé pour répondre à cette "
                        "problématique. En effet, de plus en plus d'entreprises utilisent l'IA "
                        "prédictive pour constater les compétences. C'est le cas avec les ATS "
                        "(Attending Tracking System) où l'IA sélectionne des CV en priorité par "
                        "rapport à des compétences prédéfinies. L'IA peut également constater "
                        "quelles sont les compétences en tension dans tel corps de métier. Un autre "
                        "outil essentiel qui permet d'identifier les compétences des collaborateurs "
                        "est le SIRH. Ce système d'information permet d'avoir une visualisation "
                        "globale sur les salariés, constater leurs compétences, s'il y a un écart "
                        "entre les compétences requises et réelles. Cela permet également de voir si "
                        "les collaborateurs ont suivi des formations ou non. Tous ces outils "
                        "informatiques permettent de constater les compétences et une adéquation de "
                        "celles-ci avec le métier permet de faire fructifier grandement la "
                        "performance de l'entreprise. Sans les compétences requises, les "
                        "collaborateurs ne peuvent pas être efficients.\n\n"
                        "On peut également constater que la compétence est devenue un enjeu clé "
                        "dans l'avenir des organisations dans certaines situations. Plusieurs "
                        "anticipations doivent être prises en compte dans l'organisation d'une "
                        "entreprise. La GEPP permet justement de mettre en avant l'anticipation des "
                        "compétences. Cet élément doit être pris en compte lorsqu'un collaborateur "
                        "part à la retraite par exemple. Il représente un savoir-faire, des "
                        "compétences de plusieurs années. Il s'agit encore plus le cas dans les "
                        "générations qui arrivent actuellement à la retraite car ces personnes sont "
                        "souvent restées pendant plusieurs décennies dans la même entreprise. Ainsi, "
                        "lors du recrutement du remplaçant, il faut quelqu'un qui doit avoir un "
                        "minimum de compétences pour remplacer un collaborateur qui a une expérience "
                        "très largement reconnue. Une inadéquation des compétences lors du "
                        "recrutement du remplacement peut conduire à un véritable déséquilibre dans "
                        "l'organisation de l'entreprise.\n\n"
                        "Une autre situation à prendre en compte dans l'enjeu qu'est la compétence "
                        "est l'anticipation de l'évolution des métiers. En effet, il s'agit d'un "
                        "point abordé dans la GEPP qui est important. On peut donner l'exemple "
                        "d'une assistante comptable qui doit faire face à l'arrivée de la "
                        "facturation électronique. Son métier va complètement évoluer et les "
                        "compétences acquises et réelles seront peut-être obsolètes pour "
                        "l'évolution de son métier. Il ne sera plus demandé de faire de la saisie "
                        "comptable mais plutôt vérifier les données transmises par le SI et valider "
                        "celles-ci. Ainsi de nouvelles compétences seront requises et l'entreprise "
                        "doit anticiper ces évolutions pour pouvoir mettre en place une nouvelle "
                        "organisation.\n\n"
                        "─── II. La gestion des compétences favorise l'autonomie dans un contexte de changement ───\n\n"
                        "Une bonne gestion des compétences favorise l'autonomie des personnes dans "
                        "un contexte de changement. En effet, un changement peut être mal perçu par "
                        "les collaborateurs. Il peut y avoir de la résistance face à ce changement, "
                        "ce qui complique l'organisation des compétences et le management à "
                        "employer. En outre, une structure hiérarchique peut aussi être "
                        "handicapante dans le changement d'organisation et la bonne gestion des "
                        "compétences. C'est le cas car ce type de structure ne favorise pas la "
                        "transmission du savoir. S'il n'y a pas de transmission du savoir, il ne "
                        "peut pas y avoir une bonne gestion des compétences car elles ne circulent "
                        "pas entre collaborateurs et la performance en est influencée.\n\n"
                        "De cette manière, il est possible de s'appuyer sur la théorie de Kotter "
                        "pour favoriser une bonne gestion des compétences. Selon lui, il est "
                        "important de définir des objectifs fixes et de permettre des victoires à "
                        "court terme pour les collaborateurs. Il est également important de tous les "
                        "faire participer aux différents projets de l'entreprise. En y prenant "
                        "part, ils peuvent devenir autonomes et mettre en application leurs "
                        "compétences. Une autre idée de Kotter est celle de la politique de "
                        "l'urgence. Il faut être réactif dans ses missions. Cette réactivité pousse "
                        "à l'autonomie.\n\n"
                        "Un second auteur peut être cité pour montrer comment avoir une bonne "
                        "gestion des compétences en vue d'une autonomie des collaborateurs. "
                        "L'auteur en question est Peter Drucker. Ce dernier évoque l'homme comme "
                        "l'atout stratégique d'une structure. Il faut définir des objectifs clairs "
                        "et atteignables pour donner une impulsion positive. D'autre part, il faut "
                        "que les collaborateurs soient dans un apprentissage en continu. Il faut "
                        "régulièrement former les équipes afin que le savoir-faire augmente et que "
                        "les compétences requises soient en adéquation avec la réalité. Tous ces "
                        "éléments permettent une bonne gestion des compétences chez les "
                        "collaborateurs et cela permet qu'ils deviennent autonomes.\n\n"
                        "─── Conclusion ───\n\n"
                        "En conclusion, la GEPP et la GEPC (gestion des évolutions de compétences "
                        "professionnelles) mettent en avant l'importance de la compétence. Comme "
                        "on peut le voir au travers de l'utilisation des systèmes informatiques, il "
                        "s'agit d'un élément que l'on ne peut pas négliger. Il faut que les "
                        "compétences requises soient en adéquation avec les compétences réelles. "
                        "Il en va de même lorsque les métiers évoluent ou qu'un collaborateur part "
                        "à la retraite. Dans le cas contraire, il y a une désorganisation "
                        "stratégique qui apparaît dans la structure. Afin d'assurer une bonne "
                        "gestion des compétences au sein des collaborateurs, il est possible de "
                        "s'appuyer sur les théories de Kotter et Drucker. Le contexte de changement "
                        "peut effectivement révéler quelques difficultés qui peuvent être palliées "
                        "par un bon management."
                    ),
                }
            ],
        }
    ],
    "tips": [
        "Définir précisément les 3 termes en intro (compétence, GPEC, GEPP) : la GPEC a été remplacée par la GEPP en 2017 (ordonnance Macron) — bien marquer cette distinction.",
        "Mobiliser des outils SI concrets : ATS, SIRH, IA prédictive — ça montre une vision moderne et opérationnelle.",
        "Donner un exemple de métier en mutation (assistant comptable + facturation électronique) pour illustrer l'anticipation des compétences.",
        "Sur la 2e partie : mobiliser Kotter (8 étapes, victoires à court terme, sentiment d'urgence) et Drucker (homme = atout stratégique, objectifs SMART, apprentissage continu).",
        "Conclure en reliant les 2 parties : pas de bonne gestion du changement sans bonne gestion des compétences.",
    ],
}


# ═══════════════════════════════════════════════════════════════════════════
# RSE — 2024-2025 (RSE et CSRD, D. DUHERON, 1h)
# Sujet : UE 9 - Conduite de changement et RSE.pdf p.2-3
# Meilleure copie : note 17/20, n° 1755 — QCM 4,5/5
# ═══════════════════════════════════════════════════════════════════════════
RSE_2024 = {
    "id": "rse_2024_2025",
    "year": "2024-2025",
    "name": "Session 1 — Jeudi 12 juin 2025",
    "duration": "1h00",
    "format": "Écrit · Aucun document autorisé",
    "professor": "D. Duheron",
    "subject": "",
    "dossiers": [
        {
            "label": "Exercice 1 — QCM (5 points)",
            "context": "1 point par question. Lire attentivement chaque énoncé : certaines questions admettent une seule bonne réponse, d'autres plusieurs réponses possibles.",
            "items": [
                {
                    "q": (
                        "1. Qu'est-ce que la RSE ? (1 seule bonne réponse)\n"
                        "  ☐ A. L'ensemble des réglementations applicable aux entreprises en matière "
                        "Environnementale et sociale\n"
                        "  ☐ B. La prise en compte volontaire par l'entreprise de son impact en "
                        "matière Environnementale et Sociétale\n"
                        "  ☐ C. Un label garantissant aux tiers que l'entreprise travaille de "
                        "manière responsable\n"
                        "  ☐ D. La Réglementation Sociétale des Entreprises"
                    ),
                    "correction": (
                        "Bonne réponse : B — « La prise en compte volontaire par l'entreprise de son "
                        "impact en matière Environnementale et Sociétale ».\n\n"
                        "La RSE n'est PAS une réglementation imposée (A faux), pas un label (C faux), "
                        "pas une « Réglementation Sociétale » qui n'existe pas (D faux). C'est bien "
                        "une démarche volontaire portant sur les impacts environnementaux ET "
                        "sociétaux (économiques, sociaux, environnementaux, gouvernance)."
                    ),
                },
                {
                    "q": (
                        "2. Qu'est-ce que la CSRD ? (1 seule bonne réponse)\n"
                        "  ☐ A. Une norme de présentation des performances extra-financières "
                        "obligatoire pour toutes les entreprises\n"
                        "  ☐ B. Règlement Européen d'application obligatoire dans tous les pays de "
                        "l'Union Européenne\n"
                        "  ☐ C. Un des outils du Green Deal Européen pour accélérer la Transition "
                        "Environnementale des entreprises\n"
                        "  ☐ D. Le guide de mise en place du Rapport de Durabilité volontaire pour "
                        "les PME"
                    ),
                    "correction": (
                        "Bonne réponse : C — « Un des outils du Green Deal Européen pour accélérer "
                        "la Transition Environnementale des entreprises ».\n\n"
                        "La CSRD (Corporate Sustainability Reporting Directive) n'est pas "
                        "obligatoire pour toutes les entreprises mais seulement celles dépassant "
                        "certains seuils (A faux). C'est une directive (à transposer) et non un "
                        "règlement (B faux). Ce n'est pas un guide PME (D faux — c'est le rôle du "
                        "VSME)."
                    ),
                },
                {
                    "q": (
                        "3. Quelle(s) démarche(s) fait/font partie des principaux sujets à prendre "
                        "en compte pour construire sa stratégie RSE ? (1 seule bonne réponse)\n"
                        "  ☐ A. L'identification des parties prenantes et la prise en compte de "
                        "leurs attentes\n"
                        "  ☐ B. La description du modèle d'affaire de l'entreprise\n"
                        "  ☐ C. L'identification des enjeux, impacts, risques et opportunités liés "
                        "aux activités de l'entreprise\n"
                        "  ☐ D. A, B et C"
                    ),
                    "correction": (
                        "Bonne réponse : D — « A, B et C ».\n\n"
                        "Les trois axes sont indispensables à toute démarche RSE structurée : "
                        "cartographie des parties prenantes, description du business model et "
                        "identification des IRO (Impacts, Risques, Opportunités)."
                    ),
                },
                {
                    "q": (
                        "4. Quels outils / référentiels sont disponibles pour les entreprises sous "
                        "les seuils de la CSRD désirant préparer un rapport de performances "
                        "extra-financières ? (Plusieurs réponses possibles)\n"
                        "  ☐ A. La norme VSME (Voluntary Small and Medium Entities) de l'EFRAG\n"
                        "  ☐ B. La CSRD\n"
                        "  ☐ C. Label Engagé RSE Afnor\n"
                        "  ☐ D. Le statut de Société à Mission prévu par la Loi PACTE de 2019"
                    ),
                    "correction": (
                        "Bonnes réponses : A, C et D.\n\n"
                        "A — VSME : norme volontaire de l'EFRAG pour PME et micro-entreprises.\n"
                        "C — Label Engagé RSE Afnor : label structurant la démarche.\n"
                        "D — Société à Mission (Loi PACTE 2019) : statut juridique pour formaliser "
                        "une raison d'être.\n\n"
                        "B (CSRD) est faux : la CSRD s'applique aux entreprises AU-DESSUS des seuils, "
                        "pas en-dessous."
                    ),
                },
                {
                    "q": (
                        "5. Parmi les 10 Thèmes contenus dans les ESRS seul le Thème E1 "
                        "« Changement climatique » est quasi-incontournable. Quels sujets "
                        "aborde-t-il ? (Plusieurs réponses possibles)\n"
                        "  ☐ A. La biodiversité\n"
                        "  ☐ B. L'adaptation au changement climatique\n"
                        "  ☐ C. L'atténuation du changement climatique\n"
                        "  ☐ D. Préservation des ressources naturelles\n\n"
                        "(N.B. : la version distribuée du sujet mentionnait « le Thème S1 » par "
                        "erreur — il s'agit bien du Thème E1 = Changement climatique.)"
                    ),
                    "correction": (
                        "Bonnes réponses : B et C.\n\n"
                        "L'ESRS E1 (Changement climatique) couvre 3 piliers :\n"
                        "  • Atténuation du changement climatique (réduction des GES)\n"
                        "  • Adaptation au changement climatique (résilience)\n"
                        "  • Énergie\n\n"
                        "La biodiversité (A) est traitée dans l'ESRS E4. La préservation des "
                        "ressources naturelles (D) est plutôt dans E5 (économie circulaire) et E3 "
                        "(ressources aquatiques et marines)."
                    ),
                },
            ],
        },
        {
            "label": "Exercice 2 — Questions de cours, réponses courtes (4 points, 2 pts/question)",
            "context": "",
            "items": [
                {
                    "q": "1. Quelles sont les composantes de l'analyse de Double Matérialité au sens de la CSRD ?",
                    "correction": (
                        "[Meilleure copie — note 17/20]\n\n"
                        "La CSRD (Corporate Sustainability Reporting Directive), en français "
                        "directive de publication d'un rapport de durabilité pour les entreprises, "
                        "découle du pacte vert européen (Green Deal) de 2019 et impose un cadre de "
                        "reporting extra-financier standardisé avec les 12 normes ESRS (European "
                        "Sustainability Reporting Standards), des standards à respecter sur les "
                        "aspects environnementaux, sociaux et de gouvernance. Cela contribue à "
                        "financer la transition écologique.\n\n"
                        "Cela permet aux entreprises de présenter une analyse de double matérialité, "
                        "allant alors plus loin que la simple matérialité de la NFRD de 2014.\n\n"
                        "La simple matérialité était l'analyse de l'impact des enjeux RSE sur la "
                        "performance financière de l'entreprise (analyse extra-financière).\n\n"
                        "La double matérialité va plus loin et impose 2 analyses :\n\n"
                        "  • La matérialité d'impact = l'impact des enjeux de l'entreprise sur "
                        "l'environnement et les tiers, les parties prenantes, qui découle de son "
                        "activité. L'entreprise va alors identifier les impacts positifs et "
                        "négatifs majeurs, déterminants, réels ou potentiels, à court, moyen et "
                        "long terme.\n\n"
                        "  • La matérialité financière = l'impact des enjeux RSE sur la performance "
                        "de l'entreprise (correspond à la simple matérialité financière). Elle va "
                        "analyser les risques et opportunités, réels ou potentiels, à CT, MT, LT, "
                        "que les conséquences sociales, environnementales et économiques peuvent "
                        "avoir sur sa capacité à mobiliser ses capitaux, sur sa création de valeur, "
                        "les répercussions sur sa performance financière et globale."
                    ),
                },
                {
                    "q": "2. Quels sont les principaux enjeux qui devraient motiver un chef d'entreprise pour mettre en place une stratégie RSE ?",
                    "correction": (
                        "[Meilleure copie — note 17/20]\n\n"
                        "Les principaux enjeux RSE sont de diverses natures :\n\n"
                        "  • Cela peut amener une entreprise à se questionner sur son modèle "
                        "d'affaire pour le rendre plus durable, anticiper les perturbations futures "
                        "et donc être plus performante\n\n"
                        "  • Réduction des coûts en diminuant sa consommation d'énergie, par la "
                        "réduction des déchets par exemple\n\n"
                        "  • Cela peut lui permettre d'innover dans de nouvelles technologies et "
                        "ainsi augmenter sa sphère de clientèle donc favoriser un meilleur chiffre "
                        "d'affaires\n\n"
                        "  • En étant plus durable, elle peut fidéliser les parties prenantes\n\n"
                        "  • Elle devient attractive pour recruter des talents et fidéliser sa "
                        "main-d'œuvre\n\n"
                        "  • Elle améliore son image de marque, sa notoriété, sa réputation et "
                        "renforce ainsi sa performance (fidélisation)"
                    ),
                },
            ],
        },
        {
            "label": "Exercice 3 — Questions de cours, réponses développées (8 points, 4 pts/question)",
            "context": "",
            "items": [
                {
                    "q": "1. Quelles sont les grandes étapes de mise en œuvre d'une démarche RSE dans une organisation ? Présentez-les en expliquant les objectifs et les enjeux de chaque étape.",
                    "correction": (
                        "[Meilleure copie — note 17/20]\n\n"
                        "Les 6 grandes étapes dans la mise en œuvre d'une démarche RSE sont :\n\n"
                        "─── 1ère étape : Déterminer les enjeux RSE ───\n\n"
                        "Cela a pour but de construire la démarche de manière complète, en répondant "
                        "aux attentes CSRD.\n"
                        "  → Faire une analyse contextuelle de l'entreprise et de son environnement :\n"
                        "       • Faire un modèle d'affaire complet\n"
                        "       • Faire une cartographie des parties prenantes\n"
                        "       • Analyser la chaîne de valeur (amont et aval)\n"
                        "  → Faire l'analyse de double matérialité pour déterminer les enjeux RSE "
                        "les plus importants (impact et financière).\n\n"
                        "─── 2e étape : Identifier la gouvernance RSE ───\n\n"
                        "Il va falloir que la direction et le Conseil d'administration et les autres "
                        "organes de direction s'impliquent dans la démarche ; c'est une condition "
                        "obligatoire pour que la démarche ait du sens et elle doit engager toute "
                        "l'entreprise dans sa globalité.\n\n"
                        "─── 3e étape : Déterminer la politique et les objectifs RSE ───\n\n"
                        "Il s'agit de réfléchir aux objectifs RSE et à la politique RSE que l'on "
                        "souhaite appliquer, en lien avec la 1ère étape. Ils doivent être cohérents "
                        "et SMART (spécifiques, mesurables, atteignables, réalistes, "
                        "temporellement définis).\n\n"
                        "─── 4e étape : Élaborer un plan d'action ───\n\n"
                        "Déterminer une feuille de route avec le plan d'action des objectifs RSE et "
                        "définir une temporalité associée aux actions.\n\n"
                        "─── 5e étape : Mesurer la performance avec des indicateurs RSE ───\n\n"
                        "Il s'agit de chiffrer la démarche pour mesurer les écarts entre le "
                        "réalisé et le prévisionnel. Par exemple, pour un objectif de replanter 10 "
                        "000 arbres : c'est un indicateur de performance qui permet de situer "
                        "l'avancement et de savoir si on peut améliorer notre action. Cela permet "
                        "d'être dans une démarche d'amélioration continue = de revoir les "
                        "objectifs et d'améliorer les actions pour y parvenir.\n\n"
                        "─── 6e étape : Communiquer et reporting ───\n\n"
                        "Il faut alors communiquer sur la démarche, être transparent, réaliser le "
                        "rapport de durabilité aux normes attendues, CSRD et celles-ci validées par "
                        "un expert (CAC (H2A) ou organisme tiers indépendant).\n\n"
                        "De plus, l'entreprise peut étendre sa démarche par des certifications ou "
                        "labels pour faire reconnaître son investissement RSE."
                    ),
                },
                {
                    "q": "2. Quels sont les objectifs d'un rapport de durabilité conforme à la CSRD ? Expliquez en quoi cette nouvelle obligation va au-delà des anciennes exigences de reporting.",
                    "correction": (
                        "[Meilleure copie — note 17/20]\n\n"
                        "Les objectifs d'un rapport de durabilité conforme à la CSRD sont :\n\n"
                        "  • La standardisation des rapports pour faciliter les comparaisons\n"
                        "  • La double matérialité (impact + financière)\n"
                        "  • Le rapport de durabilité validé et certifié\n\n"
                        "Le rapport de durabilité est certifié par le CAC (inscrit à la H2A) ou un "
                        "organisme tiers indépendant qui atteste et certifie la solidité.\n\n"
                        "Il doit respecter les 12 normes ESRS, standardisées, ce qui permet aux "
                        "investisseurs de pouvoir comparer plus sereinement les rapports, qui "
                        "peuvent influencer les choix d'investissements.\n\n"
                        "Le vérificateur émet un rapport de certification avec une assurance limitée "
                        "(formulée négativement), d'une durée de validité de 6 ans, qui atteste donc "
                        "de la conformité de la démarche. Cela va donc plus loin puisque le fait "
                        "que la démarche soit contrôlée, les entreprises sont contraintes à faire "
                        "leur rapport de manière sérieuse et conforme.\n\n"
                        "Le vérificateur garantit la conformité, la sincérité et la fiabilité du "
                        "reporting après avoir vérifié qu'il n'y avait pas d'erreurs, d'omissions, "
                        "d'incohérences (avec les bilans financiers par exemple) ou qu'il soit "
                        "incomplet.\n\n"
                        "Il vérifie aussi toutes les informations en lien avec la chaîne de valeur, "
                        "le modèle d'affaire, les analyses d'impacts, les calculs effectués…\n\n"
                        "Ainsi, les investisseurs retrouvent confiance dans le processus et peuvent "
                        "investir dans la transition écologique."
                    ),
                },
            ],
        },
        {
            "label": "Exercice 4 — Question rédactionnelle de synthèse (3 points)",
            "context": "En une page maximum, exposez en quoi la RSE va avoir un impact sur votre futur métier. Vous pouvez vous positionner en tant que futur Responsable Financier d'une Entreprise, Expert-Comptable ou Commissaire aux Comptes… (précisez votre positionnement).",
            "items": [
                {
                    "q": "Rédigez votre synthèse (1 page maximum).",
                    "correction": (
                        "[Meilleure copie — note 17/20 — positionnement expert-comptable]\n\n"
                        "En tant qu'expert-comptable, la RSE aura un impact car de plus en plus "
                        "d'entreprises seront concernées. En effet, les seuils des entreprises "
                        "concernées seront amenés à diminuer (attente du positionnement européen "
                        "sur ce sujet, Omnibus 2) et surtout, les entreprises peuvent accéder à une "
                        "démarche volontaire et peuvent donc prendre part à la transition "
                        "écologique dès à présent.\n\n"
                        "En effet, le VSME (Voluntary Small and Medium Enterprise) est une démarche "
                        "volontaire pour les PME qui souhaitent être dans la RSE, avec des "
                        "objectifs simplifiés des ESRS. Cela concerne les micro-entreprises et les "
                        "PME jusqu'à 250 salariés, ce qui constitue la majorité de la clientèle "
                        "d'un cabinet d'expertise-comptable.\n\n"
                        "Nous pourrons alors accompagner et aider les entrepreneurs dans leur "
                        "démarche, en apportant nos conseils puisque nous sommes formés à la RSE. "
                        "De plus, étant en collaboration avec les CAC déjà formés à la "
                        "vérification, nous pourrons mieux guider nos clients.\n\n"
                        "Cela consistera à les accompagner dans leurs choix de niveau :\n"
                        "  • 1er niveau : objectifs classiques des RSE avec les enjeux "
                        "traditionnels de GES\n"
                        "  • 2e niveau plus poussé : comme le CRD classique mais avec des "
                        "objectifs allégés\n\n"
                        "Le rôle de soutien, appui et conseil sera donc important et constitue un "
                        "rôle essentiel pour accompagner les clients.\n\n"
                        "De plus, en tant qu'expert-comptable, on peut également mettre en place "
                        "une VSME au sein de son propre cabinet pour être soi-même acteur de la "
                        "démarche, ce qui peut attirer les talents, les nouvelles générations, "
                        "favoriser l'attractivité du cabinet et le pouvoir à innover, renforcer la "
                        "fidélisation des collaborateurs et la performance globale (motivation)."
                    ),
                }
            ],
        },
    ],
    "tips": [
        "Bien gérer son temps : QCM (5 min) → Ex2 court (10 min) → Ex3 développé (25 min) → Ex4 synthèse (15 min). La synthèse rapporte 3 points : ne pas la bâcler.",
        "Pour le QCM : attention à la Q5 qui mentionne « S1 » dans l'énoncé — il faut comprendre qu'il s'agit de E1 (Changement climatique). Les ESRS commencent par E (Environnement), S (Social), G (Gouvernance).",
        "Mémoriser les 6 étapes de la démarche RSE : enjeux → gouvernance → politique → plan d'action → mesure → reporting.",
        "Double matérialité = (impact + financière). C'est LA notion centrale de la CSRD à parfaitement maîtriser.",
        "Pour la synthèse Ex4 : se positionner clairement (expert-comptable / CAC / RF) dès l'intro. Mobiliser VSME pour le marché PME (cœur de clientèle des cabinets).",
    ],
}


# ═══════════════════════════════════════════════════════════════════════════
# APPLICATION
# ═══════════════════════════════════════════════════════════════════════════
def update_course(course_id: str, new_annale: dict) -> None:
    """Remplace l'annale 2024-2025 du cours (ou ajoute en première position).
    Préserve les autres annales (ex. anciennes années sans source verbatim).
    """
    path = DATA / f'{course_id}.json'
    d = json.loads(path.read_text())
    annales = d.get('annales', [])
    # Filtrer toute annale 2024-2025 existante pour la remplacer
    annales = [a for a in annales if a.get('year') != '2024-2025']
    # Insérer la nouvelle en première position
    annales.insert(0, new_annale)
    d['annales'] = annales
    path.write_text(json.dumps(d, ensure_ascii=False, indent=2))
    print(f'{course_id}.json : annale 2024-2025 réécrite verbatim, total {len(annales)} annale(s)')


if __name__ == '__main__':
    update_course('evo_orga', EVO_ORGA_2024)
    update_course('strat', STRAT_2024)
    update_course('gouv', GOUV_2024)
    update_course('conduite_chgt', CONDUITE_2024)
    update_course('rse', RSE_2024)
    print('\n✓ 5 annales 2024-2025 transcrites verbatim depuis Annales 2024/')
