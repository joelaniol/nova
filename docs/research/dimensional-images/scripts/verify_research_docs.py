"""Automated Quality Gate for Dimensional Images Research Documentation.

Verifies:
1. All Markdown links point to existing files.
2. All embedded images exist and are valid readable images.
3. No UTF-8 BOM, strict LF line endings.
4. All JSON and CSV protocol files parse cleanly.
5. Strict Boundary Check: Zero references to private paths or internal code outside the research folder.
"""

import os
import re
import csv
import json
from PIL import Image

BASE_DIR = r"E:\-=Entwicklung=-\NovaBrowser\public\docs\research\dimensional-images"
RESEARCH_README = r"E:\-=Entwicklung=-\NovaBrowser\public\docs\research\README.md"

def verify_docs():
    errors = []
    checked_md_count = 0
    checked_links_count = 0
    checked_json_count = 0
    checked_csv_count = 0
    checked_images_count = 0

    private_regex = re.compile(
        r"[A-Za-z]:[\\/]+-=|-=Entwicklung=-|[\\/]+Users[\\/]+GNetwork\b|"
        r"dev-programme|nova_ai_workspace|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|clk_[A-Za-z0-9]{16,}"
    )

    for root, dirs, files in os.walk(BASE_DIR):
        for f in files:
            fpath = os.path.join(root, f)
            relpath = os.path.relpath(fpath, BASE_DIR)

            with open(fpath, "rb") as fp:
                raw_bytes = fp.read()

            # Check BOM
            if raw_bytes.startswith(b"\xef\xbb\xbf"):
                errors.append(f"UTF-8 BOM detected in {relpath}")

            # Check LF on text files only
            if f.endswith((".md", ".json", ".jsonl", ".csv", ".txt", ".html", ".css", ".js")):
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
                            if line.strip():
                                json.loads(line)
                    checked_json_count += 1
                except Exception as e:
                    errors.append(f"Invalid JSONL in {relpath} (line {lno}): {e}")

            # Check CSV
            elif f.endswith(".csv"):
                try:
                    with open(fpath, "r", encoding="utf-8") as cf:
                        reader = csv.reader(cf)
                        rows = list(reader)
                        if not rows:
                            errors.append(f"Empty CSV in {relpath}")
                    checked_csv_count += 1
                except Exception as e:
                    errors.append(f"Invalid CSV in {relpath}: {e}")

            # Check Images
            elif f.endswith(".png") or f.endswith(".webp"):
                try:
                    with Image.open(fpath) as img:
                        img.verify()
                    checked_images_count += 1
                except Exception as e:
                    errors.append(f"Corrupt image {relpath}: {e}")

            # Check Markdown
            elif f.endswith(".md"):
                checked_md_count += 1
                text = raw_bytes.decode("utf-8")

                # Boundary check
                if private_regex.search(text):
                    m = private_regex.search(text).group(0)
                    errors.append(f"Private content leak '{m}' in {relpath}")

                # Check Markdown links
                links = re.findall(r"\[.*?\]\((.*?)\)", text)
                for link in links:
                    if link.startswith("http://") or link.startswith("https://") or link.startswith("#") or link.startswith("mailto:"):
                        continue
                    clean_link = link.split("#")[0]
                    if not clean_link:
                        continue
                    target_path = os.path.normpath(os.path.join(root, clean_link))
                    checked_links_count += 1
                    if not os.path.exists(target_path):
                        errors.append(f"Broken link '{link}' in {relpath} -> {target_path}")

    # Check Research README
    if os.path.exists(RESEARCH_README):
        with open(RESEARCH_README, "rb") as fp:
            raw = fp.read()
            if raw.startswith(b"\xef\xbb\xbf"):
                errors.append("UTF-8 BOM in public/docs/research/README.md")

    print(f"=== Research Docs Verification Summary ===")
    print(f"Markdown files verified: {checked_md_count}")
    print(f"Relative links verified: {checked_links_count}")
    print(f"JSON / JSONL files verified: {checked_json_count}")
    print(f"CSV files verified: {checked_csv_count}")
    print(f"Images verified: {checked_images_count}")
    print(f"Total Errors / Violations: {len(errors)}")

    if errors:
        for err in errors:
            print(f"  [ERROR] {err}")
        return False
    else:
        print("[SUCCESS] All files pass all scientific publication quality gates!")
        return True

if __name__ == "__main__":
    import sys
    success = verify_docs()
    sys.exit(0 if success else 1)
