<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
  <meta name="theme-color" content="#080c14" />
  <meta name="apple-mobile-web-app-capable" content="yes" />
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
  <meta name="apple-mobile-web-app-title" content="ReviewPro" />
  <meta name="description" content="نظام ذكي لإدارة تقييمات Google Maps للعيادات الطبية" />

  <!-- PWA -->
  <link rel="manifest" href="/manifest.json" />
  <link rel="apple-touch-icon" href="/icons/icon-192.png" />

  <!-- Open Graph -->
  <meta property="og:title" content="ReviewPro - إدارة تقييمات العيادات" />
  <meta property="og:description" content="نظام ذكي بالذكاء الاصطناعي لتحسين تقييمات Google Maps" />
  <meta property="og:type" content="website" />

  <title>ReviewPro ⭐</title>

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <!-- Google Places API (New) - REST based, no CORS issues -->
  <script>
    function loadGoogleMaps() { /* REST API - no script needed */ }
    window.addEventListener('DOMContentLoaded', loadGoogleMaps);
  </script>
  <link href="https://fonts.googleapis.com/css2?family=Almarai:wght@300;400;700;800&family=IBM+Plex+Mono:wght@500&display=swap" rel="stylesheet" />

  <style>
    :root {
      --bg: #080c14;
      --bg2: #0d1117;
      --bg3: #111827;
      --border: rgba(255,255,255,0.07);
      --border2: rgba(255,255,255,0.12);
      --text: #e2e8f0;
      --text2: #94a3b8;
      --text3: #475569;
      --blue: #0ea5e9;
      --blue2: #38bdf8;
      --green: #10b981;
      --green2: #34d399;
      --yellow: #f59e0b;
      --red: #ef4444;
      --safe-top: env(safe-area-inset-top, 0px);
      --safe-bottom: env(safe-area-inset-bottom, 0px);
    }
    * { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }
    html, body { height: 100%; overflow: hidden; }
    body {
      font-family: 'Almarai', sans-serif;
      background: var(--bg);
      color: var(--text);
      overscroll-behavior: none;
    }
    #app { height: 100%; display: flex; flex-direction: column; }

    /* ── SCROLLABLE AREA ── */
    .page { flex: 1; overflow-y: auto; -webkit-overflow-scrolling: touch; padding-bottom: calc(80px + var(--safe-bottom)); }
    .page::-webkit-scrollbar { display: none; }

    /* ── TOP BAR ── */
    .topbar {
      padding: calc(var(--safe-top) + 12px) 16px 12px;
      background: rgba(8,12,20,0.97);
      border-bottom: 1px solid var(--border);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      position: sticky; top: 0; z-index: 100;
      display: flex; align-items: center; gap: 12px;
    }
    .topbar-title { flex: 1; }
    .topbar-title h1 { font-size: 17px; font-weight: 800; color: var(--text); }
    .topbar-title p { font-size: 11px; color: var(--text3); margin-top: 1px; }
    .logo { width: 36px; height: 36px; border-radius: 10px; background: linear-gradient(135deg, var(--blue), #0284c7); display: flex; align-items: center; justify-content: center; font-size: 18px; flex-shrink: 0; }

    /* ── BOTTOM NAV ── */
    .bottom-nav {
      position: fixed; bottom: 0; left: 0; right: 0;
      padding: 10px 0 calc(10px + var(--safe-bottom));
      background: rgba(8,12,20,0.97);
      border-top: 1px solid var(--border);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      display: flex; z-index: 100;
    }
    .nav-btn { flex: 1; display: flex; flex-direction: column; align-items: center; gap: 3px; padding: 6px 4px; cursor: pointer; border: none; background: none; color: var(--text3); font-family: 'Almarai', sans-serif; font-size: 10px; font-weight: 700; transition: color .2s; }
    .nav-btn.active { color: var(--blue2); }
    .nav-btn .nav-icon { font-size: 20px; }

    /* ── CARDS ── */
    .card { background: rgba(255,255,255,0.03); border: 1px solid var(--border); border-radius: 16px; }
    .card-blue { background: rgba(56,189,248,0.05); border: 1px solid rgba(56,189,248,0.15); border-radius: 16px; }
    .card-green { background: rgba(16,185,129,0.05); border: 1px solid rgba(16,185,129,0.15); border-radius: 16px; }

    /* ── INPUTS ── */
    .inp { width: 100%; padding: 12px 14px; border-radius: 10px; border: 1px solid rgba(255,255,255,0.1); background: rgba(255,255,255,0.05); color: var(--text); font-family: 'Almarai', sans-serif; font-size: 15px; transition: all .2s; resize: none; }
    .inp:focus { border-color: var(--blue); background: rgba(14,165,233,0.07); }
    .inp::placeholder { color: var(--text3); }
    select.inp { appearance: none; cursor: pointer; }
    select.inp option { background: var(--bg2); }

    /* ── BUTTONS ── */
    .btn { padding: 13px 20px; border-radius: 12px; border: none; cursor: pointer; font-family: 'Almarai', sans-serif; font-size: 15px; font-weight: 700; transition: all .2s; display: flex; align-items: center; justify-content: center; gap: 8px; }
    .btn:active { transform: scale(0.97); }
    .btn-primary { background: linear-gradient(135deg, #0ea5e9, #0284c7); color: #fff; box-shadow: 0 4px 15px rgba(14,165,233,0.25); }
    .btn-primary:disabled { opacity: .5; cursor: not-allowed; transform: none; }
    .btn-ghost { background: rgba(255,255,255,0.05); color: var(--text2); border: 1px solid var(--border); }
    .btn-sm { padding: 7px 14px; font-size: 12px; border-radius: 8px; }
    .btn-full { width: 100%; }

    /* ── TAGS ── */
    .tag { display: inline-block; padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 700; }
    .tag-green { background: rgba(52,211,153,0.12); color: var(--green2); border: 1px solid rgba(52,211,153,0.2); }
    .tag-red { background: rgba(248,113,113,0.12); color: #f87171; border: 1px solid rgba(248,113,113,0.2); }
    .tag-yellow { background: rgba(251,191,36,0.12); color: #fbbf24; border: 1px solid rgba(251,191,36,0.2); }
    .tag-blue { background: rgba(56,189,248,0.12); color: var(--blue2); border: 1px solid rgba(56,189,248,0.2); }

    /* ── RESULT BOXES ── */
    .result { padding: 16px; border-radius: 12px; font-size: 14px; line-height: 1.9; white-space: pre-wrap; color: #cbd5e1; animation: fadeUp .3s ease; }
    .streaming-cursor::after { content: '▋'; animation: blink .7s infinite; color: var(--blue2); }
    @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }
    .stream-box { padding: 16px; border-radius: 14px; background: rgba(14,165,233,0.04); border: 1px solid rgba(14,165,233,0.15); font-size: 13px; line-height: 1.9; color: var(--text2); white-space: pre-wrap; min-height: 60px; }
    .result-green { background: rgba(16,185,129,0.05); border: 1px solid rgba(16,185,129,0.15); }
    .result-blue { background: rgba(56,189,248,0.05); border: 1px solid rgba(56,189,248,0.15); }

    /* ── STEP TABS ── */
    .steps { display: flex; overflow-x: auto; gap: 0; border-bottom: 1px solid var(--border); }
    .steps::-webkit-scrollbar { display: none; }
    .step-tab { flex-shrink: 0; padding: 10px 14px; font-size: 12px; font-weight: 700; cursor: pointer; background: none; border: none; border-bottom: 2px solid transparent; font-family: 'Almarai', sans-serif; color: var(--text3); white-space: nowrap; transition: all .2s; }
    .step-tab.active { color: var(--blue2); border-bottom-color: var(--blue2); }

    /* ── CLINIC CARD ── */
    .clinic-row { padding: 14px 16px; border-radius: 12px; border: 1px solid var(--border); background: rgba(255,255,255,0.02); cursor: pointer; transition: all .2s; margin-bottom: 10px; }
    .clinic-row:active, .clinic-row.active { border-color: rgba(56,189,248,0.3); background: rgba(56,189,248,0.04); }

    /* ── STARS ── */
    .star-row { display: flex; gap: 6px; }
    .star { font-size: 26px; cursor: pointer; transition: transform .1s; user-select: none; }
    .star:active { transform: scale(1.3); }

    /* ── INSTALL BANNER ── */
    #install-banner { display: none; margin: 12px 16px 0; padding: 14px 16px; border-radius: 14px; background: linear-gradient(135deg, rgba(14,165,233,0.1), rgba(2,132,199,0.08)); border: 1px solid rgba(14,165,233,0.25); align-items: center; gap: 12px; }
    #install-banner.show { display: flex; }

    /* ── SPINNER ── */
    .spinner { width: 18px; height: 18px; border: 2px solid rgba(255,255,255,0.15); border-top-color: var(--blue2); border-radius: 50%; animation: spin .7s linear infinite; }

    /* ── EMPTY STATE ── */
    .empty { text-align: center; padding: 48px 20px; }
    .empty .icon { font-size: 48px; margin-bottom: 14px; }
    .empty h3 { font-size: 16px; color: var(--text2); margin-bottom: 8px; }
    .empty p { font-size: 13px; color: var(--text3); }

    /* ── SECTION LABEL ── */
    .lbl { display: block; color: var(--text3); font-size: 12px; font-weight: 700; margin-bottom: 7px; letter-spacing: .5px; }

    /* ── DIVIDER ── */
    .divider { height: 1px; background: var(--border); margin: 18px 0; }

    /* ── STAT GRID ── */
    .stat-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
    .stat-box { text-align: center; padding: 12px 8px; border-radius: 12px; background: rgba(255,255,255,0.03); border: 1px solid var(--border); }
    .stat-num { font-size: 22px; font-weight: 800; }
    .stat-lbl { font-size: 10px; color: var(--text3); margin-top: 3px; }

    /* ── ANIMATIONS ── */
    @keyframes fadeUp { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes slideIn { from { opacity:0; transform:translateX(8px); } to { opacity:1; transform:translateX(0); } }
    @keyframes spin { to { transform: rotate(360deg); } }
    @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.4} }
    @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }
    .streaming-cursor::after { content:'▋'; animation:blink .7s infinite; color:var(--blue2); margin-right:2px; }
    .btn-primary:not(:disabled):hover { filter: brightness(1.1); box-shadow: 0 6px 20px rgba(14,165,233,0.35); }
    .clinic-row:hover { border-color: rgba(56,189,248,0.3); background: rgba(56,189,248,0.04); }
    .review-item { animation: slideIn .2s ease; }
    .pulsing { animation: pulse 1.5s infinite; }

    /* ── REVIEW ITEM ── */
    .review-item { background: rgba(255,255,255,0.03); border: 1px solid var(--border); border-radius: 12px; padding: 14px; margin-bottom: 10px; }

    /* ── TOAST ── */
    #toast { position: fixed; bottom: calc(90px + var(--safe-bottom)); left: 50%; transform: translateX(-50%) translateY(20px); background: rgba(16,185,129,0.15); border: 1px solid rgba(16,185,129,0.3); color: var(--green2); padding: 10px 20px; border-radius: 30px; font-size: 13px; font-weight: 700; opacity: 0; transition: all .3s; pointer-events: none; white-space: nowrap; z-index: 200; }
    #toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }

    /* ── PRICING ── */
    .price-card { padding: 18px; border-radius: 14px; border: 1px solid var(--border); background: rgba(255,255,255,0.02); margin-bottom: 12px; }
    .price-card.featured { border-color: rgba(14,165,233,0.35); background: rgba(14,165,233,0.05); }
    .price-amount { font-size: 28px; font-weight: 800; color: var(--blue2); }
    .price-period { font-size: 13px; color: var(--text3); }

    /* ── SKIP LINK ── */
    .skip-link { position: absolute; top: -100%; left: 50%; transform: translateX(-50%); padding: 8px 16px; background: var(--blue); color: #fff; border-radius: 0 0 8px 8px; font-size: 14px; font-weight: 700; z-index: 999; text-decoration: none; }
    .skip-link:focus { top: 0; }

    /* ── FOCUS VISIBLE ── */
    .btn:focus-visible, .nav-btn:focus-visible { outline: 2px solid var(--blue2); outline-offset: 2px; }
    .inp:focus-visible { outline: 2px solid var(--blue); outline-offset: 2px; }
    .step-tab:focus-visible { outline: 2px solid var(--blue2); outline-offset: -2px; }
    .star:focus-visible { outline: 2px solid #f59e0b; border-radius: 2px; }
    .clinic-row:focus-visible { outline: 2px solid var(--blue2); }
  </style>
</head>
<body>
<div id="app">
  <a href="#page-content" class="skip-link">تخطى إلى المحتوى الرئيسي</a>

  <!-- TOP BAR -->
  <div class="topbar" id="topbar">
    <div class="logo" aria-hidden="true">⭐</div>
    <div class="topbar-title">
      <h1 id="page-title">ReviewPro</h1>
      <p id="page-sub">نظام إدارة تقييمات Google Maps</p>
    </div>
    <button class="btn btn-ghost btn-sm" id="top-action" style="display:none"></button>
  </div>

  <!-- INSTALL BANNER -->
  <div id="install-banner">
    <span style="font-size:22px" aria-hidden="true">📲</span>
    <div style="flex:1">
      <div style="font-size:13px;font-weight:700;color:var(--blue2)">ثبّت التطبيق</div>
      <div style="font-size:11px;color:var(--text3)">أضفه لشاشتك الرئيسية</div>
    </div>
    <button class="btn btn-primary btn-sm" id="install-btn">تثبيت</button>
    <button class="btn btn-ghost btn-sm" id="dismiss-banner" style="padding:7px 10px" aria-label="إغلاق">✕</button>
  </div>

  <!-- PAGES -->
  <main class="page" id="page-content" tabindex="-1"></main>

  <!-- BOTTOM NAV -->
  <nav class="bottom-nav" aria-label="شريط التنقل الرئيسي">
    <button class="nav-btn active" data-page="home" aria-current="page">
      <span class="nav-icon" aria-hidden="true">🏥</span>العيادات
    </button>
    <button class="nav-btn" data-page="workspace">
      <span class="nav-icon" aria-hidden="true">⚡</span>الأدوات
    </button>
    <button class="nav-btn" data-page="pricing">
      <span class="nav-icon" aria-hidden="true">💰</span>الأسعار
    </button>
    <button class="nav-btn" data-page="settings">
      <span class="nav-icon" aria-hidden="true">⚙️</span>الإعدادات
    </button>
  </nav>

  <div id="toast" role="status" aria-live="polite" aria-atomic="true"></div>
</div>

<script>
// ══════════════════════════════════════════════
// STATE
// ══════════════════════════════════════════════
const state = {
  page: 'home',
  step: 'search',
  clinics: JSON.parse(localStorage.getItem('rp_clinics') || '[]'),
  activeClinic: null,
  loading: false,
  // workspace
  clinicName: '', clinicType: 'عيادة عامة', clinicCity: '',
  searchQuery: '', searchResult: '',
  reviews: [{ id: 1, text: '', rating: 1, response: '' }],
  analysis: '', strategy: '', report: '',
};

const CLINIC_TYPES = ['عيادة عامة','عيادة أسنان','عيادة جلدية','عيادة نساء وولادة','عيادة أطفال','مركز طبي'];
const STEPS = [
  { id:'search', icon:'🔍', label:'البحث' },
  { id:'analyze', icon:'📊', label:'التحليل' },
  { id:'respond', icon:'💬', label:'الردود' },
  { id:'strategy', icon:'🎯', label:'الاستراتيجية' },
  { id:'report', icon:'📋', label:'التقرير' },
];

// ══════════════════════════════════════════════
// CLAUDE API
// ══════════════════════════════════════════════
// Streaming callback: onChunk(text) called on each token, returns full text
async function callClaude(system, user, onChunk) {
  const apiKey = localStorage.getItem('rp_api_key') || '';
  if (!apiKey) { showToast('⚠️ أدخل مفتاح API في الإعدادات'); return 'لم يتم إدخال مفتاح API.'; }
  try {
    const res = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': apiKey,
        'anthropic-version': '2023-06-01',
        'anthropic-dangerous-direct-browser-access': 'true',
      },
      body: JSON.stringify({
        model: 'claude-haiku-4-5-20251001',
        max_tokens: 2000,
        stream: true,
        system,
        messages: [{ role: 'user', content: user }]
      })
    });
    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      const msg = err.error?.message || `خطأ ${res.status}`;
      showToast('❌ ' + msg); return 'خطأ: ' + msg;
    }
    // Read SSE stream
    const reader = res.body.getReader();
    const decoder = new TextDecoder();
    let full = '';
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      const chunk = decoder.decode(value, { stream: true });
      for (const line of chunk.split('\n')) {
        if (!line.startsWith('data: ')) continue;
        const data = line.slice(6).trim();
        if (data === '[DONE]') break;
        try {
          const json = JSON.parse(data);
          const text = json.delta?.text || '';
          if (text) {
            full += text;
            if (onChunk) onChunk(full);
          }
        } catch(e) {}
      }
    }
    return full;
  } catch(e) {
    showToast('❌ خطأ في الاتصال: ' + e.message);
    return 'خطأ في الاتصال.';
  }
}

// Legacy wrapper for non-streaming calls
async function callClaudeSimple(system, user) {
  return callClaude(system, user, null);
}



// ══════════════════════════════════════════════
// GOOGLE MAPS PLACES
// ══════════════════════════════════════════════
// Extract Place ID from Google Maps URL
function extractPlaceId(url) {
  const patterns = [
    /[?&]cid=(\d+)/,
    /!1s(ChIJ[^!&]+)/,
    /place\/[^/]+\/(ChIJ[^/?&]+)/,
    /!1s(0x[a-f0-9]+:[a-f0-9a-f]+)/i,
  ];
  for (const p of patterns) {
    const m = url.match(p);
    if (m && m[1]) return m[1];
  }
  return null;
}

// Fetch reviews directly by Place ID (skip search step)
async function fetchByPlaceId(placeId, apiKey) {
  const res = await fetch(`/proxy/google/details/${placeId}`, {
    headers: {
      'X-Goog-Api-Key': apiKey,
      'X-Goog-FieldMask': 'id,displayName,rating,userRatingCount,reviews,formattedAddress'
    }
  });
  const detail = await res.json();
  if (detail.error) throw new Error('خطأ Google: ' + (detail.error.message || 'تحقق من المفتاح'));
  return {
    name: detail.displayName?.text || '',
    rating: detail.rating,
    user_ratings_total: detail.userRatingCount,
    formatted_address: detail.formattedAddress,
    reviews: (detail.reviews || []).map(r => ({
      text: r.text?.text || r.originalText?.text || '',
      rating: r.rating || 3,
      author_name: r.authorAttribution?.displayName || ''
    }))
  };
}

async function fetchGoogleReviews(query) {
  const apiKey = localStorage.getItem('gmaps_key');
  if (!apiKey) throw new Error('أدخل مفتاح Google Maps في الإعدادات');

  // Step 1: Search directly
  const searchRes = await fetch('/proxy/google/search', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-Goog-Api-Key': apiKey,
      'X-Goog-FieldMask': 'places.id,places.displayName,places.rating,places.userRatingCount,places.formattedAddress'
    },
    body: JSON.stringify({ textQuery: query, languageCode: 'ar' })
  });
  const searchData = await searchRes.json();
  if (searchData.error) throw new Error('خطأ Google: ' + (searchData.error.message || 'تحقق من المفتاح'));
  if (!searchData.places?.length) throw new Error('لم يتم العثور على العيادة في Google Maps');

  const place = searchData.places[0];
  const placeId = place.id;

  // Step 2: Get place details directly
  const detailRes = await fetch(`/proxy/google/details/${placeId}`, {
    headers: {
      'X-Goog-Api-Key': apiKey,
      'X-Goog-FieldMask': 'id,displayName,rating,userRatingCount,reviews,formattedAddress'
    }
  });
  const detail = await detailRes.json();
  if (detail.error) throw new Error('فشل جلب التفاصيل: ' + (detail.error.message || ''));

  // Normalize to expected format
  return {
    name: detail.displayName?.text || place.displayName?.text || query,
    rating: detail.rating || place.rating,
    user_ratings_total: detail.userRatingCount || place.userRatingCount,
    formatted_address: detail.formattedAddress || place.formattedAddress,
    reviews: (detail.reviews || []).map(r => ({
      text: r.text?.text || r.originalText?.text || '',
      rating: r.rating || 3,
      author_name: r.authorAttribution?.displayName || ''
    }))
  };
}

// ══════════════════════════════════════════════
// UTILS
// ══════════════════════════════════════════════
function saveClinics() { localStorage.setItem('rp_clinics', JSON.stringify(state.clinics)); }
function ratingColor(r) { return r >= 4 ? '#34d399' : r === 3 ? '#fbbf24' : '#f87171'; }
function ratingLabel(r) { return r >= 4 ? 'إيجابي' : r === 3 ? 'محايد' : 'سلبي'; }
function avgRating() {
  const filled = state.reviews.filter(r => r.text);
  return filled.length ? (filled.reduce((s,r)=>s+r.rating,0)/filled.length).toFixed(1) : '0';
}
function showToast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg; t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2500);
}
function copyText(text) {
  navigator.clipboard.writeText(text).then(() => showToast('✓ تم النسخ!'));
}
function setLoading(val) { state.loading = val; render(); }

// ══════════════════════════════════════════════
// ACTIONS
// ══════════════════════════════════════════════
async function doGmapsFetch() {
  const inp = document.getElementById('gmaps-url-input');
  const urlVal = inp ? inp.value.trim() : '';
  if (!urlVal) { showToast('⚠️ الصق رابط العيادة من Google Maps'); return; }
  setLoading(true);
  try {
    const apiKey = localStorage.getItem('gmaps_key');
    if (!apiKey) { showToast('⚠️ أدخل مفتاح Google في الإعدادات'); setLoading(false); return; }
    let detail;
    const placeId = extractPlaceId(urlVal);
    if (placeId) {
      showToast('✅ تم استخراج المعرّف — جاري الجلب...');
      detail = await fetchByPlaceId(placeId, apiKey);
    } else if (urlVal.includes('goo.gl') || urlVal.includes('maps.app')) {
      throw new Error('❌ الرابط المختصر لا يعمل\nافتح العيادة في المتصفح وانسخ رابط شريط العنوان الكامل');
    } else {
      // Fallback: search by clinic name
      showToast('🔍 جاري البحث...');
      detail = await fetchGoogleReviews(state.clinicName || urlVal);
    }
    state.clinicName = detail.name || state.searchQuery;
    // Map Google reviews to state.reviews
    const reviews = detail.reviews || [];
    if (!reviews.length) { showToast('⚠️ لا توجد تقييمات متاحة لهذه العيادة'); setLoading(false); return; }
    state.reviews = reviews.map((r, i) => ({
      id: i + 1,
      text: r.text || '',
      rating: r.rating || 3,
      response: r.author_name ? '' : ''
    }));
    const avg = detail.rating ? detail.rating.toFixed(1) : avgRating();
    const total = detail.user_ratings_total || reviews.length;
    showToast(`✅ تم جلب ${reviews.length} تقييمات — المعدل: ${avg}★ (${total} تقييم إجمالاً)`);
    state.step = 'analyze';
  } catch(e) {
    showToast('❌ ' + e.message);
  }
  setLoading(false);
}

async function doSearch() {
  if (!state.searchQuery.trim() || state.loading) return;
  setLoading(true);
  state.searchResult = await callClaude(
    'أنت مساعد متخصص في تحليل سوق العيادات الطبية. أجب بالعربية بشكل منظم ومختصر.',
    `حلل وضع هذه العيادة من حيث تقييمات Google Maps:\nالعيادة: ${state.searchQuery} - ${state.clinicType} في ${state.clinicCity||'المملكة'}\n\n1. 🏥 نبذة عن مكانتها في السوق\n2. ⭐ تقدير وضع تقييماتها الحالي\n3. 🔍 أبرز نقاط الضعف الشائعة\n4. 💡 أهم 3 فرص للتحسين\n5. 🎯 مدى احتياجها للخدمة (عالي/متوسط/منخفض)`
  );
  state.clinicName = state.searchQuery;
  setLoading(false);
}

async function doAnalyze() {
  const filled = state.reviews.filter(r => r.text.trim());
  if (!filled.length || state.loading) return;
  setLoading(true);
  const positive = filled.filter(r=>r.rating>=4);
  const neutral  = filled.filter(r=>r.rating===3);
  const negative = filled.filter(r=>r.rating<=2);
  const txt = filled.map((r,i) =>
    `[تقييم ${i+1}] النجوم: ${r.rating}/5 | الحالة: ${ratingLabel(r.rating)}\nالنص: "${r.text}"`
  ).join('\n\n');

  try {
  state.analysis = await callClaude(
    `أنت محلل خبير في إدارة سمعة العيادات الطبية وتجربة المرضى. مهمتك تحليل تقييمات Google Maps بعمق واحترافية عالية. أجب دائماً بالعربية الفصحى المبسطة. هيكل إجابتك بدقة كما هو مطلوب.`,
    `حلّل هذه التقييمات لـ "${state.clinicName||'العيادة'}" (${state.clinicType}${state.clinicCity?' - '+state.clinicCity:''})

إحصائيات:
- إجمالي التقييمات: ${filled.length}
- متوسط التقييم: ${avgRating()}/5
- إيجابية (4-5★): ${positive.length} | محايدة (3★): ${neutral.length} | سلبية (1-2★): ${negative.length}

التقييمات:
${txt}

أعطني التحليل بهذا الهيكل الدقيق:

##SUMMARY##
[جملتان فقط: ملخص دقيق يصف الوضع العام للعيادة ومستوى رضا المرضى]

##SCORE##
[رقم من 1 إلى 100 يمثل الصحة الرقمية للعيادة بناءً على التقييمات]

##STRENGTHS##
[3 نقاط قوة مستخلصة من التقييمات الفعلية، كل نقطة في سطر يبدأ بـ •]

##WEAKNESSES##
[3 نقاط ضعف مستخلصة من التقييمات الفعلية، كل نقطة في سطر يبدأ بـ •]

##PATIENT_PAIN##
[أبرز شكوى متكررة من المرضى في جملة واحدة واضحة]

##URGENT##
[أرقام التقييمات التي تحتاج رداً عاجلاً مثال: 1,3 أو "لا يوجد" — بدون تفسير]

##PREDICTION##
[توقع التقييم بعد 3 أشهر إذا نُفذت التوصيات، مثال: 4.2★ مع سبب قصير]

##TOP_ACTION##
[الإجراء الواحد الأهم الذي يجب تنفيذه هذا الأسبوع فقط]`
  , (partial) => { state.analysis = partial; render(); });
  } catch(e) { showToast('❌ ' + e.message); }
  state.analyzing = false;
  setLoading(false);
  render();
}

async function doRespond(id) {
  if (state.loading) return;
  const rev = state.reviews.find(r => r.id === id);
  if (!rev?.text.trim()) return;
  setLoading(true);
  rev.response = '';
  rev.streaming = true;
  render();
  try {
    rev.response = await callClaude(
      'أنت متخصص في إدارة سمعة العيادات. اكتب رداً احترافياً دافئاً بالعربية. 3-4 جمل فقط. أنهِ باسم العيادة.',
      `اكتب رداً على: ${state.clinicName||'عيادتنا'} (${state.clinicType})\nالتقييم: ${rev.rating}/5 (${ratingLabel(rev.rating)})\n"${rev.text}"`,
      (partial) => { rev.response = partial; render(); }
    );
  } catch(e) { showToast('❌ ' + e.message); }
  rev.streaming = false;
  setLoading(false);
  render();
}

async function doRespondAll() {
  const pending = state.reviews.filter(r => r.text.trim() && !r.response);
  for (const r of pending) { await doRespond(r.id); }
}

async function doStrategy() {
  if (state.loading) return;
  setLoading(true);
  state.strategy = '';
  state.strategyStreaming = true;
  render();
  const filled = state.reviews.filter(r=>r.text);
  const avg = avgRating();
  const txt = filled.map((r,i) => `تقييم ${i+1} (${r.rating}★): "${r.text}"`).join('\n');
  try {
    state.strategy = await callClaude(
      'أنت استراتيجي متخصص في تحسين سمعة العيادات الطبية. أجب بالعربية.',
      `ضع خطة تحسين 90 يوماً لـ ${state.clinicName||'العيادة'} (تقييم حالي: ${avg}/5):\n${txt}\n\nالخطة يجب أن تشمل:\n1. الشهر الأول: إجراءات عاجلة\n2. الشهر الثاني: تحسينات هيكلية\n3. الشهر الثالث: تعزيز التقييمات\n4. مؤشرات النجاح`,
      (p) => { state.strategy = p; render(); }
    );
  } catch(e) { showToast('❌ ' + e.message); }
  state.strategyStreaming = false;
  setLoading(false);
}

async function doReport() {
  if (state.loading) return;
  setLoading(true);
  const filled = state.reviews.filter(r=>r.text);
  state.report = await callClaude(
    'أنت محترف في إعداد التقارير الطبية. اكتب تقارير احترافية بالعربية.',
    `أعد تقريراً شهرياً لـ ${state.clinicName||'العيادة'} (${state.clinicType}):\n- متوسط التقييم: ${avgRating()}/5\n- إجمالي التقييمات: ${filled.length}\n- إيجابية: ${filled.filter(r=>r.rating>=4).length}\n- سلبية: ${filled.filter(r=>r.rating<=2).length}\n- ردود منجزة: ${filled.filter(r=>r.response).length}/${filled.length}\n\n📋 ملخص تنفيذي\n📊 أبرز الأرقام\n✅ إنجازات الشهر\n⚠️ التحديات\n💡 توصيات الشهر القادم\n⭐ تقييم عام من 10`
  );
  // Save clinic
  const clinic = { id: Date.now(), name: state.clinicName, type: state.clinicType, city: state.clinicCity, avgRating: parseFloat(avgRating()), reviewCount: filled.length, date: new Date().toLocaleDateString('ar-SA') };
  state.clinics = [...state.clinics.filter(c=>c.name!==clinic.name), clinic];
  saveClinics();
  setLoading(false);
  showToast('✓ تم حفظ التقرير!');
}

// ══════════════════════════════════════════════
// RENDER
// ══════════════════════════════════════════════
function render() {
  const content = document.getElementById('page-content');
  const title = document.getElementById('page-title');
  const sub = document.getElementById('page-sub');
  const topBtn = document.getElementById('top-action');

  document.querySelectorAll('.nav-btn').forEach(b => {
    const isActive = b.dataset.page === state.page;
    b.classList.toggle('active', isActive);
    if (isActive) b.setAttribute('aria-current', 'page');
    else b.removeAttribute('aria-current');
  });

  if (state.page === 'home') {
    title.textContent = 'ReviewPro';
    sub.textContent = `${state.clinics.length} عيادة مسجلة`;
    topBtn.style.display = 'block'; topBtn.textContent = '+ جديد';
    topBtn.onclick = () => { state.page = 'workspace'; state.step = 'search'; state.searchResult=''; state.analysis=''; state.strategy=''; state.report=''; state.reviews=[{id:1,text:'',rating:1,response:''}]; state.clinicName=''; state.searchQuery=''; render(); };
    content.innerHTML = renderHome();
  } else if (state.page === 'workspace') {
    title.textContent = state.clinicName || 'عيادة جديدة';
    sub.textContent = state.clinicType;
    topBtn.style.display = 'none';
    content.innerHTML = renderWorkspace();
    bindWorkspace();
  } else if (state.page === 'pricing') {
    title.textContent = 'الأسعار'; sub.textContent = 'باقات الخدمة'; topBtn.style.display='none';
    content.innerHTML = renderPricing();
  } else if (state.page === 'settings') {
    title.textContent = 'الإعدادات'; sub.textContent = 'ReviewPro'; topBtn.style.display='none';
    content.innerHTML = renderSettings();
    bindSettings();
  }
}

// ── HOME ──────────────────────────────────────
function renderHome() {
  const totalReviews = state.clinics.reduce((s,c)=>s+c.reviewCount,0);
  const avgAll = state.clinics.length ? (state.clinics.reduce((s,c)=>s+c.avgRating,0)/state.clinics.length).toFixed(1) : '—';
  const hasKey = !!localStorage.getItem('rp_api_key');
  return `
  <div style="padding:16px">
    ${!hasKey ? `
    <div onclick="goPage('settings')" style="cursor:pointer;margin-bottom:14px;padding:13px 15px;border-radius:12px;background:rgba(245,158,11,0.08);border:1px solid rgba(245,158,11,0.3);display:flex;align-items:center;gap:10px">
      <span style="font-size:20px">🔑</span>
      <div style="flex:1">
        <div style="font-size:13px;font-weight:800;color:#fbbf24">مفتاح API غير موجود</div>
        <div style="font-size:11px;color:var(--text3);margin-top:2px">اضغط هنا لإضافته في الإعدادات</div>
      </div>
      <span style="color:var(--text3);font-size:16px">←</span>
    </div>` : ''}
    <div class="stat-grid" style="margin-bottom:16px">
      <div class="stat-box"><div class="stat-num" style="color:var(--blue2)">${state.clinics.length}</div><div class="stat-lbl">العيادات</div></div>
      <div class="stat-box"><div class="stat-num" style="color:var(--yellow)">${avgAll}${state.clinics.length?'★':''}</div><div class="stat-lbl">متوسط التقييم</div></div>
      <div class="stat-box"><div class="stat-num" style="color:var(--green2)">${totalReviews}</div><div class="stat-lbl">تقييمات</div></div>
    </div>
    ${state.clinics.length === 0 ? `
      <div class="empty">
        <div class="icon" aria-hidden="true">🏥</div>
        <h3>لا توجد عيادات بعد</h3>
        <p>اضغط + جديد لإضافة عيادتك الأولى</p>
      </div>
    ` : state.clinics.map(c => `
      <div class="clinic-row" role="button" tabindex="0" onclick="openClinic(${c.id})" onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();openClinic(${c.id})}"  aria-label="${c.name}، ${c.type}${c.city?' في '+c.city:''}، التقييم ${c.avgRating} نجوم">
        <div style="display:flex;justify-content:space-between;align-items:center">
          <div>
            <div style="font-weight:800;font-size:15px">${c.name}</div>
            <div style="font-size:12px;color:var(--text3);margin-top:3px">${c.type}${c.city?' • '+c.city:''}</div>
          </div>
          <div style="text-align:left">
            <div style="font-size:20px;font-weight:800;color:${ratingColor(c.avgRating)}" aria-label="${c.avgRating} نجوم">${c.avgRating}★</div>
            <div class="tag tag-blue" style="font-size:10px;margin-top:4px">${c.reviewCount} تقييم</div>
          </div>
        </div>
        <div style="font-size:11px;color:var(--text3);margin-top:8px">📅 ${c.date}</div>
      </div>
    `).join('')}
  </div>`;
}

function openClinic(id) {
  const c = state.clinics.find(x=>x.id===id);
  if (!c) return;
  state.clinicName = c.name; state.clinicType = c.type; state.clinicCity = c.city;
  state.page = 'workspace'; state.step = 'analyze';
  state.reviews = [{id:1,text:'',rating:1,response:''}];
  state.analysis=''; state.strategy=''; state.report=''; state.searchResult='';
  render();
}
window.openClinic = openClinic;

// ── WORKSPACE ─────────────────────────────────
function renderWorkspace() {
  return `
  <div>
    <div class="steps" role="tablist" aria-label="خطوات العمل">
      ${STEPS.map(s=>`<button class="step-tab ${state.step===s.id?'active':''}" role="tab" aria-selected="${state.step===s.id}" data-step="${s.id}" type="button">${s.icon} ${s.label}</button>`).join('')}
    </div>
    <div style="padding:16px" id="step-content">
      ${renderStep()}
    </div>
  </div>`;
}

function renderStep() {
  if (state.step === 'search') return renderSearch();
  if (state.step === 'analyze') return renderAnalyze();
  if (state.step === 'respond') return renderRespond();
  if (state.step === 'strategy') return renderStrategy();
  if (state.step === 'report') return renderReport();
  return '';
}

function renderSearch() { return `
  <h2 style="font-size:17px;font-weight:800;margin-bottom:4px">🔍 البحث وتحليل العيادة</h2>
  <p style="font-size:13px;color:var(--text3);margin-bottom:16px">ابدأ بإدخال اسم العيادة</p>
  <div style="display:flex;flex-direction:column;gap:12px;margin-bottom:14px">
    <div><label class="lbl" for="sq">اسم العيادة أو الدكتور</label>
      <input class="inp" id="sq" placeholder="مثال: عيادة د. محمد العمري" value="${state.searchQuery}" /></div>
    <div><label class="lbl" for="city">المدينة</label>
      <input class="inp" id="city" placeholder="مثال: الرياض" value="${state.clinicCity}" /></div>
    <div><label class="lbl" for="ctype">نوع العيادة</label>
      <select class="inp" id="ctype">${CLINIC_TYPES.map(t=>`<option ${state.clinicType===t?'selected':''}>${t}</option>`).join('')}</select></div>
  </div>
  <button class="btn btn-primary btn-full" id="do-search" ${state.loading?'disabled':''}>
    ${state.loading ? '<span class="spinner"></span> جاري التحليل...' : '🔍 تحليل بالذكاء الاصطناعي'}
  </button>

  ${state.searchResult ? `
    <div class="divider"></div>
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
      <span class="lbl" style="margin:0">نتيجة التحليل</span>
      <button class="btn btn-ghost btn-sm" onclick="copyText(\`${state.searchResult.replace(/`/g,"'")}\`)">نسخ</button>
    </div>
    <div class="result result-blue">${state.searchResult}</div>
    <button class="btn btn-primary btn-full" style="margin-top:14px" onclick="goStep('analyze')">التالي: إدخال التقييمات ←</button>
  ` : ''}
`; }

function parseAnalysis(raw) {
  const get = (key) => {
    const m = raw.match(new RegExp('##' + key + '##\\s*([\\s\\S]*?)(?=##|$)'));
    return m ? m[1].trim() : '';
  };
  return {
    summary:    get('SUMMARY'),
    score:      get('SCORE'),
    strengths:  get('STRENGTHS'),
    weaknesses: get('WEAKNESSES'),
    pain:       get('PATIENT_PAIN'),
    urgent:     get('URGENT'),
    prediction: get('PREDICTION'),
    topAction:  get('TOP_ACTION'),
  };
}

function renderAnalysisCards(raw) {
  const p = parseAnalysis(raw);
  const score = parseInt(p.score) || 0;
  const scoreColor = score >= 75 ? 'var(--green2)' : score >= 50 ? '#fbbf24' : '#f87171';
  const scoreBg = score >= 75 ? 'rgba(52,211,153,0.08)' : score >= 50 ? 'rgba(251,191,36,0.08)' : 'rgba(248,113,113,0.08)';
  const scoreBorder = score >= 75 ? 'rgba(52,211,153,0.2)' : score >= 50 ? 'rgba(251,191,36,0.2)' : 'rgba(248,113,113,0.2)';

  const fmtBullets = (txt) => txt.split('\n').filter(l=>l.trim()).map(l =>
    `<div style="display:flex;gap:8px;align-items:flex-start;margin-bottom:7px">
      <span style="flex-shrink:0;margin-top:2px">${l.startsWith('•') ? l[0] : '•'}</span>
      <span>${l.replace(/^•\s*/,'')}</span>
    </div>`
  ).join('');

  // fallback: if structured parsing failed, show raw
  if (!p.summary && !p.score) {
    return `<div class="result result-green">${raw}</div>`;
  }

  return `
  <div style="display:flex;flex-direction:column;gap:12px;animation:fadeUp .35s ease">

    <!-- Score + Summary -->
    <div style="display:grid;grid-template-columns:auto 1fr;gap:12px;align-items:center;padding:16px;border-radius:14px;background:${scoreBg};border:1px solid ${scoreBorder}">
      <div style="text-align:center;padding:0 8px">
        <div style="font-size:32px;font-weight:800;color:${scoreColor};line-height:1">${score}</div>
        <div style="font-size:10px;color:var(--text3);margin-top:3px">الصحة الرقمية</div>
        <div style="width:48px;height:4px;border-radius:4px;background:rgba(255,255,255,0.08);margin:6px auto 0;overflow:hidden">
          <div style="height:100%;width:${score}%;background:${scoreColor};border-radius:4px;transition:width 1s ease"></div>
        </div>
      </div>
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--text3);margin-bottom:5px;letter-spacing:.5px">الملخص العام</div>
        <div style="font-size:13px;color:var(--text);line-height:1.75">${p.summary || '—'}</div>
      </div>
    </div>

    <!-- Strengths + Weaknesses -->
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
      <div style="padding:14px;border-radius:12px;background:rgba(52,211,153,0.05);border:1px solid rgba(52,211,153,0.15)">
        <div style="font-size:11px;font-weight:800;color:var(--green2);margin-bottom:10px">✅ نقاط القوة</div>
        <div style="font-size:12px;color:var(--text2);line-height:1.7">${fmtBullets(p.strengths || '—')}</div>
      </div>
      <div style="padding:14px;border-radius:12px;background:rgba(248,113,113,0.05);border:1px solid rgba(248,113,113,0.15)">
        <div style="font-size:11px;font-weight:800;color:#f87171;margin-bottom:10px">⚠️ نقاط الضعف</div>
        <div style="font-size:12px;color:var(--text2);line-height:1.7">${fmtBullets(p.weaknesses || '—')}</div>
      </div>
    </div>

    <!-- Pain point -->
    ${p.pain ? `
    <div style="padding:13px 15px;border-radius:12px;background:rgba(245,158,11,0.06);border:1px solid rgba(245,158,11,0.2);display:flex;gap:10px;align-items:flex-start">
      <span style="font-size:18px;flex-shrink:0">😤</span>
      <div>
        <div style="font-size:11px;font-weight:800;color:#fbbf24;margin-bottom:4px">أبرز شكوى المرضى</div>
        <div style="font-size:13px;color:var(--text2)">${p.pain}</div>
      </div>
    </div>` : ''}

    <!-- Urgent + Prediction row -->
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
      <div style="padding:13px;border-radius:12px;background:rgba(239,68,68,0.05);border:1px solid rgba(239,68,68,0.18);text-align:center">
        <div style="font-size:11px;font-weight:800;color:#f87171;margin-bottom:6px">🚨 رد عاجل</div>
        <div style="font-size:13px;font-weight:700;color:var(--text)">${p.urgent || 'لا يوجد'}</div>
      </div>
      <div style="padding:13px;border-radius:12px;background:rgba(56,189,248,0.05);border:1px solid rgba(56,189,248,0.18);text-align:center">
        <div style="font-size:11px;font-weight:800;color:var(--blue2);margin-bottom:6px">📈 توقع 3 أشهر</div>
        <div style="font-size:13px;font-weight:700;color:var(--text)">${p.prediction || '—'}</div>
      </div>
    </div>

    <!-- Top Action -->
    ${p.topAction ? `
    <div style="padding:14px 16px;border-radius:12px;background:linear-gradient(135deg,rgba(14,165,233,0.1),rgba(2,132,199,0.06));border:1px solid rgba(14,165,233,0.25);display:flex;gap:10px;align-items:flex-start">
      <span style="font-size:18px;flex-shrink:0">⚡</span>
      <div>
        <div style="font-size:11px;font-weight:800;color:var(--blue2);margin-bottom:4px">الإجراء الأهم هذا الأسبوع</div>
        <div style="font-size:13px;color:var(--text);font-weight:700">${p.topAction}</div>
      </div>
    </div>` : ''}

  </div>`;
}

function renderAnalyze() {
  const filled = state.reviews.filter(r => r.text.trim());
  return `
  <div style="display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:14px">
    <div>
      <h2 style="font-size:17px;font-weight:800;margin-bottom:3px">📊 تحليل التقييمات</h2>
      <p style="font-size:12px;color:var(--text3)">أدخل التقييمات وسيحللها الذكاء الاصطناعي</p>
    </div>
    ${filled.length > 0 ? `<span class="tag tag-blue">${filled.length} تقييم</span>` : ''}
  </div>

  ${localStorage.getItem('gmaps_key') ? `
  <div style="margin-bottom:14px;padding:14px;border-radius:14px;background:rgba(56,189,248,0.05);border:1px solid rgba(56,189,248,0.2)">
    <div style="font-size:12px;font-weight:800;color:var(--blue2);margin-bottom:10px">📍 جلب التقييمات من Google Maps</div>

    <div style="padding:10px 12px;border-radius:10px;background:rgba(251,191,36,0.06);border:1px solid rgba(251,191,36,0.2);margin-bottom:10px">
      <div style="font-size:11px;font-weight:800;color:#fbbf24;margin-bottom:4px">📋 كيف تحصل على الرابط؟</div>
      <div style="font-size:11px;color:var(--text3);line-height:1.8">
        1. افتح العيادة في Google Maps على الكمبيوتر<br>
        2. انسخ الرابط من <b style="color:var(--text2)">شريط العنوان</b> في المتصفح مباشرة<br>
        <span style="color:#f87171">⚠️ لا تستخدم زر "مشاركة" — الرابط المختصر لا يعمل</span>
      </div>
    </div>

    <div style="display:flex;gap:8px;margin-bottom:6px">
      <input class="inp" id="gmaps-url-input" type="text"
        placeholder="https://www.google.com/maps/place/..."
        style="flex:1;font-size:12px;margin-bottom:0" />
      <button class="btn btn-primary" id="do-gmaps-fetch" style="flex-shrink:0;padding:0 16px" ${state.loading?'disabled':''}>
        ${state.loading ? '<span class="spinner"></span>' : '📥 جلب'}
      </button>
    </div>
    <div style="font-size:11px;color:var(--text3);text-align:center">سيجلب آخر 5 تقييمات ويملأها تلقائياً ⬇️</div>
  </div>
  ` : `
  <div style="margin-bottom:14px;padding:12px;border-radius:12px;background:rgba(245,158,11,0.05);border:1px dashed rgba(245,158,11,0.25);text-align:center">
    <div style="font-size:12px;color:#fbbf24">💡 أضف مفتاح Google Maps في الإعدادات لجلب التقييمات تلقائياً</div>
  </div>
  `}

  <div id="reviews-list">
    ${state.reviews.map((r,i) => `
      <div class="review-item" style="position:relative">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
          <div style="display:flex;align-items:center;gap:8px">
            <span style="font-size:12px;font-weight:800;color:var(--text3)">#${i+1}</span>
            <div class="star-row" role="radiogroup" aria-label="التقييم" style="gap:3px">
              ${[1,2,3,4,5].map(s=>`<span class="star" role="radio" aria-checked="${s<=r.rating}" aria-label="${s} نجوم" tabindex="${s===r.rating?'0':'-1'}" onclick="setRating(${r.id},${s})" onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();setRating(${r.id},${s});}" style="font-size:22px;color:${s<=r.rating?'#f59e0b':'#1e2d40'}">${s<=r.rating?'★':'☆'}</span>`).join('')}
            </div>
          </div>
          <div style="display:flex;align-items:center;gap:6px">
            <span class="tag" style="background:${ratingColor(r.rating)}18;color:${ratingColor(r.rating)};border:1px solid ${ratingColor(r.rating)}30;font-size:10px">${ratingLabel(r.rating)} ${r.rating}★</span>
            ${state.reviews.length>1 ? `<button style="background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.2);color:#f87171;border-radius:6px;padding:3px 8px;font-size:12px;cursor:pointer" onclick="removeReview(${r.id})">✕</button>` : ''}
          </div>
        </div>
        <textarea class="inp" rows="3" aria-label="نص التقييم ${i+1}" placeholder="الصق نص التقييم من Google Maps..." onchange="updateReview(${r.id},'text',this.value)" onblur="updateReview(${r.id},'text',this.value)" style="font-size:13px;line-height:1.7">${r.text}</textarea>
        ${r.text ? `<div style="font-size:11px;color:var(--text3);margin-top:5px;text-align:left">${r.text.length} حرف</div>` : ''}
      </div>
    `).join('')}
  </div>

  <div style="display:flex;gap:10px;margin-bottom:14px">
    <button class="btn btn-ghost" style="flex:1;font-size:13px" onclick="addReview()">➕ إضافة تقييم</button>
    <button class="btn btn-primary" style="flex:2" id="do-analyze" ${state.loading||!filled.length?'disabled':''}>
      ${state.loading ? '<span class="spinner"></span> جاري التحليل...' : `📊 حلّل الآن (${filled.length})`}
    </button>
  </div>

  ${!filled.length ? `
    <div style="padding:14px;border-radius:12px;background:rgba(56,189,248,0.04);border:1px dashed rgba(56,189,248,0.2);text-align:center">
      <div style="font-size:12px;color:var(--text3)">💡 أدخل نص تقييم واحد على الأقل للبدء</div>
    </div>
  ` : ''}

  ${state.analyzing ? `
    <div class="divider"></div>
    <div style="font-size:12px;font-weight:800;color:var(--blue2);margin-bottom:8px;display:flex;align-items:center;gap:6px">
      <span class="spinner" style="width:12px;height:12px;border-width:2px"></span> جاري التحليل...
    </div>
    <div class="stream-box streaming-cursor">${(state.analysis||'').replace(/</g,'&lt;').replace(/>/g,'&gt;')}</div>
  ` : state.analysis ? `
    <div class="divider"></div>
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px">
      <span style="font-size:14px;font-weight:800;color:var(--text)">نتائج التحليل</span>
      <button class="btn btn-ghost btn-sm" onclick="copyText(\`${state.analysis.replace(/`/g,"'")}\`)">📋 نسخ</button>
    </div>
    ${renderAnalysisCards(state.analysis)}
    <button class="btn btn-primary btn-full" style="margin-top:16px" onclick="goStep('respond')">التالي: توليد الردود ←</button>
  ` : ''}

`; }

function renderRespond() {
  const filled = state.reviews.filter(r=>r.text.trim());
  return `
  <h2 style="font-size:17px;font-weight:800;margin-bottom:4px">💬 توليد الردود</h2>
  <p style="font-size:13px;color:var(--text3);margin-bottom:16px">رد احترافي على كل تقييم</p>
  ${filled.length === 0 ? `<div class="empty"><div class="icon" aria-hidden="true">💬</div><h3>لا توجد تقييمات</h3><p>أدخل التقييمات أولاً</p><button class="btn btn-ghost" style="margin-top:12px" onclick="goStep('analyze')">← العودة</button></div>` : ''}
  ${filled.length > 1 ? `<button class="btn btn-primary btn-full" style="margin-bottom:14px" id="do-respond-all" ${state.loading?'disabled':''}>${state.loading?'<span class="spinner"></span> جاري...':'⚡ رد على الكل دفعة واحدة'}</button>` : ''}
  ${filled.map(r => `
    <div class="review-item">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
        <div style="display:flex;gap:3px" role="img" aria-label="${r.rating} من 5 نجوم">${[1,2,3,4,5].map(s=>`<span style="color:${s<=r.rating?'#f59e0b':'#1e2d40'};font-size:16px" aria-hidden="true">★</span>`).join('')}</div>
        <span class="tag" style="background:${ratingColor(r.rating)}18;color:${ratingColor(r.rating)};border:1px solid ${ratingColor(r.rating)}30;font-size:10px">${ratingLabel(r.rating)}</span>
      </div>
      <div style="background:rgba(255,255,255,0.03);border-radius:8px;padding:10px;font-size:13px;color:var(--text2);margin-bottom:10px;line-height:1.7">"${r.text}"</div>
      ${r.response ? `
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
          <span class="tag tag-green" style="font-size:10px">✓ جاهز</span>
          <button class="btn btn-ghost btn-sm" onclick="copyText(\`${r.response.replace(/`/g,"'")}\`)">نسخ</button>
        </div>
        <div class="result result-green" style="font-size:13px">${r.response}</div>
      ` : `<button class="btn btn-primary btn-full do-respond" data-id="${r.id}" ${state.loading?'disabled':''}>${state.loading?'<span class="spinner"></span>':'💬 ولّد الرد'}</button>`}
    </div>
  `).join('')}
  ${filled.some(r=>r.response) ? `<button class="btn btn-primary btn-full" style="margin-top:8px" onclick="goStep('strategy')">التالي: الاستراتيجية ←</button>` : ''}
`; }

function renderStrategy() { return `
  <h2 style="font-size:17px;font-weight:800;margin-bottom:4px">🎯 استراتيجية التحسين</h2>
  <p style="font-size:13px;color:var(--text3);margin-bottom:16px">خطة 90 يوم لتحسين التقييمات</p>
  <div class="stat-grid" style="margin-bottom:14px">
    <div class="stat-box"><div class="stat-num" style="color:var(--yellow)">${avgRating()}★</div><div class="stat-lbl">المتوسط</div></div>
    <div class="stat-box"><div class="stat-num" style="color:var(--green2)">${state.reviews.filter(r=>r.rating>=4&&r.text).length}</div><div class="stat-lbl">إيجابية</div></div>
    <div class="stat-box"><div class="stat-num" style="color:#f87171">${state.reviews.filter(r=>r.rating<=2&&r.text).length}</div><div class="stat-lbl">سلبية</div></div>
  </div>
  <button class="btn btn-primary btn-full" id="do-strategy" ${state.loading?'disabled':''}>
    ${state.loading ? '<span class="spinner"></span> جاري...' : '🎯 ولّد خطة التحسين'}
  </button>
  ${state.strategy ? `
    <div class="divider"></div>
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
      <span class="lbl" style="margin:0">خطة التحسين</span>
      <button class="btn btn-ghost btn-sm" onclick="copyText(\`${state.strategy.replace(/`/g,"'")}\`)">نسخ</button>
    </div>
    <div class="result result-blue">${state.strategy}</div>
    <button class="btn btn-primary btn-full" style="margin-top:14px" onclick="goStep('report')">التالي: التقرير ←</button>
  ` : ''}
`; }

function renderReport() { return `
  <h2 style="font-size:17px;font-weight:800;margin-bottom:4px">📋 التقرير الشهري</h2>
  <p style="font-size:13px;color:var(--text3);margin-bottom:16px">تقرير احترافي جاهز للعميل</p>
  <div class="card-blue" style="padding:14px;margin-bottom:14px;display:grid;grid-template-columns:1fr 1fr;gap:10px">
    <div><div class="lbl">العيادة</div><div style="font-size:14px;font-weight:700;color:var(--blue2)">${state.clinicName||'غير محدد'}</div></div>
    <div><div class="lbl">الشهر</div><div style="font-size:14px;font-weight:700;color:var(--blue2)">${new Date().toLocaleDateString('ar-SA',{month:'long',year:'numeric'})}</div></div>
  </div>
  <button class="btn btn-primary btn-full" id="do-report" ${state.loading?'disabled':''}>
    ${state.loading ? '<span class="spinner"></span> جاري...' : '📋 ولّد التقرير الكامل'}
  </button>
  ${state.report ? `
    <div class="divider"></div>
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
      <span class="lbl" style="margin:0">التقرير الشهري</span>
      <button class="btn btn-ghost btn-sm" onclick="copyText(\`${state.report.replace(/`/g,"'")}\`)">نسخ</button>
    </div>
    <div class="result result-green">${state.report}</div>
    <div class="card-blue" style="padding:16px;margin-top:16px;text-align:center">
      <div style="font-size:24px;margin-bottom:8px">✅</div>
      <div style="font-size:14px;font-weight:800;color:var(--blue2);margin-bottom:4px">تم الحفظ!</div>
      <button class="btn btn-primary" style="margin-top:10px" onclick="goPage('home')">العودة للرئيسية</button>
    </div>
  ` : ''}
`; }

// ── PRICING ───────────────────────────────────
function renderPricing() { return `
  <div style="padding:16px">
    <h2 style="font-size:18px;font-weight:800;margin-bottom:6px">💰 باقات الخدمة</h2>
    <p style="font-size:13px;color:var(--text3);margin-bottom:20px">قدمها للعيادات كخدمة شهرية</p>
    <div class="price-card">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
        <span style="font-size:15px;font-weight:800">أساسية</span>
        <span class="tag tag-blue">مناسب للبداية</span>
      </div>
      <div><span class="price-amount">500</span><span class="price-period"> ريال / شهر</span></div>
      <div class="divider"></div>
      <div style="display:flex;flex-direction:column;gap:8px;font-size:13px;color:var(--text2)">
        <div>✅ تقرير شهري احترافي</div>
        <div>✅ ردود على جميع التقييمات</div>
        <div>✅ تحليل التقييمات</div>
        <div style="color:var(--text3)">✗ استراتيجية التحسين</div>
      </div>
    </div>
    <div class="price-card featured">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
        <span style="font-size:15px;font-weight:800">احترافية</span>
        <span class="tag tag-green">الأكثر طلباً</span>
      </div>
      <div><span class="price-amount">900</span><span class="price-period"> ريال / شهر</span></div>
      <div class="divider"></div>
      <div style="display:flex;flex-direction:column;gap:8px;font-size:13px;color:var(--text2)">
        <div>✅ كل ما في الأساسية</div>
        <div>✅ استراتيجية تحسين 90 يوم</div>
        <div>✅ رسائل WhatsApp جاهزة</div>
        <div>✅ متابعة أسبوعية</div>
      </div>
    </div>
    <div class="price-card">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
        <span style="font-size:15px;font-weight:800">متكاملة</span>
        <span class="tag tag-yellow">للمراكز الكبيرة</span>
      </div>
      <div><span class="price-amount">1,500</span><span class="price-period"> ريال / شهر</span></div>
      <div class="divider"></div>
      <div style="display:flex;flex-direction:column;gap:8px;font-size:13px;color:var(--text2)">
        <div>✅ كل ما في الاحترافية</div>
        <div>✅ إدارة كاملة للردود</div>
        <div>✅ تقرير تفصيلي مع رسوم بيانية</div>
        <div>✅ أولوية الرد خلال ساعة</div>
      </div>
    </div>
    <div class="card" style="padding:16px;margin-top:4px">
      <div style="font-size:13px;font-weight:800;color:var(--text2);margin-bottom:10px">📈 حسابات الربح</div>
      <div style="display:flex;flex-direction:column;gap:8px;font-size:13px;color:var(--text3)">
        <div>5 عيادات أساسية = <span style="color:var(--green2);font-weight:700">2,500 ريال/شهر</span></div>
        <div>10 عيادات مختلطة = <span style="color:var(--green2);font-weight:700">~8,000 ريال/شهر</span></div>
        <div>تكاليف الأدوات = <span style="color:#f87171;font-weight:700">~430 ريال/شهر</span></div>
      </div>
    </div>
  </div>
`; }

// ── SETTINGS ──────────────────────────────────
function renderSettings() {
  const savedKey = localStorage.getItem('rp_api_key') || '';
  const maskedKey = savedKey ? '••••••••' + savedKey.slice(-6) : '';
  const hasKey = !!savedKey;
  return `
  <div style="padding:16px">
    <h2 style="font-size:18px;font-weight:800;margin-bottom:20px">⚙️ الإعدادات</h2>

    <div style="padding:16px;border-radius:16px;border:1px solid ${hasKey ? 'rgba(52,211,153,0.25)' : 'rgba(245,158,11,0.35)'};background:${hasKey ? 'rgba(52,211,153,0.04)' : 'rgba(245,158,11,0.05)'};margin-bottom:12px">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
        <div style="font-size:13px;font-weight:800;color:${hasKey ? 'var(--green2)' : '#fbbf24'}">${hasKey ? '✅ مفتاح API متصل' : '🔑 مفتاح API مطلوب'}</div>
        ${hasKey ? `<span class="tag tag-green" style="font-size:10px">نشط</span>` : `<span style="font-size:10px;padding:2px 8px;border-radius:6px;background:rgba(245,158,11,0.15);color:#fbbf24;font-weight:700">غير مُعيَّن</span>`}
      </div>
      ${hasKey ? `
        <div style="display:flex;align-items:center;gap:8px;padding:10px 12px;background:rgba(255,255,255,0.04);border-radius:8px;border:1px solid var(--border);margin-bottom:10px">
          <span id="key-display" style="flex:1;font-family:monospace;font-size:13px;color:var(--text2)">${maskedKey}</span>
          <button id="toggle-key-view" style="background:none;border:none;color:var(--text3);cursor:pointer;font-size:12px;padding:2px 6px">👁 عرض</button>
        </div>
      ` : `
        <div style="font-size:12px;color:var(--text3);margin-bottom:10px;line-height:1.65">احصل على مفتاحك من <span style="color:var(--blue2);font-weight:700">console.anthropic.com</span> ← API Keys</div>
      `}
      <input class="inp" id="api-key-input" type="password" placeholder="sk-ant-api03-..." style="font-family:monospace;font-size:13px;margin-bottom:8px" />
      <div style="display:flex;gap:8px">
        <button class="btn btn-primary" style="flex:1" id="save-api-key">💾 حفظ المفتاح</button>
        ${hasKey ? `<button class="btn btn-ghost" style="color:#f87171;border-color:rgba(239,68,68,0.2);padding:0 14px" id="clear-api-key">🗑</button>` : ''}
      </div>
    </div>

    <!-- Google Maps Key -->
    <div style="padding:16px;border-radius:16px;border:1px solid ${!!localStorage.getItem('gmaps_key') ? 'rgba(52,211,153,0.25)' : 'rgba(56,189,248,0.25)'};background:${!!localStorage.getItem('gmaps_key') ? 'rgba(52,211,153,0.04)' : 'rgba(56,189,248,0.04)'};margin-bottom:12px">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
        <div style="font-size:13px;font-weight:800;color:${!!localStorage.getItem('gmaps_key') ? 'var(--green2)' : 'var(--blue2)'}">
          ${!!localStorage.getItem('gmaps_key') ? '✅ Google Maps متصل' : '📍 Google Maps API (اختياري)'}
        </div>
        ${!!localStorage.getItem('gmaps_key') ? `<span class="tag tag-green" style="font-size:10px">نشط</span>` : `<span style="font-size:10px;padding:2px 8px;border-radius:6px;background:rgba(56,189,248,0.1);color:var(--blue2);font-weight:700">غير متصل</span>`}
      </div>
      <div style="font-size:12px;color:var(--text3);margin-bottom:10px;line-height:1.65">
        يجلب التقييمات مباشرة من Google Maps تلقائياً<br>
        <b style="color:var(--text2)">خطوات الإعداد:</b><br>
        1. اذهب لـ <span style="color:var(--blue2);font-weight:700">console.cloud.google.com</span><br>
        2. فعّل <span style="color:var(--blue2)">Places API (New)</span><br>
        3. أنشئ API Key وأضفه هنا
      </div>
      ${!!localStorage.getItem('gmaps_key') ? `
        <div style="padding:8px 12px;background:rgba(255,255,255,0.04);border-radius:8px;border:1px solid var(--border);margin-bottom:10px;font-family:monospace;font-size:13px;color:var(--text2)">
          ••••••••${(localStorage.getItem('gmaps_key')||'').slice(-6)}
        </div>
      ` : ''}
      <input class="inp" id="gmaps-key-input" type="password" placeholder="AIza..." style="font-family:monospace;font-size:13px;margin-bottom:8px" />
      <div style="display:flex;gap:8px">
        <button class="btn btn-primary" style="flex:1;background:linear-gradient(135deg,#1a73e8,#0d47a1)" id="save-gmaps-key">💾 حفظ مفتاح Google</button>
        ${!!localStorage.getItem('gmaps_key') ? `<button class="btn btn-ghost" style="color:#f87171;border-color:rgba(239,68,68,0.2);padding:0 14px" id="clear-gmaps-key">🗑</button>` : ''}
      </div>
    </div>

    <div class="card" style="padding:16px;margin-bottom:12px">
      <div style="font-size:13px;font-weight:700;color:var(--text2);margin-bottom:12px">البيانات</div>
      <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-bottom:1px solid var(--border)">
        <span style="font-size:14px">العيادات المحفوظة</span>
        <span class="tag tag-blue">${state.clinics.length}</span>
      </div>
      <button class="btn btn-ghost btn-full" style="margin-top:12px;color:#f87171;border-color:rgba(239,68,68,0.2)" id="clear-data">🗑️ مسح جميع البيانات</button>
    </div>
    <div class="card" style="padding:16px;margin-bottom:12px">
      <div style="font-size:13px;font-weight:700;color:var(--text2);margin-bottom:12px">التطبيق</div>
      <div style="font-size:13px;color:var(--text3);display:flex;flex-direction:column;gap:8px">
        <div style="display:flex;justify-content:space-between"><span>الإصدار</span><span>1.0.0</span></div>
        <div style="display:flex;justify-content:space-between"><span>النوع</span><span>PWA</span></div>
        <div style="display:flex;justify-content:space-between"><span>الذكاء الاصطناعي</span><span>Claude Sonnet 4</span></div>
      </div>
    </div>
    <div class="card-green" style="padding:14px">
      <div style="font-size:13px;font-weight:700;color:var(--green2);margin-bottom:6px">📲 تثبيت التطبيق</div>
      <div style="font-size:12px;color:var(--text3);margin-bottom:10px">أضفه لشاشتك الرئيسية للوصول السريع بدون متصفح</div>
      <div style="font-size:12px;color:var(--text2)">
        <div style="margin-bottom:4px">iOS: شارك ← إضافة للشاشة الرئيسية</div>
        <div>Android: القائمة ← تثبيت التطبيق</div>
      </div>
    </div>
  </div>
`; }

// ══════════════════════════════════════════════
// BIND EVENTS
// ══════════════════════════════════════════════
function bindWorkspace() {
  document.querySelectorAll('.step-tab').forEach(t =>
    t.addEventListener('click', () => { state.step = t.dataset.step; render(); })
  );
  // Search
  const sq = document.getElementById('sq');
  if (sq) { sq.addEventListener('input', e => state.searchQuery = e.target.value); sq.addEventListener('keydown', e => e.key==='Enter' && doSearch().then(render)); }
  const city = document.getElementById('city');
  if (city) city.addEventListener('input', e => state.clinicCity = e.target.value);
  const ctype = document.getElementById('ctype');
  if (ctype) ctype.addEventListener('change', e => state.clinicType = e.target.value);
  const ds = document.getElementById('do-search');
  if (ds) ds.addEventListener('click', () => doSearch().then(render));
  const dgf = document.getElementById('do-gmaps-fetch');
  if (dgf) dgf.addEventListener('click', () => doGmapsFetch().then(render));
  // Allow Enter key in URL input
  const gui = document.getElementById('gmaps-url-input');
  if (gui) gui.addEventListener('keydown', (e) => { if(e.key==='Enter') doGmapsFetch().then(render); });
  // Analyze
  const da = document.getElementById('do-analyze');
  if (da) da.addEventListener('click', () => doAnalyze().then(render));
  // Respond
  const dra = document.getElementById('do-respond-all');
  if (dra) dra.addEventListener('click', () => doRespondAll().then(render));
  document.querySelectorAll('.do-respond').forEach(b =>
    b.addEventListener('click', () => doRespond(parseInt(b.dataset.id)).then(render))
  );
  // Strategy
  const dst = document.getElementById('do-strategy');
  if (dst) dst.addEventListener('click', () => doStrategy().then(render));
  // Report
  const dr = document.getElementById('do-report');
  if (dr) dr.addEventListener('click', () => doReport().then(render));
}

function bindSettings() {
  const cd = document.getElementById('clear-data');
  if (cd) cd.addEventListener('click', () => {
    if (confirm('هل تريد مسح جميع البيانات؟')) {
      state.clinics = []; saveClinics(); showToast('تم المسح'); render();
    }
  });

  const saveBtn = document.getElementById('save-api-key');
  if (saveBtn) saveBtn.addEventListener('click', () => {
    const inp = document.getElementById('api-key-input');
    const val = inp ? inp.value.trim() : '';
    if (!val) { showToast('⚠️ أدخل المفتاح أولاً'); return; }
    if (!val.startsWith('sk-ant-')) { showToast('⚠️ المفتاح يجب أن يبدأ بـ sk-ant-'); return; }
    localStorage.setItem('rp_api_key', val);
    showToast('✅ تم حفظ المفتاح بنجاح!');
    render();
  });

  const clearKey = document.getElementById('clear-api-key');
  if (clearKey) clearKey.addEventListener('click', () => {
    if (confirm('هل تريد حذف مفتاح API؟')) {
      localStorage.removeItem('rp_api_key');
      showToast('🗑️ تم حذف المفتاح');
      render();
    }
  });

  const toggleBtn = document.getElementById('toggle-key-view');
  if (toggleBtn) toggleBtn.addEventListener('click', () => {
    const savedKey = localStorage.getItem('rp_api_key') || '';
    const disp = document.getElementById('key-display');
    const inp = document.getElementById('api-key-input');
    if (inp && inp.value === savedKey) {
      if (disp) disp.textContent = '••••••••' + savedKey.slice(-6);
      inp.value = '';
      toggleBtn.textContent = '👁 عرض';
    } else {
      if (disp) disp.textContent = savedKey;
      if (inp) inp.value = savedKey;
      toggleBtn.textContent = '🙈 إخفاء';
    }
  });

  // Google Maps key
  const saveGmaps = document.getElementById('save-gmaps-key');
  if (saveGmaps) saveGmaps.addEventListener('click', () => {
    const inp = document.getElementById('gmaps-key-input');
    const val = inp ? inp.value.trim() : '';
    if (!val) { showToast('⚠️ أدخل مفتاح Google أولاً'); return; }
    if (val.length < 10) { showToast('⚠️ المفتاح غير صحيح'); return; }
    localStorage.setItem('gmaps_key', val);
    showToast('✅ تم حفظ مفتاح Google!');
    loadGoogleMaps();
    render();
  });
  const clearGmaps = document.getElementById('clear-gmaps-key');
  if (clearGmaps) clearGmaps.addEventListener('click', () => {
    if (confirm('حذف مفتاح Google Maps؟')) {
      localStorage.removeItem('gmaps_key');
      const s = document.getElementById('gmap-script');
      if (s) s.remove();
      showToast('🗑️ تم حذف مفتاح Google');
      render();
    }
  });
}

// ══════════════════════════════════════════════
// GLOBAL HELPERS (called from inline onclick)
// ══════════════════════════════════════════════
window.goStep = (s) => { state.step = s; render(); };
window.goPage = (p) => { state.page = p; render(); };
window.copyText = copyText;

window.addReview = () => {
  state.reviews.push({ id: Date.now(), text: '', rating: 1, response: '' });
  render();
};
window.removeReview = (id) => {
  state.reviews = state.reviews.filter(r => r.id !== id);
  render();
};
window.setRating = (id, val) => {
  state.reviews = state.reviews.map(r => r.id === id ? { ...r, rating: val } : r);
  render();
};
window.updateReview = (id, field, val) => {
  state.reviews = state.reviews.map(r => r.id === id ? { ...r, [field]: val } : r);
};

// ══════════════════════════════════════════════
// NAV
// ══════════════════════════════════════════════
document.querySelectorAll('.nav-btn').forEach(b =>
  b.addEventListener('click', () => { state.page = b.dataset.page; render(); })
);

// ══════════════════════════════════════════════
// PWA INSTALL
// ══════════════════════════════════════════════
let deferredPrompt = null;
window.addEventListener('beforeinstallprompt', (e) => {
  e.preventDefault();
  deferredPrompt = e;
  if (!localStorage.getItem('rp_install_dismissed')) {
    document.getElementById('install-banner').classList.add('show');
  }
});
document.getElementById('install-btn').addEventListener('click', async () => {
  if (deferredPrompt) {
    deferredPrompt.prompt();
    const { outcome } = await deferredPrompt.userChoice;
    if (outcome === 'accepted') showToast('🎉 تم التثبيت!');
    deferredPrompt = null;
  }
  document.getElementById('install-banner').classList.remove('show');
});
document.getElementById('dismiss-banner').addEventListener('click', () => {
  document.getElementById('install-banner').classList.remove('show');
  localStorage.setItem('rp_install_dismissed', '1');
});

// ══════════════════════════════════════════════
// SERVICE WORKER
// ══════════════════════════════════════════════
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js').catch(() => {});
}

// ══════════════════════════════════════════════
// INIT
// ══════════════════════════════════════════════
render();
</script>
</body>
</html>
