#!/usr/bin/env python3
"""SHA256 manifest for a BepInEx mod collection.

Excludes configuration files, package documentation, debug symbols and
well-known distribution metadata while preserving game assets of any type.
"""

import argparse
import hashlib
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import quote


DOC_NAME_RE = re.compile(
    r"^(?:readme|read[ -]?me|changelog|change[ -]?log|changes|"
    r"license|licence|copying|notice|authors|contributors|contributing)"
    r"(?:$|[._ -].*)",
    re.IGNORECASE,
)

# Do NOT exclude all .json, .png, .txt, or extensionless files: mods can load them.
IGNORED_FILES = {".megaignore", ".ds_store", "thumbs.db", "desktop.ini"}
IGNORED_DIRS = {".git", ".github", "__pycache__", ".vs"}
IGNORED_SUFFIXES = {".cfg", ".pdb", ".bak", ".tmp"}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def is_package_metadata(relative: Path) -> bool:
    """Exclude only standard mod-package root metadata, not nested assets."""
    parts = relative.parts
    if len(parts) == 3 and parts[0].casefold() == "plugins":
        # plugins/<mod package>/icon.png and manifest.json
        return parts[2].casefold() in {"icon.png", "manifest.json"}
    return False


def skip_reason(file_path: Path, root: Path, output: Path) -> str | None:
    relative = file_path.relative_to(root)
    lower_name = file_path.name.casefold()

    if file_path.resolve() == output.resolve():
        return "generált manifest"
    if any(part.casefold() in IGNORED_DIRS for part in relative.parts[:-1]):
        return "fejlesztői mappa"
    if lower_name in IGNORED_FILES:
        return "segédfájl"
    if file_path.suffix.casefold() in IGNORED_SUFFIXES:
        return "konfiguráció / debug / ideiglenes fájl"
    if DOC_NAME_RE.match(file_path.name):
        return "dokumentáció / licenc"
    if is_package_metadata(relative):
        return "modcsomag metaadat"
    # .xml paired with a .dll is generally API documentation. Other .xml files stay.
    if file_path.suffix.casefold() == ".xml" and file_path.with_suffix(".dll").is_file():
        return "DLL-hez tartozó XML dokumentáció"
    return None


def remote_sha256(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "LC-Mod-Patcher-Manifest-Generator/1.0"})
    digest = hashlib.sha256()
    with urllib.request.urlopen(request, timeout=45) as response:
        for block in iter(lambda: response.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def generate_manifest(folder: str, base_url: str, output_file: str | None,
                      verify_remote: bool) -> int:
    root = Path(folder).expanduser().resolve()
    if not root.is_dir():
        print(f"HIBA: A forrásmappa nem található: {root}", file=sys.stderr)
        return 1

    output = (Path(output_file).expanduser().resolve() if output_file
              else Path(__file__).resolve().parent / "manifest.json")
    base_url = base_url.rstrip("/")
    if not base_url.startswith("https://"):
        print("HIBA: A --base-url HTTPS címmel kezdődjön.", file=sys.stderr)
        return 1

    entries = []
    skipped = {}
    errors = []

    for file_path in sorted(root.rglob("*")):
        if not file_path.is_file() or file_path.is_symlink():
            continue
        reason = skip_reason(file_path, root, output)
        if reason:
            skipped[reason] = skipped.get(reason, 0) + 1
            continue

        relative_path = file_path.relative_to(root).as_posix()
        url = base_url + "/" + quote(relative_path, safe="/")
        local_hash = sha256_file(file_path)

        if verify_remote:
            try:
                github_hash = remote_sha256(url)
                if github_hash != local_hash:
                    errors.append(f"SHA256 ELTÉRÉS: {relative_path}\n"
                                  f"  Helyi:  {local_hash}\n"
                                  f"  GitHub: {github_hash}")
                    continue
            except (urllib.error.URLError, TimeoutError, OSError) as exc:
                errors.append(f"LETÖLTÉSI HIBA: {relative_path}: {exc}")
                continue

        entries.append({"path": relative_path, "sha256": local_hash, "url": url})
        print(f"[OK] {relative_path}")

    print(f"\nManifestbe kerülő fájlok: {len(entries)}")
    for reason, count in sorted(skipped.items()):
        print(f"Kihagyva – {reason}: {count}")

    if errors:
        print(f"\n{len(errors)} HIBA: a manifest NEM lett felülírva!", file=sys.stderr)
        for message in errors:
            print(message, file=sys.stderr)
        print("Javítsd a GitHub 'files/' tartalmát vagy a forrásmappát, majd futtasd újra.",
              file=sys.stderr)
        return 1

    output.parent.mkdir(parents=True, exist_ok=True)
    tmp = output.with_name(output.name + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as stream:
        json.dump({"files": entries}, stream, ensure_ascii=False, indent=4)
        stream.write("\n")
    tmp.replace(output)
    print(f"Manifest elkészült: {output}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="BepInEx SHA256 manifest készítése")
    parser.add_argument("folder", help="A GitHub 'files/' mappájának megfelelő helyi mappa")
    parser.add_argument("--base-url", required=True, help="A GitHub raw files/ alap URL-je")
    parser.add_argument("--output", help="Manifest mentésének helye (alapból a script mellett)")
    parser.add_argument("--verify-remote", action="store_true",
                        help="Ellenőrzi minden fájl GitHub-hashét; eltéréskor nem írja felül a manifestet")
    args = parser.parse_args()
    return generate_manifest(args.folder, args.base_url, args.output, args.verify_remote)


if __name__ == "__main__":
    raise SystemExit(main())
