#!/usr/bin/env python3

import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path


def extract_lyrics_with_lines(mscx_path: Path) -> dict[str, str]:
    root = ET.parse(mscx_path).getroot()
    verses = defaultdict(str)

    for lyric in root.findall(".//Lyrics"):
        text = (lyric.findtext("text") or "").strip()
        if not text:
            continue

        no = (lyric.findtext("no") or "0").strip()
        syllabic = (lyric.findtext("syllabic") or "").strip()

        if syllabic in ("begin", "middle"):
            verses[no] += text + "-"
        else:
            verses[no] += text + " "

    return {k: v.strip() for k, v in verses.items()}


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/new/lyrics_extractor_with_lines.py <path-to-file.mscx>")
        return 1

    mscx_path = Path(sys.argv[1])
    if not mscx_path.exists():
        print(f"File not found: {mscx_path}")
        return 1

    try:
        verses = extract_lyrics_with_lines(mscx_path)
    except Exception as e:
        print(f"Failed to parse {mscx_path}: {e}")
        return 1

    for no in sorted(verses.keys(), key=lambda x: int(x)):
        line_no = int(no) + 1
        print(f"[{line_no}] {verses[no]}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
