"""Generator wersji językowych strony: /en/ i /ua/ budowane z polskich plików HTML.

Uruchom z katalogu głównego repo:   python tools/i18n/build.py

Jak to działa
- Polskie strony (index.html, faq.html, …) są źródłem prawdy.
- Dla każdej strony moduł w tools/i18n/pages/ zawiera pary tłumaczeń (pl, en, uk)
  — dokładne fragmenty tekstu/HTML z polskiej strony — oraz opcjonalnie całe
  przetłumaczone bloki (dokumenty prawne).
- Jeśli któryś polski fragment nie zostanie znaleziony (bo zmieniłeś tekst na
  stronie PL), skrypt PRZERYWA z błędem i pokazuje, który — wtedy popraw/uzupełnij
  tłumaczenie w module strony i uruchom ponownie. Dzięki temu w EN/UKR nie
  zostanie po cichu polski tekst.
- Na końcu skrypt wypisuje widoczne słowa z polskimi znakami, które zostały
  w wersjach EN/UKR (poza nazwami własnymi) — do szybkiego przejrzenia.
"""
import hashlib
import importlib
import io
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.dirname(__file__))

SITE = 'https://plaszowska25.pl/'
LANGS = {
    # kod języka strony, folder, og:locale, inLanguage
    'en': dict(code='en', folder='en', locale='en_GB', inlang='en-GB'),
    'uk': dict(code='uk', folder='ua', locale='uk_UA', inlang='uk-UA'),
}
PAGES = {
    'index.html': 'index',
    'faq.html': 'faq',
    'nasi-terapeuci.html': 'therapists',
    'polityka-prywatnosci.html': 'privacy',
    'regulamin.html': 'terms',
}
# Nazwy własne, które mogą zostać z polskimi znakami
PROPER = {'Płaszowska', 'Płaszowskiej', 'Płaszów', 'Kraków', 'Kraków.', 'Spółka', 'odpowiedzialnością', 'ograniczoną',
          'Płaszowska+25+Kraków', 'Płaszowskiej', 'Gabinety', 'z', 'o.o.'}

LANG_SWITCH_RE = re.compile(r'<nav class="lang-switch".*?</nav>', re.S)


def block_hash(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()[:16]


def lang_switch(fname, lang):
    cur = LANGS[lang]['folder']
    def href(target_folder):
        if target_folder == cur:
            return fname
        return ('../' + fname) if target_folder == '' else ('../' + target_folder + '/' + fname)
    items = [('', 'pl', 'PL'), ('en', 'en', 'EN'), ('ua', 'uk', 'UKR')]
    links = ''.join(
        f'<a href="{href(folder)}" hreflang="{hl}" lang="{hl}"{" aria-current=\"true\"" if hl == lang else ""}>{label}</a>'
        for folder, hl, label in items)
    return f'<nav class="lang-switch" aria-label="Język / Language / Мова">{links}</nav>'


def localize(html, fname, lang, mod):
    L = LANGS[lang]
    folder = L['folder']
    page_path = '' if fname == 'index.html' else fname

    # 1) bloki (całe przetłumaczone sekcje, np. treść regulaminu)
    for blk in getattr(mod, 'BLOCKS', []):
        start, end = blk['start'], blk['end']
        i = html.find(start)
        j = html.find(end, i)
        if i < 0 or j < 0:
            raise SystemExit(f'[{fname}] nie znaleziono bloku {start!r}…{end!r}')
        j += len(end)
        pl_block = html[i:j]
        if block_hash(pl_block) != blk['pl_hash']:
            raise SystemExit(
                f'[{fname}] polska treść bloku {start!r} zmieniła się (hash {block_hash(pl_block)} ≠ {blk["pl_hash"]}).\n'
                f'Zaktualizuj tłumaczenie w tools/i18n/pages/{PAGES[fname]}.py i wpisz nowy pl_hash.')
        html = html[:i] + blk[lang] + html[j:]

    # 2) pary tłumaczeń: wspólne + strony; najdłuższe najpierw (żeby krótkie nie psuły dłuższych)
    import common
    pairs = list(common.PAIRS) + list(getattr(mod, 'PAIRS', []))
    pairs.sort(key=lambda p: len(p[0]), reverse=True)
    missing = []
    for pl, en, uk in pairs:
        if pl in html:
            html = html.replace(pl, en if lang == 'en' else uk)
        elif (pl, en, uk) in getattr(mod, 'PAIRS', []):
            missing.append(pl)
    if missing:
        raise SystemExit(f'[{fname}] nie znaleziono polskich fragmentów (tekst PL się zmienił?):\n  - ' +
                         '\n  - '.join(m[:120] for m in missing))

    # 3) atrybuty techniczne
    html = html.replace('<html lang="pl">', f'<html lang="{L["code"]}">', 1)
    html = re.sub(r'(href|src|srcset)="(assets/|favicon\.ico|site\.webmanifest)', r'\1="../\2', html)
    # srcset z kilkoma wariantami: kolejne ścieżki po przecinku też poprawiamy
    html = re.sub(r'srcset="[^"]*"', lambda m: re.sub(r', assets/', ', ../assets/', m.group(0)), html)
    html = html.replace(f'<link rel="canonical" href="{SITE}', f'<link rel="canonical" href="{SITE}{folder}/')
    html = html.replace(f'<meta property="og:url" content="{SITE}', f'<meta property="og:url" content="{SITE}{folder}/')
    html = html.replace('<meta property="og:locale" content="pl_PL" />',
                        f'<meta property="og:locale" content="{L["locale"]}" />\n<meta property="og:locale:alternate" content="pl_PL" />')
    html = html.replace('"inLanguage": "pl-PL"', f'"inLanguage": "{L["inlang"]}"')
    html = re.sub(r'("item": "' + re.escape(SITE) + r')', r'\1' + folder + '/', html)
    html = LANG_SWITCH_RE.sub(lang_switch(fname, lang), html, count=1)
    if lang == 'uk':
        # Instrument Serif nie ma cyrylicy — dociągamy Cormorant Garamond (fallback w stosie fontów)
        html = html.replace('family=Instrument+Serif:ital@0;1&',
                            'family=Instrument+Serif:ital@0;1&family=Cormorant+Garamond:ital,wght@0,500;1,500&', 1)
    return html


def leftover_polish(html):
    text = re.sub(r'<(script|style)\b.*?</\1>', ' ', html, flags=re.S)
    text = re.sub(r'<div id="tweaks">.*?\n</div>', ' ', text, flags=re.S)  # ukryty panel edycji (narzędzie wewnętrzne)
    text = re.sub(r'<[^>]+>', ' ', text)
    words = set(re.findall(r'[\wąćęłńóśźżĄĆĘŁŃÓŚŹŻ.+]*[ąćęłńóśźżĄĆĘŁŃÓŚŹŻ][\wąćęłńóśźżĄĆĘŁŃÓŚŹŻ.+]*', text))
    return sorted(w for w in words if w not in PROPER)


SITEMAP = {  # strona: (changefreq, priorytet wersji PL)
    'index.html': ('weekly', 1.0),
    'nasi-terapeuci.html': ('monthly', 0.7),
    'faq.html': ('monthly', 0.6),
    'polityka-prywatnosci.html': ('yearly', 0.3),
    'regulamin.html': ('yearly', 0.3),
}


def write_sitemap():
    import datetime
    today = datetime.date.today().isoformat()
    def url(fname, folder):
        path = '' if fname == 'index.html' else fname
        return f'{SITE}{folder + "/" if folder else ""}{path}'
    variants = [('', 'pl')] + [(L['folder'], code) for code, L in LANGS.items()]
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for fname, (freq, prio) in SITEMAP.items():
        alts = ''.join(f'\n    <xhtml:link rel="alternate" hreflang="{hl}" href="{url(fname, f)}"/>' for f, hl in variants)
        alts += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{url(fname, "")}"/>'
        for folder, _ in variants:
            p = prio if not folder else round(prio * 0.8, 1)
            out.append(f'  <url>\n    <loc>{url(fname, folder)}</loc>\n    <lastmod>{today}</lastmod>\n'
                       f'    <changefreq>{freq}</changefreq>\n    <priority>{p}</priority>{alts}\n  </url>')
    out.append('</urlset>\n')
    io.open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8', newline='\n').write('\n'.join(out))


def main():
    write_sitemap()
    report = []
    for fname, modname in PAGES.items():
        mod = importlib.import_module('pages.' + modname)
        src = io.open(os.path.join(ROOT, fname), encoding='utf-8').read()
        for lang, L in LANGS.items():
            out = localize(src, fname, lang, mod)
            out_dir = os.path.join(ROOT, L['folder'])
            os.makedirs(out_dir, exist_ok=True)
            io.open(os.path.join(out_dir, fname), 'w', encoding='utf-8', newline='').write(out)
            left = leftover_polish(out)
            if left:
                report.append(f'{L["folder"]}/{fname}: {", ".join(left)}')
    print('Wygenerowano:', ', '.join(f'{L["folder"]}/' for L in LANGS.values()))
    if report:
        print('\nUwaga — słowa z polskimi znakami pozostałe w tłumaczeniach (sprawdź, czy to nazwy własne):')
        print('\n'.join('  ' + r for r in report))


if __name__ == '__main__':
    main()
