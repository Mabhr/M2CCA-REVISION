"""Insère les chapitres Partie 2 + Partie 3 dans strat.html.

Source : /Users/mathieucours/Documents/M2 CCA/Management stratégique/
  - Support de cours Partie 2 2026.pdf (Interagir avec les acteurs de son environnement)
  - Support de cours Partie 3 2025.pdf (Légitimer la stratégie)

Tags : data-theme="concurrentielle" pour P2, "corporate" pour P3.
Index continue : chap-9 à chap-22.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / 'strat.html'

# Contenu des 14 chapitres (P2 = 8, P3 = 6)
NEW_CHAPTERS = '''
<div class="course-chapter" data-theme="concurrentielle" data-chap-idx="9" id="chap-9">
  <h2>9. Partie 2 — Introduction : les 3 enjeux stratégiques majeurs</h2>
  <div class="def-box">
    <div class="def-label">Architecture du cours — 3 enjeux</div>
    <p>Le cours s'articule autour de <strong>3 grands enjeux stratégiques</strong> qui structurent l'analyse contemporaine de la stratégie d'entreprise :</p>
    <ul>
      <li><strong>Enjeu 1 — Repenser la création de valeur</strong> : de nouvelles manières de créer de la valeur apparaissent dans la plupart des secteurs. Elles contribuent à imposer un nouveau modèle d'organisation : les plateformes. Comment fonctionnent-elles ? Quelles sont leurs conditions de réussite ? Comment peuvent réagir les acteurs en place ? <em>(Partie 1)</em></li>
      <li><strong>Enjeu 2 — Interagir avec les acteurs de son environnement</strong> : les ruptures technologiques contribuent à l'effondrement des frontières traditionnelles entre les secteurs. Les modèles classiques d'analyse de l'environnement perdent de leur intérêt. Comment envisager l'environnement des entreprises ? Comment gérer les relations avec les concurrents ? <em>(Partie 2)</em></li>
      <li><strong>Enjeu 3 — Légitimer la stratégie</strong> : de nombreux acteurs entendent aujourd'hui évaluer voire influencer les orientations prises par les entreprises. Peut-on déployer une stratégie cohérente avec les objectifs des parties prenantes ? Comment intégrer l'influence des parties prenantes dans la réflexion stratégique ? <em>(Partie 3)</em></li>
    </ul>
  </div>
  <h3>Rappel : le modèle des 5 forces de Porter (1985)</h3>
  <div class="key-box">
    <strong>5 forces de Porter</strong> — Outil fondamental pour analyser l'intensité concurrentielle d'un secteur :
    <ul>
      <li><strong>Rivalité dans le secteur</strong> (concurrence existante)</li>
      <li><strong>Menace des entrants potentiels</strong> (et hauteur des barrières à l'entrée/sortie)</li>
      <li><strong>Menace des substituts</strong></li>
      <li><strong>Pouvoir de négociation des clients</strong></li>
      <li><strong>Pouvoir de négociation des fournisseurs</strong></li>
    </ul>
    Souvent complété par une 6e force : la <strong>démographie / pouvoirs publics</strong>.
  </div>
  <div class="example-box">
    <strong>Cas SNCF : « Notre plus gros concurrent, c'est Google ! »</strong><br>
    Pourquoi le dirigeant de la SNCF affirme-t-il cela ? Parce que le modèle des 5 forces ne montre pas la <strong>désintermédiation par les plateformes</strong> : Google capte les recherches « voyage en ligne », transformant la chaîne de valeur. Les fournisseurs de la SNCF sont peu nombreux (intégration verticale en amont), mais sa place dans le monde du « voyage en ligne » est menacée par des acteurs hors-secteur.
  </div>

  <h3>L'écosystème d'affaires (ESA), une notion-clé</h3>
  <div class="def-box">
    <div class="def-label">Écosystème d'affaires — définition</div>
    <p>Dans le vocabulaire du management stratégique, un <strong>écosystème est une communauté d'intérêts</strong>, constituée d'organisations issues de secteurs différents et co-produisant une prestation. Cet ensemble est piloté par une ou plusieurs entreprises.</p>
    <p>C'est une nouvelle façon pour l'entreprise de penser son environnement stratégique : <strong>envisager son environnement au-delà de son secteur ou sa filière</strong> (qui sont les acteurs et les « règles du jeu » dont on doit tenir compte ?).</p>
  </div>
  <div class="key-box">
    <strong>Une communauté économique caractérisée par :</strong>
    <ul>
      <li>Des interactions entre des entreprises et d'autres types d'acteurs (fournisseurs, producteurs, concurrents, clients et autres parties prenantes)</li>
      <li>Un apport mutuel de compétences</li>
      <li>Des acteurs évoluant vers une direction commune, définie par les acteurs centraux (voire 1 seul)</li>
      <li>Des relations de <strong>coopétition</strong> entre les membres (coopération + compétition simultanées)</li>
    </ul>
  </div>

  <h3>L'importance des mouvements concurrentiels</h3>
  <p>En matière de stratégie, il faut garder à l'esprit qu'il y a une <strong>interaction dynamique</strong> entre l'entreprise considérée et ses adversaires. Les choix stratégiques d'une entreprise A en t1 sont contraints par les choix des entreprises rivales en t0, mais ces dernières seront amenées en t2 à intégrer dans leurs décisions les choix de l'entreprise A.</p>
  <p>Historiquement, la littérature s'est d'abord focalisée sur le <em>résultat</em> (positions concurrentielles, école du positionnement de Porter). Depuis quelques années, on voit se développer de nombreux travaux qui s'intéressent davantage au <em>processus</em> (mouvements concurrentiels), reconnaissant au concurrent une capacité plus ou moins forte à contrecarrer les initiatives.</p>
</div>

<div class="course-chapter" data-theme="concurrentielle" data-chap-idx="10" id="chap-10">
  <h2>10. Partie 2 — Le triangle des registres relationnels (Koenig, 2004)</h2>
  <div class="def-box">
    <div class="def-label">3 logiques relationnelles fondamentales</div>
    <p>Selon Koenig (2004), les relations entre entreprises s'organisent selon <strong>3 logiques</strong>, avec une multitude de situations intermédiaires :</p>
    <table class="comp-table">
      <thead><tr><th>Logique</th><th>Registre</th><th>Mécanisme</th></tr></thead>
      <tbody>
        <tr><td><strong>Affrontement</strong></td><td>1. Concurrence</td><td>Recherche d'un avantage par déstabilisation de l'adversaire</td></tr>
        <tr><td><strong>Coopération</strong></td><td>2. Alliance</td><td>Association entre concurrents pour un projet/activité spécifique</td></tr>
        <tr><td><strong>Évitement</strong></td><td>3. Entente</td><td>Limitation tacite ou formalisée de la rivalité</td></tr>
      </tbody>
    </table>
  </div>
  <div class="key-box">
    <strong>Plan de la 2e partie</strong> — la suite du cours déroule ces 3 registres :
    <ul>
      <li><strong>1. La concurrence</strong> : mouvements simples (offensifs radicaux, contrôle des ressources, défensifs) et complexes (collectifs, multipoints)</li>
      <li><strong>2. Les alliances</strong> : facteurs explicatifs + 3 types (complémentaire, co-intégration, pseudo-concentration)</li>
      <li><strong>3. Les ententes</strong> : incitations + 4 formes (Baumard 2000)</li>
    </ul>
  </div>
</div>

<div class="course-chapter" data-theme="concurrentielle" data-chap-idx="11" id="chap-11">
  <h2>11. Partie 2 — Mouvements concurrentiels simples</h2>
  <h3>① Les mouvements offensifs radicaux</h3>
  <p>Trois mouvements offensifs typiques permettent de gérer le conflit avec les concurrents :</p>

  <h4>Les guerres de prix</h4>
  <div class="key-box">
    Elles <strong>détruisent les marges</strong>, anéantissent la loyauté du consommateur, ralentissent l'innovation. Elles nécessitent le plus souvent de disposer de <strong>capacités importantes</strong> pour jouer sur les « effets volumes » et pouvoir supporter le choc financier.
  </div>
  <div class="example-box">
    <strong>Cas Bonduelle (1990s)</strong> — La conserve de légumes en France était un oligopole avec 4 acteurs principaux (Bonduelle, Cecab, Avril, Boutet-Nicolas). Bonduelle se lance dans une stratégie de développement de sa capacité de production par croissances interne et externe, puis profite des asymétries de capacités pour déclencher une <strong>guerre de prix de 1993 à 1999</strong>. Au terme de la guerre : Avril est racheté par Bonduelle, Boutet-Nicolas par Cecab. Le secteur devient un duopole, les deux survivants remontent considérablement les prix. <em>(Source : Le Roy, AIMS, 2004)</em>
  </div>
  <div class="example-box">
    <strong>Cas Delta vs Qantas (février 2025)</strong> — Delta Airlines annonce un service direct Melbourne–Los Angeles avec des tarifs dès 867 $ aller-retour, clairement positionnés pour concurrencer Qantas. Mécanique : Delta propose des prix très agressifs → Qantas est forcée de réagir (alignement ou avantages supplémentaires) → Qantas lance des promotions massives (1 199 à 1 799 $) → Virgin Australia doit aussi ajuster (+10 % de passagers entre Australie et États-Unis).
  </div>

  <h4>Les stratégies de prolifération</h4>
  <div class="key-box">
    Elles consistent à <strong>inonder un marché de produits, de marques ou d'informations</strong> pour faire obstacle à la concurrence. Elles nécessitent un <strong>pouvoir de négociation élevé</strong> sur les circuits de distribution et de communication.
  </div>
  <div class="example-box">
    <strong>Cas céréales pour petit-déjeuner</strong> — Marché oligopolistique dominé par Kellogg's et Nestlé (60 % des ventes en valeur) suivis par Quaker et Jordans. Les membres protègent leurs positions par une <strong>hypersegmentation associée à une prolifération</strong> de produits, sous-marques et licences (Disney…). Seules les MDD ont vraiment réussi à pénétrer le marché (PDM moyenne en volume de 20-22 %).
  </div>

  <h4>Les stratégies de préemption</h4>
  <div class="key-box">
    Il s'agit de <strong>prendre ou revendiquer un marché</strong> avant que celui-ci ne soit convoité ou complètement bloqué par des concurrents.
  </div>
  <div class="example-box">
    <strong>Cas L'Équipe vs Le 10 Sport (2008-2009)</strong> — L'Équipe (Groupe Amaury) bénéficie d'un monopole de plus de 20 ans. Le 3 novembre 2008, lancement du « 10 Sport » sur le créneau de la presse « low cost ». Le même jour, le groupe Amaury contre-attaque avec « Aujourd'hui Sport » : même format (tabloïd), même positionnement (football), même prix (0,50 €). En moins de 5 mois, le nouvel entrant est écarté. Le 30 juin 2009, Amaury cesse la parution d'« Aujourd'hui Sport ». L'Équipe retrouve sa position de monopole.
  </div>
  <div class="example-box">
    <strong>Cas Amazon — préemption logistique urbaine (2020-2023)</strong> — Avec l'explosion du e-commerce et la promesse de livraisons rapides, la logistique urbaine devient un avantage stratégique clé. Amazon mène une politique massive d'<strong>acquisition ou location longue durée d'entrepôts et de hubs logistiques</strong>, avant même que la concurrence (Carrefour, Walmart, etc.) n'ait le temps de réagir. Elle réserve des espaces en centre-ville, en périphérie, dans des friches, parfois sans les utiliser immédiatement (occupation préventive). Résultat : Cdiscount, Fnac-Darty, La Poste se retrouvent face à une pénurie ; Amazon devient quasi-incontournable.
  </div>

  <h3>② Les manœuvres de contrôle des ressources</h3>
  <div class="def-box">
    <div class="def-label">Actif critique</div>
    <p>Une immobilisation corporelle ou incorporelle <strong>nécessaire à l'entrée sur un marché</strong> ou au contrôle d'une activité, et qui ne connaît <strong>ni substitut, ni possibilité d'échange, ni possibilité d'imitation</strong>. L'objectif est d'amasser le plus rapidement possible des actifs nécessaires au développement des concurrents.</p>
  </div>
  <div class="def-box">
    <div class="def-label">Actif spécialisé</div>
    <p>Il s'agit de <strong>« verrouiller » le marché par un contrôle sur des actifs qui jouent un rôle prépondérant</strong> et qui représentent un coût d'entrée sur le marché : actifs tangibles, savoir-faire, clientèle. <em>(Source : Baumard, 2000)</em></p>
    <p><strong>L'enjeu consiste à concevoir un business model autour de ces actifs.</strong></p>
  </div>
  <h4>Exemples de verrouillage par contrôle d'actifs (modèle « rasoir / lame »)</h4>
  <table class="comp-table">
    <thead><tr><th>Secteur</th><th>Dispositif principal (« rasoir »)</th><th>Consommable / service (« lame »)</th><th>Verrouillage</th></tr></thead>
    <tbody>
      <tr><td>Smartphones</td><td>Appareil</td><td>Contenu numérique</td><td>Écosystème fermé</td></tr>
      <tr><td>Bornes EV</td><td>Infrastructure</td><td>Énergie, data</td><td>Emplacement, abonnement</td></tr>
      <tr><td>Brosses à dents électriques</td><td>Manche</td><td>Têtes de brosse</td><td>Format propriétaire</td></tr>
      <tr><td>Imprimante 3D</td><td>Imprimante 3D</td><td>Filaments / résines propriétaires</td><td>Restrictions brevets, compatibilité</td></tr>
    </tbody>
  </table>
  <div class="example-box">
    <strong>Cas G7 Taxis Paris</strong> — Jusqu'en 2012, le groupe G7 contrôle près des <strong>2/3 des taxis parisiens (11 000 sur 17 000)</strong> avec 2 sociétés : Taxis G7 et Taxis Bleus. Le métier nécessite une licence (prise en charge à la volée, accès aux bornes, voies de bus). Nouvelles attributions quasi-inexistantes → marché secondaire géré par le syndicat. G7 détient aussi location de licences, équipements, assurances, école de taxi. <strong>Uber va perturber ce marché en contournant, par l'innovation technologique, les barrières à l'entrée.</strong>
  </div>

  <h3>③ Les mouvements défensifs individuels</h3>

  <h4>La défense par rétorsion</h4>
  <div class="key-box">
    L'éventail des mesures est très large : prix cassés, procès, intégration verticale, blocage des circuits de distribution. Les firmes recherchent plus souvent des <strong>moyens dissuasifs et indirects</strong> avant d'avoir recours à des représailles frontales dont l'issue est incertaine et les coûts importants.
  </div>
  <div class="example-box">
    <strong>Cas Continental Airlines vs America West (fin 1980s)</strong> — Stratagème « Assiéger Wei pour sauver Zhao » : America West propose des vols Houston bon marché. Continental Airlines (dominant à Houston) <strong>riposte en cassant les prix sur Phoenix</strong> (cœur du système America West) avec un code de prix dans son système de réservation montrant clairement qu'il s'agit d'une réponse. America West supprime ses prix cassés. Continental fait de même. <em>(Source : Koenig 1996)</em>
  </div>

  <h4>La défense par dispersion et dépréciation</h4>
  <div class="key-box">
    Une firme en forte vulnérabilité (pas de capacité défensive effective) va tenter de <strong>retirer au « prédateur » la motivation même de son offensive</strong>. C'est le « stratagème de la ville vide » ou des « batailles presque perdues ».
  </div>
  <div class="example-box">
    <strong>Cas Hermès vs LVMH (2010-2014)</strong> — En 2010, LVMH annonce 17,1 % du capital d'Hermès via produits financiers complexes. Hermès, plus petit, ne peut s'opposer frontalement. <strong>Réponse défensive sophistiquée</strong> :<br>
    ① <strong>Création d'un holding familial défensif</strong> : la famille fonde une holding regroupant plus de 50 % du capital ; pacte interdisant la vente pendant 20 ans → toute prise de contrôle hostile devient impossible.<br>
    ② <strong>Communication subtile mais ferme</strong> : « Nous sommes très calmes. Cela ne change rien à notre stratégie » (Axel Dumas). Posture typique du stratagème de la ville vide : calme apparent, forteresse interne consolidée.<br>
    <strong>Résultat</strong> : LVMH se retire du capital d'Hermès (2014). Hermès préserve son indépendance.
  </div>
</div>

<div class="course-chapter" data-theme="concurrentielle" data-chap-idx="12" id="chap-12">
  <h2>12. Partie 2 — Mouvements concurrentiels complexes</h2>

  <h3>① Les mouvements offensifs collectifs</h3>
  <div class="example-box">
    <strong>Cas tabac américain (années 1930)</strong> — Les grands fabricants de tabac américains attaquent les fabricants de cigarettes très bon marché (PDM des perturbateurs montée à 17 %). Stratégie collective brutale :
    <ul>
      <li>2 baisses coordonnées des prix pour obtenir un écart d'au moins 3 cents sur les perturbateurs</li>
      <li>Distributeurs forcés de coopérer sous menace de sanctions (ruptures de livraison)</li>
      <li>De très grandes quantités de tabac rachetées en amont puis détruites pour empêcher les outsiders d'accéder à des ressources bon marché</li>
    </ul>
    La part de marché des outsiders chute rapidement à 6 %. Une fois « l'ennemi » affaibli, les oligopoleurs remontent unanimement leurs prix → comblent en un an les pertes engendrées par la guerre de prix.
  </div>

  <h3>② Les mouvements défensifs collectifs</h3>
  <div class="key-box">
    Dans certains secteurs (oligopoles notamment), les entreprises développent des stratégies de <strong>« bouclier commun »</strong> pour inverser le rapport de force initialement favorable à l'attaquant. Ces stratégies se matérialisent en une rétorsion commune menée par les alliés (prix cassés, dénonciation médiatique) ou en un ensemble de rétorsions coordonnées en amont et en aval de la chaîne de valeur.
  </div>
  <div class="example-box">
    <strong>Cas Amazon Marketplace (2000-2010)</strong> — Stratégie : <em>« faire travailler les ennemis pour soi »</em>. Amazon invite des milliers de vendeurs indépendants (marques, distributeurs, artisans, voire concurrents) à vendre sur sa plateforme. Ces vendeurs enrichissent l'offre, attirent des millions de clients et génèrent des données précieuses. <strong>Objectif</strong> : analyser les données pour repérer les produits les plus rentables et lancer ses propres marques (Amazon Basics). Résultat : Amazon devient n°1 du e-commerce, ses marques maison dominent certains segments, certains vendeurs sont évincés après avoir révélé malgré eux les niches profitables.
  </div>
  <div class="example-box">
    <strong>Cas compagnies aériennes traditionnelles vs low-cost (années 2000)</strong> — Ryanair et easyJet pénètrent massivement le marché européen, menace directe pour Air France, Lufthansa, British Airways. <strong>Bouclier commun oligopolistique</strong> :<br>
    ① <strong>Lancement de filiales low-cost</strong> par les majors (Transavia, Germanwings) : protéger le cœur tout en menant une guerre tarifaire sur un périmètre limité.<br>
    ② <strong>Coordination informelle</strong> sur certaines lignes court-courrier : prix drastiquement réduits (même à perte) de façon quasi-synchronisée.<br>
    ③ <strong>Pression sur les fournisseurs/partenaires</strong> (aéroports principaux, agences, créneaux horaires) pour limiter l'accès aux low-cost. Lobbying commun (sécurité, droits passagers).<br>
    <strong>Résultat</strong> : la pénétration du low-cost est freinée sur certains segments. Les majors conservent leur domination sur les long-courriers et lignes business-clés.
  </div>

  <h3>③ La concurrence multipoints</h3>
  <div class="def-box">
    <div class="def-label">Concurrence multipoints</div>
    <p>Situations dans lesquelles des firmes sont en concurrence plus ou moins frontale sur <strong>plusieurs couples produits-marchés</strong>. On peut observer des comportements d'attaque mais aussi de <strong>tolérance mutuelle</strong> (par exemple des pactes de non-agression). Les situations multipoints sont propices à l'élaboration de <strong>ripostes décalées</strong>.</p>
  </div>
  <div class="example-box">
    <strong>Cas Gillette vs Bic (1975-1992)</strong> — Un cas d'école de concurrence multipoints :
    <ol>
      <li><strong>1975</strong> : Bic entre massivement sur les rasoirs jetables.</li>
      <li>Gillette répond en lançant ses propres rasoirs jetables → consomme des ressources et <strong>cannibalise</strong> sa ligne de rasoirs sophistiqués.</li>
      <li><strong>1985</strong> : situation intenable. Gillette développe alors une stratégie de <strong>« feinte » sur les briquets</strong>.</li>
      <li>Bic, obligé de réagir, mobilise l'essentiel de ses ressources sur les briquets → fragilise son activité rasoirs.</li>
      <li><strong>1987</strong> : Gillette récupère sa position de force sur les rasoirs et « sacrifie » son activité briquet. Bic reprend sa position de leader sur les briquets.</li>
      <li><strong>1992</strong> : Gillette consolide son activité rasoirs (R&amp;D + lancement du Sensor).</li>
    </ol>
    <em>(Source : McGrath et al., 1998, p. 733)</em>
  </div>
  <div class="example-box">
    <strong>Cas Coca-Cola vs Pepsi — un match sans fin</strong> — Concurrence directe sur plusieurs marchés : sodas (Coca/Pepsi), boissons non gazeuses (Minute Maid/Tropicana), eaux (Dasani/Aquafina), snacking (Lay's PepsiCo / Smartfood Coca-Cola), dans plus de 200 pays.<br>
    ① <strong>Ripostes différées</strong> : Pepsi attaque les sodas en Inde → Coca ne riposte pas immédiatement mais intensifie sa présence sur les jus/eaux dans le même pays.<br>
    ② <strong>Tolérance mutuelle implicite</strong> : dans certains pays émergents instables (Venezuela, Pakistan), les deux groupes ont parfois stabilisé leurs efforts marketing → forme de pacte de non-agression implicite.<br>
    ③ <strong>Imitation stratégique à bas bruit</strong> : Coca copie Pepsi (mini-canettes, éditions personnalisées) et vice-versa.<br>
    <strong>Résultat</strong> : « guerre froide » permanente avec poussées ponctuelles (Cola War des années 80), mais globalement stabilité gérée grâce à la conscience multipoints.
  </div>
</div>

<div class="course-chapter" data-theme="concurrentielle" data-chap-idx="13" id="chap-13">
  <h2>13. Partie 2 — Les alliances</h2>

  <div class="def-box">
    <div class="def-label">Alliance — définition</div>
    <p><strong>Associations entre plusieurs entreprises concurrentes</strong> qui choisissent de mener à bien un <strong>projet ou une activité spécifique</strong> en coordonnant les compétences, moyens et ressources nécessaires.</p>
    <p>3 caractéristiques principales :</p>
    <ul>
      <li>Ce sont des <strong>centres de décision multiples</strong>…</li>
      <li>… qui relèvent de la <strong>négociation permanente</strong>…</li>
      <li>… et qui <strong>n'évitent pas toujours les conflits d'intérêts</strong>.</li>
    </ul>
  </div>

  <h3>Facteurs explicatifs du recours à l'alliance</h3>
  <div class="key-box">
    <strong>4 avantages génériques</strong> (Strategor, 2024) :
    <ul>
      <li><strong>Obtention d'économies d'échelle</strong></li>
      <li><strong>Combinaison de ressources complémentaires</strong></li>
      <li><strong>Possibilité d'apprentissage et/ou de transfert de compétences</strong></li>
      <li><strong>Protection contre les concurrents les plus puissants</strong></li>
    </ul>
    <strong>2 avantages originaux par rapport aux options stratégiques classiques :</strong>
    <ul>
      <li><strong>L'autonomie conservée</strong></li>
      <li><strong>La réversibilité toujours possible</strong></li>
    </ul>
  </div>

  <h3>Les 3 types d'alliances</h3>
  <table class="comp-table">
    <thead><tr><th></th><th>Actifs / compétences apportés</th><th>Output de l'alliance</th></tr></thead>
    <tbody>
      <tr><td><strong>Alliance complémentaire</strong></td><td>Différents</td><td>Produits spécifiques à chaque allié</td></tr>
      <tr><td><strong>Alliance de co-intégration</strong></td><td>Similaires</td><td>Un même composant commun intégré dans les offres respectives</td></tr>
      <tr><td><strong>Alliance de pseudo-concentration</strong></td><td>Similaires</td><td>Un même produit commun commercialisé en commun</td></tr>
    </tbody>
  </table>

  <h4>① L'alliance complémentaire</h4>
  <div class="key-box">
    <strong>Forme générique</strong> : sur un marché où elle est déjà implantée, une firme fabrique et/ou commercialise un produit initialement développé par une entreprise concurrente.<br>
    <strong>Objectif principal</strong> : exploiter la complémentarité des apports en évitant un investissement supplémentaire pour chaque partenaire.<br>
    <strong>Organisation</strong> : chaque allié effectue les tâches liées aux actifs et compétences qu'il maîtrise.
  </div>
  <div class="example-box">
    <strong>Exemples</strong> : Apple-Samsung (écrans smartphones).<br>
    <strong>Cas Sanofi &amp; GSK COVID-19 (2020)</strong> — Alliance complémentaire pour développer un vaccin anti-COVID. Sanofi apporte l'antigène (principe actif), GSK fournit l'adjuvant (améliore la réponse immunitaire). Objectifs : mutualiser les forces tout en restant concurrents sur d'autres traitements, aller plus vite et réduire les coûts R&amp;D dans un contexte d'urgence.
  </div>

  <h4>② L'alliance de co-intégration</h4>
  <div class="key-box">
    <strong>Forme générique</strong> : association de firmes concurrentes qui développent et/ou fabriquent un <strong>élément, un composant commun, voire un produit</strong>, qui sera intégré dans leurs offres respectives.<br>
    <strong>Objectif principal</strong> : atteindre la taille critique sur une fonction ou un composant sans faire appel à un fournisseur extérieur.<br>
    <strong>Organisation</strong> : répartition des travaux de R&amp;D entre les alliés et/ou fabrication dans une usine commune.
  </div>
  <div class="example-box">
    <strong>Exemples</strong> : moteur V6 PRV (PSA / Fiat / Renault), 806/Évasion/Ulysse (Citroën, Peugeot, Fiat), C1/Aygo/107 (Citroën-Toyota-Peugeot dans la même usine tchèque avec 3 positionnements différents : Toyota cible « 25-35 ans citadins », Peugeot mise sur la malice/ludique pour foyers multimotorisés, Citroën interpelle ceux qui ne mettent pas tout leur argent dans leur voiture).<br>
    <strong>Cas BMW &amp; Mercedes-Benz (2019)</strong> — Deux concurrents historiques fusionnent leurs services d'autopartage, VTC et stationnement dans une joint-venture 50/50, investissant 1 Md€. Objectif : lutter contre Uber, Lyft ou Google dans la mobilité urbaine — domaine hors de leur cœur de métier automobile, mais crucial. Chacun conserve son activité principale (voitures) tout en unissant ses efforts dans un secteur complémentaire.
  </div>

  <h4>③ L'alliance de pseudo-concentration</h4>
  <div class="key-box">
    <strong>Forme générique</strong> : consortium d'entreprises concurrentes qui développe, fabrique et commercialise un <strong>produit commun</strong>.<br>
    <strong>Objectif principal</strong> : <strong>atteindre la taille critique en évitant la concentration</strong>.<br>
    <strong>Organisation</strong> : projet en coopération découpé en sous-ensembles dont le développement et la production sont répartis entre alliés.
  </div>
  <div class="example-box">
    <strong>Exemples</strong> : Concorde, Airbus, Eurocopter.<br>
    <strong>Cas Thalès – Hitachi – CAF – Alstom</strong> — Les 4 entreprises ont formé plusieurs consortiums pour répondre à des appels d'offres publics (ex. lignes TGV, métros automatiques). Exemples : métro automatique Grand Paris Express (ligne 15), projet SNCF des postes d'aiguillage du futur. Objectif : mutualiser les expertises (signalisation, matériel roulant, contrôle-commande) pour remporter des marchés géants sans fusionner, partager coûts/risques/responsabilités. Chacun prend en charge une partie du projet (trains, signalisation, IT, essais).
  </div>
</div>

<div class="course-chapter" data-theme="concurrentielle" data-chap-idx="14" id="chap-14">
  <h2>14. Partie 2 — Les ententes</h2>

  <div class="def-box">
    <div class="def-label">Entente — définition</div>
    <p><strong>Association entre entreprises, de manière tacite ou formalisée, dans le but de restreindre le jeu de la concurrence.</strong></p>
    <p>L'entente a pour objectif ou pour effet de limiter l'intensité de la rivalité entre concurrents. Elle peut contribuer au bien-être collectif ou être contraire à l'intérêt de diverses parties prenantes. Les autorités de contrôle procèdent donc à un <strong>bilan économique des avantages et des inconvénients</strong>.</p>
  </div>

  <h3>Les incitations aux ententes</h3>
  <div class="key-box">
    Les <strong>5 incitations classiques</strong> sont :
    <ul>
      <li>Un <strong>fort degré de concentration</strong></li>
      <li>Une <strong>forte homogénéité du produit</strong></li>
      <li>Une <strong>inélasticité de la demande</strong> par rapport au prix</li>
      <li>Des <strong>coûts fixes importants</strong></li>
      <li>Des <strong>procédures d'appel d'offres</strong></li>
    </ul>
  </div>

  <h3>Les 4 formes génériques d'ententes (Baumard, 2000)</h3>
  <p>Les manœuvres de limitation de la concurrence peuvent être <em>légitimes</em> car elles ne traduisent pas systématiquement une volonté d'entrave. La limitation peut avoir des origines diverses (standard technique commun, pression de clients puissants) et être « spontanée » (oligopoles) ou « orchestrée ».</p>
  <table class="comp-table">
    <thead><tr><th></th><th>Émergentes</th><th>Délibérées</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>Légitimes</strong></td>
        <td><strong>① Limitation naturelle</strong><br>Les prix, comportements, investissements paraissent concertés mais répondent en fait à une variable explicative commune étrangère à la volonté des acteurs.</td>
        <td><strong>② Limitation contrainte</strong><br>Les coalitions sont tolérées par les autorités lorsqu'elles permettent le « développement du progrès économique ».</td>
      </tr>
      <tr>
        <td><strong>Illégitimes</strong></td>
        <td><strong>③ Limitation de coordination</strong><br>Coordination tacite, aucune trace d'accord recueillie. La volonté de fausser le jeu concurrentiel est néanmoins considérée par les autorités. <em>(sanctuaires)</em></td>
        <td><strong>④ Limitation déloyale</strong><br>Volonté commune des parties d'entraver la concurrence par des comportements coordonnés, des interdictions d'accès au marché, des pratiques de prix discriminatoires. <em>(cartels)</em></td>
      </tr>
    </tbody>
  </table>

  <h3>Cas emblématiques</h3>
  <div class="example-box">
    <strong>Cartel des palaces parisiens (2005)</strong> — Le Conseil de la Concurrence condamne 6 prestigieux palaces (Bristol, Crillon, George V, Meurice, Plaza Athénée, Ritz) à des amendes de 55 000 à 248 000 €. L'enquête a montré un système d'échange régulier (mails, réunions) sur « des informations commerciales confidentielles » et sur « des éléments nécessaires à l'élaboration de leurs plans marketing ». Ces échanges ont permis qu'aucun de ces hôtels ne cherche à s'engager dans des stratégies remettant en cause les positions des autres membres de l'oligopole.
  </div>
  <div class="example-box">
    <strong>Limitation de coordination par sanctuaires : Airbus A340 (1998)</strong> — Airbus lance un appel d'offres sur la motorisation de la version allongée de l'A340. General Electric déclare « qu'elle n'a rien à proposer à Airbus ». Pratt &amp; Whitney annonce qu'elle ne répondra pas si Rolls Royce et GE sont sur les rangs. La voie est libre pour Rolls Royce. Peu après, Pratt &amp; Whitney annonce qu'elle va développer avec General Electric un moteur pour fournir Airbus sur ses projets futurs de très gros porteurs. <em>(Source : Baumard, 2000, p. 185-186)</em>
  </div>

  <h3>Autres ententes emblématiques sanctionnées</h3>
  <table class="comp-table">
    <thead><tr><th>Année</th><th>Secteur</th><th>Sanction</th></tr></thead>
    <tbody>
      <tr><td>2005</td><td>3 opérateurs de téléphonie mobile (Orange/SFR/Bouygues)</td><td>534 M€ (256 / 220 / 58)</td></tr>
      <tr><td>2006</td><td>13 grandes marques de parfumerie + 3 distributeurs (entente verticale)</td><td>46,2 M€</td></tr>
      <tr><td>2008</td><td>11 entreprises du négoce de produits sidérurgiques + FDDM (ArcelorMittal en tête)</td><td>575,4 M€ (dont 301,7 ArcelorMittal)</td></tr>
      <tr><td>2011</td><td>Géants des lessives (Colgate-Palmolive, Henkel, Unilever, P&amp;G)</td><td>368 M€ + 951 M€ pour produits d'hygiène (L'Oréal…)</td></tr>
      <tr><td>2014</td><td>5 entreprises EU/JP — roulements automobiles</td><td>953 M€ (Commission EU)</td></tr>
      <tr><td>2018</td><td>6 marques d'électroménager (Bosch, Siemens, Candy, Liebherr, Electrolux, Indesit, Whirlpool — 70 % du marché)</td><td>189 M€</td></tr>
      <tr><td>2021</td><td>3 fabricants français de sandwichs MDD (entre 2010 et 2016)</td><td>Sanction Autorité de la concurrence</td></tr>
      <tr><td>2025</td><td>15 constructeurs automobiles + ACEA (recyclage VHU)</td><td>458 M€ (Commission EU)</td></tr>
    </tbody>
  </table>
</div>

<div class="course-chapter" data-theme="concurrentielle" data-chap-idx="15" id="chap-15">
  <h2>15. Partie 2 — Synthèse et points-clés</h2>
  <div class="key-box">
    <strong>3 logiques relationnelles structurent l'interaction concurrentielle</strong> (Koenig, 2004) :
    <ol>
      <li><strong>Affrontement → Concurrence</strong> : mouvements simples (offensifs : prix, prolifération, préemption ; contrôle des ressources ; défensifs : rétorsion, ville vide) et complexes (offensifs/défensifs collectifs, multipoints)</li>
      <li><strong>Coopération → Alliances</strong> : 3 types (complémentaire, co-intégration, pseudo-concentration)</li>
      <li><strong>Évitement → Ententes</strong> : 4 formes (Baumard 2000) — légitimes (naturelle, contrainte) ou illégitimes (coordination/sanctuaires, déloyale/cartels)</li>
    </ol>
  </div>
  <div class="key-box">
    <strong>Concepts transversaux à retenir</strong> :
    <ul>
      <li><strong>Écosystème d'affaires (ESA)</strong> : communauté d'intérêts inter-secteurs, pilotée par 1 ou plusieurs acteurs, avec relations de coopétition</li>
      <li><strong>Coopétition</strong> : coopération + compétition simultanées</li>
      <li><strong>Actif critique vs actif spécialisé</strong> (Baumard 2000) : verrouillage du marché par le contrôle des ressources rares</li>
      <li><strong>Stratagème de la ville vide</strong> : posture défensive en situation de vulnérabilité (Hermès vs LVMH)</li>
      <li><strong>Concurrence multipoints</strong> : interactions sur plusieurs couples produits-marchés → ripostes décalées et tolérance implicite</li>
    </ul>
  </div>
</div>

<div class="course-chapter" data-theme="concurrentielle" data-chap-idx="16" id="chap-16">
  <h2>16. Partie 2 — Tableau récapitulatif des 5 forces de Porter et leurs limites</h2>
  <p>Le modèle des 5 forces de Porter (1985) reste l'outil de référence pour analyser l'intensité concurrentielle, mais il <strong>ne suffit plus</strong> dans un environnement marqué par l'effondrement des frontières sectorielles.</p>
  <table class="comp-table">
    <thead><tr><th>Force</th><th>Indicateur d'intensité</th><th>Limite</th></tr></thead>
    <tbody>
      <tr><td>Rivalité entre concurrents</td><td>Nombre, taille, différenciation, croissance du marché</td><td>Ignore les concurrents hors-secteur (ex. Google vs SNCF)</td></tr>
      <tr><td>Menace des entrants</td><td>Hauteur des barrières à l'entrée (capital, brevets, réseau)</td><td>Sous-estime la disruption technologique (Uber vs G7)</td></tr>
      <tr><td>Menace des substituts</td><td>Performance/prix, propension à changer</td><td>Difficulté à anticiper les substituts radicaux (smartphone vs appareil photo)</td></tr>
      <tr><td>Pouvoir clients</td><td>Concentration, sensibilité prix, coût de switch</td><td>Ignore les communautés et les effets de réseau côté demande</td></tr>
      <tr><td>Pouvoir fournisseurs</td><td>Concentration, intégration verticale possible</td><td>Ignore les plateformes qui inversent le rapport de force</td></tr>
      <tr><td><em>(6e force)</em> Démographie / pouvoirs publics</td><td>Régulation, démographie, lobbying</td><td>—</td></tr>
    </tbody>
  </table>
  <div class="example-box">
    <strong>D'où la nécessité de mobiliser l'écosystème d'affaires (ESA)</strong> et l'analyse des mouvements concurrentiels en complément du modèle de Porter pour appréhender les enjeux contemporains.
  </div>
</div>

<div class="course-chapter" data-theme="corporate" data-chap-idx="17" id="chap-17">
  <h2>17. Partie 3 — Pourquoi la gouvernance est-elle devenue une question stratégique ?</h2>

  <div class="def-box">
    <div class="def-label">Entreprise — définition</div>
    <p><strong>Système de coopération établi entre divers partenaires apporteurs de ressources</strong> dont le but commun est de faire produire à l'entreprise de la richesse (un surplus par rapport aux ressources consommées). <em>(Strategor, 2009, p. 633-654)</em></p>
  </div>

  <div class="def-box">
    <div class="def-label">Gouvernance d'entreprise — objet</div>
    <p>La gouvernance d'entreprise a pour objet de <strong>définir les organes et les mécanismes qui fixent les droits et obligations des différentes parties prenantes</strong> afin de maximiser la valeur créée et d'assurer sa répartition équitable.</p>
    <p>Pour attirer les partenaires et garantir la pérennité de l'entreprise, il convient de leur offrir une rémunération « satisfaisante » compte tenu de leurs objectifs et des risques qu'ils prennent.</p>
  </div>

  <h3>Évolution historique de la gouvernance</h3>
  <div class="key-box">
    <strong>① Gouvernance familiale</strong> (jusqu'à la fin du 19e siècle)<br>
    La propriété de la firme reste dans les mains de familles, les <strong>« dynasties industrielles »</strong> : Krupp, de Dietrich, Schneider…
  </div>
  <div class="key-box">
    <strong>② Gouvernance managériale</strong> (à partir du 20e siècle)<br>
    Les besoins en capitaux obligent les propriétaires à <strong>ouvrir le capital</strong>, d'où une dissociation de plus en plus forte de la propriété et de la gestion.
    <ul>
      <li>L'actionnaire devient un <strong>« propriétaire sans contrôle »</strong>.</li>
      <li>Le dirigeant devient un <strong>« manager professionnel »</strong>, compétent mais dont les intérêts ne sont pas toujours convergents avec ceux des propriétaires.</li>
    </ul>
  </div>
  <div class="key-box">
    <strong>③ Gouvernance actionnariale</strong> (à partir du milieu des années 1980)<br>
    Grand retour des actionnaires, dû notamment à :
    <ul>
      <li>La <strong>multiplication des opérations douteuses et grands scandales</strong> posant la question du contrôle des dirigeants (Enron…)</li>
      <li>La <strong>montée en puissance des fonds de pension</strong> et autres investisseurs institutionnels (OPCVM, banques, assurances) ayant un fort pouvoir de négociation et dotés de compétences financières</li>
    </ul>
  </div>
  <div class="example-box">
    <strong>Pouvoir et contrôle des dirigeants — Affaire EADS Airbus A380</strong> — En 2006, des dirigeants d'EADS ont vendu leurs actions peu avant l'annonce du retard de livraison de l'Airbus A380. Étaient-ils au courant ? Affaire emblématique des dérives de la gouvernance managériale et de la nécessité de contrôler les dirigeants.
  </div>
</div>

<div class="course-chapter" data-theme="corporate" data-chap-idx="18" id="chap-18">
  <h2>18. Partie 3 — Les acteurs financiers et leur influence</h2>

  <h3>Les fonds de pension</h3>
  <div class="def-box">
    <div class="def-label">Fonds de pension</div>
    <p>Caisses de retraite privées qui <strong>collectent l'épargne des salariés tout au long de leur vie active, la placent et leur reversent sous forme de rente</strong> lorsqu'ils sont en retraite.</p>
    <p>Les fonds de pension anglo-saxons, qui <strong>détiendraient 40 % du capital des entreprises du CAC 40</strong>, ont des <strong>exigences de rentabilité très élevées</strong>.</p>
    <p><em>Exemples : CalPers, CalTech…</em></p>
  </div>

  <h3>Les fonds d'investissement (private equity)</h3>
  <div class="key-box">
    Les fonds d'investissement ont pour objectif d'<strong>investir dans des sociétés sélectionnées</strong>. Ils sont spécialisés suivant l'objectif de leur intervention (stades différents de maturité) :
    <ul>
      <li><strong>Fonds de capital-risque</strong></li>
      <li><strong>Fonds de capital développement</strong> : devenir actionnaires d'entreprises en forte croissance avec des besoins de financement élevés sous forme de capitaux propres</li>
      <li><strong>Fonds de LBO</strong> : investissent dans des entreprises cédées par un groupe qui se recentre, par une famille (succession), ou pour aider la croissance externe. Ils <strong>financent leurs acquisitions par une bonne part de dettes</strong> et ont une préférence très nette pour disposer du contrôle exclusif compte tenu du risque important.</li>
    </ul>
  </div>

  <h3>Les fonds activistes</h3>
  <div class="def-box">
    <div class="def-label">Fonds activistes</div>
    <p>Ils cherchent à <strong>s'assurer que les buts des dirigeants coïncident avec les leurs</strong>. Généralement, ils mettent la pression sur des groupes peu performants, <strong>proposant des mesures correctives</strong> visant à améliorer leur valeur.</p>
  </div>
</div>

<div class="course-chapter" data-theme="corporate" data-chap-idx="19" id="chap-19">
  <h2>19. Partie 3 — Les parties prenantes</h2>

  <div class="def-box">
    <div class="def-label">Parties prenantes — définition</div>
    <p><strong>Acteurs qui participent au fonctionnement de l'entreprise parce qu'ils dépendent de celle-ci pour atteindre leurs propres objectifs.</strong></p>
  </div>

  <h3>3 types de parties prenantes</h3>
  <table class="comp-table">
    <thead><tr><th>Type</th><th>Exemples</th></tr></thead>
    <tbody>
      <tr><td><strong>Internes</strong></td><td>Directions d'activités (business units), comité d'entreprise, comité d'hygiène et de sécurité…</td></tr>
      <tr><td><strong>Interfaces</strong></td><td>Conseil d'administration, assemblée d'actionnaires, conseil de direction, syndicats…</td></tr>
      <tr><td><strong>Externes</strong></td><td>Fournisseurs, clients, distributeurs, banques, lobbies, collectivités territoriales, autorités de régulation…</td></tr>
    </tbody>
  </table>

  <h3>Divergences d'intérêts entre parties prenantes</h3>
  <div class="example-box">
    <strong>Exemples typiques de conflits</strong> :
    <ul>
      <li>Une nouvelle stratégie suppose l'émission de nouvelles actions → colère des actionnaires (dilution du pouvoir)</li>
      <li>Un projet de fusion avec un concurrent → inacceptable pour les syndicats (suppressions de postes)</li>
      <li>Un projet de vente par Internet → conflit avec les distributeurs traditionnels</li>
      <li>La privatisation d'une entreprise publique → conflit social (perte de statut)</li>
    </ul>
  </div>

  <h3>La matrice pouvoir / intérêt des parties prenantes (Johnson et al., 2005)</h3>
  <table class="comp-table">
    <thead><tr><th></th><th>Intérêt faible</th><th>Intérêt élevé</th></tr></thead>
    <tbody>
      <tr><td><strong>Pouvoir faible</strong></td><td>A — Effort minimal</td><td>B — À garder informés</td></tr>
      <tr><td><strong>Pouvoir élevé</strong></td><td>C — À garder satisfaits</td><td>D — <strong>Acteurs clés</strong></td></tr>
    </tbody>
  </table>
  <div class="key-box">
    <strong>Utilisation de la matrice</strong> :
    <ul>
      <li><strong>D (acteurs clés)</strong> : associer activement à la stratégie, dialogue intense</li>
      <li><strong>C (à garder satisfaits)</strong> : surveiller leurs attentes, anticiper leurs réactions</li>
      <li><strong>B (à garder informés)</strong> : communication régulière mais pas de décision conjointe</li>
      <li><strong>A (effort minimal)</strong> : information de base seulement</li>
    </ul>
  </div>
  <p><em>Source : Johnson et al., 2005, p. 218</em></p>

  <h3>Exemple : le conseil d'administration de Renault</h3>
  <div class="example-box">
    Le Conseil de Renault est composé de <strong>19 membres</strong> :
    <ul>
      <li>3 administrateurs élus par l'Assemblée générale des actionnaires</li>
      <li>2 administrateurs désignés par arrêté en qualité de représentants de l'État</li>
      <li>3 administrateurs élus par les salariés</li>
      <li>1 administrateur nommé sur proposition des actionnaires salariés</li>
      <li>(autres : administrateurs indépendants)</li>
    </ul>
    Conformément au <strong>code AFEP/MEDEF</strong>, un administrateur est considéré comme <strong>indépendant</strong> s'il « n'entretient aucune relation de quelque nature que ce soit avec la société, son groupe ou sa direction qui puisse compromettre l'exercice de sa liberté de jugement ».<br><br>
    <strong>Missions principales du Conseil</strong> : déterminer la stratégie (sur proposition du PDG), examiner chaque année le plan à moyen terme et le budget, veiller à la qualité de l'information financière, évaluer la performance du PDG hors sa présence (1 fois/an) et fixer sa rémunération, préparer et convoquer l'Assemblée générale.
  </div>
</div>

<div class="course-chapter" data-theme="corporate" data-chap-idx="20" id="chap-20">
  <h2>20. Partie 3 — Mécanismes de contrôle et d'incitation des dirigeants</h2>

  <h3>Mécanismes internes</h3>
  <div class="key-box">
    <ul>
      <li><strong>L'organisation interne de l'entreprise</strong> (séparation entre pouvoir de décision et responsabilité du contrôle)</li>
      <li><strong>Le conseil d'administration</strong> (le « sommet » des systèmes de contrôle de l'entreprise)</li>
      <li><strong>La rémunération des dirigeants</strong> : partie variable avec intéressement à CT (primes et bonus) et intéressement à LT (stock-options)</li>
      <li><strong>L'assemblée générale des actionnaires</strong></li>
    </ul>
  </div>

  <h3>Mécanismes externes</h3>
  <div class="key-box">
    <ul>
      <li><strong>Le droit</strong> (lois, autorités de contrôle comme l'AMF)</li>
      <li><strong>La presse</strong></li>
      <li><strong>Le marché</strong> (notamment financier)</li>
    </ul>
  </div>
  <p><em>Source : Strategor, 2009, p. 633-654</em></p>

  <h3>Définition de la gouvernance — OCDE</h3>
  <div class="def-box">
    <div class="def-label">Définition OCDE</div>
    <p>« Le gouvernement d'entreprise fait référence aux <strong>relations entre la direction d'une entreprise, son conseil d'administration, ses actionnaires et autres parties prenantes</strong>. Il détermine également la structure par laquelle sont définis les objectifs d'une entreprise, ainsi que les moyens de les atteindre et d'assurer une surveillance des résultats obtenus. »</p>
  </div>

  <h3>2 grandes tendances clés</h3>

  <h4>Tendance 1 — Le développement des pratiques d'audit interne</h4>
  <div class="key-box">
    <strong>5 principes clés mis en avant</strong> :
    <ul>
      <li>Mettre à la disposition du CA les ressources nécessaires pour des demandes de renseignements complémentaires</li>
      <li>Doter les acteurs de la gouvernance des informations nécessaires pour contribuer à la définition de la stratégie</li>
      <li>Instaurer une politique de surveillance des résultats</li>
      <li>Prévoir les interactions nécessaires entre le CA, la direction et les auditeurs internes et externes</li>
      <li>Définir les pratiques de rémunération notamment celle de la DG</li>
    </ul>
    Encouragement à la mise en place de <strong>comités d'audit</strong> dans les entreprises (notamment par l'AMF).
  </div>
  <div class="key-box">
    <strong>Renforcement du rôle du CA — Code AFEP-Medef</strong><br>
    « Le conseil d'administration agit en toute circonstance dans l'intérêt social de l'entreprise. »<br>
    « La détermination des orientations stratégiques est la première mission du conseil d'administration. Il examine et décide les opérations importantes, éventuellement après étude au sein d'un comité ad hoc. Les membres du conseil sont informés de l'évolution des marchés, de l'environnement concurrentiel et des principaux enjeux. »
  </div>
  <div class="example-box">
    <strong>5 comités spécialisés typiques du CA</strong> :
    <ul>
      <li>Comité des comptes</li>
      <li>Comité des rémunérations</li>
      <li>Comité des nominations</li>
      <li>Comité RSE</li>
      <li>Comité Stratégique</li>
    </ul>
  </div>

  <h4>Tendance 2 — La mise en avant de la responsabilité sociale de l'entreprise (RSE)</h4>
  <div class="key-box">
    <strong>Pourquoi l'entreprise devrait-elle adopter un comportement citoyen ?</strong>
    <ul>
      <li><strong>La nécessité d'un « développement durable »</strong> : exigences de la société civile, préoccupations nouvelles (travail, santé, écologie), développement des ONG, etc.</li>
      <li><strong>Une réglementation et des normes de plus en plus exigeantes</strong> : Accord de Kyoto, de Paris, réglementations nationales, normes environnementales (ISO 14000), bilan carbone, etc.</li>
      <li><strong>Une pression croissante de certaines parties prenantes</strong> : associations de consommateurs, institutions scientifiques, riverains des sites, ONG, investisseurs socialement responsables, etc.</li>
    </ul>
    <em>Source : Strategor, 2009, p. 659-672</em>
  </div>
  <div class="example-box">
    <strong>La controverse Friedman vs Freeman</strong><br>
    En 1970, dans un article du <em>New York Times</em>, <strong>Milton Friedman</strong> (Prix Nobel 1976) affirme : <em>« La responsabilité sociale des entreprises est d'accroître ses profits. »</em> La RSE y est décrite comme une hypocrisie destinée à abuser le public. Friedman ajoute que les gens d'affaires qui font la promotion de ces programmes sont probablement victimes d'une « pulsion suicidaire ». Cet article affirme la <strong>prééminence de l'actionnaire présenté comme le propriétaire de l'entreprise</strong>.<br><br>
    À l'opposé, la <strong>théorie des parties prenantes (Freeman, 1984)</strong> postule que l'entreprise a des responsabilités envers tous ses stakeholders, pas uniquement ses actionnaires.
  </div>
  <div class="example-box">
    <strong>Le rôle croissant des ONG</strong> — Volkswagen aux États-Unis (dieselgate), Total en Birmanie, Vinci au Qatar (Coupe du monde, conditions de travail) : en matière de droits de l'homme comme d'environnement, les ONG jouent un rôle croissant d'avertissement sur les pratiques des multinationales. <em>(Source : Le Figaro, AFP, 23/09/2015)</em>
  </div>
  <div class="example-box">
    <strong>Vers un comité des parties prenantes au sein du CA ?</strong> — Avec le développement de l'investissement socialement responsable et l'appel de certains fonds de pension à ce que les entreprises servent le bien commun, certains acteurs militent pour la mise en place d'un <strong>comité des parties prenantes spécifique</strong>. Levier potentiellement efficace pour amener les entreprises à mieux servir le bien commun et intégrer leurs principales parties prenantes dans leurs stratégies.
  </div>
</div>

<div class="course-chapter" data-theme="corporate" data-chap-idx="21" id="chap-21">
  <h2>21. Partie 3 — Les matrices de portefeuille et le modèle MACS</h2>

  <h3>L'impact de la logique actionnariale sur les décisions stratégiques</h3>
  <div class="key-box">
    Les matrices traditionnelles (<strong>BCG, McKinsey, ADL</strong>) sont nées à une époque où la diversification s'inscrivait dans une optique de <strong>répartition des risques</strong>. Le rôle principal du siège était alors d'allouer les ressources entre les activités.<br><br>
    On observe à l'heure actuelle que :
    <ul>
      <li>La <strong>diversification (surtout conglomérale) n'a plus la cote</strong> auprès des milieux financiers. L'heure est au <strong>recentrage sur le « core business »</strong>.</li>
      <li>Dans bon nombre de cas, la <strong>« création de valeur »</strong> est devenue le leitmotiv de la stratégie.</li>
    </ul>
  </div>

  <h3>Cas Unilever — rationalisation du portefeuille de marques</h3>
  <div class="example-box">
    En 2000, Unilever a décidé d'optimiser son portefeuille produits. <strong>En 4 ans, celui-ci est passé de 1 600 à 400 marques</strong>. Les marques se voient aujourd'hui concurrencées de plus en plus durement par les marques de distributeurs (MDD) qui représenteraient un tiers des achats en volume en Europe.<br><br>
    <strong>Matrice Unilever (axes : Progression des ventes × Marge opérationnelle)</strong> :
    <ul>
      <li><strong>Activités ni rentables ni en progression</strong> : Planta, Astra, Puget, Rama → à céder ou abandonner</li>
      <li><strong>Activités peu rentables mais en progression</strong> : Findus, Iglo → développer la marge</li>
      <li><strong>Activités profitables sur des marchés dynamiques</strong> : Magnum, Solero, Ben &amp; Jerry's, Omo, Cif, Skip, Sun → investir</li>
      <li><strong>Activités à forte marge qui ne progressent pas</strong> : Lipton, Impulse, Pepsodent, Timotei, Amora, Knorr → maintenir et rentabiliser</li>
    </ul>
    <em>Source : J.P. Morgan / L'Expansion, 05-10-2004</em>
  </div>

  <h3>Le modèle MACS (Market Activated Corporate Strategy)</h3>
  <div class="def-box">
    <div class="def-label">Modèle MACS — McKinsey</div>
    <p>Le modèle MACS a été développé par <strong>McKinsey</strong>. Il a pour but d'<strong>orienter les choix d'allocation des ressources en vue de maximiser la valeur de l'entreprise</strong>.</p>
    <p>Il utilise <strong>2 critères</strong> :</p>
    <ul>
      <li><strong>La valeur intrinsèque (VI) de l'activité</strong> (axe horizontal) — mesurée par la valeur actualisée des cash-flows futurs que l'activité est capable de générer.</li>
      <li><strong>La capacité du groupe à accroître cette valeur (AP — apport parental)</strong> (axe vertical) — surcroît de valeur que le groupe peut apporter à l'activité, dépendant des synergies entre toutes les activités du groupe.</li>
    </ul>
  </div>
  <table class="comp-table">
    <thead><tr><th></th><th>Valeur intrinsèque faible</th><th>Valeur intrinsèque élevée</th></tr></thead>
    <tbody>
      <tr><td><strong>Apport parental fort (+)</strong></td><td>Conserver</td><td><strong>Développer en priorité</strong></td></tr>
      <tr><td><strong>Apport parental faible (−)</strong></td><td>Abandonner</td><td>Cession à un meilleur parent OU Scission</td></tr>
    </tbody>
  </table>
  <div class="key-box">
    <strong>Logique de l'avantage parental (« parental advantage »)</strong> :
    <ul>
      <li>Une <strong>ligne horizontale</strong> sépare les activités où le groupe apporte de la valeur (au-dessus = parenting advantage) de celles où un autre parent ferait mieux (en dessous)</li>
      <li>En dessous de la ligne : <strong>cession à un meilleur parent ou scission</strong> = logique de création de valeur poussée à son paroxysme</li>
    </ul>
    <em>Source : Strategor, 2009, p. 453-454</em>
  </div>
  <div class="example-box">
    <strong>Exemple d'application — Groupe diversifié à 4 DAS</strong> :
    <ul>
      <li>DAS 1 (VI : 200, AP : FORT) → Développer en priorité</li>
      <li>DAS 2 (VI : 50, AP : FORT) → Conserver</li>
      <li>DAS 3 (VI : 150, AP : FAIBLE) → Céder ou scinder (un autre groupe extrairait plus de valeur)</li>
      <li>DAS 4 (VI : 250, AP : FAIBLE) → Céder à un meilleur parent</li>
    </ul>
    Les synergies (design, marketing, R&amp;D) traversent les DAS et conditionnent l'apport parental.
  </div>
</div>

<div class="course-chapter" data-theme="corporate" data-chap-idx="22" id="chap-22">
  <h2>22. Partie 3 — Synthèse : légitimer la stratégie</h2>
  <div class="key-box">
    <strong>3 grandes idées à retenir</strong> :
    <ol>
      <li><strong>La gouvernance d'entreprise est une question stratégique</strong>. Son évolution historique (familiale → managériale → actionnariale) traduit une montée en puissance des actionnaires et des investisseurs institutionnels (fonds de pension, private equity, fonds activistes), avec des exigences de rentabilité élevées et des outils de contrôle renforcés (CA, comités spécialisés, AFEP-Medef, AMF).</li>
      <li><strong>Les parties prenantes doivent être identifiées et hiérarchisées</strong>. La matrice pouvoir × intérêt (Johnson et al., 2005) permet d'adapter les efforts d'engagement. La RSE (Freeman, 1984) s'oppose à la vision actionnariale pure (Friedman, 1970) et s'impose progressivement sous la pression des ONG, des consommateurs et de la réglementation.</li>
      <li><strong>Les outils de portefeuille évoluent</strong>. Les matrices BCG, McKinsey, ADL ont été conçues dans une optique de répartition des risques (diversification). Aujourd'hui, la logique de création de valeur pousse au recentrage : le modèle MACS de McKinsey croise valeur intrinsèque et avantage parental pour décider de développer, conserver, céder ou abandonner chaque DAS.</li>
    </ol>
  </div>
  <div class="key-box">
    <strong>Concepts-clés à maîtriser</strong> :
    <ul>
      <li>Gouvernance familiale, managériale, actionnariale</li>
      <li>Propriétaire sans contrôle (actionnaire) / manager professionnel (dirigeant)</li>
      <li>Fonds de pension, fonds d'investissement (capital-risque, capital-développement, LBO), fonds activistes</li>
      <li>Parties prenantes : internes, interfaces, externes</li>
      <li>Matrice pouvoir/intérêt (Johnson 2005) : effort minimal / à garder informés / à garder satisfaits / acteurs clés</li>
      <li>Code AFEP-Medef, comités spécialisés du CA (comptes, rémunérations, nominations, RSE, stratégique)</li>
      <li>Friedman 1970 vs Freeman 1984</li>
      <li>Matrice MACS : valeur intrinsèque × apport parental</li>
      <li>Avantage parental (parenting advantage)</li>
      <li>Recentrage sur le core business vs diversification conglomérale</li>
    </ul>
  </div>
  <p style="text-align:center; margin-top:2rem; font-style:italic; color:var(--text3);">— Fin de la 3e partie / Fin du cours Management Stratégique —</p>
</div>
'''

def insert():
    text = HTML.read_text()
    # Cherche la fin de getCoursHTML : `; }`
    # Localise précisément la fin du dernier chapitre (`</div>` puis `\n\`; }`)
    marker = '`; }\n\n/* ═══════ SYNTH HTML ═══════ */'
    if marker not in text:
        raise SystemExit('Marker SYNTH HTML introuvable — getCoursHTML déjà patché ou structure modifiée')
    new_text = text.replace(marker, NEW_CHAPTERS + marker, 1)
    HTML.write_text(new_text)
    # Compte les nouveaux chapitres
    n_new = NEW_CHAPTERS.count('course-chapter')
    print(f'✓ {n_new} nouveaux chapitres insérés dans strat.html')


if __name__ == '__main__':
    insert()
