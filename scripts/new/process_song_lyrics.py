#!/usr/bin/env python3

import argparse
import subprocess
import sys
from pathlib import Path


SYLLABIFY_DIR = Path("/home/bebox/Work/Croatian-syllabification")
SYLLABIFY_SCRIPT = SYLLABIFY_DIR / "syllabify_cli.py"


def run_command(command: list[str], cwd: Path) -> str:
    result = subprocess.run(command, cwd=cwd, text=True, capture_output=True)
    if result.returncode != 0:
        details = result.stderr.strip() or result.stdout.strip() or "Unknown error"
        raise RuntimeError(details)
    return result.stdout


def get_song_root(mscx_file: Path) -> Path:
    if mscx_file.parent.name == "musescore":
        return mscx_file.parent.parent
    return mscx_file.parent


def keep_only_lyrics(raw_text: str) -> str:
    lines = []
    for line in raw_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("title =") or stripped.startswith("composer ="):
            continue
        lines.append(line.replace("'", ""))

    while lines and not lines[0].strip():
        lines.pop(0)

    text = "\n".join(lines)
    if text and not text.endswith("\n"):
        text += "\n"
    return text


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract lyrics and generate raw/mscx/syllabified text files for a MuseScore file."
    )
    parser.add_argument("mscx_file", help="Path to .mscx file")
    args = parser.parse_args()

    mscx_file = Path(args.mscx_file).resolve()
    if not mscx_file.exists():
        print(f"File not found: {mscx_file}", file=sys.stderr)
        return 1
    if mscx_file.suffix.lower() != ".mscx":
        print(f"Expected .mscx file, got: {mscx_file}", file=sys.stderr)
        return 1

    script_dir = Path(__file__).resolve().parent
    extractor_raw = script_dir / "lyrics_extractor.py"
    extractor_lines = script_dir / "lyrics_extractor_with_lines.py"

    song_root = get_song_root(mscx_file)
    song_name = mscx_file.stem

    raw_output = song_root / f"{song_name}_raw.txt"
    mscx_output = song_root / f"{song_name}_mscx.txt"
    syllb_output = song_root / f"{song_name}_syllb.txt"

    try:
        raw_text = run_command([sys.executable, str(extractor_raw), str(mscx_file)], cwd=script_dir)
        raw_output.write_text(keep_only_lyrics(raw_text), encoding="utf-8")

        mscx_text = run_command([sys.executable, str(extractor_lines), str(mscx_file)], cwd=script_dir)
        mscx_output.write_text(mscx_text, encoding="utf-8")

        syllb_text = run_command(
            [sys.executable, str(SYLLABIFY_SCRIPT), "-f", str(raw_output)],
            cwd=SYLLABIFY_DIR,
        )
        syllb_output.write_text(syllb_text, encoding="utf-8")
    except RuntimeError as error:
        print(f"Processing failed: {error}", file=sys.stderr)
        return 1

    print(f"Created: {raw_output}")
    print(f"Created: {mscx_output}")
    print(f"Created: {syllb_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
