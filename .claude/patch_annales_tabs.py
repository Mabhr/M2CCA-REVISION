"""Ajoute le support multi-annale (onglets en haut) dans le renderer getAnnalesHTML
des 6 HTML, sans toucher au reste du rendu d'une annale.

Changements :
  - `return list.map((a, aIdx) => {` → `const renderOne = (a, aIdx) => {`
  - `}).join('');\n}` → `};\n[tabs logic + return]\n}`
  - Ajoute la fonction switchAnnale() juste avant getAnnalesHTML.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = ['conduite_chgt.html', 'evo_orga.html', 'gouv.html', 'inge_fi.html', 'rse.html', 'strat.html']

OLD_MAP_OPEN = '  return list.map((a, aIdx) => {'
NEW_MAP_OPEN = '  const renderOne = (a, aIdx) => {'

OLD_MAP_CLOSE = '''      ${tipsHTML}
    </div>`;
  }).join(\'\');
}
'''

NEW_MAP_CLOSE = '''      ${tipsHTML}
    </div>`;
  };
  if (list.length === 1) return renderOne(list[0], 0);
  // Multi-annales : onglets en haut + un seul corps visible à la fois
  const tabsHTML = list.map((a, i) => `
    <button class="annale-tab${i === 0 ? ' active' : ''}" type="button" onclick="switchAnnale(${i}, this)">
      <span class="annale-tab-year">${escAnnale(a.year || '')}</span>
      ${a.name ? `<span class="annale-tab-name">${escAnnale(a.name)}</span>` : ''}
    </button>`).join('');
  return `
    <div class="annales-tabs">${tabsHTML}</div>
    <div class="annales-bodies">
      ${list.map((a, i) => `<div class="annale-body-wrap" data-annale-idx="${i}" style="${i === 0 ? '' : 'display:none'}">${renderOne(a, i)}</div>`).join('')}
    </div>`;
}
'''

SWITCH_FN = '''function switchAnnale(idx, btn) {
  document.querySelectorAll('.annale-body-wrap').forEach(el => {
    el.style.display = parseInt(el.dataset.annaleIdx, 10) === idx ? '' : 'none';
  });
  document.querySelectorAll('.annale-tab').forEach(b => b.classList.remove('active'));
  if (btn) btn.classList.add('active');
  // Collapse toutes les corrections de l'annale qu'on quitte pour repartir propre
  document.querySelectorAll('.annale-correction').forEach(el => { el.style.display = 'none'; });
  document.querySelectorAll('.annale-show-corr').forEach(b => { b.textContent = '▸ Afficher la correction'; b.classList.remove('open'); });
}

'''


def patch(html_file: str) -> None:
    path = ROOT / html_file
    text = path.read_text()
    if 'function switchAnnale' in text:
        print(f'{html_file}: déjà patché (skip)')
        return
    if OLD_MAP_OPEN not in text:
        raise SystemExit(f'{html_file}: OLD_MAP_OPEN non trouvé')
    if OLD_MAP_CLOSE not in text:
        raise SystemExit(f'{html_file}: OLD_MAP_CLOSE non trouvé')
    new_text = text.replace(OLD_MAP_OPEN, NEW_MAP_OPEN, 1)
    new_text = new_text.replace(OLD_MAP_CLOSE, NEW_MAP_CLOSE, 1)
    # Injecte switchAnnale juste avant la déclaration de getAnnalesHTML
    new_text = new_text.replace('function getAnnalesHTML() {', SWITCH_FN + 'function getAnnalesHTML() {', 1)
    path.write_text(new_text)
    print(f'{html_file}: multi-annale tabs activé')


if __name__ == '__main__':
    for f in FILES:
        patch(f)
