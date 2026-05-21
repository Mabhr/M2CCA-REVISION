"""Normalise toutes les questions quiz à un seul schéma : q/o/c/e/theme/src.

Convertit choices→o, answer→c, expl→e. Supprime id (non utilisé par le renderer).
S'applique sur tous les fichiers data/*.json par sécurité.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / 'data'

COURSES = ['conduite_chgt', 'evo_orga', 'gouv', 'inge_fi', 'rse', 'strat']


def normalize_quiz(q):
    if 'choices' in q:
        q['o'] = q.pop('choices')
    if 'answer' in q:
        q['c'] = q.pop('answer')
    if 'expl' in q:
        q['e'] = q.pop('expl')
    # id pas utilisé par le renderer (les questions sont indexées par position)
    if 'id' in q:
        del q['id']
    return q


for course in COURSES:
    path = ROOT / f'{course}.json'
    if not path.exists():
        continue
    d = json.loads(path.read_text())
    qs = d.get('quizQuestions', [])
    converted = 0
    for q in qs:
        if 'choices' in q or 'answer' in q or 'expl' in q or 'id' in q:
            normalize_quiz(q)
            converted += 1
    if converted:
        path.write_text(json.dumps(d, ensure_ascii=False, indent=2))
        print(f'{course}: {converted}/{len(qs)} questions normalisées (choices→o, answer→c, expl→e)')
    else:
        print(f'{course}: déjà normalisé')
