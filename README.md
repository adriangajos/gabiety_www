# gabiety_www
Płaszowska 25 - Gabinety - WWW

## Wersje językowe (EN / UKR)

Strony w `en/` i `ua/` są **generowane** z polskich plików, nie edytuj ich ręcznie.

1. Zmień tekst na polskiej stronie (np. `index.html`).
2. Uzupełnij tłumaczenie w `tools/i18n/pages/<strona>.py` (wspólne elementy: `tools/i18n/common.py`).
3. Uruchom `python tools/i18n/build.py`. Skrypt zatrzyma się, jeśli jakiś polski fragment nie ma tłumaczenia, i odświeży `sitemap.xml`.

Teksty generowane w JavaScript (terminarz, formularze, cookies) są w `assets/js/i18n.js`.
Po zmianach w CSS/JS podbij parametr `?v=` w linkach do plików.
