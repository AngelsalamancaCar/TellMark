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

### 2. Build the package
Run the bundled script. It converts the document with **liteparse** (or uses the
text directly for `.txt`/`.md`) and assembles the package folder:

```bash
python3 scripts/build_package.py "<input-file>" -o "<name>-review-package"
```

The package contains `document.md` (line-anchored text), `rules.md` (the tell
criteria), `prompt.md` (the standardized instruction), `output-spec.md` (the
required report format), `manifest.json`, and a `README.md`. This folder is
portable: it has everything any agent harness needs, with no extra context.

### 3. Run the review
Read `prompt.md`, `rules.md`, `document.md`, and `output-spec.md` from the
package, then **perform the review yourself** following `prompt.md`'s method and
producing the report exactly as `output-spec.md` specifies. Save it as
`report.md` inside the package folder.

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

### 4. Deliver
Present the `report.md` and the package folder to the user. Lead with the honest
overall assessment, then findings, then the concrete rewrite recommendations.

## What's bundled

- `scripts/build_package.py` — converts + assembles the package.
- `scripts/gen_rule_catalog.py` — regenerates `rules.md` from upstream
  vale-ai-tells (maintenance only; the catalog is already built).
- `assets/rules/ai-tells.md` — the 60-criterion tell catalog used in every run.
- `assets/templates/` — the `prompt.md`, `output-spec.md`, and package `README`.
- `references/pipeline.md` — how the pipeline works, dependencies, and limits.

## Important framing

The tell catalog is adapted from the open-source **vale-ai-tells** project (MIT,
© Tony Burns). Its own guidance: these patterns target technical documentation
and are *less* meaningful in creative or marketing writing, and the goal is
cleaning up prose — not adjudicating who wrote it. Report accordingly: candidates
and suggestions, not accusations.
