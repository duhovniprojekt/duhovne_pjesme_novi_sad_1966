#!/usr/bin/env python3

import argparse
import difflib
import re
import subprocess
import sys
from pathlib import Path


SYLLABIFY_DIR = Path("/home/bebox/Work/Croatian-syllabification")
SYLLABIFY_SCRIPT = SYLLABIFY_DIR / "syllabify_cli.py"
APOSTROPHES = {"'", "’"}


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


def trim_trailing_spaces(text: str) -> str:
    lines = text.splitlines()
    trimmed = "\n".join(line.rstrip() for line in lines)
    if text.endswith("\n"):
        trimmed += "\n"
    return trimmed


def apply_hardcoded_exceptions(text: str) -> str:
    text = re.sub(r"\bgr\s*-\s*je\b", "grje", text)
    text = re.sub(r"\bGr\s*-\s*je\b", "Grje", text)
    return text


def restore_apostrophes_from_mscx(syllb_text: str, mscx_text: str) -> str:
    def strip_apostrophes(token: str) -> str:
        return "".join(ch for ch in token if ch not in APOSTROPHES)

    def rebuild_token_from_template(source_token: str, template_token: str) -> str:
        source_no_apost = strip_apostrophes(source_token)
        template_no_apost = strip_apostrophes(template_token)
        if source_no_apost != template_no_apost:
            return source_token

        rebuilt = []
        source_pos = 0
        for ch in template_token:
            if ch in APOSTROPHES:
                rebuilt.append(ch)
                continue

            if source_pos < len(source_no_apost):
                rebuilt.append(source_no_apost[source_pos])
                source_pos += 1

        if source_pos < len(source_no_apost):
            rebuilt.append(source_no_apost[source_pos:])

        return "".join(rebuilt)

    syllb_lines = syllb_text.splitlines()
    mscx_lines = mscx_text.splitlines()

    restored_lines = []
    for index, syllb_line in enumerate(syllb_lines):
        if index >= len(mscx_lines):
            restored_lines.append(syllb_line)
            continue

        mscx_line = mscx_lines[index]
        mscx_tokens = re.findall(r"\S+", mscx_line)
        syllb_parts = re.findall(r"\S+|\s+", syllb_line)
        syllb_token_part_indexes = [i for i, part in enumerate(syllb_parts) if not part.isspace()]
        syllb_tokens = [syllb_parts[i] for i in syllb_token_part_indexes]

        if not mscx_tokens or not syllb_tokens:
            restored_lines.append(syllb_line)
            continue

        mscx_norm = [strip_apostrophes(token) for token in mscx_tokens]
        syllb_norm = [strip_apostrophes(token) for token in syllb_tokens]

        matcher = difflib.SequenceMatcher(a=mscx_norm, b=syllb_norm, autojunk=False)
        for opcode, m_start, m_end, s_start, s_end in matcher.get_opcodes():
            if opcode != "equal":
                continue

            block_size = m_end - m_start
            for offset in range(block_size):
                m_token = mscx_tokens[m_start + offset]
                if not any(ch in APOSTROPHES for ch in m_token):
                    continue

                s_token_idx = s_start + offset
                if s_token_idx >= len(syllb_token_part_indexes):
                    continue

                part_idx = syllb_token_part_indexes[s_token_idx]
                syllb_parts[part_idx] = rebuild_token_from_template(
                    syllb_parts[part_idx],
                    m_token,
                )

        restored_lines.append("".join(syllb_parts))

    if len(mscx_lines) < len(syllb_lines):
        restored_lines.extend(syllb_lines[len(mscx_lines):])

    output = "\n".join(restored_lines)
    if syllb_text.endswith("\n"):
        output += "\n"
    return output


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
        mscx_text = trim_trailing_spaces(mscx_text)
        mscx_output.write_text(mscx_text, encoding="utf-8")

        syllb_text = run_command(
            [sys.executable, str(SYLLABIFY_SCRIPT), "-f", str(raw_output)],
            cwd=SYLLABIFY_DIR,
        )
        syllb_text = restore_apostrophes_from_mscx(syllb_text, mscx_text)
        syllb_text = apply_hardcoded_exceptions(syllb_text)
        syllb_output.write_text(trim_trailing_spaces(syllb_text), encoding="utf-8")
    except RuntimeError as error:
        print(f"Processing failed: {error}", file=sys.stderr)
        return 1

    print(f"Created: {raw_output}")
    print(f"Created: {mscx_output}")
    print(f"Created: {syllb_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
