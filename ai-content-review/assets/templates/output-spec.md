# Output specification — AI-content review report

Produce **one Markdown document** with these sections, in this order.

## 1. Overall assessment

Two to four sentences. State the overall impression in calibrated terms (e.g.,
"low / moderate / high concentration of AI-associated patterns") and say what
drives it. Include a one-line caveat that these are heuristic signals, not proof
of authorship. Do **not** give a single AI/human verdict or an unjustified
percentage.

## 2. Signal summary

A short table aggregating what was found:

| Category | Distinct tells | Total hits | Notable concentration |
|---|---|---|---|
| Vocabulary & word choice | … | … | e.g. "intro paragraph" |
| Hedging & throat-clearing | … | … | … |
| … | | | |

Only include rows with at least one genuine (post-judgment) hit.

## 3. Findings

One entry per genuine flagged passage, ordered by location. Use this shape:

> **[L<line>]** — *<CriterionName>* (severity: <level>)
> Extract: "<the exact flagged text>"
> Why: <one sentence on why this reads as a tell **here**, in context>

Group tightly-clustered hits under a single location note when that reads better.

## 4. Recommendations

For each finding or cluster, give a concrete, specific improvement — ideally a
suggested rewrite, not just "remove this." Example:

> **[L12] Hedging** — "It's important to note that the API is fast."
> → "The API responds in under 50 ms." (Drop the throat-clearing; state the fact.)

Close with 2-3 higher-level notes on the document's overall voice if a pattern
recurs (e.g., "Nearly every list is exactly three items — vary the cadence.").

## 5. Limitations

Two to three sentences: these tells are heuristics with real false-positive
rates; they over-flag formal, translated, and non-native writing; intentional
style can trip them; and absence of tells does not certify human authorship. The
report is an editing aid and a prompt for human judgment, not an adjudication.
