# Elementy wspólne dla wszystkich stron (nawigacja, menu mobilne, stopki podstron).
# Format: (fragment PL, EN, UKR). Fragmenty, których nie ma na danej stronie, są pomijane.
# Zasada redakcyjna: bez pauzy „—" w tekstach (w żadnym języku).
PAIRS = [
    # nawigacja i menu mobilne
    ('>O centrum</a>', '>About</a>', '>Про центр</a>'),
    ('>Oferta</a>', '>Offer</a>', '>Пропозиція</a>'),
    ('>Gabinety</a>', '>Rooms</a>', '>Кабінети</a>'),
    ('>Cennik</a>', '>Prices</a>', '>Ціни</a>'),
    ('>Dostępność</a>', '>Availability</a>', '>Наявність</a>'),
    ('>Nasi terapeuci</a>', '>Our therapists</a>', '>Наші терапевти</a>'),
    ('>Kontakt</a>', '>Contact</a>', '>Контакти</a>'),
    ('>Zarezerwuj gabinet</a>', '>Book a room</a>', '>Забронювати кабінет</a>'),
    ('>Zarezerwuj</a>', '>Book</a>', '>Забронювати</a>'),
    ('aria-label="Zamknij"', 'aria-label="Close"', 'aria-label="Закрити"'),
    ('aria-label="Menu">≡</button>', 'aria-label="Menu">≡</button>', 'aria-label="Меню">≡</button>'),
    ('aria-label="Menu" aria-expanded="false">≡</button>', 'aria-label="Menu" aria-expanded="false">≡</button>', 'aria-label="Меню" aria-expanded="false">≡</button>'),
    ('alt="Centrum Terapeutyczne Płaszowska 25"', 'alt="Płaszowska 25 Therapy Centre"', 'alt="Терапевтичний центр Płaszowska 25"'),

    # stopki podstron
    ('>Strona główna</a>', '>Home</a>', '>Головна</a>'),
    ('>Polityka prywatności</a>', '>Privacy policy</a>', '>Політика конфіденційності</a>'),
    ('>Regulamin</a>', '>Terms</a>', '>Регламент</a>'),
    ('data-cookie-settings>Ustawienia cookies</button>', 'data-cookie-settings>Cookie settings</button>', 'data-cookie-settings>Налаштування cookies</button>'),
    ('© 2026 Centrum Terapeutyczne Płaszowska 25, Kraków', '© 2026 Płaszowska 25 Therapy Centre, Kraków', '© 2026 Терапевтичний центр Płaszowska 25, Краків'),
    ('© Centrum Terapeutyczne Płaszowska 25, Kraków', '© Płaszowska 25 Therapy Centre, Kraków', '© Терапевтичний центр Płaszowska 25, Краків'),

    # dane strukturalne: okruszki
    ('"name": "Strona główna"', '"name": "Home"', '"name": "Головна"'),
]
