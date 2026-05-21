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
    *{box-sizing:border-box;}
    html,body{margin:0;padding:0;background:#fff;color:#1a1a1a;
      font-family:Georgia,'Times New Roman',serif;font-size:11.5pt;line-height:1.5;}
    .pdf-doc{padding:0 2mm;}
    .pdf-h1{font-size:20pt;color:#2f5fa6;margin:0 0 2mm;border-bottom:2px solid #2f5fa6;padding-bottom:2mm;}
    .pdf-sub{color:#555;font-size:10pt;margin:0 0 2mm;font-style:italic;}
    .pdf-meta{color:#777;font-size:8.5pt;margin:0 0 6mm;}
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

function m2PdfHeader(suffix, meta) {
  var t = m2CourseTitle();
  var sub = (window.DATA && DATA.subtitle) ? '<p class="pdf-sub">' + m2Esc(DATA.subtitle) + '</p>' : '';
  return '<div class="pdf-h1">' + m2Esc(t) + ' — ' + m2Esc(suffix) + '</div>' + sub
    + '<p class="pdf-meta">M2 CCA · ' + m2Esc(meta) + '</p>';
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
    '<div class="pdf-doc">' + m2PdfHeader('Cours', 'Fiche de révision') + body + '</div>');
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
    '<div class="pdf-doc">' + m2PdfHeader('Annales', 'Sujets et corrigés') + cl.innerHTML + '</div>');
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
  var meta = running ? 'Sujet généré' : 'Sujet corrigé';
  m2OpenPrint(m2CourseTitle() + ' - ' + suffix,
    '<div class="pdf-doc">' + m2PdfHeader(suffix, meta) + cl.innerHTML + '</div>');
}

/* Détection de la section active et injection du bouton d'export. */
function m2DetectSection(root) {
  if (root.querySelector('.course-chapter')) return 'cours';
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
