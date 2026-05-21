"""Remplace getAnnalesHTML dans les 6 HTML par la version qui gère :
   - nouveau schéma : a.dossiers[].items[{q,correction}] avec bouton 'Afficher la correction' par question
   - ancien schéma : conservé en fallback (subject + exercises + bestCopy + corrige + tips)
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

OLD = '''function getAnnalesHTML() {
  const list = (DATA.annales || []);
  if (!list.length) return `<div class="annales-empty"><p>Aucune annale disponible pour ce cours.</p></div>`;
  return list.map((a, idx) => {
    const exHTML = (a.exercises || []).map(e => `
      <div class="annale-exercise">
        <div class="annale-exercise-label">${e.label}</div>
        <div class="annale-exercise-content">${(e.content||'').replace(/\\n/g,'<br>')}</div>
      </div>
    `).join('');

    const bc = a.bestCopy;
    let bestCopyHTML = '';
    if (bc) {
      const planHTML = (bc.plan||[]).map(line => {
        const t = (line||'').trim();
        if (!t) return '<div class="annale-plan-spacer"></div>';
        if (/^(I+\\.|[0-9]+\\.|Introduction|Conclusion|Exercice|Q[0-9]+|•)/.test(t)) {
          return `<div class="annale-plan-line annale-plan-main">${t}</div>`;
        }
        return `<div class="annale-plan-line">${t}</div>`;
      }).join('');
      const conceptsHTML = (bc.keyConcepts||[]).map(c => `<span class="annale-concept">${c}</span>`).join('');
      const qcmHTML = (bc.qcmAnswers||[]).length
        ? `<div class="annale-block annale-qcm"><div class="annale-block-title">QCM — réponses correctes</div>${bc.qcmAnswers.map(q=>`<div class="annale-qcm-line">${q}</div>`).join('')}</div>`
        : '';
      bestCopyHTML = `
      <div class="annale-bestcopy">
        <div class="annale-bestcopy-head">
          <span class="annale-grade">📝 Note : ${bc.grade}</span>
          ${bc.subjectChosen ? `<span class="annale-chosen">Sujet traité : ${bc.subjectChosen}</span>` : ''}
        </div>
        ${qcmHTML}
        <div class="annale-block">
          <div class="annale-block-title">Plan-type / structure de la copie</div>
          <div class="annale-plan">${planHTML}</div>
        </div>
        ${(bc.keyConcepts||[]).length ? `
        <div class="annale-block">
          <div class="annale-block-title">Mots-clés &amp; concepts mobilisés</div>
          <div class="annale-concepts">${conceptsHTML}</div>
        </div>` : ''}
        ${bc.correctorNotes ? `<div class="annale-corrector"><strong>Annotations du correcteur :</strong> ${bc.correctorNotes}</div>` : ''}
      </div>`;
    }

    let corrigeHTML = '';
    if (a.corrige && a.corrige.available) {
      const hl = (a.corrige.highlights||[]).map(h => `<li>${h}</li>`).join('');
      corrigeHTML = `
      <div class="annale-corrige">
        <div class="annale-block-title">Corrigé officiel — points clés</div>
        ${a.corrige.summary ? `<p class="annale-corrige-summary">${a.corrige.summary}</p>` : ''}
        <ul>${hl}</ul>
      </div>`;
    }

    const tipsHTML = (a.tips||[]).length ? `
      <div class="annale-tips">
        <div class="annale-block-title">💡 Conseils méthodologiques</div>
        <ul>${a.tips.map(t => `<li>${t}</li>`).join('')}</ul>
      </div>` : '';

    const meta = [a.duration ? `⏱ ${a.duration}` : '', a.format || '', a.professor ? `👤 ${a.professor}` : '']
      .filter(Boolean).join(' · ');

    return `
    <div class="annale-card">
      <div class="annale-head">
        <div class="annale-head-row">
          <div class="annale-year">${a.year || ''}</div>
          <div class="annale-title">${a.name || 'Annale'}</div>
        </div>
        ${meta ? `<div class="annale-meta">${meta}</div>` : ''}
      </div>
      <div class="annale-subject">
        <div class="annale-block-title">📋 Sujet</div>
        <div class="annale-subject-content">${(a.subject||'').replace(/\\n/g,'<br>')}</div>
      </div>
      ${exHTML ? `<div class="annale-exercises">${exHTML}</div>` : ''}
      ${bestCopyHTML}
      ${corrigeHTML}
      ${tipsHTML}
    </div>`;
  }).join('');
}
'''

NEW = '''function escAnnale(s) {
  return String(s == null ? '' : s).replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
}
function toggleAnnaleCorrection(id, btn) {
  const el = document.getElementById(id);
  if (!el) return;
  const isHidden = el.style.display === 'none' || !el.style.display;
  el.style.display = isHidden ? 'block' : 'none';
  btn.textContent = isHidden ? '▾ Masquer la correction' : '▸ Afficher la correction';
  btn.classList.toggle('open', isHidden);
}
function expandAllAnnales(scope) {
  document.querySelectorAll(scope + ' .annale-correction').forEach(el => { el.style.display = 'block'; });
  document.querySelectorAll(scope + ' .annale-show-corr').forEach(btn => { btn.textContent = '▾ Masquer la correction'; btn.classList.add('open'); });
}
function collapseAllAnnales(scope) {
  document.querySelectorAll(scope + ' .annale-correction').forEach(el => { el.style.display = 'none'; });
  document.querySelectorAll(scope + ' .annale-show-corr').forEach(btn => { btn.textContent = '▸ Afficher la correction'; btn.classList.remove('open'); });
}

function getAnnalesHTML() {
  const list = (DATA.annales || []);
  if (!list.length) return `<div class="annales-empty"><p>Aucune annale disponible pour ce cours.</p></div>`;
  return list.map((a, aIdx) => {
    const meta = [a.duration ? `⏱ ${a.duration}` : '', a.format || '', a.professor ? `👤 ${a.professor}` : '']
      .filter(Boolean).join(' · ');
    const head = `
      <div class="annale-head">
        <div class="annale-head-row">
          <div class="annale-year">${escAnnale(a.year || '')}</div>
          <div class="annale-title">${escAnnale(a.name || 'Annale')}</div>
        </div>
        ${meta ? `<div class="annale-meta">${escAnnale(meta)}</div>` : ''}
      </div>`;
    const tipsHTML = (a.tips||[]).length ? `
      <div class="annale-tips">
        <div class="annale-block-title">💡 Conseils méthodologiques</div>
        <ul>${a.tips.map(t => `<li>${escAnnale(t)}</li>`).join('')}</ul>
      </div>` : '';

    // ── NOUVEAU SCHÉMA : dossiers[].items[{q,correction}] avec bouton par sous-question ──
    if (Array.isArray(a.dossiers) && a.dossiers.length) {
      const cardId = `annale-card-${aIdx}`;
      const dossiersHTML = a.dossiers.map((ds, dIdx) => {
        const itemsHTML = (ds.items || []).map((it, iIdx) => {
          const corrId = `corr-${aIdx}-${dIdx}-${iIdx}`;
          return `
          <div class="annale-question">
            <div class="annale-q-text">${escAnnale(it.q || '')}</div>
            ${it.correction ? `
              <button class="annale-show-corr" type="button" onclick="toggleAnnaleCorrection('${corrId}', this)">▸ Afficher la correction</button>
              <div class="annale-correction" id="${corrId}" style="display:none">${escAnnale(it.correction)}</div>
            ` : ''}
          </div>`;
        }).join('');
        return `
        <div class="annale-dossier">
          <div class="annale-dossier-label">${escAnnale(ds.label || '')}</div>
          ${ds.context ? `<div class="annale-dossier-context">${escAnnale(ds.context)}</div>` : ''}
          <div class="annale-dossier-items">${itemsHTML}</div>
        </div>`;
      }).join('');
      const subjectHTML = a.subject ? `
        <div class="annale-subject">
          <div class="annale-block-title">📋 Énoncé général</div>
          <div class="annale-subject-content">${escAnnale(a.subject)}</div>
        </div>` : '';
      return `
      <div class="annale-card" id="${cardId}">
        ${head}
        <div class="annale-toolbar">
          <button class="annale-toolbar-btn" type="button" onclick="expandAllAnnales('#${cardId}')">▾ Tout afficher</button>
          <button class="annale-toolbar-btn" type="button" onclick="collapseAllAnnales('#${cardId}')">▸ Tout masquer</button>
        </div>
        ${subjectHTML}
        <div class="annale-dossiers">${dossiersHTML}</div>
        ${tipsHTML}
      </div>`;
    }

    // ── ANCIEN SCHÉMA (fallback pour annales non encore migrées) ──
    const exHTML = (a.exercises || []).map(e => `
      <div class="annale-exercise">
        <div class="annale-exercise-label">${escAnnale(e.label)}</div>
        <div class="annale-exercise-content">${escAnnale(e.content||'').replace(/\\n/g,'<br>')}</div>
      </div>
    `).join('');
    const bc = a.bestCopy;
    let bestCopyHTML = '';
    if (bc) {
      const planHTML = (bc.plan||[]).map(line => {
        const t = (line||'').trim();
        if (!t) return '<div class="annale-plan-spacer"></div>';
        if (/^(I+\\.|[0-9]+\\.|Introduction|Conclusion|Exercice|Q[0-9]+|•)/.test(t)) {
          return `<div class="annale-plan-line annale-plan-main">${escAnnale(t)}</div>`;
        }
        return `<div class="annale-plan-line">${escAnnale(t)}</div>`;
      }).join('');
      const conceptsHTML = (bc.keyConcepts||[]).map(c => `<span class="annale-concept">${escAnnale(c)}</span>`).join('');
      const qcmHTML = (bc.qcmAnswers||[]).length
        ? `<div class="annale-block annale-qcm"><div class="annale-block-title">QCM — réponses correctes</div>${bc.qcmAnswers.map(q=>`<div class="annale-qcm-line">${escAnnale(q)}</div>`).join('')}</div>`
        : '';
      bestCopyHTML = `
      <div class="annale-bestcopy">
        <div class="annale-bestcopy-head">
          <span class="annale-grade">📝 Note : ${escAnnale(bc.grade)}</span>
          ${bc.subjectChosen ? `<span class="annale-chosen">Sujet traité : ${escAnnale(bc.subjectChosen)}</span>` : ''}
        </div>
        ${qcmHTML}
        <div class="annale-block">
          <div class="annale-block-title">Plan-type / structure de la copie</div>
          <div class="annale-plan">${planHTML}</div>
        </div>
        ${(bc.keyConcepts||[]).length ? `
        <div class="annale-block">
          <div class="annale-block-title">Mots-clés &amp; concepts mobilisés</div>
          <div class="annale-concepts">${conceptsHTML}</div>
        </div>` : ''}
        ${bc.correctorNotes ? `<div class="annale-corrector"><strong>Annotations du correcteur :</strong> ${escAnnale(bc.correctorNotes)}</div>` : ''}
      </div>`;
    }
    let corrigeHTML = '';
    if (a.corrige && a.corrige.available) {
      const hl = (a.corrige.highlights||[]).map(h => `<li>${escAnnale(h)}</li>`).join('');
      corrigeHTML = `
      <div class="annale-corrige">
        <div class="annale-block-title">Corrigé officiel — points clés</div>
        ${a.corrige.summary ? `<p class="annale-corrige-summary">${escAnnale(a.corrige.summary)}</p>` : ''}
        <ul>${hl}</ul>
      </div>`;
    }
    return `
    <div class="annale-card">
      ${head}
      <div class="annale-subject">
        <div class="annale-block-title">📋 Sujet</div>
        <div class="annale-subject-content">${escAnnale(a.subject||'').replace(/\\n/g,'<br>')}</div>
      </div>
      ${exHTML ? `<div class="annale-exercises">${exHTML}</div>` : ''}
      ${bestCopyHTML}
      ${corrigeHTML}
      ${tipsHTML}
    </div>`;
  }).join('');
}
'''


def patch(html_file: str) -> None:
    path = ROOT / html_file
    text = path.read_text()
    if OLD not in text:
        raise SystemExit(f'{html_file}: ancien getAnnalesHTML non trouvé (déjà patché ?)')
    new_text = text.replace(OLD, NEW, 1)
    path.write_text(new_text)
    print(f'{html_file}: renderer annales migré')


if __name__ == '__main__':
    for f in ['conduite_chgt.html', 'evo_orga.html', 'gouv.html',
              'inge_fi.html', 'rse.html', 'strat.html']:
        patch(f)
