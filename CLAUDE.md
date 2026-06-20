# CLAUDE.md

Guidance for AI coding agents working in this repository. Read this before
editing — several design choices here are deliberate and easy to "fix" wrongly.

## What this project is

A skill that reviews a document for **potential AI-generated content**. It does
two things, and the separation between them is the central design idea:

1. **Prepare** — `scripts/build_package.py` converts a document and assembles a
   portable *prompt-package folder* (`document.md`, `rules.md`, `prompt.md`,
   `output-spec.md`, `manifest.json`, `README.md`).
2. **Review** — an agent reads that package and produces `report.md`. All
   judgment lives here, driven by `prompt.md` + `output-spec.md`.

The output is an editing aid, **never** an authorship verdict. That framing is a
hard product constraint, not a stylistic preference (see Invariants).

## Mental model

> The script is deterministic plumbing. The agent is the judge.

Keep these on opposite sides of the line. The script must not score, classify, or
flag — it only converts and assembles. The agent must not be handed raw
lint-style hits to rubber-stamp — it weighs each candidate in context.

## Key files

| Path | Role | When editing, don't… |
|---|---|---|
| `SKILL.md` | Manifest + workflow. The `description` frontmatter is the **trigger** mechanism. | …casually reword the description; it controls when the skill fires. |
| `scripts/build_package.py` | Convert (liteparse or passthrough) + anchor lines + copy assets + write manifest. Also fills `{LANG_NAME}` into `prompt.md` from the `-l` flag's catalog `name`. | …add any detection/scoring logic here. Prep only — the `-l`→`{LANG_NAME}` fill is a file-selection/substitution echo of a choice already made, not new judgment. |
| `scripts/gen_rule_catalog.py` | Regenerate the catalog from upstream vale-ai-tells YAML. Maintenance only. | …hand-edit `ai-tells.md` instead; regenerate so it stays faithful. |
| `assets/rules/ai-tells.md` | The 60-criterion catalog used every run (generated artifact). | …treat as hand-authored; it's derived. |
| `assets/rules/es-tells.md` | Spanish tell catalog, selected with `-l es`. **Exception to invariant 4**: hand-authored, not generated — no upstream Spanish source exists. | …regenerate it (there's no generator); edit it directly and keep its provenance header + `ES-TELLS-NOTICE.txt`. |
| `assets/templates/prompt.md` | The standardized review instruction, with a `{LANG_NAME}` placeholder telling the agent what language to write `report.md` in. | …weaken the false-positive / calibration guidance; don't hardcode a language — keep it as the `{LANG_NAME}` placeholder. |
| `assets/templates/output-spec.md` | Required report shape. | …drop the Limitations section. |
| `references/pipeline.md` | Internals, deps, extension points. | |

## Commands

```bash
# Build a package from any supported input
python3 scripts/build_package.py INPUT -o OUTPUT_DIR

# Smoke-test without liteparse (passthrough path)
printf '# Title\n\nIt is important to note that we delve into a rich tapestry.\n' > /tmp/t.md
python3 scripts/build_package.py /tmp/t.md -o /tmp/t-pkg && ls /tmp/t-pkg

# Regenerate the catalog (needs a vale-ai-tells checkout + pyyaml)
python3 scripts/gen_rule_catalog.py /path/to/vale-ai-tells/styles/ai-tells \
    -o assets/rules/ai-tells.md
```

There is no automated test suite yet. The cheapest sanity check is the
passthrough smoke test above plus eyeballing the generated package.

## Design decisions & rationale

- **Prompt-package, not a monolithic call.** A self-contained folder runs in any
  harness and gives provenance and reproducibility. Don't collapse it into a
  single hardcoded prompt string.
- **No Vale, by choice.** The criteria originate as Vale rules, but a literal
  linter can't distinguish a deliberate em-dash from a tell, can't weigh
  clustering, and floods false positives. The agent does. Trade-off accepted:
  matching is no longer perfectly deterministic. Do **not** reintroduce a linter
  pass unless the product goal changes.
- **`ai-tells` (prose) catalog, not `ai-tells-commits`.** Upstream also ships a
  commit-message pack and an experimental statistical pack. This project targets
  prose. Adding the experimental metrics as an *optional* second catalog is a
  reasonable extension; swapping in the commits pack is not, unless reviewing
  commit messages.
- **liteparse text format is the default.** Its plain-text output has a stable
  shape across versions, so anchoring is reliable. liteparse can also emit JSON
  with bounding boxes; that path is unverified here and left as an extension.
- **Spanish catalog is a scoped exception, not a precedent.** `es-tells.md` is
  hand-authored because upstream vale-ai-tells ships no Spanish pack, so
  `gen_rule_catalog.py` has nothing to regenerate from. This does **not** license
  hand-editing `ai-tells.md` (which stays generated, invariant 4). The `-l` flag
  that selects between catalogs is plumbing — file selection only, no detection
  or scoring — and must stay that way if more languages are added.
- **Report language follows the document, automatically.** The `-l` flag picked
  in phase 1 (Prepare) now also decides the language of `report.md` in phase 2
  (Review): `build_package.py` fills `{LANG_NAME}` (e.g. "English"/"Spanish")
  into `prompt.md` from `CATALOGS[lang]["name"]`, and the agent writes the whole
  report in that language (quoted extracts stay verbatim in the source language).
  There is no separate "what language should the report be in" question anymore
  — `SKILL.md` reflects this. This is still just plumbing: the script echoes a
  choice the user already made via `-l`, it does not detect or infer language.
- **Heuristic framing is load-bearing.** Every layer (catalog header, prompt,
  output spec, README) repeats that these are candidates, not proof, and that the
  tool over-flags non-native writing. This is intentional redundancy.

## Invariants — preserve these when editing

1. The script never judges. Detection/calibration stays in the agent layer.
2. Output is framed as candidates + improvement suggestions, never a verdict or
   an unjustified percentage. Keep the non-native-writer false-positive caution.
3. Attribution stays intact: vale-ai-tells is **MIT** (© Tony Burns) — ship
   `VALE-AI-TELLS-LICENSE.txt` and keep the source note in the catalog header.
   (The upstream README badge says Apache; the actual LICENSE is MIT. Trust the
   LICENSE file.)
4. `ai-tells.md` is generated. Change it via `gen_rule_catalog.py`, not by hand.
   (Sole exception: `es-tells.md` is hand-authored — there is no upstream Spanish
   source to generate from. This exception does not extend to `ai-tells.md`.)
5. Don't add network calls, telemetry, or browser storage anywhere.

## Extension points

- **Page/coordinate locations.** Extend `convert()` in `build_package.py` to call
  `lit parse --format json`, map blocks to pages, and emit `[p<n>]` + coordinates
  instead of (or alongside) line numbers. Validate against real liteparse JSON
  output first — its schema isn't pinned in this repo.
- **Optional experimental catalog.** Generate a second `ai-tells-experimental.md`
  from upstream and let the package include it on request.
- **Inline vs. handoff.** The skill can run the review itself or only emit the
  folder for an external harness. Keep both modes working.

## Gotchas

- Some upstream YAML rules are multi-document (`---` mid-file); the parser takes
  the first doc with an `extends` key. Preserve that handling.
- ~half the rules are literal phrase lists, ~half are regex/structural patterns.
  The catalog renders the former as example triggers and the latter as described
  shapes — don't try to surface raw regex to the agent as if it were literal.
- liteparse needs LibreOffice (Office formats) and ImageMagick (images) at
  runtime; the script fails with a clear message if `lit` is missing.
