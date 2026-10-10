"""Automated Quality Gate for Dimensional Images Research Documentation.

Stand-Alone, Relative-Path Verification Gate:
1. Resolves repository root relative to script location.
2. Asserts required core research documents exist.
3. Verifies all relative Markdown links point to existing files.
4. Verifies all embedded images exist and are valid readable images.
5. Strict Encoding Check: No UTF-8 BOM, strict LF line endings on all text files.
6. Validates all JSON, JSONL, and CSV protocol files.
7. Strict Privacy/Boundary Check: No hardcoded local drive paths or private credentials.
"""

import os
import re
import sys
import csv
import json
from pathlib import Path
from PIL import Image

SCRIPT_DIR = Path(__file__).resolve().parent

if len(sys.argv) > 1 and sys.argv[1].strip():
    BASE_DIR = Path(sys.argv[1]).resolve()
elif SCRIPT_DIR.name == "scripts":
    BASE_DIR = SCRIPT_DIR.parent
else:
    BASE_DIR = SCRIPT_DIR

REQUIRED_FILES = [
    "README.md",
    "METHODOLOGY.md",
    "LIMITATIONS.md",
    "EXPERIMENTS.md",
    "REFERENCES.md",
]


def verify_docs():
    errors = []
    checked_md_count = 0
    checked_links_count = 0
    checked_json_count = 0
    checked_csv_count = 0
    checked_images_count = 0

    if not BASE_DIR.exists() or not BASE_DIR.is_dir():
        print(f"[FATAL ERROR] Base directory does not exist: {BASE_DIR}")
        sys.exit(1)

    # 1. Verify existence of required core documentation files
    for req in REQUIRED_FILES:
        req_path = BASE_DIR / req
        if not req_path.is_file():
            errors.append(f"Required document missing: {req}")

    # Generic shapes only: the check must not itself name a private folder, user or repository.
    private_regex = re.compile(
        r"[A-Za-z]:[\\/]+-=\w|-=\w+=-|[\\/]+Users[\\/]+[^\\/\s]+[\\/]|"
        r"ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}"
    )

    link_regex = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
    img_regex = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")

    for root, dirs, files in os.walk(BASE_DIR):
        for f in files:
            fpath = Path(root) / f
            relpath = fpath.relative_to(BASE_DIR).as_posix()

            try:
                raw_bytes = fpath.read_bytes()
            except Exception as e:
                errors.append(f"Cannot read file {relpath}: {e}")
                continue

            # Check BOM
            if raw_bytes.startswith(b"\xef\xbb\xbf"):
                errors.append(f"UTF-8 BOM detected in {relpath}")

            # Check LF on text files only
            if f.endswith((".md", ".json", ".jsonl", ".csv", ".txt", ".py")):
                if b"\r\n" in raw_bytes:
                    errors.append(f"CRLF line endings detected in {relpath}")

            # Check JSON
            if f.endswith(".json"):
                try:
                    with open(fpath, "r", encoding="utf-8") as jf:
                        json.load(jf)
                    checked_json_count += 1
                except Exception as e:
                    errors.append(f"Invalid JSON in {relpath}: {e}")

            # Check JSONL
            elif f.endswith(".jsonl"):
                try:
                    with open(fpath, "r", encoding="utf-8") as jlf:
                        for lno, line in enumerate(jlf, 1):
                            line = line.strip()
                            if line:
                                json.loads(line)
                    checked_json_count += 1
                except Exception as e:
                    errors.append(f"Invalid JSONL in {relpath} line {lno}: {e}")

            # Check CSV
            elif f.endswith(".csv"):
                try:
                    with open(fpath, "r", encoding="utf-8") as cf:
                        reader = csv.reader(cf)
                        rows = list(reader)
                        if not rows:
                            errors.append(f"Empty CSV file in {relpath}")
                    checked_csv_count += 1
                except Exception as e:
                    errors.append(f"Invalid CSV in {relpath}: {e}")

            # Check Image readability
            elif f.endswith((".png", ".webp", ".jpg", ".jpeg")):
                try:
                    with Image.open(fpath) as im:
                        im.verify()
                    checked_images_count += 1
                except Exception as e:
                    errors.append(f"Corrupt image file in {relpath}: {e}")

            # Check Markdown links and leaks
            if f.endswith(".md"):
                checked_md_count += 1
                text = raw_bytes.decode("utf-8", errors="replace")

                # Check private leaks
                leak_match = private_regex.search(text)
                if leak_match:
                    errors.append(f"Private path or credential leak in {relpath}: '{leak_match.group(0)}'")

                # Check links
                for m in link_regex.finditer(text):
                    target = m.group(2).split("#")[0].strip()
                    if not target or target.startswith("http://") or target.startswith("https://") or target.startswith("mailto:"):
                        continue
                    checked_links_count += 1
                    target_path = (fpath.parent / target).resolve()
                    if not target_path.exists():
                        errors.append(f"Broken relative link in {relpath}: target '{target}' does not exist")

                # Check embedded images
                for m in img_regex.finditer(text):
                    img_target = m.group(2).split("#")[0].strip()
                    if not img_target or img_target.startswith("http://") or img_target.startswith("https://"):
                        continue
                    img_path = (fpath.parent / img_target).resolve()
                    if not img_path.exists():
                        errors.append(f"Broken image reference in {relpath}: image '{img_target}' does not exist")

    print("=== Research Docs Verification Summary ===")
    print(f"Repository root: {BASE_DIR}")
    print(f"Markdown files verified: {checked_md_count}")
    print(f"Relative links verified: {checked_links_count}")
    print(f"JSON / JSONL files verified: {checked_json_count}")
    print(f"CSV files verified: {checked_csv_count}")
    print(f"Images verified: {checked_images_count}")
    print(f"Total Errors / Violations: {len(errors)}")

    if errors:
        for err in errors:
            print(f"  [ERROR] {err}")
        sys.exit(1)
    else:
        print("[SUCCESS] All files pass all scientific publication quality gates!")
        sys.exit(0)


if __name__ == "__main__":
    verify_docs()
