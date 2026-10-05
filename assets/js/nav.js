// ---- Menu mobilne dla podstron bez własnego skryptu (regulamin, polityka prywatności)
(function(){
  const burger = document.getElementById('burger');
  const sheet = document.getElementById('sheet');
  if (!burger || !sheet) return;
  const close = sheet.querySelector('.close');
  const set = on => {
    sheet.classList.toggle('on', on);
    burger.setAttribute('aria-expanded', String(on));
    document.documentElement.style.overflow = on ? 'hidden' : '';
  };
  burger.addEventListener('click', () => set(true));
  if (close) close.addEventListener('click', () => set(false));
  sheet.querySelectorAll('a').forEach(a => a.addEventListener('click', () => set(false)));
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && sheet.classList.contains('on')) set(false); });
})();
