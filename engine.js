/* ═══════════════════════════════════════════════════════════
   M2 CCA — Moteur partagé (engine.js)
   Utilitaires communs : state, shuffle, fetchData, rendus,
   flashcards, quiz, confettis, ripple.
   ═══════════════════════════════════════════════════════════ */

/* ═══════ GLOBAL ERROR GUARD (évite l'écran noir silencieux) ═══════ */
window.addEventListener('error', (ev) => {
  const root = document.getElementById('appRoot');
  if (!root || root.querySelector('.err-banner')) return;
  root.insertAdjacentHTML('afterbegin', `
    <div class="err-banner" style="padding:1rem 1.2rem;margin-bottom:1rem;background:rgba(176,90,71,0.12);border:1px solid #b05a47;border-radius:10px;color:#e8b8a8;font-size:0.85rem;font-family:'JetBrains Mono',monospace">
      ⚠️ Erreur JS : ${ev.message || 'erreur inconnue'} — <a href="index.html" style="color:#85b0e0">retour à l'accueil</a>
    </div>`);
});

/* ═══════ CONTEXTE COURS & CONSTANTES ═══════ */
/* Clé de cours dérivée du nom de fichier — namespace la persistance (checklist,
   progression) pour éviter les collisions d'ids entre deux cours. */
const COURSE_KEY = (function () {
  const f = (location.pathname.split('/').pop() || '').replace(/\.html$/, '');
  return f === 'rse' ? 'rse_csrd' : (f || 'index');
})();
/* Plafond de cartes par session de révision espacée (évite les sessions fleuves). */
const SRS_SESSION_MAX = 20;

/* ═══════ STATE (progression checklist) ═══════ */
const STATE_KEY = 'm2cca_state';

function loadState() {
  try { return JSON.parse(localStorage.getItem(STATE_KEY)) || { checked: {} }; }
  catch (e) { return { checked: {} }; }
}
let state = loadState();
function saveState() { localStorage.setItem(STATE_KEY, JSON.stringify(state)); }
function isChecked(id) { return !!state.checked[id]; }
function toggleCheck(id) { state.checked[id] = !state.checked[id]; saveState(); }
function getProgress(items) {
  if (!items || !items.length) return 0;
  return Math.round(items.filter(i => isChecked(i.id)).length / items.length * 100);
}

/* ═══════ SCORES QUIZ ═══════ */
function loadQuizScores(key) {
  try { return JSON.parse(localStorage.getItem(key)) || []; }
  catch (e) { return []; }
}
function saveQuizScore(key, score, total) {
  const scores = loadQuizScores(key);
  scores.unshift({ score, total, date: Date.now() });
  localStorage.setItem(key, JSON.stringify(scores.slice(0, 20)));
}

/* Mini-courbe SVG de l'évolution des scores de quiz (du plus ancien au plus récent). */
function sparklineHTML(scores) {
  if (!scores || scores.length < 2) {
    return '<div class="quiz-spark-empty">Fais au moins 2 quiz pour voir ta courbe de progression.</div>';
  }
  const pts = scores.slice().reverse().map(s => s.total ? Math.round(s.score / s.total * 100) : 0);
  const W = 260, H = 54, pad = 6;
  const stepX = (W - 2 * pad) / (pts.length - 1);
  const xy = pts.map((p, i) => [pad + i * stepX, pad + (1 - p / 100) * (H - 2 * pad)]);
  const path = xy.map((c, i) => (i ? 'L' : 'M') + c[0].toFixed(1) + ' ' + c[1].toFixed(1)).join(' ');
  const area = path + ' L' + xy[xy.length - 1][0].toFixed(1) + ' ' + (H - pad)
    + ' L' + pad + ' ' + (H - pad) + ' Z';
  const dots = xy.map(c => '<circle cx="' + c[0].toFixed(1) + '" cy="' + c[1].toFixed(1)
    + '" r="2.6" fill="var(--accent3)"/>').join('');
  const delta = pts[pts.length - 1] - pts[0];
  const trend = delta > 0 ? '↗ +' + delta + ' pts' : (delta < 0 ? '↘ ' + delta + ' pts' : '→ stable');
  const trendCol = delta > 0 ? 'var(--green)' : (delta < 0 ? 'var(--red)' : 'var(--text3)');
  const midY = (pad + (H - 2 * pad) * 0.5).toFixed(1);
  return '<div class="quiz-spark">'
    + '<svg viewBox="0 0 ' + W + ' ' + H + '" class="quiz-spark-svg" aria-label="Courbe des scores de quiz">'
    + '<line x1="' + pad + '" y1="' + midY + '" x2="' + (W - pad) + '" y2="' + midY
    + '" stroke="var(--border)" stroke-width="1" stroke-dasharray="3 3"/>'
    + '<path d="' + area + '" fill="rgba(61,114,180,0.12)"/>'
    + '<path d="' + path + '" fill="none" stroke="var(--accent)" stroke-width="2" '
    + 'stroke-linejoin="round" stroke-linecap="round"/>'
    + dots + '</svg>'
    + '<div class="quiz-spark-lbl">' + pts.length + ' parties · '
    + '<span style="color:' + trendCol + '">' + trend + '</span> depuis le début</div>'
    + '</div>';
}

/* ═══════ PROGRESSION PAR COURS (agrégat lu par l'accueil) ═══════ */
const PROGRESS_KEY = 'm2cca_progress';
function loadCourseProgress() {
  try { return JSON.parse(localStorage.getItem(PROGRESS_KEY)) || {}; }
  catch (e) { return {}; }
}
function saveCourseProgress(courseKey, done, total) {
  try {
    const all = loadCourseProgress();
    all[courseKey] = { done: done, total: total, ts: Date.now() };
    localStorage.setItem(PROGRESS_KEY, JSON.stringify(all));
  } catch (e) { /* quota / navigation privée : ignoré */ }
}

/* ═══════ SRS — SPACED REPETITION (SM-2 simplifié) ═══════ */
const SRS_DAY_MS = 86400000;
function srsKey(courseKey) { return 'm2cca_srs_' + courseKey; }

function loadSRS(courseKey) {
  try { return JSON.parse(localStorage.getItem(srsKey(courseKey))) || {}; }
  catch (e) { return {}; }
}
function saveSRS(courseKey, state) {
  try { localStorage.setItem(srsKey(courseKey), JSON.stringify(state)); }
  catch (e) { console.warn('[srs] persistence failed', e); }
}

/* Met à jour l'état d'une carte selon la note (again / good / easy). Retourne le nouvel état. */
function srsScheduleCard(prev, grade) {
  let { ef = 2.5, interval = 0, reps = 0 } = prev || {};
  const now = Date.now();
  if (grade === 'again') {
    reps = 0;
    interval = 0; // immédiatement due → réapparait au prochain build de queue
    ef = Math.max(1.3, ef - 0.2);
  } else if (grade === 'good') {
    if (reps === 0) interval = 1;
    else if (reps === 1) interval = 6;
    else interval = Math.max(1, Math.round(interval * ef));
    reps += 1;
  } else if (grade === 'easy') {
    if (reps === 0) interval = 3;
    else if (reps === 1) interval = 10;
    else interval = Math.max(1, Math.round(interval * ef * 1.3));
    ef = ef + 0.15;
    reps += 1;
  }
  return { ef, interval, reps, due: now + interval * SRS_DAY_MS, last: now };
}

/* Construit la file de révision : new + due, priorité aux jamais-vues puis aux plus en retard. */
function srsBuildQueue(state, totalCards, maxSize) {
  const now = Date.now();
  const items = [];
  for (let i = 0; i < totalCards; i++) {
    const s = state[i];
    if (!s) items.push({ i, priority: 0, due: 0 });               // never seen
    else if (s.due <= now) items.push({ i, priority: 1, due: s.due }); // due/overdue
  }
  items.sort((a, b) => a.priority - b.priority || a.due - b.due);
  const cap = maxSize || items.length;
  return items.slice(0, cap).map(it => it.i);
}

/* Statistiques globales : new / due / learned / nextDue */
function srsGetStats(state, totalCards) {
  const now = Date.now();
  let neww = 0, due = 0, learned = 0;
  let nextDue = Infinity;
  for (let i = 0; i < totalCards; i++) {
    const s = state[i];
    if (!s) neww += 1;
    else if (s.due <= now) due += 1;
    else {
      learned += 1;
      if (s.due < nextDue) nextDue = s.due;
    }
  }
  return {
    total: totalCards,
    new: neww,
    due,
    learned,
    sessionSize: neww + due,
    nextDue: nextDue === Infinity ? null : nextDue,
  };
}

/* Pour l'aperçu sur les boutons : prochain intervalle si on grade ainsi (en jours) */
function srsPreviewInterval(prev, grade) {
  const next = srsScheduleCard(prev, grade);
  return next.interval;
}

/* Format humain d'un intervalle : maintenant, 1 j, 6 j, 2 mois, etc. */
function srsFormatInterval(days) {
  if (days <= 0) return 'mtnt';
  if (days < 1) return '<1 j';
  if (days < 30) return Math.round(days) + ' j';
  if (days < 365) return Math.round(days / 30) + ' mois';
  return (days / 365).toFixed(1) + ' an';
}

/* ═══════ UTILS ═══════ */
function shuffle(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function animCount(el, target, suffix = '', dur = 1200) {
  if (!el) return;
  const start = Date.now();
  const tick = () => {
    const t = Math.min((Date.now() - start) / dur, 1);
    const ease = 1 - Math.pow(1 - t, 3);
    el.textContent = Math.round(ease * target) + suffix;
    if (t < 1) requestAnimationFrame(tick);
    else el.textContent = target + suffix;
  };
  requestAnimationFrame(tick);
}

/* ═══════ DATA LOADER (JSON ou fallback inline) ═══════ */
async function loadJSON(path, fallback) {
  const ctrl = new AbortController();
  const tid = setTimeout(() => ctrl.abort(), 4000);
  try {
    const res = await fetch(path, { signal: ctrl.signal });
    clearTimeout(tid);
    if (!res.ok) throw new Error('HTTP ' + res.status);
    return await res.json();
  } catch (e) {
    clearTimeout(tid);
    console.warn('[engine] fallback inline pour', path, '—', e.message);
    return fallback || null;
  }
}

/* ═══════ STREAK ═══════ */
const STREAK_KEY = 'm2cca_streak';
function getStreak() {
  const today = new Date().toDateString();
  let s;
  try { s = JSON.parse(localStorage.getItem(STREAK_KEY)) || { count: 0, last: '' }; }
  catch (e) { s = { count: 0, last: '' }; }
  if (s.last === today) return s.count;
  const yesterday = new Date(Date.now() - 86400000).toDateString();
  s.count = s.last === yesterday ? s.count + 1 : 1;
  s.last = today;
  localStorage.setItem(STREAK_KEY, JSON.stringify(s));
  return s.count;
}

/* ═══════ RIPPLE EFFECT ═══════ */
function attachRipple(el) {
  el.addEventListener('click', (e) => {
    const rect = el.getBoundingClientRect();
    const r = document.createElement('span');
    r.className = 'ripple';
    const size = Math.max(rect.width, rect.height);
    r.style.width = r.style.height = size + 'px';
    r.style.left = (e.clientX - rect.left - size / 2) + 'px';
    r.style.top = (e.clientY - rect.top - size / 2) + 'px';
    el.appendChild(r);
    setTimeout(() => r.remove(), 600);
  });
}

/* ═══════ CONFETTI (allégé) ═══════ */
function launchConfetti() {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const canvas = document.createElement('canvas');
  Object.assign(canvas.style, { position: 'fixed', inset: 0, pointerEvents: 'none', zIndex: 9999, width: '100%', height: '100%' });
  canvas.width = innerWidth; canvas.height = innerHeight;
  document.body.appendChild(canvas);
  const ctx = canvas.getContext('2d');
  const colors = ['#3d72b4', '#c88346', '#5c8fd1', '#5a9168', '#c99850', '#dde3ec'];
  const COUNT = 55, MAX_FRAMES = 180;
  const p = Array.from({ length: COUNT }, () => ({
    x: Math.random() * canvas.width, y: -20,
    vx: (Math.random() - 0.5) * 6, vy: Math.random() * 4 + 2,
    color: colors[Math.floor(Math.random() * colors.length)],
    size: Math.random() * 8 + 4, rot: Math.random() * 360,
    rotV: (Math.random() - 0.5) * 12, op: 1
  }));
  let frame = 0;
  (function anim() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    let alive = false;
    for (let i = 0; i < p.length; i++) {
      const q = p[i];
      if (q.y < canvas.height + 20) {
        alive = true; q.x += q.vx; q.y += q.vy; q.vy += 0.08; q.rot += q.rotV;
        if (q.y > canvas.height * 0.7) q.op = Math.max(0, q.op - 0.02);
        ctx.save(); ctx.globalAlpha = q.op; ctx.translate(q.x, q.y); ctx.rotate(q.rot * Math.PI / 180);
        ctx.fillStyle = q.color; ctx.fillRect(-q.size / 2, -q.size / 4, q.size, q.size / 2);
        ctx.restore();
      }
    }
    if (alive && frame++ < MAX_FRAMES) requestAnimationFrame(anim); else canvas.remove();
  })();
}

/* ═══════ HELPERS DE RENDU PARTIEL FLASHCARD / QUIZ ═══════ */
/* Évite les innerHTML complets : on met à jour uniquement le contenu qui change.
 * Signature étendue : ctx = { fcQueue, fcKnown, fcStreak, fcSRS, fcSRSMode, fcSessionSize }
 * Rétrocompatible : appelable comme (DATA, fcQueue, fcKnown, fcStreak) sans SRS. */
function updateFlashCardPartial(DATA, fcQueueOrCtx, fcKnown, fcStreak) {
  let ctx;
  if (Array.isArray(fcQueueOrCtx)) {
    ctx = { fcQueue: fcQueueOrCtx, fcKnown, fcStreak, fcSRS: {}, fcSRSMode: 'shuffle', fcSessionSize: DATA.flashcards.length };
  } else {
    ctx = fcQueueOrCtx;
  }
  const { fcQueue, fcSRS = {}, fcSRSMode = 'shuffle', fcSessionSize } = ctx;
  const total = DATA.flashcards.length;
  const known = (ctx.fcKnown || []).length;
  const sessionSize = fcSessionSize || total;
  const pct = sessionSize > 0 ? Math.round(known / sessionSize * 100) : 0;

  const pbFill = document.querySelector('.fc-pb-fill');
  const pbLabel = document.querySelector('.fc-pb-label');
  const counter = document.querySelector('.fc-counter');
  const cardEl = document.getElementById('fcCard');
  const qEl = document.querySelector('.flashcard-q');
  const aEl = document.querySelector('.flashcard-a');
  const actions = document.querySelector('.fc-actions');

  if (!pbFill || !pbLabel || !counter || !cardEl || !qEl || !aEl || fcQueue.length === 0) {
    return false;
  }

  const cardIdx = fcQueue[0];
  const card = DATA.flashcards[cardIdx];
  const cardSRS = fcSRS[cardIdx];
  pbFill.style.width = pct + '%';
  const streakHTML = (ctx.fcStreak || 0) >= 2 ? `<span class="fc-streak">🔥 ${ctx.fcStreak} d'affilée</span>` : '';
  const stats = srsGetStats(fcSRS, total);
  const dueHTML = (stats.due > 0 && fcSRSMode === 'srs') ? ` · <span style="color:var(--orange)">${stats.due} dues</span>` : '';
  pbLabel.innerHTML = `${known} / ${sessionSize} en session · ${stats.learned}/${stats.total} maîtrisées${dueHTML} ${streakHTML}`;
  counter.textContent = `Carte ${known + 1} sur ${sessionSize} — ${fcQueue.length} restante(s)`;
  cardEl.classList.remove('flipped');
  qEl.textContent = card.q;
  aEl.textContent = card.a;
  // Badge source : cliquable si srcChap présent → ouvre le chapitre du cours
  let srcEl = aEl.parentElement.querySelector('.flashcard-src');
  if (srcEl) srcEl.remove();
  if (card.src) {
    const isLink = !!card.srcChap;
    srcEl = document.createElement(isLink ? 'a' : 'div');
    srcEl.className = 'flashcard-src' + (isLink ? ' flashcard-src-link' : '');
    if (isLink) {
      srcEl.href = '#chap-' + card.srcChap;
      srcEl.title = 'Cliquer pour ouvrir ce chapitre dans le cours';
      srcEl.onclick = function (e) {
        e.preventDefault();
        e.stopPropagation();
        if (typeof switchTab === 'function') {
          window._pendingCoursJump = function () {
            const el = document.getElementById('chap-' + card.srcChap);
            if (el) {
              if (el.style.display === 'none' && typeof coursTheme !== 'undefined') {
                coursTheme = 'all';
                if (typeof applyCoursFilter === 'function') applyCoursFilter();
                if (typeof renderCoursPills === 'function') renderCoursPills();
              }
              el.scrollIntoView({ behavior: 'smooth', block: 'start' });
              el.classList.add('chap-target-flash');
              setTimeout(function () { el.classList.remove('chap-target-flash'); }, 2400);
            }
          };
          switchTab('cours');
        }
      };
    }
    srcEl.innerHTML = '✓ ' + card.src + (isLink ? ' →' : '');
    aEl.parentElement.appendChild(srcEl);
  }

  // Mise à jour des boutons SRS (intervalles)
  if (actions && fcSRSMode === 'srs') {
    const ivAgain = srsFormatInterval(srsPreviewInterval(cardSRS, 'again'));
    const ivGood  = srsFormatInterval(srsPreviewInterval(cardSRS, 'good'));
    const ivEasy  = srsFormatInterval(srsPreviewInterval(cardSRS, 'easy'));
    const ivs = actions.querySelectorAll('.fc-btn-iv');
    if (ivs.length >= 3) {
      ivs[0].textContent = ivAgain;
      ivs[1].textContent = ivGood;
      ivs[2].textContent = ivEasy;
    }
  }
  return true;
}

function updateQuizQuestionPartial(quizState) {
  if (!quizState) return false;
  const qi = quizState.current;
  const q = quizState.questions[qi];
  const total = quizState.questions.length;
  const letters = ['A','B','C','D'];

  const card = document.getElementById('quizCard');
  const progSpan = document.querySelector('.quiz-progress span');
  const globalFill = document.querySelector('.quiz-global-fill');
  if (!card || !progSpan || !q) return false;

  card.classList.remove('shake');
  progSpan.textContent = `Question ${qi + 1} / ${total}`;
  if (globalFill) globalFill.style.width = Math.round((qi / total) * 100) + '%';

  // ── Question Vrai/Faux multiple : rendu spécifique
  if (q.type === 'tf') {
    return renderTFQuestionInline(card, q, qi, quizState);
  }

  const srcBadge = q.src
    ? (q.srcChap
        ? ` <a class="quiz-src-badge quiz-src-badge-link" href="#chap-${q.srcChap}" onclick="event.preventDefault();event.stopPropagation();window._pendingCoursJump=function(){var el=document.getElementById('chap-${q.srcChap}');if(el){if(el.style.display==='none'&&typeof coursTheme!=='undefined'){coursTheme='all';if(typeof applyCoursFilter==='function')applyCoursFilter();if(typeof renderCoursPills==='function')renderCoursPills();}el.scrollIntoView({behavior:'smooth',block:'start'});el.classList.add('chap-target-flash');setTimeout(function(){el.classList.remove('chap-target-flash');},2400);}};switchTab('cours');" title="Cliquer pour ouvrir ce chapitre dans le cours">✓ ${q.src} →</a>`
        : ` <span class="quiz-src-badge">✓ ${q.src}</span>`)
    : '';
  card.innerHTML = `
    <div class="quiz-q-num">Q${qi + 1}${srcBadge}</div>
    <div class="quiz-q-text">${q.q}</div>
    <div class="quiz-options" id="quizOpts">
      ${q.o.map((opt, i) => `
        <button class="quiz-option" data-i="${i}" onclick="selectAnswer(event, ${qi}, ${i})">
          <div class="opt-letter">${letters[i]}</div>
          <span>${opt}</span>
        </button>`).join('')}
    </div>`;
  card.querySelectorAll('.quiz-option').forEach(attachRipple);
  return true;
}

/* ═══════ VRAI/FAUX MULTIPLE ═══════
 * Format question : { type: 'tf', q: 'Sur le thème X :', aff: [{t,c,e}, ...4 items], theme, src, srcChap }
 * Réponse stockée : quizState.answers[qi] = { aff: [bool|null × 4], locked: bool }
 * Une question TF compte juste pour CORRECT/INCORRECT (binaire) : il faut les 4 affirmations justes.
 */
function renderTFQuestionInline(card, q, qi, quizState) {
  quizState.answers[qi] = quizState.answers[qi] || { aff: q.aff.map(() => null), locked: false };
  const ans = quizState.answers[qi];
  const srcBadge = q.src
    ? (q.srcChap
        ? ` <a class="quiz-src-badge quiz-src-badge-link" href="#chap-${q.srcChap}" onclick="event.preventDefault();event.stopPropagation();window._pendingCoursJump=function(){var el=document.getElementById('chap-${q.srcChap}');if(el){if(el.style.display==='none'&&typeof coursTheme!=='undefined'){coursTheme='all';if(typeof applyCoursFilter==='function')applyCoursFilter();if(typeof renderCoursPills==='function')renderCoursPills();}el.scrollIntoView({behavior:'smooth',block:'start'});el.classList.add('chap-target-flash');setTimeout(function(){el.classList.remove('chap-target-flash');},2400);}};switchTab('cours');" title="Cliquer pour ouvrir ce chapitre dans le cours">✓ ${q.src} →</a>`
        : ` <span class="quiz-src-badge">✓ ${q.src}</span>`)
    : '';
  const rowsHTML = q.aff.map((a, ai) => {
    const v = ans.aff[ai];
    const selV = v === true ? ' selected' : '';
    const selF = v === false ? ' selected' : '';
    return `
      <div class="tf-row" data-aff="${ai}">
        <div class="tf-text">${a.t}</div>
        <div class="tf-buttons">
          <button class="tf-btn tf-vrai${selV}" onclick="selectTFAnswer(${qi}, ${ai}, true)" aria-label="Vrai">V</button>
          <button class="tf-btn tf-faux${selF}" onclick="selectTFAnswer(${qi}, ${ai}, false)" aria-label="Faux">F</button>
        </div>
      </div>`;
  }).join('');
  card.innerHTML = `
    <div class="quiz-q-num">Q${qi + 1} <span class="quiz-q-type-badge">Vrai / Faux</span>${srcBadge}</div>
    <div class="quiz-q-text">${q.q}</div>
    <div class="tf-hint">Coche V ou F pour chaque affirmation. La correction détaillée s'affiche une fois les 4 réponses données.</div>
    <div class="tf-affirmations">${rowsHTML}</div>
  `;
  // Si la question avait déjà été validée (navigation arrière hypothétique), re-affiche les corrections
  if (ans.locked) finalizeTFAnswer(qi, /*rerender*/true);
  return true;
}

function selectTFAnswer(qi, affIdx, value) {
  if (typeof quizState === 'undefined' || !quizState) return;
  const q = quizState.questions[qi];
  if (!q || q.type !== 'tf') return;
  const ans = quizState.answers[qi] = quizState.answers[qi] || { aff: q.aff.map(() => null), locked: false };
  if (ans.locked) return;
  ans.aff[affIdx] = value;
  // refresh UI for that row
  const card = document.getElementById('quizCard');
  if (card) {
    const row = card.querySelector(`.tf-row[data-aff="${affIdx}"]`);
    if (row) {
      row.querySelector('.tf-vrai').classList.toggle('selected', value === true);
      row.querySelector('.tf-faux').classList.toggle('selected', value === false);
    }
  }
  // Si toutes les affirmations sont répondues, on valide
  if (ans.aff.every(v => v !== null)) {
    finalizeTFAnswer(qi, false);
  }
}

function finalizeTFAnswer(qi, rerender) {
  if (typeof quizState === 'undefined' || !quizState) return;
  const q = quizState.questions[qi];
  if (!q || q.type !== 'tf') return;
  const ans = quizState.answers[qi];
  if (!ans) return;
  ans.locked = true;
  const allCorrect = q.aff.every((a, i) => a.c === ans.aff[i]);
  // Push to errors list if any wrong (only on first finalize, not on rerender)
  if (!rerender && !allCorrect && Array.isArray(quizState.errors)) {
    // évite les doublons
    if (!quizState.errors.some(e => e.qi === qi)) quizState.errors.push({ qi, chosen: -1 });
  }
  const card = document.getElementById('quizCard');
  if (!card) return;
  // Décorer chaque ligne
  q.aff.forEach((a, i) => {
    const row = card.querySelector(`.tf-row[data-aff="${i}"]`);
    if (!row) return;
    const userVal = ans.aff[i];
    const isCorrect = a.c === userVal;
    row.classList.add(isCorrect ? 'tf-ok' : 'tf-ko');
    row.querySelectorAll('.tf-btn').forEach(b => b.classList.add('tf-disabled'));
    // mettre en évidence la bonne réponse
    const correctBtn = row.querySelector(a.c ? '.tf-vrai' : '.tf-faux');
    if (correctBtn) correctBtn.classList.add('tf-correct-highlight');
    // append explanation (sauf si déjà là en cas de rerender)
    if (!row.querySelector('.tf-explanation') && a.e) {
      const expl = document.createElement('div');
      expl.className = 'tf-explanation' + (isCorrect ? ' ok' : ' ko');
      const label = a.c ? 'Vrai' : 'Faux';
      expl.innerHTML = `<strong>${isCorrect ? '✓' : '✗'} Réponse : ${label}.</strong> ${a.e}`;
      row.appendChild(expl);
    }
  });
  if (!rerender) {
    if (!allCorrect) {
      card.classList.add('shake');
      setTimeout(() => card.classList.remove('shake'), 500);
    }
  }
  // Bouton "Suivant" si pas déjà présent
  if (!card.querySelector('.quiz-next-btn')) {
    const nextBtn = document.createElement('button');
    nextBtn.className = 'quiz-next-btn';
    const isLast = quizState.current >= quizState.questions.length - 1;
    nextBtn.textContent = isLast ? 'Voir les résultats →' : 'Question suivante →';
    nextBtn.onclick = () => { quizState.current++; if (typeof renderQuizQuestion === 'function') renderQuizQuestion(); };
    card.appendChild(nextBtn);
  }
}

/* Helper de scoring uniforme QCM + TF — à utiliser dans showQuizResult de chaque cours */
function isQuestionCorrect(q, answer) {
  if (!q) return false;
  if (q.type === 'tf') {
    if (!answer || !Array.isArray(answer.aff)) return false;
    return q.aff.every((a, i) => a.c === answer.aff[i]);
  }
  return answer === q.c;
}

/* HTML formaté de la « bonne réponse » pour la zone d'erreurs à revoir.
 * Utilisé dans le showQuizResult de chaque cours. */
function formatCorrectAnswerHTML(q) {
  if (!q) return '';
  if (q.type === 'tf') {
    return q.aff.map(a => `<div class="error-tf-aff"><span class="error-tf-label">${a.c ? 'V' : 'F'}</span> ${a.t}</div>`).join('');
  }
  return '✓ ' + (q.o ? q.o[q.c] : '');
}

/* ═══════ QUIZ — préparation & rejeu ═══════ */
/* Renvoie une COPIE de la question avec les options mélangées : la position de la
   bonne réponse varie d'une partie à l'autre (impossible à mémoriser). Ne mute
   jamais les données source. */
function quizShuffleQuestion(q) {
  if (!q) return q;
  if (q.type === 'tf') {
    return Object.assign({}, q, { aff: shuffle(q.aff || []) });
  }
  if (!Array.isArray(q.o)) return Object.assign({}, q);
  const order = shuffle(q.o.map((_, i) => i));
  return Object.assign({}, q, {
    o: order.map(i => q.o[i]),
    c: order.indexOf(q.c),
  });
}

/* Relance un quiz composé uniquement des questions ratées de la partie en cours. */
function replayErrors() {
  if (typeof quizState === 'undefined' || !quizState || !quizState.errors || !quizState.errors.length) return;
  const errQs = quizState.errors.map(e => quizState.questions[e.qi]);
  quizState = {
    questions: shuffle(errQs).map(quizShuffleQuestion),
    current: 0,
    answers: [],
    timerEnabled: false,
    errors: [],
  };
  if (typeof renderQuizQuestion === 'function') renderQuizQuestion();
}

/* ═══════ SCROLL-SPY (desktop only) ═══════ */
function buildScrollSpy(containerSelector, targetSelector) {
  if (window.innerWidth < 1200) return;
  const container = document.querySelector(containerSelector);
  if (!container) return;
  const headers = Array.from(document.querySelectorAll(targetSelector));
  if (!headers.length) return;
  const spy = document.createElement('div');
  spy.className = 'scroll-spy';
  spy.innerHTML = headers.map((h, i) => {
    h.id = h.id || 'sec-' + i;
    return `<a class="scroll-spy-item" href="#${h.id}" data-target="${h.id}">${h.textContent.trim()}</a>`;
  }).join('');
  document.body.appendChild(spy);
  const io = new IntersectionObserver((entries) => {
    entries.forEach(en => {
      if (en.isIntersecting) {
        spy.querySelectorAll('.scroll-spy-item').forEach(s => s.classList.remove('active'));
        const a = spy.querySelector(`[data-target="${en.target.id}"]`);
        if (a) a.classList.add('active');
      }
    });
  }, { rootMargin: '-40% 0px -55% 0px' });
  headers.forEach(h => io.observe(h));
  spy._cleanup = () => { io.disconnect(); spy.remove(); };
  return spy;
}

function removeScrollSpy() {
  const spy = document.querySelector('.scroll-spy');
  if (spy && spy._cleanup) spy._cleanup();
  else if (spy) spy.remove();
}


/* ═══════════════════════════════════════════════════════════
   EXPORT PDF — impression navigateur (cours, examen, annales)
   Transversal : disponible sur tous les cours de la plateforme.
   ═══════════════════════════════════════════════════════════ */

function m2Esc(s) {
  return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) {
    return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
  });
}

function m2CourseTitle() {
  if (window.DATA && DATA.title) return DATA.title;
  return (document.title || 'Cours').replace(/\s*[—-]\s*M2 CCA.*$/, '').trim() || 'Cours';
}

function m2PdfStyles() {
  return `
    :root{
      --accent:#2f5fa6;--accent2:#3d72b4;--accent3:#2f5fa6;
      --copper:#b8791f;--copper-2:#9a6420;
      --green:#2e7d4f;--green-bg:#eef5f0;--red:#b3392f;--red-bg:#f7ecea;
      --orange:#b8791f;--orange-bg:#fbf4e8;--cyan:#3a7a86;
      --text:#1a1a1a;--text2:#444;--text3:#777;--border:#c4c4c4;
      --bg:#fff;--bg2:#f6f8fb;--bg3:#eef1f6;--card:#fff;--card-hover:#f0f3f8;
      --glass:#f6f8fb;--glass-b:#d8dee8;--radius:6px;
    }
    *{box-sizing:border-box;}
    html,body{margin:0;padding:0;background:#fff;color:#1a1a1a;
      font-family:Georgia,'Times New Roman',serif;font-size:11.5pt;line-height:1.5;}
    .pdf-doc{padding:0 2mm;}
    .pdf-h1{font-size:20pt;color:#2f5fa6;margin:0 0 2mm;border-bottom:2px solid #2f5fa6;padding-bottom:2mm;}
    .pdf-sub{color:#555;font-size:10pt;margin:0 0 2mm;font-style:italic;}
    .pdf-meta{color:#777;font-size:8.5pt;margin:0 0 6mm;}
    /* ── Page de garde ── */
    .pdf-cover{break-after:page;height:250mm;display:flex;flex-direction:column;
      align-items:center;justify-content:center;text-align:center;
      border-top:5pt solid;border-bottom:5pt solid;padding:14mm 12mm;}
    .pdf-cover-eyebrow{font-size:10pt;letter-spacing:2.5pt;text-transform:uppercase;
      color:#888;margin-bottom:20mm;font-family:'Helvetica Neue',Arial,sans-serif;}
    .pdf-cover-icon{font-size:46pt;line-height:1;margin-bottom:12mm;}
    .pdf-cover-kicker{font-size:12pt;font-weight:bold;letter-spacing:3.5pt;text-transform:uppercase;
      margin-bottom:5mm;font-family:'Helvetica Neue',Arial,sans-serif;}
    .pdf-cover-title{font-size:33pt;font-weight:bold;color:#1a1a1a;line-height:1.12;
      margin:0 0 6mm;max-width:160mm;}
    .pdf-cover-sub{font-size:12.5pt;color:#555;font-style:italic;max-width:135mm;line-height:1.5;}
    .pdf-cover-rule{width:38mm;height:3pt;margin:15mm 0 8mm;border-radius:2pt;}
    .pdf-cover-foot{font-size:10pt;color:#888;line-height:1.7;font-family:'Helvetica Neue',Arial,sans-serif;}
    h2,.chapter-title{font-size:15pt;color:#2f5fa6;margin:7mm 0 3mm;
      border-bottom:1px solid #c4c4c4;padding-bottom:1.5mm;break-after:avoid;}
    h3{font-size:12.5pt;color:#1a1a1a;margin:5mm 0 2mm;break-after:avoid;}
    p{margin:0 0 2.5mm;}
    ul,ol{margin:0 0 3mm;padding-left:7mm;}
    li{margin:0 0 1mm;}
    strong{color:#000;}
    em{color:#333;}
    table{width:100%;border-collapse:collapse;margin:3mm 0;font-size:10pt;break-inside:avoid;}
    th,td{border:1px solid #b8b8b8;padding:1.6mm 2.4mm;text-align:left;vertical-align:top;}
    th{background:#e9eef5;color:#1a1a1a;font-weight:bold;}
    .def-box,.key-box,.example-box{border:1px solid #c4c4c4;border-left:4px solid #2f5fa6;
      background:#f6f8fb;padding:2.5mm 3.5mm;margin:3mm 0;break-inside:avoid;border-radius:2px;}
    .key-box{border-left-color:#b8791f;background:#fbf7ef;}
    .example-box{border-left-color:#2e7d4f;background:#f1f7f3;
      font-family:'Courier New',monospace;font-size:10pt;}
    .course-chapter{margin:0 0 4mm;}
    .annale-head,.annale-dossier,.exam-result-dossier,.annale-question{break-inside:avoid;}
    .annale-year,.annale-title,.exam-result-dossier-title{font-weight:bold;color:#2f5fa6;}
    .annale-meta{color:#777;font-size:9pt;}
    .annale-dossier-label{font-weight:bold;font-size:12pt;margin:5mm 0 2mm;color:#1a1a1a;}
    .annale-dossier-context,.annale-q-text,.exam-result-q-text{margin:2mm 0;}
    .annale-correction,.exam-result-q-body{background:#f1f7f3;border-left:3px solid #2e7d4f;
      padding:2mm 3mm;margin:1.5mm 0;white-space:pre-wrap;font-size:10pt;}
    .annale-tips{border:1px dashed #b8791f;background:#fbf7ef;padding:2.5mm 3.5mm;margin:3mm 0;}
    .annale-block-title{font-weight:bold;margin-bottom:1.5mm;}
    .exam-result-q{margin:2mm 0;break-inside:avoid;}
    .exam-result-q-head{font-weight:bold;margin-bottom:1mm;}
    .exam-result-q.ko .exam-result-q-body{border-left-color:#b3392f;background:#fbf1f0;}
    .score-box{border:2px solid #2f5fa6;border-radius:4px;padding:3mm;text-align:center;margin:0 0 4mm;}
    .score-num,.score-emoji{font-size:15pt;font-weight:bold;}
    .exam-dossier,.exam-q{break-inside:avoid;margin:3mm 0;}
    input,textarea{border:1px solid #999;padding:1mm;font-family:inherit;font-size:10pt;
      background:#fff;color:#000;}
    textarea{width:100%;min-height:22mm;white-space:pre-wrap;display:block;}
    input[type=text],input[type=number]{min-width:28mm;}
    button,.scroll-spy,.m2-pdf-bar,.exam-timer-bar{display:none !important;}
    a{color:#1a1a1a;text-decoration:none;}
    /* ── Schémas (rendu clair pour impression) ── */
    .schema-intro{display:none;}
    .schema-theme{font-size:14pt;font-weight:bold;color:#2f5fa6;margin:7mm 0 3mm;
      border-bottom:1px solid #c4c4c4;padding-bottom:1.5mm;break-after:avoid;}
    .schema-card{border:1px solid #c4c4c4;border-radius:3px;padding:4mm;margin:0 0 4mm;break-inside:avoid;}
    .schema-title{font-weight:bold;font-size:11.5pt;margin-bottom:3mm;}
    .schema-viz{margin-bottom:3mm;}
    .schema-note{font-size:9pt;color:#555;border-top:1px solid #ddd;padding-top:2mm;}
    .sch-formula{font-family:'Courier New',monospace;font-size:9.5pt;color:#2f5fa6;background:#f6f8fb;
      border:1px solid #d8dee8;border-radius:3px;padding:2mm;text-align:center;margin-top:3mm;}
    .sch-bar{display:flex;border-radius:3px;overflow:hidden;min-height:16mm;}
    .sch-bar-seg{display:flex;flex-direction:column;align-items:center;justify-content:center;
      gap:1mm;padding:2mm;color:#fff;font-size:8.5pt;text-align:center;}
    .sch-bar-seg strong{font-family:'Courier New',monospace;font-size:9.5pt;}
    .sch-seg-cp{background:#2f5fa6;flex:58;}.sch-seg-dette{background:#b8791f;flex:42;}
    .sch-bar-legend{display:flex;justify-content:space-between;font-size:8pt;color:#777;margin-top:1mm;}
    .sch-eq{text-align:center;font-family:'Courier New',monospace;font-size:9.5pt;color:#444;margin-bottom:3mm;}
    .sch-duo{display:flex;gap:3mm;}
    .sch-duo-box{flex:1;border:1px solid #c4c4c4;border-radius:3px;padding:3mm;background:#f6f8fb;}
    .sch-duo-box h4{font-size:10pt;margin:0 0 2mm;}
    .sch-tag{display:inline-block;font-size:8pt;padding:0.6mm 2mm;border-radius:3px;
      margin:0.6mm 1mm 0.6mm 0;font-family:'Helvetica Neue',Arial,sans-serif;}
    .tag-ok{background:#eef5f0;color:#2e7d4f;}.tag-no{background:#f7ecea;color:#b3392f;}
    .tag-neu{background:#eef1f6;color:#555;border:1px solid #d8dee8;}
    .sch-gauge{display:flex;border:1px solid #c4c4c4;border-radius:3px;overflow:hidden;}
    .sch-gauge-zone{flex:1;padding:2.5mm;text-align:center;font-size:8.5pt;color:#444;}
    .sch-gauge-zone strong{display:block;font-family:'Courier New',monospace;font-size:10pt;color:#1a1a1a;margin-bottom:1mm;}
    .sch-svg{width:100%;max-width:115mm;height:auto;display:block;margin:0 auto;}
    .sch-svg-donut{max-width:72mm;}
    .sch-flow{display:flex;align-items:center;gap:2mm;flex-wrap:wrap;justify-content:center;}
    .sch-flow-box{border:1px solid #2f5fa6;border-radius:3px;padding:2mm 3mm;background:#eef3fa;
      text-align:center;font-size:9pt;font-weight:bold;}
    .sch-flow-box small{display:block;font-weight:normal;font-size:7.5pt;color:#777;margin-top:0.6mm;}
    .sch-flow-pivot{border-color:#b8791f;background:#fbf4e8;}
    .sch-flow-op{font-size:7.5pt;color:#777;font-family:'Courier New',monospace;text-align:center;}
    .sch-substeps-label{font-size:9pt;font-weight:bold;color:#444;margin:3mm 0 2mm;}
    .sch-steps{display:flex;flex-direction:column;gap:1.5mm;}
    .sch-step{display:flex;gap:2.5mm;align-items:flex-start;}
    .sch-step-num{flex-shrink:0;width:6mm;height:6mm;border-radius:50%;background:#2f5fa6;color:#fff;
      display:flex;align-items:center;justify-content:center;font-size:8.5pt;font-weight:bold;}
    .sch-step-txt{font-size:9.5pt;color:#444;}
    .sch-cols3{display:flex;gap:2.5mm;}
    .sch-mode{flex:1;border:1px solid #c4c4c4;border-radius:3px;padding:3mm;background:#f6f8fb;text-align:center;}
    .sch-mode h4{font-size:9.5pt;margin:0 0 2mm;}
    .sch-mode small{display:block;font-size:8pt;color:#777;margin-top:2mm;}
    .sch-annuity{display:flex;align-items:flex-end;justify-content:center;gap:2mm;height:18mm;}
    .sch-annuity i{width:5mm;background:#2f5fa6;border-radius:2px 2px 0 0;}
    .sch-tunnel{display:flex;flex-direction:column;}
    .sch-tunnel-band{padding:2.5mm;text-align:center;font-size:9pt;}
    .sch-band-top{background:#f7ecea;color:#b3392f;}
    .sch-band-mid{background:#eef1f6;font-weight:bold;padding:4mm 2.5mm;}
    .sch-band-bot{background:#eef5f0;color:#2e7d4f;}
    .sch-tunnel-line{text-align:center;font-family:'Courier New',monospace;font-size:8pt;color:#b8791f;
      font-weight:bold;padding:1mm 0;border-top:1.5pt dashed #b8791f;border-bottom:1.5pt dashed #b8791f;}
    .sch-scopes{display:flex;flex-direction:column;gap:1.5mm;}
    .sch-scope{border-radius:3px;padding:2.5mm 3mm;color:#fff;}
    .sch-scope strong{display:block;font-size:9.5pt;margin-bottom:0.6mm;}
    .sch-scope small{font-size:8pt;}
    .sch-scope-1{background:#2f5fa6;}.sch-scope-2{background:#3a7a86;}.sch-scope-3{background:#b8791f;}
    .sch-legend{margin-top:3mm;display:flex;flex-direction:column;gap:1.2mm;}
    .sch-legend-row{display:flex;align-items:center;gap:2mm;font-size:9pt;color:#444;}
    .sch-dot{width:3mm;height:3mm;border-radius:50%;flex-shrink:0;}
    .sch-grid4{display:flex;flex-wrap:wrap;gap:2.5mm;}
    .sch-g4cell{flex:1 1 44%;border:1px solid #c4c4c4;border-radius:3px;padding:3mm;background:#f6f8fb;}
    .sch-g4cell h4{font-size:9.5pt;margin:0 0 1.5mm;}
    .sch-g4cell h4 .sch-g4num{display:inline-block;font-family:'Courier New',monospace;font-size:8pt;
      color:#fff;background:#2f5fa6;padding:0.4mm 1.6mm;border-radius:2px;margin-right:2mm;}
    .sch-g4cell p{font-size:8.5pt;color:#777;margin:0;}
    .sch-tl{display:flex;flex-direction:column;padding-left:6mm;border-left:1.5pt solid #c4c4c4;}
    .sch-tl-item{padding:1.5mm 0;}
    .sch-tl-date{font-family:'Courier New',monospace;font-size:8.5pt;color:#b8791f;font-weight:bold;}
    .sch-tl-label{font-size:9pt;color:#444;}
    .sch-stairs{display:flex;align-items:flex-end;gap:1.5mm;}
    .sch-stair{flex:1;border-radius:2px 2px 0 0;padding:2mm 1mm;color:#fff;text-align:center;
      display:flex;flex-direction:column;justify-content:flex-end;gap:0.6mm;}
    .sch-stair strong{font-family:'Courier New',monospace;font-size:8.5pt;}
    .sch-stair span{font-size:7pt;}
    .sch-matrix{display:grid;grid-template-columns:6mm 1fr 1fr;gap:1.5mm;}
    .sch-mx-q{border:1px solid #c4c4c4;border-radius:3px;padding:2.5mm;font-size:8.5pt;text-align:center;
      display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1mm;background:#f6f8fb;}
    .sch-mx-q strong{font-size:9pt;}
    .sch-mx-y{grid-row:1/3;writing-mode:vertical-rl;transform:rotate(180deg);display:flex;
      align-items:center;justify-content:center;font-size:7.5pt;color:#777;}
    .sch-mx-x{grid-column:2/4;display:flex;align-items:center;justify-content:center;font-size:7.5pt;color:#777;}
    .sch-bmc{display:grid;gap:1.5mm;grid-template-columns:repeat(5,1fr);
      grid-template-areas:"p a v r s" "p k v c s" "co co co re re";}
    .sch-bmc>div{border:1px solid #c4c4c4;border-radius:3px;padding:2mm 1.5mm;font-size:7.5pt;
      background:#f6f8fb;text-align:center;color:#777;}
    .sch-bmc b{display:block;color:#1a1a1a;font-size:8pt;margin-bottom:0.6mm;}
    .sch-bmc .bmc-v{background:#eef3fa;border-color:#2f5fa6;}
    .sch-bmc .bmc-p{grid-area:p;}.sch-bmc .bmc-a{grid-area:a;}.sch-bmc .bmc-k{grid-area:k;}
    .sch-bmc .bmc-v{grid-area:v;}.sch-bmc .bmc-r{grid-area:r;}.sch-bmc .bmc-c{grid-area:c;}
    .sch-bmc .bmc-s{grid-area:s;}.sch-bmc .bmc-co{grid-area:co;}.sch-bmc .bmc-re{grid-area:re;}
    @page{margin:14mm 12mm;}
  `;
}

function m2OpenPrint(title, bodyHTML) {
  var old = document.getElementById('m2-print-frame');
  if (old) old.remove();
  var f = document.createElement('iframe');
  f.id = 'm2-print-frame';
  f.setAttribute('aria-hidden', 'true');
  f.style.cssText = 'position:fixed;left:-9999px;top:0;width:0;height:0;border:0;';
  document.body.appendChild(f);
  var d = f.contentWindow.document;
  d.open();
  d.write('<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><title>'
    + m2Esc(title) + '</title><style>' + m2PdfStyles() + '</style></head><body>'
    + bodyHTML + '</body></html>');
  d.close();
  var done = false;
  var go = function () {
    if (done) return; done = true;
    try { f.contentWindow.focus(); f.contentWindow.print(); }
    catch (e) { alert('Impression impossible : ' + e); }
    setTimeout(function () { f.remove(); }, 2000);
  };
  if (d.readyState === 'complete') setTimeout(go, 400);
  else { f.onload = function () { setTimeout(go, 400); }; setTimeout(go, 1400); }
}

/* Icône + couleur d'accent par cours, pour la page de garde des PDF. */
var M2_COURSE_META = {
  inge_fi:       { icon: '💹', color: '#42795a' },
  gouv:          { icon: '🏛️', color: '#2f5fa6' },
  strat:         { icon: '🎯', color: '#a87a2e' },
  evo_orga:      { icon: '🏢', color: '#a87a2e' },
  conduite_chgt: { icon: '🔄', color: '#3a7a86' },
  rse_csrd:      { icon: '🌱', color: '#42795a' },
};

/* Page de garde stylée, personnalisée selon le cours. docType : « Cours complet »,
   « Schémas », « Annales corrigées », « Examen blanc »… */
function m2PdfCoverPage(docType) {
  var meta = M2_COURSE_META[COURSE_KEY] || { icon: '📘', color: '#2f5fa6' };
  var sub = (window.DATA && DATA.subtitle) ? DATA.subtitle : '';
  var now = new Date().toLocaleDateString('fr-FR', { day: 'numeric', month: 'long', year: 'numeric' });
  return '<div class="pdf-cover" style="border-color:' + meta.color + '">'
    + '<div class="pdf-cover-eyebrow">M2 CCA · Comptabilité Contrôle Audit</div>'
    + '<div class="pdf-cover-icon">' + meta.icon + '</div>'
    + '<div class="pdf-cover-kicker" style="color:' + meta.color + '">' + m2Esc(docType) + '</div>'
    + '<div class="pdf-cover-title">' + m2Esc(m2CourseTitle()) + '</div>'
    + (sub ? '<div class="pdf-cover-sub">' + m2Esc(sub) + '</div>' : '')
    + '<div class="pdf-cover-rule" style="background:' + meta.color + '"></div>'
    + '<div class="pdf-cover-foot">Fiche de révision &middot; Mathieu Belloir<br>' + now + '</div>'
    + '</div>';
}

/* Export du cours : seuls les chapitres VISIBLES (le filtre par axe s'applique). */
function m2ExportCours() {
  var root = document.getElementById('appRoot');
  var chaps = root ? root.querySelectorAll('.course-chapter') : [];
  var body = '';
  Array.prototype.forEach.call(chaps, function (c) {
    if (getComputedStyle(c).display !== 'none') {
      var cl = c.cloneNode(true);
      cl.querySelectorAll('button').forEach(function (e) { e.remove(); });
      cl.style.display = '';
      body += cl.outerHTML;
    }
  });
  if (!body) { alert('Aucun chapitre à exporter pour ce filtre.'); return; }
  m2OpenPrint(m2CourseTitle() + ' - Cours',
    m2PdfCoverPage('Cours complet') + '<div class="pdf-doc">' + body + '</div>');
}

/* Export des schémas : tous les repères visuels du cours. */
function m2ExportSchemas() {
  var root = document.getElementById('appRoot');
  var host = root ? root.querySelector('.fade-up') : null;
  if (!host) { alert('Schémas introuvables.'); return; }
  var cl = host.cloneNode(true);
  cl.querySelectorAll('button, .m2-pdf-bar').forEach(function (e) { e.remove(); });
  m2OpenPrint(m2CourseTitle() + ' - Schémas',
    m2PdfCoverPage('Schémas') + '<div class="pdf-doc">' + cl.innerHTML + '</div>');
}

/* Export des annales : sujets + corrections (corrections dépliées). */
function m2ExportAnnales() {
  var root = document.getElementById('appRoot');
  var host = root ? root.querySelector('.fade-up') : null;
  if (!host) { alert('Annales introuvables.'); return; }
  var cl = host.cloneNode(true);
  cl.querySelectorAll('.annale-correction').forEach(function (e) { e.style.display = 'block'; });
  cl.querySelectorAll('button, .m2-pdf-bar').forEach(function (e) { e.remove(); });
  m2OpenPrint(m2CourseTitle() + ' - Annales',
    m2PdfCoverPage('Annales corrigées') + '<div class="pdf-doc">' + cl.innerHTML + '</div>');
}

/* Export de l'examen blanc (sujet) ou de son corrigé selon l'état en cours. */
function m2ExportExamen() {
  var root = document.getElementById('appRoot');
  if (!root) return;
  var running = root.querySelector('.exam-running');
  var scoreBox = root.querySelector('.score-box');
  var host = running || (scoreBox ? scoreBox.parentNode : null) || root.querySelector('.fade-up');
  if (!host) { alert('Examen introuvable.'); return; }
  var cl = host.cloneNode(true);
  cl.querySelectorAll('button, .m2-pdf-bar, .exam-timer-bar').forEach(function (e) { e.remove(); });
  var suffix = running ? 'Examen blanc' : 'Corrigé de l\'examen blanc';
  m2OpenPrint(m2CourseTitle() + ' - ' + suffix,
    m2PdfCoverPage(suffix) + '<div class="pdf-doc">' + cl.innerHTML + '</div>');
}

/* Détection de la section active et injection du bouton d'export. */
function m2DetectSection(root) {
  if (root.querySelector('.course-chapter')) return 'cours';
  if (root.querySelector('.schema-card')) return 'schemas';
  if (root.querySelector('.exam-running')) return 'examen-blanc';
  if (root.querySelector('.score-box, .exam-result-dossier')) return 'examen-corrige';
  if (root.querySelector('.annale-head')) return 'annales';
  return null;
}

function m2RefreshPdfBar() {
  var root = document.getElementById('appRoot');
  if (!root) return;
  var kind = m2DetectSection(root);
  var existing = document.getElementById('m2-pdf-bar');
  if (!kind) { if (existing) existing.remove(); return; }
  if (existing) {
    if (existing.dataset.kind === kind) return;
    existing.remove();
  }
  var ph = root.querySelector('.page-header');
  if (!ph) return;
  var label, fn, hint = '';
  if (kind === 'cours') {
    label = '⬇ Télécharger le cours (PDF)'; fn = 'm2ExportCours()';
    hint = 'Le filtre par axe sélectionné est appliqué à l\'export.';
  } else if (kind === 'schemas') {
    label = '⬇ Télécharger les schémas (PDF)'; fn = 'm2ExportSchemas()';
    hint = 'Tous les repères visuels du cours.';
  } else if (kind === 'annales') {
    label = '⬇ Télécharger les annales (PDF)'; fn = 'm2ExportAnnales()';
    hint = 'Sujets et corrigés inclus.';
  } else if (kind === 'examen-blanc') {
    label = '⬇ Télécharger l\'examen blanc (PDF)'; fn = 'm2ExportExamen()';
  } else {
    label = '⬇ Télécharger le corrigé (PDF)'; fn = 'm2ExportExamen()';
  }
  var bar = document.createElement('div');
  bar.id = 'm2-pdf-bar';
  bar.className = 'm2-pdf-bar';
  bar.dataset.kind = kind;
  bar.innerHTML = '<button type="button" class="m2-pdf-btn" onclick="' + fn + '">'
    + label + '</button>' + (hint ? '<span class="m2-pdf-hint">' + hint + '</span>' : '');
  ph.insertAdjacentElement('afterend', bar);
}

var m2BarPending = false;
function m2ScheduleBar() {
  if (m2BarPending) return;
  m2BarPending = true;
  requestAnimationFrame(function () { m2BarPending = false; m2RefreshPdfBar(); });
}

function m2InitPdfExport() {
  var root = document.getElementById('appRoot');
  if (!root) return;
  try {
    var obs = new MutationObserver(m2ScheduleBar);
    obs.observe(root, { childList: true, subtree: true });
  } catch (e) { /* navigateur sans MutationObserver : ignoré */ }
  m2RefreshPdfBar();
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', m2InitPdfExport);
} else {
  m2InitPdfExport();
}


/* ═══════════════════════════════════════════════════════════
   COURS — LOGIQUE PARTAGÉE (mutualisée depuis les 6 pages cours)
   Navigation, checklist, flashcards, quiz, deep-link, annales.
   ═══════════════════════════════════════════════════════════ */
function escAnnale(s) {
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
function switchAnnale(idx, btn) {
  document.querySelectorAll('.annale-body-wrap').forEach(el => {
    el.style.display = parseInt(el.dataset.annaleIdx, 10) === idx ? '' : 'none';
  });
  document.querySelectorAll('.annale-tab').forEach(b => b.classList.remove('active'));
  if (btn) btn.classList.add('active');
  // Collapse toutes les corrections de l'annale qu'on quitte pour repartir propre
  document.querySelectorAll('.annale-correction').forEach(el => { el.style.display = 'none'; });
  document.querySelectorAll('.annale-show-corr').forEach(b => { b.textContent = '▸ Afficher la correction'; b.classList.remove('open'); });
}
function getFilteredFlashcards() {
  if (fcTheme === 'all') return DATA.flashcards.map((_, i) => i);
  return DATA.flashcards.map((fc, i) => fc.theme === fcTheme ? i : -1).filter(i => i >= 0);
}
function getFilteredQuizQuestions() {
  if (quizTheme === 'all') return DATA.quizQuestions;
  return DATA.quizQuestions.filter(q => q.theme === quizTheme);
}
function setFcTheme(id) { fcTheme = id; switchTab('flash'); }
function setQuizTheme(id) { quizTheme = id; switchTab('quiz'); }
function setCoursTheme(id) { coursTheme = id; applyCoursFilter(); renderCoursPills(); }
function setQuizCount(n) {
  quizCount = n;
  document.querySelectorAll('.quiz-count-btn').forEach(b => b.classList.toggle('active', Number(b.dataset.n) === n));
  const p = document.querySelector('.quiz-setup p');
  if (p) {
    const fq = getFilteredQuizQuestions();
    p.textContent = Math.min(quizCount, fq.length) + ' questions tirées au sort sur ' + fq.length + (quizTheme !== 'all' ? ' (thème filtré)' : '');
  }
}
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
  const host = document.getElementById('coursThemeSelectorWrap');
  if (host) host.innerHTML = themeSelectorHTML('cours');
}
function themeSelectorHTML(scope) {
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
}
function switchTab(id) {
  currentTab = id;
  renderNav();
  removeScrollSpy();
  const t = TABS.find(t => t.id === id);
  document.getElementById('progressFill').style.width = (t ? t.prog : 0) + '%';
  renderTab(id);
  window.scrollTo({ top: 0, behavior: 'smooth' });
}
function renderNav() {
  document.getElementById('navTabs').innerHTML = TABS.map(t =>
    `<button class="nav-tab${t.id === currentTab ? ' active' : ''}" onclick="switchTab('${t.id}')">${t.label}</button>`
  ).join('');
}
function renderTab(id) {
  const root = document.getElementById('appRoot');
  const header = `
    <div class="page-header">
      <button class="back-home" onclick="window.location.href='index.html'">← Accueil</button>
      <div class="page-title">${DATA.title}</div>
      <div class="page-subtitle">${DATA.subtitle}</div>
    </div>`;
  if (id === 'checklist') root.innerHTML = header + renderChecklist();
  else if (id === 'cours') {
    root.innerHTML = header + `<div class="fade-up"><div id="coursThemeSelectorWrap"></div>${getCoursHTML()}<div id="coursEmpty" class="cours-empty" style="display:none">Aucun chapitre dans cet axe pour ce cours.</div></div>`;
    document.getElementById('coursThemeSelectorWrap').innerHTML = themeSelectorHTML('cours');
    applyCoursFilter();
    setTimeout(() => buildScrollSpy('.main', '.course-chapter:not([style*="display: none"]) h2'), 100);
    if (window._pendingCoursJump) { window._pendingCoursJump(); window._pendingCoursJump = null; }
  }
  else if (id === 'synth') root.innerHTML = header + `<div class="fade-up fade-up-stagger">${getSynthHTML()}</div>`;
  else if (id === 'schemas') root.innerHTML = header + `<div class="fade-up fade-up-stagger">${getSchemasHTML()}</div>`;
  else if (id === 'flash') { root.innerHTML = header + renderFlash(); bindFlash(); }
  else if (id === 'quiz')  { root.innerHTML = header + renderQuizSetup(); }
  else if (id === 'annales'){ root.innerHTML = header + `<div class="fade-up fade-up-stagger">${getAnnalesHTML()}</div>`; }
  else if (id === 'sujets') { root.innerHTML = header + renderSujetsTypes(); }
  else if (id === 'examen') { renderExamen(); }
}
function parseDeepLink() {
  const h = window.location.hash || '';
  if (!h) return null;
  const out = {};
  // Format 1 : #chap-3
  let m = h.match(/^#chap-(\d+)$/);
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
  const re = new RegExp('(' + word.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');
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
function renderChecklist() {
  const items = DATA.checklistItems;
  const total = items.length;
  const done = items.filter(i => isChecked(COURSE_KEY + ':' + i.id)).length;
  const pct = total ? Math.round(done / total * 100) : 0;
  saveCourseProgress(COURSE_KEY, done, total);
  const r = 54, circ = 2 * Math.PI * r;
  const offset = circ - (pct / 100) * circ;

  return `
  <div class="cl-progress-wrap fade-up">
    <div style="position:relative;width:140px;height:140px;margin:0 auto">
      <svg width="140" height="140" viewBox="0 0 140 140" class="cl-ring-svg" aria-label="Progression ${pct}%">
        <defs>
          <linearGradient id="ringGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="var(--accent)"/>
            <stop offset="100%" stop-color="var(--copper)"/>
          </linearGradient>
        </defs>
        <circle cx="70" cy="70" r="${r}" fill="none" stroke="var(--bg3)" stroke-width="10"/>
        <circle cx="70" cy="70" r="${r}" fill="none" stroke="url(#ringGrad)" stroke-width="10"
          stroke-linecap="round" stroke-dasharray="${circ.toFixed(1)}" stroke-dashoffset="${offset.toFixed(1)}"
          style="transition:stroke-dashoffset 0.8s cubic-bezier(0.34,1.56,0.64,1)"/>
      </svg>
      <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center">
        <div style="font-family:'JetBrains Mono',monospace;font-size:1.6rem;font-weight:700;color:var(--text)">${pct}%</div>
        <div style="font-size:0.7rem;color:var(--text3);margin-top:2px">${done}/${total} points</div>
      </div>
    </div>
    <div style="margin-top:1.5rem;font-family:'Playfair Display',serif;font-size:1rem;color:var(--text2)">Progression du cours</div>
  </div>
  <div class="checklist-list fade-up-stagger">
    ${items.map(i => { const cid = COURSE_KEY + ':' + i.id, ck = isChecked(cid); return `
      <div class="cl-item${ck ? ' done' : ''}" data-id="${cid}" role="checkbox" aria-checked="${ck}" tabindex="0" onclick="handleCheck('${cid}')" onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();handleCheck('${cid}');}">
        <div class="cl-box">${ck ? '✓' : ''}</div>
        <span class="cl-label">${i.label}</span>
      </div>`; }).join('')}
  </div>`;
}
function handleCheck(id) {
  toggleCheck(id);
  switchTab('checklist');
}
function initFlashcards() {
  fcSRS = loadSRS(DATA.quizKey);
  const allowedIdx = new Set(getFilteredFlashcards());
  const total = allowedIdx.size;
  if (fcSRSMode === 'srs') {
    fcQueue = srsBuildQueue(fcSRS, DATA.flashcards.length).filter(i => allowedIdx.has(i)).slice(0, SRS_SESSION_MAX);
    if (fcQueue.length === 0) {
      fcQueue = shuffle([...allowedIdx]).slice(0, SRS_SESSION_MAX);
    }
  } else {
    fcQueue = shuffle([...allowedIdx]);
  }
  fcSessionSize = fcQueue.length;
  fcKnown = []; fcFlipped = false; fcStreak = 0;
}
function renderFlash() {
  initFlashcards();
  return buildFlashHTML();
}
function buildFlashHTML() {
  const total = DATA.flashcards.length;
  const knownCount = fcKnown.length;
  const pct = fcSessionSize > 0 ? Math.round(knownCount / fcSessionSize * 100) : 0;
  const stats = srsGetStats(fcSRS, total);

  if (fcQueue.length === 0) {
    launchConfetti();
    return `
    <div class="fade-up">
      <div class="fc-done">
        <div style="font-size:3rem;margin-bottom:0.5rem">🎉</div>
        <div class="fc-done-title">Toutes les cartes maîtrisées !</div>
        <p style="color:var(--text2);margin:0.5rem 0 1rem">${total}/${total} cartes — Score parfait</p>
        <button class="fc-reset-btn" onclick="resetFlash()">↺ Recommencer</button>
      </div>
    </div>`;
  }

  const card = DATA.flashcards[fcQueue[0]];
  const streakHTML = fcStreak >= 2 ? `<span class="fc-streak">🔥 ${fcStreak} d'affilée</span>` : '';
  return `
  <div class="fade-up">
    ${themeSelectorHTML('flash')}
    <div class="fc-header">
      <div class="fc-progress-bar">
        <div class="fc-pb-label">${knownCount} / ${fcSessionSize} en session · ${stats.learned}/${stats.total} maîtrisées${stats.due > 0 && fcSRSMode==='srs' ? ` · <span style=\"color:var(--orange)\">${stats.due} dues</span>` : ''} ${streakHTML}</div>
        <div class="fc-pb-track"><div class="fc-pb-fill" style="width:${pct}%"></div></div>
      </div>
      <div class="fc-shortcuts">${fcSRSMode === 'srs' ? '🧠 SRS' : '🔀 Mélangé'} · <span onclick="toggleSRSMode()" style="cursor:pointer;text-decoration:underline">basculer</span></div>
    </div>
    <div class="fc-counter">Carte ${fcKnown.length + 1} sur ${total} — ${fcQueue.length} restante(s)</div>
    <div class="flashcard-container">
      <div class="flashcard${fcFlipped ? ' flipped' : ''}" id="fcCard" role="button" tabindex="0" aria-label="Carte de révision — cliquer ou Espace pour retourner" onclick="flipCard()" onkeydown="if(event.key==='Enter'){event.preventDefault();flipCard();}">
        <div class="flashcard-face flashcard-front">
          <div class="flashcard-q">${card.q}</div>
          <div class="flashcard-hint">Cliquez pour révéler la réponse</div>
        </div>
        <div class="flashcard-face flashcard-back">
          <div class="flashcard-a">${card.a}</div>
        </div>
      </div>
    </div>
    <div class="fc-actions">
      <button class="fc-btn-review" onclick="markReview()" title="Raccourci : ←">
        <span class="fc-btn-lbl">✗ À revoir</span>
        <span class="fc-btn-iv">${srsFormatInterval(srsPreviewInterval(fcSRS[fcQueue[0]], 'again'))}</span>
      </button>
      <button class="fc-btn-known" onclick="markKnown()" title="Raccourci : ↓">
        <span class="fc-btn-lbl">✓ Bien</span>
        <span class="fc-btn-iv">${srsFormatInterval(srsPreviewInterval(fcSRS[fcQueue[0]], 'good'))}</span>
      </button>
      <button class="fc-btn-easy" onclick="markEasy()" title="Raccourci : →">
        <span class="fc-btn-lbl">★ Facile</span>
        <span class="fc-btn-iv">${srsFormatInterval(srsPreviewInterval(fcSRS[fcQueue[0]], 'easy'))}</span>
      </button>
    </div>
    <div style="text-align:center;margin-top:0.6rem">
      <button class="fc-btn-skip" onclick="skipCard()" title="Passer cette carte sans la noter">↪ Passer (sans noter)</button>
    </div>
    <div style="text-align:center;margin-top:1rem">
      <button class="fc-reset-btn" onclick="resetFlash()">↺ Réinitialiser</button>
    </div>
  </div>`;
}
function flipCard() {
  fcFlipped = !fcFlipped;
  const card = document.getElementById('fcCard');
  if (card) card.classList.toggle('flipped', fcFlipped);
}
function markKnown() {
  if (!fcQueue.length) return;
  const idx = fcQueue.shift();
  fcSRS[idx] = srsScheduleCard(fcSRS[idx], 'good');
  saveSRS(DATA.quizKey, fcSRS);
  fcKnown.push(idx); fcStreak++; fcFlipped = false; rerenderFlash();
}
function markReview() {
  if (!fcQueue.length) return;
  const idx = fcQueue.shift();
  fcSRS[idx] = srsScheduleCard(fcSRS[idx], 'again');
  saveSRS(DATA.quizKey, fcSRS);
  fcQueue.push(idx); fcStreak = 0; fcFlipped = false; rerenderFlash();
}
function markEasy() {
  if (!fcQueue.length) return;
  const idx = fcQueue.shift();
  fcSRS[idx] = srsScheduleCard(fcSRS[idx], 'easy');
  saveSRS(DATA.quizKey, fcSRS);
  fcKnown.push(idx); fcStreak++; fcFlipped = false; rerenderFlash();
}
function skipCard() {
  if (!fcQueue.length) return;
  fcQueue.push(fcQueue.shift()); fcFlipped = false; rerenderFlash();
}
function toggleSRSMode() {
  fcSRSMode = (fcSRSMode === 'srs') ? 'shuffle' : 'srs';
  switchTab('flash');
}
function resetFlash() { initFlashcards(); rerenderFlash(); }
function rerenderFlash() {
  const ctx = { fcQueue, fcKnown, fcStreak, fcSRS, fcSRSMode, fcSessionSize };
  if (updateFlashCardPartial(DATA, ctx)) return;
  const root = document.getElementById('appRoot');
  const header = root.querySelector('.page-header') ? root.querySelector('.page-header').outerHTML : '';
  root.innerHTML = header + buildFlashHTML();
}
function bindFlash() { document.addEventListener('keydown', fcKeyHandler); }
function fcKeyHandler(e) {
  if (currentTab !== 'flash') { document.removeEventListener('keydown', fcKeyHandler); return; }
  if (e.code === 'Space') { e.preventDefault(); flipCard(); }
  else if (e.code === 'ArrowLeft') { if (fcQueue.length > 0) markReview(); }
  else if (e.code === 'ArrowDown') { e.preventDefault(); if (fcQueue.length > 0) markKnown(); }
  else if (e.code === 'ArrowRight') { if (fcQueue.length > 0) markEasy(); }
  else if (e.code === 'Tab' || e.code === 'KeyS') { e.preventDefault(); if (fcQueue.length > 0) skipCard(); }
}
function renderQuizSetup() {
  const scores = loadQuizScores(DATA.quizKey).slice(0, 3);
  const histHTML = scores.length === 0
    ? '<p style="color:var(--text3);font-size:0.82rem">Aucune partie précédente</p>'
    : scores.map(s => {
        const pct = Math.round(s.score / s.total * 100);
        const d = new Date(s.date);
        const ds = d.toLocaleDateString('fr-FR',{day:'2-digit',month:'2-digit'}) + ' ' + d.toLocaleTimeString('fr-FR',{hour:'2-digit',minute:'2-digit'});
        const col = pct >= 75 ? 'var(--green)' : pct >= 50 ? 'var(--orange)' : 'var(--red)';
        return `<span class="quiz-score-pill"><span style="color:${col};font-weight:700">${s.score}/${s.total}</span><span style="color:var(--text3)">${ds}</span></span>`;
      }).join('');

  const filteredQuiz = getFilteredQuizQuestions();
  const quizSize = Math.min(quizCount, filteredQuiz.length);
  return `
  <div class="fade-up">
    ${themeSelectorHTML('quiz')}
    <div class="quiz-setup">
      <div style="font-size:2rem;margin-bottom:0.5rem">🎯</div>
      <h3>Quiz — ${DATA.title}</h3>
      <p>${quizSize} questions tirées au sort sur ${filteredQuiz.length}${quizTheme !== 'all' ? ' (thème filtré)' : ''}</p>
      <div class="quiz-count">
        <span class="quiz-count-label">Nombre de questions</span>
        <div class="quiz-count-opts">
          ${[5, 10, 20].map(n => `<button class="quiz-count-btn${quizCount === n ? ' active' : ''}" data-n="${n}" onclick="setQuizCount(${n})">${n}</button>`).join('')}
        </div>
      </div>
      <div class="quiz-history">
        <div class="quiz-history-title">Progression des scores</div>
        ${sparklineHTML(loadQuizScores(DATA.quizKey))}
        ${histHTML}
      </div>
      <div id="timerToggle" class="quiz-timer-toggle" onclick="toggleTimer()">
        <span>⏱</span> Timer 30s par question
      </div>
      <br>
      <button class="start-btn" onclick="startQuiz()">Lancer le quiz</button>
    </div>
  </div>`;
}
function toggleTimer() {
  const el = document.getElementById('timerToggle');
  if (!el) return;
  const on = el.classList.toggle('on');
  el._timerOn = on;
  if (quizState) quizState.timerEnabled = on;
}
function startQuiz() {
  const timerEl = document.getElementById('timerToggle');
  const timerOn = timerEl ? !!timerEl._timerOn : false;
  const pool = getFilteredQuizQuestions();
  quizState = {
    questions: shuffle([...pool]).slice(0, Math.min(quizCount, pool.length)).map(quizShuffleQuestion),
    current: 0,
    answers: [],
    timerEnabled: timerOn,
    errors: []
  };
  renderQuizQuestion();
}
function renderQuizQuestion() {
  if (!quizState || quizState.current >= quizState.questions.length) { showQuizResult(); return; }
  clearInterval(timerInterval);
  timeLeft = 30;
  if (updateQuizQuestionPartial(quizState)) {
    if (quizState.timerEnabled) {
      const fill = document.getElementById('timerFill');
      if (fill) { fill.style.width = '100%'; fill.classList.remove('warn'); }
      const label = document.getElementById('timerLabel');
      if (label) label.textContent = timeLeft + 's';
      startQuestionTimer(quizState.current);
    }
    return;
  }
  const qi = quizState.current;
  const q = quizState.questions[qi];
  const total = quizState.questions.length;
  const letters = ['A','B','C','D'];
  const timerBar = quizState.timerEnabled ? `<div class="quiz-timer-bar"><div class="quiz-timer-fill" id="timerFill" style="width:100%"></div></div>` : '';
  const timerLabel = quizState.timerEnabled ? `<span style="font-family:'JetBrains Mono',monospace;color:var(--cyan);font-size:0.78rem" id="timerLabel">${timeLeft}s</span>` : '';

  const root = document.getElementById('appRoot');
  root.innerHTML = `
  <div class="page-header">
    <button class="back-home" onclick="window.location.href='index.html'">← Accueil</button>
    <div class="page-title">${DATA.title}</div>
    <div class="page-subtitle">${DATA.subtitle}</div>
  </div>
  <div class="fade-up">
    <div class="quiz-progress">
      <span>Question ${qi + 1} / ${total}</span>
      ${timerLabel}
    </div>
    ${timerBar}
    <div class="quiz-global-bar"><div class="quiz-global-fill" style="width:${Math.round((qi/total)*100)}%"></div></div>
    <div class="quiz-card" id="quizCard">${q.type === 'tf' ? '' : `
      <div class="quiz-q-num">Q${qi + 1}</div>
      <div class="quiz-q-text">${q.q}</div>
      <div class="quiz-options" id="quizOpts">
        ${q.o.map((opt, i) => `
          <button class="quiz-option" data-i="${i}" onclick="selectAnswer(event, ${qi}, ${i})">
            <div class="opt-letter">${letters[i]}</div>
            <span>${opt}</span>
          </button>`).join('')}
      </div>`}
    </div>
  </div>`;

  if (q.type === 'tf') renderTFQuestionInline(document.getElementById('quizCard'), q, qi, quizState);
  document.querySelectorAll('.quiz-option').forEach(attachRipple);

  if (quizState.timerEnabled) startQuestionTimer(qi);
}
function startQuestionTimer(qi) {
  timeLeft = 30;
  const fill = document.getElementById('timerFill');
  const label = document.getElementById('timerLabel');
  clearInterval(timerInterval);
  timerInterval = setInterval(() => {
    timeLeft--;
    if (fill) {
      fill.style.width = (timeLeft / 30 * 100) + '%';
      if (timeLeft <= 10) fill.classList.add('warn');
    }
    if (label) label.textContent = timeLeft + 's';
    if (timeLeft <= 0) { clearInterval(timerInterval); autoWrong(qi); }
  }, 1000);
}
function autoWrong(qi) {
  if (!quizState || quizState.answers[qi] !== undefined) return;
  quizState.answers[qi] = -1;
  quizState.errors.push({ qi, chosen: -1 });
  const opts = document.querySelectorAll('.quiz-option');
  opts.forEach(o => o.classList.add('disabled'));
  const q = quizState.questions[qi];
  if (opts[q.c]) opts[q.c].classList.add('correct');
  document.getElementById('quizCard').classList.add('shake');
  showExplanation(q, true, qi);
}
function selectAnswer(ev, qi, chosen) {
  if (!quizState || quizState.answers[qi] !== undefined) return;
  clearInterval(timerInterval);
  quizState.answers[qi] = chosen;
  const q = quizState.questions[qi];
  const correct = chosen === q.c;
  if (!correct) quizState.errors.push({ qi, chosen });
  const opts = document.querySelectorAll('.quiz-option');
  opts.forEach(o => o.classList.add('disabled'));
  opts[q.c].classList.add('correct');
  opts[q.c].classList.add('correct-highlight');
  if (!correct) {
    if (opts[chosen]) opts[chosen].classList.add('wrong');
    document.getElementById('quizCard').classList.add('shake');
    setTimeout(() => document.getElementById('quizCard')?.classList.remove('shake'), 500);
  }
  showExplanation(q, !correct, qi);
}
function showExplanation(q, wrong, qi) {
  const card = document.getElementById('quizCard');
  if (!card) return;
  const expl = document.createElement('div');
  expl.className = 'quiz-expl';
  expl.textContent = q.e;
  card.appendChild(expl);
  const nextBtn = document.createElement('button');
  nextBtn.className = 'quiz-next-btn';
  const isLast = quizState.current >= quizState.questions.length - 1;
  nextBtn.textContent = isLast ? 'Voir les résultats →' : 'Question suivante →';
  nextBtn.onclick = () => { quizState.current++; renderQuizQuestion(); };
  card.appendChild(nextBtn);
}
function showQuizResult() {
  clearInterval(timerInterval);
  const total = quizState.questions.length;
  const score = quizState.answers.filter((a, i) => isQuestionCorrect(quizState.questions[i], a)).length;
  saveQuizScore(DATA.quizKey, score, total);
  const pct = Math.round(score / total * 100);
  const emoji = pct >= 90 ? '🏆' : pct >= 75 ? '🎉' : pct >= 50 ? '👍' : '💪';
  const msg = pct >= 90 ? 'Excellent !' : pct >= 75 ? 'Très bien !' : pct >= 50 ? 'Bien !' : 'Continue tes efforts !';
  if (pct >= 90) launchConfetti();

  const errorsHTML = quizState.errors.length === 0
    ? '<p style="color:var(--green);text-align:center;margin-top:1rem">Aucune erreur — parfait !</p>'
    : `<div class="errors-list">
        <div style="font-size:0.78rem;text-transform:uppercase;letter-spacing:1px;color:var(--text3);font-family:'JetBrains Mono',monospace;margin-bottom:0.7rem">Erreurs à revoir</div>
        ${quizState.errors.map(err => {
          const q = quizState.questions[err.qi];
          const yourAns = q.type === 'tf' ? '' : (err.chosen >= 0 && q.o ? q.o[err.chosen] : 'Pas de réponse');
          return `<div class="error-item"><div class="eq">${q.q}</div>${yourAns ? `<div class="ea-wrong">✗ Ta réponse : ${yourAns}</div>` : ''}<div class="ea">${formatCorrectAnswerHTML(q)}</div>${q.e ? `<div class="ea-expl">${q.e}</div>` : ''}</div>`;
        }).join('')}
      </div>`;

  const root = document.getElementById('appRoot');
  root.innerHTML = `
  <div class="page-header">
    <button class="back-home" onclick="window.location.href='index.html'">← Accueil</button>
    <div class="page-title">${DATA.title}</div>
    <div class="page-subtitle">${DATA.subtitle}</div>
  </div>
  <div class="fade-up">
    <div class="score-box">
      <div class="score-emoji">${emoji}</div>
      <div class="score-num" id="scoreNum">0/${total}</div>
      <div class="score-label">${msg} · ${pct}%</div>
      <div class="score-actions">
        <button class="btn-secondary" onclick="switchTab('quiz')">↺ Relancer</button>
        <button class="btn-primary" id="errBtn" onclick="toggleErrors()">${quizState.errors.length > 0 ? 'Voir les erreurs' : "Pas d'erreurs"}</button>
        ${quizState.errors.length > 0 ? `<button class="btn-secondary" onclick="replayErrors()">↻ Rejouer mes ${quizState.errors.length} erreur${quizState.errors.length > 1 ? 's' : ''}</button>` : ''}
      </div>
      <div id="errSection" style="display:none">${errorsHTML}</div>
    </div>
  </div>`;

  const el = document.getElementById('scoreNum');
  const start = Date.now();
  const dur = 1500;
  (function tick() {
    const t = Math.min((Date.now() - start) / dur, 1);
    const ease = 1 - Math.pow(1 - t, 3);
    el.textContent = Math.round(ease * score) + '/' + total;
    if (t < 1) requestAnimationFrame(tick);
  })();
}
function toggleErrors() {
  const sec = document.getElementById('errSection');
  const btn = document.getElementById('errBtn');
  if (!sec) return;
  const visible = sec.style.display !== 'none';
  sec.style.display = visible ? 'none' : 'block';
  if (btn) btn.textContent = visible ? 'Voir les erreurs' : 'Masquer les erreurs';
}
