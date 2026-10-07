// ---- Zgody cookies: baner, panel ustawień, wycofanie zgody (RODO art. 7 ust. 3).
// Wspólne dla wszystkich stron i języków. Wymaga i18n.js (P25_T.ck).
// Każdy element z atrybutem [data-cookie-settings] otwiera panel ustawień.
(function(){
  const KEY = 'p25_cookie_consent';
  const GA_ID = 'G-K0J6DQPGLL';
  const PIXEL_ID = '887690594397355';
  const T = (window.P25_T || {}).ck;
  if (!T) return;

  // Odczyt zgody; zgodność wstecz ze starym formatem 'accept' / 'decline'
  function read() {
    let raw = null;
    try { raw = localStorage.getItem(KEY); } catch (e) {}
    if (raw === 'accept') return { a: true, m: true };
    if (raw === 'decline') return { a: false, m: false };
    try { const v = JSON.parse(raw); if (v && typeof v === 'object') return { a: !!v.a, m: !!v.m }; } catch (e) {}
    return null;
  }
  function write(c) {
    try { localStorage.setItem(KEY, JSON.stringify({ a: c.a, m: c.m, t: new Date().toISOString() })); } catch (e) {}
  }

  // ---- ładowanie narzędzi (tylko po zgodzie)
  function loadGA() {
    if (GA_ID === 'G-XXXXXXXXXX' || window.gtag) return;
    const s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function(){ dataLayer.push(arguments); };
    gtag('js', new Date());
    gtag('config', GA_ID, { anonymize_ip: true });
  }
  function loadPixel() {
    if (location.hostname !== 'plaszowska25.pl') return; // nie śledzimy stagingu ani adresu testowego OVH
    if (window.fbq) return;
    !function(f,b,e,v,n,t,s)
    {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
    n.callMethod.apply(n,arguments):n.queue.push(arguments)};
    if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
    n.queue=[];t=b.createElement(e);t.async=!0;
    t.src=v;s=b.getElementsByTagName(e)[0];
    s.parentNode.insertBefore(t,s)}(window, document,'script',
    'https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', PIXEL_ID);
    fbq('track', 'PageView');
  }
  function apply(c) {
    if (c.a) loadGA();
    if (c.m) loadPixel();
  }

  // Usunięcie cookies narzędzi po wycofaniu zgody (wszystkie warianty domeny)
  function clearCookies(prefixes) {
    const host = location.hostname.split('.');
    const domains = [''];
    for (let i = 0; i < host.length - 1; i++) domains.push('; domain=.' + host.slice(i).join('.'));
    document.cookie.split(';').forEach(c => {
      const name = c.split('=')[0].trim();
      if (!prefixes.some(p => name.startsWith(p))) return;
      domains.forEach(d => { document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/' + d; });
    });
  }

  function save(next) {
    const prev = read() || { a: false, m: false };
    write(next);
    hideBanner(); closePanel();
    const revoked = (prev.a && !next.a) || (prev.m && !next.m);
    if (revoked) {
      if (prev.a && !next.a) { window['ga-disable-' + GA_ID] = true; clearCookies(['_ga', '_gid', '_gat']); }
      if (prev.m && !next.m) { if (window.fbq) fbq('consent', 'revoke'); clearCookies(['_fbp', '_fbc']); }
      // skrypty już załadowane da się w pełni wyłączyć tylko przeładowaniem strony
      toast(T.saved);
      setTimeout(() => location.reload(), 900);
      return;
    }
    apply(next);
    toast(T.saved);
  }

  // ---- UI
  const el = (html) => { const d = document.createElement('div'); d.innerHTML = html.trim(); return d.firstChild; };

  // stary, statyczny baner z HTML (jeśli jeszcze jest) — zastępujemy nowym
  const legacy = document.getElementById('cookie');
  if (legacy) legacy.remove();

  const banner = el(`
    <div id="cookie" role="dialog" aria-live="polite" aria-label="${T.title}">
      <div class="ck-t"><strong>${T.title}</strong>${T.text}</div>
      <div class="ck-actions">
        <button type="button" class="ck-btn link" data-ck="settings">${T.settings}</button>
        <button type="button" class="ck-btn ghost" data-ck="decline">${T.decline}</button>
        <button type="button" class="ck-btn primary" data-ck="accept">${T.accept}</button>
      </div>
    </div>`);

  const panel = el(`
    <div id="ckPanel" role="dialog" aria-modal="true" aria-labelledby="ckPanelTitle" hidden>
      <div class="ckp-card">
        <button type="button" class="ckp-close" data-ck="close" aria-label="${T.close}">✕</button>
        <h3 id="ckPanelTitle">${T.panelTitle}</h3>
        <p class="ckp-intro">${T.panelIntro}</p>
        <div class="ckp-row">
          <div><strong>${T.necessary}</strong><p>${T.necessaryDesc}</p></div>
          <span class="ckp-always">${T.always}</span>
        </div>
        <label class="ckp-row">
          <div><strong>${T.analytics}</strong><p>${T.analyticsDesc}</p></div>
          <span class="ckp-switch"><input type="checkbox" id="ckA" /><span aria-hidden="true"></span></span>
        </label>
        <label class="ckp-row">
          <div><strong>${T.marketing}</strong><p>${T.marketingDesc}</p></div>
          <span class="ckp-switch"><input type="checkbox" id="ckM" /><span aria-hidden="true"></span></span>
        </label>
        <div class="ckp-actions">
          <button type="button" class="ck-btn ghost" data-ck="reject">${T.rejectAll}</button>
          <button type="button" class="ck-btn ghost" data-ck="save">${T.save}</button>
          <button type="button" class="ck-btn primary" data-ck="accept">${T.acceptAll}</button>
        </div>
      </div>
    </div>`);

  const toastEl = el('<div id="ckToast" role="status" aria-live="polite"></div>');
  document.body.append(banner, panel, toastEl);

  const ckA = panel.querySelector('#ckA'), ckM = panel.querySelector('#ckM');
  let lastFocus = null;

  function showBanner() { banner.classList.add('on'); }
  function hideBanner() { banner.classList.remove('on'); }
  function openPanel() {
    const c = read() || { a: false, m: false };
    ckA.checked = c.a; ckM.checked = c.m;
    lastFocus = document.activeElement;
    panel.hidden = false;
    requestAnimationFrame(() => panel.classList.add('on'));
    panel.querySelector('.ckp-close').focus();
  }
  function closePanel() {
    if (panel.hidden) return;
    panel.classList.remove('on');
    panel.hidden = true;
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }
  let toastTimer;
  function toast(msg) {
    toastEl.textContent = msg;
    toastEl.classList.add('on');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toastEl.classList.remove('on'), 2400);
  }

  document.addEventListener('click', e => {
    const opener = e.target.closest('[data-cookie-settings]');
    if (opener) { e.preventDefault(); openPanel(); return; }
    const b = e.target.closest('[data-ck]');
    if (!b) { if (e.target === panel) closePanel(); return; }
    const act = b.getAttribute('data-ck');
    if (act === 'accept')  save({ a: true, m: true });
    if (act === 'decline' || act === 'reject') save({ a: false, m: false });
    if (act === 'save')    save({ a: ckA.checked, m: ckM.checked });
    if (act === 'settings') openPanel();
    if (act === 'close')   closePanel();
  });
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && !panel.hidden) closePanel(); });

  const saved = read();
  if (saved) apply(saved);
  else showBanner();

  // ---- konwersje: jedno wywołanie wysyła zdarzenie do GA4 i Meta. Każde narzędzie
  // dostaje je tylko wtedy, gdy jest załadowane, czyli po odpowiedniej zgodzie.
  window.P25_track = function(gaEvent, metaEvent, params) {
    const p = Object.assign({ page_language: document.documentElement.lang }, params || {});
    if (gaEvent && window.gtag) gtag('event', gaEvent, p);
    if (metaEvent && window.fbq) fbq('track', metaEvent);
  };
  // Kliknięcia w telefon i e-mail centrum (na każdej stronie)
  document.addEventListener('click', e => {
    const a = e.target.closest('a[href^="tel:"], a[href^="mailto:"]');
    if (!a) return;
    const isTel = a.href.startsWith('tel:');
    window.P25_track(isTel ? 'click_phone' : 'click_email', 'Contact', {
      link_url: a.href.split('?')[0],
      link_location: a.closest('footer') ? 'footer' : a.closest('.mbar') ? 'mobile_bar' : 'page'
    });
  });

  window.P25_openCookieSettings = openPanel;
})();
