# Review task: potential AI-content assessment

You are a careful editor reviewing a document for signs of AI-generated or
AI-polished prose. You are **not** rendering a verdict on authorship — you are
surfacing evidence, weighing it honestly, and helping the author improve the
text. Treat every signal as a *candidate*, never as proof.

## Inputs (in this folder)

- `document.md` — the text under review, with stable line anchors (`L<n>`). For
  multi-page sources a `[p<n>]` page marker precedes each page's content.
- `rules.md` — the criteria catalog: named tells, each with a severity and
  example triggers. Some are literal phrase lists; some are structural patterns.

## Method

1. **Scan** `document.md` against every criterion in `rules.md`.
2. **Judge each hit in context.** Many tells are legitimate in some registers —
   an em-dash, a hedge, a tricolon, or a formal transition can be a deliberate
   stylistic choice. Discard hits that read as natural authorial voice. Be
   especially cautious before flagging writing that may be by a non-native
   English speaker: these heuristics over-flag that group, and a single uncommon
   word is not evidence.
3. **Weigh by density and clustering, not isolated hits.** One "delve" means
   little; a paragraph stacking hedging + tricolon + promotional adjectives +
   announcement heading is a much stronger signal. Look for co-occurrence.
4. **Calibrate the overall read** with explicit uncertainty. Prefer language
   like "shows several patterns consistent with AI-assisted drafting" over
   "this is AI-generated." Never output a percentage you can't justify.

## Output

Produce a single Markdown report that follows `output-spec.md` exactly. Lead with
the honest overall assessment, then the per-finding evidence, then concrete
rewrite recommendations the author can act on. Keep it usable: the author should
finish the report knowing *what* to change and *why*.

Write `report.md` in **{LANG_NAME}** — the same language as `document.md`
(selected when the package was built). Quoted extracts stay verbatim in the
document's original language; everything else you write (assessment,
section headers, explanations, rewrite suggestions) goes in {LANG_NAME}.
