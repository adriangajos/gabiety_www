// ---- apply tweak values to DOM
function applyTweaks(t) {
  document.querySelectorAll('[data-tw]').forEach(el => {
    const k = el.getAttribute('data-tw');
    if (t[k] == null) return;
    if (k === 'email') {
      el.innerHTML = '<a href="mailto:' + t[k] + '?subject=Rezerwacja%20Gabinetu">' + t[k] + '</a>';
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

// ---- Live schedule from Firebase
(function(){
  const ROOMS = 7;
  const DAYS = ['Poniedziałek','Wtorek','Środa','Czwartek','Piątek','Sobota','Niedziela'];
  const tbody = document.getElementById('crmBody');

  // Firestore key format: {roomNumber}-{dayIndex}-{AM|PM}
  // roomNumber: 1–7, dayIndex: 0=Pon … 6=Nd
  function buildKey(roomIdx, dayIdx, slot) {
    return (roomIdx + 1) + '-' + dayIdx + '-' + slot.toUpperCase();
  }

  function render(occupied) {
    let html = '';
    DAYS.forEach((dayName, di) => {
      const isWeekend = di >= 5;
      html += '<tr>';
      html += `<td class="col-day" rowspan="2">${dayName}</td>`;
      html += `<td class="col-pora"><span class="pora-label">Przedpołudnie</span><span class="pora-hours">6:00 – 15:00</span></td>`;
      for (let r = 0; r < ROOMS; r++) {
        const isBusy = occupied.has(buildKey(r, di, 'AM'));
        const cls = isBusy ? 'busy' : (isWeekend ? 'weekend' : 'free');
        const txt = isBusy ? 'Zajęte' : 'Wolne';
        const title = `${dayName} · Gabinet ${r+1} · 6:00–15:00`;
        html += `<td class="col-slot"><span class="pill ${cls}" data-title="${title}">${txt}</span></td>`;
      }
      html += '</tr><tr>';
      html += `<td class="col-pora"><span class="pora-label">Popołudnie</span><span class="pora-hours">15:00 – 23:00</span></td>`;
      for (let r = 0; r < ROOMS; r++) {
        const isBusy = occupied.has(buildKey(r, di, 'PM'));
        const cls = isBusy ? 'busy' : (isWeekend ? 'weekend' : 'free');
        const txt = isBusy ? 'Zajęte' : 'Wolne';
        const title = `${dayName} · Gabinet ${r+1} · 15:00–23:00`;
        html += `<td class="col-slot"><span class="pill ${cls}" data-title="${title}">${txt}</span></td>`;
      }
      html += '</tr>';
    });

    tbody.innerHTML = html;

    tbody.querySelectorAll('.pill.free').forEach(el => {
      el.addEventListener('click', () => {
        const t = el.getAttribute('data-title');
        const subject = encodeURIComponent('Rezerwacja Gabinetu');
        const body = encodeURIComponent('Dzień dobry,\n\nChciał(a)bym zarezerwować termin:\n' + t + '\n\nProszę o kontakt w sprawie szczegółów.\n\nPozdrawiam,');
        window.location.href = 'mailto:gabinety@plaszowska25.pl?subject=' + subject + '&body=' + body;
      });
    });
  }

  // Show loading state
  render(new Set());

  // Connect to Firebase — wait for SDK to be ready
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
      const occupied = new Set(snapshot.docs.map(d => d.id));
      render(occupied);
    }, err => {
      console.warn('Schedule fetch error:', err);
    });
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
