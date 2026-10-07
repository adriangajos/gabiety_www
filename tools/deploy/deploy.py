"""Wdrożenie strony na hosting OVH (plaszowska25.pl) przez SFTP.

Uruchom z katalogu głównego repo:
    python tools/deploy/deploy.py            # wysyła zmienione pliki
    python tools/deploy/deploy.py --dry-run  # tylko pokazuje, co by zrobił
    python tools/deploy/deploy.py --skip .htaccess  # pomija wskazane pliki (tym razem)

Jak to działa
- Na serwer trafiają tylko pliki strony (lista INCLUDE niżej), nigdy tools/, .git, .idea itp.
- Skrypt trzyma na serwerze manifest (sumy SHA-256 wgranych plików) poza katalogiem
  www, więc przy kolejnym wdrożeniu wysyła tylko to, co się zmieniło, i usuwa pliki,
  które zniknęły z repo. Usuwa wyłącznie pliki, które sam kiedyś wgrał.
- Serwer, login i hasło są w pliku netrc poza repo (domyślnie ~/.ovh-ftp/.ovh-ftp.txt,
  inna ścieżka: zmienna P25_NETRC). Format jednej linii (dane z panelu OVH, zakładka FTP - SSH):
      machine SERWER_FTP login LOGIN password HASLO
- Wymaga curl z obsługą sftp. Wbudowany curl Windows jej nie ma, więc domyślnie
  bierzemy ten z Git for Windows (inna ścieżka: zmienna P25_CURL).
"""
import argparse
import fnmatch
import hashlib
import json
import os
import subprocess
import sys
import tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Serwer i login bierzemy z pliku netrc (poza repo, które jest publiczne).
NETRC = os.environ.get('P25_NETRC', os.path.join(os.path.expanduser('~'), '.ovh-ftp', '.ovh-ftp.txt'))
CURL = os.environ.get('P25_CURL', 'C:/Program Files/Git/mingw64/bin/curl.exe')
# Odcisk klucza RSA serwera SFTP (ssh-keyscan, 2026-10-07). Jeśli OVH zmieni klucz,
# curl odmówi połączenia: sprawdź nowy odcisk i podmień.
HOST_KEY_SHA256 = 'itDZ6cuojUbG3+jrh5F/igkXa2xjzejbYJkNAlw8/VM'

INCLUDE = [
    '*.html', '.htaccess', 'favicon.ico', 'robots.txt', 'sitemap.xml', 'site.webmanifest',
    'llms.txt', 'en/*.html', 'ua/*.html', 'assets/**',
]


def server():
    """(host, katalog domowy) z pierwszej linii netrc: machine HOST login LOGIN password ..."""
    with open(NETRC, encoding='utf-8') as f:
        words = f.read().split()
    host, login = words[words.index('machine') + 1], words[words.index('login') + 1]
    return host, '/home/' + login


def local_files():
    files = {}
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        for name in filenames:
            rel = os.path.relpath(os.path.join(dirpath, name), ROOT).replace(os.sep, '/')
            if not any(match(rel, pat) for pat in INCLUDE):
                continue
            with open(os.path.join(ROOT, rel), 'rb') as f:
                files[rel] = hashlib.sha256(f.read()).hexdigest()
    return files


def match(rel, pat):
    if pat.endswith('/**'):
        return rel.startswith(pat[:-2])
    return fnmatch.fnmatchcase(rel, pat) and rel.count('/') == pat.count('/')


def curl(*args, check=True):
    cmd = [CURL, '-sS', '--netrc-file', NETRC, '--hostpubsha256', HOST_KEY_SHA256, *args]
    res = subprocess.run(cmd, capture_output=True)
    if check and res.returncode != 0:
        sys.exit('curl: ' + res.stderr.decode('utf-8', 'replace').strip())
    return res


def url(path):
    return f'sftp://{HOST}{path}'


def remote_manifest():
    res = curl(url(MANIFEST), check=False)
    if res.returncode == 0:
        return json.loads(res.stdout.decode('utf-8'))
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--skip', action='append', default=[], metavar='WZORZEC',
                    help='nie wysyłaj i nie usuwaj pasujących plików (manifest zachowuje ich starą wersję)')
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

    if not os.path.isfile(CURL):
        sys.exit(f'Nie znaleziono curl z obsługą sftp: {CURL} (ustaw P25_CURL)')
    if not os.path.isfile(NETRC):
        sys.exit(f'Brak pliku z danymi logowania: {NETRC}')

    global HOST, WEBROOT, MANIFEST
    HOST, home = server()
    WEBROOT, MANIFEST = home + '/www', home + '/.p25-deploy.json'

    local = local_files()
    old = remote_manifest()
    first = old is None
    old = old or {}
    for p in [p for p in set(local) | set(old) if any(fnmatch.fnmatchcase(p, s) for s in args.skip)]:
        if p in old:
            local[p] = old[p]
        else:
            local.pop(p, None)

    upload = sorted(p for p, h in local.items() if old.get(p) != h)
    delete = sorted(p for p in old if p not in local)

    print(f'Plików strony: {len(local)}, do wysłania: {len(upload)}, do usunięcia: {len(delete)}'
          + (' (pierwsze wdrożenie)' if first else ''))
    for p in upload:
        print('  +', p)
    for p in delete:
        print('  -', p)
    if args.dry_run or not (upload or delete or first):
        return

    if first:
        # Domyślna strona powitalna OVH to symlink do pliku systemowego; zapis przez
        # niego by się nie udał, więc usuwamy sam link ('*' = brak pliku to nie błąd).
        curl('-Q', f'*rm {WEBROOT}/index.html', url(WEBROOT + '/'), '-o', os.devnull)

    if upload:
        # Jedno wywołanie curl = jedno połączenie SSH dla wszystkich plików
        with tempfile.NamedTemporaryFile('w', suffix='.curl', delete=False, encoding='utf-8') as cfg:
            for p in upload:
                cfg.write(f'upload-file = "{os.path.join(ROOT, p).replace(os.sep, "/")}"\n')
                cfg.write(f'url = "{url(WEBROOT + "/" + p)}"\n')
        try:
            curl('--ftp-create-dirs', '-K', cfg.name)
        finally:
            os.unlink(cfg.name)

    for p in delete:
        curl('-Q', f'*rm {WEBROOT}/{p}', url(WEBROOT + '/'), '-o', os.devnull)

    with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False, encoding='utf-8') as m:
        json.dump(local, m, indent=0, sort_keys=True)
    try:
        curl('-T', m.name, url(MANIFEST))
    finally:
        os.unlink(m.name)
    print('Gotowe.')


if __name__ == '__main__':
    main()
