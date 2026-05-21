"""Réécrit getSynthHTML pour conduite_chgt et evo_orga avec UNIQUEMENT le contenu Besombes.
Le reste est purgé."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CONDUITE_NEW_SYNTH = '''function getSynthHTML() {
  return `

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(61,114,180,0.18)">🔄</div> Processus du changement (Besombes)
  </div>
  <div class="synth-grid">
    <div class="synth-mini"><strong>Loi de Le Chatelier</strong><p>Toute modification d'un équilibre provoque des phénomènes qui s'y opposent → associer augmentation des pressions ET diminution des résistances.</p></div>
    <div class="synth-mini"><strong>Lewin — 3 phases</strong><p>① Décristallisation (remise en cause) → ② Changement (tâches, structure, techniques, comportements) → ③ Cristallisation (renforcement positif).</p></div>
    <div class="synth-mini"><strong>Kotter</strong><p>Modèle de référence (titre seul chez Besombes — à connaître comme grille structurée).</p></div>
    <div class="synth-mini"><strong>Kübler-Ross</strong><p>Courbe du changement (schéma Philippe Moret) — réactions émotionnelles face au changement.</p></div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(176,90,71,0.18)">⚔️</div> Résistances &amp; stratégies
  </div>
  <div class="synth-grid">
    <div class="synth-mini"><strong>3 facteurs psychosociologiques</strong><p>Découverte d'attitudes différentes · image de soi vue par les autres · nouveau sens à un mot.</p></div>
    <div class="synth-mini"><strong>7 résistances</strong><p>Manque d'info · peur de l'inconnu · besoin de sécurité · besoin inexistant · peur de perdre des acquis · moment mal choisi · manque de ressources.</p></div>
    <div class="synth-mini"><strong>4 leviers</strong><p>Communiquer · Faire participer · Soutenir · Négocier.</p></div>
    <div class="synth-mini"><strong>3 stratégies utiles</strong><p>Coercition (sanctions/récompenses) · Persuasion rationnelle (logique) · Partage du pouvoir (responsabilisation).</p></div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(90,145,104,0.18)">📋</div> Démarche 8 étapes (Besombes)
  </div>
  <div class="synth-grid">
    <div class="synth-mini"><strong>① Amorcer + ② Diagnostic</strong><p>Définir une politique (facteurs internes + externes) puis analyser l'existant (forces/faiblesses, cartographie).</p></div>
    <div class="synth-mini"><strong>③ Nouveau cadre + ④ Mobiliser</strong><p>Documentation, carte compétences, formation, communication, outils pilotage + sensibilisation, compréhension, règles du jeu.</p></div>
    <div class="synth-mini"><strong>⑤ Plans d'action + ⑥ Mise en œuvre</strong><p>Hiérarchiser, calendrier, responsables, indicateurs → déployer en restant vigilant.</p></div>
    <div class="synth-mini"><strong>⑦ Mesurer + ⑧ S'améliorer</strong><p>Constater écarts, corriger, motiver → fixer de nouveaux objectifs (cycle ~2 ans).</p></div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(200,131,70,0.18)">🧭</div> Vocation 3 étapes &amp; outils
  </div>
  <div class="synth-grid">
    <div class="synth-mini"><strong>3 étapes vocation</strong><p>Écouter (compréhension) → Mobiliser (périmètre commun) → Faciliter (mise en œuvre).</p></div>
    <div class="synth-mini"><strong>Qualifier solutions</strong><p>Grille à 4 cases : Gains attendus / Contraintes / Points d'appui / Freins.</p></div>
    <div class="synth-mini"><strong>Prioriser</strong><p>Matrice Importance × Facilité (Maîtrise) — identifier les actions prioritaires et celles « au parking ».</p></div>
    <div class="synth-mini"><strong>RACI</strong><p>Responsable (1) · Acteur (1-n) · Contribution (0-n) · Information (0-n).</p></div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(138,122,168,0.18)">👥</div> Acteurs &amp; communication
  </div>
  <div class="synth-grid">
    <div class="synth-mini"><strong>3 comportements 10-80-10</strong><p>Proactifs (10-20 %, à utiliser) · Passifs (60-80 %, à rassurer) · Opposants (10-20 %, à laisser s'isoler).</p></div>
    <div class="synth-mini"><strong>3 niveaux d'acteurs</strong><p>Top Management (impulsion) → Middle Management (relais) → Ressources Métiers (terrain).</p></div>
    <div class="synth-mini"><strong>Grille communication</strong><p>« Pourquoi changer ? » → comm projet · « Qu'est-ce qui change ? » → sensibilisation · « À la hauteur ? » → formation · « Pas prêt ? » → assistance proximité.</p></div>
    <div class="synth-mini"><strong>10 points clés</strong><p>Participer · Factuel · Réaliste · Communiquer honnête · Coordonner · Accompagner · Mesurer · Méthodologie · DG + middle · Ressources métiers.</p></div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(77,154,168,0.18)">🎯</div> Compétences (Besombes)
  </div>
  <div class="synth-grid">
    <div class="synth-mini"><strong>Chaîne des rôles</strong><p>Rôle confié → perçu → accepté → tenu. La description de poste minimise l'écart confié/tenu.</p></div>
    <div class="synth-mini"><strong>Compétence</strong><p>Disposition à mobiliser, combiner, mettre en œuvre des ressources : savoir / savoir-faire / savoir-être (combinaison dynamique).</p></div>
    <div class="synth-mini"><strong>GPEC / GEPP</strong><p>Réduire de façon anticipée les écarts besoins / ressources (effectifs + compétences) avec implication du salarié.</p></div>
    <div class="synth-mini"><strong>Organisation qualifiante</strong><p>Enrichissement des tâches + volonté éducative + recherche de compétitivité (dictionnaire de compétences).</p></div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(61,114,180,0.18)">🤝</div> Équipe &amp; management
  </div>
  <div class="synth-grid">
    <div class="synth-mini"><strong>5 étapes d'équipe</strong><p>Constitution → Tension → Normalisation → Production → Dissolution.</p></div>
    <div class="synth-mini"><strong>Lewin (équipe)</strong><p>« L'essence d'un groupe est l'interdépendance de chacun de ses membres. »</p></div>
    <div class="synth-mini"><strong>Continuum management</strong><p>7 niveaux entre AUTORITÉ (directif) et IMPLICATIF (délégation, responsabilisant).</p></div>
    <div class="synth-mini"><strong>4 attentes manager</strong><p>Honnête (intégrité) · Compétent · Tourné vers l'avenir (vision) · Motivant.</p></div>
    <div class="synth-mini"><strong>Modèle Gilbert (1980)</strong><p>Performance = Objectifs × Moyens × Résultats. Écarts : Efficacité · Efficience · Pertinence.</p></div>
    <div class="synth-mini"><strong>Culture (5 forces)</strong><p>Mythes · Rites · Identité · Valeurs · Histoire.</p></div>
  </div>
</div>

`;
}
'''

EVO_NEW_SYNTH = '''function getSynthHTML() {
  return `

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(61,114,180,0.18)">🌍</div> Introduction &amp; contexte (Besombes)
  </div>
  <div class="synth-grid">
    <div class="synth-mini"><strong>Frise historique</strong><p>−400 000 (feu) → XVIIIe (Révolution industrielle) → fin XXe (TIC) → 2030 (IA). 3 tensions : Pouvoir / Contre-pouvoir / Spécialisation.</p></div>
    <div class="synth-mini"><strong>3 logiques</strong><p>1900 : production · 1950 : vente · aujourd'hui : création de valeur.</p></div>
    <div class="synth-mini"><strong>Schéma BOR</strong><p>Besoin → Organisation → Réponse, avec cohérence Ressources humaines × Ressources matérielles/financières.</p></div>
    <div class="synth-mini"><strong>12 thèmes du cours</strong><p>IA · Robotique/cobotique · Capital humain · Stratégie vs Organisation · Contingence · Innovation · RSE · Réseau/territoire · Processus · Chaîne de valeur · Productivité/création de valeur · Nouvelles formes de travail.</p></div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(176,90,71,0.18)">🎯</div> DPPO Drucker (1954)
  </div>
  <div class="synth-grid">
    <div class="synth-mini"><strong>6 principes Drucker</strong><p>① Mission · ② Objectifs clairs · ③ Analyser/organiser le travail · ④ Informer/écouter · ⑤ Évaluer · ⑥ Former.</p></div>
    <div class="synth-mini"><strong>Champ opérationnel</strong><p>Structure hiérarchique → transversale · objectifs stratégiques déclinés en opérationnels · pilotage participatif.</p></div>
    <div class="synth-mini"><strong>Différenciation</strong><p>Avantage concurrentiel décisif. Seules les différences perçues par le client ont de la valeur. Chaîne de valeur.</p></div>
    <div class="synth-mini"><strong>Métier</strong><p>Somme des savoir-faire + capacité combinatoire. La vision du métier conditionne la découverte de nouvelles voies.</p></div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(90,145,104,0.18)">⚙️</div> Approche processus &amp; ISO 9001
  </div>
  <div class="synth-grid">
    <div class="synth-mini"><strong>Définition (ISO 8402)</strong><p>Ensemble des moyens et activités qui transforment des entrants en sortants dans un but défini et mesurable (Baracchini 2007).</p></div>
    <div class="synth-mini"><strong>3 types de processus</strong><p>Réalisation · Support · Pilotage.</p></div>
    <div class="synth-mini"><strong>Vocabulaire</strong><p>Macroprocessus → Processus → Sous-processus → Tâches.</p></div>
    <div class="synth-mini"><strong>Tortue de Crosby</strong><p>4 questions : Avec quoi ? · Avec qui ? · Comment ? · Combien ?</p></div>
    <div class="synth-mini"><strong>ISO 9001:2000 (SMQ)</strong><p>Client (entrée) → Direction · Ressources · Réalisation · Mesure → Client (sortie). Amélioration continue.</p></div>
    <div class="synth-mini"><strong>Cartographie</strong><p>Identifier les interactions entre processus, leur nature, diagramme global.</p></div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(200,131,70,0.18)">📊</div> Performance (Besombes)
  </div>
  <div class="synth-grid">
    <div class="synth-mini"><strong>Dualité Stratégie-Organisation</strong><p>Pro-activité de conquête + limitation du risque (Morin : ago-antagoniste · Chandler 1962 : structure follows strategy).</p></div>
    <div class="synth-mini"><strong>Définition performance</strong><p>Processus contingent · représentation · accord parties prenantes · émergence du sens.</p></div>
    <div class="synth-mini"><strong>US Navy</strong><p>Mission · outputs · standards · budget · reporting · accountability.</p></div>
    <div class="synth-mini"><strong>Efficacité vs Efficience (Drucker)</strong><p>Efficacité = « faire les bonnes choses » · Efficience = « faire les choses de la bonne façon ».</p></div>
    <div class="synth-mini"><strong>Modèle Gilbert (1980)</strong><p>Performance = Objectifs / Moyens / Résultats → Efficacité · Efficience · Pertinence.</p></div>
    <div class="synth-mini"><strong>Crozier (1922-2013)</strong><p>Concepteur de l'analyse stratégique. Organisation = corps vivant. Arbre Pouvoir / Droit / Intérêt.</p></div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(138,122,168,0.18)">🧭</div> Pilotage &amp; dialogue social
  </div>
  <div class="synth-grid">
    <div class="synth-mini"><strong>Ghosn</strong><p>« La réussite : 5 % de stratégie et 95 % d'action. »</p></div>
    <div class="synth-mini"><strong>4 niveaux dialogue social</strong><p>TOP · Proximité · Opérateurs · IRP — formel + informel.</p></div>
    <div class="synth-mini"><strong>Structure fonctionnelle → projet</strong><p>De la communication séquentielle à la communication continue circulaire (PDCA : Prévoir-Faire-Contrôler-Agir).</p></div>
    <div class="synth-mini"><strong>7 leviers vision → action</strong><p>Offre choisie · Segmenter · Réseaux · Innovation · Convergence compétences · Transversalité · Offre experte+globale.</p></div>
    <div class="synth-mini"><strong>3 conditions du management</strong><p>Pas de performance sans management · pas de management sans stratégie partagée · pas de réussite sans management.</p></div>
    <div class="synth-mini"><strong>Pilotage quotidien</strong><p>Pilote + Fréquence + Mesure + Communication. Karajan : « abandonner la baguette pour ne pas gêner l'orchestre ».</p></div>
  </div>
</div>

<div class="synth-card">
  <div class="synth-card-title">
    <div class="synth-icon" style="background:rgba(77,154,168,0.18)">✨</div> Citations &amp; conclusion
  </div>
  <div class="synth-grid">
    <div class="synth-mini"><strong>Paul Valéry</strong><p>« Un bon chef est celui qui a besoin des autres. »</p></div>
    <div class="synth-mini"><strong>Étude Deloitte 2016</strong><p>90 % des entreprises envisagent une évolution. 11 % ont une structure projet/transverse → « réseau d'équipes » (Philippe Burger).</p></div>
    <div class="synth-mini"><strong>Tainter</strong><p>Effondrement par complexité — 6 facteurs (résolution problèmes → coûts par habitant → rendements marginaux décroissants → sécession).</p></div>
    <div class="synth-mini"><strong>Conclusion</strong><p>La performance est éphémère. CO-CONSTRUIRE pour CO-AGIR et être CO-RESPONSABLE.</p></div>
  </div>
</div>

`;
}
'''


def replace_synth(html_file, new_synth):
    path = ROOT / html_file
    text = path.read_text()
    # Pattern : function getSynthHTML() { ... } puis blank line OR /* ═══════ TABS ═══════ */ ou autre fonction
    pattern = re.compile(r'function getSynthHTML\(\)\s*\{\s*return\s*`[\s\S]*?`;\s*\}\n', re.MULTILINE)
    if not pattern.search(text):
        raise SystemExit(f'{html_file}: getSynthHTML non trouvé')
    new_text = pattern.sub(new_synth, text, count=1)
    path.write_text(new_text)
    print(f'✓ {html_file} : getSynthHTML réécrit (Besombes strict)')


if __name__ == '__main__':
    replace_synth('conduite_chgt.html', CONDUITE_NEW_SYNTH)
    replace_synth('evo_orga.html', EVO_NEW_SYNTH)
