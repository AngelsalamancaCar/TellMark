# ai-content-review

Prepare and run a **"potential AI content"** review of a document. The project
converts any document into a self-contained *prompt-package folder* and lets an
agent (Claude CLI or any other harness) review it — flagging passages that read
as AI-generated or AI-polished and suggesting concrete rewrites.

> **It is an editing aid, not an authorship verdict.** The signals it uses are
> heuristic. They over-flag formal, translated, and non-native English writing,
> and absence of signals does not certify human authorship. Do not use the output
> as the basis for an accusation.

## How it works

```
source doc ──(liteparse: lit parse --format text)──► layout text
            └─(.txt / .md: used directly)
layout text ──(line-anchor + page markers)──► document.md
-l en|es ──► picks rules.md (ai-tells.md / es-tells.md) + fills {LANG_NAME} in prompt.md
bundled criteria + prompt + spec ──────────────────► <name>-review-package/
package ──(agent harness runs prompt.md)──► report.md, written in {LANG_NAME}
```

Two clean stages, and one thing that passes between them:

1. **Prepare (deterministic).** `build_package.py` converts the document and
   assembles a portable folder containing everything an agent needs. You tell
   it the document's language with `-l` (`en` default, or `es`); that choice
   picks the matching tell catalog (`ai-tells.md` / `es-tells.md`) **and** gets
   baked into `prompt.md` as `{LANG_NAME}` (e.g. "English" / "Spanish").
2. **Review (judgment).** An agent reads the package's prompt and criteria,
   weighs each candidate signal *in context*, and writes `report.md`. No linter
   runs — judgment is the whole point.

### How phase 1 and phase 2 connect

The only handoff between the two phases is the package folder — phase 2 never
talks back to phase 1, and phase 1 never judges. Concretely:

- Phase 1 picks **which catalog** (`rules.md`) phase 2 validates against, based
  on the `-l` flag.
- That same `-l` choice decides **the report's output language**. There is no
  separate "what language should the report be in" prompt — phase 2 always
  writes `report.md` in the language phase 1 was told the document is in
  (`{LANG_NAME}` in `prompt.md`, filled from `CATALOGS[lang]["name"]` in
  `build_package.py`). Quoted extracts inside the report stay verbatim in the
  document's original language; everything the agent writes around them
  (assessment, headers, explanations, rewrite suggestions) uses `{LANG_NAME}`.
- `manifest.json` records the `lang` that was chosen, so the package is
  self-describing even outside this repo.

## What a generated package contains

| File | Purpose |
|---|---|
| `document.md` | The source text, converted and line-anchored (`L<n>`, with `[p<n>]` page markers). |
| `rules.md` | The AI-tell criteria catalog the agent validates against (`ai-tells.md` or `es-tells.md`, per `-l`). |
| `prompt.md` | The standardized review instruction, with `{LANG_NAME}` filled in so the agent knows what language to write `report.md` in. |
| `output-spec.md` | The exact report format the agent must produce. |
| `manifest.json` | Provenance: source hash, converter, tool versions, timestamp, the `lang` chosen and catalog used. |
| `README.md` | How to run the package in any harness. |
| `report.md` | Written by the agent during phase 2 — not present right after `build_package.py` runs. |

The folder is self-contained — hand it to any agent and it has full context.

## Install

- **Python 3.9+** (required).
- **liteparse** for non-text inputs: `pip install liteparse` (provides the `lit`
  CLI). `.txt` / `.md` inputs need nothing extra.
- **LibreOffice** for `.docx` / `.pptx` / `.xlsx`; **ImageMagick** for images —
  only if you feed those formats.
- **PyYAML** only if you regenerate the rule catalog.

## Usage

### Build a package

```bash
python3 scripts/build_package.py "path/to/document.pdf" -o "doc-review-package"        # English (default)
python3 scripts/build_package.py "path/to/documento.pdf" -o "doc-review-package" -l es  # Spanish
```

Accepts PDF, DOCX, PPTX, images (via liteparse), or `.txt` / `.md` (used as-is).
`-l` (`en` default, `es`) picks the document's language — it selects the tell
catalog **and** the language `report.md` will be written in (see
[How phase 1 and phase 2 connect](#how-phase-1-and-phase-2-connect)).

### Run the review

**As a skill.** Drop the project into an agent that supports skills (it ships a
`SKILL.md`). Ask something like *"check this draft for AI writing"* and it builds
the package and produces the report.

**Manually, with Claude CLI:**

```bash
cd doc-review-package
claude -p "$(cat prompt.md)

=== rules.md ===
$(cat rules.md)

=== document.md ===
$(cat document.md)

=== output-spec.md ===
$(cat output-spec.md)" > report.md
```

Any other harness works too: feed `prompt.md` as the instruction and the other
files as context.

## The rule catalog

`assets/rules/ai-tells.md` is a 60-criterion catalog distilled from the
open-source [**vale-ai-tells**](https://github.com/tbhb/vale-ai-tells) project
(the `ai-tells` prose pack), grouped into vocabulary, hedging, promotional
register, rhetorical cadence, filler/metacommentary, headings, punctuation, and
tone. To update it against a newer upstream release:

```bash
# clone https://github.com/tbhb/vale-ai-tells first
python3 scripts/gen_rule_catalog.py /path/to/vale-ai-tells/styles/ai-tells \
    -o assets/rules/ai-tells.md
```

`assets/rules/es-tells.md` is the Spanish counterpart, selected with `-l es`.
Unlike `ai-tells.md` it is **hand-authored** — there's no upstream Spanish pack
to regenerate from — so it carries its own provenance notice
(`ES-TELLS-NOTICE.txt`) alongside the shared vale-ai-tells license.

## Limitations & responsible use

- Heuristic detection with real false-positive rates; treat every hit as a
  *candidate* for human judgment.
- Especially unreliable on non-native, translated, or deliberately formal prose.
- The catalog reflects 2024–2025 patterns and drifts over time.
- Intended to help authors *improve* writing, not to adjudicate who wrote it.

## Repository layout

```
.
├── SKILL.md                       # skill manifest + workflow (triggering)
├── scripts/
│   ├── build_package.py           # convert + assemble the package
│   └── gen_rule_catalog.py        # regenerate the catalog from upstream
├── assets/
│   ├── rules/
│   │   ├── ai-tells.md            # English criteria catalog (generated, default)
│   │   ├── es-tells.md            # Spanish criteria catalog (hand-authored, -l es)
│   │   ├── ES-TELLS-NOTICE.txt    # provenance notice for es-tells.md
│   │   └── VALE-AI-TELLS-LICENSE.txt
│   └── templates/
│       ├── prompt.md              # standardized review prompt ({LANG_NAME} placeholder)
│       ├── output-spec.md         # report format
│       └── package-readme.md      # README placed in each package
└── references/
    └── pipeline.md                # pipeline internals, deps, limits
```

## Attribution & license

This repository is licensed under the **MIT License** — see [`LICENSE`](LICENSE).
You may use, copy, modify, and redistribute it with attribution and no warranty.

The bundled tell catalog is derived from **vale-ai-tells** by Tony Burns,
MIT-licensed (see `assets/rules/VALE-AI-TELLS-LICENSE.txt`). Conversion uses
[liteparse](https://github.com/run-llama/liteparse) (Apache-2.0) by LlamaIndex.
Redistributing the catalog must preserve the vale-ai-tells MIT notice.
