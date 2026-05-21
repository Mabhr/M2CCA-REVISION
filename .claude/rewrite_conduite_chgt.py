"""Réécrit conduite_chgt.html + data/conduite_chgt.json en suivant strictement
les 2 PDFs Besombes (Conduite du changement 2025 + Gestion des compétences).

SUPPRESSION TOTALE des auteurs/modèles hors-Besombes :
  - ADKAR (Prosci/Hiatt), Beckhard-Harris, Bridges
  - Argyris & Schön, Senge (5 disciplines)
  - Maslow, Herzberg, McGregor (X/Y), Deci & Ryan
  - Spreitzer (empowerment), Schaufeli, Maslach (burn-out)
  - Schein (3 niveaux culture), Hofstede / OCAI
  - Crozier & Friedberg, Fauvet (sociodynamique), Watzlawick
  - Tuckman attribution explicite (les 5 étapes restent, mais sans nommer Tuckman)
  - Tannenbaum-Schmidt attribution explicite
  - Citation Drucker « culture mange stratégie »
  - Kotter 8 étapes détaillées (Besombes affiche juste le titre)
  - Lewin champs de force (Besombes mentionne seulement les 3 phases)
  - Kübler-Ross 5 phases détaillées
  - Mintzberg, Porter (étaient des distracteurs)

CONSERVATION Besombes strict (47p + 41p) :
  - processus_chgt : Le Chatelier, Lewin (3 phases), Kotter (titre seul),
                     Kübler-Ross (courbe seule), 3 facteurs psychosociologiques,
                     7 résistances, 5 stratégies anti-résistance, 3 stratégies utiles
  - demarche      : 8 étapes Besombes (Amorcer→S'améliorer), vocation 3 étapes
                     (Écoute/Mobilisation/Coordination), qualification
                     gains/contraintes/appuis/freins, matrice Facilité×Importance
  - acteurs       : Top/Middle/Ressources métiers, 10-80-10, comité pilotage
  - pilotage      : RACI, matrice questions/dispositifs (Communication→Assistance),
                     instance décisionnaire, 10 points clés
  - competences   : description de poste (rôle confié/perçu/accepté/tenu),
                     compétence (savoir/savoir-faire/savoir-être), GPEC,
                     éthique performance, organisation qualifiante,
                     système d'évaluation (sanction/formative),
                     3 missionnements × 3 appréciations
  - equipe        : 5 étapes constitution (non nommé Tuckman), continuum directif/
                     délégatif (non nommé Tannenbaum), Pertinence/Cap/Actions/
                     Ressources, 4 attentes manager, agilité, Gilbert 1980
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / 'conduite_chgt.html'
JSON = ROOT / 'data' / 'conduite_chgt.json'


# ═══════════════════════════════════════════════════════════════════════════
# NOUVEAU CONTENU getCoursHTML — 11 chapitres Besombes uniquement
# ═══════════════════════════════════════════════════════════════════════════
NEW_COURS = '''function getCoursHTML() {
  return `

<div class="course-chapter" data-theme="processus_chgt" data-chap-idx="1" id="chap-1">
  <h2>1. Les processus du changement — la Loi de Le Chatelier</h2>
  <div class="def-box">
    <div class="def-label">Loi de Le Chatelier (analogie fondatrice)</div>
    <p>« <strong>Toute modification apportée à l'équilibre d'un système entraîne au sein de celui-ci l'apparition de phénomènes qui tendent à s'opposer à cette modification et à en annuler les effets.</strong> »</p>
    <p>Cette loi physique sert d'analogie pour comprendre la résistance naturelle des organisations face au changement.</p>
  </div>
  <h3>Conséquence pratique pour conduire un changement</h3>
  <div class="key-box">
    Pour réussir un changement, il faut modifier cet équilibre <strong>dans un sens délibéré</strong>. Deux propositions se présentent :
    <ul>
      <li><strong>Augmenter les pressions</strong> dans le sens du changement</li>
      <li><strong>Diminuer les résistances</strong> envers ce même changement</li>
    </ul>
    <p style="margin-top:0.6rem"><strong>La bonne pratique : associer les deux.</strong></p>
  </div>
</div>

<div class="course-chapter" data-theme="processus_chgt" data-chap-idx="2" id="chap-2">
  <h2>2. Les processus de changement selon Kurt Lewin</h2>
  <div class="def-box">
    <div class="def-label">Modèle de Lewin — 3 phases</div>
    <p>Kurt Lewin a modélisé le changement organisationnel en <strong>3 phases successives</strong> :</p>
  </div>
  <table class="comp-table">
    <thead><tr><th>Phase</th><th>Contenu</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>① Décristallisation</strong></td>
        <td>Préparation au changement. <strong>Remise en cause du fonctionnement actuel</strong>.</td>
      </tr>
      <tr>
        <td><strong>② Changement</strong></td>
        <td>Changement en tant que tel : <strong>modifications des tâches, de la structure, des techniques et du comportement des individus</strong>.</td>
      </tr>
      <tr>
        <td><strong>③ Cristallisation</strong></td>
        <td><strong>Renforcement positif des résultats souhaités</strong> : évaluation des résultats et suivi.</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="course-chapter" data-theme="processus_chgt" data-chap-idx="3" id="chap-3">
  <h2>3. Autres modèles évoqués — Kotter & Kübler-Ross</h2>
  <div class="key-box">
    <strong>⚠️ Note méthodologique</strong> — Le support du prof mentionne ces 2 modèles sans les détailler. Ils sont indiqués comme références à connaître. La présentation suivante reste donc volontairement synthétique.
  </div>

  <h3>Modèle de Kotter</h3>
  <div class="def-box">
    <p>Le <strong>modèle de Kotter</strong> est mentionné comme référence en conduite du changement. Le support de Besombes l'évoque par son titre, sans détailler les 8 étapes classiquement associées à ce modèle. C'est un modèle à mobiliser lors d'une question d'examen sur les démarches structurées.</p>
  </div>

  <h3>Modèle de Kübler-Ross — la courbe du changement</h3>
  <div class="def-box">
    <p>Le <strong>modèle de Kübler-Ross</strong>, présenté via la « courbe du changement » (schéma Philippe Moret), permet de comprendre les <strong>réactions émotionnelles des acteurs</strong> face au changement.</p>
    <p>Comme pour Kotter, le support ne détaille pas les phases ; il indique la courbe comme outil de lecture des processus d'adhésion / de deuil organisationnels.</p>
  </div>
</div>

<div class="course-chapter" data-theme="processus_chgt" data-chap-idx="4" id="chap-4">
  <h2>4. Facteurs psychosociologiques, résistances et stratégies</h2>

  <h3>Les 3 facteurs psychosociologiques du changement</h3>
  <div class="key-box">
    <ol>
      <li>La <strong>découverte chez autrui d'attitudes sociales différentes</strong> des nôtres</li>
      <li>La <strong>découverte de l'image de soi vue par les autres</strong>, bien différente de ce que nous pensions être</li>
      <li>La <strong>découverte d'un nouveau sens à un mot</strong>, nous qui prenions notre sens pour la vérité absolue</li>
    </ol>
  </div>

  <h3>Les 7 résistances au changement</h3>
  <div class="key-box">
    <ol>
      <li><strong>Manque d'informations</strong> des collaborateurs</li>
      <li><strong>Peur de l'inconnu</strong></li>
      <li><strong>Besoin de sécurité</strong></li>
      <li><strong>Besoin de changement inexistant</strong></li>
      <li><strong>Peur de perdre des acquis</strong></li>
      <li><strong>Moment mal choisi</strong></li>
      <li><strong>Manque de ressources</strong></li>
    </ol>
  </div>

  <h3>Lutter contre les résistances — 5 leviers</h3>
  <table class="comp-table">
    <thead><tr><th>Levier</th><th>Pratique</th></tr></thead>
    <tbody>
      <tr><td><strong>① Communiquer</strong></td><td>Éliminer les craintes liées à l'incertitude · informer suffisamment et expliquer clairement le but visé</td></tr>
      <tr><td><strong>② Faire participer</strong></td><td>Créer un sentiment d'engagement · impliquer de la planification à la réalisation</td></tr>
      <tr><td><strong>③ Soutenir</strong></td><td>Assurer la confiance et la crédibilité · consacrer plus de temps aux collaborateurs en difficulté</td></tr>
      <tr><td><strong>④ Négocier</strong></td><td>Éliminer les conflits avec des buts personnels (challenge personnel) · harmoniser les buts et objectifs (cohérence d'ensemble)</td></tr>
    </tbody>
  </table>

  <h3>3 stratégies utiles selon le contexte</h3>
  <table class="comp-table">
    <thead><tr><th>Stratégie</th><th>Mécanisme</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>La coercition</strong></td>
        <td>Réactions par <strong>peur des sanctions</strong> ou par <strong>attrait des récompenses</strong>. Adopter de nouvelles attitudes en s'appuyant sur l'autorité que confère le poste.</td>
      </tr>
      <tr>
        <td><strong>La persuasion rationnelle</strong></td>
        <td>Individus essentiellement rationnels — leurs actes s'appuient sur la logique. Fait appel au <strong>pouvoir lié à la compétence</strong> pour convaincre.</td>
      </tr>
      <tr>
        <td><strong>Le partage de pouvoir</strong></td>
        <td>La <strong>responsabilisation</strong> comme facteur de motivation. Implication des personnes dans le processus de changement.</td>
      </tr>
    </tbody>
  </table>
  <div class="example-box">
    <strong>Limites de la dynamique de groupe</strong> — Chacune des solutions est au gré des dirigeants ; chacune ayant ses avantages et inconvénients selon le moment. C'est <strong>une question de discernement et de philosophie de gestion</strong>. Attention : <em>désir de participer à condition de ne pas perdre d'autonomie</em>.
  </div>
</div>

<div class="course-chapter" data-theme="demarche" data-chap-idx="5" id="chap-5">
  <h2>5. L'univers du changement et la démarche en 8 étapes (Besombes)</h2>

  <h3>L'univers du changement — 4 dimensions</h3>
  <div class="def-box">
    Le <strong>management du changement</strong> s'inscrit dans 4 dimensions interconnectées :
    <ul>
      <li><strong>Stratégie</strong></li>
      <li><strong>Méthodes et activités</strong></li>
      <li><strong>Collaborateurs</strong></li>
      <li><strong>Partenaires externes</strong></li>
    </ul>
  </div>

  <h3>La démarche Besombes — 8 étapes</h3>
  <table class="comp-table">
    <thead><tr><th>Étape</th><th>Action</th><th>Détail</th></tr></thead>
    <tbody>
      <tr><td><strong>① Amorcer</strong></td><td>Définir une stratégie / politique</td><td>Analyser facteurs internes (organisation actuelle, compétences disponibles) et externes (demande clients, prospective, autres acteurs)</td></tr>
      <tr><td><strong>② Analyser l'existant</strong></td><td>Diagnostic</td><td>Identification forces/faiblesses · cartographie relations services/individus · prise en compte mode classement information · résultats qualitatifs détenus</td></tr>
      <tr><td><strong>③ Définir le nouveau cadre</strong></td><td>Innover, objectifs opérationnels</td><td>Documentation centralisée · carte des compétences · fiches prestations · programme de formation · stratégie de communication · outils de pilotage</td></tr>
      <tr><td><strong>④ Mobiliser</strong></td><td>Mobiliser les acteurs</td><td>Sensibilisation collective + individuelle · s'assurer de la compréhension · former aux nouvelles méthodes · définir règles du jeu, modalités d'évaluation, méthodes de soutien</td></tr>
      <tr><td><strong>⑤ Élaborer les plans d'actions</strong></td><td>Hiérarchiser, planifier</td><td>Hiérarchiser les actions · définir le calendrier · nommer les responsables · répartir les équipes · définir temps d'échanges et indicateurs de pilotage</td></tr>
      <tr><td><strong>⑥ Mise en œuvre</strong></td><td>Déployer</td><td>S'assurer du bon déroulement · rester vigilant et en appui des équipes · contrôler dérives · respecter délais</td></tr>
      <tr><td><strong>⑦ Mesurer et évaluer</strong></td><td>Mesurer résultats</td><td>Mesurer les résultats · constater écarts positifs/négatifs · corriger · informer collaborateurs · motiver</td></tr>
      <tr><td><strong>⑧ S'améliorer</strong></td><td>Boucler la démarche</td><td>Associer l'équipe à la réflexion · fixer nouveaux objectifs · responsabiliser · envisager nouvelles actions</td></tr>
    </tbody>
  </table>

  <h3>Qui fait quoi ? — gouvernance projet</h3>
  <div class="key-box">
    <ul>
      <li><strong>Direction</strong> : Projet stratégique</li>
      <li><strong>Comité de pilotage projet</strong> : Gestion participative</li>
      <li><strong>Groupes de travail</strong> : exécution opérationnelle (4 groupes typiques)</li>
    </ul>
  </div>

  <h3>Quel temps ?</h3>
  <div class="example-box">
    Pour réaliser ce parcours de l'étape 1 à l'étape 7 il faut envisager une période de <strong>2 ans en moyenne — ni trop, ni trop peu</strong>.
  </div>

  <h3>Outils nécessaires</h3>
  <div class="key-box">
    <ul>
      <li>Base expert d'informations qualifiées</li>
      <li>Fiches produits</li>
      <li>Outils de communication</li>
      <li>Référentiels de formation</li>
      <li>Cartographie</li>
      <li>Outils d'aide à la décision (observatoire, fichier qualifié)</li>
    </ul>
  </div>
</div>

<div class="course-chapter" data-theme="demarche" data-chap-idx="6" id="chap-6">
  <h2>6. La vocation de la conduite du changement — 3 grandes étapes</h2>
  <div class="def-box">
    <div class="def-label">Chaîne de valeur de la conduite du changement (Besombes)</div>
    <p>De la <strong>Problématique</strong> au <strong>Changement</strong> en passant par 3 étapes structurantes :</p>
    <ul>
      <li><strong>Garantir la bonne compréhension</strong> et la pertinence de la problématique → Écoute · Propositions · Échanges</li>
      <li><strong>Fédérer les parties prenantes</strong> autour d'un périmètre commun → Mobilisation · Priorisation · Structuration · Alignement</li>
      <li><strong>Faciliter la mise en œuvre</strong> du changement → Coordination · Communication · Accompagnement</li>
    </ul>
  </div>

  <h3>Étape 1 — Écouter et comprendre</h3>
  <div class="key-box">
    <ul>
      <li>Écouter <strong>ceux qui ont formulé la problématique</strong>, mais aussi ceux qui peuvent y être confrontés</li>
      <li>Plutôt <strong>en face à face et individuellement</strong></li>
      <li>Pour <strong>comprendre la problématique</strong>, mesurer les <strong>écarts d'angles de vue</strong> et de motivation</li>
      <li>Évaluer la <strong>hauteur de la marche à franchir</strong></li>
      <li>Capter (sans censurer) les idées, propositions, suggestions</li>
      <li>Instaurer un <strong>dialogue et une relation de confiance</strong></li>
      <li>Identifier les parties prenantes (managers, sachants, « clients » du changement, contributeurs transverses)</li>
      <li>Formaliser une <strong>synthèse</strong> et la partager avec les décideurs</li>
    </ul>
  </div>

  <h3>Étape 2 — Fédérer autour d'un périmètre commun</h3>
  <div class="key-box">
    <ul>
      <li>Mobiliser les parties prenantes (panel représentatif et légitime)</li>
      <li><strong>Qualifier les solutions</strong> envisageables</li>
      <li>Définir ensemble des <strong>critères de priorisation</strong></li>
      <li>Sélectionner les solutions à mettre en place</li>
      <li>Identifier celles qui pourraient faire l'objet d'un <strong>« Lot 2 »</strong></li>
      <li>Valider ensemble un <strong>plan d'action commun</strong> (« comment passer de la lettre au Père Noël à un projet collectif »)</li>
    </ul>
  </div>

  <h4>Comment qualifier les solutions — grille à 4 cases</h4>
  <table class="comp-table">
    <thead><tr><th></th><th>Favorable</th><th>Défavorable</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>Résultats</strong></td>
        <td><strong>Gains attendus</strong> : gain de temps, productivité, niveau de service, qualité, fiabilité</td>
        <td><strong>Contraintes</strong> : éléments externes sur lesquels on a peu d'emprise mais qui impactent</td>
      </tr>
      <tr>
        <td><strong>Conditions</strong></td>
        <td><strong>Points d'appui</strong> : éléments favorables à utiliser au maximum (sponsor de poids, effet de levier)</td>
        <td><strong>Freins</strong> : éléments qui s'opposent à l'atteinte du résultat (mais sur lesquels on peut agir)</td>
      </tr>
    </tbody>
  </table>

  <h4>Prioriser les pistes — matrice Importance × Facilité</h4>
  <div class="key-box">
    Représentation graphique avec en abscisses la <strong>Facilité / Maîtrise</strong> et en ordonnées l'<strong>Importance</strong>. Permet d'identifier les actions à mener en priorité (Importance élevée + Facilité élevée) vs à mettre « au parking » (Importance faible).
  </div>

  <h3>Étape 3 — Faciliter la mise en œuvre</h3>
  <div class="key-box">
    <ul>
      <li>Construire la <strong>structure qui permettra de piloter</strong> et coordonner les actions</li>
      <li>Constitution d'une équipe de <strong>correspondants métiers</strong></li>
      <li>Répartition des rôles + cellule de coordination</li>
      <li>Initialisation d'un <strong>plan de communication</strong></li>
      <li>Indicateurs de pilotage</li>
      <li>Validation par les décideurs (structure et ressources)</li>
      <li>Communiquer rapidement pour : expliquer et vendre la cible, donner du sens, rassurer, informer sur la suite</li>
    </ul>
  </div>
</div>

<div class="course-chapter" data-theme="acteurs" data-chap-idx="7" id="chap-7">
  <h2>7. Les acteurs face au changement</h2>

  <h3>3 types de comportements face au changement</h3>
  <table class="comp-table">
    <thead><tr><th>Catégorie</th><th>%</th><th>Profil</th><th>Action recommandée</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>Les PROACTIFS (constructifs)</strong></td>
        <td>10 à 20 %</td>
        <td>Favorables au changement, se positionnent comme <strong>prescripteurs</strong></td>
        <td><strong>Les utiliser</strong></td>
      </tr>
      <tr>
        <td><strong>Les PASSIFS (hésitants)</strong></td>
        <td>60 à 80 %</td>
        <td>En attente de résultats probants, veulent <strong>être sécurisés</strong></td>
        <td><strong>Les rassurer</strong></td>
      </tr>
      <tr>
        <td><strong>Les OPPOSANTS (destructeurs)</strong></td>
        <td>10 à 20 %</td>
        <td>Opposés aux projets, avancent systématiquement des <strong>arguments « contre »</strong></td>
        <td><strong>Les laisser s'isoler</strong> pour mieux les raccrocher</td>
      </tr>
    </tbody>
  </table>

  <h3>3 niveaux d'acteurs pour accompagner le changement</h3>
  <div class="key-box">
    <strong>① S'appuyer sur le Top Management</strong> pour donner l'<strong>impulsion et la légitimité</strong> :
    <ul>
      <li>Montrer à tous que le projet est moteur pour l'organisation</li>
      <li>Prendre les décisions importantes et les communiquer</li>
      <li>… ce qui suppose que le Top Management est <strong>impliqué et motivé</strong></li>
    </ul>
  </div>
  <div class="key-box">
    <strong>② Puis sur le Middle Management opérationnel</strong> pour <strong>relayer</strong> :
    <ul>
      <li>S'impliquer dans les actions de communication</li>
      <li>Intégrer les changements dans le management au quotidien</li>
      <li>Contribuer à l'accompagnement post-déploiement</li>
      <li>… ce qui suppose que le Management de proximité bénéficie d'un <strong>temps d'avance</strong></li>
    </ul>
  </div>
  <div class="key-box">
    <strong>③ Miser sur des Ressources Métiers</strong> pour accompagner le changement :
    <ul>
      <li>Ils <strong>connaissent l'organisation</strong></li>
      <li>Ils sont <strong>légitimes</strong></li>
      <li>Ils <strong>resteront</strong></li>
      <li>… ce qui suppose de les mobiliser et de les animer le plus en amont possible, puis de les accompagner dans ce rôle</li>
    </ul>
  </div>
</div>

<div class="course-chapter" data-theme="pilotage" data-chap-idx="8" id="chap-8">
  <h2>8. Outils opérationnels : RACI, matrices et grille communication</h2>

  <h3>La méthode RACI</h3>
  <div class="def-box">
    <div class="def-label">RACI — 4 rôles par activité</div>
    <ul>
      <li><strong>R : Responsable (1 et un seul par activité)</strong> — Donne son approbation, et assume la responsabilité globale de l'activité et ses conséquences</li>
      <li><strong>A : Acteur (1 à n par étape)</strong> — Réalise les activités</li>
      <li><strong>C : Contribution (0 à n par étape)</strong> — Dispose d'une information / d'une expertise pour la réalisation de l'activité, mais n'a pas d'autorité sur celle-ci (c'est R qui décide)</li>
      <li><strong>I : Information (0 à n par étape)</strong> — Informé de l'activité, sans avoir d'intervention dans sa réalisation (est généralement indirectement impacté)</li>
    </ul>
  </div>

  <h3>Identifier les impacts organisationnels</h3>
  <div class="key-box">
    <ol>
      <li>Identifier les impacts <strong>par processus / sous-processus</strong></li>
      <li>Identifier les <strong>scénarios</strong> et formuler une recommandation, puis faire arbitrer</li>
      <li><strong>Formaliser le RACI</strong> par processus</li>
    </ol>
  </div>

  <h3>Grille communication × dispositif (suivre les questions des acteurs)</h3>
  <table class="comp-table">
    <thead><tr><th>Question posée par l'acteur</th><th>Dispositif à mettre en œuvre</th></tr></thead>
    <tbody>
      <tr><td><strong>« Pourquoi changer ? »</strong></td><td>Communication projet · Kits de communication</td></tr>
      <tr><td><strong>« Comment ça va se passer ? »</strong></td><td>Information ciblée par métier, domaine, fonction, rôle</td></tr>
      <tr><td><strong>« Qu'est-ce qui change pour moi ? »</strong></td><td>Modules de sensibilisation</td></tr>
      <tr><td><strong>« Vais-je être à la hauteur ? »</strong></td><td>Formation aux nouveautés (outils, processus, comportements)</td></tr>
      <tr><td><strong>« Comment vais-je faire ? »</strong></td><td>Modules de formation</td></tr>
      <tr><td><strong>« Suis-je prêt ? »</strong></td><td>Entraînement libre ou encadré</td></tr>
      <tr><td><strong>« Je ne suis pas prêt ! »</strong></td><td>Assistance de proximité</td></tr>
      <tr><td><strong>« Comment faire encore mieux ? »</strong></td><td>Assistance à distance + Management au quotidien</td></tr>
    </tbody>
  </table>

  <h3>Piloter le changement — préalable</h3>
  <div class="key-box">
    Constituer une <strong>instance décisionnaire dédiée à l'accompagnement du changement</strong> qui couvre :
    <ul>
      <li>Cohérence avec les orientations stratégiques</li>
      <li>Indicateurs à suivre</li>
      <li>Ressources nécessaires, relais terrain</li>
      <li>Tactique de déploiement</li>
      <li>Coordination équipe projet</li>
      <li>Planification, suivi du plan d'action</li>
      <li>Déploiement des actions de communication clés</li>
      <li>Alertes et risques</li>
    </ul>
  </div>

  <h3>Matrice de décision &amp; Matrice d'impact</h3>
  <div class="example-box">
    Le support s'appuie sur 2 outils visuels : la <strong>matrice de décision (vote pour décider)</strong> et la <strong>matrice d'impact</strong>, utilisées pour arbitrer entre options et qualifier les conséquences organisationnelles.
  </div>
</div>

<div class="course-chapter" data-theme="pilotage" data-chap-idx="9" id="chap-9">
  <h2>9. Les 10 points clés de la conduite du changement (Besombes)</h2>
  <div class="key-box">
    <ol>
      <li><strong>Faire participer les acteurs clés</strong> — savoir les identifier, puis les mobiliser</li>
      <li><strong>Rester factuel</strong> — écouter, comprendre, restituer, donner les moyens de qualifier et prioriser</li>
      <li><strong>Être réaliste</strong> — tenir compte de la capacité de changement du terrain, voire de son envie de changement</li>
      <li><strong>Communiquer « honnête » et « utile »</strong> — sans noyer sous un flot d'information</li>
      <li><strong>Faciliter la coordination des projets</strong> — afin de contribuer à la stratégie</li>
      <li><strong>Accompagner le changement</strong> — en tenant compte du processus de « deuil » des collaborateurs</li>
      <li><strong>Mesurer les impacts</strong> d'un projet et l'ampleur du changement — avant de décider « quoi communiquer » ou « qui sensibiliser et former à quoi »</li>
      <li><strong>S'appuyer sur une méthodologie structurée et rassurante</strong> pour garantir l'appropriation des changements</li>
      <li><strong>S'appuyer sur la Direction Générale</strong> pour donner l'impulsion et la légitimité, puis sur le middle management opérationnel pour relayer</li>
      <li><strong>S'appuyer sur des ressources métiers internes</strong> pour accompagner le changement — et les « chouchouter »</li>
    </ol>
  </div>
  <div class="def-box" style="text-align:center; margin-top:1.5rem;">
    <p style="font-style:italic;">« La conduite du changement repose moins sur une méthode magique que sur une <strong>discipline d'écoute, de coordination et d'accompagnement</strong>, articulée autour d'une démarche structurée et de quelques outils robustes. »</p>
  </div>
</div>

<div class="course-chapter" data-theme="competences" data-chap-idx="10" id="chap-10">
  <h2>10. La gestion des compétences — fondamentaux Besombes</h2>

  <h3>De la description de poste à la performance — chaîne des rôles</h3>
  <div class="def-box">
    <div class="def-label">Traitement et exploitation des descriptions de poste</div>
    <p>4 rôles successifs définissent la performance organisationnelle :</p>
    <ul>
      <li><strong>Rôle confié</strong> (par l'organisation)</li>
      <li><strong>Rôle perçu</strong> (par le salarié)</li>
      <li><strong>Rôle accepté</strong> (par le salarié)</li>
      <li><strong>Rôle tenu</strong> (effectivement)</li>
    </ul>
    <p style="margin-top:0.6rem">La <strong>description de poste</strong> permet de minimiser l'<strong>écart d'efficacité</strong> entre rôle confié et rôle tenu.</p>
  </div>

  <h3>Pourquoi la gestion des compétences est devenue critique</h3>
  <div class="key-box">
    Les entreprises doivent en permanence se remettre en cause, tant leur environnement est soumis à des <strong>mutations importantes</strong>. L'organisation doit être <strong>aussi réactive que possible</strong> et permettre le développement des initiatives conduisant à l'obtention de la performance.
  </div>
  <h4>Problèmes RH actuels</h4>
  <div class="key-box">
    <ul>
      <li><strong>Transformation des niveaux de qualifications</strong></li>
      <li><strong>Modification de la structure de population</strong> (âge, niveau…)</li>
      <li><strong>Modification du comportement</strong></li>
      <li><strong>Départs / promotions</strong></li>
      <li><strong>Modification du rapport au travail</strong></li>
    </ul>
  </div>

  <h3>Définition de la compétence</h3>
  <div class="def-box">
    <div class="def-label">La compétence selon Besombes</div>
    <p>« La compétence est une <strong>disposition à mobiliser, à combiner et mettre en œuvre des ressources</strong> (savoir, savoir-faire, savoir-être). C'est la <strong>combinaison dynamique</strong> de différents éléments. »</p>
    <ul>
      <li><strong>Savoir théorique</strong></li>
      <li><strong>Procédures et / ou bonnes pratiques</strong></li>
      <li><strong>Savoir-faire</strong></li>
      <li><strong>Expérience non formalisée</strong></li>
    </ul>
  </div>

  <h3>Identification des compétences</h3>
  <div class="key-box">
    <strong>Méthode 1 — Selon le potentiel estimé</strong> (5 critères) :
    <ol>
      <li>Motivation</li>
      <li>Caractère</li>
      <li>Image que l'on a de soi</li>
      <li>Les connaissances et le savoir</li>
      <li>Le savoir-faire</li>
    </ol>
    <p style="margin-top:0.6rem"><em>Il est préférable d'embaucher quelqu'un qui a 1, 2, 3 et de le former à 4 et 5.</em></p>
  </div>
  <div class="key-box">
    <strong>Méthode 2 — L'approche par les compétences professionnelles</strong> :
    <ul>
      <li>Les compétences sont définies par leur <strong>contenu en termes de savoir</strong></li>
      <li>Permet de rapprocher les <strong>diplômes souhaités dans les référentiels d'emplois</strong></li>
    </ul>
  </div>

  <h3>Compétences selon l'objectif poursuivi</h3>
  <div class="key-box">
    <strong>Identification des compétences nécessaires</strong> :
    <ul>
      <li>Établir un <strong>référentiel des métiers ou des emplois</strong>, élaboré soit dans le cadre d'une réflexion menée dans l'entreprise, soit provenant de l'extérieur et adapté</li>
      <li>Indication du <strong>niveau de maîtrise sur 4 à 5 niveaux</strong></li>
    </ul>
  </div>
  <div class="key-box">
    <strong>Identification des compétences détenues</strong> — 4 outils :
    <ul>
      <li><strong>Mesure de l'employabilité individuelle</strong></li>
      <li><strong>Bilan de compétences</strong></li>
      <li><strong>Portefeuille de compétences</strong></li>
      <li><strong>Cartes de compétences</strong></li>
    </ul>
  </div>
</div>

<div class="course-chapter" data-theme="competences" data-chap-idx="11" id="chap-11">
  <h2>11. GPEC, organisation qualifiante et systèmes d'évaluation</h2>

  <h3>GPEC — Gestion Prévisionnelle des Emplois et des Compétences</h3>
  <div class="def-box">
    <div class="def-label">Objectif de la GPEC</div>
    <p>Vise à <strong>réduire, de façon anticipée, les écarts entre les besoins et les ressources</strong> de l'entreprise en termes d'effectifs et de compétences en fonction des objectifs identifiés, avec l'<strong>implication du salarié</strong> dans le cadre d'un projet d'évolution professionnelle.</p>
  </div>

  <h3>Éthique de performance</h3>
  <div class="key-box">
    L'<strong>éthique de performance</strong> repose sur un triangle :
    <ul>
      <li><strong>Actionnaires</strong> (stratégie, vision)</li>
      <li><strong>Salariés</strong> (création de valeur)</li>
      <li><strong>Clients</strong> (profits)</li>
    </ul>
    Au centre : la <strong>Direction</strong> assure l'équilibre permanent et la constance de l'objectif stratégique.
  </div>

  <h3>L'organisation qualifiante</h3>
  <div class="def-box">
    <p>L'<strong>organisation qualifiante</strong> repose sur 3 piliers :</p>
    <ul>
      <li><strong>Enrichissement des tâches</strong></li>
      <li><strong>Volonté éducative</strong> (développement de l'apprentissage permanent)</li>
      <li><strong>Recherche de la compétitivité</strong></li>
    </ul>
  </div>
  <div class="key-box">
    <strong>Éléments préalables</strong> :
    <ul>
      <li>Identification et connaissance des emplois actuels (résultats attendus, compétences requises via <strong>dictionnaire de compétences</strong>)</li>
      <li>Prévision raisonnable et réaliste de l'évolution de l'emploi</li>
    </ul>
    <strong>Mise en œuvre</strong> : travailler sur l'organisation en tenant compte
    <ul>
      <li>Des compétences existantes ou pouvant être recrutées</li>
      <li>En augmentant le niveau de compétences (plan de formation)</li>
      <li>En faisant évoluer les compétences</li>
    </ul>
  </div>

  <h3>Description de poste — schéma de principe</h3>
  <div class="def-box">
    <p>La <strong>description de poste</strong> est un outil à la fois RH et organisationnel. Distinguons :</p>
    <ul>
      <li><strong>Le poste</strong> (emploi tenu) : unité physiquement identifiable</li>
      <li><strong>La fonction</strong> : activités mises en œuvre tendant vers le même but</li>
    </ul>
  </div>
  <table class="comp-table">
    <thead><tr><th>Rubrique</th><th>Contenu</th></tr></thead>
    <tbody>
      <tr><td><strong>Intitulé du poste</strong></td><td>Nom officiel du poste</td></tr>
      <tr><td><strong>Missions</strong></td><td>Finalités du poste</td></tr>
      <tr><td><strong>Dimensions</strong></td><td>Chiffres significatifs</td></tr>
      <tr><td><strong>Contexte général</strong></td><td>Cadre général de travail, contraintes</td></tr>
      <tr><td><strong>Nature et étendue des activités</strong></td><td>Analyse du cadre d'activité et de ses moyens</td></tr>
      <tr><td><strong>Résultats attendus</strong></td><td>Identification des objectifs</td></tr>
    </tbody>
  </table>

  <h3>Les 3 dimensions des compétences</h3>
  <div class="key-box">
    <strong>① En termes de métier</strong> : connaissances techniques et théoriques · connaissances pratiques et savoir-faire<br>
    <strong>② En termes de management</strong> : compétences relationnelles liées au métier · planification, organisation, coordination, contrôle · direction, animation, motivation<br>
    <strong>③ Orientation vers les résultats</strong> : initiation, autonomie · engagement, sens des responsabilités · sens des priorités et flexibilité · contribution aux axes de progrès
  </div>

  <h3>Les systèmes d'évaluation</h3>
  <div class="def-box">
    <p>L'évaluation des compétences doit s'envisager au regard d'<strong>objectifs à atteindre</strong>. Elle doit mettre en évidence des <strong>écarts à combler</strong> et permettre de fonder des démarches de progrès.</p>
    <p>Inducteur de changement, l'instauration d'un système d'évaluation fait évoluer : <strong>comportements, pratiques managériales, relations d'autorité, mentalités, représentations culturelles</strong>.</p>
  </div>
  <table class="comp-table">
    <thead><tr><th>Vers une évaluation « sanction »</th><th>Vers une évaluation « formative »</th></tr></thead>
    <tbody>
      <tr>
        <td>
          La performance, les résultats. <strong>Outil de mesures</strong> :
          <ul>
            <li>Les objectifs quantitatifs</li>
            <li>Les plans d'actions</li>
            <li>Le management de la performance</li>
          </ul>
        </td>
        <td>
          Les compétences, la tenue du poste. <strong>Outils de mesure</strong> :
          <ul>
            <li>Les orientations développement</li>
          </ul>
        </td>
      </tr>
    </tbody>
  </table>

  <h4>Conditions de mise en œuvre</h4>
  <div class="key-box">
    Pour mettre en œuvre un système d'appréciation, il faut confier aux salariés :
    <ul>
      <li>Des <strong>missions claires</strong></li>
      <li>Des <strong>moyens adaptés</strong></li>
    </ul>
    <strong>3 types de missionnement</strong> :
    <ul>
      <li>Les <strong>directives</strong> (règle, procédure, plan d'action)</li>
      <li>Les <strong>objectifs quantitatifs</strong></li>
      <li>Les <strong>orientations ou objectifs qualitatifs</strong></li>
    </ul>
    <strong>3 types d'appréciation</strong> :
    <ul>
      <li>Le <strong>contrôle</strong></li>
      <li>La <strong>mesure</strong></li>
      <li>L'<strong>appréciation</strong></li>
    </ul>
  </div>

  <h4>Implications du système d'appréciation</h4>
  <div class="key-box">
    La mise en œuvre s'appuyant sur des <strong>entretiens individuels</strong> fait appel à des notions qui relèvent de la <strong>culture d'entreprise</strong>. La démarche doit intégrer :
    <ul>
      <li>La clarification des postes</li>
      <li>La clarification des objectifs</li>
      <li>Des objectifs quantitatifs</li>
      <li>Des plans d'actions formalisés</li>
      <li>L'appréciation des résultats</li>
      <li>La notion de performance</li>
    </ul>
  </div>

  <h3>La culture d'entreprise — 5 forces</h3>
  <div class="def-box">
    La culture d'entreprise repose sur 5 forces :
    <ul>
      <li><strong>Mythes</strong></li>
      <li><strong>Rites</strong></li>
      <li><strong>Identité</strong></li>
      <li><strong>Valeurs</strong></li>
      <li><strong>Histoire</strong></li>
    </ul>
  </div>
</div>

<div class="course-chapter" data-theme="equipe" data-chap-idx="12" id="chap-12">
  <h2>12. L'équipe et le management agile (Besombes)</h2>

  <h3>Les 5 étapes de constitution d'une équipe</h3>
  <table class="comp-table">
    <thead><tr><th>Étape</th><th>Description</th><th>Rôle du manager</th></tr></thead>
    <tbody>
      <tr><td><strong>① CONSTITUTION</strong></td><td>Création de l'équipe, découverte des autres et de la légitimité de chacun, positionnement au sein de l'équipe</td><td>Team Building</td></tr>
      <tr><td><strong>② TENSION</strong></td><td>Confrontation des opinions (parfois violemment), divergences objectives ou irrationnelles, tensions</td><td>Prévention · Gestion des conflits</td></tr>
      <tr><td><strong>③ NORMALISATION</strong></td><td>Acceptation d'un but commun, d'un cadre commun de travail, apparition de règles et structuration de l'équipe</td><td>Négociation</td></tr>
      <tr><td><strong>④ PRODUCTION</strong></td><td>Travail collectif vers le but commun. En marche vers l'efficacité de l'équipe</td><td>Motivation</td></tr>
      <tr><td><strong>⑤ DISSOLUTION</strong></td><td>Dissolution de l'équipe (membres partis, nouveaux arrivants)</td><td>Valorisation</td></tr>
    </tbody>
  </table>

  <h3>Travailler en équipe — définition</h3>
  <div class="def-box">
    <div class="def-label">Définition de l'équipe (selon Lewin)</div>
    <p>« <strong>L'essence d'un groupe est l'interdépendance de chacun de ses membres.</strong> » — Kurt Lewin</p>
    <p>Caractéristiques d'une équipe :</p>
    <ul>
      <li><strong>Objectif commun</strong></li>
      <li><strong>Interaction psychologique</strong></li>
      <li><strong>Existence collective</strong></li>
    </ul>
  </div>

  <h3>Le continuum de management — comportement managérial selon l'autorité</h3>
  <div class="key-box">
    Le management s'inscrit sur un continuum entre <strong>autorité du responsable</strong> et <strong>liberté d'action du groupe</strong>, organisé en 7 niveaux :
    <table class="comp-table">
      <thead><tr><th>Centré sur l'animateur</th><th>Centré sur le groupe</th></tr></thead>
      <tbody>
        <tr><td>AUTORITÉ — directif</td><td>IMPLICATIF — délégation, responsabilisant</td></tr>
        <tr><td>INFORMATION</td><td>NÉGOCIATION</td></tr>
        <tr><td>EXPLICATIF</td><td>EXPLICATIF — concertation</td></tr>
        <tr><td>CONSULTATION</td><td></td></tr>
      </tbody>
    </table>
  </div>

  <h3>Management et responsabilisation — modèle Pertinence / Cap / Actions / Ressources</h3>
  <div class="key-box">
    Pour responsabiliser, articuler 4 dimensions :
    <ul>
      <li><strong>Cap</strong> — Quelle est la destination à atteindre ?</li>
      <li><strong>Actions</strong> — Comment s'y prendre pour atteindre le cap ?</li>
      <li><strong>Ressources</strong> — Avec qui et quoi pour atteindre le cap ?</li>
      <li><strong>Pertinence</strong> — Sens ? Utilité ? Cohérence ?</li>
    </ul>
  </div>

  <h3>Les 4 attentes vis-à-vis du manager</h3>
  <div class="key-box">
    Ce que les managés attendent de leur manager (notamment dans une équipe « nouvelle ») :
    <ol>
      <li><strong>Honnête</strong> — l'intégrité (confiance)</li>
      <li><strong>Compétent</strong> — la compétence (technique &amp; managériale)</li>
      <li><strong>Tourné vers l'avenir</strong> — la vision</li>
      <li><strong>Motivant</strong> — le dynamisme (implication et responsabilisation)</li>
    </ol>
  </div>

  <h3>Agilité managériale</h3>
  <div class="def-box">
    <div class="def-label">Agilité managériale</div>
    <p>La <strong>capacité d'adaptation et d'innovation</strong> mobilisée ensemble face à :</p>
    <ul>
      <li>Quelles problématiques ?</li>
      <li>Quelle résolution de problème ensemble ?</li>
      <li>Quel plan d'actions concerté ?</li>
    </ul>
  </div>

  <h3>Manager n'est pas une fin en soi, c'est un moyen</h3>
  <div class="key-box">
    Manager sert à :
    <ul>
      <li>Réussir un projet ensemble (ou un défi à relever)</li>
      <li>Rester concentré sur l'essentiel (satisfaction du client et des collaborateurs)</li>
      <li>Se connaître soi-même pour entrer en relation et dans une dynamique positive de travail avec l'autre. Être cohérent ensemble.</li>
      <li>La discipline de groupe crée les conditions de la réussite : ses membres formulent ensemble le projet, se mettent d'accord sur les objectifs, définissent une méthode de travail commune, développent des compétences complémentaires à un niveau élevé, s'engagent collectivement à atteindre les résultats souhaités.</li>
    </ul>
  </div>

  <h3>Le Modèle de Gilbert (1980) — triangle de la performance</h3>
  <div class="def-box">
    <div class="def-label">Modèle de Gilbert (1980)</div>
    <p>La <strong>performance</strong> se construit à l'intersection de 3 dimensions :</p>
    <ul>
      <li><strong>OBJECTIFS</strong></li>
      <li><strong>MOYENS</strong></li>
      <li><strong>RÉSULTATS</strong></li>
    </ul>
    Les écarts entre ces sommets définissent :
    <ul>
      <li><strong>Objectifs ↔ Résultats</strong> : Efficacité</li>
      <li><strong>Moyens ↔ Résultats</strong> : Efficience</li>
      <li><strong>Objectifs ↔ Moyens</strong> : Pertinence</li>
    </ul>
  </div>

  <h3>Conclusion — la quête d'équilibre</h3>
  <div class="def-box" style="text-align:center;">
    <p style="font-style:italic;">« La recherche de l'<strong>équilibre entre les besoins en ressources de l'organisation et les ressources prévisibles</strong> conduit à rechercher divers modes d'ajustements internes et externes. »</p>
  </div>
</div>
`;
}
'''


# ═══════════════════════════════════════════════════════════════════════════
# NOUVEAU JSON — themes / flashcards / quiz / checklist Besombes uniquement
# ═══════════════════════════════════════════════════════════════════════════
NEW_THEMES = [
    {"id": "processus_chgt", "icon": "🔄", "label": "Processus du changement (Le Chatelier, Lewin, Kotter, Kübler-Ross)"},
    {"id": "demarche", "icon": "📋", "label": "Démarche en 8 étapes Besombes"},
    {"id": "acteurs", "icon": "👥", "label": "Acteurs face au changement"},
    {"id": "pilotage", "icon": "🧭", "label": "Outils & pilotage (RACI, matrices)"},
    {"id": "competences", "icon": "🎯", "label": "Gestion des compétences"},
    {"id": "equipe", "icon": "🤝", "label": "Équipe & management agile"},
]

NEW_CHECKLIST = [
    {"id": "cc1", "label": "Loi de Le Chatelier — analogie résistance au changement"},
    {"id": "cc2", "label": "Lewin — 3 phases : Décristallisation / Changement / Cristallisation"},
    {"id": "cc3", "label": "Modèle de Kotter (mentionné comme référence à connaître)"},
    {"id": "cc4", "label": "Modèle de Kübler-Ross — courbe du changement (mentionné)"},
    {"id": "cc5", "label": "3 facteurs psychosociologiques du changement"},
    {"id": "cc6", "label": "7 résistances classiques au changement"},
    {"id": "cc7", "label": "4 leviers anti-résistance : Communiquer / Faire participer / Soutenir / Négocier"},
    {"id": "cc8", "label": "3 stratégies utiles : coercition / persuasion rationnelle / partage de pouvoir"},
    {"id": "cc9", "label": "L'univers du changement — 4 dimensions"},
    {"id": "cc10", "label": "Démarche Besombes en 8 étapes (Amorcer → S'améliorer)"},
    {"id": "cc11", "label": "Gouvernance projet — Direction / Comité de pilotage / Groupes de travail"},
    {"id": "cc12", "label": "Vocation conduite du changement — 3 étapes (Écoute / Mobilisation / Coordination)"},
    {"id": "cc13", "label": "Qualifier les solutions — 4 cases (Gains/Contraintes/Appuis/Freins)"},
    {"id": "cc14", "label": "Matrice de priorisation Importance × Facilité"},
    {"id": "cc15", "label": "3 types de comportements 10-80-10 (Proactifs / Passifs / Opposants)"},
    {"id": "cc16", "label": "3 niveaux d'acteurs : Top Management → Middle → Ressources métiers"},
    {"id": "cc17", "label": "Méthode RACI — Responsable / Acteur / Contribution / Information"},
    {"id": "cc18", "label": "Grille communication × dispositif (questions des acteurs → modules)"},
    {"id": "cc19", "label": "Instance décisionnaire dédiée à l'accompagnement"},
    {"id": "cc20", "label": "Les 10 points clés de la conduite du changement"},
    {"id": "cc21", "label": "Chaîne des rôles : confié → perçu → accepté → tenu"},
    {"id": "cc22", "label": "Définition compétence : savoir / savoir-faire / savoir-être (combinaison dynamique)"},
    {"id": "cc23", "label": "5 critères d'identification des compétences par potentiel estimé"},
    {"id": "cc24", "label": "Référentiel des métiers + 4-5 niveaux de maîtrise"},
    {"id": "cc25", "label": "4 outils d'identification des compétences détenues"},
    {"id": "cc26", "label": "GPEC — objectif réduire écarts besoins / ressources"},
    {"id": "cc27", "label": "Éthique de performance — triangle Actionnaires / Salariés / Clients"},
    {"id": "cc28", "label": "Organisation qualifiante — 3 piliers"},
    {"id": "cc29", "label": "Description de poste — 6 rubriques (Intitulé / Missions / Dimensions / Contexte / Activités / Résultats)"},
    {"id": "cc30", "label": "3 dimensions des compétences : métier / management / orientation résultats"},
    {"id": "cc31", "label": "Évaluation sanction vs formative"},
    {"id": "cc32", "label": "3 missionnements × 3 appréciations"},
    {"id": "cc33", "label": "Culture d'entreprise — 5 forces (Mythes / Rites / Identité / Valeurs / Histoire)"},
    {"id": "cc34", "label": "5 étapes constitution d'équipe (Constitution / Tension / Normalisation / Production / Dissolution)"},
    {"id": "cc35", "label": "Définition équipe selon Lewin — interdépendance"},
    {"id": "cc36", "label": "Continuum management directif → délégatif (7 niveaux)"},
    {"id": "cc37", "label": "Modèle Pertinence / Cap / Actions / Ressources"},
    {"id": "cc38", "label": "4 attentes manager — Honnête / Compétent / Tourné vers l'avenir / Motivant"},
    {"id": "cc39", "label": "Agilité managériale — capacité d'adaptation et d'innovation"},
    {"id": "cc40", "label": "Modèle de Gilbert (1980) — Performance = Objectifs / Moyens / Résultats"},
]

NEW_FLASHCARDS = [
    # ═══ processus_chgt ═══
    {"q": "Loi de Le Chatelier appliquée au changement organisationnel", "a": "« Toute modification apportée à l'équilibre d'un système entraîne au sein de celui-ci l'apparition de phénomènes qui tendent à s'opposer à cette modification et à en annuler les effets. »\n\nConséquence : pour réussir un changement, modifier l'équilibre dans un sens délibéré en :\n  • Augmentant les pressions dans le sens du changement\n  • Diminuant les résistances\n\nBonne pratique : associer les deux.", "theme": "processus_chgt"},
    {"q": "Modèle de Kurt Lewin — les 3 phases", "a": "Kurt Lewin a modélisé le changement en 3 phases :\n\n① DÉCRISTALLISATION — préparation au changement, remise en cause du fonctionnement actuel\n\n② CHANGEMENT — modifications des tâches, de la structure, des techniques et du comportement des individus\n\n③ CRISTALLISATION — renforcement positif des résultats souhaités, évaluation et suivi", "theme": "processus_chgt"},
    {"q": "Modèles de Kotter et Kübler-Ross — niveau Besombes", "a": "Le support Besombes mentionne ces 2 modèles comme références à connaître MAIS sans les détailler :\n\n• Kotter — modèle de référence en conduite du changement (titre seul)\n\n• Kübler-Ross — courbe du changement (schéma Philippe Moret) qui permet de comprendre les réactions émotionnelles face au changement (titre + schéma seuls)\n\n→ À mobiliser en examen comme modèles structurants, sans les détailler outre mesure.", "theme": "processus_chgt"},
    {"q": "3 facteurs psychosociologiques du changement", "a": "① La découverte chez autrui d'attitudes sociales différentes des nôtres\n\n② La découverte de l'image de soi vue par les autres, bien différente de ce que nous pensions être\n\n③ La découverte d'un nouveau sens à un mot, nous qui prenions notre sens pour la vérité absolue", "theme": "processus_chgt"},
    {"q": "Les 7 résistances au changement (Besombes)", "a": "① Manque d'informations des collaborateurs\n② Peur de l'inconnu\n③ Besoin de sécurité\n④ Besoin de changement inexistant\n⑤ Peur de perdre des acquis\n⑥ Moment mal choisi\n⑦ Manque de ressources", "theme": "processus_chgt"},
    {"q": "Les 4 leviers pour lutter contre les résistances", "a": "① COMMUNIQUER — éliminer les craintes liées à l'incertitude, expliquer clairement le but visé\n\n② FAIRE PARTICIPER — créer un sentiment d'engagement, impliquer de la planification à la réalisation\n\n③ SOUTENIR — assurer la confiance et la crédibilité, consacrer plus de temps aux collaborateurs en difficulté\n\n④ NÉGOCIER — éliminer les conflits avec des buts personnels, harmoniser objectifs (cohérence d'ensemble)", "theme": "processus_chgt"},
    {"q": "Les 3 stratégies utiles face au changement", "a": "① LA COERCITION — réactions par peur des sanctions ou par attrait des récompenses ; s'appuyer sur l'autorité conférée par le poste\n\n② LA PERSUASION RATIONNELLE — individus essentiellement rationnels, actes basés sur la logique ; appel au pouvoir lié à la compétence\n\n③ LE PARTAGE DE POUVOIR — la responsabilisation comme facteur de motivation ; implication des personnes dans le processus de changement", "theme": "processus_chgt"},
    {"q": "Limites de la dynamique de groupe en situation de changement", "a": "Chacune des solutions est au gré des dirigeants ; chacune ayant ses avantages et inconvénients selon le moment.\n\n→ Question de DISCERNEMENT et de PHILOSOPHIE DE GESTION\n\nAttention au paradoxe : désir de participer à condition de ne pas perdre d'autonomie.", "theme": "processus_chgt"},

    # ═══ demarche ═══
    {"q": "L'univers du changement — 4 dimensions", "a": "Le management du changement s'inscrit dans 4 dimensions interconnectées :\n\n• STRATÉGIE\n• MÉTHODES ET ACTIVITÉS\n• COLLABORATEURS\n• PARTENAIRES EXTERNES", "theme": "demarche"},
    {"q": "Les 8 étapes de la démarche Besombes", "a": "① AMORCER — Définir une stratégie / politique\n② ANALYSER L'EXISTANT — Diagnostic\n③ DÉFINIR LE NOUVEAU CADRE — Innover, objectifs opérationnels\n④ MOBILISER — Sensibiliser, former\n⑤ ÉLABORER LES PLANS D'ACTIONS — Hiérarchiser, planifier\n⑥ MISE EN ŒUVRE — Déployer, contrôler dérives\n⑦ MESURER ET ÉVALUER — Constater écarts, corriger, motiver\n⑧ S'AMÉLIORER — Boucler la démarche, fixer nouveaux objectifs\n\nDurée moyenne : 2 ans — ni trop, ni trop peu.", "theme": "demarche"},
    {"q": "Étape 1 — Amorcer : analyser facteurs internes et externes", "a": "FACTEURS INTERNES :\n  • L'organisation actuelle : points forts / points faibles\n  • Les compétences disponibles : immédiatement / CT / MT / inexistantes\n\nFACTEURS EXTERNES :\n  • La demande des clients (évolution / tendances)\n  • L'observation statistique\n  • La prospective économique (nouveaux thèmes, nouvelles règles)\n  • Les autres acteurs (financeurs, association, commune…)\n\nLa stratégie sera élaborée à partir de l'analyse de ces éléments.", "theme": "demarche"},
    {"q": "Étape 4 — Mobiliser : 6 actions clés", "a": "① Sensibiliser l'ensemble des collaborateurs collectivement ET individuellement aux nouveaux objectifs\n② S'assurer de la compréhension de tous\n③ Former aux nouvelles méthodes\n④ Définir les règles du jeu\n⑤ Définir les modalités d'évaluation\n⑥ Définir les méthodes de soutien", "theme": "demarche"},
    {"q": "Étape 5 — Élaborer les plans d'actions : 5 livrables", "a": "① Hiérarchiser les actions\n② Définir le calendrier\n③ Nommer les responsables et répartir les équipes\n④ Définir les temps d'échanges\n⑤ Définir les indicateurs de pilotage", "theme": "demarche"},
    {"q": "Gouvernance projet — qui fait quoi ?", "a": "3 niveaux de gouvernance projet :\n\n• DIRECTION → Projet stratégique\n• COMITÉ DE PILOTAGE PROJET → Gestion participative\n• GROUPES DE TRAVAIL (typiquement 4) → Exécution opérationnelle", "theme": "demarche"},
    {"q": "Vocation de la conduite du changement — 3 étapes", "a": "De la PROBLÉMATIQUE au CHANGEMENT via 3 étapes :\n\n① GARANTIR LA BONNE COMPRÉHENSION et la pertinence de la problématique\n   → Écoute · Propositions · Échanges\n\n② FÉDÉRER LES PARTIES PRENANTES autour d'un périmètre commun\n   → Mobilisation · Priorisation · Structuration · Alignement\n\n③ FACILITER LA MISE EN ŒUVRE du changement\n   → Coordination · Communication · Accompagnement", "theme": "demarche"},
    {"q": "Qualifier les solutions — grille à 4 cases", "a": "Pour qualifier une solution :\n\nCôté RÉSULTATS :\n  • GAINS ATTENDUS — gain de temps, productivité, niveau de service, qualité, fiabilité\n  • CONTRAINTES — éléments externes sur lesquels on a peu d'emprise mais qui impactent\n\nCôté CONDITIONS :\n  • POINTS D'APPUI — éléments favorables à utiliser au maximum (sponsor de poids, effet de levier)\n  • FREINS — éléments qui s'opposent à l'atteinte du résultat (mais sur lesquels on peut agir)", "theme": "demarche"},
    {"q": "Matrice de priorisation Importance × Facilité", "a": "Outil de priorisation graphique :\n\n• Abscisses : FACILITÉ / MAÎTRISE (0-10)\n• Ordonnées : IMPORTANCE (0-10)\n\nPermet d'identifier :\n  • Actions PRIORITAIRES : Importance élevée + Facilité élevée\n  • Actions « AU PARKING » : Importance faible (sortir de la roadmap)", "theme": "demarche"},

    # ═══ acteurs ═══
    {"q": "Les 3 types de comportements face au changement (10-80-10)", "a": "Face à tout changement, 3 types de comportements :\n\n① LES PROACTIFS (constructifs) — 10 à 20 %\n   Favorables au changement, se positionnent comme prescripteurs\n   → LES UTILISER\n\n② LES PASSIFS (hésitants) — 60 à 80 %\n   En attente de résultats probants, veulent être sécurisés\n   → LES RASSURER\n\n③ LES OPPOSANTS (destructeurs) — 10 à 20 %\n   Opposés aux projets, avancent des arguments « contre »\n   → LES LAISSER S'ISOLER pour mieux les raccrocher", "theme": "acteurs"},
    {"q": "S'appuyer sur le Top Management — pourquoi et comment", "a": "Le Top Management donne L'IMPULSION ET LA LÉGITIMITÉ :\n\n• Montrer à tous que le projet est moteur pour l'organisation\n• Prendre les décisions importantes et les communiquer\n\nPrérequis : le Top Management doit être IMPLIQUÉ ET MOTIVÉ.", "theme": "acteurs"},
    {"q": "S'appuyer sur le Middle Management — rôle de relais", "a": "Le Middle Management opérationnel RELAIE le changement :\n\n• S'impliquer dans les actions de communication\n• Intégrer les changements dans le management au quotidien\n• Contribuer à l'accompagnement post-déploiement\n\nPrérequis : le Management de proximité doit bénéficier d'un TEMPS D'AVANCE.", "theme": "acteurs"},
    {"q": "Miser sur les Ressources Métiers — 3 atouts", "a": "Les Ressources Métiers internes sont des relais légitimes car :\n\n• Ils CONNAISSENT l'organisation\n• Ils sont LÉGITIMES\n• Ils RESTERONT\n\nCondition : les mobiliser et les animer LE PLUS EN AMONT POSSIBLE, puis les accompagner dans ce rôle.", "theme": "acteurs"},

    # ═══ pilotage ═══
    {"q": "La méthode RACI — 4 rôles par activité", "a": "Pour chaque activité, on distingue 4 rôles :\n\n• R : RESPONSABLE (1 et un seul) — Donne son approbation, assume la responsabilité globale\n\n• A : ACTEUR (1 à n) — Réalise les activités\n\n• C : CONTRIBUTION (0 à n) — Dispose d'une information / expertise mais n'a pas d'autorité\n\n• I : INFORMATION (0 à n) — Informé sans intervention (généralement indirectement impacté)", "theme": "pilotage"},
    {"q": "Identifier les impacts organisationnels — démarche", "a": "Démarche en 3 temps :\n\n① Identifier les impacts par PROCESSUS / SOUS-PROCESSUS\n② Identifier les SCÉNARIOS et formuler une recommandation, puis faire arbitrer\n③ FORMALISER LE RACI par processus", "theme": "pilotage"},
    {"q": "Grille communication × dispositif — Pourquoi changer ?", "a": "Selon la question posée par l'acteur, le dispositif diffère :\n\n• « Pourquoi changer ? » → Communication projet · Kits de communication\n• « Comment ça va se passer ? » → Information ciblée par métier, domaine, fonction, rôle\n• « Qu'est-ce qui change pour moi ? » → Modules de sensibilisation\n• « Vais-je être à la hauteur ? » → Formation aux nouveautés\n• « Comment vais-je faire ? » → Modules de formation\n• « Suis-je prêt ? » → Entraînement libre ou encadré\n• « Je ne suis pas prêt ! » → Assistance de proximité\n• « Comment faire encore mieux ? » → Assistance à distance + Management au quotidien", "theme": "pilotage"},
    {"q": "Instance décisionnaire dédiée à l'accompagnement du changement", "a": "Préalable au pilotage : constituer une instance qui couvre 8 dimensions :\n\n• Cohérence avec les orientations stratégiques\n• Indicateurs à suivre\n• Ressources nécessaires, relais terrain\n• Tactique de déploiement\n• Coordination équipe projet\n• Planification, suivi du plan d'action\n• Déploiement des actions de communication clés\n• Alertes et risques", "theme": "pilotage"},
    {"q": "Les 10 points clés de la conduite du changement (Besombes)", "a": "① Faire participer les acteurs clés\n② Rester factuel\n③ Être réaliste\n④ Communiquer « honnête » et « utile »\n⑤ Faciliter la coordination des projets\n⑥ Accompagner le changement (tenir compte du « deuil »)\n⑦ Mesurer les impacts d'un projet avant de communiquer\n⑧ S'appuyer sur une méthodologie structurée et rassurante\n⑨ S'appuyer sur la DG puis sur le middle management\n⑩ S'appuyer sur des ressources métiers internes et les « chouchouter »", "theme": "pilotage"},

    # ═══ competences ═══
    {"q": "Chaîne des rôles — description de poste (Besombes)", "a": "La performance organisationnelle dépend de 4 rôles successifs :\n\n• RÔLE CONFIÉ (par l'organisation)\n• RÔLE PERÇU (par le salarié)\n• RÔLE ACCEPTÉ (par le salarié)\n• RÔLE TENU (effectivement)\n\nLa DESCRIPTION DE POSTE permet de minimiser l'écart d'efficacité entre rôle confié et rôle tenu.", "theme": "competences"},
    {"q": "Définition de la compétence selon Besombes", "a": "« La compétence est une DISPOSITION À MOBILISER, À COMBINER ET METTRE EN ŒUVRE DES RESSOURCES (savoir, savoir-faire, savoir-être). »\n\nC'est la COMBINAISON DYNAMIQUE de différents éléments :\n  • Savoir théorique\n  • Procédures et / ou bonnes pratiques\n  • Savoir-faire\n  • Expérience non formalisée", "theme": "competences"},
    {"q": "Les 5 critères d'identification des compétences (potentiel estimé)", "a": "① Motivation\n② Caractère\n③ Image que l'on a de soi\n④ Les connaissances et le savoir\n⑤ Le savoir-faire\n\nBonne pratique : il est préférable d'EMBAUCHER quelqu'un qui a 1, 2, 3 et de le FORMER à 4 et 5.", "theme": "competences"},
    {"q": "Les 4 outils d'identification des compétences détenues", "a": "Pour mesurer l'employabilité individuelle :\n\n① Mesure de l'employabilité individuelle\n② Bilan de compétences\n③ Portefeuille de compétences\n④ Cartes de compétences\n\nLe RÉFÉRENTIEL DES MÉTIERS indique le niveau de maîtrise sur 4 à 5 niveaux.", "theme": "competences"},
    {"q": "GPEC — définition et objectif (Besombes)", "a": "Gestion Prévisionnelle des Emplois et des Compétences :\n\n« Vise à RÉDUIRE, DE FAÇON ANTICIPÉE, LES ÉCARTS entre les besoins et les ressources de l'entreprise en termes d'effectifs et de compétences en fonction des objectifs identifiés, avec l'IMPLICATION DU SALARIÉ dans le cadre d'un projet d'évolution professionnelle. »", "theme": "competences"},
    {"q": "Éthique de performance — triangle Besombes", "a": "L'éthique de performance repose sur un triangle :\n\n• ACTIONNAIRES (stratégie, vision)\n• SALARIÉS (création de valeur)\n• CLIENTS (profits)\n\nAu centre : la DIRECTION assure l'équilibre permanent et la constance de l'objectif stratégique.", "theme": "competences"},
    {"q": "L'organisation qualifiante — 3 piliers", "a": "L'organisation qualifiante repose sur :\n\n① ENRICHISSEMENT DES TÂCHES\n② VOLONTÉ ÉDUCATIVE (développement de l'apprentissage permanent)\n③ RECHERCHE DE LA COMPÉTITIVITÉ\n\nÉléments préalables : identification des emplois actuels (résultats attendus + compétences requises via DICTIONNAIRE DE COMPÉTENCES) + prévision réaliste de l'évolution.", "theme": "competences"},
    {"q": "Description de poste — 6 rubriques", "a": "Schéma de principe d'une description de poste :\n\n① INTITULÉ DU POSTE\n② MISSIONS\n③ DIMENSIONS (chiffres significatifs)\n④ CONTEXTE GÉNÉRAL DU POSTE (cadre général de travail, contraintes)\n⑤ NATURE ET ÉTENDUE DES ACTIVITÉS (analyse du cadre d'activité et de ses moyens)\n⑥ RÉSULTATS ATTENDUS (identification des objectifs)\n\nDistinguer : LE POSTE (emploi tenu, unité physiquement identifiable) vs LA FONCTION (activités tendant vers le même but).", "theme": "competences"},
    {"q": "Les 3 dimensions des compétences (Besombes)", "a": "① EN TERMES DE MÉTIER\n  • Connaissances techniques et théoriques\n  • Connaissances pratiques et savoir-faire\n\n② EN TERMES DE MANAGEMENT\n  • Compétences relationnelles liées au métier\n  • Planification, organisation, coordination, contrôle\n  • Direction, animation, motivation\n\n③ ORIENTATION VERS LES RÉSULTATS\n  • Initiation, autonomie\n  • Engagement, sens des responsabilités\n  • Sens des priorités et flexibilité\n  • Contribution aux axes de progrès", "theme": "competences"},
    {"q": "Système d'évaluation — sanction vs formative", "a": "L'évaluation des compétences s'envisage au regard d'OBJECTIFS À ATTEINDRE.\n\nÉVALUATION « SANCTION » :\n  Cible : la performance, les résultats\n  Outils : objectifs quantitatifs, plans d'actions, management de la performance\n\nÉVALUATION « FORMATIVE » :\n  Cible : les compétences, la tenue du poste\n  Outils : orientations développement\n\nL'instauration d'un système d'évaluation INDUIT LE CHANGEMENT : comportements, pratiques managériales, relations d'autorité, mentalités, représentations culturelles.", "theme": "competences"},
    {"q": "Les 3 missionnements × 3 appréciations", "a": "Pour mettre en œuvre un système d'appréciation, confier aux salariés MISSIONS CLAIRES + MOYENS ADAPTÉS.\n\n3 TYPES DE MISSIONNEMENT :\n  • Les directives (règle, procédure, plan d'action)\n  • Les objectifs quantitatifs\n  • Les orientations ou objectifs qualitatifs\n\n3 TYPES D'APPRÉCIATION :\n  • Le contrôle\n  • La mesure\n  • L'appréciation", "theme": "competences"},
    {"q": "La culture d'entreprise — 5 forces (Besombes)", "a": "La culture d'entreprise repose sur 5 forces :\n\n• MYTHES\n• RITES\n• IDENTITÉ\n• VALEURS\n• HISTOIRE\n\nLa mise en œuvre d'un système d'appréciation s'appuyant sur des entretiens individuels fait appel à des notions qui RELÈVENT DE LA CULTURE D'ENTREPRISE.", "theme": "competences"},

    # ═══ equipe ═══
    {"q": "Les 5 étapes de constitution d'une équipe", "a": "① CONSTITUTION — création de l'équipe, découverte des autres et de la légitimité de chacun → Team Building\n\n② TENSION — confrontation des opinions, divergences objectives ou irrationnelles → Prévention / Gestion des conflits\n\n③ NORMALISATION — acceptation d'un but commun, apparition de règles et structuration → Négociation\n\n④ PRODUCTION — travail collectif vers le but commun → Motivation\n\n⑤ DISSOLUTION — dissolution (membres partis, nouveaux arrivants) → Valorisation", "theme": "equipe"},
    {"q": "Définition de l'équipe selon Lewin", "a": "« L'ESSENCE D'UN GROUPE EST L'INTERDÉPENDANCE DE CHACUN DE SES MEMBRES. » — Kurt Lewin\n\n3 caractéristiques d'une équipe :\n  • Objectif commun\n  • Interaction psychologique\n  • Existence collective", "theme": "equipe"},
    {"q": "Continuum de management directif → délégatif (7 niveaux)", "a": "Le comportement managérial s'inscrit sur un continuum entre AUTORITÉ DU RESPONSABLE et LIBERTÉ D'ACTION DU GROUPE.\n\nCentré sur l'animateur (autorité forte) :\n  • AUTORITÉ (directif)\n  • INFORMATION\n  • EXPLICATIF\n  • CONSULTATION\n\nCentré sur le groupe (liberté forte) :\n  • EXPLICATIF (concertation)\n  • NÉGOCIATION\n  • IMPLICATIF (délégation, responsabilisant)", "theme": "equipe"},
    {"q": "Modèle Pertinence / Cap / Actions / Ressources", "a": "Pour responsabiliser, articuler 4 dimensions :\n\n• CAP — Quelle est la destination à atteindre ?\n• ACTIONS — Comment s'y prendre pour atteindre le cap ?\n• RESSOURCES — Avec qui et quoi pour atteindre le cap ?\n• PERTINENCE — Sens ? Utilité ? Cohérence ?", "theme": "equipe"},
    {"q": "Les 4 attentes vis-à-vis du manager", "a": "Ce que les managés attendent de leur manager :\n\n① HONNÊTE — l'intégrité (confiance)\n② COMPÉTENT — la compétence (technique & managériale)\n③ TOURNÉ VERS L'AVENIR — la vision\n④ MOTIVANT — le dynamisme (implication et responsabilisation)", "theme": "equipe"},
    {"q": "Agilité managériale", "a": "Définition : la CAPACITÉ D'ADAPTATION ET D'INNOVATION mobilisée ensemble face à :\n\n• Quelles problématiques ?\n• Quelle résolution de problème ensemble ?\n• Quel plan d'actions concerté ?", "theme": "equipe"},
    {"q": "Manager n'est pas une fin en soi", "a": "Manager est un MOYEN pour :\n\n• Réussir un projet ensemble (ou un défi à relever)\n• Rester concentré sur l'essentiel (satisfaction client + collaborateurs)\n• Se connaître soi-même pour entrer en relation positive avec l'autre\n• La discipline de groupe crée les conditions de la réussite : les membres formulent ensemble le projet, se mettent d'accord sur les objectifs, définissent une méthode de travail commune, développent des compétences complémentaires, s'engagent collectivement à atteindre les résultats souhaités.", "theme": "equipe"},
    {"q": "Modèle de Gilbert (1980) — triangle de la performance", "a": "La PERFORMANCE se construit à l'intersection de 3 dimensions :\n\n• OBJECTIFS\n• MOYENS\n• RÉSULTATS\n\nLes écarts entre ces 3 sommets définissent :\n  • Objectifs ↔ Résultats : EFFICACITÉ\n  • Moyens ↔ Résultats : EFFICIENCE\n  • Objectifs ↔ Moyens : PERTINENCE", "theme": "equipe"},
]

NEW_QUIZ = [
    {"q": "Quelle loi physique sert d'analogie pour comprendre la résistance au changement organisationnel selon Besombes ?", "o": ["Loi de Le Chatelier", "Loi de Pareto", "Loi de Murphy", "Loi de Parkinson"], "c": 0, "e": "La loi de Le Chatelier énonce que toute modification de l'équilibre d'un système entraîne l'apparition de phénomènes qui tendent à s'y opposer. Pour réussir un changement, il faut donc associer 2 actions : augmenter les pressions dans le sens du changement ET diminuer les résistances.", "theme": "processus_chgt"},
    {"q": "Quelles sont les 3 phases du modèle de Kurt Lewin ?", "o": ["Diagnostic / Action / Évaluation", "Décristallisation / Changement / Cristallisation", "Préparation / Exécution / Contrôle", "Mobilisation / Production / Dissolution"], "c": 1, "e": "Lewin a modélisé le changement en 3 phases : ① Décristallisation (remise en cause du fonctionnement actuel), ② Changement (modifications des tâches, structure, techniques, comportements), ③ Cristallisation (renforcement positif des résultats souhaités, évaluation et suivi).", "theme": "processus_chgt"},
    {"q": "Combien de résistances classiques au changement sont identifiées par Besombes ?", "o": ["3 résistances", "5 résistances", "7 résistances", "10 résistances"], "c": 2, "e": "Les 7 résistances classiques : manque d'informations, peur de l'inconnu, besoin de sécurité, besoin de changement inexistant, peur de perdre des acquis, moment mal choisi, manque de ressources.", "theme": "processus_chgt"},
    {"q": "Parmi les 3 stratégies utiles face au changement (Besombes), laquelle fait appel à la responsabilisation comme facteur de motivation ?", "o": ["La coercition", "La persuasion rationnelle", "Le partage de pouvoir", "L'incitation financière"], "c": 2, "e": "Le partage de pouvoir mobilise la responsabilisation comme facteur de motivation, par l'implication des personnes dans le processus de changement. La coercition s'appuie sur sanctions/récompenses ; la persuasion rationnelle sur la logique et la compétence.", "theme": "processus_chgt"},
    {"q": "Combien d'étapes compte la démarche Besombes de conduite du changement ?", "o": ["4 étapes", "5 étapes", "8 étapes", "10 étapes"], "c": 2, "e": "La démarche Besombes comporte 8 étapes : ① Amorcer, ② Analyser l'existant, ③ Définir le nouveau cadre, ④ Mobiliser, ⑤ Élaborer les plans d'actions, ⑥ Mise en œuvre, ⑦ Mesurer et évaluer, ⑧ S'améliorer. Durée moyenne : 2 ans.", "theme": "demarche"},
    {"q": "Selon Besombes, combien de temps faut-il en moyenne pour réaliser la démarche complète (étapes 1 à 7) ?", "o": ["6 mois", "1 an", "2 ans", "5 ans"], "c": 2, "e": "Pour réaliser le parcours de l'étape 1 à l'étape 7, il faut envisager une période de 2 ans en moyenne — « ni trop, ni trop peu ».", "theme": "demarche"},
    {"q": "Quelles sont les 4 dimensions de « l'univers du changement » selon Besombes ?", "o": ["Stratégie / Méthodes et activités / Collaborateurs / Partenaires externes", "Vision / Mission / Objectifs / Valeurs", "Plan / Do / Check / Act", "Direction / Encadrement / Production / Support"], "c": 0, "e": "Les 4 dimensions de l'univers du changement sont : Stratégie, Méthodes et activités, Collaborateurs, Partenaires externes. Le management du changement s'inscrit à la croisée de ces 4 dimensions.", "theme": "demarche"},
    {"q": "Quel est l'ordre des 3 grandes étapes de la vocation de la conduite du changement (Besombes) ?", "o": ["Plan d'action → Périmètre → Adhésion", "Compréhension → Périmètre commun → Mise en œuvre", "Diagnostic → Mobilisation → Évaluation", "Stratégie → Tactique → Opérationnel"], "c": 1, "e": "La vocation se décline en 3 étapes : ① Garantir la bonne compréhension et la pertinence de la problématique (Écoute), ② Fédérer les parties prenantes autour d'un périmètre commun (Mobilisation), ③ Faciliter la mise en œuvre du changement (Coordination).", "theme": "demarche"},
    {"q": "Pour qualifier les solutions, Besombes propose une grille à 4 cases. Quels sont les éléments FAVORABLES ?", "o": ["Gains attendus + Contraintes", "Points d'appui + Freins", "Gains attendus + Points d'appui", "Contraintes + Freins"], "c": 2, "e": "La grille croise Résultats (Gains attendus vs Contraintes) et Conditions (Points d'appui vs Freins). Les éléments FAVORABLES sont les Gains attendus (résultats positifs) et les Points d'appui (éléments à utiliser au max comme un sponsor de poids).", "theme": "demarche"},
    {"q": "Quels sont les axes de la matrice de priorisation des actions selon Besombes ?", "o": ["Coût × Bénéfice", "Importance × Facilité (Maîtrise)", "Urgence × Importance (Eisenhower)", "Probabilité × Impact"], "c": 1, "e": "La matrice de priorisation Besombes croise IMPORTANCE (ordonnées) et FACILITÉ / MAÎTRISE (abscisses). Elle permet d'identifier les actions à mener en priorité (Importance + Facilité élevées) vs celles à mettre « au parking » (Importance faible).", "theme": "demarche"},
    {"q": "Selon Besombes, quelle est la répartition typique des comportements face au changement ?", "o": ["50 % proactifs / 50 % opposants", "10-20 % proactifs / 60-80 % passifs / 10-20 % opposants", "1/3 - 1/3 - 1/3", "25 % proactifs / 50 % passifs / 25 % opposants"], "c": 1, "e": "Besombes décrit 3 catégories : 10-20 % de PROACTIFS (constructifs, à utiliser), 60-80 % de PASSIFS (hésitants, à rassurer), 10-20 % d'OPPOSANTS (destructeurs, à laisser s'isoler).", "theme": "acteurs"},
    {"q": "Quels sont les 3 niveaux d'acteurs sur lesquels s'appuyer pour accompagner le changement selon Besombes ?", "o": ["DG / RH / Communication", "Top Management / Middle Management / Ressources Métiers", "Sponsors / Champions / Utilisateurs", "Direction / Cadres / Employés"], "c": 1, "e": "Besombes identifie 3 niveaux d'acteurs : ① Le Top Management donne l'impulsion et la légitimité, ② Le Middle Management opérationnel relaie, ③ Les Ressources Métiers internes accompagnent (elles connaissent l'organisation, sont légitimes, et resteront).", "theme": "acteurs"},
    {"q": "Que signifie l'acronyme RACI ?", "o": ["Risque / Action / Contrôle / Indicateur", "Responsable / Acteur / Contribution / Information", "Réalisation / Audit / Conformité / Innovation", "Référent / Adjoint / Coordinateur / Intervenant"], "c": 1, "e": "RACI = Responsable (1 et un seul par activité) / Acteur (1 à n, réalise) / Contribution (0 à n, expertise sans autorité) / Information (0 à n, informé sans intervention). Outil clé de répartition des rôles dans un projet de changement.", "theme": "pilotage"},
    {"q": "Selon la grille communication × dispositif de Besombes, quel dispositif répond à la question « Suis-je prêt ? »", "o": ["Kits de communication", "Modules de sensibilisation", "Entraînement libre ou encadré", "Modules de formation"], "c": 2, "e": "La question « Suis-je prêt ? » se traite par un Entraînement libre ou encadré. La grille fait correspondre chaque question des acteurs (Pourquoi changer / Comment ça va se passer / Qu'est-ce qui change pour moi / Vais-je être à la hauteur / Comment vais-je faire / Suis-je prêt / Je ne suis pas prêt / Comment faire encore mieux) à un dispositif spécifique.", "theme": "pilotage"},
    {"q": "Selon Besombes, combien de points clés résument la conduite du changement ?", "o": ["5 points", "7 points", "10 points", "12 points"], "c": 2, "e": "Besombes synthétise sa démarche en 10 points clés : faire participer les acteurs, rester factuel, être réaliste, communiquer honnêtement, faciliter la coordination, accompagner en tenant compte du « deuil », mesurer les impacts, s'appuyer sur une méthodologie, s'appuyer sur la DG + middle management, s'appuyer sur les ressources métiers.", "theme": "pilotage"},
    {"q": "Selon Besombes, quel est l'ordre de la chaîne des rôles dans une description de poste ?", "o": ["Confié → Tenu → Perçu → Accepté", "Perçu → Confié → Accepté → Tenu", "Confié → Perçu → Accepté → Tenu", "Accepté → Perçu → Tenu → Confié"], "c": 2, "e": "La chaîne des rôles selon Besombes : Rôle CONFIÉ (par l'organisation) → Rôle PERÇU (par le salarié) → Rôle ACCEPTÉ (par le salarié) → Rôle TENU (effectivement). La description de poste permet de minimiser l'écart d'efficacité entre rôle confié et rôle tenu.", "theme": "competences"},
    {"q": "Selon Besombes, qu'est-ce que la compétence ?", "o": ["L'ensemble des diplômes obtenus", "Une disposition à mobiliser, combiner et mettre en œuvre des ressources (savoir, savoir-faire, savoir-être)", "L'expérience professionnelle accumulée", "Le savoir technique acquis en formation"], "c": 1, "e": "Définition Besombes : « La compétence est une disposition à mobiliser, à combiner et mettre en œuvre des ressources (savoir, savoir-faire, savoir-être). C'est la combinaison dynamique de différents éléments : savoir théorique, procédures et bonnes pratiques, savoir-faire, expérience non formalisée. »", "theme": "competences"},
    {"q": "Quel est l'objectif de la GPEC selon Besombes ?", "o": ["Maximiser la productivité", "Réduire de façon anticipée les écarts entre besoins et ressources de l'entreprise en effectifs et compétences", "Augmenter les salaires", "Réduire les coûts de main-d'œuvre"], "c": 1, "e": "La GPEC (Gestion Prévisionnelle des Emplois et des Compétences) vise à réduire, de façon anticipée, les écarts entre les besoins et les ressources de l'entreprise en termes d'effectifs et de compétences en fonction des objectifs identifiés, avec l'implication du salarié dans le cadre d'un projet d'évolution professionnelle.", "theme": "competences"},
    {"q": "L'éthique de performance de Besombes repose sur quel triangle ?", "o": ["Coût / Qualité / Délai", "Actionnaires / Salariés / Clients", "Direction / Encadrement / Production", "Mission / Vision / Valeurs"], "c": 1, "e": "L'éthique de performance repose sur 3 parties prenantes : ACTIONNAIRES (stratégie, vision), SALARIÉS (création de valeur), CLIENTS (profits). Au centre : la DIRECTION assure l'équilibre permanent et la constance de l'objectif stratégique.", "theme": "competences"},
    {"q": "Selon Besombes, quels sont les 3 piliers de l'organisation qualifiante ?", "o": ["Formation / Évaluation / Promotion", "Enrichissement des tâches / Volonté éducative / Recherche de la compétitivité", "Recrutement / Formation / Fidélisation", "Diagnostic / Action / Mesure"], "c": 1, "e": "L'organisation qualifiante repose sur : ① Enrichissement des tâches, ② Volonté éducative (développement de l'apprentissage permanent), ③ Recherche de la compétitivité. Elle s'appuie sur un dictionnaire de compétences et une prévision réaliste de l'évolution de l'emploi.", "theme": "competences"},
    {"q": "Selon Besombes, l'évaluation des compétences peut tendre vers 2 finalités. Lesquelles ?", "o": ["Promotion vs licenciement", "Évaluation « sanction » vs évaluation « formative »", "Quantitative vs qualitative", "Hiérarchique vs participative"], "c": 1, "e": "Besombes distingue : ÉVALUATION « SANCTION » (cible la performance et les résultats, outils : objectifs quantitatifs, plans d'actions, management de la performance) vs ÉVALUATION « FORMATIVE » (cible les compétences et la tenue du poste, outils : orientations développement).", "theme": "competences"},
    {"q": "Combien de types de missionnement Besombes distingue-t-il dans la mise en œuvre d'un système d'appréciation ?", "o": ["2 types", "3 types", "4 types", "5 types"], "c": 1, "e": "Besombes distingue 3 TYPES DE MISSIONNEMENT : ① Les directives (règle, procédure, plan d'action), ② Les objectifs quantitatifs, ③ Les orientations ou objectifs qualitatifs. Avec en parallèle 3 TYPES D'APPRÉCIATION : contrôle, mesure, appréciation.", "theme": "competences"},
    {"q": "Selon Besombes, sur quoi repose la culture d'entreprise ?", "o": ["Mythes / Rites / Identité / Valeurs / Histoire", "Vision / Mission / Valeurs", "Pouvoir / Droit / Intérêt", "Stratégie / Structure / Système"], "c": 0, "e": "Selon Besombes, la culture d'entreprise repose sur 5 forces : MYTHES, RITES, IDENTITÉ, VALEURS, HISTOIRE. La mise en œuvre d'un système d'appréciation s'appuyant sur des entretiens individuels fait appel à des notions qui relèvent de cette culture.", "theme": "competences"},
    {"q": "Quelles sont les 5 étapes de constitution d'une équipe selon Besombes ?", "o": ["Initiation / Action / Maturité / Récolte / Fin", "Constitution / Tension / Normalisation / Production / Dissolution", "Plan / Do / Check / Act / Repeat", "Forming / Storming / Norming / Performing / Adjourning"], "c": 1, "e": "Besombes présente les 5 étapes en français : ① CONSTITUTION (team building), ② TENSION (gestion des conflits), ③ NORMALISATION (négociation), ④ PRODUCTION (motivation), ⑤ DISSOLUTION (valorisation). Sans nommer Tuckman ni utiliser la terminologie anglaise.", "theme": "equipe"},
    {"q": "Selon Lewin, qu'est-ce qui caractérise l'essence d'un groupe ?", "o": ["La hiérarchie", "L'interdépendance de chacun de ses membres", "L'autonomie de chacun", "La compétition"], "c": 1, "e": "« L'essence d'un groupe est l'interdépendance de chacun de ses membres » (Lewin). 3 caractéristiques d'une équipe : objectif commun, interaction psychologique, existence collective.", "theme": "equipe"},
    {"q": "Le continuum de management directif → délégatif comporte combien de niveaux ?", "o": ["3 niveaux", "5 niveaux", "7 niveaux", "10 niveaux"], "c": 2, "e": "Le continuum présenté par Besombes comporte 7 niveaux entre autorité du responsable et liberté d'action du groupe : Autorité (directif), Information, Explicatif, Consultation, Explicatif (concertation), Négociation, Implicatif (délégation, responsabilisant).", "theme": "equipe"},
    {"q": "Quelles sont les 4 dimensions du modèle de responsabilisation de Besombes ?", "o": ["Cap / Actions / Ressources / Pertinence", "Plan / Do / Check / Act", "Direction / Décision / Délégation / Délivrance", "Objectifs / Moyens / Méthodes / Mesures"], "c": 0, "e": "Le modèle articule : CAP (destination à atteindre), ACTIONS (comment s'y prendre), RESSOURCES (avec qui et quoi), PERTINENCE (sens, utilité, cohérence). Outil de responsabilisation managériale.", "theme": "equipe"},
    {"q": "Selon Besombes, quelles sont les 4 attentes des managés vis-à-vis de leur manager ?", "o": ["Sympathique / Disponible / Patient / Compréhensif", "Honnête / Compétent / Tourné vers l'avenir / Motivant", "Strict / Juste / Récompensant / Sanctionnant", "Charismatique / Visionnaire / Inspirant / Engagé"], "c": 1, "e": "Les 4 attentes : ① HONNÊTE (intégrité, confiance), ② COMPÉTENT (technique & managériale), ③ TOURNÉ VERS L'AVENIR (vision), ④ MOTIVANT (dynamisme, implication, responsabilisation).", "theme": "equipe"},
    {"q": "Quel est le triangle du Modèle de Gilbert (1980) ?", "o": ["Coût / Qualité / Délai", "Objectifs / Moyens / Résultats", "Mission / Vision / Valeurs", "Plan / Action / Contrôle"], "c": 1, "e": "Le Modèle de Gilbert (1980) est un triangle Objectifs / Moyens / Résultats. Les 3 écarts définissent : Efficacité (Objectifs ↔ Résultats), Efficience (Moyens ↔ Résultats), Pertinence (Objectifs ↔ Moyens).", "theme": "equipe"},
]


# ═══════════════════════════════════════════════════════════════════════════
# APPLICATION
# ═══════════════════════════════════════════════════════════════════════════
def rewrite_html():
    text = HTML.read_text()
    pattern = re.compile(r'function getCoursHTML\(\)\s*\{\s*return\s*`[\s\S]*?`;\s*\}\n', re.MULTILINE)
    if not pattern.search(text):
        raise SystemExit('getCoursHTML non trouvé dans conduite_chgt.html')
    new_text = pattern.sub(NEW_COURS, text, count=1)
    HTML.write_text(new_text)
    print('✓ conduite_chgt.html : getCoursHTML réécrit (Besombes uniquement)')


def rewrite_json():
    d = json.loads(JSON.read_text())
    d['themes'] = NEW_THEMES
    d['flashcards'] = NEW_FLASHCARDS
    d['quizQuestions'] = NEW_QUIZ
    d['checklistItems'] = NEW_CHECKLIST
    d['title'] = 'Conduite du changement & gestion des compétences'
    d['subtitle'] = 'Cours F. Besombes — Démarche 8 étapes · GPEC · RACI · Gilbert 1980'
    JSON.write_text(json.dumps(d, ensure_ascii=False, indent=2))
    print('✓ data/conduite_chgt.json :')
    print(f'   themes        : {len(NEW_THEMES)}')
    print(f'   flashcards    : {len(NEW_FLASHCARDS)}')
    print(f'   quizQuestions : {len(NEW_QUIZ)}')
    print(f'   checklistItems: {len(NEW_CHECKLIST)}')


if __name__ == '__main__':
    rewrite_html()
    rewrite_json()
