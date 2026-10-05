// ---- Teksty generowane przez JS (terminarz, formularze, cookies) w 3 językach.
// Język strony bierzemy z <html lang="pl|en|uk">. Treść HTML stron jest tłumaczona
// statycznie (katalogi /en/ i /ua/), tu są tylko napisy budowane w skryptach.
(function(){
  const STR = {
    pl: {
      days: ['Poniedziałek','Wtorek','Środa','Czwartek','Piątek','Sobota','Niedziela'],
      roomTypes: { 'Mały': 'Mały', 'Duży': 'Duży', 'Biurowy': 'Biurowy' },
      room: 'Gabinet',
      am: 'Przedpołudnie', pm: 'Popołudnie', amShort: 'Przedp.', pmShort: 'Popoł.',
      slotAM: 'Przedpołudnie · 6:00–15:00', slotPM: 'Popołudnie · 15:00–23:00',
      fullDay: 'Cały dzień 6:00–23:00',
      free: 'Wolne', busy: 'Zajęte', loading: 'Ładowanie grafiku',
      weekendShow: 'Pokaż weekend (sobota – niedziela)', weekendHide: 'Zwiń weekend',
      today: 'Dziś',
      pickRoom: 'Wybierz gabinet',
      freeCount: n => `${n} ${plural(n, 'wolny', 'wolne', 'wolnych')}`,
      todayFree: n => `Dziś wolnych: <strong>${n}</strong> ${plural(n, 'blok', 'bloki', 'bloków')}`,
      todayNone: 'Na dziś wszystkie bloki są zajęte. Sprawdź kolejne dni',
      quoteEmpty: 'Zaznacz terminy powyżej, aby zobaczyć wstępną wycenę.',
      quoteTitle: 'Wstępna wycena', quoteTotal: 'Razem (za tydzień najmu)',
      quoteNote: 'Ceny brutto, orientacyjne. Ostateczna stawka potwierdzana indywidualnie. Dwa bloki w jednym dniu rozliczamy jak cały dzień.',
      currency: 'zł',
      bannerTitle: 'Masz pytania? Jesteśmy do dyspozycji:',
      send: 'Wyślij zapytanie', sending: 'Wysyłanie…',
      sendError: 'Nie udało się wysłać zapytania. Napisz do nas: gabinety@plaszowska25.pl',
      pickSlot: 'Zaznacz co najmniej jeden termin, aby wysłać zapytanie.',
      viewSend: 'Umów oglądanie', viewPickDate: 'Wybierz preferowaną datę oglądania.',
      viewTimes: { morning: 'Rano (8:00–11:00)', midday: 'Południe (11:00–13:00)', afternoon: 'Popołudnie (13:00–15:00)', other: 'Inna pora (ustalimy telefonicznie)' },
      mapPopup: 'Centrum Terapeutyczne, Kraków',
      ck: {
        title: 'Cookies i prywatność',
        text: 'Ten serwis wykorzystuje pliki cookies niezbędne do działania strony oraz, za Twoją zgodą, cookies analityczne (Google Analytics 4) i marketingowe (Meta Pixel) służące do statystyk oraz pomiaru skuteczności reklam. Wybierając „Tylko niezbędne”, nie uruchamiasz cookies analitycznych ani marketingowych. Szczegóły w <a href="polityka-prywatnosci.html">Polityce prywatności</a>.',
        decline: 'Tylko niezbędne', accept: 'Akceptuję wszystkie', settings: 'Ustawienia',
        panelTitle: 'Ustawienia cookies',
        panelIntro: 'Zdecyduj, na które pliki cookies się zgadzasz. Zgodę możesz w każdej chwili zmienić lub wycofać. Link „Ustawienia cookies” znajdziesz w stopce każdej strony.',
        necessary: 'Niezbędne', necessaryDesc: 'Zapamiętanie Twoich wyborów i podstawowe działanie strony. Nie można ich wyłączyć.',
        always: 'Zawsze aktywne',
        analytics: 'Analityczne', analyticsDesc: 'Google Analytics 4: anonimowe statystyki odwiedzin, które pomagają nam ulepszać stronę.',
        marketing: 'Marketingowe', marketingDesc: 'Meta Pixel (Facebook/Instagram): pomiar skuteczności naszych reklam.',
        save: 'Zapisz wybór', acceptAll: 'Zaakceptuj wszystkie', rejectAll: 'Odrzuć opcjonalne',
        saved: 'Zapisano ustawienia cookies.', close: 'Zamknij'
      }
    },
    en: {
      days: ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],
      roomTypes: { 'Mały': 'Small', 'Duży': 'Large', 'Biurowy': 'Office' },
      room: 'Room',
      am: 'Morning', pm: 'Afternoon', amShort: 'AM', pmShort: 'PM',
      slotAM: 'Morning · 6:00–15:00', slotPM: 'Afternoon · 15:00–23:00',
      fullDay: 'Full day 6:00–23:00',
      free: 'Free', busy: 'Booked', loading: 'Loading schedule',
      weekendShow: 'Show weekend (Saturday – Sunday)', weekendHide: 'Hide weekend',
      today: 'Today',
      pickRoom: 'Choose a room',
      freeCount: n => `${n} free`,
      todayFree: n => `Free today: <strong>${n}</strong> ${n === 1 ? 'block' : 'blocks'}`,
      todayNone: 'All blocks are booked today. Check the coming days',
      quoteEmpty: 'Select time slots above to see an estimated price.',
      quoteTitle: 'Estimated price', quoteTotal: 'Total (per week of rental)',
      quoteNote: 'Gross prices, indicative. The final rate is confirmed individually. Two blocks on the same day are charged as a full day.',
      currency: 'PLN',
      bannerTitle: 'Questions? We are happy to help:',
      send: 'Send enquiry', sending: 'Sending…',
      sendError: 'We could not send your enquiry. Please write to us: gabinety@plaszowska25.pl',
      pickSlot: 'Select at least one time slot to send your enquiry.',
      viewSend: 'Book a viewing', viewPickDate: 'Choose your preferred viewing date.',
      viewTimes: { morning: 'Morning (8:00–11:00)', midday: 'Midday (11:00–13:00)', afternoon: 'Afternoon (13:00–15:00)', other: 'Another time (we will arrange it by phone)' },
      mapPopup: 'Therapy Centre, Kraków',
      ck: {
        title: 'Cookies & privacy',
        text: 'This website uses cookies that are necessary for it to work and, with your consent, analytics cookies (Google Analytics 4) and marketing cookies (Meta Pixel) used for statistics and measuring the effectiveness of our ads. If you choose “Necessary only”, no analytics or marketing cookies are set. Details in our <a href="polityka-prywatnosci.html">Privacy Policy</a>.',
        decline: 'Necessary only', accept: 'Accept all', settings: 'Settings',
        panelTitle: 'Cookie settings',
        panelIntro: 'Choose which cookies you agree to. You can change or withdraw your consent at any time. The “Cookie settings” link is in the footer of every page.',
        necessary: 'Necessary', necessaryDesc: 'Remembering your choices and basic site functionality. These cannot be switched off.',
        always: 'Always active',
        analytics: 'Analytics', analyticsDesc: 'Google Analytics 4: anonymous visit statistics that help us improve the website.',
        marketing: 'Marketing', marketingDesc: 'Meta Pixel (Facebook/Instagram): measuring the effectiveness of our ads.',
        save: 'Save choices', acceptAll: 'Accept all', rejectAll: 'Reject optional',
        saved: 'Cookie settings saved.', close: 'Close'
      }
    },
    uk: {
      days: ['Понеділок','Вівторок','Середа','Четвер','Пʼятниця','Субота','Неділя'],
      roomTypes: { 'Mały': 'Малий', 'Duży': 'Великий', 'Biurowy': 'Офісний' },
      room: 'Кабінет',
      am: 'До обіду', pm: 'Після обіду', amShort: 'До об.', pmShort: 'Після об.',
      slotAM: 'До обіду · 6:00–15:00', slotPM: 'Після обіду · 15:00–23:00',
      fullDay: 'Цілий день 6:00–23:00',
      free: 'Вільно', busy: 'Зайнято', loading: 'Завантаження графіка',
      weekendShow: 'Показати вихідні (субота – неділя)', weekendHide: 'Згорнути вихідні',
      today: 'Сьогодні',
      pickRoom: 'Оберіть кабінет',
      freeCount: n => `${n} ${plural(n, 'вільний', 'вільні', 'вільних')}`,
      todayFree: n => `Сьогодні вільно: <strong>${n}</strong> ${plural(n, 'блок', 'блоки', 'блоків')}`,
      todayNone: 'На сьогодні всі блоки зайняті. Перегляньте наступні дні',
      quoteEmpty: 'Позначте терміни вище, щоб побачити попередню вартість.',
      quoteTitle: 'Попередня вартість', quoteTotal: 'Разом (за тиждень оренди)',
      quoteNote: 'Ціни брутто, орієнтовні. Остаточна ставка підтверджується індивідуально. Два блоки в один день оплачуються як цілий день.',
      currency: 'зл',
      bannerTitle: 'Маєте запитання? Ми на звʼязку:',
      send: 'Надіслати запит', sending: 'Надсилання…',
      sendError: 'Не вдалося надіслати запит. Напишіть нам: gabinety@plaszowska25.pl',
      pickSlot: 'Позначте щонайменше один термін, щоб надіслати запит.',
      viewSend: 'Записатися на огляд', viewPickDate: 'Оберіть бажану дату огляду.',
      viewTimes: { morning: 'Зранку (8:00–11:00)', midday: 'Опівдні (11:00–13:00)', afternoon: 'Після обіду (13:00–15:00)', other: 'Інший час (домовимося телефоном)' },
      mapPopup: 'Терапевтичний центр, Краків',
      ck: {
        title: 'Cookies і конфіденційність',
        text: 'Цей сайт використовує файли cookies, необхідні для його роботи, а також, за Вашою згодою, аналітичні (Google Analytics 4) та маркетингові (Meta Pixel) cookies для статистики й оцінки ефективності реклами. Обравши «Лише необхідні», Ви не вмикаєте аналітичні та маркетингові cookies. Детальніше в <a href="polityka-prywatnosci.html">Політиці конфіденційності</a>.',
        decline: 'Лише необхідні', accept: 'Прийняти всі', settings: 'Налаштування',
        panelTitle: 'Налаштування cookies',
        panelIntro: 'Оберіть, на які файли cookies Ви погоджуєтеся. Згоду можна будь-коли змінити або відкликати. Посилання «Налаштування cookies» є у футері кожної сторінки.',
        necessary: 'Необхідні', necessaryDesc: 'Запамʼятовування Ваших виборів і базова робота сайту. Їх не можна вимкнути.',
        always: 'Завжди активні',
        analytics: 'Аналітичні', analyticsDesc: 'Google Analytics 4: анонімна статистика відвідувань, яка допомагає нам покращувати сайт.',
        marketing: 'Маркетингові', marketingDesc: 'Meta Pixel (Facebook/Instagram): оцінка ефективності нашої реклами.',
        save: 'Зберегти вибір', acceptAll: 'Прийняти всі', rejectAll: 'Відхилити необовʼязкові',
        saved: 'Налаштування cookies збережено.', close: 'Закрити'
      }
    }
  };

  // Polski i ukraiński: 1 / 2–4 (poza 12–14) / reszta
  function plural(n, one, few, many) {
    if (n === 1) return one;
    const d = n % 10, h = n % 100;
    return (d >= 2 && d <= 4 && !(h >= 12 && h <= 14)) ? few : many;
  }

  const lang = (document.documentElement.lang || 'pl').slice(0, 2);
  window.P25_LANG = STR[lang] ? lang : 'pl';
  window.P25_T = STR[window.P25_LANG];
  window.P25_PL = STR.pl; // treść maili do biura zawsze po polsku
})();
