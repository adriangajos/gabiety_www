# Tłumaczenia strony głównej: (PL, EN, UKR). Bez pauzy „—" w tekstach.
PLACE_EN = ', Płaszowska 25, Kraków"'
PLACE_UK = ', Płaszowska 25, Краків"'

PAIRS = [
    # ---------- <head> ----------
    ('<title>Wynajem gabinetów terapeutycznych Kraków | Płaszowska 25</title>',
     '<title>Therapy rooms for rent in Kraków | Płaszowska 25</title>',
     '<title>Оренда терапевтичних кабінетів у Кракові | Płaszowska 25</title>'),
    ('content="Nowoczesne gabinety terapeutyczne do wynajęcia w Krakowie. Komfort, dyskrecja, elastyczne warunki dla psychologów i terapeutów."',
     'content="Modern therapy rooms for rent in Kraków. Comfort, discretion and flexible terms for psychologists and therapists."',
     'content="Сучасні терапевтичні кабінети в оренду в Кракові. Комфорт, конфіденційність і гнучкі умови для психологів і терапевтів."'),
    ('content="Wynajem gabinetów terapeutycznych w Krakowie | Płaszowska 25"',
     'content="Therapy rooms for rent in Kraków | Płaszowska 25"',
     'content="Оренда терапевтичних кабінетів у Кракові | Płaszowska 25"'),
    ('content="Nowoczesne, w pełni wyposażone gabinety do wynajęcia dla psychologów i terapeutów. Elastyczne bloki, przejrzysty cennik."',
     'content="Modern, fully furnished rooms for psychologists and therapists. Flexible blocks, clear pricing."',
     'content="Сучасні, повністю облаштовані кабінети для психологів і терапевтів. Гнучкі блоки, прозорі ціни."'),
    ('content="Gabinet terapeutyczny do wynajęcia, Centrum Płaszowska 25, Kraków"',
     'content="Therapy room for rent, Płaszowska 25, Kraków"',
     'content="Терапевтичний кабінет в оренду, Płaszowska 25, Краків"'),
    ('"description": "Wynajem nowoczesnych gabinetów terapeutycznych w Krakowie dla psychologów, psychoterapeutów i specjalistów."',
     '"description": "Modern therapy rooms for rent in Kraków for psychologists, psychotherapists and other specialists."',
     '"description": "Оренда сучасних терапевтичних кабінетів у Кракові для психологів, психотерапевтів та інших фахівців."'),

    # ---------- nawigacja / menu ----------
    ('aria-label="Płaszowska 25, strona główna"', 'aria-label="Płaszowska 25, home"', 'aria-label="Płaszowska 25, головна"'),
    ('aria-label="Menu">≡<span class="burger-label"> Menu</span></button>', 'aria-label="Menu">≡<span class="burger-label"> Menu</span></button>', 'aria-label="Меню">≡<span class="burger-label"> Меню</span></button>'),
    ('>Umów oglądanie gabinetu →</button>', '>Book a viewing →</button>', '>Записатися на огляд →</button>'),
    ('>Umów oglądanie gabinetu</button>', '>Book a viewing</button>', '>Записатися на огляд</button>'),
    ('>Umów oglądanie</button>', '>Book a viewing</button>', '>Записатися на огляд</button>'),

    # ---------- hero ----------
    ('data-tw="heroEyebrow">Kraków · Płaszów</span>', 'data-tw="heroEyebrow">Kraków · Płaszów</span>', 'data-tw="heroEyebrow">Краків · Плашув</span>'),
    ('>Gabinety terapeutyczne <span class="h1-nowrap"><em>do wynajęcia</em> w Krakowie.</span> Komfort, jakiego potrzebujesz.</h1>',
     '>Therapy rooms <span class="h1-nowrap"><em>for rent</em> in Kraków.</span> The comfort you need.</h1>',
     '>Терапевтичні кабінети <span class="h1-nowrap"><em>в оренду</em> у Кракові.</span> Комфорт, якого Ви потребуєте.</h1>'),
    ('''data-tw="heroLead">
          Nowoczesne, w pełni wyposażone gabinety do wynajęcia dla psychologów,
          psychoterapeutów i specjalistów wspierających zdrowie psychiczne.
        </p>''',
     '''data-tw="heroLead">
          Modern, fully furnished rooms for rent for psychologists,
          psychotherapists and other mental health professionals.
        </p>''',
     '''data-tw="heroLead">
          Сучасні, повністю облаштовані кабінети в оренду для психологів,
          психотерапевтів та інших фахівців у сфері психічного здоровʼя.
        </p>'''),
    ('data-tw="heroCtaPrimary">Sprawdź dostępność →</a>', 'data-tw="heroCtaPrimary">Check availability →</a>', 'data-tw="heroCtaPrimary">Перевірити наявність →</a>'),
    ('data-tw="heroCtaSecondary">Zobacz gabinety</a>', 'data-tw="heroCtaSecondary">See the rooms</a>', 'data-tw="heroCtaSecondary">Переглянути кабінети</a>'),
    ('</span> Elastyczne godziny wynajmu</span>', '</span> Flexible rental hours</span>', '</span> Гнучкі години оренди</span>'),
    ('</span> Piękna poczekalnia dla pacjentów</span>', '</span> A beautiful waiting room for clients</span>', '</span> Затишна зала очікування для клієнтів</span>'),
    ('</span> Dyskrecja i cisza</span>', '</span> Discretion and quiet</span>', '</span> Конфіденційність і тиша</span>'),

    # ---------- opisy zdjęć (alt) ----------
    (', Centrum Płaszowska 25, Kraków"', PLACE_EN, PLACE_UK),
    (', Płaszowska 25, Kraków"', PLACE_EN, PLACE_UK),
    ('alt="Gabinet terapeutyczny z fotelem i biurkiem przy oknie na ogród,', 'alt="Therapy room with an armchair and a desk by a window overlooking the garden,', 'alt="Терапевтичний кабінет із кріслом і письмовим столом біля вікна в сад,'),
    ('alt="Poczekalnia z różową recepcją i fotelami dla pacjentów,', 'alt="Waiting room with a pink reception desk and armchairs for clients,', 'alt="Зала очікування з рожевою стійкою рецепції та кріслами для клієнтів,'),
    ('alt="Gabinet z dwoma beżowymi fotelami do wynajęcia w wybranym dniu tygodnia,', 'alt="Room with two beige armchairs for rent on a chosen day of the week,', 'alt="Кабінет із двома бежевими кріслами для оренди в обраний день тижня,'),
    ('alt="Przytulny gabinet z sofą i fotelem uszakiem do stałego najmu,', 'alt="Cosy room with a sofa and a wingback armchair for a permanent lease,', 'alt="Затишний кабінет із диваном і кріслом із «вухами» для постійної оренди,'),
    ('alt="Gabinet terapeutyczny z szarym fotelem uszakiem i biurkiem przy oknie na ogród,', 'alt="Therapy room with a grey wingback armchair and a desk by a garden window,', 'alt="Терапевтичний кабінет із сірим кріслом із «вухами» та письмовим столом біля вікна в сад,'),
    ('alt="Jasny gabinet z szarą sofą, żółtym fotelem i stołem,', 'alt="Bright room with a grey sofa, a yellow armchair and a table,', 'alt="Світлий кабінет із сірим диваном, жовтим кріслом і столом,'),
    ('alt="Gabinet terapeutyczny z żółtym fotelem uszakiem i sofą, wyjście na ogród,', 'alt="Therapy room with a yellow wingback armchair and a sofa, with access to the garden,', 'alt="Терапевтичний кабінет із жовтим кріслом із «вухами» та диваном, вихід у сад,'),
    ('alt="Gabinet z dwoma beżowymi fotelami i różową komodą przy oknie,', 'alt="Room with two beige armchairs and a pink chest of drawers by the window,', 'alt="Кабінет із двома бежевими кріслами та рожевим комодом біля вікна,'),
    ('alt="Korytarz z garderobą i wieszakami przy gabinetach,', 'alt="Corridor with a cloakroom and coat hooks next to the rooms,', 'alt="Коридор із гардеробом і вішаками біля кабінетів,'),
    ('alt="Gabinet terapeutyczny z sofą i fotelem w pepitkę,', 'alt="Therapy room with a sofa and a houndstooth armchair,', 'alt="Терапевтичний кабінет із диваном і кріслом у «гусячу лапку»,'),
    ('alt="Przytulny gabinet z sofą, fotelem uszakiem i różową szafą,', 'alt="Cosy room with a sofa, a wingback armchair and a pink wardrobe,', 'alt="Затишний кабінет із диваном, кріслом із «вухами» та рожевою шафою,'),
    ('alt="Gabinet z beżowym fotelem, biurkiem i miejscem do pracy,', 'alt="Room with a beige armchair, a desk and a workspace,', 'alt="Кабінет із бежевим кріслом, письмовим столом і робочим місцем,'),
    ('alt="Przejście między gabinetami z sofą i widokiem na poczekalnię,', 'alt="Passage between the rooms with a sofa and a view of the waiting room,', 'alt="Прохід між кабінетами з диваном і видом на залу очікування,'),
    ('alt="Gabinet terapeutyczny z biurkiem i sofą w pepitkę,', 'alt="Therapy room with a desk and a houndstooth sofa,', 'alt="Терапевтичний кабінет із письмовим столом і диваном у «гусячу лапку»,'),
    ('alt="Przestronna łazienka dostępna dla osób z niepełnosprawnością,', 'alt="Spacious bathroom accessible to people with disabilities,', 'alt="Простора вбиральня, доступна для людей з інвалідністю,'),
    ('alt="Słoneczny gabinet z żółtym fotelem i biurkiem, dwa okna na ogród,', 'alt="Sunny room with a yellow armchair and a desk, two windows overlooking the garden,', 'alt="Сонячний кабінет із жовтим кріслом і письмовим столом, два вікна в сад,'),
    ('alt="Jasny gabinet z szarą sofą i żółtym fotelem dla terapeutów,', 'alt="Bright room with a grey sofa and a yellow armchair for therapists,', 'alt="Світлий кабінет із сірим диваном і жовтим кріслом для терапевтів,'),

    # ---------- O centrum ----------
    ('<span class="eyebrow">O centrum</span>', '<span class="eyebrow">About the centre</span>', '<span class="eyebrow">Про центр</span>'),
    ('<h2>Miejsce stworzone z&nbsp;myślą o&nbsp;pracy ze&nbsp;słuchaniem.</h2>',
     '<h2>A place designed for the work of listening.</h2>',
     '<h2>Простір, створений для роботи, що ґрунтується на&nbsp;слуханні.</h2>'),
    ('''          Cisza, światło dzienne i przestrzeń, w której pacjent i&nbsp;terapeuta
          mogą skupić się wyłącznie na tym, co najważniejsze: rozmowie.''',
     '''          Quiet, daylight and a space where client and therapist
          can focus entirely on what matters most: the conversation.''',
     '''          Тиша, денне світло і простір, де клієнт і&nbsp;терапевт
          можуть повністю зосередитися на найважливішому: розмові.'''),
    ('''          Płaszowska 25 to kameralne centrum w dobrze skomunikowanej części
          Krakowa. Udostępniamy gabinety specjalistom, którym zależy na
          profesjonalnej, komfortowej przestrzeni, bez kompromisów w&nbsp;kwestii
          akustyki, wyposażenia i atmosfery.''',
     '''          Płaszowska 25 is an intimate centre in a well-connected part of
          Kraków. We offer rooms to professionals who value a professional,
          comfortable space, with no compromises on acoustics, furnishings
          or atmosphere.''',
     '''          Центр Płaszowska 25 розташований у районі Кракова з добрим
          транспортним сполученням. Ми надаємо кабінети фахівцям, яким важливий
          професійний і комфортний простір без компромісів щодо акустики,
          облаштування та атмосфери.'''),
    ('''          Wynajem jest elastyczny: bloki półdniowe, całe dni lub stały najem. Troszczymy się
          o poczekalnię, czystość i zaplecze, żebyś mógł/mogła skupić się
          na&nbsp;swojej pracy.''',
     '''          Rental is flexible: half-day blocks, full days or a permanent lease. We take care
          of the waiting room, cleaning and facilities, so you can focus
          on&nbsp;your work.''',
     '''          Оренда гнучка: блоки по пів дня, цілі дні або постійна оренда. Ми дбаємо
          про залу очікування, чистоту та інфраструктуру, щоб Ви могли зосередитися
          на&nbsp;своїй роботі.'''),
    ('<div class="l">gabinetów</div>', '<div class="l">rooms</div>', '<div class="l">кабінетів</div>'),
    ('<div class="l">dostępność</div>', '<div class="l">access</div>', '<div class="l">доступ</div>'),
    ('<div class="n">10 min</div><div class="l">do centrum</div>', '<div class="n">10 min</div><div class="l">to the city centre</div>', '<div class="n">10 хв</div><div class="l">до центру міста</div>'),

    # ---------- Oferta ----------
    ('<span class="eyebrow">Oferta</span>', '<span class="eyebrow">Offer</span>', '<span class="eyebrow">Пропозиція</span>'),
    ('<h2>Wszystko, czego potrzebujesz do prowadzenia praktyki.</h2>', '<h2>Everything you need to run your practice.</h2>', '<h2>Усе необхідне для Вашої практики.</h2>'),
    ('<p>Dwa warianty współpracy: wybierz okno w konkretnym dniu tygodnia albo\ncały gabinet na stałe.</p>',
     '<p>Two ways to work with us: choose a slot on a specific day of the week\nor a whole room on a permanent basis.</p>',
     '<p>Два варіанти співпраці: оберіть час у конкретний день тижня\nабо цілий кабінет на постійній основі.</p>'),
    ('<span class="card-num">01 / okno tygodniowe</span>', '<span class="card-num">01 / weekly slot</span>', '<span class="card-num">01 / щотижневий блок</span>'),
    ('<h3>Wynajem określonego okna w konkretnym dniu tygodnia</h3>', '<h3>Rent a fixed slot on a specific day of the week</h3>', '<h3>Оренда визначеного часу в конкретний день тижня</h3>'),
    ('<p>Wybierz powtarzalny blok półdniowy lub całodniowy w stałym dniu tygodnia. Ten sam gabinet, ten sam termin co tydzień.</p>',
     '<p>Choose a recurring half-day or full-day block on a fixed weekday. Same room, same time, every week.</p>',
     '<p>Оберіть регулярний блок на пів дня або на цілий день у фіксований день тижня. Той самий кабінет, той самий час щотижня.</p>'),
    ('<li>Bloki: 6–15, 15–23 lub 6–23</li>', '<li>Blocks: 6–15, 15–23 or 6–23</li>', '<li>Блоки: 6–15, 15–23 або 6–23</li>'),
    ('<li>Powtarzalne okno tygodniowe</li>', '<li>Recurring weekly slot</li>', '<li>Регулярний щотижневий блок</li>'),
    ('<li>Indywidualna umowa</li>', '<li>Individual agreement</li>', '<li>Індивідуальний договір</li>'),
    ('<span class="card-num">02 / stały najem</span>', '<span class="card-num">02 / permanent lease</span>', '<span class="card-num">02 / постійна оренда</span>'),
    ('<h3>Stały wynajem całego gabinetu</h3>', '<h3>Permanent lease of a whole room</h3>', '<h3>Постійна оренда цілого кабінету</h3>'),
    ('<p>Twój gabinet na wyłączność, dostępny 7 dni w tygodniu, urządzony pod Twoją praktykę.</p>',
     '<p>A room that is yours alone, available 7 days a week and arranged for your practice.</p>',
     '<p>Кабінет лише для Вас, доступний 7 днів на тиждень і облаштований під Вашу практику.</p>'),
    ('<li>Pełna dostępność 24/7</li>', '<li>Full 24/7 access</li>', '<li>Повний доступ 24/7</li>'),
    ('<li>Własna szafka</li>', '<li>Your own locker</li>', '<li>Власна шафка</li>'),
    ('<li>Wycena indywidualna</li>', '<li>Individual pricing</li>', '<li>Індивідуальна ціна</li>'),

    # ---------- W cenie ----------
    ('<span class="eyebrow">W cenie</span>', '<span class="eyebrow">Included</span>', '<span class="eyebrow">Що входить у вартість</span>'),
    ('>W cenie</a>', '>Included</a>', '>Що входить</a>'),
    ('<h2>Przychodzisz i&nbsp;pracujesz. Resztą zajmujemy się my.</h2>', '<h2>You come in and work. We take care of the rest.</h2>', '<h2>Ви приходите й працюєте. Про решту дбаємо ми.</h2>'),
    ('<p>Każdy blok najmu obejmuje pełne zaplecze centrum, bez dodatkowych opłat.</p>',
     '<p>Every rental block includes full use of the centre’s facilities, with no extra fees.</p>',
     '<p>Кожен блок оренди включає повний доступ до інфраструктури центру без додаткових оплат.</p>'),
    ('<h3>Umeblowany gabinet</h3>', '<h3>Furnished room</h3>', '<h3>Мебльований кабінет</h3>'),
    ('<p>Wygodne fotele, stolik i&nbsp;miejsce do notatek, a&nbsp;w&nbsp;wybranych gabinetach także kozetka.</p>',
     '<p>Comfortable armchairs, a side table and space for notes, plus a couch in selected rooms.</p>',
     '<p>Зручні крісла, столик і місце для нотаток, а&nbsp;в&nbsp;деяких кабінетах також кушетка.</p>'),
    ('<h3>Światło dzienne</h3>', '<h3>Daylight</h3>', '<h3>Денне світло</h3>'),
    ('<p>Jasne wnętrza z&nbsp;dużymi oknami, część gabinetów z&nbsp;widokiem na ogród.</p>',
     '<p>Bright interiors with large windows, some rooms overlooking the garden.</p>',
     '<p>Світлі приміщення з великими вікнами, частина кабінетів із видом на сад.</p>'),
    ('<h3>Akustyka i&nbsp;dyskrecja</h3>', '<h3>Acoustics and discretion</h3>', '<h3>Акустика і&nbsp;конфіденційність</h3>'),
    ('<p>Wyciszone gabinety, w&nbsp;których rozmowa zostaje między Tobą a&nbsp;pacjentem.</p>',
     '<p>Soundproofed rooms where the conversation stays between you and your client.</p>',
     '<p>Звукоізольовані кабінети, де розмова залишається між Вами та клієнтом.</p>'),
    ('<h3>Poczekalnia</h3>', '<h3>Waiting room</h3>', '<h3>Зала очікування</h3>'),
    ('<p>Przytulna poczekalnia dla pacjentów. Nikt nie czeka na korytarzu.</p>',
     '<p>A cosy waiting room for clients. Nobody has to wait in the corridor.</p>',
     '<p>Затишна зала очікування для клієнтів. Ніхто не чекає в коридорі.</p>'),
    ('<h3>Sprzątanie</h3>', '<h3>Cleaning</h3>', '<h3>Прибирання</h3>'),
    ('<p>Regularnie sprzątane gabinety i&nbsp;części wspólne. Przychodzisz do gotowego.</p>',
     '<p>Rooms and common areas are cleaned regularly. Everything is ready when you arrive.</p>',
     '<p>Кабінети та спільні зони регулярно прибираються. Ви приходите, і все вже готово.</p>'),
    ('<h3>Dostępna łazienka</h3>', '<h3>Accessible bathroom</h3>', '<h3>Доступна вбиральня</h3>'),
    ('<p>Przestronna łazienka przystosowana dla osób z&nbsp;niepełnosprawnością.</p>',
     '<p>A spacious bathroom adapted for people with disabilities.</p>',
     '<p>Простора вбиральня, пристосована для людей з&nbsp;інвалідністю.</p>'),
    ('<h3>Garderoba</h3>', '<h3>Cloakroom</h3>', '<h3>Гардероб</h3>'),
    ('<p>Miejsce na okrycia wierzchnie dla Ciebie i&nbsp;Twoich pacjentów.</p>',
     '<p>Space for coats for you and your clients.</p>',
     '<p>Місце для верхнього одягу для Вас і&nbsp;Ваших клієнтів.</p>'),
    ('<h3>Elastyczne godziny</h3>', '<h3>Flexible hours</h3>', '<h3>Гнучкі години</h3>'),
    ('<p>Bloki od 6:00 do 23:00, a&nbsp;przy stałym najmie dostęp 24/7.</p>',
     '<p>Blocks from 6:00 to 23:00, and 24/7 access with a permanent lease.</p>',
     '<p>Блоки з 6:00 до 23:00, а&nbsp;при постійній оренді доступ 24/7.</p>'),

    # ---------- Galeria ----------
    ('<span class="eyebrow">Gabinety</span>', '<span class="eyebrow">Rooms</span>', '<span class="eyebrow">Кабінети</span>'),
    ('<h2>Siedem gabinetów. Każdy inny, każdy gotowy do pracy.</h2>', '<h2>Seven rooms. Each one different, each one ready for work.</h2>', '<h2>Сім кабінетів. Кожен інший, кожен готовий до роботи.</h2>'),
    ('<p>Umeblowane zgodnie ze standardami pracy terapeutycznej: fotele, kozetka (w wybranych), dobre oświetlenie i akustyka.</p>',
     '<p>Furnished to therapeutic standards: armchairs, a couch (in selected rooms), good lighting and acoustics.</p>',
     '<p>Облаштовані відповідно до стандартів терапевтичної роботи: крісла, кушетка (у деяких кабінетах), добре освітлення та акустика.</p>'),
    ('<span class="cap">Gabinety Płaszowska</span>', '<span class="cap">Płaszowska rooms</span>', '<span class="cap">Кабінети Płaszowska</span>'),
    ('Zdjęcia to nie wszystko. Przyjdź i&nbsp;poczuj atmosferę na miejscu.',
     'Photos are not everything. Come and feel the atmosphere in person.',
     'Фото не передають усього. Приходьте й відчуйте атмосферу на місці.'),

    # ---------- Dla kogo ----------
    ('<span class="eyebrow">Dla kogo</span>', '<span class="eyebrow">Who it is for</span>', '<span class="eyebrow">Для кого</span>'),
    ('<h2>Jeśli tworzysz przestrzeń dla innych, zadbaj o&nbsp;swoją.</h2>', '<h2>If you create space for others, take care of your own.</h2>', '<h2>Якщо Ви створюєте простір для інших, подбайте і&nbsp;про свій.</h2>'),
    ('<p>Pracujemy z doświadczonymi specjalistami i osobami, które dopiero zaczynają własną praktykę.</p>',
     '<p>We work with experienced professionals and with people who are just starting their own practice.</p>',
     '<p>Ми працюємо як із досвідченими фахівцями, так і з тими, хто лише починає власну практику.</p>'),
    ('</span> Psychologowie i psychoterapeuci</div>', '</span> Psychologists and psychotherapists</div>', '</span> Психологи та психотерапевти</div>'),
    ('</span> Specjaliści terapii par i rodzin</div>', '</span> Couples and family therapists</div>', '</span> Фахівці з терапії пар і сімей</div>'),
    ('</span> Coachowie i terapeuci uzależnień</div>', '</span> Coaches and addiction therapists</div>', '</span> Коучі та терапевти залежностей</div>'),
    ('</span> Logopedzi i neurologopedzi</div>', '</span> Speech and neuro-speech therapists</div>', '</span> Логопеди та нейрологопеди</div>'),
    ('</span> Seksuolodzy i terapeuci traumy</div>', '</span> Sexologists and trauma therapists</div>', '</span> Сексологи та терапевти травми</div>'),
    ('</span> Superwizorzy i prowadzący grupy</div>', '</span> Supervisors and group facilitators</div>', '</span> Супервізори та ведучі груп</div>'),

    # ---------- Harmonogram ----------
    ('<span class="eyebrow">Rezerwacja na żywo</span>', '<span class="eyebrow">Live booking</span>', '<span class="eyebrow">Бронювання онлайн</span>'),
    ('<h2>Sprawdź, czy Twój termin jest dostępny.</h2>', '<h2>Check whether your time slot is available.</h2>', '<h2>Перевірте, чи вільний потрібний Вам час.</h2>'),
    ('<h3>Harmonogram Całotygodniowy</h3>', '<h3>Weekly schedule</h3>', '<h3>Тижневий графік</h3>'),
    ('<th class="col-day">Dzień</th>', '<th class="col-day">Day</th>', '<th class="col-day">День</th>'),
    ('<th class="col-pora">Pora</th>', '<th class="col-pora">Time</th>', '<th class="col-pora">Час</th>'),
    ('<th>Gabinet ', '<th>Room ', '<th>Кабінет '),
    ('<span class="gtype">Mały</span>', '<span class="gtype">Small</span>', '<span class="gtype">Малий</span>'),
    ('<span class="gtype gtype-l">Duży</span>', '<span class="gtype gtype-l">Large</span>', '<span class="gtype gtype-l">Великий</span>'),
    ('<span class="gtype gtype-b">Biurowy</span>', '<span class="gtype gtype-b">Office</span>', '<span class="gtype gtype-b">Офісний</span>'),

    # ---------- Cennik ----------
    ('<span class="eyebrow">Cennik</span>', '<span class="eyebrow">Prices</span>', '<span class="eyebrow">Ціни</span>'),
    ('<h2>Przejrzyste bloki, bez ukrytych opłat.</h2>', '<h2>Clear blocks, no hidden fees.</h2>', '<h2>Прозорі блоки без прихованих платежів.</h2>'),
    ('<p>Gabinety wynajmujemy w blokach. Wszystkie ceny brutto.</p>', '<p>Rooms are rented in blocks. All prices are gross (VAT included).</p>', '<p>Кабінети здаються блоками. Усі ціни брутто (з ПДВ).</p>'),
    ('<span>Blok</span>', '<span>Block</span>', '<span>Блок</span>'),
    ('<span>Mały gabinet <small style="font-weight:400; opacity:0.7;">+ biurowy</small></span>',
     '<span>Small room <small style="font-weight:400; opacity:0.7;">+ office</small></span>',
     '<span>Малий кабінет <small style="font-weight:400; opacity:0.7;">+ офісний</small></span>'),
    ('<span>Duży gabinet</span>', '<span>Large room</span>', '<span>Великий кабінет</span>'),
    ('<div class="label">Przedpołudnie</div>', '<div class="label">Morning</div>', '<div class="label">До обіду</div>'),
    ('<div class="label">Popołudnie</div>', '<div class="label">Afternoon</div>', '<div class="label">Після обіду</div>'),
    ('<div class="label">Cały dzień</div>', '<div class="label">Full day</div>', '<div class="label">Цілий день</div>'),
    ('<div class="label">Wynajem miesięczny</div>', '<div class="label">Monthly rental</div>', '<div class="label">Оренда на місяць</div>'),
    ('6:00–23:00 · 17&nbsp;godz.', '6:00–23:00 · 17&nbsp;hrs', '6:00–23:00 · 17&nbsp;год.'),
    ('<span class="hours">Stały grafik, preferencyjne stawki</span>', '<span class="hours">Fixed schedule, preferential rates</span>', '<span class="hours">Фіксований графік, пільгові ставки</span>'),
    ('&nbsp;zł<small>brutto</small>', '&nbsp;PLN<small>gross</small>', '&nbsp;зл<small>брутто</small>'),
    ('<div class="amt">Wycena indywidualna</div>', '<div class="amt">Individual quote</div>', '<div class="amt">Індивідуальна ціна</div>'),
    ('>Rezerwuj →</a>', '>Book →</a>', '>Забронювати →</a>'),
    ('>Skontaktuj się →</a>', '>Get in touch →</a>', '>Звʼязатися →</a>'),
    ('Masz pytania o&nbsp;wynajem? Zobacz <a', 'Questions about renting? See the <a', 'Маєте запитання щодо оренди? Перегляньте <a'),
    ('>najczęściej zadawane pytania →</a>', '>frequently asked questions →</a>', '>поширені запитання →</a>'),

    # ---------- Kontakt ----------
    ('<span class="eyebrow">Kontakt</span>', '<span class="eyebrow">Contact</span>', '<span class="eyebrow">Контакти</span>'),
    ('<h2>Porozmawiajmy o&nbsp;Twojej praktyce.</h2>', '<h2>Let’s talk about your practice.</h2>', '<h2>Поговорімо про Вашу практику.</h2>'),
    ('<p>Zadzwoń lub napisz. Oddzwonimy w ciągu jednego dnia roboczego i&nbsp;umówimy oglądanie gabinetu.</p>',
     '<p>Call or write to us. We will get back to you within one working day and arrange a viewing.</p>',
     '<p>Зателефонуйте або напишіть. Ми відповімо протягом одного робочого дня й&nbsp;домовимося про огляд кабінету.</p>'),
    ('<span class="k">Adres</span>', '<span class="k">Address</span>', '<span class="k">Адреса</span>'),
    ('<span class="k">Telefon</span>', '<span class="k">Phone</span>', '<span class="k">Телефон</span>'),
    ('<span class="k">Godziny</span>', '<span class="k">Office hours</span>', '<span class="k">Години роботи</span>'),
    ('Pon–Pt · 8:00–15:00<br/>', 'Mon–Fri · 8:00–15:00<br/>', 'Пн–Пт · 8:00–15:00<br/>'),
    ('>Sprawdź wolne terminy</a>', '>Check free slots</a>', '>Перевірити вільні терміни</a>'),

    # ---------- Stopka ----------
    ('<h3>Zobacz gabinet na&nbsp;żywo.</h3>', '<h3>See the room in person.</h3>', '<h3>Подивіться кабінет наживо.</h3>'),
    ('<p>Umów się na oglądanie. Oprowadzimy Cię po centrum, pokażemy wolne gabinety i&nbsp;odpowiemy na pytania.</p>',
     '<p>Book a viewing. We will show you around the centre and the available rooms, and answer your questions.</p>',
     '<p>Запишіться на огляд. Ми проведемо Вас центром, покажемо вільні кабінети й&nbsp;відповімо на запитання.</p>'),
    ('>Zadzwoń: +48&nbsp;510&nbsp;574&nbsp;421</a>', '>Call: +48&nbsp;510&nbsp;574&nbsp;421</a>', '>Зателефонувати: +48&nbsp;510&nbsp;574&nbsp;421</a>'),
    ('''          Centrum terapeutyczne w&nbsp;Krakowie. Gabinety do wynajęcia dla&nbsp;psychologów i&nbsp;terapeutów.''',
     '''          Therapy centre in Kraków. Rooms for rent for psychologists and therapists.''',
     '''          Терапевтичний центр у&nbsp;Кракові. Кабінети в оренду для психологів і&nbsp;терапевтів.'''),
    ('<h4>Nawigacja</h4>', '<h4>Navigation</h4>', '<h4>Навігація</h4>'),
    ('<h4>Kontakt</h4>', '<h4>Contact</h4>', '<h4>Контакти</h4>'),
    ('<h4>Social</h4>', '<h4>Social</h4>', '<h4>Соцмережі</h4>'),
    ('© 2026 Płaszowska 25 · Wszelkie prawa zastrzeżone', '© 2026 Płaszowska 25 · All rights reserved', '© 2026 Płaszowska 25 · Усі права захищено'),

    # ---------- Formularz rezerwacji ----------
    ('aria-label="Formularz zapytania rezerwacyjnego"', 'aria-label="Booking enquiry form"', 'aria-label="Форма запиту на бронювання"'),
    ('<h3>Formularz zapytania rezerwacyjnego</h3>', '<h3>Booking enquiry form</h3>', '<h3>Форма запиту на бронювання</h3>'),
    ('''<p>Zaznacz na różowo interesujące Cię wolne terminy, a&nbsp;przygotujemy wstępną
           wycenę i odezwiemy się z potwierdzeniem dostępności.</p>''',
     '''<p>Mark the free slots you are interested in (they turn pink) and we will prepare
           an estimate and get back to you to confirm availability.</p>''',
     '''<p>Позначте вільні терміни, які Вас цікавлять (вони стануть рожевими), і&nbsp;ми підготуємо
           попередній розрахунок та звʼяжемося з Вами для підтвердження.</p>'''),
    ('>Imię i nazwisko *</label>', '>Full name *</label>', '>Імʼя та прізвище *</label>'),
    ('>E-mail *</label>', '>Email *</label>', '>E-mail *</label>'),
    ('>Telefon *</label>', '>Phone *</label>', '>Телефон *</label>'),
    ('>Specjalizacja <small>(opcjonalnie)</small></label>', '>Specialisation <small>(optional)</small></label>', '>Спеціалізація <small>(необовʼязково)</small></label>'),
    ('>Wiadomość <small>(opcjonalnie)</small></label>', '>Message <small>(optional)</small></label>', '>Повідомлення <small>(необовʼязково)</small></label>'),
    ('<h4>Wybierz terminy najmu</h4>', '<h4>Choose rental slots</h4>', '<h4>Оберіть терміни оренди</h4>'),
    ('<span class="lg lg-free"></span> wolne', '<span class="lg lg-free"></span> free', '<span class="lg lg-free"></span> вільно'),
    ('<span class="lg lg-sel"></span> wybrane', '<span class="lg lg-sel"></span> selected', '<span class="lg lg-sel"></span> обрано'),
    ('<span class="lg lg-busy"></span> zajęte', '<span class="lg lg-busy"></span> booked', '<span class="lg lg-busy"></span> зайнято'),
    ('hidden>Zaznacz co najmniej jeden termin, aby wysłać zapytanie.</p>', 'hidden>Select at least one time slot to send your enquiry.</p>', 'hidden>Позначте щонайменше один термін, щоб надіслати запит.</p>'),
    ('id="bkSubmit">Wyślij zapytanie</button>', 'id="bkSubmit">Send enquiry</button>', 'id="bkSubmit">Надіслати запит</button>'),
    ('<h3>Dziękujemy za zapytanie!</h3>', '<h3>Thank you for your enquiry!</h3>', '<h3>Дякуємо за запит!</h3>'),
    ('''<p>Otrzymaliśmy Twoje zgłoszenie i&nbsp;skontaktujemy się z&nbsp;Tobą tak szybko,
         jak to&nbsp;możliwe, zwykle w&nbsp;ciągu jednego dnia roboczego.</p>''',
     '''<p>We have received your enquiry and will contact you as soon
         as possible, usually within one working day.</p>''',
     '''<p>Ми отримали Ваш запит і&nbsp;звʼяжемося з&nbsp;Вами якнайшвидше,
         зазвичай протягом одного робочого дня.</p>'''),
    ('>Zamknij</button>', '>Close</button>', '>Закрити</button>'),

    # ---------- Formularz oglądania ----------
    ('<span class="eyebrow">Oglądanie gabinetu</span>', '<span class="eyebrow">Room viewing</span>', '<span class="eyebrow">Огляд кабінету</span>'),
    ('<h3 id="vwTitle">Umów się na oglądanie</h3>', '<h3 id="vwTitle">Book a viewing</h3>', '<h3 id="vwTitle">Запишіться на огляд</h3>'),
    ('<p>Wybierz dogodny dzień i&nbsp;porę. Oprowadzimy Cię po centrum, pokażemy wolne gabinety i&nbsp;odpowiemy na wszystkie pytania.</p>',
     '<p>Choose a convenient day and time. We will show you around the centre and the available rooms, and answer all your questions.</p>',
     '<p>Оберіть зручний день і&nbsp;час. Ми проведемо Вас центром, покажемо вільні кабінети й&nbsp;відповімо на всі запитання.</p>'),
    ('>Preferowana data *</label>', '>Preferred date *</label>', '>Бажана дата *</label>'),
    ('>Preferowana pora</label>', '>Preferred time</label>', '>Бажаний час</label>'),
    ('<span>To wstępna prośba o&nbsp;termin. <strong>Odezwiemy się, aby potwierdzić termin oglądania</strong>, zwykle w&nbsp;ciągu jednego dnia roboczego.</span>',
     '<span>This is a preliminary request. <strong>We will get in touch to confirm the viewing date</strong>, usually within one working day.</span>',
     '<span>Це попередній запит. <strong>Ми звʼяжемося з Вами, щоб підтвердити дату огляду</strong>, зазвичай протягом одного робочого дня.</span>'),
    ('<h3>Dziękujemy!</h3>', '<h3>Thank you!</h3>', '<h3>Дякуємо!</h3>'),
    ('<p>Otrzymaliśmy Twoją prośbę o&nbsp;oglądanie. Odezwiemy się, aby potwierdzić termin oglądania, zwykle w&nbsp;ciągu jednego dnia roboczego.</p>',
     '<p>We have received your viewing request. We will get in touch to confirm the viewing date, usually within one working day.</p>',
     '<p>Ми отримали Ваш запит на огляд. Ми звʼяжемося з&nbsp;Вами, щоб підтвердити дату огляду, зазвичай протягом одного робочого дня.</p>'),

    # ---------- Pasek mobilny, popupy, lightbox ----------
    ('aria-label="Szybkie akcje"', 'aria-label="Quick actions"', 'aria-label="Швидкі дії"'),
    ('</svg>\n    Zadzwoń\n  </a>', '</svg>\n    Call\n  </a>', '</svg>\n    Подзвонити\n  </a>'),
    ('</svg>\n    Oglądanie\n  </button>', '</svg>\n    Viewing\n  </button>', '</svg>\n    Огляд\n  </button>'),
    ('js-open-booking">Zarezerwuj</button>', 'js-open-booking">Book</button>', 'js-open-booking">Забронювати</button>'),
    ('aria-label="Aktualna promocja"', 'aria-label="Current offer"', 'aria-label="Актуальна акція"'),
    ('<span class="eyebrow">Promocja</span>', '<span class="eyebrow">Offer</span>', '<span class="eyebrow">Акція</span>'),
    ('aria-label="Galeria zdjęć"', 'aria-label="Photo gallery"', 'aria-label="Фотогалерея"'),
    ('aria-label="Poprzednie"', 'aria-label="Previous"', 'aria-label="Попереднє"'),
    ('aria-label="Następne"', 'aria-label="Next"', 'aria-label="Наступне"'),
]
