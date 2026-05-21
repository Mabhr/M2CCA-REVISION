"""Réécrit getSynthHTML des 5 cours (sauf inge_fi qui est OK) en mode
« fiche de révision complète » : phrases complètes, contexte, exemples concrets,
pas d'abréviations cryptiques.

Chaque mini-card contient :
- Un titre court qui nomme le concept
- 1-3 phrases explicatives en français complet
- Au moins un exemple concret, un chiffre, une citation, ou une référence précise
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


CONDUITE_SYNTH = '''function getSynthHTML() {
  return `

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(61,114,180,0.18)">🔄</div> Le changement comme processus
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>Loi de Le Chatelier — l'analogie fondatrice</strong>
      <p>Toute modification de l'équilibre d'un système provoque des phénomènes qui s'y opposent. Appliquée à l'organisation : tout changement génère naturellement des résistances. Pour réussir, il faut <strong>simultanément augmenter les pressions favorables et diminuer les résistances</strong> — l'un sans l'autre échoue.</p>
    </div>
    <div class="synth-mini">
      <strong>Modèle de Kurt Lewin (1947) — 3 phases</strong>
      <p>① <strong>Décristallisation</strong> : on remet en cause les habitudes, on prépare les esprits. ② <strong>Changement</strong> : modifications concrètes des tâches, de la structure, des techniques et des comportements. ③ <strong>Cristallisation</strong> : on stabilise les nouveaux comportements par un renforcement positif (évaluation, suivi, célébrations).</p>
    </div>
    <div class="synth-mini">
      <strong>Modèle de Kotter</strong>
      <p>Cité comme référence par Besombes (sans détailler les 8 étapes classiques). À mobiliser comme grille structurée pour démarche de transformation. C'est l'un des modèles incontournables à connaître nominativement à l'examen.</p>
    </div>
    <div class="synth-mini">
      <strong>Courbe de Kübler-Ross</strong>
      <p>Modèle psychologique des étapes émotionnelles face au changement (initialement étapes du deuil). Schéma transposé au monde de l'entreprise par Philippe Moret : choc → déni → résistance → exploration → acceptation. Permet d'anticiper les réactions individuelles.</p>
    </div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(176,90,71,0.18)">⚔️</div> Résistance &amp; adhésion
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>Pourquoi le changement perturbe</strong>
      <p>Trois facteurs psychosociologiques déstabilisent l'individu : découvrir chez les autres des attitudes différentes des siennes ; voir son image renvoyée par les autres comme différente de l'idée qu'on s'en faisait ; et constater qu'un même mot a un sens différent selon les personnes.</p>
    </div>
    <div class="synth-mini">
      <strong>Les 7 sources de résistance</strong>
      <p>① Manque d'informations claires sur le projet · ② peur de l'inconnu · ③ besoin de sécurité menacé · ④ pas de besoin de changement ressenti · ⑤ peur de perdre des acquis (statut, avantages) · ⑥ moment mal choisi (autre urgence) · ⑦ manque de ressources (temps, moyens).</p>
    </div>
    <div class="synth-mini">
      <strong>4 leviers pour surmonter la résistance</strong>
      <p><strong>Communiquer</strong> (éliminer les craintes par l'information). <strong>Faire participer</strong> (créer un sentiment d'engagement dès la planification). <strong>Soutenir</strong> (assurer confiance et crédibilité, accompagner les plus en difficulté). <strong>Négocier</strong> (harmoniser objectifs personnels et organisationnels).</p>
    </div>
    <div class="synth-mini">
      <strong>3 stratégies utiles selon le contexte</strong>
      <p><strong>Coercition</strong> : autorité hiérarchique, peur des sanctions, attrait des récompenses (efficace dans l'urgence). <strong>Persuasion rationnelle</strong> : appel à la logique et à la compétence (pour convaincre par les faits). <strong>Partage du pouvoir</strong> : responsabilisation comme moteur de motivation (le plus durable mais le plus long).</p>
    </div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(90,145,104,0.18)">📋</div> La démarche en 8 étapes (Besombes)
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>Étapes 1-2 : Amorcer &amp; Diagnostiquer</strong>
      <p>① <strong>Amorcer</strong> : définir la politique en analysant les facteurs internes (organisation actuelle, compétences disponibles) et externes (demande clients, prospective économique, autres acteurs). ② <strong>Diagnostic</strong> : forces/faiblesses, cartographie des relations, prise en compte des résultats déjà existants.</p>
    </div>
    <div class="synth-mini">
      <strong>Étapes 3-4 : Cadre &amp; Mobiliser</strong>
      <p>③ <strong>Nouveau cadre</strong> : documentation centralisée, carte des compétences, fiches prestations, programme de formation, communication, outils de pilotage. ④ <strong>Mobiliser</strong> : sensibilisation collective ET individuelle aux nouveaux objectifs, formation aux méthodes, définition des règles du jeu et des modalités d'évaluation.</p>
    </div>
    <div class="synth-mini">
      <strong>Étapes 5-6 : Plans &amp; Mise en œuvre</strong>
      <p>⑤ <strong>Plans d'action</strong> : hiérarchiser les actions, calendrier, désigner les responsables, répartir les équipes, définir indicateurs de pilotage. ⑥ <strong>Mise en œuvre</strong> : déployer en restant vigilant, en appui des équipes, en contrôlant les dérives et en respectant les délais.</p>
    </div>
    <div class="synth-mini">
      <strong>Étapes 7-8 : Mesurer &amp; S'améliorer (~2 ans)</strong>
      <p>⑦ <strong>Mesurer</strong> : constater écarts positifs et négatifs, corriger, informer les collaborateurs, motiver. ⑧ <strong>S'améliorer</strong> : associer l'équipe à la réflexion, fixer de nouveaux objectifs, responsabiliser. Besombes estime que ce parcours complet demande <strong>2 ans en moyenne — ni trop, ni trop peu</strong>.</p>
    </div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(200,131,70,0.18)">🧭</div> La vocation en 3 phases (Écoute / Mobilisation / Coordination)
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>Phase 1 : Écouter pour comprendre</strong>
      <p>On commence par <strong>écouter ceux qui ont formulé la problématique mais aussi ceux qui la vivront</strong>, plutôt en face-à-face individuel. Objectif : comprendre les écarts d'angles de vue, mesurer la hauteur de la marche, capter sans censurer les idées, instaurer un dialogue de confiance. On termine par une synthèse partagée avec les décideurs.</p>
    </div>
    <div class="synth-mini">
      <strong>Phase 2 : Mobiliser autour d'un périmètre commun</strong>
      <p>Réunir un panel représentatif des parties prenantes pour <strong>qualifier les solutions, définir des critères de priorisation, sélectionner les actions à mettre en place</strong>. Le mot d'ordre : passer « de la lettre au Père Noël à un projet collectif réaliste ».</p>
    </div>
    <div class="synth-mini">
      <strong>Qualifier les solutions — grille à 4 cases</strong>
      <p>Côté résultats : <strong>Gains attendus</strong> (productivité, qualité, niveau de service) vs <strong>Contraintes</strong> (éléments externes subis). Côté conditions : <strong>Points d'appui</strong> (sponsor de poids, effet de levier) vs <strong>Freins</strong> (obstacles internes sur lesquels on peut agir).</p>
    </div>
    <div class="synth-mini">
      <strong>Prioriser — matrice Importance × Facilité</strong>
      <p>Représentation graphique avec deux axes notés de 0 à 10. Les actions à mener en priorité sont celles à <strong>importance élevée ET facilité élevée</strong>. Les autres sont mises « au parking » (importance faible) ou méritent un travail préparatoire (importance haute / facilité faible).</p>
    </div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(138,122,168,0.18)">👥</div> Les acteurs face au changement
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>Le triptyque 10-80-10</strong>
      <p>Face à tout changement, on retrouve trois profils dans la population. <strong>10 à 20 % de proactifs</strong> (constructifs, prescripteurs) qu'il faut <strong>utiliser</strong> comme relais. <strong>60 à 80 % de passifs</strong> (hésitants, en attente de preuves) qu'il faut <strong>rassurer</strong>. <strong>10 à 20 % d'opposants</strong> (destructeurs systématiques) qu'il faut <strong>laisser s'isoler</strong> pour pouvoir mieux les récupérer ensuite.</p>
    </div>
    <div class="synth-mini">
      <strong>Trois niveaux d'appui successifs</strong>
      <p>① <strong>Le Top Management</strong> donne l'impulsion et la légitimité (mais doit lui-même être convaincu). ② <strong>Le Middle Management</strong> relaie et intègre le changement dans le quotidien (à condition d'avoir un temps d'avance). ③ <strong>Les Ressources Métiers internes</strong> accompagnent sur le terrain — elles connaissent l'organisation, sont légitimes, et resteront.</p>
    </div>
    <div class="synth-mini">
      <strong>La grille communication selon les questions</strong>
      <p>À chaque question des acteurs correspond un dispositif. « Pourquoi changer ? » → comm projet · « Qu'est-ce qui change pour moi ? » → modules de sensibilisation · « Vais-je être à la hauteur ? » → formation · « Suis-je prêt ? » → entraînement · « Je ne suis pas prêt ! » → assistance de proximité.</p>
    </div>
    <div class="synth-mini">
      <strong>La méthode RACI — clarifier les rôles</strong>
      <p>Outil de répartition des rôles, à formaliser par processus. <strong>R</strong>esponsable (un seul par activité, approuve et assume). <strong>A</strong>cteur (1 à n, réalise concrètement). <strong>C</strong>ontribution (apporte information / expertise sans autorité). <strong>I</strong>nformation (mis au courant, généralement indirectement impacté).</p>
    </div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(77,154,168,0.18)">🎯</div> La gestion des compétences
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>Définition Besombes de la compétence</strong>
      <p>« Une disposition à mobiliser, combiner et mettre en œuvre des ressources : savoir, savoir-faire et savoir-être. C'est une <strong>combinaison dynamique</strong> de plusieurs éléments — savoir théorique, procédures, bonnes pratiques, savoir-faire et expérience non formalisée. »</p>
    </div>
    <div class="synth-mini">
      <strong>La chaîne des rôles dans la performance</strong>
      <p>Un poste passe par 4 étapes : le <strong>rôle confié</strong> par l'organisation → le <strong>rôle perçu</strong> par le salarié → le <strong>rôle accepté</strong> → le <strong>rôle tenu</strong> effectivement. La description de poste sert à <strong>minimiser l'écart d'efficacité</strong> entre rôle confié et rôle tenu.</p>
    </div>
    <div class="synth-mini">
      <strong>GPEC / GEPP — l'anticipation</strong>
      <p>La Gestion Prévisionnelle des Emplois et des Compétences vise à <strong>réduire de façon anticipée les écarts entre besoins et ressources</strong> de l'entreprise (effectifs et compétences), au regard des objectifs identifiés, avec l'implication du salarié dans un projet d'évolution professionnelle.</p>
    </div>
    <div class="synth-mini">
      <strong>L'organisation qualifiante</strong>
      <p>Repose sur 3 piliers : <strong>enrichissement des tâches</strong>, <strong>volonté éducative</strong> (apprentissage permanent), <strong>recherche de la compétitivité</strong>. Elle s'appuie sur un dictionnaire de compétences et une prévision réaliste de l'évolution de l'emploi. C'est l'antithèse de l'organisation taylorienne.</p>
    </div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(61,114,180,0.18)">🤝</div> L'équipe &amp; le management
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>Les 5 étapes de constitution d'une équipe</strong>
      <p>① <strong>Constitution</strong> (création, découverte, positionnement → team building) · ② <strong>Tension</strong> (confrontation des opinions → prévention/gestion des conflits) · ③ <strong>Normalisation</strong> (acceptation d'un but commun → négociation) · ④ <strong>Production</strong> (travail collectif efficace → motivation) · ⑤ <strong>Dissolution</strong> (départs, nouveaux arrivants → valorisation).</p>
    </div>
    <div class="synth-mini">
      <strong>Le continuum directif → délégatif</strong>
      <p>Le management se positionne sur 7 niveaux entre l'<strong>autorité du responsable</strong> et la <strong>liberté du groupe</strong> : autorité (directif) → information → explicatif → consultation → concertation → négociation → implicatif (délégation). Le bon style dépend de la maturité de l'équipe.</p>
    </div>
    <div class="synth-mini">
      <strong>Les 4 attentes vis-à-vis du manager</strong>
      <p>Ce que les managés attendent : un manager <strong>honnête</strong> (intégrité, source de confiance) ; <strong>compétent</strong> (techniquement et managérialement) ; <strong>tourné vers l'avenir</strong> (vision) ; <strong>motivant</strong> (dynamisme, capacité à impliquer). Sans ces 4 piliers, pas de leadership crédible.</p>
    </div>
    <div class="synth-mini">
      <strong>Le Modèle de Gilbert (1980)</strong>
      <p>La performance se construit à l'intersection de 3 dimensions : <strong>Objectifs · Moyens · Résultats</strong>. Les écarts définissent : <strong>Efficacité</strong> (Objectifs ↔ Résultats), <strong>Efficience</strong> (Moyens ↔ Résultats), <strong>Pertinence</strong> (Objectifs ↔ Moyens). Outil simple et complet d'analyse de la performance.</p>
    </div>
  </div>
</div>

`;
}
'''


EVO_SYNTH = '''function getSynthHTML() {
  return `

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(61,114,180,0.18)">🌍</div> Le contexte d'évolution des organisations
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>Une aventure vieille de 400 000 ans</strong>
      <p>L'organisation humaine se structure depuis la maîtrise du feu. Trois tensions traversent toute organisation : <strong>Pouvoir / Contre-pouvoir / Spécialisation</strong>. L'accélération récente est nette : Révolution industrielle au XVIIIᵉ → TIC à la fin du XXᵉ → IA d'ici 2030.</p>
    </div>
    <div class="synth-mini">
      <strong>Les 3 grandes logiques économiques</strong>
      <p>Vers 1900, l'entreprise est dominée par une <strong>logique de production</strong> (faire plus, à moindre coût). À partir de 1950, c'est la <strong>logique de vente</strong> (commercialiser, distribuer). Aujourd'hui, c'est la <strong>logique de création de valeur</strong> qui prime — la performance ne se réduit plus à la productivité.</p>
    </div>
    <div class="synth-mini">
      <strong>Quelles organisations contemporaines ?</strong>
      <p>Quatre formes émergentes qui défient les modèles classiques : les <strong>entreprises virtuelles</strong>, les <strong>industries sans usines</strong> (modèle fabless), les <strong>grandes entreprises composées d'une multitude de PME</strong>, et les <strong>organisations sur l'ensemble des territoires</strong> (réseaux distribués).</p>
    </div>
    <div class="synth-mini">
      <strong>Le schéma BOR — la logique permanente</strong>
      <p>Toute organisation répond à un <strong>Besoin</strong> par une <strong>Réponse</strong>, en mobilisant une <strong>Organisation</strong>. La cohérence repose sur deux piliers : les ressources humaines et les compétences d'un côté ; les ressources matérielles et financières de l'autre. C'est le squelette de toute analyse d'organisation.</p>
    </div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(176,90,71,0.18)">🎯</div> Drucker et la Direction Par Objectifs
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>Peter Drucker (1909-2005), DPPO 1954</strong>
      <p>Peter Drucker conceptualise en 1954 la <strong>Direction Par Objectifs (DPPO)</strong>, rupture avec le management par les tâches. Le principe : on ne dirige plus en disant comment faire, mais en fixant <strong>quoi atteindre</strong> et en laissant l'autonomie sur le comment.</p>
    </div>
    <div class="synth-mini">
      <strong>Les 6 principes fondamentaux</strong>
      <p>① <strong>Définir la mission</strong> de l'entité · ② <strong>Fixer des objectifs clairs</strong> pour chaque équipe · ③ <strong>Analyser et organiser le travail</strong> pour créer de la satisfaction · ④ <strong>Informer et écouter</strong> ses collaborateurs · ⑤ <strong>Évaluer les résultats</strong> avec des normes spécifiques · ⑥ <strong>Former ses collaborateurs en permanence</strong>.</p>
    </div>
    <div class="synth-mini">
      <strong>Changement de paradigme : tâches → objectifs</strong>
      <p>L'école classique pensait l'entreprise comme un ensemble de tâches à optimiser (logique taylorienne). Drucker la pense comme un ensemble d'objectifs à atteindre. Cette bascule fonde la transversalité moderne et la responsabilisation des équipes.</p>
    </div>
    <div class="synth-mini">
      <strong>Citation Paul Valéry</strong>
      <p>« <em>Un bon chef est celui qui a besoin des autres.</em> » Mobilisée par Besombes pour rappeler que <strong>la performance se construit en faisant réussir les autres</strong>, pas en s'imposant ni en faisant à leur place.</p>
    </div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(90,145,104,0.18)">⚙️</div> L'approche processus &amp; ISO 9001
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>Du modèle tâches au modèle processus</strong>
      <p>L'évolution du management consiste à passer d'une <strong>logique de tâches</strong> (héritée de l'école classique) à une <strong>approche processus</strong> orientée vers la performance et l'excellence. C'est le pivot pour comprendre les organisations modernes.</p>
    </div>
    <div class="synth-mini">
      <strong>Définition formelle (ISO 8402)</strong>
      <p>Selon la norme ISO 8402 (citée par Baracchini 2007) : un processus est « un ensemble des moyens et activités qui <strong>transforment des éléments entrants en éléments sortants</strong> dans un but défini et mesurable ». Le vocabulaire descend du macroprocessus (Client, RH…) au processus, sous-processus puis tâche.</p>
    </div>
    <div class="synth-mini">
      <strong>Les 3 types de processus</strong>
      <p>① <strong>Réalisation</strong> : conçoit et délivre le produit ou service (conception, fabrication, vente). ② <strong>Support</strong> : appuie la réalisation (RH, formation, informatique, comptabilité, maintenance). ③ <strong>Pilotage</strong> : met en œuvre les objectifs (politique, stratégie, décision, budget, mesure).</p>
    </div>
    <div class="synth-mini">
      <strong>La tortue de Crosby — 4 questions</strong>
      <p>Pour caractériser un processus, on répond à 4 questions structurantes : <strong>Avec quoi ?</strong> (moyens et équipements) · <strong>Avec qui ?</strong> (compétences) · <strong>Comment ?</strong> (méthodes) · <strong>Combien ?</strong> (indicateurs de pilotage). Outil simple à mobiliser pour cartographier n'importe quel processus.</p>
    </div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(200,131,70,0.18)">📊</div> Performance et pilotage
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>Dualité Stratégie / Organisation</strong>
      <p>L'entreprise doit conjuguer démarche pro-active de conquête et limitation du risque. Edgar Morin parle d'<strong>éléments ago-antagonistes</strong> qu'il faut faire converger. Alfred Chandler (1962) formule la fameuse <strong>« structure follows strategy »</strong> : il y a un lien indissociable entre la structure d'une entreprise et sa stratégie.</p>
    </div>
    <div class="synth-mini">
      <strong>Définition de la performance (Besombes)</strong>
      <p>La performance d'une organisation est <strong>issue d'un processus de construction contingent</strong>. Elle est la conséquence d'une représentation, sans réalité propre — résultat de l'<strong>accord entre parties prenantes</strong>, fondé sur le consensus et la coopération. Elle est devenue stratégique et contribue à l'émergence du sens.</p>
    </div>
    <div class="synth-mini">
      <strong>Efficacité vs efficience (Drucker)</strong>
      <p>Drucker tranche : « L'<strong>efficacité</strong> consiste à <strong>faire les bonnes choses</strong>. L'<strong>efficience</strong> consiste à <strong>faire les choses de la bonne façon</strong>. » La performance dans un contexte donné est la capacité d'être <strong>à la fois efficace ET efficient</strong>.</p>
    </div>
    <div class="synth-mini">
      <strong>Le Modèle de Gilbert (1980)</strong>
      <p>Triangle simple et puissant : la performance se construit à l'intersection de 3 dimensions — <strong>Objectifs · Moyens · Résultats</strong>. Trois écarts en découlent : Efficacité (Objectifs ↔ Résultats), Efficience (Moyens ↔ Résultats), Pertinence (Objectifs ↔ Moyens). Grille universelle d'analyse.</p>
    </div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(138,122,168,0.18)">🧭</div> Pilotage et dialogue social
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>Michel Crozier (1922-2013)</strong>
      <p>Concepteur de l'<strong>analyse stratégique et de l'action collective</strong>. Sa thèse : les organisations sont comparables à des <strong>organismes vivants</strong> — elles planifient, analysent, expérimentent, décident, s'adaptent et innovent face à leur environnement. L'arbre de décision dynamique mobilise trois leviers : <strong>Pouvoir, Droit, Intérêt</strong>.</p>
    </div>
    <div class="synth-mini">
      <strong>Citation Carlos Ghosn</strong>
      <p>« La réussite d'une entreprise, c'est <strong>5 % de stratégie et 95 % d'action.</strong> » Mobilisée par Besombes pour justifier le poids du dialogue social et du pilotage opérationnel. Sans action concrète portée par les équipes, la meilleure stratégie reste lettre morte.</p>
    </div>
    <div class="synth-mini">
      <strong>De la structure fonctionnelle à la structure projet</strong>
      <p>Passage d'une <strong>communication séquentielle descendante</strong> centrée sur les tâches à une <strong>communication continue circulaire</strong> centrée sur les processus. Le cycle est piloté par le PDCA : <strong>Prévoir → Faire → Contrôler (en autonomie) → Agir ou Réagir</strong>.</p>
    </div>
    <div class="synth-mini">
      <strong>Les 4 niveaux du dialogue social</strong>
      <p>Pour réussir le changement, le dialogue doit traverser 4 strates : le <strong>Top Management</strong>, le <strong>Management de Proximité</strong>, les <strong>Opérateurs</strong>, et les <strong>IRP</strong> (Instances Représentatives du Personnel). Deux registres : <strong>formel</strong> (réunions, accords) et <strong>informel</strong> (proximité quotidienne).</p>
    </div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(77,154,168,0.18)">✨</div> Mises en perspective &amp; conclusion
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>Tainter et l'effondrement par complexité</strong>
      <p>Joseph Tainter a étudié les effondrements de sociétés et identifié 6 facteurs : les sociétés humaines sont faites pour résoudre des problèmes ; les systèmes sociopolitiques ont besoin d'énergie ; la complexité croît plus vite que les bénéfices (<strong>rendements marginaux décroissants</strong>) ; la société persiste dans une stratégie de moins en moins rentable ; des segments cherchent la sécession ; effondrement.</p>
    </div>
    <div class="synth-mini">
      <strong>Étude Deloitte 2016 (Philippe Burger)</strong>
      <p>« <strong>90 % des entreprises françaises envisagent une évolution de leur organisation.</strong> 11 % déclarent déjà avoir une structure organisée autour de projets ou programmes transverses. » Émergence d'un nouveau modèle : le <strong>réseau d'équipes</strong>, équipes responsables, flexibles, interconnectées.</p>
    </div>
    <div class="synth-mini">
      <strong>Les 7 leviers de la vision à l'action</strong>
      <p>① Avoir une offre <strong>choisie et non subie</strong> · ② <strong>Segmenter</strong> ses clients · ③ Cultiver des <strong>réseaux</strong> pour une réponse globale · ④ Cultiver la <strong>capacité innovante</strong> · ⑤ Assurer la <strong>convergence des compétences</strong> · ⑥ Intensifier la <strong>transversalité</strong> · ⑦ Construire une <strong>offre experte (notre métier) ET globale (partenaires)</strong>.</p>
    </div>
    <div class="synth-mini">
      <strong>Conclusion — CO-CONSTRUIRE / CO-AGIR / CO-RESPONSABLE</strong>
      <p>« La performance est éphémère et il convient à chaque instant de <strong>renouveler l'expérience collective</strong> qui permet de la construire. » Karajan disait : « <em>L'art de diriger consiste à abandonner la baguette pour ne pas gêner l'orchestre.</em> » Le manager du XXIᵉ siècle est avant tout un <strong>catalyseur</strong>.</p>
    </div>
  </div>
</div>

`;
}
'''


GOUV_SYNTH = '''function getSynthHTML() {
  return `

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(61,114,180,0.18)">🏛️</div> Fondamentaux de la gouvernance SI
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>Définition du Système d'Information</strong>
      <p>Un SI est l'<strong>ensemble des données et ressources matérielles et logicielles</strong> de l'entreprise permettant de stocker ou faire circuler l'information. C'est à la fois le <strong>point de départ</strong> (collecte de données) et le <strong>point d'arrivée</strong> (aide à la décision) de toute analyse.</p>
    </div>
    <div class="synth-mini">
      <strong>Gouvernance des SI (Lebey)</strong>
      <p>« Moyens de <strong>gestion et de régulation</strong> des SI mis en place pour atteindre les objectifs et les communiquer : Audit, Bonnes pratiques, Tableaux de bord, Benchmarking, Certification. » Elle associe <strong>pilotage</strong> (décisions pour préparer le futur) et <strong>contrôle</strong> (écart réalisé / prévisionnel).</p>
    </div>
    <div class="synth-mini">
      <strong>Les 5 fondements ISACA</strong>
      <p>L'ISACA définit 5 piliers : ① <strong>Alignement stratégique</strong> (le SI doit servir la stratégie globale) · ② <strong>Création de valeur</strong> (le SI doit générer de la valeur) · ③ <strong>Gestion des risques</strong> · ④ <strong>Gestion des ressources</strong> (humaines, financières, techniques) · ⑤ <strong>Mesure de la performance</strong> (par des indicateurs).</p>
    </div>
    <div class="synth-mini">
      <strong>Modèle Henderson-Venkatraman</strong>
      <p>4 formes d'alignement stratégique SI / business : ① <strong>Exécution opérationnelle</strong> de la stratégie · ② <strong>SI vecteur de transformation</strong> technologique · ③ <strong>SI à l'origine de la stratégie</strong> (source d'avantage concurrentiel) · ④ <strong>SI prestataire de services</strong> opérationnels aux métiers.</p>
    </div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(200,131,70,0.18)">🏢</div> La DSI et l'externalisation
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>Les 3 pôles de la DSI</strong>
      <p>Une DSI s'organise typiquement autour de 3 pôles : <strong>Production</strong> (exploitation des infrastructures, maintien en condition opérationnelle) · <strong>Support</strong> (assistance utilisateurs, Help Desk) · <strong>Développement / Études</strong> (conception et mise en place des nouvelles applications, gestion de projet).</p>
    </div>
    <div class="synth-mini">
      <strong>Externalisation et infogérance</strong>
      <p>Plusieurs degrés : <strong>infogérance globale</strong> (tout le SI confié à un prestataire) ; <strong>sélective</strong> (une fonction précise) ; <strong>de parc</strong> (matériel) ; <strong>de production</strong> (exploitation). En cas de fonction métier confiée, on parle de <strong>BPO</strong> (Business Process Outsourcing).</p>
    </div>
    <div class="synth-mini">
      <strong>TMA — Tierce Maintenance Applicative</strong>
      <p>3 domaines distincts : <strong>MCO</strong> (Maintien en Conditions Opérationnelles — corriger les bugs, garder le système qui tourne) · <strong>MEV</strong> (Maintenance Évolutive — adapter le logiciel aux évolutions réglementaires ou métier) · <strong>Maintenance évolutive de fond</strong> (refonte, modernisation).</p>
    </div>
    <div class="synth-mini">
      <strong>SLA, OLA, réversibilité</strong>
      <p>Le <strong>SLA</strong> (Service Level Agreement) fixe les engagements de qualité (disponibilité, délais) avec le prestataire externe, assortis de pénalités. L'<strong>OLA</strong> (Operational Level Agreement) en est l'équivalent interne entre services. La <strong>réversibilité</strong> garantit la possibilité de ré-internaliser ; la <strong>transférabilité</strong> de changer de prestataire.</p>
    </div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(90,145,104,0.18)">📚</div> Les grands référentiels
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>COBIT — gouvernance IT</strong>
      <p>Référentiel ISACA pour aligner le SI sur les objectifs métier. Structuré en <strong>4 domaines</strong> (Planification &amp; Organisation, Acquisition &amp; Implémentation, Delivery &amp; Support, Surveillance &amp; Évaluation) déclinés en 34 processus. Il intègre <strong>7 critères d'information</strong> (efficacité, efficience, confidentialité, intégrité, disponibilité, conformité, fiabilité).</p>
    </div>
    <div class="synth-mini">
      <strong>ITIL — gestion des services IT</strong>
      <p>Référentiel britannique pour la <strong>fourniture et le support des services informatiques</strong>. Couvre le cycle de vie des services : conception, transition, exploitation, amélioration continue. Processus emblématiques : gestion des incidents, des problèmes, des changements, des configurations, et SLA.</p>
    </div>
    <div class="synth-mini">
      <strong>CMMI — maturité des processus</strong>
      <p>Modèle américain (Department of Defense) qui évalue la maturité d'une organisation sur 5 niveaux : ① <strong>Initial</strong> (chaotique) · ② <strong>Reproductible</strong> (premières pratiques) · ③ <strong>Défini</strong> (processus documentés et appliqués) · ④ <strong>Maîtrisé</strong> (mesuré quantitativement) · ⑤ <strong>Optimisé</strong> (amélioration continue).</p>
    </div>
    <div class="synth-mini">
      <strong>Val IT &amp; Risk IT</strong>
      <p>Compléments ISACA à COBIT. <strong>Val IT</strong> structure la gestion de la valeur des investissements IT (gouvernance de la valeur / portefeuille / investissements). <strong>Risk IT</strong> structure la gestion des risques IT en 3 domaines : Risk Governance (RG), Risk Evaluation (RE), Risk Response (RR).</p>
    </div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(176,90,71,0.18)">🔒</div> Risques, sécurité, contrôle interne
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>Famille ISO 27000 — sécurité de l'information</strong>
      <p>Famille de normes dédiée à la sécurité de l'information. <strong>ISO 27001</strong> définit le SMSI (Système de Management de la Sécurité). <strong>ISO 27002</strong> liste 133 bonnes pratiques. Famille élargie : 27004 (indicateurs), 27005 (gestion des risques). C'est la base de toute PSSI sérieuse.</p>
    </div>
    <div class="synth-mini">
      <strong>COSO — contrôle interne</strong>
      <p>Référentiel américain (1992, révisé 2002 après Enron/Worldcom) sur le contrôle interne. <strong>3 objectifs</strong> (efficacité opérationnelle, fiabilité du reporting, conformité réglementaire) et <strong>5 composantes</strong> (environnement de contrôle, évaluation des risques, activités de contrôle, information/communication, pilotage). Lien direct avec la LSF française (2003).</p>
    </div>
    <div class="synth-mini">
      <strong>BSC — Balanced Scorecard (Kaplan-Norton)</strong>
      <p>Tableau de bord équilibré sur <strong>4 axes</strong> : ① <strong>Financier</strong> (résultats, rentabilité) · ② <strong>Client</strong> (satisfaction, parts de marché) · ③ <strong>Processus internes</strong> (efficacité opérationnelle, qualité) · ④ <strong>Innovation et apprentissage</strong> (R&amp;D, formation). Méthode de pilotage stratégique qui traduit la stratégie en KPI.</p>
    </div>
    <div class="synth-mini">
      <strong>PSSI — Politique de Sécurité des SI</strong>
      <p>Démarche globale, pas juste un antivirus. Elle comprend : identification et évaluation des <strong>risques</strong>, définition des <strong>règles</strong>, contrôles techniques et organisationnels, <strong>sensibilisation</strong> des utilisateurs, audits réguliers, <strong>mise à jour continue</strong>. Inclut un PCA (Plan de Continuité d'Activité) et un PRA (Plan de Reprise).</p>
    </div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(138,122,168,0.18)">🔍</div> L'audit des SI
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>Audit des SI — définition et objectifs</strong>
      <p>L'audit des SI vérifie que le SI répond aux objectifs de l'entreprise dans le respect de la réglementation. Ses missions : évaluer les risques, contrôler les processus, valider la conformité, identifier les opportunités d'amélioration. Repose sur des normes (ISA, NEP 315, NEP 330) et des référentiels (COBIT, ISO 27000).</p>
    </div>
    <div class="synth-mini">
      <strong>NEP 315 &amp; NEP 330</strong>
      <p><strong>NEP 315</strong> : « Connaissance de l'entité et de son environnement et évaluation du risque d'anomalies significatives ». <strong>NEP 330</strong> : « Procédures d'audit mises en œuvre par le commissaire aux comptes à l'issue de son évaluation des risques ». Transposition française des ISA 315 et 330.</p>
    </div>
    <div class="synth-mini">
      <strong>Cadre légal français</strong>
      <p>Plusieurs textes structurent l'audit financier et SI : <strong>SOX</strong> (Sarbanes-Oxley, USA 2002) · <strong>NRE</strong> (Loi 2001) · <strong>LSF</strong> (Loi de Sécurité Financière 2003 — équivalent français de SOX) · <strong>Loi Breton</strong> 2005 · Code de commerce (articles L.225-37, L.225-68, L.225-235 sur le rapport de contrôle interne).</p>
    </div>
    <div class="synth-mini">
      <strong>12 vecteurs du guide d'audit gouvernance SI</strong>
      <p>L'AFAI/ISACA décompose l'audit de gouvernance en 12 vecteurs structurants couvrant : la stratégie, l'organisation de la DSI, la gestion des projets, l'exploitation, la sécurité, la conformité, les indicateurs de pilotage, les relations utilisateurs, les achats, la gestion des données. Grille à mobiliser pour structurer une mission d'audit.</p>
    </div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(77,154,168,0.18)">🚀</div> Enjeux numériques actuels
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>RGPD — protection des données</strong>
      <p>Règlement européen 2016 (applicable mai 2018). Impose des obligations : nommer un <strong>DPO</strong> (Délégué à la Protection des Données), tenir un registre des traitements, notifier toute violation à la <strong>CNIL sous 72h</strong> (article 33), réaliser une <strong>PIA</strong> pour les traitements à risque, garantir les droits des personnes (consultation, rectification, portabilité, oubli).</p>
    </div>
    <div class="synth-mini">
      <strong>Facturation électronique 2026-2027</strong>
      <p>Chantier <strong>informatique, financier et managérial</strong>. Les entreprises doivent choisir une <strong>PDP</strong> (Plateforme de Dématérialisation Partenaire) ou utiliser le <strong>PPF</strong> (Portail Public Facturation, ex-Chorus Pro). Formats imposés : Factur-X (PDF/A-3 + XML), UBL, CII. Calendrier graduel : réception septembre 2026, émission GE/ETI 2026 puis PME 2027.</p>
    </div>
    <div class="synth-mini">
      <strong>Intelligence artificielle &amp; SI</strong>
      <p>Apports : automatisation, analyse prédictive, IA générative. Risques : résistance au changement, dépendance technologique, sécurité des données, perte de compétences, biais et hallucinations. Cadre émergent : l'<strong>IA Act européen</strong> classifie les usages par risque (inacceptable / élevé / limité / minimal). Compléments : ISO 42001 (management de l'IA), NIST AI RMF.</p>
    </div>
    <div class="synth-mini">
      <strong>Dématérialisation des bulletins de paie</strong>
      <p>63 % des travailleurs reçoivent leur fiche en numérique en 2024 (vs 42 % en 2020). Conservation imposée pendant <strong>50 ans</strong> dans un <strong>coffre-fort numérique</strong>. Obligations : intégrité, authenticité, disponibilité, non-répudiation, hébergement souverain (France/UE). Risques : vol de données, défiance des salariés (80 % expriment des préoccupations).</p>
    </div>
  </div>
</div>

`;
}
'''


RSE_SYNTH = '''function getSynthHTML() {
  return `

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(90,145,104,0.18)">🌱</div> Fondamentaux de la RSE
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>Définition de la RSE</strong>
      <p>La RSE est la <strong>prise en compte volontaire</strong> par l'entreprise de son <strong>impact environnemental et sociétal</strong>, en plus de sa performance financière. Ce n'est ni une réglementation, ni un label, ni une « Réglementation Sociétale » qui n'existe pas. C'est une démarche d'entreprise, qui peut être soutenue par des outils (CSRD, labels…).</p>
    </div>
    <div class="synth-mini">
      <strong>Les 3 piliers du Développement Durable</strong>
      <p>Confirmés au Sommet de Johannesburg (2002, 10 ans après Rio 1992) : ① <strong>Sphère économique</strong> (viabilité, création de valeur durable) · ② <strong>Sphère sociale</strong> (équité, conditions de travail, droits humains) · ③ <strong>Sphère environnementale</strong> (préservation des ressources, climat, biodiversité). Le DD se trouve à l'intersection des trois.</p>
    </div>
    <div class="synth-mini">
      <strong>Théorie du Donut (Kate Raworth, 2010)</strong>
      <p>Image d'un anneau entre deux cercles : à l'intérieur, le <strong>plancher social</strong> (besoins humains : santé, éducation, eau, énergie, équité, expression…) ; à l'extérieur, le <strong>plafond planétaire</strong> (les 9 limites planétaires : climat, biodiversité, azote, eau douce, ozone…). L'objectif : faire tenir l'humanité dans cet espace juste et sûr.</p>
    </div>
    <div class="synth-mini">
      <strong>Global Compact ONU (Kofi Annan, 2000)</strong>
      <p>Initiative volontaire : engagement à respecter <strong>10 principes</strong> structurés en 4 piliers : Droits de l'Homme (2 principes) · Normes du travail (4 principes : liberté syndicale, abolition du travail forcé / des enfants, non-discrimination) · Environnement (3 principes dont la précaution) · Lutte contre la corruption (1 principe). Plus de 20 000 entreprises adhérentes mondialement.</p>
    </div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(61,114,180,0.18)">📋</div> CSRD &amp; ESRS — le cadre 2024
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>La directive CSRD</strong>
      <p><strong>Corporate Sustainability Reporting Directive</strong> — directive européenne 2022, applicable progressivement à partir de 2024. Elle généralise et standardise le reporting de durabilité, en remplacement de l'ancienne NFRD. Objectif : rendre les informations extra-financières <strong>comparables, fiables et utiles</strong> aux investisseurs. Outil du Green Deal européen.</p>
    </div>
    <div class="synth-mini">
      <strong>Les 12 normes ESRS</strong>
      <p>Les <strong>European Sustainability Reporting Standards</strong> structurent le reporting CSRD. 2 normes transversales (ESRS 1 « Exigences générales », ESRS 2 « Disclosures généraux »), 5 normes Environnementales (E1 Climat, E2 Pollution, E3 Eau, E4 Biodiversité, E5 Économie circulaire), 4 Sociales (S1 Effectifs propres, S2 Chaîne de valeur, S3 Communautés, S4 Consommateurs), 1 Gouvernance (G1 Conduite des affaires).</p>
    </div>
    <div class="synth-mini">
      <strong>Les 4 piliers de l'ESRS 1 — la grille à connaître</strong>
      <p>L'ESRS 1 organise l'information autour de 4 piliers transversaux applicables à toutes les ESRS : ① <strong>GOV</strong> Gouvernance (rôle des organes de direction, contrôle interne) · ② <strong>SBM</strong> Stratégie &amp; Business Model · ③ <strong>IRO</strong> Impacts / Risques / Opportunités · ④ <strong>MT</strong> Metrics &amp; Targets (indicateurs et cibles).</p>
    </div>
    <div class="synth-mini">
      <strong>Les 82 Disclosure Requirements</strong>
      <p>La CSRD impose 82 DR au total : 12 dans ESRS 2 (BP-1/2, GOV-1 à GOV-5, SBM-1 à SBM-3, IRO-1/2) + 32 environnementaux (dont E1 = 9 DR) + 32 sociaux (dont S1 = 17 DR) + 6 gouvernance (G1). Cette granularité est ce qui rend la CSRD si exigeante par rapport à l'ancien régime.</p>
    </div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(200,131,70,0.18)">⚖️</div> Double matérialité &amp; rapport de durabilité
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>De la matérialité simple à la double</strong>
      <p>L'ancienne matérialité (NFRD 2014) analysait uniquement l'<strong>impact des enjeux RSE sur la performance financière</strong> de l'entreprise. Avec la CSRD, on bascule en 2022 vers la <strong>double matérialité</strong>, principe fondamental qui demande deux analyses combinées.</p>
    </div>
    <div class="synth-mini">
      <strong>Les deux axes de la double matérialité</strong>
      <p>① <strong>Matérialité d'impact</strong> (Inside-Out) : impact de l'entreprise <strong>sur l'environnement et la société</strong> (positifs et négatifs, réels et potentiels). ② <strong>Matérialité financière</strong> (Outside-In) : risques et opportunités ESG qui <strong>affectent financièrement</strong> l'entreprise. Un thème est matériel s'il est significatif sous l'une OU l'autre dimension.</p>
    </div>
    <div class="synth-mini">
      <strong>Le concept IRO</strong>
      <p>Mécanique opératoire de la double matérialité : <strong>Impacts / Risques / Opportunités</strong>. Démarche en 3 étapes (ESRS 1) : ① identifier les IRO sur l'<strong>ensemble de la chaîne de valeur</strong> (amont + propre + aval) · ② évaluer leur matérialité (gravité, probabilité, ampleur, irréversibilité, étendue) · ③ déterminer l'information à publier sur les IRO matériels.</p>
    </div>
    <div class="synth-mini">
      <strong>Rapport de durabilité — assurance limitée</strong>
      <p>Le rapport CSRD est intégré au rapport de gestion et soumis à une <strong>assurance limitée</strong> (formulée négativement : « rien ne nous laisse penser que… »), réalisée par le CAC ou un OTI (Organisme Tiers Indépendant). L'assurance pourrait passer à <strong>raisonnable</strong> à terme. Validité pluriannuelle, sanctions en cas de manquement.</p>
    </div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(176,90,71,0.18)">📅</div> Évolution réglementaire &amp; Omnibus 2025
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>Chronologie réglementaire française</strong>
      <p><strong>NRE</strong> 2001 (premières obligations) → <strong>Grenelle II</strong> 2010 (élargissement) → <strong>DPEF</strong> 2017 (transposition NFRD) → <strong>Loi PACTE</strong> 2019 (raison d'être, société à mission) → <strong>CSRD</strong> 2022. Chaque texte a élargi le périmètre et renforcé les obligations, avant la simplification opérée par l'Omnibus 2025.</p>
    </div>
    <div class="synth-mini">
      <strong>Rapport Draghi 2024 — le déclencheur</strong>
      <p>Le rapport « <em>The future of European competitiveness</em> » de Mario Draghi (septembre 2024) alerte sur la perte de compétitivité européenne face aux États-Unis et à la Chine, mettant en cause une réglementation jugée trop lourde. La Commission européenne réagit en lançant le paquet <strong>Omnibus</strong> en février 2025.</p>
    </div>
    <div class="synth-mini">
      <strong>Omnibus 2025 — CSRD allégée</strong>
      <p>Modifications majeures : <strong>application reportée à 2028</strong> (au lieu de 2026). Seuils relevés à <strong>1 000 salariés / 50 M€ CA / 25 M€ bilan</strong>, ce qui réduit d'environ <strong>80 %</strong> le nombre d'entreprises soumises. Refonte allégée des 12 ESRS, abandon des standards sectoriels, fin de la collecte fournisseurs non-CSRD. <strong>La double matérialité est conservée</strong>.</p>
    </div>
    <div class="synth-mini">
      <strong>Omnibus 2025 — Taxonomie &amp; CS3D</strong>
      <p><strong>Taxonomie</strong> : −70 % d'obligations de reporting + introduction d'un seuil de matérialité financière + création du <strong>Green Asset Ratio</strong> bancaire. <strong>CS3D</strong> (Devoir de vigilance) : limité aux <strong>partenaires directs</strong> de la chaîne de valeur, évaluations tous les <strong>5 ans</strong> (vs annuel), <strong>suppression des sanctions financières proportionnelles au CA</strong> mondial.</p>
    </div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(138,122,168,0.18)">🛠️</div> Démarche RSE &amp; outils
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>Démarche RSE en 6 étapes (cohérente avec la CSRD)</strong>
      <p>① <strong>Déterminer les enjeux RSE</strong> (cartographie parties prenantes, double matérialité, IRO) · ② <strong>Identifier la gouvernance</strong> (engagement direction, CA, organes) · ③ <strong>Définir politique &amp; objectifs SMART</strong> · ④ <strong>Déterminer les actions</strong> · ⑤ <strong>Mesurer la performance</strong> (indicateurs) · ⑥ <strong>Communiquer / reporting</strong> (rapport de durabilité, assurance).</p>
    </div>
    <div class="synth-mini">
      <strong>Société à Mission — Loi PACTE 2019</strong>
      <p>Statut juridique qui permet d'inscrire une <strong>raison d'être</strong> dans les statuts et des <strong>objectifs sociaux et environnementaux</strong> que l'entreprise s'engage à poursuivre. Suivi par un <strong>Comité de Mission</strong> et un OTI qui vérifie l'atteinte des objectifs. Exemples : Danone, MAIF, Camif, Yves Rocher. Outil d'engagement formalisé même sans obligation CSRD.</p>
    </div>
    <div class="synth-mini">
      <strong>VSME (EFRAG) — pour les PME</strong>
      <p>Norme <strong>volontaire</strong> Voluntary SME développée par l'EFRAG pour les PME sous les seuils CSRD qui souhaitent quand même produire un rapport de durabilité (besoin clients, financement, attractivité). 2 modules : <strong>Basic</strong> (essentiel) et <strong>Comprehensive</strong> (complet). Cœur de clientèle des cabinets d'expertise-comptable.</p>
    </div>
    <div class="synth-mini">
      <strong>Label Engagé RSE AFNOR</strong>
      <p>Label structurant pour démarrer une démarche RSE, basé sur la norme ISO 26000. Évalue la maturité de l'entreprise sur 4 niveaux (Engagé → Confirmé → Exemplaire → Leader). Démarche volontaire mais reconnue, particulièrement adaptée aux ETI et PME.</p>
    </div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(77,154,168,0.18)">👔</div> Impact sur la profession comptable
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>Nouvelles missions de l'expert-comptable</strong>
      <p>L'EC devient <strong>tiers de confiance numérique et extra-financier</strong>. Missions émergentes : accompagnement à la démarche RSE, mise en place d'un reporting durabilité, conseil sur le VSME pour les PME, audit interne RSE, formation des dirigeants aux ESRS, calcul des indicateurs ESG, intégration des risques climatiques dans les comptes.</p>
    </div>
    <div class="synth-mini">
      <strong>Le rôle du CAC dans la CSRD</strong>
      <p>Le Commissaire aux Comptes (ou un OTI agréé) émet une <strong>assurance limitée</strong> sur le rapport de durabilité. Il vérifie la conformité aux ESRS, la sincérité des informations publiées, l'absence d'erreurs ou d'incohérences (notamment avec les bilans financiers). Sa mission s'élargit donc au-delà du financier traditionnel.</p>
    </div>
    <div class="synth-mini">
      <strong>Performance financière vs performance RSE</strong>
      <p>Un faux débat. Les études montrent que les politiques RSE bien conçues sont <strong>créatrices de valeur</strong> : elles réduisent le coût du capital (ISR, fonds éthiques), améliorent la résilience face aux crises, attirent les talents et les clients sensibles, anticipent les risques réglementaires. La RSE devient un levier de performance globale et de différenciation stratégique.</p>
    </div>
    <div class="synth-mini">
      <strong>Greenwashing — risques et garde-fous</strong>
      <p>Communication mensongère ou trompeuse sur les performances environnementales (allégations vagues, accent sur un seul critère, labels non certifiés…). Constitue une <strong>pratique commerciale trompeuse</strong> sanctionnée pénalement et civilement. La directive européenne anti-greenwashing (2024) renforce les obligations de preuve scientifique pour toute allégation environnementale.</p>
    </div>
  </div>
</div>

`;
}
'''


STRAT_SYNTH = '''function getSynthHTML() {
  return `

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(61,114,180,0.18)">🎯</div> Stratégie — fondements
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>Définition d'Alfred Chandler (1962)</strong>
      <p>« La stratégie est la <strong>détermination des objectifs à long terme</strong> d'une entreprise et l'adoption des actions et allocations de ressources nécessaires pour atteindre ces objectifs. » Chandler a aussi formulé la fameuse thèse <strong>« structure follows strategy »</strong> : la structure organisationnelle découle des choix stratégiques.</p>
    </div>
    <div class="synth-mini">
      <strong>Définition opérationnelle de Strategor (2020)</strong>
      <p>« Pour une équipe dirigeante, faire de la stratégie consiste à <strong>choisir les activités à réaliser à moyen/long terme et à allouer les ressources</strong> de manière à atteindre un niveau de performance satisfaisant, avec l'objectif de <strong>créer de la valeur pour les parties prenantes</strong>. » Vision moderne et inclusive.</p>
    </div>
    <div class="synth-mini">
      <strong>Faire de la stratégie en 3 actes</strong>
      <p>① <strong>Anticiper</strong> : détecter les signaux faibles et les tendances lourdes qui dessinent les futurs possibles. ② <strong>Diagnostiquer</strong> : analyser l'environnement (« que va-t-il se passer ? ») ET l'organisation (« de quoi serai-je capable ? »). ③ <strong>Choisir et allouer</strong> : décider des activités à développer et des ressources à y consacrer.</p>
    </div>
    <div class="synth-mini">
      <strong>Les 4 formes de la valeur</strong>
      <p>① <strong>Valeur économique</strong> : richesse créée par les activités. ② <strong>Valeur perçue</strong> : perception du client sur les fonctionnalités, la marque, les services associés. ③ <strong>Valeur actionnariale</strong> : richesse créée spécifiquement pour les actionnaires. ④ <strong>Valeur parties prenantes</strong> : appréciabilité et fiabilité pour l'ensemble des stakeholders.</p>
    </div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(200,131,70,0.18)">🧱</div> Business Model &amp; scalabilité
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>Business Model — définition</strong>
      <p>Selon Osterwalder &amp; Pigneur (2011) : description de la manière dont une organisation <strong>crée, délivre et capture de la valeur</strong>. Strategor (2009) le décompose en 3 composantes : la <strong>proposition de valeur</strong>, l'<strong>architecture de valeur</strong> (qui fait quoi, avec quels partenaires) et l'<strong>équation économique</strong> (revenus / coûts / marge).</p>
    </div>
    <div class="synth-mini">
      <strong>Les 9 blocs du Business Model Canvas</strong>
      <p>Outil visuel à 9 blocs : Segments de clientèle · Proposition de valeur · Canaux · Relations clients · Flux de revenus · Ressources clés · Activités clés · Partenaires clés · Structure de coûts. Permet de représenter et de challenger n'importe quel modèle d'affaires sur une seule page.</p>
    </div>
    <div class="synth-mini">
      <strong>Scalabilité — un BM qui passe à l'échelle</strong>
      <p>Capacité d'un Business Model à <strong>croître sans augmentation proportionnelle des coûts</strong>. Indicateurs clés : le <strong>levier opérationnel</strong> (coûts fixes vs variables), le <strong>ratio coût marginal / revenu marginal</strong>, les <strong>économies d'échelle</strong> et de champ. Un BM scalable peut servir des millions de clients sans démultiplier sa structure (Spotify vs école de musique).</p>
    </div>
    <div class="synth-mini">
      <strong>4 critères d'évaluation d'un BM</strong>
      <p>① <strong>Cohérence interne</strong> (les blocs s'alignent) · ② <strong>Robustesse</strong> (résistance aux chocs et à la concurrence) · ③ <strong>Flexibilité</strong> (adaptation au changement) · ④ <strong>Scalabilité</strong> (capacité à croître). Le BM Canvas est valide si ces 4 critères sont satisfaits.</p>
    </div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(90,145,104,0.18)">🌐</div> Les plateformes numériques
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>Définition d'une plateforme</strong>
      <p>Dispositif de <strong>coordination de ressources et d'actions</strong>, contrôlé par un opérateur privé qui en est le chef d'orchestre. Deux caractéristiques nécessaires : chaque groupe (offreurs ET demandeurs) est <strong>client</strong> de la plateforme ; elle permet une <strong>mise en relation directe</strong> entre offreurs et demandeurs. Exemples : Airbnb, Uber, Amazon Marketplace, Apple Store.</p>
    </div>
    <div class="synth-mini">
      <strong>Les 6 mécanismes de Benavent (2016)</strong>
      <p>① <strong>Externalités de réseau et de standard</strong> (loi de Metcalfe : la valeur croît au carré) · ② <strong>Crowdsourcing</strong> (les usagers produisent l'offre) · ③ <strong>Marchés de réputation</strong> (système de notation, confiance) · ④ <strong>Économie de la longue traîne</strong> (variété infinie sans stocks) · ⑤ <strong>Science de l'appariement</strong> (matching offre/demande) · ⑥ <strong>Marchés bifaces voire multifaces</strong> (revenus multiples).</p>
    </div>
    <div class="synth-mini">
      <strong>Les 4 erreurs typiques (Cusumano, 2022)</strong>
      <p>① <strong>Pricing</strong> : mal valoriser une face entraîne un BM cassé. ② <strong>Méfiance</strong> : sans dispositifs de confiance entre acteurs inconnus, le projet échoue (notation, labels, assurances). ③ <strong>Timing</strong> : trop tôt (marché pas prêt) ou trop tard (concurrents établis avec effets de réseau verrouillés). ④ <strong>Orgueil</strong> : croire la partie gagnée après le basculement → MySpace face à Facebook.</p>
    </div>
    <div class="synth-mini">
      <strong>MVP — Minimum Viable Product</strong>
      <p>Mécanisme pour se lancer rapidement : un produit qui ne présente pas encore toutes les caractéristiques du produit final mais qui permet déjà de <strong>générer du chiffre d'affaires et de récolter les retours utilisateurs</strong> pour l'améliorer. Stratégie particulièrement adaptée aux plateformes où le timing est critique.</p>
    </div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(176,90,71,0.18)">⚔️</div> Stratégies concurrentielles (Partie 2)
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>Le modèle des 5 forces de Porter (1985)</strong>
      <p>Analyse de l'intensité concurrentielle d'un secteur via 5 forces : <strong>① Rivalité</strong> entre concurrents, <strong>② Menace des entrants</strong> potentiels (hauteur des barrières à l'entrée), <strong>③ Menace des substituts</strong>, <strong>④ Pouvoir de négociation des clients</strong>, <strong>⑤ Pouvoir de négociation des fournisseurs</strong>. Souvent complété par une 6ᵉ force : démographie / pouvoirs publics.</p>
    </div>
    <div class="synth-mini">
      <strong>L'écosystème d'affaires</strong>
      <p>Pour aller au-delà du modèle de Porter (qui ne montre pas les menaces hors-secteur, comme Google pour la SNCF) : <strong>communauté d'intérêts</strong> constituée d'organisations issues de secteurs différents, co-produisant une prestation, pilotée par un acteur central. Notion-clé : la <strong>coopétition</strong> (coopération + compétition simultanées).</p>
    </div>
    <div class="synth-mini">
      <strong>Le triangle des registres relationnels (Koenig, 2004)</strong>
      <p>Trois logiques fondamentales structurent l'interaction concurrentielle : <strong>Affrontement</strong> (concurrence — guerres de prix, prolifération, préemption, contrôle d'actifs) · <strong>Coopération</strong> (alliances : complémentaire, co-intégration, pseudo-concentration) · <strong>Évitement</strong> (ententes — légitimes ou illégitimes selon Baumard 2000).</p>
    </div>
    <div class="synth-mini">
      <strong>Les 3 types d'alliances</strong>
      <p>① <strong>Alliance complémentaire</strong> : actifs différents, produits spécifiques à chaque allié (ex. Sanofi + GSK vaccin COVID). ② <strong>Alliance de co-intégration</strong> : actifs similaires, un composant commun intégré dans les offres respectives (ex. C1/Aygo/107). ③ <strong>Alliance de pseudo-concentration</strong> : actifs similaires, un produit commun commercialisé en commun (ex. Airbus).</p>
    </div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(138,122,168,0.18)">🏗️</div> Corporate Strategy (Partie 3)
  </div>
  <div class="synth-grid">
    <div class="synth-mini">
      <strong>Évolution historique de la gouvernance</strong>
      <p>① <strong>Gouvernance familiale</strong> (jusqu'au XIXᵉ) — dynasties industrielles Krupp, Schneider, de Dietrich. ② <strong>Gouvernance managériale</strong> (XXᵉ) — séparation propriété/gestion, le dirigeant devient un « manager professionnel ». ③ <strong>Gouvernance actionnariale</strong> (depuis les années 1980) — retour en force des actionnaires : scandales (Enron), fonds de pension, OPCVM.</p>
    </div>
    <div class="synth-mini">
      <strong>Les parties prenantes et leur hiérarchisation</strong>
      <p>Acteurs qui dépendent de l'entreprise et la font fonctionner. Trois types : <strong>internes</strong> (business units, CSE), <strong>interfaces</strong> (CA, AG, syndicats), <strong>externes</strong> (clients, fournisseurs, banques, lobbies). La <strong>matrice de Johnson (2005)</strong> les hiérarchise selon deux axes : Pouvoir × Intérêt → 4 cases (effort minimal / à garder informés / à garder satisfaits / acteurs clés).</p>
    </div>
    <div class="synth-mini">
      <strong>Friedman (1970) vs Freeman — le débat fondateur</strong>
      <p>Milton Friedman (NYT, 1970) : « <strong>La responsabilité sociale des entreprises est d'accroître ses profits.</strong> » Vision <strong>actionnariale pure</strong>. À l'opposé, la théorie des parties prenantes pose que l'entreprise a des responsabilités envers tous ses stakeholders. La pression des ONG et de la réglementation pousse aujourd'hui vers cette seconde vision (CSRD, Loi PACTE, Sociétés à Mission).</p>
    </div>
    <div class="synth-mini">
      <strong>Le modèle MACS de McKinsey</strong>
      <p><strong>Market Activated Corporate Strategy</strong> : matrice de portefeuille moderne croisant deux axes — <strong>Valeur Intrinsèque</strong> de l'activité (cash-flows actualisés) × <strong>Apport Parental</strong> (synergies que le groupe peut apporter). 4 cases : Développer · Conserver · Céder à un meilleur parent · Abandonner. Implémente la logique de l'<strong>avantage parental</strong> : si le groupe ne crée pas de valeur, il faut scinder ou céder.</p>
    </div>
  </div>
</div>

`;
}
'''


def replace_synth(html_file, new_synth):
    path = ROOT / html_file
    text = path.read_text()
    pattern = re.compile(r'function getSynthHTML\(\)\s*\{\s*return\s*`[\s\S]*?`;\s*\}\n', re.MULTILINE)
    if not pattern.search(text):
        raise SystemExit(f'{html_file}: getSynthHTML non trouvé')
    new_text = pattern.sub(new_synth, text, count=1)
    path.write_text(new_text)
    print(f'✓ {html_file} : Synth réécrit en mode fiche de révision complète')


if __name__ == '__main__':
    replace_synth('conduite_chgt.html', CONDUITE_SYNTH)
    replace_synth('evo_orga.html', EVO_SYNTH)
    replace_synth('gouv.html', GOUV_SYNTH)
    replace_synth('rse.html', RSE_SYNTH)
    replace_synth('strat.html', STRAT_SYNTH)
