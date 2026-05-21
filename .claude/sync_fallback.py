"""Synchronise la constante FALLBACK de chaque cours HTML avec son data/X.json.

Le FALLBACK sert de source de données en mode file:// (quand fetch est bloqué).
Sans `annales` et `themes` dedans, le filtre par axe et l'onglet Annales sont vides.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAIRS = [
    ('conduite_chgt.html', 'data/conduite_chgt.json'),
    ('evo_orga.html', 'data/evo_orga.json'),
    ('gouv.html', 'data/gouv.json'),
    ('inge_fi.html', 'data/inge_fi.json'),
    ('rse.html', 'data/rse.json'),
    ('strat.html', 'data/strat.json'),
]


def sync(html_file: str, json_file: str) -> None:
    html_path = ROOT / html_file
    json_path = ROOT / json_file
    html = html_path.read_text()
    payload = json.loads(json_path.read_text())
    # Sérialise joliment pour lisibilité (2-space indent), encadré par 'const FALLBACK = ' et ';'
    new_block = 'const FALLBACK = ' + json.dumps(payload, ensure_ascii=False, indent=2) + ';'

    # Cherche le const FALLBACK = { ... }; existant et le remplace.
    # Le bloc actuel peut s'étendre sur des centaines de lignes — on capture jusqu'au '};' final
    # en s'appuyant sur l'équilibrage des accolades.
    marker = 'const FALLBACK = {'
    start = html.find(marker)
    if start == -1:
        raise SystemExit(f'{html_file}: FALLBACK non trouvé')
    # Équilibrer { ... } à partir de start
    depth = 0
    i = start + len('const FALLBACK = ')
    end = -1
    while i < len(html):
        ch = html[i]
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                end = i + 1
                break
        i += 1
    if end == -1:
        raise SystemExit(f'{html_file}: accolade fermante introuvable')
    # Le ';' suit normalement immédiatement
    if html[end:end + 1] == ';':
        end += 1
    elif html[end:end + 2] == ' ;':
        end += 2

    new_html = html[:start] + new_block + html[end:]
    html_path.write_text(new_html)
    annales_n = len(payload.get('annales', []))
    themes_n = len(payload.get('themes', []))
    fc_n = len(payload.get('flashcards', []))
    quiz_n = len(payload.get('quizQuestions', []) or payload.get('quiz', []))
    print(f'{html_file}: FALLBACK resynchronisé → annales={annales_n}, themes={themes_n}, flashcards={fc_n}, quiz={quiz_n}')


if __name__ == '__main__':
    for h, j in PAIRS:
        sync(h, j)
