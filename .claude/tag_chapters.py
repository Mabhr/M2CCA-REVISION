"""Tag <div class="course-chapter"> with data-theme + data-chap-idx in each HTML file.

Mapping is 1-based chapter index → theme id (matching themes in the course's JSON).
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

MAPPINGS = {
    'conduite_chgt.html': {
        # Réécrit en Besombes strict (12 chapitres)
        1: 'processus_chgt', 2: 'processus_chgt', 3: 'processus_chgt', 4: 'processus_chgt',
        5: 'demarche', 6: 'demarche',
        7: 'acteurs',
        8: 'pilotage', 9: 'pilotage',
        10: 'competences', 11: 'competences',
        12: 'equipe',
    },
    'evo_orga.html': {
        # Réécrit en Besombes strict (11 chapitres)
        1: 'intro', 2: 'intro',
        3: 'dppo',
        4: 'intro', 5: 'intro', 6: 'intro', 7: 'intro',
        8: 'processus',
        9: 'performance', 10: 'performance',
        11: 'pilotage',
    },
    'gouv.html': {
        1: 'gouvernance', 2: 'gouvernance', 3: 'gouvernance', 4: 'gouvernance',
        5: 'gouvernance', 6: 'gouvernance', 7: 'gouvernance',
        8: 'securite', 9: 'securite',
        10: 'transfo_digital',
    },
    'inge_fi.html': {
        1: 'marches_fi', 2: 'marches_fi', 3: 'marches_fi',
        4: 'cout_capital',
        5: 'derives', 6: 'derives',
        7: 'esg',
    },
    'rse.html': {
        1: 'fondamentaux', 2: 'fondamentaux',
        3: 'csrd_esrs', 4: 'csrd_esrs',
        5: 'materialite',
        6: 'outils_metier', 7: 'outils_metier',
        8: 'materialite',
        9: 'outils_metier',
    },
    'strat.html': {
        1: 'business_models', 2: 'business_models', 3: 'business_models',
        4: 'business_models', 5: 'business_models',
        6: 'plateformes', 7: 'plateformes', 8: 'plateformes',
        9: 'concurrentielle', 10: 'concurrentielle', 11: 'concurrentielle',
        12: 'concurrentielle', 13: 'concurrentielle', 14: 'concurrentielle',
        15: 'concurrentielle', 16: 'concurrentielle',
        17: 'corporate', 18: 'corporate', 19: 'corporate',
        20: 'corporate', 21: 'corporate', 22: 'corporate',
    },
}


def tag(html_file: str, mapping: dict[int, str]) -> None:
    path = ROOT / html_file
    text = path.read_text()
    # Match each `<div class="course-chapter">` opening tag (no existing attrs).
    pattern = re.compile(r'<div class="course-chapter">')
    count = [0]

    def replace(_match):
        count[0] += 1
        idx = count[0]
        theme = mapping.get(idx)
        if theme is None:
            return _match.group(0)
        return f'<div class="course-chapter" data-theme="{theme}" data-chap-idx="{idx}" id="chap-{idx}">'

    new_text, n = pattern.subn(replace, text)
    if n != len(mapping):
        raise SystemExit(f'{html_file}: expected {len(mapping)} chapters, replaced {n}')
    path.write_text(new_text)
    print(f'{html_file}: tagged {n} chapters')


if __name__ == '__main__':
    for f, m in MAPPINGS.items():
        tag(f, m)
