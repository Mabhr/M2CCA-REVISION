"""Nettoie inge_fi des concepts non sourcés dans le cours Robin :
  - Chap 7 (Évaluation d'entreprise : DCF, ANR, comparables, M&A) : SUPPRIMER ENTIER
  - Chap 8 (Politique financière : Modigliani-Miller, pecking order, effet levier, rachat actions) : SUPPRIMER ENTIER
  - Flashcards / quiz : retirer les items hors-Robin (évaluation, M&A, options avancées, capital-invest., réglementaires)
  - Renuméroter chap 9 → chap 7 pour combler le trou
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / 'inge_fi.html'
JSON = ROOT / 'data' / 'inge_fi.json'

# Indices des flashcards/quiz à supprimer (déterminés par audit)
FC_TO_REMOVE = [21, 22, 23, 24, 32, 36, 37]
QUIZ_TO_REMOVE = [8, 9, 24, 25, 26, 27, 28, 31, 34, 35, 36, 37, 40, 41, 42, 44, 52, 57]


def clean_html():
    text = HTML.read_text()
    # Trouve et supprime le bloc CH 7 entier
    # Pattern : <!-- ══ CH 7 ... --> ... <!-- ══ CH 8 ... -->
    # On supprime CH7 + CH8 en une seule passe
    pattern_ch7_ch8 = re.compile(
        r'\s*<!-- ══ CH 7[^\n]*?══ -->\s*<div class="course-chapter"[^>]*data-chap-idx="7"[\s\S]*?<!-- ══ CH 9',
        re.MULTILINE
    )
    m = pattern_ch7_ch8.search(text)
    if not m:
        # Fallback : retirer en cherchant les divs avec data-chap-idx="7" et "8"
        # Supprime de "<!-- ══ CH 7" jusqu'à "<!-- ══ CH 9"
        idx7 = text.find('<!-- ══ CH 7')
        idx9 = text.find('<!-- ══ CH 9')
        if idx7 == -1 or idx9 == -1:
            raise SystemExit('Marqueurs CH 7 / CH 9 non trouvés')
        # On garde tout avant CH7 + on insère un peu d'espace + CH9 (renuméroté en CH7)
        text = text[:idx7] + '\n\n    ' + text[idx9:]
    else:
        text = text[:m.start()] + '\n\n    <!-- ══ CH 9' + text[m.end():]
    # Renumérote l'ancien chap 9 → chap 7
    text = text.replace(
        '<!-- ══ CH 9 : Critères ESG & finance durable ══ -->',
        '<!-- ══ CH 7 : Critères ESG & finance durable ══ -->',
        1
    )
    text = text.replace(
        '<div class="course-chapter" data-theme="esg" data-chap-idx="9" id="chap-9">',
        '<div class="course-chapter" data-theme="esg" data-chap-idx="7" id="chap-7">',
        1
    )
    text = text.replace(
        '<h2 class="chapter-title">9 · Finance durable',
        '<h2 class="chapter-title">7 · Finance durable',
        1
    )
    HTML.write_text(text)
    print('✓ inge_fi.html : chap 7 (Évaluation) et chap 8 (Politique financière) supprimés ; ancien chap 9 renuméroté en chap 7')


def clean_json():
    d = json.loads(JSON.read_text())
    fcs = d.get('flashcards', [])
    qs = d.get('quizQuestions', [])
    new_fcs = [fc for i, fc in enumerate(fcs) if i not in FC_TO_REMOVE]
    new_qs = [q for i, q in enumerate(qs) if i not in QUIZ_TO_REMOVE]
    d['flashcards'] = new_fcs
    d['quizQuestions'] = new_qs
    # Retire le thème "evaluation_ma" qui n'a plus de contenu
    d['themes'] = [t for t in d.get('themes', []) if t.get('id') != 'evaluation_ma']
    # Met aussi à jour la checklist si elle contient des items évaluation/M&A
    cl = d.get('checklistItems', [])
    REMOVE_LABELS = ['évaluation d\'entreprise', 'fusion-acquisition', 'politique de dividende',
                     'rachat d\'actions']
    new_cl = [c for c in cl if not any(k in c.get('label', '').lower() for k in REMOVE_LABELS)]
    d['checklistItems'] = new_cl
    JSON.write_text(json.dumps(d, ensure_ascii=False, indent=2))
    print(f'✓ data/inge_fi.json :')
    print(f'   themes        : {len(d["themes"])} (evaluation_ma retiré)')
    print(f'   flashcards    : {len(fcs)} → {len(new_fcs)} (-{len(fcs)-len(new_fcs)})')
    print(f'   quizQuestions : {len(qs)} → {len(new_qs)} (-{len(qs)-len(new_qs)})')
    print(f'   checklistItems: {len(cl)} → {len(new_cl)} (-{len(cl)-len(new_cl)})')


if __name__ == '__main__':
    clean_html()
    clean_json()
