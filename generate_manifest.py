import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import quote


def calculate_sha256(file_path: Path) -> str:
    sha256 = hashlib.sha256()
    with file_path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            sha256.update(chunk)
    return sha256.hexdigest()


def generate_manifest(folder: str, base_url: str) -> None:
    root = Path(folder).resolve()
    output = Path(__file__).resolve().parent / 'manifest.json'

    if not root.is_dir():
        raise FileNotFoundError(f'A mappa nem található: {root}')
    if not base_url.lower().startswith('https://'):
        raise ValueError('A --base-url HTTPS URL legyen.')

    files = []
    skipped_cfg = 0
    skipped_mega = 0

    for file_path in sorted(root.rglob('*')):
        if not file_path.is_file():
            continue

        if file_path.suffix.lower() == '.cfg':
            skipped_cfg += 1
            print(f'[CFG KIHAGYVA] {file_path.relative_to(root).as_posix()}')
            continue

        if file_path.name.lower() == '.megaignore':
            skipped_mega += 1
            print(f'[MEGA KIHAGYVA] {file_path.relative_to(root).as_posix()}')
            continue

        relative_path = file_path.relative_to(root).as_posix()
        file_hash = calculate_sha256(file_path)
        # Az egyes útvonalszegmensek URL-kódolása; a / elválasztók megmaradnak.
        url_path = quote(relative_path, safe='/')
        download_url = base_url.rstrip('/') + '/' + url_path

        files.append({'path': relative_path, 'sha256': file_hash, 'url': download_url})
        print(f'[HASH OK] {relative_path}')

    with output.open('w', encoding='utf-8') as stream:
        json.dump({'files': files}, stream, indent=4, ensure_ascii=False)

    print('\n============================')
    print('MANIFEST ELKÉSZÜLT!')
    print(f'Fájlok száma: {len(files)}')
    print(f'CFG kihagyva: {skipped_cfg}')
    print(f'.megaignore kihagyva: {skipped_mega}')
    print(f'Mentés helye: {output}')
    print('============================')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='LC Mod Patcher manifest generátor')
    parser.add_argument('folder', help='A GitHub files/ mappájával egyező helyi mappa')
    parser.add_argument('--base-url', required=True, help='GitHub raw files/ URL')
    args = parser.parse_args()
    generate_manifest(args.folder, args.base_url)
