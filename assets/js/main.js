// ---- apply tweak values to DOM
function applyTweaks(t) {
  document.querySelectorAll('[data-tw]').forEach(el => {
    const k = el.getAttribute('data-tw');
    if (t[k] == null) return;
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

// ---- Live schedule from Firebase + formularz zapytania rezerwacyjnego
(function(){
  const ROOMS = 7;
  const DAYS = ['Poniedziałek','Wtorek','Środa','Czwartek','Piątek','Sobota','Niedziela'];
  // Typy gabinetów wg nagłówka tabeli (G1..G7)
  const ROOM_TYPES = ['Mały','Duży','Mały','Mały','Duży','Mały','Biurowy'];
  // Cennik brutto (zł) — biurowy rozliczany jak mały
  const PRICES = {
    'Mały':    { AM: 250, PM: 299, DAY: 500 },
    'Duży':    { AM: 350, PM: 399, DAY: 600 },
    'Biurowy': { AM: 250, PM: 299, DAY: 500 }
  };
  const SLOT_TEXT = { AM: 'Przedpołudnie · 6:00–15:00', PM: 'Popołudnie · 15:00–23:00' };

  const tbody = document.getElementById('crmBody');
  let occupied = new Set();
  // Czy dotarł już pierwszy snapshot z Firestore. Dopóki false, nie pokazujemy
  // slotów jako „Wolne" (bo pusty `occupied` = wszystko wolne), tylko placeholder
  // ładowania — inaczej przy zimnym wejściu widać fałszywie all-free.
  let loaded = false;

  // Firestore key format: {roomNumber}-{dayIndex}-{AM|PM} (room 1–7, day 0=Pon…6=Nd)
  function buildKey(roomIdx, dayIdx, slot) {
    return (roomIdx + 1) + '-' + dayIdx + '-' + slot.toUpperCase();
  }

  function render() {
    let html = '';
    DAYS.forEach((dayName, di) => {
      [['AM','Przedpołudnie','6:00 – 15:00'], ['PM','Popołudnie','15:00 – 23:00']].forEach(([slot, label, hours], si) => {
        html += '<tr>';
        if (si === 0) html += `<td class="col-day" rowspan="2">${dayName}</td>`;
        html += `<td class="col-pora"><span class="pora-label">${label}</span><span class="pora-hours">${hours}</span></td>`;
        for (let r = 0; r < ROOMS; r++) {
          const title = `${dayName} · Gabinet ${r+1} · ${hours.replace(/ /g,'')}`;
          if (!loaded) {
            html += `<td class="col-slot"><span class="pill loading" data-title="${title}" aria-label="Ładowanie grafiku">···</span></td>`;
            continue;
          }
          const isBusy = occupied.has(buildKey(r, di, slot));
          const cls = isBusy ? 'busy' : 'free';
          const txt = isBusy ? 'Zajęte' : 'Wolne';
          const data = isBusy ? '' : ` data-r="${r}" data-d="${di}" data-s="${slot}"`;
          html += `<td class="col-slot"><span class="pill ${cls}" data-title="${title}"${data}>${txt}</span></td>`;
        }
        html += '</tr>';
      });
    });

    tbody.innerHTML = html;

    tbody.querySelectorAll('.pill.free').forEach(el => {
      el.addEventListener('click', () => {
        openModal(+el.dataset.r, +el.dataset.d, el.dataset.s);
      });
    });
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

  function fillBanner() {
    const t = (typeof TWEAKS !== 'undefined') ? TWEAKS : {};
    const email = t.email || 'gabinety@plaszowska25.pl';
    document.getElementById('bkBanner').innerHTML =
      `<span class="bk-banner-t">Masz pytania? Jesteśmy do dyspozycji:</span>
       <span class="bk-banner-row">
         <a href="tel:${(t.phone||'').replace(/\s/g,'')}">${t.phone||''}</a>
         <a href="mailto:${email}">${email}</a>
       </span>`;
  }

  function buildCalendar() {
    let html = '<table class="bk-grid"><thead><tr><th class="bk-gc"></th><th class="bk-gc"></th>';
    for (let r = 0; r < ROOMS; r++) {
      html += `<th>Gabinet ${r+1}<span>${ROOM_TYPES[r]}</span></th>`;
    }
    html += '</tr></thead><tbody>';
    DAYS.forEach((dayName, di) => {
      ['AM','PM'].forEach((slot, si) => {
        html += '<tr>';
        if (si === 0) html += `<td class="bk-gday" rowspan="2">${dayName}</td>`;
        html += `<td class="bk-gpora">${slot === 'AM' ? 'Przedp.' : 'Popoł.'}</td>`;
        for (let r = 0; r < ROOMS; r++) {
          const key = r + '-' + di + '-' + slot;
          if (occupied.has(buildKey(r, di, slot))) {
            html += '<td><span class="bk-cell busy" title="Zajęte">✕</span></td>';
          } else {
            const sel = selected.has(key);
            html += `<td><button type="button" class="bk-cell free${sel ? ' sel' : ''}" data-key="${key}" aria-pressed="${sel}" title="${dayName} · Gabinet ${r+1} · ${SLOT_TEXT[slot]}"></button></td>`;
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
      const p = PRICES[ROOM_TYPES[g.r]];
      const room = `Gabinet ${g.r+1} (${ROOM_TYPES[g.r]})`;
      if (g.am && g.pm) {
        lines.push({ label: `${DAYS[g.d]} · ${room} · Cały dzień 6:00–23:00`, price: p.DAY });
        total += p.DAY;
      } else {
        const slot = g.am ? 'AM' : 'PM';
        lines.push({ label: `${DAYS[g.d]} · ${room} · ${SLOT_TEXT[slot]}`, price: p[slot] });
        total += p[slot];
      }
    });
    return { lines, total };
  }

  function updateQuote() {
    const { lines, total } = computeQuote();
    if (!lines.length) {
      bkQuote.innerHTML = '<div class="bk-quote-empty">Zaznacz terminy powyżej, aby zobaczyć wstępną wycenę.</div>';
      return;
    }
    let html = '<h4>Wstępna wycena</h4><ul class="bk-quote-list">';
    lines.forEach(l => {
      html += `<li><span>${l.label}</span><span class="bk-price">${l.price} zł</span></li>`;
    });
    html += `</ul><div class="bk-quote-total"><span>Razem (za tydzień najmu)</span><span>${total} zł</span></div>`;
    html += '<p class="bk-quote-note">Ceny brutto, orientacyjne. Ostateczna stawka potwierdzana indywidualnie. Dwa bloki w jednym dniu rozliczamy jak cały dzień.</p>';
    bkQuote.innerHTML = html;
    if (lines.length) bkError.hidden = true;
  }

  function openModal(preR, preD, preSlot) {
    selected.clear();
    if (preSlot) selected.add(preR + '-' + preD + '-' + preSlot);
    bkForm.hidden = false;
    bkSuccess.hidden = true;
    bkError.hidden = true;
    bkSubmit.disabled = false;
    bkSubmit.textContent = 'Wyślij zapytanie';
    fillBanner();
    buildCalendar();
    updateQuote();
    bk.classList.add('on');
    document.body.style.overflow = 'hidden';
    if (bkScroll) bkScroll.scrollTop = 0;
  }

  function closeModal() {
    bk.classList.remove('on');
    document.body.style.overflow = '';
  }

  // wszystkie przyciski rezerwacji (nagłówek + cennik) otwierają formularz bez wstępnego terminu
  document.querySelectorAll('.js-open-booking').forEach(btn => {
    btn.addEventListener('click', e => { e.preventDefault(); openModal(); });
  });

  document.getElementById('bkClose').addEventListener('click', closeModal);
  document.getElementById('bkDone').addEventListener('click', closeModal);
  bk.addEventListener('click', e => { if (e.target === bk) closeModal(); });
  window.addEventListener('keydown', e => {
    if (e.key === 'Escape' && bk.classList.contains('on')) closeModal();
  });

  bkForm.addEventListener('submit', async e => {
    e.preventDefault();
    const { lines, total } = computeQuote();
    if (!lines.length) { bkError.hidden = false; return; }
    if (!bkForm.reportValidity()) return;

    const name  = document.getElementById('bkName').value.trim();
    const email = document.getElementById('bkEmail').value.trim();
    const phone = document.getElementById('bkPhone').value.trim();
    const spec  = document.getElementById('bkSpec').value.trim();
    const note  = document.getElementById('bkMsg').value.trim();

    const message =
      `Nowe zapytanie rezerwacyjne — Płaszowska 25\n\n` +
      `Imię i nazwisko: ${name}\n` +
      `E-mail: ${email}\n` +
      `Telefon: ${phone}\n` +
      (spec ? `Specjalizacja: ${spec}\n` : '') +
      `\nWybrane terminy:\n` +
      lines.map(l => `• ${l.label} — ${l.price} zł`).join('\n') +
      `\n\nSzacunkowa wycena (za tydzień najmu): ${total} zł\n` +
      (note ? `\nWiadomość:\n${note}\n` : '');

    bkSubmit.disabled = true;
    bkSubmit.textContent = 'Wysyłanie…';

    const key = (typeof WEB3FORMS_KEY !== 'undefined') ? WEB3FORMS_KEY : '';
    if (!key || key === 'WKLEJ-TUTAJ-ACCESS-KEY') {
      console.warn('Brak skonfigurowanego WEB3FORMS_KEY — zapytanie nie zostało wysłane.', { name, email, phone, message });
      showSuccess();
      return;
    }

    try {
      const res = await fetch('https://api.web3forms.com/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify({
          access_key: key,
          subject: 'Nowe zapytanie rezerwacyjne — Płaszowska 25',
          from_name: name,
          replyto: email,
          name, email, phone,
          message
        })
      });
      const data = await res.json();
      if (data.success) { showSuccess(); }
      else { throw new Error(data.message || 'Błąd wysyłki'); }
    } catch (err) {
      console.warn('Web3Forms error:', err);
      bkError.hidden = false;
      bkError.textContent = 'Nie udało się wysłać zapytania. Napisz do nas: gabinety@plaszowska25.pl';
      bkSubmit.disabled = false;
      bkSubmit.textContent = 'Wyślij zapytanie';
    }
  });

  function showSuccess() {
    bkForm.hidden = true;
    bkSuccess.hidden = false;
    if (bkScroll) bkScroll.scrollTop = 0;
  }

  // Stan początkowy (ładowanie)
  render();

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
    db.doc('artifacts/gabinety-plaszowska/users/shared/settings/promotion')
      .get()
      .then(doc => { if (doc.exists) showPromo(doc.data()); })
      .catch(err => console.warn('Promo fetch error:', err));
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
    .bindPopup('<b>Płaszowska 25</b>Centrum Terapeutyczne, Kraków')
    .openPopup();
});

// ---- Cookie banner
(function() {
  const KEY = 'p25_cookie_consent';
  const banner = document.getElementById('cookie');
  const saved = localStorage.getItem(KEY);
  if (!saved) {
    setTimeout(() => banner.classList.add('on'), 800);
  } else if (saved === 'accept') {
    loadGA();
  }
  document.getElementById('ckAccept').onclick = () => {
    localStorage.setItem(KEY, 'accept');
    banner.classList.remove('on');
    loadGA();
  };
  document.getElementById('ckDecline').onclick = () => {
    localStorage.setItem(KEY, 'decline');
    banner.classList.remove('on');
  };
  function loadGA() {
    const GA_ID = 'G-XXXXXXXXXX';
    if (GA_ID === 'G-XXXXXXXXXX') return;
    const s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    function gtag(){ dataLayer.push(arguments); }
    window.gtag = gtag;
    gtag('js', new Date());
    gtag('config', GA_ID, { anonymize_ip: true });
  }
})();

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
    document.body.style.overflow = 'hidden';
  }
  function close() { lb.classList.remove('on'); document.body.style.overflow = ''; }

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
