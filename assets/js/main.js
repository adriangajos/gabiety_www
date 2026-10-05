// Teksty interfejsu w języku strony (i18n.js); treść maili do biura zawsze po polsku.
const T  = window.P25_T;
const PL = window.P25_PL;
const LANG = window.P25_LANG || 'pl';

// ---- apply tweak values to DOM
// Na wersjach EN/UA podmieniamy tylko dane kontaktowe i kolory — teksty są przetłumaczone w HTML.
const TWEAK_ANY_LANG = ['address', 'phone', 'email'];
function applyTweaks(t) {
  document.querySelectorAll('[data-tw]').forEach(el => {
    const k = el.getAttribute('data-tw');
    if (t[k] == null) return;
    if (LANG !== 'pl' && !TWEAK_ANY_LANG.includes(k)) return;
    if (k === 'email') {
      el.innerHTML = '<a href="mailto:' + t[k] + '?subject=Rezerwacja%20Gabinetu">' + t[k] + '</a>';
    } else if (k === 'phone') {
      el.innerHTML = '<a href="tel:' + t[k].replace(/[^+\d]/g, '') + '">' + t[k] + '</a>';
    } else if (el.hasAttribute('data-tw-html')) {
      el.innerHTML = t[k];
    } else {
      el.textContent = t[k];
    }
  });
  document.documentElement.style.setProperty('--accent', t.accent);
  document.documentElement.style.setProperty('--paper', t.paper);
  document.documentElement.style.setProperty('--paper-2',
    'color-mix(in oklab, ' + t.paper + ' 80%, black 8%)');
}
applyTweaks(TWEAKS);

// ---- tweak panel wiring
const panel = document.getElementById('tweaks');
panel.querySelectorAll('[data-k]').forEach(input => {
  const k = input.getAttribute('data-k');
  input.value = TWEAKS[k] ?? '';
  input.addEventListener('input', () => {
    TWEAKS[k] = input.value;
    applyTweaks(TWEAKS);
    window.parent.postMessage({ type: '__edit_mode_set_keys', edits: { [k]: input.value } }, '*');
  });
});

// ---- edit-mode protocol
window.addEventListener('message', (e) => {
  if (!e.data || typeof e.data !== 'object') return;
  if (e.data.type === '__activate_edit_mode') panel.classList.add('on');
  if (e.data.type === '__deactivate_edit_mode') panel.classList.remove('on');
});
window.parent.postMessage({ type: '__edit_mode_available' }, '*');

// ---- mobile nav
const sheet = document.getElementById('sheet');
document.getElementById('burger').onclick = () => sheet.classList.add('on');
document.getElementById('closeSheet').onclick = () => sheet.classList.remove('on');
sheet.querySelectorAll('a').forEach(a => a.onclick = () => sheet.classList.remove('on'));

// hide "Zarezerwuj" btn on very small screens
const mq = window.matchMedia('(max-width: 640px)');
function applyMq() {
  document.querySelectorAll('[data-hide-mobile]').forEach(el => {
    el.style.display = mq.matches ? 'none' : '';
  });
}
mq.addEventListener('change', applyMq); applyMq();

// ---- Pasek akcji na telefonie: pojawia się po przewinięciu za sekcję hero
(function(){
  const bar = document.getElementById('mbar');
  const hero = document.querySelector('.hero');
  if (!bar || !hero || !('IntersectionObserver' in window)) { if (bar) bar.classList.add('on'); return; }
  new IntersectionObserver(([entry]) => {
    bar.classList.toggle('on', !entry.isIntersecting);
  }, { threshold: 0 }).observe(hero);
})();

// Blokada przewijania strony pod oknem; iOS Safari wymaga ustawienia na <html> i <body>
function lockScroll(on) {
  document.documentElement.style.overflow = on ? 'hidden' : '';
  document.body.style.overflow = on ? 'hidden' : '';
}

// ---- Wspólna obsługa okien dialogowych (fokus, Esc, blokada scrolla)
function makeDialog(root, { onOpen } = {}) {
  let lastFocus = null;
  const scroller = root.querySelector('.bk-scroll');
  function open(...args) {
    lastFocus = document.activeElement;
    if (onOpen) onOpen(...args);
    root.classList.add('on');
    lockScroll(true);
    if (scroller) scroller.scrollTop = 0;
    const first = root.querySelector('input, button.bk-close');
    if (first) setTimeout(() => first.focus({ preventScroll: true }), 30);
  }
  function close() {
    root.classList.remove('on');
    lockScroll(false);
    if (lastFocus && lastFocus.focus) lastFocus.focus({ preventScroll: true });
  }
  root.addEventListener('click', e => { if (e.target === root) close(); });
  window.addEventListener('keydown', e => { if (e.key === 'Escape' && root.classList.contains('on')) close(); });
  return { open, close, isOpen: () => root.classList.contains('on') };
}

// Wysyłka przez Web3Forms (ten sam klucz co formularz rezerwacji)
async function sendWeb3Forms(payload) {
  const key = (typeof WEB3FORMS_KEY !== 'undefined') ? WEB3FORMS_KEY : '';
  if (!key || key === 'WKLEJ-TUTAJ-ACCESS-KEY') {
    console.warn('Brak skonfigurowanego WEB3FORMS_KEY, wiadomość nie została wysłana.', payload);
    return true;
  }
  const res = await fetch('https://api.web3forms.com/submit', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
    body: JSON.stringify({ access_key: key, ...payload })
  });
  const data = await res.json();
  if (!data.success) throw new Error(data.message || 'Błąd wysyłki');
  return true;
}
const LANG_NOTE = LANG === 'pl' ? '' : `\nJęzyk strony: ${LANG === 'en' ? 'angielski (EN)' : 'ukraiński (UKR)'}. Odpowiedz w tym języku lub po angielsku.\n`;

// ---- Live schedule from Firebase + formularz zapytania rezerwacyjnego
(function(){
  const ROOMS = 7;
  // Typy gabinetów wg nagłówka tabeli (G1..G7) — klucze polskie, etykiety z i18n
  const ROOM_TYPES = ['Mały','Duży','Mały','Mały','Duży','Mały','Biurowy'];
  // Cennik brutto (zł) — biurowy rozliczany jak mały
  const PRICES = {
    'Mały':    { AM: 250, PM: 299, DAY: 500 },
    'Duży':    { AM: 350, PM: 399, DAY: 600 },
    'Biurowy': { AM: 250, PM: 299, DAY: 500 }
  };
  const SLOT_TEXT    = { AM: T.slotAM,  PM: T.slotPM };
  const SLOT_TEXT_PL = { AM: PL.slotAM, PM: PL.slotPM };
  // Koniec bloku (godzina w Krakowie) — po nim blok nie liczy się już jako „dziś wolny"
  const SLOT_END = { AM: 15, PM: 23 };

  const tbody = document.getElementById('crmBody');
  const todayEl = document.getElementById('todayFree');
  let occupied = new Set();
  // Czy dotarł już pierwszy snapshot z Firestore. Dopóki false, nie pokazujemy
  // slotów jako „Wolne" (bo pusty `occupied` = wszystko wolne), tylko placeholder
  // ładowania — inaczej przy zimnym wejściu widać fałszywie all-free.
  let loaded = false;

  // Firestore key format: {roomNumber}-{dayIndex}-{AM|PM} (room 1–7, day 0=Pon…6=Nd)
  function buildKey(roomIdx, dayIdx, slot) {
    return (roomIdx + 1) + '-' + dayIdx + '-' + slot.toUpperCase();
  }

  // Dzień tygodnia (0=Pon) i godzina w Krakowie — niezależnie od strefy odwiedzającego
  function krakowNow() {
    const parts = new Intl.DateTimeFormat('en-GB', { timeZone: 'Europe/Warsaw', weekday: 'short', hour: '2-digit', hour12: false }).formatToParts(new Date());
    const wd = parts.find(p => p.type === 'weekday').value;
    const hour = +parts.find(p => p.type === 'hour').value % 24;
    return { day: ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'].indexOf(wd), hour };
  }
  function isTodaySlotOpen(now, di, slot) { return di === now.day && now.hour < SLOT_END[slot]; }

  // Weekend (Sob–Nd) domyślnie zwinięty; stan przeżywa re-render po snapshocie
  let weekendOpen = false;

  function render() {
    const now = krakowNow();
    let freeToday = 0;
    let html = '';
    T.days.forEach((dayName, di) => {
      [['AM', T.am, '6:00 – 15:00'], ['PM', T.pm, '15:00 – 23:00']].forEach(([slot, label, hours], si) => {
        html += di >= 5 ? `<tr class="wk-row"${weekendOpen ? '' : ' hidden'}>` : '<tr>';
        if (si === 0) html += `<td class="col-day" rowspan="2">${dayName}</td>`;
        html += `<td class="col-pora"><span class="pora-label">${label}</span><span class="pora-hours">${hours}</span></td>`;
        for (let r = 0; r < ROOMS; r++) {
          const title = `${dayName} · ${T.room} ${r+1} · ${hours.replace(/ /g,'')}`;
          if (!loaded) {
            html += `<td class="col-slot"><span class="pill loading" data-title="${title}" aria-label="${T.loading}">···</span></td>`;
            continue;
          }
          const isBusy = occupied.has(buildKey(r, di, slot));
          const openToday = !isBusy && isTodaySlotOpen(now, di, slot);
          if (openToday) freeToday++;
          const cls = isBusy ? 'busy' : 'free';
          const txt = isBusy ? T.busy : T.free;
          const data = isBusy ? '' : ` data-r="${r}" data-d="${di}" data-s="${slot}" role="button" tabindex="0"`;
          html += `<td class="col-slot"><span class="pill ${cls}" data-title="${title}"${data}>${txt}</span></td>`;
        }
        html += '</tr>';
      });
    });
    html += `<tr class="wk-toggle"><td colspan="${ROOMS + 2}"><button type="button" aria-expanded="${weekendOpen}">${weekendOpen ? T.weekendHide : T.weekendShow}<span class="wk-chev" aria-hidden="true">▾</span></button></td></tr>`;

    tbody.innerHTML = html;

    tbody.querySelector('.wk-toggle button').addEventListener('click', () => {
      weekendOpen = !weekendOpen;
      render();
    });

    tbody.querySelectorAll('.pill.free').forEach(el => {
      const go = () => booking.open(+el.dataset.r, +el.dataset.d, el.dataset.s);
      el.addEventListener('click', go);
      el.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); go(); } });
    });

    if (todayEl) {
      todayEl.innerHTML = !loaded ? '' : (freeToday ? T.todayFree(freeToday) : T.todayNone);
    }
  }

  // ===== Formularz zapytania rezerwacyjnego (popup) =====
  const bk       = document.getElementById('bk');
  const bkCal    = document.getElementById('bkCal');
  const bkQuote  = document.getElementById('bkQuote');
  const bkForm   = document.getElementById('bkForm');
  const bkScroll = bk.querySelector('.bk-scroll');
  const bkSuccess= document.getElementById('bkSuccess');
  const bkError  = document.getElementById('bkError');
  const bkSubmit = document.getElementById('bkSubmit');
  const selected = new Set(); // klucze "r-d-SLOT"

  function fillBanner(target) {
    const t = (typeof TWEAKS !== 'undefined') ? TWEAKS : {};
    const email = t.email || 'gabinety@plaszowska25.pl';
    target.innerHTML =
      `<span class="bk-banner-t">${T.bannerTitle}</span>
       <span class="bk-banner-row">
         <a href="tel:${(t.phone||'').replace(/\s/g,'')}">${t.phone||''}</a>
         <a href="mailto:${email}">${email}</a>
       </span>`;
  }

  function buildCalendar() {
    let html = '<table class="bk-grid"><thead><tr><th class="bk-gc"></th><th class="bk-gc"></th>';
    for (let r = 0; r < ROOMS; r++) {
      html += `<th>${T.room} ${r+1}<span>${T.roomTypes[ROOM_TYPES[r]]}</span></th>`;
    }
    html += '</tr></thead><tbody>';
    T.days.forEach((dayName, di) => {
      ['AM','PM'].forEach((slot, si) => {
        html += '<tr>';
        if (si === 0) html += `<td class="bk-gday" rowspan="2">${dayName}</td>`;
        html += `<td class="bk-gpora">${slot === 'AM' ? T.amShort : T.pmShort}</td>`;
        for (let r = 0; r < ROOMS; r++) {
          const key = r + '-' + di + '-' + slot;
          if (occupied.has(buildKey(r, di, slot))) {
            html += `<td><span class="bk-cell busy" title="${T.busy}">✕</span></td>`;
          } else {
            const sel = selected.has(key);
            html += `<td><button type="button" class="bk-cell free${sel ? ' sel' : ''}" data-key="${key}" aria-pressed="${sel}" title="${dayName} · ${T.room} ${r+1} · ${SLOT_TEXT[slot]}"></button></td>`;
          }
        }
        html += '</tr>';
      });
    });
    html += '</tbody></table>';
    bkCal.innerHTML = html;

    bkCal.querySelectorAll('.bk-cell.free').forEach(btn => {
      btn.addEventListener('click', () => {
        const k = btn.dataset.key;
        if (selected.has(k)) { selected.delete(k); btn.classList.remove('sel'); btn.setAttribute('aria-pressed','false'); }
        else { selected.add(k); btn.classList.add('sel'); btn.setAttribute('aria-pressed','true'); }
        updateQuote();
      });
    });
  }

  // lines[].label — w języku strony; lines[].labelPl — do maila dla biura
  function computeQuote() {
    const groups = {};
    selected.forEach(k => {
      const [r, d, slot] = k.split('-');
      const id = r + '-' + d;
      const g = groups[id] || (groups[id] = { r: +r, d: +d, am: false, pm: false });
      if (slot === 'AM') g.am = true; else g.pm = true;
    });
    const lines = [];
    let total = 0;
    Object.values(groups).sort((a, b) => a.d - b.d || a.r - b.r).forEach(g => {
      const type = ROOM_TYPES[g.r];
      const p = PRICES[type];
      const room   = `${T.room} ${g.r+1} (${T.roomTypes[type]})`;
      const roomPl = `Gabinet ${g.r+1} (${type})`;
      if (g.am && g.pm) {
        lines.push({ label: `${T.days[g.d]} · ${room} · ${T.fullDay}`, labelPl: `${PL.days[g.d]} · ${roomPl} · ${PL.fullDay}`, price: p.DAY });
        total += p.DAY;
      } else {
        const slot = g.am ? 'AM' : 'PM';
        lines.push({ label: `${T.days[g.d]} · ${room} · ${SLOT_TEXT[slot]}`, labelPl: `${PL.days[g.d]} · ${roomPl} · ${SLOT_TEXT_PL[slot]}`, price: p[slot] });
        total += p[slot];
      }
    });
    return { lines, total };
  }

  function updateQuote() {
    const { lines, total } = computeQuote();
    if (!lines.length) {
      bkQuote.innerHTML = `<div class="bk-quote-empty">${T.quoteEmpty}</div>`;
      return;
    }
    let html = `<h4>${T.quoteTitle}</h4><ul class="bk-quote-list">`;
    lines.forEach(l => {
      html += `<li><span>${l.label}</span><span class="bk-price">${l.price} ${T.currency}</span></li>`;
    });
    html += `</ul><div class="bk-quote-total"><span>${T.quoteTotal}</span><span>${total} ${T.currency}</span></div>`;
    html += `<p class="bk-quote-note">${T.quoteNote}</p>`;
    bkQuote.innerHTML = html;
    if (lines.length) bkError.hidden = true;
  }

  const booking = makeDialog(bk, {
    onOpen(preR, preD, preSlot) {
      selected.clear();
      if (preSlot) selected.add(preR + '-' + preD + '-' + preSlot);
      bkForm.hidden = false;
      bkSuccess.hidden = true;
      bkError.hidden = true;
      bkError.textContent = T.pickSlot;
      bkSubmit.disabled = false;
      bkSubmit.textContent = T.send;
      fillBanner(document.getElementById('bkBanner'));
      buildCalendar();
      updateQuote();
    }
  });

  // wszystkie przyciski rezerwacji (nagłówek, cennik, pasek mobilny) otwierają formularz bez wstępnego terminu
  document.querySelectorAll('.js-open-booking').forEach(btn => {
    btn.addEventListener('click', e => { e.preventDefault(); booking.open(); });
  });
  document.getElementById('bkClose').addEventListener('click', booking.close);
  document.getElementById('bkDone').addEventListener('click', booking.close);

  bkForm.addEventListener('submit', async e => {
    e.preventDefault();
    const { lines, total } = computeQuote();
    if (!lines.length) { bkError.textContent = T.pickSlot; bkError.hidden = false; return; }
    if (!bkForm.reportValidity()) return;

    const name  = document.getElementById('bkName').value.trim();
    const email = document.getElementById('bkEmail').value.trim();
    const phone = document.getElementById('bkPhone').value.trim();
    const spec  = document.getElementById('bkSpec').value.trim();
    const note  = document.getElementById('bkMsg').value.trim();

    const message =
      `Nowe zapytanie rezerwacyjne | Płaszowska 25\n\n` +
      `Imię i nazwisko: ${name}\n` +
      `E-mail: ${email}\n` +
      `Telefon: ${phone}\n` +
      (spec ? `Specjalizacja: ${spec}\n` : '') +
      LANG_NOTE +
      `\nWybrane terminy:\n` +
      lines.map(l => `• ${l.labelPl}: ${l.price} zł`).join('\n') +
      `\n\nSzacunkowa wycena (za tydzień najmu): ${total} zł\n` +
      (note ? `\nWiadomość:\n${note}\n` : '');

    bkSubmit.disabled = true;
    bkSubmit.textContent = T.sending;
    try {
      await sendWeb3Forms({
        subject: 'Nowe zapytanie rezerwacyjne | Płaszowska 25',
        from_name: name, replyto: email,
        name, email, phone, message
      });
      showSuccess();
    } catch (err) {
      console.warn('Web3Forms error:', err);
      bkError.hidden = false;
      bkError.textContent = T.sendError;
      bkSubmit.disabled = false;
      bkSubmit.textContent = T.send;
    }
  });

  function showSuccess() {
    bkForm.hidden = true;
    bkSuccess.hidden = false;
    if (bkScroll) bkScroll.scrollTop = 0;
    if (window.fbq) fbq('track', 'Lead'); // konwersja: wysłane zapytanie rezerwacyjne
  }

  // ===== Formularz „Umów oglądanie gabinetu" (popup) =====
  (function(){
    const vw = document.getElementById('vw');
    if (!vw) return;
    const form    = document.getElementById('vwForm');
    const dateIn  = document.getElementById('vwDate');
    const timeIn  = document.getElementById('vwTime');
    const err     = document.getElementById('vwError');
    const submit  = document.getElementById('vwSubmit');
    const success = document.getElementById('vwSuccess');

    // opcje pory dnia z i18n
    timeIn.innerHTML = Object.entries(T.viewTimes).map(([k, v]) => `<option value="${k}">${v}</option>`).join('');

    const iso = d => d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0');
    function setDateBounds() {
      const min = new Date(); min.setDate(min.getDate() + 1);
      const max = new Date(); max.setDate(max.getDate() + 90);
      dateIn.min = iso(min); dateIn.max = iso(max);
    }

    const viewing = makeDialog(vw, {
      onOpen() {
        setDateBounds();
        form.hidden = false; success.hidden = true; err.hidden = true;
        submit.disabled = false; submit.textContent = T.viewSend;
        fillBanner(document.getElementById('vwBanner'));
      }
    });
    document.querySelectorAll('.js-open-viewing').forEach(btn => {
      btn.addEventListener('click', e => { e.preventDefault(); sheet.classList.remove('on'); viewing.open(); });
    });
    document.getElementById('vwClose').addEventListener('click', viewing.close);
    document.getElementById('vwDone').addEventListener('click', viewing.close);

    form.addEventListener('submit', async e => {
      e.preventDefault();
      err.hidden = true;
      if (!dateIn.value) { err.textContent = T.viewPickDate; err.hidden = false; dateIn.focus(); return; }
      if (!form.reportValidity()) return;

      const name  = document.getElementById('vwName').value.trim();
      const email = document.getElementById('vwEmail').value.trim();
      const phone = document.getElementById('vwPhone').value.trim();
      const note  = document.getElementById('vwMsg').value.trim();
      const [y, m, d] = dateIn.value.split('-').map(Number);
      const datePl = new Date(y, m - 1, d).toLocaleDateString('pl-PL', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' });

      const message =
        `Prośba o oglądanie gabinetu | Płaszowska 25\n\n` +
        `Imię i nazwisko: ${name}\n` +
        `E-mail: ${email}\n` +
        `Telefon: ${phone}\n` +
        LANG_NOTE +
        `\nPreferowany termin oglądania: ${datePl}\n` +
        `Preferowana pora: ${PL.viewTimes[timeIn.value]}\n` +
        (note ? `\nWiadomość:\n${note}\n` : '') +
        `\n(Termin wymaga potwierdzenia: odezwij się do klienta.)`;

      submit.disabled = true; submit.textContent = T.sending;
      try {
        await sendWeb3Forms({
          subject: `Oglądanie gabinetu: ${datePl}, ${name}`,
          from_name: name, replyto: email,
          name, email, phone, message
        });
        form.hidden = true; success.hidden = false;
        if (window.fbq) fbq('track', 'Schedule'); // konwersja: prośba o oglądanie
      } catch (ex) {
        console.warn('Web3Forms error:', ex);
        err.textContent = T.sendError; err.hidden = false;
        submit.disabled = false; submit.textContent = T.viewSend;
      }
    });
  })();

  // Stan początkowy (ładowanie)
  render();
  // licznik „dziś wolnych" aktualizuje się z upływem czasu
  setInterval(() => { if (loaded) render(); }, 5 * 60 * 1000);

  // Połączenie z Firebase — czekaj na SDK
  function initFirebase() {
    if (typeof firebase === 'undefined' || !firebase.firestore) {
      setTimeout(initFirebase, 100);
      return;
    }

    if (!firebase.apps.length) {
      firebase.initializeApp({
        apiKey: 'AIzaSyAiiRA2GjCuOd7_CezBu6HDqBQCp01qMNo',
        authDomain: 'gabinety-plaszowska.firebaseapp.com',
        projectId: 'gabinety-plaszowska',
        storageBucket: 'gabinety-plaszowska.firebasestorage.app',
        messagingSenderId: '383190262104',
        appId: '1:383190262104:web:a13ce66ab5c3cabd17052d'
      });
    }

    const db = firebase.firestore();
    const scheduleRef = db.collection(
      'artifacts/gabinety-plaszowska/users/shared/schedule'
    );

    scheduleRef.onSnapshot(snapshot => {
      occupied = new Set(snapshot.docs.map(d => d.id));
      loaded = true;
      render();
    }, err => {
      console.warn('Schedule fetch error:', err);
      // Awaria odczytu — zdejmij placeholder, żeby nie utknąć na „ładowaniu".
      loaded = true;
      render();
    });

    // Popup promocyjny — dokument zarządzany w CRM („Aktualna promocja").
    // Treść promocji jest po polsku, więc pokazujemy ją tylko na polskiej wersji.
    if (LANG === 'pl') {
      db.doc('artifacts/gabinety-plaszowska/users/shared/settings/promotion')
        .get()
        .then(doc => { if (doc.exists) showPromo(doc.data()); })
        .catch(err => console.warn('Promo fetch error:', err));
    }
  }

  function showPromo(p) {
    if (!p || p.publishAsPopup !== true) return;
    const header = (p.header || '').trim();
    const text   = (p.text || '').trim();
    if (!header && !text) return;

    // Nie naprzykrzaj się: pokaż raz na sesję; nowa promocja (zmiana updatedAt)
    // pokaże się ponownie.
    const sig = 'promo:' + (p.updatedAt || header + '|' + text);
    try { if (sessionStorage.getItem(sig) === 'seen') return; } catch (e) {}

    const wrap = document.getElementById('promo');
    if (!wrap) return;
    document.getElementById('promoHeader').textContent = header;
    document.getElementById('promoText').textContent = text;

    const close = () => {
      wrap.classList.remove('on');
      try { sessionStorage.setItem(sig, 'seen'); } catch (e) {}
    };
    document.getElementById('promoClose').addEventListener('click', close);
    document.getElementById('promoOk').addEventListener('click', close);
    wrap.addEventListener('click', e => { if (e.target === wrap) close(); });
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape' && wrap.classList.contains('on')) close();
    });

    wrap.classList.add('on');
  }

  initFirebase();
})();

// ---- OSM map (Leaflet)
window.addEventListener('load', () => {
  if (typeof L === 'undefined') return;
  const el = document.getElementById('osm-map');
  if (!el) return;
  const lat = 50.0395, lon = 19.9670;
  const map = L.map(el, { zoomControl: true, scrollWheelZoom: false }).setView([lat, lon], 16);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    maxZoom: 19
  }).addTo(map);
  const icon = L.divIcon({ className: 'pin-pulse', iconSize: [18,18], iconAnchor: [9,9] });
  L.marker([lat, lon], { icon }).addTo(map)
    .bindPopup('<b>Płaszowska 25</b>' + T.mapPopup)
    .openPopup();
});

// ---- Lightbox
(function(){
  const tiles = Array.from(document.querySelectorAll('.tile'));
  const lb = document.getElementById('lb');
  const lbImg = lb.querySelector('.lb-img');
  const lbI = document.getElementById('lbI');
  const lbN = document.getElementById('lbN');
  let idx = 0;

  lbN.textContent = tiles.length;

  function show(i) {
    idx = (i + tiles.length) % tiles.length;
    const src = tiles[idx].querySelector('img').getAttribute('src');
    const alt = tiles[idx].querySelector('img').getAttribute('alt') || '';
    lbImg.src = src; lbImg.alt = alt;
    lbI.textContent = idx + 1;
    lb.classList.add('on');
    lockScroll(true);
  }
  function close() { lb.classList.remove('on'); lockScroll(false); }

  tiles.forEach((t, i) => t.addEventListener('click', () => show(i)));
  lb.querySelector('.lb-prev').onclick = (e) => { e.stopPropagation(); show(idx - 1); };
  lb.querySelector('.lb-next').onclick = (e) => { e.stopPropagation(); show(idx + 1); };
  lb.querySelector('.lb-close').onclick = close;
  lb.addEventListener('click', (e) => { if (e.target === lb) close(); });

  window.addEventListener('keydown', (e) => {
    if (!lb.classList.contains('on')) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowLeft') show(idx - 1);
    if (e.key === 'ArrowRight') show(idx + 1);
  });
})();
