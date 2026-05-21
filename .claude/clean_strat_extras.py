"""Nettoie strat des concepts non sourcés dans les PDFs Tellier :
  - Zucker 1986 (3 modes de confiance) — totalement inventé
  - Freeman 1984 cité nommément — remplacer par "vision parties prenantes"
  - VRIO / RBV / PESTEL / Schumpeter — vocabulaire académique ajouté
  - Mestic vs Tinder — exemple inventé
  - Loi PACTE / société à mission — hors PDFs

Stratégie :
  - Flashcards / quiz / checklist : retirer les items qui mentionnent
    explicitement ces concepts comme cours du prof
  - HTML : retirer le 4e exemple Mestic dans le tableau Cusumano chap 8
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / 'strat.html'
JSON = ROOT / 'data' / 'strat.json'

# Items à supprimer (par index dans le tableau)
FC_TO_REMOVE = [27, 40, 46, 49, 51, 52, 55]
QUIZ_TO_REMOVE = [41, 45, 54, 61, 66, 71, 72]
CHECKLIST_IDS_TO_REMOVE = ['s22']


def clean_json():
    d = json.loads(JSON.read_text())
    fcs = d.get('flashcards', [])
    qs = d.get('quizQuestions', [])
    cl = d.get('checklistItems', [])
    new_fcs = [fc for i, fc in enumerate(fcs) if i not in FC_TO_REMOVE]
    new_qs = [q for i, q in enumerate(qs) if i not in QUIZ_TO_REMOVE]
    new_cl = [c for c in cl if c.get('id') not in CHECKLIST_IDS_TO_REMOVE]
    d['flashcards'] = new_fcs
    d['quizQuestions'] = new_qs
    d['checklistItems'] = new_cl
    JSON.write_text(json.dumps(d, ensure_ascii=False, indent=2))
    print(f'✓ strat.json :')
    print(f'   flashcards  : {len(fcs)} → {len(new_fcs)} (-{len(fcs)-len(new_fcs)})')
    print(f'   quiz        : {len(qs)} → {len(new_qs)} (-{len(qs)-len(new_qs)})')
    print(f'   checklist   : {len(cl)} → {len(new_cl)} (-{len(cl)-len(new_cl)})')


def clean_html():
    text = HTML.read_text()
    # Retire la ligne "Mestic / Tinder" du tableau d'erreur d'orgueil dans chap 8
    old_row = '      <tr><td>Mestic</td><td>Tinder</td><td>Rencontre basée sur des valeurs communes</td></tr>\n'
    if old_row in text:
        text = text.replace(old_row, '', 1)
        print('✓ strat.html : ligne Mestic/Tinder retirée du chap 8')
    else:
        print('  (ligne Mestic/Tinder déjà absente)')
    HTML.write_text(text)


if __name__ == '__main__':
    clean_json()
    clean_html()
