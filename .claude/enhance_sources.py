"""Améliore le système de traçabilité :
1. Retire le nom du prof du champ `src` (Besombes/Robin/Tellier/Lebey/Duheron)
2. Ajoute un champ `srcChap` = numéro de chapitre cible pour le deep-link
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / 'data'

# Mapping (préfixe du src après strip prof) → numéro de chapitre cible
# Chaque liste est traitée du plus spécifique au moins spécifique (premier match gagne)
CHAP_MAPPINGS = {
    'conduite_chgt': [
        # PDF Conduite du changement (47 slides)
        ('Conduite p.3', 1),       # Le Chatelier
        ('Conduite p.4', 3),       # Kotter (titre)
        ('Conduite p.5', 2),       # Lewin 3 phases
        ('Conduite p.6', 3),       # Kübler-Ross
        ('Conduite p.7', 4),       # 3 facteurs psycho
        ('Conduite p.8-9', 4),     # 7 résistances + leviers
        ('Conduite p.8', 4),       # 7 résistances
        ('Conduite p.9', 4),       # leviers anti-résistance
        ('Conduite p.10', 4),      # 3 stratégies utiles
        ('Conduite p.12', 5),      # Univers du changement
        ('Conduite p.13-23', 5),   # Démarche 8 étapes
        ('Conduite p.13', 5),
        ('Conduite p.14', 5),      # Qui fait quoi
        ('Conduite p.15', 5),
        ('Conduite p.16', 5),
        ('Conduite p.17', 5),
        ('Conduite p.18', 5),
        ('Conduite p.19', 5),
        ('Conduite p.20', 5),
        ('Conduite p.21', 5),
        ('Conduite p.22', 5),
        ('Conduite p.23', 5),
        ('Conduite p.24', 5),
        ('Conduite p.25', 5),
        ('Conduite p.27-30', 6),   # Vocation 3 étapes
        ('Conduite p.27', 6),
        ('Conduite p.28', 6),
        ('Conduite p.29', 6),
        ('Conduite p.30', 6),
        ('Conduite p.31', 6),      # Qualifier solutions
        ('Conduite p.32', 6),      # Matrice priorisation
        ('Conduite p.33', 6),      # Mise en œuvre
        ('Conduite p.34-35', 7),
        ('Conduite p.36', 7),      # 10-80-10
        ('Conduite p.37-39', 7),   # Top/Middle/Métiers
        ('Conduite p.37', 7),
        ('Conduite p.38', 7),
        ('Conduite p.39', 7),
        ('Conduite p.40', 8),      # RACI
        ('Conduite p.41', 8),      # Grille communication
        ('Conduite p.42', 8),      # Instance décisionnaire
        ('Conduite p.43-45', 8),   # Matrices décision/impact
        ('Conduite p.46-47', 9),   # 10 points clés
        # PDF Gestion des Compétences (41 slides)
        ('Compétences p.3', 10),   # Rôle confié/perçu/accepté/tenu
        ('Compétences p.4', 10),
        ('Compétences p.5', 10),   # Problèmes RH
        ('Compétences p.6', 10),   # Définition compétence
        ('Compétences p.7', 10),   # 5 critères potentiel
        ('Compétences p.8', 10),   # Approche compétences pro
        ('Compétences p.9', 10),   # Référentiel
        ('Compétences p.10', 10),  # 4 outils
        ('Compétences p.11', 11),  # GPEC
        ('Compétences p.12', 11),  # Éthique performance
        ('Compétences p.14', 11),  # Organisation qualifiante
        ('Compétences p.15', 11),
        ('Compétences p.16', 11),
        ('Compétences p.18-19', 11),  # Description de poste
        ('Compétences p.18', 11),
        ('Compétences p.19', 11),
        ('Compétences p.20', 11),  # 3 dimensions compétences
        ('Compétences p.22', 11),  # Système d'évaluation intro
        ('Compétences p.23', 11),
        ('Compétences p.24', 11),
        ('Compétences p.25', 11),  # Sanction vs formative
        ('Compétences p.26', 11),
        ('Compétences p.27', 11),  # 3 missionnements
        ('Compétences p.28', 11),
        ('Compétences p.29', 11),
        ('Compétences p.30', 11),  # Culture 5 forces
        ('Compétences p.31-32', 12),  # 5 étapes équipe
        ('Compétences p.31', 12),
        ('Compétences p.32', 12),
        ('Compétences p.33', 12),  # Lewin équipe
        ('Compétences p.35', 12),  # Continuum
        ('Compétences p.36', 12),  # Cap/Actions/Ressources
        ('Compétences p.37', 12),  # 4 attentes manager
        ('Compétences p.38', 12),  # Agilité
        ('Compétences p.39', 12),
        ('Compétences p.40', 12),  # Gilbert 1980
        ('Compétences p.41', 12),
        ('Compétences', 10),       # default
        ('Conduite', 5),           # default
    ],
    'evo_orga': [
        ('Évo p.3-5', 1),
        ('Évo p.3', 1),
        ('Évo p.4', 1),
        ('Évo p.5', 1),
        ('Évo p.6', 1),
        ('Évo p.7', 1),
        ('Évo p.8', 2),    # 12 thèmes
        ('Évo p.9', 2),
        ('Évo p.10-12', 3),  # DPPO
        ('Évo p.10', 3),
        ('Évo p.11', 3),
        ('Évo p.12', 3),
        ('Évo p.13', 4),    # Différenciation
        ('Évo p.14', 5),    # Métier
        ('Évo p.15-16', 6), # Tainter
        ('Évo p.15', 6),
        ('Évo p.16', 6),
        ('Évo p.17', 7),    # Deloitte
        ('Évo p.18', 7),
        ('Évo p.19', 7),    # Culture
        ('Évo p.20', 7),    # Valéry
        ('Évo p.21-32', 8), # Approche processus
        ('Évo p.21', 8),
        ('Évo p.22', 8),
        ('Évo p.23', 8),
        ('Évo p.24', 8),
        ('Évo p.25', 8),
        ('Évo p.26', 8),
        ('Évo p.27', 8),
        ('Évo p.28', 8),
        ('Évo p.29', 8),
        ('Évo p.30', 8),
        ('Évo p.31', 8),
        ('Évo p.32', 8),
        ('Évo p.33-42', 9), # Performance
        ('Évo p.33', 9),
        ('Évo p.34', 9),
        ('Évo p.35', 9),
        ('Évo p.36', 9),
        ('Évo p.37', 9),
        ('Évo p.38', 9),
        ('Évo p.39', 9),
        ('Évo p.40', 9),
        ('Évo p.41', 9),
        ('Évo p.42', 10),   # Crozier
        ('Évo p.43', 10),
        ('Évo p.44', 11),   # Dialogue social
        ('Évo p.45', 11),   # Structure projet
        ('Évo p.46', 11),   # 7 leviers
        ('Évo p.47', 11),
        ('Évo p.48', 11),
        ('Évo p.49', 11),
        ('Évo p.50', 11),   # Karajan
        ('Évo p.51', 11),
        ('Évo p.52', 11),
        ('Évo p.53', 11),
        ('Évo p.54', 11),   # Conclusion
        ('Évo', 1),         # default
    ],
    'inge_fi': [
        ('Chap 1', 4),                    # CMPC
        ('Chap 2 (Marché monétaire)', 1),
        ('Chap 2 (IPO)', 2),
        ('Chap 2', 1),                    # Marchés (default)
        ('Chap 3', 3),                    # Obligations
        ('Chap 4', 4),
        ('Chap 5', 5),                    # Dérivés
        ('Chap 6', 6),                    # Options
        ('Chap 7', 7),                    # ESG
        ('Omnibus.docx', 7),
    ],
    'strat': [
        ('Intro', 1),
        ('P1 (Plateformes)', 6),
        ('P1 (Benavent 2016)', 7),
        ('P1 (Cusumano 2022)', 8),
        ('P1', 4),                # Business Model (default)
        ('P2 (Porter 1985)', 9),
        ('P2 (Koenig 2004)', 10),
        ('P2 (Baumard 2000)', 11),
        ('P2 (Hermès vs LVMH)', 11),
        ('P2 (Gillette vs Bic)', 12),
        ('P2', 9),                # default P2
        ('P3 (Johnson 2005)', 19),
        ('P3 (Friedman 1970)', 20),
        ('P3', 17),               # default P3
    ],
    'gouv': [
        ('Gouvernance', 3),       # ISACA + alignement par défaut
        ('Audit', 9),             # Audit des SI
        ('Audit/Gouv', 7),        # référentiels
        ('Sujet UE 7', 10),       # Enjeux numériques actuels
    ],
    'rse': [
        ('Omnibus.docx', 3),               # CSRD (Omnibus impacte CSRD)
        ('ESRS xlsx checklist', 4),        # ESRS
        ('RSE + ESRS xlsx', 4),
        ('RSE + Omnibus.docx', 3),
        ('RSE (Raworth 2010)', 2),
        ('RSE / Omnibus.docx', 3),
        ('RSE', 1),               # Fondamentaux (default)
    ],
}

PROF_PREFIXES = [
    'Besombes — ',
    'Robin — ',
    'Tellier — ',
    'Lebey — ',
    'Duheron — ',
]


def strip_prof(src):
    for prefix in PROF_PREFIXES:
        if src.startswith(prefix):
            return src[len(prefix):]
    return src


def find_chap(src_short, course):
    mapping = CHAP_MAPPINGS.get(course, [])
    # Trie par longueur de pattern décroissante pour matcher le plus spécifique d'abord
    sorted_map = sorted(mapping, key=lambda x: -len(x[0]))
    for prefix, chap in sorted_map:
        if src_short.startswith(prefix):
            return chap
    return None


def enhance(course):
    path = ROOT / f'{course}.json'
    if not path.exists():
        return
    d = json.loads(path.read_text())

    updated_fc = updated_q = 0
    for fc in d.get('flashcards', []):
        src = fc.get('src')
        if not src:
            continue
        new_src = strip_prof(src)
        chap = find_chap(new_src, course)
        fc['src'] = new_src
        if chap is not None:
            fc['srcChap'] = chap
        updated_fc += 1
    for q in d.get('quizQuestions', []):
        src = q.get('src')
        if not src:
            continue
        new_src = strip_prof(src)
        chap = find_chap(new_src, course)
        q['src'] = new_src
        if chap is not None:
            q['srcChap'] = chap
        updated_q += 1

    path.write_text(json.dumps(d, ensure_ascii=False, indent=2))
    # Compte combien ont srcChap renseigné
    fc_with_chap = sum(1 for fc in d['flashcards'] if fc.get('srcChap'))
    q_with_chap = sum(1 for q in d['quizQuestions'] if q.get('srcChap'))
    print(f'{course}: fc {updated_fc} mises à jour ({fc_with_chap} avec srcChap)'
          f' | quiz {updated_q} mises à jour ({q_with_chap} avec srcChap)')


if __name__ == '__main__':
    for c in ['conduite_chgt', 'evo_orga', 'inge_fi', 'strat', 'gouv', 'rse']:
        enhance(c)
