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
bundled criteria + prompt + spec ──────────────────► <name>-review-package/
package ──(agent harness runs prompt.md)──► report.md
```

Two clean stages:

1. **Prepare (deterministic).** `build_package.py` converts the document and
   assembles a portable folder containing everything an agent needs.
2. **Review (judgment).** An agent reads the package's prompt and criteria,
   weighs each candidate signal *in context*, and writes the report. No linter
   runs — judgment is the whole point.

## What a generated package contains

| File | Purpose |
|---|---|
| `document.md` | The source text, converted and line-anchored (`L<n>`, with `[p<n>]` page markers). |
| `rules.md` | The AI-tell criteria catalog the agent validates against. |
| `prompt.md` | The standardized review instruction. |
| `output-spec.md` | The exact report format the agent must produce. |
| `manifest.json` | Provenance: source hash, converter, tool versions, timestamp. |
| `README.md` | How to run the package in any harness. |

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
python3 scripts/build_package.py "path/to/document.pdf" -o "doc-review-package"
```

Accepts PDF, DOCX, PPTX, images (via liteparse), or `.txt` / `.md` (used as-is).

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
│   │   ├── ai-tells.md            # the criteria catalog (bundled)
│   │   └── VALE-AI-TELLS-LICENSE.txt
│   └── templates/
│       ├── prompt.md              # standardized review prompt
│       ├── output-spec.md         # report format
│       └── package-readme.md      # README placed in each package
└── references/
    └── pipeline.md                # pipeline internals, deps, limits
```

## Attribution & license

The bundled tell catalog is derived from **vale-ai-tells** by Tony Burns,
MIT-licensed (see `assets/rules/VALE-AI-TELLS-LICENSE.txt`). Conversion uses
[liteparse](https://github.com/run-llama/liteparse) (Apache-2.0) by LlamaIndex.

Choose and add a license for this repository itself (e.g. `LICENSE` at the root);
note that redistributing the catalog must preserve the vale-ai-tells MIT notice.
