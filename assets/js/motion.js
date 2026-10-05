// ---- Motion: reveal przy scrollu (port komponentu 21st „Reveal": fade + unblur + stagger),
// licznik w statystykach, cień nawigacji po przewinięciu.
// Bez JS / przy prefers-reduced-motion treść jest po prostu widoczna (klasa js-motion nie jest dodawana).
(function(){
  const nav = document.querySelector('.nav');
  if (nav) {
    const onScroll = () => nav.classList.toggle('is-scrolled', window.scrollY > 8);
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce || !('IntersectionObserver' in window)) return;
  document.documentElement.classList.add('js-motion');

  // Grupy elementów: w obrębie grupy kolejne dzieci dostają rosnące opóźnienie
  const GROUPS = [
    '.section-head > *',
    '.about-body > *',
    '.offer-grid > .card',
    '.perks-grid > .perk',
    '.foot-cta > *',
    '.gallery > .tile',
    '.for-who-body .chip',
    '.price-table > .price-row',
    '.contact-grid > *',
  ];
  const SINGLES = ['.about-photo', '.for-who-photo', '.avail-wrap', '.price-table > .price-head'];

  const targets = [];
  GROUPS.forEach(sel => {
    const byParent = new Map();
    document.querySelectorAll(sel).forEach(el => {
      const list = byParent.get(el.parentElement) || [];
      list.push(el); byParent.set(el.parentElement, list);
    });
    // galeria: stagger w obrębie „wiersza" (4 kolumny), żeby dalsze kafle nie czekały za długo
    byParent.forEach(list => list.forEach((el, i) => targets.push([el, sel.includes('tile') ? i % 4 : Math.min(i, 6)])));
  });
  SINGLES.forEach(sel => document.querySelectorAll(sel).forEach(el => targets.push([el, 0])));

  const STAGGER = 90, DURATION = 800;
  targets.forEach(([el, i]) => {
    el.setAttribute('data-reveal', '');
    el.style.setProperty('--reveal-delay', (i * STAGGER) + 'ms');
  });

  const io = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      const el = entry.target;
      // element już nad widokiem (wejście z kotwicy / przywrócony scroll) — pokaż bez animacji
      if (!entry.isIntersecting) {
        if (entry.boundingClientRect.bottom < 0) {
          io.unobserve(el);
          el.removeAttribute('data-reveal');
          el.style.removeProperty('--reveal-delay');
        }
        return;
      }
      io.unobserve(el);
      el.classList.add('is-in');
      if (el.matches('.about-body > .about-stats')) countUp(el);
      // po animacji oddajemy elementowi jego własne transition (np. hover kart)
      const delay = parseInt(el.style.getPropertyValue('--reveal-delay'), 10) || 0;
      setTimeout(() => {
        el.removeAttribute('data-reveal');
        el.classList.remove('is-in');
        el.style.removeProperty('--reveal-delay');
      }, delay + DURATION + 100);
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
  targets.forEach(([el]) => io.observe(el));

  // „7 gabinetów", „10 min" — liczy od zera; wartości typu „24/7" zostają bez zmian
  function countUp(root) {
    root.querySelectorAll('.stat .n').forEach(n => {
      const m = n.textContent.trim().match(/^(\d+)(\D*)$/);
      if (!m || m[2].includes('/')) return;
      const end = +m[1], suffix = m[2], t0 = performance.now(), dur = 1200;
      const tick = now => {
        const p = Math.min((now - t0) / dur, 1);
        n.textContent = Math.round(end * (1 - Math.pow(1 - p, 3))) + suffix;
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    });
  }
})();
