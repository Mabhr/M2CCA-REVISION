"""Génère l'index de recherche embarqué pour le mode file://.

À relancer après modification du contenu des cours :
    python3 .claude/build_search_index.py

Le script écrit l'index dans index.html entre les marqueurs :
    /* SEARCH_INDEX_START */ ... /* SEARCH_INDEX_END */
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COURSES_JSON = ROOT / 'data' / 'courses.json'
INDEX_HTML = ROOT / 'index.html'

START = '/* SEARCH_INDEX_START */'
END = '/* SEARCH_INDEX_END */'


def extract_chapters(html_text: str) -> list[dict]:
    """Extrait les .course-chapter du HTML brut en équilibrant les <div>."""
    chapters = []
    open_re = re.compile(
        r'<div class="course-chapter" data-theme="([^"]+)" data-chap-idx="(\d+)" id="chap-\d+">'
    )
    for m in open_re.finditer(html_text):
        start = m.end()
        depth = 1
        i = start
        while depth > 0 and i < len(html_text):
            no = html_text.find('<div', i)
            nc = html_text.find('</div>', i)
            if nc == -1:
                break
            if no != -1 and no < nc:
                depth += 1
                i = no + 4
            else:
                depth -= 1
                i = nc + 6
        inner = html_text[start:i - 6]
        # Récupérer le titre H2
        h2 = re.search(r'<h2[^>]*>([\s\S]*?)</h2>', inner)
        chap_title = re.sub(r'<[^>]+>', '', h2.group(1)).strip() if h2 else f'Chapitre {m.group(2)}'
        chap_title = re.sub(r'\s+', ' ', chap_title)
        # Texte propre (tags retirés)
        text = re.sub(r'<[^>]+>', ' ', inner)
        text = re.sub(r'\s+', ' ', text).strip()
        chapters.append({
            'idx': int(m.group(2)),
            'theme': m.group(1),
            'title': chap_title,
            'text': text,
        })
    return chapters


def main() -> None:
    courses = json.loads(COURSES_JSON.read_text())['courses']
    out = []
    for course_id, c in courses.items():
        if not (c.get('hasContent') and c.get('url')):
            continue
        html_path = ROOT / c['url']
        if not html_path.exists():
            print(f'! {course_id}: {html_path} introuvable')
            continue
        html_text = html_path.read_text()
        # Données du cours : thèmes, flashcards, quiz
        json_path = ROOT / 'data' / (Path(c['url']).stem + '.json')
        course_data = json.loads(json_path.read_text()) if json_path.exists() else {}
        themes_arr = course_data.get('themes', [])
        theme_labels = {t['id']: f"{t.get('icon', '')} {t['label']}".strip() for t in themes_arr}
        meta = {
            'cId': course_id,
            'cT': c.get('title', course_id),
            'cI': c.get('icon', '📘'),
            'cU': c.get('url'),
        }

        chaps = extract_chapters(html_text)
        for chap in chaps:
            out.append({
                **meta, 'k': 'cours', 'i': chap['idx'], 't': chap['title'],
                'th': chap['theme'], 'thL': theme_labels.get(chap['theme'], chap['theme']),
                'x': chap['text'],
            })

        flashcards = course_data.get('flashcards', [])
        for fc in flashcards:
            q = (fc.get('q') or '').strip()
            a = (fc.get('a') or '').strip()
            th = fc.get('theme', '')
            out.append({
                **meta, 'k': 'flash', 'i': 0, 't': q,
                'th': th, 'thL': theme_labels.get(th, ''),
                'x': re.sub(r'\s+', ' ', f'{q} — {a}').strip(),
            })

        quizz = course_data.get('quizQuestions', [])
        for qz in quizz:
            q = (qz.get('q') or '').strip()
            th = qz.get('theme', '')
            extra = ''
            if qz.get('type') == 'tf':
                extra = ' ' + ' '.join((af.get('t') or '') for af in qz.get('aff', []))
            out.append({
                **meta, 'k': 'quiz', 'i': 0, 't': q,
                'th': th, 'thL': theme_labels.get(th, ''),
                'x': re.sub(r'\s+', ' ', q + extra).strip(),
            })

        print(f'{course_id}: {len(chaps)} chapitres, {len(flashcards)} flashcards, {len(quizz)} quiz')

    # Sérialisation compacte
    payload = json.dumps(out, ensure_ascii=False, separators=(',', ':'))
    block = f'{START}\nconst GS_BUILTIN_INDEX = {payload};\n{END}'

    html = INDEX_HTML.read_text()
    if START in html and END in html:
        new = re.sub(
            re.escape(START) + r'[\s\S]*?' + re.escape(END),
            lambda _: block,
            html,
            count=1,
        )
    else:
        # Insère avant la fonction buildGlobalSearchIndex
        marker = 'async function buildGlobalSearchIndex()'
        if marker not in html:
            raise SystemExit('Marqueur d\'insertion introuvable dans index.html')
        new = html.replace(marker, block + '\n\n' + marker, 1)
    INDEX_HTML.write_text(new)
    total_chars = sum(len(c['x']) for c in out)
    print(f'\n✓ Index embarqué dans index.html : {len(out)} entrées, {total_chars:,} caractères ({len(payload):,} octets JSON)')


if __name__ == '__main__':
    main()
