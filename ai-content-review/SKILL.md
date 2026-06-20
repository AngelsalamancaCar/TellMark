---
name: ai-content-review
description: >
  Prepare and run a "potential AI content" review of a document. Use this skill
  whenever the user wants to check, detect, flag, or assess whether text reads as
  AI-generated or AI-polished — including phrasings like "does this sound like
  AI", "check this for AI tells", "review this draft for AI writing", "how
  human does this read", or asks for feedback on making writing sound less like
  AI. Works on PDFs, Word/PowerPoint files, images, or plain text. It converts
  the document, assembles a portable prompt-package folder (text + tell criteria
  + standardized prompt + output spec), and produces a report of flagged
  passages with concrete rewrite recommendations. Trigger it even when the user
  only uploads a document and asks "is this AI?" without naming a process.
---

# AI-content review

This skill turns any document into a self-contained **review package** and then
runs a standardized review against it. It surfaces *candidate* AI tells with
locations and improvement suggestions — it is an editing aid, **not** an
authorship verdict. Detection is heuristic and over-flags formal, translated,
and non-native writing, so always keep human judgment in the loop and frame
results with calibrated uncertainty.

## When this triggers

The user has a piece of writing and wants to know whether it reads as AI-made,
or wants help making it read less so. The input may be an uploaded file or text
pasted into the conversation.

## Workflow

### 1. Locate the document
Find the file the user wants reviewed (typically under `/mnt/user-data/uploads/`).
If they pasted raw text instead, save it to a `.md` file first so the script can
process it.

Also determine the **document's language** — ask the user, or infer it if the
text makes it obvious. This picks the *tell catalog* (English documents use the
default `ai-tells.md`; Spanish documents use the hand-authored `es-tells.md` via
`-l es`) **and** the language `report.md` will be written in — the two now move
together, see step 3.

### 2. Build the package
Run the bundled script. It converts the document with **liteparse** (or uses the
text directly for `.txt`/`.md`) and assembles the package folder. Add `-l es` for
a Spanish document so the Spanish catalog is bundled as `rules.md`:

```bash
python3 scripts/build_package.py "<input-file>" -o "<name>-review-package"        # English (default)
python3 scripts/build_package.py "<input-file>" -o "<name>-review-package" -l es  # Spanish
```

The package contains `document.md` (line-anchored text), `rules.md` (the tell
criteria), `prompt.md` (the standardized instruction), `output-spec.md` (the
required report format), `manifest.json`, and a `README.md`. This folder is
portable: it has everything any agent harness needs, with no extra context.

### 3. Report language is decided
`report.md` is written in the **same language as the document** — whichever one
was picked in step 1 (`-l` flag). `build_package.py` bakes this into `prompt.md`
(the `{LANG_NAME}` placeholder, filled with "English" or "Spanish"), so there is
no separate question to ask the user here. Quoted extracts inside the report
stay verbatim in the document's original language regardless.

### 4. Run the review
Read `prompt.md`, `rules.md`, `document.md`, and `output-spec.md` from the
package, then **perform the review yourself** following `prompt.md`'s method and
producing the report exactly as `output-spec.md` specifies, written in the
language `prompt.md` names (step 3). Save it as `report.md` inside the package
folder.

The core of the method (full detail in `prompt.md`):
- Scan the document against every criterion in `rules.md`.
- Judge each hit *in context* — discard ones that read as natural voice; be
  especially careful with writing that may be by a non-native English speaker.
- Weigh by density and clustering, not isolated hits.
- Calibrate the overall read with explicit uncertainty; never output a bare
  AI/human verdict or an unjustifiable percentage.

If the user instead wants to run the review in an external harness (e.g. Claude
CLI), point them at the package `README.md` — it has the exact command — rather
than running it here.

### 5. Deliver
Present the `report.md` and the package folder to the user. Lead with the honest
overall assessment, then findings, then the concrete rewrite recommendations.

## What's bundled

- `scripts/build_package.py` — converts + assembles the package.
- `scripts/gen_rule_catalog.py` — regenerates `rules.md` from upstream
  vale-ai-tells (maintenance only; the catalog is already built).
- `assets/rules/ai-tells.md` — the 60-criterion English tell catalog (default).
- `assets/rules/es-tells.md` — the hand-authored Spanish tell catalog, selected
  with `-l es`. See "Important framing" for its different provenance.
- `assets/templates/` — the `prompt.md`, `output-spec.md`, and package `README`.
- `references/pipeline.md` — how the pipeline works, dependencies, and limits.

## Important framing

The English tell catalog is adapted from the open-source **vale-ai-tells**
project (MIT, © Tony Burns). Its own guidance: these patterns target technical
documentation and are *less* meaningful in creative or marketing writing, and the
goal is cleaning up prose — not adjudicating who wrote it. Report accordingly:
candidates and suggestions, not accusations.

The Spanish catalog (`es-tells.md`) has **different provenance**: it is
hand-authored for this project (no upstream Spanish source exists), with a
taxonomy inspired by vale-ai-tells but original phrase content under its own
notice (`ES-TELLS-NOTICE.txt`). Extra caveats apply to it: it over-flags formal,
academic, and translated Spanish; it covers a general/neutral register and does
not yet distinguish Spain vs. Latin American variants; and the em-dash (raya)
signal is downgraded because the raya is standard Spanish punctuation. Same
framing holds — candidates, not verdicts.
