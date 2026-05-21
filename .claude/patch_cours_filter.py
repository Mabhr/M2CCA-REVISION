"""Patch each course HTML to add:
- coursTheme variable + setCoursTheme()
- themeSelectorHTML extended to handle 'cours' scope
- renderTab('cours') now wraps the cours content and applies the filter
- Deep-link hash handler that opens at the right chapter & highlights a word
- Reusable applyCoursFilter() helper
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = ['conduite_chgt.html', 'evo_orga.html', 'gouv.html', 'inge_fi.html', 'rse.html', 'strat.html']

OLD_VAR = "let fcTheme = 'all', quizTheme = 'all';"
NEW_VAR = "let fcTheme = 'all', quizTheme = 'all', coursTheme = 'all';"

OLD_SETTERS = "function setFcTheme(id) { fcTheme = id; switchTab('flash'); }\nfunction setQuizTheme(id) { quizTheme = id; switchTab('quiz'); }"
NEW_SETTERS = """function setFcTheme(id) { fcTheme = id; switchTab('flash'); }
function setQuizTheme(id) { quizTheme = id; switchTab('quiz'); }
function setCoursTheme(id) { coursTheme = id; applyCoursFilter(); renderCoursPills(); }
function applyCoursFilter() {
  document.querySelectorAll('.course-chapter').forEach(el => {
    const matches = coursTheme === 'all' || el.dataset.theme === coursTheme;
    el.style.display = matches ? '' : 'none';
  });
  const empty = document.getElementById('coursEmpty');
  if (empty) {
    const visible = Array.from(document.querySelectorAll('.course-chapter')).some(el => el.style.display !== 'none');
    empty.style.display = visible ? 'none' : 'block';
  }
}
function renderCoursPills() {
  const host = document.getElementById('coursThemeSelector');
  if (host) host.outerHTML = themeSelectorHTML('cours');
}"""

OLD_TS = """function themeSelectorHTML(scope) {
  const current = scope === 'flash' ? fcTheme : quizTheme;
  const fn = scope === 'flash' ? 'setFcTheme' : 'setQuizTheme';
  const themes = DATA.themes || [];
  if (!themes.length) return '';
  const counts = {};
  if (scope === 'flash') {
    counts.all = DATA.flashcards.length;
    themes.forEach(t => counts[t.id] = DATA.flashcards.filter(fc => fc.theme === t.id).length);
  } else {
    counts.all = DATA.quizQuestions.length;
    themes.forEach(t => counts[t.id] = DATA.quizQuestions.filter(q => q.theme === t.id).length);
  }
  const pill = (id, label, count) => `<button class="theme-pill${current === id ? ' active' : ''}" onclick="${fn}('${id}')" title="${label}">${label} <span class="theme-count">${count}</span></button>`;
  return `<div class="theme-selector">
    <div class="theme-label">Filtre par thème</div>
    <div class="theme-pills">
      ${pill('all', '🔍 Tous', counts.all)}
      ${themes.map(t => pill(t.id, t.icon + ' ' + t.label, counts[t.id] || 0)).join('')}
    </div>
  </div>`;
}"""

NEW_TS = """function themeSelectorHTML(scope) {
  const current = scope === 'flash' ? fcTheme : (scope === 'quiz' ? quizTheme : coursTheme);
  const fn = scope === 'flash' ? 'setFcTheme' : (scope === 'quiz' ? 'setQuizTheme' : 'setCoursTheme');
  const themes = DATA.themes || [];
  if (!themes.length) return '';
  const counts = {};
  if (scope === 'flash') {
    counts.all = DATA.flashcards.length;
    themes.forEach(t => counts[t.id] = DATA.flashcards.filter(fc => fc.theme === t.id).length);
  } else if (scope === 'quiz') {
    counts.all = DATA.quizQuestions.length;
    themes.forEach(t => counts[t.id] = DATA.quizQuestions.filter(q => q.theme === t.id).length);
  } else {
    // cours : on compte les .course-chapter DOM si déjà présents, sinon fallback à 0
    const chaps = document.querySelectorAll('.course-chapter');
    counts.all = chaps.length;
    themes.forEach(t => counts[t.id] = Array.from(chaps).filter(c => c.dataset.theme === t.id).length);
  }
  const pill = (id, label, count) => `<button class="theme-pill${current === id ? ' active' : ''}" onclick="${fn}('${id}')" title="${label}">${label} <span class="theme-count">${count}</span></button>`;
  return `<div class="theme-selector" id="coursThemeSelector-${scope}">
    <div class="theme-label">Filtre par axe</div>
    <div class="theme-pills">
      ${pill('all', '🔍 Tous', counts.all)}
      ${themes.map(t => pill(t.id, t.icon + ' ' + t.label, counts[t.id] || 0)).join('')}
    </div>
  </div>`;
}"""

OLD_RENDER_COURS = "else if (id === 'cours') { root.innerHTML = header + `<div class=\"fade-up\">${getCoursHTML()}</div>`; setTimeout(() => buildScrollSpy('.main', '.course-chapter h2'), 100); }"
NEW_RENDER_COURS = """else if (id === 'cours') {
    root.innerHTML = header + `<div class="fade-up"><div id="coursThemeSelectorWrap"></div>${getCoursHTML()}<div id="coursEmpty" class="cours-empty" style="display:none">Aucun chapitre dans cet axe pour ce cours.</div></div>`;
    document.getElementById('coursThemeSelectorWrap').innerHTML = themeSelectorHTML('cours');
    applyCoursFilter();
    setTimeout(() => buildScrollSpy('.main', '.course-chapter:not([style*=\"display: none\"]) h2'), 100);
    if (window._pendingCoursJump) { window._pendingCoursJump(); window._pendingCoursJump = null; }
  }"""

DEEPLINK_INIT = """
/* ═══════ DEEP LINK (hash : #cours=N&q=word ou #chap-N) ═══════ */
function parseDeepLink() {
  const h = window.location.hash || '';
  if (!h) return null;
  const out = {};
  // Format 1 : #chap-3
  let m = h.match(/^#chap-(\\d+)$/);
  if (m) { out.chap = parseInt(m[1], 10); return out; }
  // Format 2 : #cours=3&q=mot&theme=xxx
  m = h.match(/^#([^?]+)/);
  if (m) {
    const params = new URLSearchParams(h.slice(1));
    if (params.has('cours')) out.chap = parseInt(params.get('cours'), 10);
    if (params.has('q')) out.q = params.get('q');
    if (params.has('theme')) out.theme = params.get('theme');
    if (params.has('tab')) out.tab = params.get('tab');
  }
  return Object.keys(out).length ? out : null;
}
function highlightInChapter(chapEl, word) {
  if (!chapEl || !word) return;
  const re = new RegExp('(' + word.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&') + ')', 'gi');
  const walker = document.createTreeWalker(chapEl, NodeFilter.SHOW_TEXT, null);
  const nodes = [];
  while (walker.nextNode()) nodes.push(walker.currentNode);
  nodes.forEach(n => {
    if (!re.test(n.nodeValue)) return;
    re.lastIndex = 0;
    const span = document.createElement('span');
    span.innerHTML = n.nodeValue.replace(re, '<mark class="search-hit">$1</mark>');
    n.parentNode.replaceChild(span, n);
  });
}
function applyDeepLink() {
  const dl = parseDeepLink();
  if (!dl) return;
  if (dl.theme) coursTheme = dl.theme;
  // S'assurer qu'on est sur l'onglet cours
  const targetTab = dl.tab || 'cours';
  const jumper = () => {
    const el = dl.chap ? document.getElementById('chap-' + dl.chap) : null;
    if (el) {
      // Si le chapitre est masqué par le filtre, réinitialise à 'all'
      if (el.style.display === 'none') { coursTheme = 'all'; applyCoursFilter(); renderCoursPills(); }
      el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      el.classList.add('chap-target-flash');
      setTimeout(() => el.classList.remove('chap-target-flash'), 2400);
      if (dl.q) highlightInChapter(el, dl.q);
    }
  };
  if (currentTab !== targetTab) {
    window._pendingCoursJump = jumper;
    switchTab(targetTab);
  } else {
    setTimeout(jumper, 80);
  }
}
window.addEventListener('hashchange', applyDeepLink);
"""

def patch(html_file: str) -> None:
    path = ROOT / html_file
    text = path.read_text()
    original = text

    if OLD_VAR not in text:
        raise SystemExit(f'{html_file}: OLD_VAR not found')
    text = text.replace(OLD_VAR, NEW_VAR, 1)

    if OLD_SETTERS not in text:
        raise SystemExit(f'{html_file}: OLD_SETTERS not found')
    text = text.replace(OLD_SETTERS, NEW_SETTERS, 1)

    if OLD_TS not in text:
        raise SystemExit(f'{html_file}: OLD_TS not found')
    text = text.replace(OLD_TS, NEW_TS, 1)

    if OLD_RENDER_COURS not in text:
        raise SystemExit(f'{html_file}: OLD_RENDER_COURS not found')
    text = text.replace(OLD_RENDER_COURS, NEW_RENDER_COURS, 1)

    # Inject deep-link helper once, before the closing </script> of the page logic.
    # Find the last </script> tag.
    if 'function parseDeepLink' not in text:
        # Inject inside the existing script. Place right after the renderTab function definition.
        marker = '/* ═══════ CHECKLIST ═══════ */'
        if marker not in text:
            raise SystemExit(f'{html_file}: CHECKLIST marker not found')
        text = text.replace(marker, DEEPLINK_INIT + '\n' + marker, 1)

    # Make sure applyDeepLink is called once the data is loaded.
    # Each page has an init flow — we hook it by listening to a delayed call.
    # The simplest: append a window.addEventListener('load', applyDeepLink) at end of script.
    # Find `</script>` after the JS module — the last one in file.
    if '/* DEEPLINK_BOOTSTRAP */' not in text:
        last_close = text.rfind('</script>')
        if last_close == -1:
            raise SystemExit(f'{html_file}: no </script>')
        bootstrap = "\n/* DEEPLINK_BOOTSTRAP */\nwindow.addEventListener('load', () => setTimeout(applyDeepLink, 200));\n"
        text = text[:last_close] + bootstrap + text[last_close:]

    if text == original:
        print(f'{html_file}: NO CHANGE')
    else:
        path.write_text(text)
        print(f'{html_file}: patched')


if __name__ == '__main__':
    for f in FILES:
        patch(f)
