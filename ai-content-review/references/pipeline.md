# Pipeline reference

## Flow

```
source doc ──(liteparse: lit parse --format text)──► layout text
            └─(.txt/.md: used directly)
layout text ──(anchor lines, mark pages)──► document.md
ai-tells.md (bundled criteria) ─┐
prompt.md / output-spec.md ─────┼──► <name>-review-package/
manifest.json / README.md ──────┘
package ──(agent harness runs prompt.md)──► report.md
```

The script (`build_package.py`) does only the deterministic prep: convert,
anchor, copy criteria + prompt + spec, write provenance. All judgment happens in
the review step, driven by `prompt.md` and `output-spec.md`.

## Dependencies

- **liteparse** (`pip install liteparse`) for non-text inputs. Provides the `lit`
  CLI. Office formats (`.docx`, `.pptx`, `.xlsx`) also need **LibreOffice**;
  images need **ImageMagick**. `.txt`/`.md` inputs need none of this.
- **Python 3.9+**. The catalog regenerator (`gen_rule_catalog.py`) additionally
  needs `pyyaml`, but only when rebuilding the catalog.

## Conversion notes

- `build_package.py` uses liteparse's **text** format for robust, layout-
  preserved output and numbers every line as an anchor.
- liteparse can also emit **JSON with bounding boxes**; if you want true
  page+coordinate locations rather than line numbers, extend `convert()` to call
  `lit parse --format json` and map blocks to pages. The text path is the default
  because its output shape is stable across versions.
- Page breaks are detected from form-feed (`\f`) characters and surfaced as
  `[p<n>]` markers. Plain prose without page structure simply gets line anchors.

## Why no Vale

The criteria originate as Vale rules, but this skill does **not** run Vale. The
rules are distilled into `ai-tells.md` so an agent can apply judgment — weighing
context, clustering, and false positives — instead of emitting raw lint hits. A
literal-match linter cannot tell a deliberate em-dash from an AI tell; the agent
can. The trade-off is that matching is no longer perfectly deterministic.

## Limitations

- Detection is heuristic. Expect false positives, especially on formal,
  translated, or non-native English writing, and on intentionally stylish prose.
- Absence of tells does not certify human authorship.
- The catalog reflects 2024-2025 patterns; tells drift over time. Re-run
  `gen_rule_catalog.py` against a fresh upstream checkout to update.
- Output is an editing aid and a prompt for human judgment — never an
  adjudication suitable for high-stakes accusations.
