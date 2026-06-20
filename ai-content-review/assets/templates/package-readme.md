# {DOC_NAME} — AI-content review package

A self-contained prompt package. Hand the whole folder to any agent harness and
it has everything needed to produce the review — no extra context required.

## Contents

| File | Purpose |
|---|---|
| `prompt.md` | The standardized instruction the agent runs. |
| `document.md` | The source text, converted and line-anchored. |
| `rules.md` | The AI-tell criteria the agent judges against. |
| `output-spec.md` | The exact report format the agent must produce. |
| `manifest.json` | Provenance: source file, hashes, tool versions, timestamp. |

## Run it

**Claude CLI (headless):**

```bash
cd "{PACKAGE_DIR}"
claude -p "$(cat prompt.md)

=== rules.md ===
$(cat rules.md)

=== document.md ===
$(cat document.md)

=== output-spec.md ===
$(cat output-spec.md)" > report.md
```

**Any other harness:** feed `prompt.md` as the instruction and the other three
files as context, then capture the model's Markdown reply as `report.md`.

The output is feedback on *potential* AI content with concrete suggestions to
improve the text. It is an editing aid, not an authorship verdict.
