
import json
import hashlib
import argparse
from pathlib import Path


def calculate_sha256(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def generate_manifest(folder, base_url):
    root = Path(folder).resolve()
    output = Path(__file__).resolve().parent / "manifest.json"

    if not root.is_dir():
        raise FileNotFoundError(f"A mappa nem található: {root}")

    files = []

    for file_path in sorted(root.rglob("*")):
        if not file_path.is_file():
            continue

        relative_path = file_path.relative_to(root).as_posix()
        file_hash = calculate_sha256(file_path)

        download_url = (
            base_url.rstrip("/") + "/" + relative_path
        )

        files.append({
            "path": relative_path,
            "sha256": file_hash,
            "url": download_url
        })

        print(f"[HASH OK] {relative_path}")

    manifest = {
        "files": files
    }

    with open(output, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=4, ensure_ascii=False)

    print("\n============================")
    print("MANIFEST ELKÉSZÜLT!")
    print(f"Fájlok száma: {len(files)}")
    print(f"Mentés helye: {output}")
    print("============================")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("folder")
    parser.add_argument("--base-url", required=True)

    args = parser.parse_args()

    generate_manifest(args.folder, args.base_url)
