"""Réécrit evo_orga.html (getCoursHTML) + data/evo_orga.json pour ne refléter QUE le
contenu du PDF Besombes (Cours évolution des modèles.pdf, 54 slides).

Suppression de TOUS les contenus hors-Besombes :
  - Taylor, Fayol, Weber, Ford, Mayo, Maslow, Herzberg, McGregor, Ouchi
  - Burns & Stalker, Lawrence & Lorsch, Woodward
  - Mintzberg, Coase, Williamson, Jensen, Barney, RBV, Freeman, DiMaggio
  - Lean, TPS, Holacratie, Laloux, entreprise libérée

CONSERVATION du contenu Besombes structuré en 5 thèmes :
  - intro       : Accélération historique, 3 logiques, 12 thèmes, types d'organisations
  - dppo        : DPPO Drucker 1954, 6 principes
  - processus   : Approche processus ISO 9001/8402, tortue de Crosby, types
  - performance : Définition, US Navy, efficacité/efficience, Gilbert 1980, Crozier
  - pilotage    : Dialogue social, structure projet, 7 leviers, CO-CONSTRUIRE
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / 'evo_orga.html'
JSON = ROOT / 'data' / 'evo_orga.json'


# ═══════════════════════════════════════════════════════════════════════════
# NOUVEAU CONTENU getCoursHTML — 10 chapitres Besombes
# ═══════════════════════════════════════════════════════════════════════════
NEW_COURS = '''function getCoursHTML() {
  return `
<div class="course-chapter" data-theme="intro" data-chap-idx="1" id="chap-1">
  <h2>1. Introduction — Une aventure vieille de 400 000 ans</h2>
  <div class="def-box">
    <div class="def-label">Une accélération notable</div>
    <p>L'organisation est une aventure ancienne, marquée par 3 tensions permanentes : <strong>Pouvoir, Contre-pouvoir, Spécialisation</strong>. Mais elle connaît une accélération récente :</p>
    <ul>
      <li><strong>−400 000 av. J.-C.</strong> : maîtrise du feu</li>
      <li><strong>XVIIIe siècle</strong> : Révolution industrielle</li>
      <li><strong>Fin XXe siècle</strong> : TIC (Technologies de l'Information et de la Communication)</li>
      <li><strong>2030</strong> : IA</li>
    </ul>
  </div>
  <h3>3 grandes logiques économiques successives</h3>
  <table class="comp-table">
    <thead><tr><th>Période</th><th>Logique dominante</th></tr></thead>
    <tbody>
      <tr><td><strong>1900</strong></td><td>Logique de <strong>production</strong></td></tr>
      <tr><td><strong>1950</strong></td><td>Logique de <strong>vente</strong></td></tr>
      <tr><td><strong>Aujourd'hui</strong></td><td>Logique de <strong>création de valeur</strong></td></tr>
    </tbody>
  </table>
  <h3>Quelles organisations aujourd'hui ?</h3>
  <div class="key-box">
    <ul>
      <li>Des <strong>entreprises virtuelles</strong></li>
      <li>Des <strong>industries sans usines</strong> (fabless-fab)</li>
      <li>Des grandes entreprises composées d'<strong>une multitude de PME</strong></li>
      <li>Des entreprises sur l'ensemble des territoires</li>
    </ul>
  </div>
  <h3>Une logique permanente</h3>
  <div class="def-box">
    <div class="def-label">Schéma BOR — Besoin / Organisation / Réponse</div>
    <p>L'organisation répond à un <strong>besoin</strong> par une <strong>réponse</strong>, sous condition de <strong>cohérence</strong> entre :</p>
    <ul>
      <li><strong>Ressources humaines / compétences</strong></li>
      <li><strong>Ressources matérielles et financières</strong></li>
    </ul>
  </div>
</div>

<div class="course-chapter" data-theme="intro" data-chap-idx="2" id="chap-2">
  <h2>2. Introduction — Les 12 thèmes du cours</h2>
  <div class="key-box">
    Le cours s'organise autour de <strong>12 thèmes</strong> qui structurent l'analyse contemporaine des modèles d'organisation :
    <table class="comp-table">
      <tbody>
        <tr><td>① Intelligence artificielle</td><td>② Robotique / cobotique</td></tr>
        <tr><td>③ Capital humain</td><td>④ Stratégie vs Organisation</td></tr>
        <tr><td>⑤ Contingence organisationnelle</td><td>⑥ Innovation</td></tr>
        <tr><td>⑦ RSE</td><td>⑧ Réseau et territoire</td></tr>
        <tr><td>⑨ Approche systémique et processus</td><td>⑩ Chaîne de valeur et globalisation</td></tr>
        <tr><td>⑪ Productivité vs création de valeur</td><td>⑫ Nouvelles formes de travail</td></tr>
      </tbody>
    </table>
  </div>
  <h3>Un changement de paradigme : Tâches → Objectifs</h3>
  <p>L'évolution du management se traduit par un passage progressif d'une logique de <strong>tâches</strong> (héritée de l'école classique) vers une logique d'<strong>objectifs</strong> (orientée performance).</p>
</div>

<div class="course-chapter" data-theme="dppo" data-chap-idx="3" id="chap-3">
  <h2>3. La Direction Par Objectifs (DPPO) — Peter Drucker, 1954</h2>
  <div class="def-box">
    <div class="def-label">DPPO — Peter Drucker (1909-2005)</div>
    <p>La <strong>Direction Par Objectifs (DPPO)</strong> a été conceptualisée en <strong>1954 par Peter Drucker</strong>.</p>
  </div>
  <h3>Les 6 principes fondamentaux du management selon Drucker</h3>
  <div class="key-box">
    <ol>
      <li><strong>Définir la mission</strong> de son entité</li>
      <li><strong>Fixer des objectifs clairs</strong> pour les équipes</li>
      <li><strong>Analyser et organiser le travail</strong> pour créer un sentiment de satisfaction chez le personnel</li>
      <li><strong>Informer et écouter</strong> ses employés</li>
      <li><strong>Évaluer les résultats</strong> au moyen de normes spécifiques</li>
      <li><strong>Former ses collaborateurs en permanence</strong></li>
    </ol>
  </div>
  <h3>Le champ des objectifs opérationnels (selon les principes de la DPPO)</h3>
  <table class="comp-table">
    <thead><tr><th>Dimension</th><th>Évolution</th></tr></thead>
    <tbody>
      <tr><td><strong>Structure</strong></td><td>De hiérarchique à <strong>transversale</strong></td></tr>
      <tr><td><strong>Équipes</strong></td><td>Déclinaison des <strong>objectifs stratégiques en objectifs opérationnels</strong> pour chaque pôle et chaque collaborateur</td></tr>
      <tr><td><strong>Pilotage et amélioration</strong></td><td>Participation des collaborateurs au déploiement des procédures et information sur les indicateurs</td></tr>
    </tbody>
  </table>
</div>

<div class="course-chapter" data-theme="intro" data-chap-idx="4" id="chap-4">
  <h2>4. La différenciation — un enjeu essentiel</h2>
  <div class="key-box">
    <ul>
      <li>Les <strong>stratégies de différenciation</strong> sont à l'origine des <strong>avantages concurrentiels décisifs</strong>.</li>
      <li>Seules les <strong>différences perçues par le client</strong> ont de la valeur.</li>
      <li>Les différences complexes s'appuient sur la <strong>spécialisation</strong>.</li>
      <li>La perception de la différence est liée à la maîtrise de l'ensemble de la <strong>chaîne de valeur</strong>.</li>
    </ul>
  </div>
</div>

<div class="course-chapter" data-theme="intro" data-chap-idx="5" id="chap-5">
  <h2>5. Le métier et le savoir-faire</h2>
  <div class="def-box">
    <div class="def-label">Le métier d'une organisation</div>
    <ul>
      <li>Le métier peut se définir comme la <strong>somme des savoir-faire acquis</strong> et à la <strong>capacité de combiner ces savoir-faire</strong>.</li>
      <li>Le <strong>processus combinatoire</strong> des savoir-faire varie d'une organisation à l'autre.</li>
      <li>Le métier d'une organisation est <strong>difficile à décrire</strong> car les combinaisons qui le forment sont aussi informelles.</li>
      <li>La <strong>vision du métier par un manager conditionne sa capacité à découvrir de nouvelles voies</strong>.</li>
    </ul>
  </div>
</div>

<div class="course-chapter" data-theme="intro" data-chap-idx="6" id="chap-6">
  <h2>6. La fin d'un monde — Tainter et l'effondrement par complexité</h2>
  <div class="def-box">
    <div class="def-label">Théorie de Tainter — facteurs d'effondrement</div>
    <p>Pour le professeur <strong>Joseph Tainter</strong>, qui a étudié les effondrements de sociétés dans notre histoire, les facteurs qui conduisent au drame sont les suivants :</p>
  </div>
  <div class="key-box">
    <ol>
      <li>Les <strong>sociétés humaines sont des organisations faites pour résoudre les problèmes</strong>.</li>
      <li>Les systèmes sociopolitiques <strong>ont besoin d'énergie</strong> pour se maintenir.</li>
      <li>La <strong>complexité accrue porte en elle des coûts accrus par habitant</strong>.</li>
      <li>L'investissement dans la complexité sociopolitique, en tant que réponse à la résolution des problèmes, atteint souvent un <strong>point de rendements marginaux décroissants</strong>.</li>
      <li>À mesure que le rendement marginal décline, la société <strong>investit toujours plus lourdement dans une stratégie proportionnellement moins rentable</strong>. Il faut alors faire face aux poussées de tensions en dehors du budget courant.</li>
      <li>Les rendements marginaux décroissants font de la complexité une <strong>stratégie d'ensemble de moins en moins séduisante</strong>, si bien que des parties d'une société perçoivent un avantage croissant à une <strong>politique de séparation ou de désintégration</strong>. Logiquement, divers segments de la population accroissent leur résistance active ou passive, ou <strong>tentent ouvertement de faire sécession</strong>.</li>
    </ol>
  </div>
</div>

<div class="course-chapter" data-theme="intro" data-chap-idx="7" id="chap-7">
  <h2>7. Le réseau d'équipes — Étude Deloitte 2016</h2>
  <div class="def-box">
    <div class="def-label">Étude Deloitte, juin 2016 — Philippe Burger</div>
    <p>Une étude publiée par le cabinet <strong>Deloitte</strong>, en juin 2016, indique que <strong>« 90 % des entreprises françaises envisagent une évolution de leur organisation »</strong>.</p>
    <p>« Il est intéressant de noter que <strong>11 % des entreprises françaises déclarent avoir une structure organisationnelle construite autour de projets ou programmes transverses</strong>. Ce chiffre, qui peut sembler faible, témoigne pourtant de l'émergence d'un <strong>nouveau modèle organisationnel : celui du réseau d'équipes</strong>. Les organisations évoluent de plus en plus d'un modèle traditionnel organisé autour de fonctions d'entreprise vers un modèle basé sur des équipes responsables, flexibles et interconnectées partout dans le monde. »</p>
    <p><em>Philippe Burger, Associé responsable Capital Humain chez Deloitte</em></p>
  </div>
  <h3>Concept organisationnel — Principes généraux</h3>
  <div class="key-box">
    <ul>
      <li><strong>Transversalité</strong></li>
      <li><strong>Autonomie vs Responsabilité</strong></li>
      <li><strong>Initiative et innovation</strong></li>
      <li><strong>Orientation Satisfaction Client</strong></li>
    </ul>
  </div>
  <h3>La culture d'entreprise</h3>
  <div class="def-box">
    <ul>
      <li>Il existe toujours <strong>une culture d'établissement qu'elle soit connue ou non</strong>.</li>
      <li>Elle est fondée sur les <strong>habitudes, les attitudes sociales, l'histoire de chacun de ses membres</strong>.</li>
      <li>Il existe une <strong>confrontation entre les valeurs personnelles des acteurs, et la culture déclarée</strong> de l'établissement et des autres.</li>
      <li>Elle est fondée sur une <strong>histoire, une identité, des règles du jeu, d'acceptation et de pouvoir, des croyances et des routines</strong> auxquelles les acteurs adhèrent ou non.</li>
    </ul>
  </div>
  <h3>Perspectives managériales</h3>
  <div class="example-box">
    <em>« Un bon chef est celui qui a besoin des autres »</em> — <strong>Paul Valéry</strong>
    <p style="margin-top:0.6rem">Pour construire la performance, il faut alors : <strong>faire réussir les autres</strong>.</p>
  </div>
</div>

<div class="course-chapter" data-theme="processus" data-chap-idx="8" id="chap-8">
  <h2>8. Approche processus &amp; ISO 9001:2000</h2>
  <div class="def-box">
    <div class="def-label">L'évolution du management</div>
    <p>Passer d'une <strong>logique de « tâches »</strong> (en perspective de l'école classique) à une <strong>approche « processus » orientée vers la performance et l'excellence</strong>.</p>
  </div>

  <h3>Définition d'un processus</h3>
  <div class="def-box">
    <div class="def-label">Norme ISO 8402 — définition formelle</div>
    <p>« <strong>Ensemble des moyens et d'activités qui transforment les éléments entrants en éléments sortants dans un but défini et mesurable</strong> » <em>(ISO 8402, cité par P. Baracchini, 2007)</em></p>
    <p>Plus simplement : un processus est un <strong>ensemble homogène de sous-processus et de tâches</strong>, qui s'enchaînent de façon logique pour transformer des intrants en extrants.</p>
  </div>

  <h3>Les 3 types de processus</h3>
  <table class="comp-table">
    <thead><tr><th>Type</th><th>Objet</th><th>Exemples</th></tr></thead>
    <tbody>
      <tr><td><strong>Processus de Réalisation</strong></td><td>Réalisation du produit ou du service</td><td>Conception, fabrication, vente, prestation</td></tr>
      <tr><td><strong>Processus Support</strong></td><td>Outils et méthodes permettant d'appuyer le processus de réalisation</td><td>RH, formation, informatique, comptabilité, maintenance</td></tr>
      <tr><td><strong>Processus de Pilotage</strong></td><td>Mise en œuvre des objectifs dans l'organisme</td><td>Politique, stratégie, technologie, décision, budget, mesure</td></tr>
    </tbody>
  </table>

  <h3>Vocabulaire hiérarchique</h3>
  <div class="key-box">
    <ul>
      <li><strong>MACROPROCESSUS</strong> : Client, RH…</li>
      <li><strong>PROCESSUS</strong> : ensemble de sous-processus</li>
      <li><strong>SOUS-PROCESSUS</strong> : ensemble de tâches</li>
      <li><strong>TÂCHES</strong> : opération spécifique</li>
    </ul>
  </div>

  <h3>Système de Management de la Qualité — Norme ISO 9001 version 2000</h3>
  <div class="key-box">
    <strong>Schéma général de l'amélioration continue</strong> :
    <ul>
      <li><strong>Client (entrée)</strong> : exigences → Données d'entrée</li>
      <li><strong>Responsabilité de la direction</strong></li>
      <li><strong>Management des ressources</strong></li>
      <li><strong>Réalisation du produit et/ou service</strong></li>
      <li><strong>Mesure, analyse et amélioration</strong></li>
      <li><strong>Client (sortie)</strong> : satisfaction → Données de sortie</li>
    </ul>
    Le tout est inscrit dans une boucle d'<strong>amélioration continue</strong>.
  </div>

  <h3>La tortue de Crosby — identification des processus</h3>
  <div class="def-box">
    <div class="def-label">Tortue de Crosby — 4 questions clés</div>
    <p>Pour caractériser un processus, on mobilise <strong>4 questions</strong> :</p>
    <ul>
      <li><strong>AVEC QUOI ?</strong> — Avec quels moyens et équipements je maîtrise le processus ?</li>
      <li><strong>AVEC QUI ?</strong> — Avec quelles compétences je maîtrise le processus ?</li>
      <li><strong>COMMENT ?</strong> — Avec quelles méthodes je maîtrise le processus ?</li>
      <li><strong>COMBIEN ?</strong> — Avec quels indicateurs je pilote le processus ?</li>
    </ul>
  </div>

  <h3>Interactions entre processus</h3>
  <div class="key-box">
    <ul>
      <li>Identifier les processus entre lesquels il existe une interaction</li>
      <li>Définir la <strong>nature de l'interaction</strong> (sortie de l'un = entrée d'un autre, etc.)</li>
      <li>Établir un <strong>diagramme de toutes les interactions</strong> entre tous les processus identifiés (<strong>cartographie des processus</strong>)</li>
    </ul>
  </div>

  <h3>La nature des processus &amp; chaîne de valeur</h3>
  <div class="key-box">
    <ul>
      <li>Processus dont les éléments de sortie sont associés aux <strong>exigences des clients</strong></li>
      <li>Processus dont les éléments de sortie ont une incidence sur l'<strong>efficacité des autres processus</strong></li>
    </ul>
    <strong>Processus et chaîne de valeur</strong> : le processus produit de la <strong>valeur ajoutée</strong>, des <strong>fournisseurs</strong> vers les <strong>clients</strong>, à travers des <strong>moyens</strong> et des <strong>règles</strong>.
  </div>
</div>

<div class="course-chapter" data-theme="performance" data-chap-idx="9" id="chap-9">
  <h2>9. La performance — définition, dualité, mesure</h2>
  <h3>Stratégie-Organisation : une dualité permanente</h3>
  <div class="def-box">
    <div class="def-label">Dualité ago-antagoniste</div>
    <ul>
      <li>L'entreprise doit avoir à la fois une <strong>démarche pro-active de conquête</strong> et en même temps <strong>limiter le risque associé</strong>.</li>
      <li>Recherche de la <strong>convergence d'éléments ago-antagonistes</strong> comme aimait à les qualifier <strong>Edgar Morin</strong>.</li>
      <li>Lien indissociable qui existe entre la <strong>structure de l'entreprise et sa stratégie</strong> — <strong>A. Chandler</strong> (« Structure follows Strategy », 1962).</li>
      <li>Le succès ou l'échec d'une politique d'entreprise réside aussi dans la <strong>maîtrise organisationnelle</strong>. Facteurs d'inertie liés : communication, comportements, jeux des acteurs.</li>
    </ul>
  </div>

  <h3>Qu'est-ce que la performance ?</h3>
  <div class="key-box">
    <strong>Questions ouvertes :</strong> Dimension objective ou subjective ? C'est un processus ? Action ou état ? Finalité mesurable ? Corollaire du management ? Atteinte de résultats prévus ?
  </div>
  <div class="def-box">
    <div class="def-label">Définition de la performance (Besombes)</div>
    <ul>
      <li>La performance d'une organisation est issue d'un <strong>processus de construction contingent</strong>.</li>
      <li>La performance est la conséquence d'une <strong>représentation</strong>, qui n'a pas de réalité propre.</li>
      <li>Elle est le résultat de <strong>l'accord entre les parties prenantes</strong> de l'organisation, fondée sur le <strong>consensus et la coopération</strong>.</li>
      <li>La performance est devenue stratégique, elle contribue à l'<strong>émergence du « sens »</strong>.</li>
    </ul>
    <p><em>Tentative de définition : la performance organisationnelle pourrait être définie comme le résultat d'un processus maîtrisé afin d'atteindre un but préalablement défini, en mobilisant des ressources variées et optimisées.</em></p>
  </div>

  <h3>L'approche de l'US Navy</h3>
  <div class="example-box">
    <em>« Processus de définition de la <strong>mission</strong> et des <strong>outputs escomptés</strong>, de détermination des <strong>standards de la performance</strong>, de <strong>mise en relation du budget</strong> avec la performance, de <strong>reporting des résultats</strong> ainsi que de <strong>l'assurance que les managers sont comptables des résultats</strong>. »</em>
  </div>

  <h3>Entre efficacité et efficience</h3>
  <table class="comp-table">
    <thead><tr><th>Concept</th><th>Définition</th><th>Citation Drucker</th></tr></thead>
    <tbody>
      <tr><td><strong>Efficacité</strong></td><td>Atteinte des résultats <strong>quelle que soit l'allocation de ressources</strong></td><td>« Faire <strong>les bonnes choses</strong> »</td></tr>
      <tr><td><strong>Efficience</strong></td><td>Atteinte des résultats, en <strong>optimisant l'allocation de ressources</strong></td><td>« Faire les choses <strong>de la bonne façon</strong> »</td></tr>
    </tbody>
  </table>
  <div class="key-box">
    <strong>Le contexte fait la différence</strong> — La performance représenterait dans un contexte donné, la <strong>capacité d'être à la fois Efficace et Efficient</strong>. La performance est alors dépendante de la définition d'objectifs <strong>partagés, compris et mis en œuvre</strong>.
  </div>

  <h3>Le Modèle de Gilbert (1980)</h3>
  <div class="def-box">
    <div class="def-label">Modèle de Gilbert (1980) — Le triangle de la performance</div>
    <p>La performance se construit à l'intersection de 3 dimensions :</p>
    <ul>
      <li><strong>OBJECTIFS</strong></li>
      <li><strong>MOYENS</strong></li>
      <li><strong>RÉSULTATS</strong></li>
    </ul>
    Les écarts entre ces 3 sommets définissent :
    <ul>
      <li><strong>Objectifs ↔ Résultats</strong> : Efficacité</li>
      <li><strong>Moyens ↔ Résultats</strong> : Efficience</li>
      <li><strong>Objectifs ↔ Moyens</strong> : Pertinence</li>
    </ul>
  </div>
</div>

<div class="course-chapter" data-theme="performance" data-chap-idx="10" id="chap-10">
  <h2>10. L'organisation est un corps vivant — Michel Crozier</h2>
  <div class="def-box">
    <div class="def-label">Michel Crozier (1922-2013)</div>
    <p>Concepteur de <strong>l'analyse stratégique et de l'action collective</strong>.</p>
    <ul>
      <li>Les organisations sont comparables à des <strong>organismes vivants</strong>.</li>
      <li>Les êtres vivants <strong>planifient, analysent, expérimentent et décident</strong>.</li>
      <li>Les êtres vivants <strong>s'adaptent et innovent</strong> face aux évolutions et à l'environnement.</li>
    </ul>
  </div>
  <h3>Vers un arbre de décision dynamique</h3>
  <div class="key-box">
    Trois leviers structurent l'arbre de décision organisationnel :
    <ul>
      <li><strong>Pouvoir</strong></li>
      <li><strong>Droit</strong></li>
      <li><strong>Intérêt</strong></li>
    </ul>
    Ces 3 dimensions interagissent en permanence et déterminent les jeux d'acteurs au sein de l'organisation.
  </div>
</div>

<div class="course-chapter" data-theme="pilotage" data-chap-idx="11" id="chap-11">
  <h2>11. Dialogue social, structure projet et pilotage de la performance</h2>

  <h3>Le dialogue social, enjeu pour construire la réussite</h3>
  <div class="example-box">
    <em>« La réussite d'une entreprise, c'est <strong>5 % de stratégie et 95 % d'action</strong>. »</em> — <strong>Carlos Ghosn</strong>
  </div>
  <div class="key-box">
    <strong>4 niveaux d'acteurs du dialogue social</strong> :
    <ul>
      <li><strong>TOP MANAGEMENT</strong></li>
      <li><strong>MANAGEMENT DE PROXIMITÉ</strong></li>
      <li><strong>OPÉRATEURS</strong></li>
      <li><strong>IRP</strong> (Instances Représentatives du Personnel)</li>
    </ul>
    Deux registres complémentaires : <strong>Dialogue social formel</strong> + <strong>Dialogue social informel</strong>.
    <p style="margin-top:0.8rem"><strong>Aller vers un dialogue social permanent centré sur le projet à réussir ensemble.</strong></p>
  </div>

  <h3>Migrer d'une structure fonctionnelle à une structure projet</h3>
  <table class="comp-table">
    <thead><tr><th>Structure fonctionnelle (contrôle)</th><th>Structure projet</th></tr></thead>
    <tbody>
      <tr>
        <td>Communication <strong>séquentielle descendante</strong>, parfois ascendante. Organisation centrée sur les <strong>tâches</strong>.</td>
        <td>Communication <strong>continue circulaire</strong>. Organisation centrée sur les <strong>processus</strong>.</td>
      </tr>
    </tbody>
  </table>
  <div class="key-box">
    <strong>Cycle PDCA (Roue de Deming) appliqué à la structure projet</strong> :
    <ul>
      <li><strong>Prévoir</strong></li>
      <li><strong>Faire</strong></li>
      <li><strong>Contrôler</strong> (autonomie)</li>
      <li><strong>Agir ou Réagir</strong></li>
    </ul>
  </div>

  <h3>Pour passer de la vision à l'action — 7 leviers</h3>
  <div class="key-box">
    <ol>
      <li>Avoir une <strong>offre choisie et non subie</strong></li>
      <li><strong>Choisir ses clients en segmentant</strong></li>
      <li>Cultiver les <strong>réseaux</strong> pour apporter une réponse globale et experte</li>
      <li>Cultiver la <strong>capacité innovante</strong> de l'organisation</li>
      <li>Assurer la <strong>convergence des compétences</strong> des collaborateurs</li>
      <li>Intensifier la <strong>transversalité</strong> de l'organisation</li>
      <li>Construire une <strong>offre experte (notre métier) et globale (partenaires)</strong></li>
    </ol>
  </div>

  <h3>Management et performance — 3 conditions</h3>
  <div class="def-box">
    <ul>
      <li>Il n'y a <strong>pas de performance sans management</strong></li>
      <li>Il n'y a <strong>pas de management sans stratégie partagée</strong></li>
      <li>Il n'y a <strong>pas de réussite sans management</strong></li>
    </ul>
    <p style="margin-top:0.8rem; font-style:italic;">Les équipes sont au cœur de la performance organisationnelle.</p>
  </div>

  <h3>Piloter la performance organisationnelle</h3>
  <div class="example-box">
    <em>« L'art de diriger consiste à abandonner la baguette pour ne pas gêner l'orchestre. »</em> — <strong>Herbert von Karajan</strong>
  </div>
  <table class="comp-table">
    <thead><tr><th>Piloter, pourquoi ?</th><th>Piloter, c'est quoi ?</th><th>Au quotidien ?</th></tr></thead>
    <tbody>
      <tr>
        <td>Car on ne peut progresser que sur ce que l'on mesure. La mesure des écarts et leur correction partagée et comprise permet à chacun de progresser.</td>
        <td>Piloter, c'est <strong>déployer la stratégie en actions</strong>. Ces actions doivent être mesurées et vérifiées régulièrement.</td>
        <td>Pour chaque action pilotée : désigner un <strong>pilote</strong>, une <strong>fréquence</strong>, un <strong>moyen de mesure</strong>, une <strong>communication</strong>.</td>
      </tr>
    </tbody>
  </table>
  <div class="key-box">
    <strong>3 piliers du pilotage au quotidien</strong> :
    <ul>
      <li><strong>PILOTAGE</strong> — Maîtriser</li>
      <li><strong>INDICATEURS</strong> — Garder le contrôle</li>
      <li><strong>INFORMATIONS</strong> — Expliquer, anticiper</li>
    </ul>
  </div>

  <h3>Conclusion — CO-CONSTRUIRE / CO-AGIR / CO-RESPONSABLE</h3>
  <div class="def-box">
    <p style="text-align:center; font-size:1.05rem;">La performance est <strong>éphémère</strong> et il convient à chaque instant de <strong>renouveler l'expérience collective</strong> qui permet de la construire.</p>
    <p style="text-align:center; font-weight:700; font-size:1.1rem; margin-top:1rem; color:var(--copper);">
      CO-CONSTRUIRE pour CO-AGIR et être CO-RESPONSABLE
    </p>
  </div>
</div>
`;
}
'''


# ═══════════════════════════════════════════════════════════════════════════
# NOUVEAU JSON — themes, flashcards, quiz, checklist Besombes uniquement
# ═══════════════════════════════════════════════════════════════════════════
NEW_THEMES = [
    {"id": "intro", "icon": "🌍", "label": "Introduction & contexte"},
    {"id": "dppo", "icon": "🎯", "label": "DPPO Drucker"},
    {"id": "processus", "icon": "⚙️", "label": "Approche processus & ISO 9001"},
    {"id": "performance", "icon": "📊", "label": "Performance"},
    {"id": "pilotage", "icon": "🧭", "label": "Pilotage & dialogue social"},
]

NEW_CHECKLIST = [
    {"id": "eo1", "label": "Frise historique : du feu (−400 000) à l'IA (2030)"},
    {"id": "eo2", "label": "3 logiques économiques : Production (1900) → Vente (1950) → Création de valeur"},
    {"id": "eo3", "label": "Quelles organisations aujourd'hui ? (virtuelles, fabless-fab, multi-PME, territoires)"},
    {"id": "eo4", "label": "Schéma BOR : Besoin / Organisation / Réponse — cohérence RH × Matériel/Financier"},
    {"id": "eo5", "label": "Les 12 thèmes structurants du cours Besombes"},
    {"id": "eo6", "label": "DPPO de Peter Drucker (1954) — 6 principes fondamentaux"},
    {"id": "eo7", "label": "Champ des objectifs opérationnels DPPO (structure, équipes, pilotage)"},
    {"id": "eo8", "label": "Stratégie de différenciation — avantage concurrentiel par perception client"},
    {"id": "eo9", "label": "Le métier comme combinaison de savoir-faire"},
    {"id": "eo10", "label": "Joseph Tainter — 6 facteurs de l'effondrement par complexité"},
    {"id": "eo11", "label": "Étude Deloitte 2016 (Philippe Burger) — réseau d'équipes (90 % / 11 %)"},
    {"id": "eo12", "label": "Concept organisationnel — transversalité, autonomie, innovation, satisfaction client"},
    {"id": "eo13", "label": "Culture d'entreprise — histoire, identité, règles du jeu, croyances"},
    {"id": "eo14", "label": "Citation Paul Valéry : « Un bon chef est celui qui a besoin des autres »"},
    {"id": "eo15", "label": "Norme ISO 8402 + ISO 9001 v.2000 — définition formelle du processus"},
    {"id": "eo16", "label": "3 types de processus : Réalisation / Support / Pilotage"},
    {"id": "eo17", "label": "Vocabulaire : Macroprocessus → Processus → Sous-processus → Tâches"},
    {"id": "eo18", "label": "Tortue de Crosby — 4 questions (Avec quoi / Avec qui / Comment / Combien)"},
    {"id": "eo19", "label": "Cartographie des processus + interactions"},
    {"id": "eo20", "label": "Dualité Stratégie-Organisation — Chandler 1962, Edgar Morin (ago-antagoniste)"},
    {"id": "eo21", "label": "Approche US Navy de la performance (mission, outputs, standards, budget, reporting)"},
    {"id": "eo22", "label": "Efficacité vs Efficience selon Drucker (bonnes choses / bonne façon)"},
    {"id": "eo23", "label": "Modèle de Gilbert (1980) — triangle Objectifs / Moyens / Résultats"},
    {"id": "eo24", "label": "Michel Crozier (1922-2013) — analyse stratégique, organisation = corps vivant"},
    {"id": "eo25", "label": "Arbre de décision dynamique : Pouvoir / Droit / Intérêt"},
    {"id": "eo26", "label": "Dialogue social — citation Ghosn (5 % stratégie / 95 % action)"},
    {"id": "eo27", "label": "4 niveaux : TOP / Proximité / Opérateurs / IRP — formel & informel"},
    {"id": "eo28", "label": "Migration structure fonctionnelle → structure projet (PDCA)"},
    {"id": "eo29", "label": "7 leviers pour passer de la vision à l'action"},
    {"id": "eo30", "label": "3 conditions du management (performance / stratégie partagée / réussite)"},
    {"id": "eo31", "label": "Citation Karajan : « L'art de diriger consiste à abandonner la baguette »"},
    {"id": "eo32", "label": "Pilotage au quotidien : pilote + fréquence + mesure + communication"},
    {"id": "eo33", "label": "Conclusion : CO-CONSTRUIRE / CO-AGIR / CO-RESPONSABLE"},
]

NEW_FLASHCARDS = [
    # ─── INTRO ───
    {"q": "Frise historique de l'évolution des organisations", "a": "Selon Besombes, 4 jalons clés :\n• −400 000 av. J.-C. : maîtrise du feu\n• XVIIIe siècle : Révolution industrielle\n• Fin XXe : TIC\n• 2030 : IA\n\n3 tensions permanentes structurent toute organisation : Pouvoir, Contre-pouvoir, Spécialisation.", "theme": "intro"},
    {"q": "Les 3 logiques économiques successives", "a": "• 1900 : Logique de PRODUCTION\n• 1950 : Logique de VENTE\n• Aujourd'hui : Logique de CRÉATION DE VALEUR", "theme": "intro"},
    {"q": "Quelles organisations aujourd'hui ? (Besombes)", "a": "4 formes typiques :\n• Entreprises virtuelles\n• Industries sans usines (fabless-fab)\n• Grandes entreprises composées d'une multitude de PME\n• Entreprises sur l'ensemble des territoires", "theme": "intro"},
    {"q": "Schéma BOR — la logique permanente", "a": "Besoin → Organisation → Réponse\n\nLa cohérence de l'organisation repose sur 2 piliers :\n• Ressources humaines / compétences\n• Ressources matérielles et financières", "theme": "intro"},
    {"q": "Les 12 thèmes du cours Besombes", "a": "① IA · ② Robotique/cobotique · ③ Capital humain · ④ Stratégie vs Organisation · ⑤ Contingence organisationnelle · ⑥ Innovation · ⑦ RSE · ⑧ Réseau et territoire · ⑨ Approche systémique et processus · ⑩ Chaîne de valeur et globalisation · ⑪ Productivité vs création de valeur · ⑫ Nouvelles formes de travail", "theme": "intro"},
    {"q": "Changement de paradigme dans le management", "a": "Évolution :\n• Logique de TÂCHES (école classique)\n→\n• Logique d'OBJECTIFS (orientée performance)\n\nCette bascule fonde la DPPO de Drucker.", "theme": "intro"},
    {"q": "Stratégie de différenciation — Besombes", "a": "4 principes-clés :\n• La différenciation est à l'origine des avantages concurrentiels décisifs\n• Seules les différences PERÇUES PAR LE CLIENT ont de la valeur\n• Les différences complexes s'appuient sur la spécialisation\n• La perception de la différence est liée à la maîtrise de l'ensemble de la chaîne de valeur", "theme": "intro"},
    {"q": "Le métier et le savoir-faire", "a": "• Le métier = somme des savoir-faire acquis + capacité à les combiner\n• Le processus combinatoire varie d'une organisation à l'autre\n• Difficile à décrire car les combinaisons sont informelles\n• La vision du métier par un manager conditionne sa capacité à découvrir de nouvelles voies", "theme": "intro"},
    {"q": "Tainter — théorie de l'effondrement par complexité (6 facteurs)", "a": "Joseph Tainter étudie les effondrements de sociétés :\n1) Les sociétés sont des organisations pour résoudre des problèmes\n2) Les systèmes sociopolitiques ont besoin d'énergie pour se maintenir\n3) La complexité accrue porte des coûts accrus par habitant\n4) L'investissement dans la complexité atteint un point de rendements marginaux décroissants\n5) Quand le rendement décline, la société investit toujours plus dans une stratégie moins rentable\n6) Les rendements décroissants poussent à la séparation ou désintégration (sécession)", "theme": "intro"},
    {"q": "Étude Deloitte 2016 (Philippe Burger) — réseau d'équipes", "a": "Chiffres clés :\n• 90 % des entreprises françaises envisagent une évolution de leur organisation\n• 11 % déclarent avoir une structure construite autour de projets/programmes transverses\n\nLe « réseau d'équipes » est un nouveau modèle organisationnel : équipes responsables, flexibles, interconnectées, partout dans le monde.", "theme": "intro"},
    {"q": "Concept organisationnel — 4 principes généraux", "a": "Principes du modèle contemporain :\n• Transversalité\n• Autonomie vs Responsabilité\n• Initiative et innovation\n• Orientation Satisfaction Client", "theme": "intro"},
    {"q": "La culture d'entreprise (Besombes)", "a": "4 caractéristiques :\n• Elle existe toujours, qu'elle soit connue ou non\n• Fondée sur les habitudes, attitudes sociales, histoire de chacun\n• Confrontation entre valeurs personnelles et culture déclarée\n• Fondée sur une histoire, une identité, des règles du jeu, des croyances et des routines", "theme": "intro"},
    {"q": "Citation Paul Valéry sur le management", "a": "« Un bon chef est celui qui a besoin des autres » — Paul Valéry\n\nPour construire la performance, il faut : FAIRE RÉUSSIR LES AUTRES.", "theme": "intro"},

    # ─── DPPO ───
    {"q": "DPPO — Direction Par Objectifs (Peter Drucker, 1954)", "a": "Concept conceptualisé en 1954 par Peter Drucker (1909-2005).\n\nC'est le passage d'une logique de TÂCHES à une logique d'OBJECTIFS, fondateur du management contemporain.", "theme": "dppo"},
    {"q": "Les 6 principes fondamentaux de la DPPO (Drucker)", "a": "1) Définir la mission de son entité\n2) Fixer des objectifs clairs pour les équipes\n3) Analyser et organiser le travail pour créer un sentiment de satisfaction\n4) Informer et écouter ses employés\n5) Évaluer les résultats au moyen de normes spécifiques\n6) Former ses collaborateurs en permanence", "theme": "dppo"},
    {"q": "Le champ des objectifs opérationnels (DPPO)", "a": "3 dimensions d'évolution :\n• STRUCTURE : de hiérarchique à transversale\n• ÉQUIPES : déclinaison des objectifs stratégiques en objectifs opérationnels pour chaque pôle et chaque collaborateur\n• PILOTAGE & AMÉLIORATION : participation des collaborateurs au déploiement des procédures + information sur les indicateurs", "theme": "dppo"},

    # ─── PROCESSUS ───
    {"q": "L'évolution du management : de la tâche au processus", "a": "Passage :\n• Logique de « tâches » (école classique)\n→\n• Approche « processus » orientée vers la performance et l'excellence", "theme": "processus"},
    {"q": "Définition formelle du processus (ISO 8402)", "a": "« Ensemble des moyens et d'activités qui transforment les éléments entrants en éléments sortants dans un but défini et mesurable » (ISO 8402, cité par P. Baracchini, 2007)\n\nPlus simplement : ensemble homogène de sous-processus et de tâches qui s'enchaînent pour transformer des intrants en extrants.", "theme": "processus"},
    {"q": "Les 3 types de processus", "a": "• PROCESSUS DE RÉALISATION : réalisation du produit/service (conception, fabrication, vente, prestation)\n• PROCESSUS SUPPORT : outils et méthodes appuyant la réalisation (RH, formation, IT, comptabilité, maintenance)\n• PROCESSUS DE PILOTAGE : mise en œuvre des objectifs (politique, stratégie, décision, budget, mesure)", "theme": "processus"},
    {"q": "Vocabulaire hiérarchique des processus", "a": "4 niveaux :\n• MACROPROCESSUS : Client, RH…\n• PROCESSUS : ensemble de sous-processus\n• SOUS-PROCESSUS : ensemble de tâches\n• TÂCHES : opération spécifique", "theme": "processus"},
    {"q": "Norme ISO 9001 version 2000 — schéma SMQ", "a": "Système de Management de la Qualité — boucle d'amélioration continue :\n\nClient (exigences) → Données d'entrée → Réalisation du produit/service → Données de sortie → Client (satisfaction)\n\nSupervisé par : Responsabilité de la direction + Management des ressources + Mesure/analyse/amélioration", "theme": "processus"},
    {"q": "La tortue de Crosby — 4 questions pour caractériser un processus", "a": "• AVEC QUOI ? — Moyens et équipements\n• AVEC QUI ? — Compétences\n• COMMENT ? — Méthodes\n• COMBIEN ? — Indicateurs de pilotage", "theme": "processus"},
    {"q": "Interactions entre processus + cartographie", "a": "Démarche :\n1) Identifier les processus entre lesquels il existe une interaction\n2) Définir la nature de l'interaction (sortie de l'un = entrée d'un autre)\n3) Établir un diagramme de toutes les interactions = CARTOGRAPHIE des processus", "theme": "processus"},
    {"q": "Nature des processus et chaîne de valeur", "a": "2 catégories de processus :\n• Ceux dont les sorties sont associées aux EXIGENCES DES CLIENTS\n• Ceux dont les sorties ont une incidence sur l'EFFICACITÉ DES AUTRES PROCESSUS\n\nLe processus produit de la VALEUR AJOUTÉE des fournisseurs vers les clients, à travers des MOYENS et des RÈGLES.", "theme": "processus"},

    # ─── PERFORMANCE ───
    {"q": "Dualité Stratégie-Organisation (Besombes)", "a": "L'entreprise doit avoir une démarche pro-active de CONQUÊTE tout en LIMITANT LE RISQUE.\n\n• Convergence d'éléments AGO-ANTAGONISTES (Edgar Morin)\n• Lien indissociable structure ↔ stratégie (Chandler, « Structure follows Strategy », 1962)\n• Maîtrise organisationnelle nécessaire : communication, comportements, jeux d'acteurs", "theme": "performance"},
    {"q": "Définition de la performance organisationnelle (Besombes)", "a": "4 caractéristiques :\n• Issue d'un PROCESSUS DE CONSTRUCTION CONTINGENT\n• Conséquence d'une REPRÉSENTATION (pas de réalité propre)\n• Résultat de l'ACCORD ENTRE LES PARTIES PRENANTES (consensus, coopération)\n• Devenue STRATÉGIQUE, contribue à l'émergence du « sens »\n\nDéfinition synthétique : résultat d'un processus maîtrisé pour atteindre un but préalablement défini, en mobilisant des ressources variées et optimisées.", "theme": "performance"},
    {"q": "L'approche US Navy de la performance", "a": "« Processus de définition de la mission et des outputs escomptés, de détermination des standards de la performance, de mise en relation du budget avec la performance, de reporting des résultats ainsi que de l'assurance que les managers sont comptables des résultats. »", "theme": "performance"},
    {"q": "Efficacité vs Efficience selon Drucker", "a": "• EFFICACITÉ : atteinte des résultats QUELLE QUE SOIT l'allocation de ressources = « Faire les bonnes choses »\n• EFFICIENCE : atteinte des résultats EN OPTIMISANT l'allocation de ressources = « Faire les choses de la bonne façon »\n\nLa performance dans un contexte donné = capacité d'être à la fois Efficace ET Efficient.", "theme": "performance"},
    {"q": "Modèle de Gilbert (1980) — triangle de la performance", "a": "PERFORMANCE = intersection de 3 dimensions :\n• OBJECTIFS\n• MOYENS\n• RÉSULTATS\n\nLes 3 écarts définissent :\n• Objectifs ↔ Résultats : EFFICACITÉ\n• Moyens ↔ Résultats : EFFICIENCE\n• Objectifs ↔ Moyens : PERTINENCE", "theme": "performance"},
    {"q": "Michel Crozier (1922-2013) — l'organisation est un corps vivant", "a": "Concepteur de l'ANALYSE STRATÉGIQUE et de l'ACTION COLLECTIVE.\n\n• Les organisations sont comparables à des organismes vivants\n• Les êtres vivants planifient, analysent, expérimentent et décident\n• Ils s'adaptent et innovent face aux évolutions et à l'environnement", "theme": "performance"},
    {"q": "L'arbre de décision dynamique de Crozier", "a": "3 leviers structurants en interaction :\n• POUVOIR\n• DROIT\n• INTÉRÊT\n\nCes 3 dimensions déterminent les jeux d'acteurs au sein de l'organisation.", "theme": "performance"},

    # ─── PILOTAGE ───
    {"q": "Citation Carlos Ghosn sur la stratégie", "a": "« La réussite d'une entreprise, c'est 5 % de stratégie et 95 % d'action. » — Carlos Ghosn\n\nCette citation justifie l'importance centrale du dialogue social et du pilotage opérationnel.", "theme": "pilotage"},
    {"q": "Le dialogue social — 4 niveaux d'acteurs", "a": "• TOP MANAGEMENT\n• MANAGEMENT DE PROXIMITÉ\n• OPÉRATEURS\n• IRP (Instances Représentatives du Personnel)\n\n2 registres : dialogue social FORMEL + dialogue social INFORMEL.\n\nObjectif : aller vers un dialogue social PERMANENT centré sur le projet à réussir ensemble.", "theme": "pilotage"},
    {"q": "Migration structure fonctionnelle → structure projet", "a": "STRUCTURE FONCTIONNELLE (contrôle) :\n• Communication séquentielle descendante (parfois ascendante)\n• Organisation centrée sur les TÂCHES\n\nSTRUCTURE PROJET :\n• Communication continue CIRCULAIRE\n• Organisation centrée sur les PROCESSUS\n\nCycle PDCA : Prévoir → Faire → Contrôler (autonomie) → Agir ou Réagir", "theme": "pilotage"},
    {"q": "Les 7 leviers pour passer de la vision à l'action", "a": "1) Avoir une offre choisie et non subie\n2) Choisir ses clients en segmentant\n3) Cultiver les réseaux pour une réponse globale et experte\n4) Cultiver la capacité innovante\n5) Assurer la convergence des compétences des collaborateurs\n6) Intensifier la transversalité\n7) Construire une offre experte (notre métier) ET globale (partenaires)", "theme": "pilotage"},
    {"q": "Management et performance — 3 conditions (Besombes)", "a": "• Il n'y a pas de PERFORMANCE sans MANAGEMENT\n• Il n'y a pas de MANAGEMENT sans STRATÉGIE PARTAGÉE\n• Il n'y a pas de RÉUSSITE sans MANAGEMENT\n\nLes équipes sont au cœur de la performance organisationnelle.", "theme": "pilotage"},
    {"q": "Citation Karajan sur le pilotage", "a": "« L'art de diriger consiste à abandonner la baguette pour ne pas gêner l'orchestre. » — Herbert von Karajan\n\nLa direction efficace consiste à donner l'autonomie aux acteurs après avoir donné le cap.", "theme": "pilotage"},
    {"q": "Pourquoi piloter ? (Besombes)", "a": "« On ne peut progresser que sur ce que l'on mesure. »\n\nLa mesure des écarts et leur correction partagée et comprise permet à chacun de progresser.", "theme": "pilotage"},
    {"q": "Qu'est-ce que piloter ?", "a": "Piloter, c'est DÉPLOYER LA STRATÉGIE EN ACTIONS.\n\nCes actions doivent être mesurées et vérifiées régulièrement pour s'assurer qu'elles satisfont à l'exigence stratégique.", "theme": "pilotage"},
    {"q": "Pilotage au quotidien — 4 éléments par action", "a": "Pour chaque action pilotée, désigner :\n• Un PILOTE\n• Une FRÉQUENCE\n• Un MOYEN DE MESURE\n• Une COMMUNICATION\n\n3 piliers : PILOTAGE (maîtriser) + INDICATEURS (garder le contrôle) + INFORMATIONS (expliquer, anticiper).", "theme": "pilotage"},
    {"q": "Conclusion du cours Besombes — CO-CONSTRUIRE / CO-AGIR / CO-RESPONSABLE", "a": "« La performance est éphémère et il convient à chaque instant de renouveler l'expérience collective qui permet de la construire. »\n\nCO-CONSTRUIRE pour CO-AGIR et être CO-RESPONSABLE", "theme": "pilotage"},
]

NEW_QUIZ = [
    {"q": "Selon Besombes, quelle est la séquence des 3 logiques économiques successives ?", "o": ["Vente → Production → Création de valeur", "Production (1900) → Vente (1950) → Création de valeur (aujourd'hui)", "Innovation → Vente → Production", "Création de valeur → Production → Vente"], "c": 1, "e": "Selon Besombes, l'évolution est : Logique de Production (1900) → Logique de Vente (1950) → Logique de Création de valeur (aujourd'hui).", "theme": "intro"},
    {"q": "En quelle année et par qui a été conceptualisée la DPPO ?", "o": ["1962 par Alfred Chandler", "1954 par Peter Drucker", "1980 par Gilbert", "1948 par Henri Fayol"], "c": 1, "e": "La Direction Par Objectifs (DPPO) a été conceptualisée en 1954 par Peter Drucker (1909-2005). C'est l'un des concepts les plus structurants du management moderne.", "theme": "dppo"},
    {"q": "Combien de principes fondamentaux compte la DPPO de Drucker ?", "o": ["4 principes", "5 principes", "6 principes", "8 principes"], "c": 2, "e": "La DPPO compte 6 principes : définir la mission, fixer des objectifs clairs, analyser/organiser le travail, informer/écouter, évaluer les résultats, former en permanence.", "theme": "dppo"},
    {"q": "Quel auteur a énoncé la théorie de l'effondrement par complexité décroissante ?", "o": ["Edgar Morin", "Joseph Tainter", "Peter Drucker", "Michel Crozier"], "c": 1, "e": "Joseph Tainter a étudié les effondrements de sociétés dans l'histoire et identifié 6 facteurs liés aux rendements marginaux décroissants de la complexité sociopolitique.", "theme": "intro"},
    {"q": "Selon l'étude Deloitte de juin 2016, quelle proportion d'entreprises françaises ont une structure organisée autour de projets transverses ?", "o": ["5 %", "11 %", "30 %", "45 %"], "c": 1, "e": "Selon Philippe Burger (Deloitte, juin 2016), 11 % des entreprises françaises déclarent avoir une structure construite autour de projets ou programmes transverses. Cette structure émergente est appelée « réseau d'équipes ».", "theme": "intro"},
    {"q": "Quelle norme ISO définit formellement le processus ?", "o": ["ISO 9001:2000", "ISO 8402", "ISO 14001", "ISO 26000"], "c": 1, "e": "L'ISO 8402 définit le processus comme « ensemble des moyens et d'activités qui transforment les éléments entrants en éléments sortants dans un but défini et mesurable ». La norme ISO 9001 v.2000 structure le SMQ qui s'appuie sur cette définition.", "theme": "processus"},
    {"q": "Quels sont les 3 types de processus selon l'approche processus ?", "o": ["Stratégique / Opérationnel / Support", "Réalisation / Support / Pilotage", "Client / Interne / Fournisseur", "Direction / Exécution / Contrôle"], "c": 1, "e": "Les 3 types sont : Processus de Réalisation (produit/service), Processus Support (RH/IT/compta/maintenance), Processus de Pilotage (politique/stratégie/décision/budget/mesure).", "theme": "processus"},
    {"q": "Que mesure la « tortue de Crosby » ?", "o": ["Le délai de traitement d'une commande", "Les caractéristiques d'un processus via 4 questions (Avec quoi/qui/comment/combien)", "Le coût total de la non-qualité", "La maturité d'une organisation sur 5 niveaux"], "c": 1, "e": "La tortue de Crosby caractérise un processus avec 4 questions : AVEC QUOI ? (moyens/équipements) — AVEC QUI ? (compétences) — COMMENT ? (méthodes) — COMBIEN ? (indicateurs).", "theme": "processus"},
    {"q": "Comment Drucker distingue-t-il efficacité et efficience ?", "o": ["L'efficacité concerne les coûts, l'efficience le temps", "L'efficacité = faire les bonnes choses ; l'efficience = faire les choses de la bonne façon", "Les deux termes sont synonymes", "L'efficacité concerne le QCD ; l'efficience le ROI"], "c": 1, "e": "Selon Drucker : « L'efficacité consiste à faire les bonnes choses et l'efficience consiste à faire les choses de la bonne façon ». L'efficacité = atteinte des résultats quelque soit l'allocation ; l'efficience = atteinte en optimisant les ressources.", "theme": "performance"},
    {"q": "Quel est le triangle du Modèle de Gilbert (1980) ?", "o": ["Performance / Coût / Qualité", "Objectifs / Moyens / Résultats", "Stratégie / Organisation / Culture", "Mission / Vision / Valeurs"], "c": 1, "e": "Le Modèle de Gilbert (1980) est un triangle Objectifs / Moyens / Résultats. Les 3 écarts définissent : Efficacité (Objectifs ↔ Résultats), Efficience (Moyens ↔ Résultats), Pertinence (Objectifs ↔ Moyens).", "theme": "performance"},
    {"q": "Qui est l'auteur de l'expression « ago-antagoniste » mobilisée par Besombes pour décrire la dualité Stratégie-Organisation ?", "o": ["Alfred Chandler", "Peter Drucker", "Edgar Morin", "Michel Crozier"], "c": 2, "e": "Edgar Morin parle de convergence d'éléments « ago-antagonistes » : l'entreprise doit avoir une démarche pro-active de conquête tout en limitant le risque associé. C'est mobilisé pour décrire la dualité Stratégie-Organisation.", "theme": "performance"},
    {"q": "À quel auteur attribue-t-on la formule « Structure follows Strategy » (1962) ?", "o": ["Alfred Chandler", "Henry Mintzberg", "Peter Drucker", "Michael Porter"], "c": 0, "e": "Alfred Chandler, dans Strategy and Structure (1962), formule le lien indissociable entre structure et stratégie : la structure suit la stratégie. Concept central pour comprendre la dualité Stratégie-Organisation chez Besombes.", "theme": "performance"},
    {"q": "Michel Crozier (1922-2013) est connu comme le concepteur de :", "o": ["La théorie des coûts de transaction", "L'analyse stratégique et de l'action collective", "La pyramide des besoins", "La théorie X et Y"], "c": 1, "e": "Michel Crozier est le concepteur de l'analyse stratégique et de l'action collective. Pour lui, les organisations sont comparables à des organismes vivants : elles planifient, analysent, expérimentent, décident et s'adaptent.", "theme": "performance"},
    {"q": "Quels sont les 3 leviers de l'arbre de décision dynamique selon Crozier ?", "o": ["Pouvoir / Droit / Intérêt", "Mission / Vision / Valeurs", "Stratégie / Tactique / Opérationnel", "Direction / Coordination / Contrôle"], "c": 0, "e": "Crozier identifie 3 leviers en interaction qui structurent les jeux d'acteurs : Pouvoir, Droit et Intérêt.", "theme": "performance"},
    {"q": "Selon Carlos Ghosn, la réussite d'une entreprise repose sur :", "o": ["50 % stratégie / 50 % action", "5 % stratégie / 95 % action", "20 % stratégie / 80 % action", "100 % stratégie"], "c": 1, "e": "Carlos Ghosn affirme : « La réussite d'une entreprise, c'est 5 % de stratégie et 95 % d'action. » Cette citation, mobilisée par Besombes, justifie l'importance centrale du dialogue social et du pilotage opérationnel.", "theme": "pilotage"},
    {"q": "Quels sont les 4 niveaux du dialogue social ?", "o": ["DG / Cadres / Employés / Ouvriers", "TOP / Proximité / Opérateurs / IRP", "Stratégique / Tactique / Opérationnel / Support", "Direction / Encadrement / Production / Syndicats"], "c": 1, "e": "Le dialogue social mobilise 4 niveaux d'acteurs : TOP MANAGEMENT, MANAGEMENT DE PROXIMITÉ, OPÉRATEURS, IRP (Instances Représentatives du Personnel). 2 registres : formel + informel.", "theme": "pilotage"},
    {"q": "À quoi correspond le cycle PDCA dans la structure projet ?", "o": ["Plan / Do / Check / Act", "Prévoir / Faire / Contrôler / Agir ou Réagir", "Préparer / Décider / Coordonner / Auditer", "Toutes les réponses sont équivalentes"], "c": 3, "e": "Le PDCA (Roue de Deming) appliqué à la structure projet par Besombes : Prévoir (Plan) / Faire (Do) / Contrôler avec autonomie (Check) / Agir ou Réagir (Act). Communication continue circulaire centrée sur les processus.", "theme": "pilotage"},
    {"q": "Selon Besombes, combien de leviers permettent de passer de la vision à l'action ?", "o": ["3 leviers", "5 leviers", "7 leviers", "10 leviers"], "c": 2, "e": "Besombes identifie 7 leviers : offre choisie/non subie · choisir ses clients en segmentant · cultiver les réseaux · cultiver la capacité innovante · convergence des compétences · transversalité · offre experte ET globale.", "theme": "pilotage"},
    {"q": "Qui a dit : « L'art de diriger consiste à abandonner la baguette pour ne pas gêner l'orchestre » ?", "o": ["Peter Drucker", "Carlos Ghosn", "Herbert von Karajan", "Paul Valéry"], "c": 2, "e": "Citation d'Herbert von Karajan mobilisée par Besombes pour illustrer l'art du pilotage : donner le cap puis laisser l'autonomie aux acteurs.", "theme": "pilotage"},
    {"q": "Selon Besombes, pourquoi piloter ?", "o": ["Pour contrôler les salariés", "Car on ne progresse que sur ce que l'on mesure", "Pour réduire les coûts", "Pour satisfaire les actionnaires"], "c": 1, "e": "« On ne peut progresser que sur ce que l'on mesure. » La mesure des écarts et leur correction partagée et comprise permet à chacun de progresser.", "theme": "pilotage"},
    {"q": "Selon Besombes, piloter c'est :", "o": ["Surveiller les indicateurs financiers", "Déployer la stratégie en actions mesurées et vérifiées régulièrement", "Établir un budget annuel", "Tenir des réunions hebdomadaires"], "c": 1, "e": "Piloter, c'est déployer la stratégie en actions. Ces actions doivent être mesurées et vérifiées régulièrement pour s'assurer qu'elles satisfont à l'exigence stratégique.", "theme": "pilotage"},
    {"q": "Pour piloter au quotidien, Besombes recommande de désigner pour chaque action :", "o": ["Un pilote, une fréquence, un moyen de mesure, une communication", "Un sponsor exécutif et un chef de projet", "Un budget et un délai", "Un livrable et une date limite"], "c": 0, "e": "Pour chaque action pilotée : un PILOTE + une FRÉQUENCE + un MOYEN DE MESURE + une COMMUNICATION. 3 piliers : Pilotage (maîtriser) + Indicateurs (garder le contrôle) + Informations (expliquer, anticiper).", "theme": "pilotage"},
    {"q": "Quelle est la conclusion du cours de Besombes ?", "o": ["La performance est durable et stable", "CO-CONSTRUIRE pour CO-AGIR et être CO-RESPONSABLE", "Il faut maximiser la productivité", "La stratégie est plus importante que l'organisation"], "c": 1, "e": "« La performance est éphémère et il convient à chaque instant de renouveler l'expérience collective qui permet de la construire. CO-CONSTRUIRE pour CO-AGIR et être CO-RESPONSABLE. »", "theme": "pilotage"},
    {"q": "Selon Besombes, le métier d'une organisation est :", "o": ["La description de poste de chaque collaborateur", "La somme des savoir-faire acquis + la capacité de les combiner", "L'ensemble des compétences requises par le poste", "La fiche de poste validée par la DRH"], "c": 1, "e": "Le métier = somme des savoir-faire acquis + capacité combinatoire. Le processus combinatoire est informel et varie d'une organisation à l'autre. La vision du métier par un manager conditionne sa capacité à découvrir de nouvelles voies.", "theme": "intro"},
    {"q": "Selon Besombes, qu'est-ce qui crée un avantage concurrentiel décisif ?", "o": ["Le prix le plus bas", "La stratégie de différenciation perçue par le client", "Les économies d'échelle", "La concentration sectorielle"], "c": 1, "e": "Les stratégies de différenciation sont à l'origine des avantages concurrentiels décisifs, MAIS seules les différences PERÇUES par le client ont de la valeur. La perception est liée à la maîtrise de l'ensemble de la chaîne de valeur.", "theme": "intro"},
]


# ═══════════════════════════════════════════════════════════════════════════
# APPLICATION
# ═══════════════════════════════════════════════════════════════════════════
def rewrite_html():
    text = HTML.read_text()
    # Remplace tout le bloc getCoursHTML par le nouveau
    pattern = re.compile(r'function getCoursHTML\(\)\s*\{\s*return\s*`[\s\S]*?`;\s*\}\n', re.MULTILINE)
    n = len(pattern.findall(text))
    if n == 0:
        raise SystemExit('getCoursHTML non trouvé dans evo_orga.html')
    new_text = pattern.sub(NEW_COURS, text, count=1)
    HTML.write_text(new_text)
    print(f'✓ evo_orga.html : getCoursHTML réécrit (Besombes uniquement)')


def rewrite_json():
    d = json.loads(JSON.read_text())
    d['themes'] = NEW_THEMES
    d['flashcards'] = NEW_FLASHCARDS
    d['quizQuestions'] = NEW_QUIZ
    d['checklistItems'] = NEW_CHECKLIST
    # Mettre à jour le titre/sous-titre si besoin
    d['title'] = 'Évolution des modèles d\'organisation'
    d['subtitle'] = 'Cours F. Besombes — DPPO · Processus · Performance · Pilotage'
    # Annales préservées telles quelles
    JSON.write_text(json.dumps(d, ensure_ascii=False, indent=2))
    print(f'✓ data/evo_orga.json :')
    print(f'   themes        : {len(NEW_THEMES)} (intro, dppo, processus, performance, pilotage)')
    print(f'   flashcards    : {len(NEW_FLASHCARDS)}')
    print(f'   quizQuestions : {len(NEW_QUIZ)}')
    print(f'   checklistItems: {len(NEW_CHECKLIST)}')


if __name__ == '__main__':
    rewrite_html()
    rewrite_json()
