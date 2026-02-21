# AGENTS Guide

This file guides autonomous agents working in this repository.
Focus on minimal, conservative changes and respect submodules.

## Repository overview
- Root repo tracks song submodules under `songs/`.
- Python utilities live in `scripts/`.
- Test assets live in `tests/` and `scripts/msmodel_examples/`.
- `includes/` and `projects/` contain supporting assets.

## Cursor/Copilot rules
- No `.cursor/rules/`, `.cursorrules`, or `.github/copilot-instructions.md` files were found.

## Build, lint, and test commands
There is no formal build or lint system configured.
Use the following commands when you need to execute or verify behavior.

### Python environment
- The scripts expect Python 3.
- Dependencies are imported directly (e.g., `typer`, `xsdata`).
- Install missing packages with `python -m pip install <pkg>` in your active env.
- There is no lockfile; keep additions minimal and document new deps.

### Run a module or script
- Example: `python scripts/parser.py`
- Example: `python scripts/masager.py --help`
- Example: `python scripts/masager.py ls songs`

### Run all tests
- `python -m unittest` (from repo root)
- `python scripts/test_parser.py`

### Run a single test
- Class: `python -m unittest scripts.test_parser.TestMethods`
- Method: `python -m unittest scripts.test_parser.TestMethods.test_header`
- Another method: `python -m unittest scripts.test_parser.TestMethods.test_time_signature`

### Generate msmodel classes (optional)
- `python scripts/masager.py create-model <path>`
- This invokes `xsdata --package msmodel <path>` under the hood.
- Generated files live in `scripts/msmodel/` and `scripts/msmodel.py`.

## Submodules and content
- `songs/NNN/` entries are git submodules; avoid editing unless you intend to update the song repo.
- If you update a submodule, commit inside the submodule first, then commit the root update.
- Keep binary assets (`.mscx`, `.mscz`, `.pdf`) untouched unless explicitly editing musical content.
- Avoid reformatting lyric README files; many include non-ASCII text.

## Code style and conventions
Follow existing patterns in the file you touch; consistency beats personal preference.

### Python formatting
- 4-space indentation, no tabs.
- Keep line length reasonable (roughly 88-100 chars); wrap long literals.
- Use blank lines to separate logical sections and top-level defs.
- Preserve existing formatting in older files that use `%`-style formatting.
- Favor f-strings for new code unless matching surrounding style.

### Imports
- Order: standard library, third-party, then local imports.
- Prefer explicit imports; wildcard imports appear in parser modules and may be kept there.
- Keep one import per line unless a group is already grouped.
- Avoid circular imports between `parser.py` and `msmodel` modules.

### Naming
- Functions and variables: `snake_case`.
- Classes: `PascalCase` (e.g., `TypeHeader`).
- Constants: `UPPER_SNAKE_CASE`.
- Files and folders: lowercase or numeric names that match existing layout.

### Types and dataclasses
- Type hints are used sparingly; add them when they clarify inputs/outputs.
- Dataclasses are used for simple value objects.
- Use `Optional[...]` when a function can return `None`.
- Keep `dataclass` usage simple; avoid heavy inheritance.

### Error handling
- Prefer explicit checks and `None` returns over raising for expected absence.
- When catching exceptions, log or print a concise message and return a safe value.
- Avoid swallowing exceptions silently; include enough context to debug.
- Do not broad-catch exceptions inside tight loops unless necessary.

### Logging and output
- Current scripts use `print` for debug output; continue this style unless refactoring.
- For reusable helpers, allow a logger callback when practical (see `utils.run_bash_cmd`).
- Avoid introducing new logging frameworks without a strong reason.

### CLI patterns
- Scripts in `scripts/` use `typer` for CLI entrypoints.
- Keep `if __name__ == "__main__":` guards for runnable scripts.
- CLI functions should be small and delegate to helpers.
- Keep CLI output stable for existing workflows.

### Data and file handling
- Use `pathlib.Path` or `os.path` consistently within a file.
- Avoid writing to `songs/` or `tests/` unless the task requires it.
- When writing files, prefer explicit encoding and newline handling.
- Use `utils.get_full_path` and related helpers where already used.

### Testing style
- Unit tests live in `scripts/test_parser.py` and use `unittest`.
- Tests are verbose and print debug output; keep that behavior if extending tests.
- Name new tests `test_<behavior>` and add to `TestMethods` or new `unittest.TestCase`.
- Use local sample `.mscx` files from `scripts/msmodel_examples/`.

### Music domain specifics
- MuseScore parsing expects `.mscx` files and the generated `msmodel` classes.
- Preserve integer key/time signature mapping tables as-is.
- When updating pitch or duration logic, keep mapping dicts in sync.
- Avoid altering LilyPond markup strings unless you know the downstream format.

## Documentation style
- Keep docs short and factual; use Markdown headings and lists.
- Avoid large tables; prefer small bullet lists for commands.
- Keep examples runnable from repo root when possible.

## Git and workflow notes
- Do not add or remove submodules unless requested.
- Avoid committing large generated diffs without explaining why.
- Keep the repo root clean; do not add editor backups or cache files.

## Test assets
- Sample MuseScore files live in `scripts/msmodel_examples/`.
- `tests/untitled.mscx` is a raw fixture; avoid editing.
- Add new fixtures under `scripts/msmodel_examples/` when possible.
- Keep filenames descriptive and lowercase.

## Quick reference commands
```bash
# List MuseScore files under a path
python scripts/masager.py ls songs

# Copy MuseScore files to a directory
python scripts/masager.py cp songs /tmp

# Run parser tests
python -m unittest scripts.test_parser.TestMethods.test_time_signature
```

## Notes for future agents
- This repo mostly hosts content; code changes should be deliberate.
- There is no automated formatter or linter configured.
- If you introduce one, document it here and update CI expectations.
- Keep ASCII-only content unless a file already contains Unicode lyrics.

## If you are unsure
- Check `README.md` for submodule workflow.
- Inspect existing scripts in `scripts/` before introducing new patterns.
- Ask for clarification only when changes affect submodules or generated files.
- Default to the least disruptive change that satisfies the request.
