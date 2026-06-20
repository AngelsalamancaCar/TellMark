# Plan: Spanish-language support for ai-content-review

## Repo reality (read first — earlier draft of this plan had the paths wrong)

The skill does **not** live at the repo root. It lives in `ai-content-review/`:

```
ai-content-review/
  SKILL.md                       # live manifest + workflow
  scripts/build_package.py       # the prep script (copies catalog at :138)
  scripts/gen_rule_catalog.py    # catalog regenerator (English only)
  assets/rules/ai-tells.md       # the live English catalog
  assets/rules/VALE-AI-TELLS-LICENSE.txt
  assets/templates/{prompt,output-spec,package-readme}.md
  references/pipeline.md
data/source/      data/processed/   # I/O, at repo ROOT (build_package resolves REPO_ROOT = SKILL_ROOT.parent)
```

There are **stale duplicate copies at the repo root** (`./SKILL.md`, `./ai-tells.md`).
`build_package.py` sets `ASSETS = ai-content-review/assets`, so only the nested
copies are live. Two consequences for this work:

1. **All edits go to the `ai-content-review/` copies**, never the root duplicates.
   Every path below is written relative to repo root and includes the prefix.
2. **Pre-existing bug to flag (not caused by this plan):** the "ask report
   language" step in the working tree was added to the *root* `SKILL.md` only;
   the live `ai-content-review/SKILL.md` doesn't have it. Whoever applies step 4
   below should port that step into the live file too (and ideally delete the
   root duplicates, or fold them into one source of truth) so the document-language
   and report-language steps both land in the file the skill actually reads.

Note: `CLAUDE.md` describes paths *as if* the skill root were the repo root
(`SKILL.md`, `scripts/build_package.py`). That's the skill-author's-eye view; on
disk everything is under `ai-content-review/`. Don't "fix" CLAUDE.md's paths as
part of this work — just know the mapping.

## Problem

`ai-content-review` ships one tell catalog, `ai-content-review/assets/rules/ai-tells.md`,
generated from upstream **vale-ai-tells** (English-only: literal phrases like
"delve", "It's important to note that", "rich tapestry"). Run against a Spanish
document, almost none of these triggers can fire — not because the prose is
clean, but because the catalog doesn't speak the language. Confirmed upstream has
no Spanish or multi-language pack (`tbhb/vale-ai-tells` styles/ has only
`ai-tells`, `ai-tells-commits`, `ai-tells-experimental`, all English). Nothing to
borrow — a Spanish catalog has to be authored from scratch.

## Scope decision

Build a **parallel catalog**, `ai-content-review/assets/rules/es-tells.md`,
selected explicitly per run — not a translation that replaces `ai-tells.md`, and
not auto-detected by default. Rationale:

- Spanish AI-tells are not a 1:1 translation of the English set (different hedge
  phrasing, different overused vocabulary, different rhetorical clichés). Needs
  independent authoring, not `s/delve/profundizar/`.
- Keeps the English path untouched and the new path additive — low risk to the
  existing, working skill.
- Auto language-detection is deferred (see Open questions). V1 ships an explicit
  flag so catalog selection stays a deterministic, inspectable choice.

This is an **exception to invariant 4 in `CLAUDE.md`** ("catalog is generated,
never hand-authored"), because there's no upstream Spanish YAML for
`gen_rule_catalog.py` to regenerate from. The exception must be stated loudly in
the file header and in `CLAUDE.md`, not quietly introduced.

---

## DRAFT: `es-tells.md` content

This is the actual phrase/pattern inventory to ship, mirroring the eight
categories in `ai-tells.md` so `prompt.md` / `output-spec.md` keep working
unmodified. Drawn from observed Spanish output of ChatGPT/Claude/Gemini — the
same empirical grounding vale-ai-tells used, done independently. **All entries
are candidates, not proof**; many are legitimate in formal, academic, or
translated registers. The catalog over-flags non-native and formal Spanish — the
agent judges in context. Regional variation (Spain vs. Latin America) is a known
gap, flagged in the header, not solved in v1.

Severity convention copied from `ai-tells.md`: literal phrase lists → `error`,
softer/structural shapes → `warning`. Format per entry: `### RuleName _(severity)_`,
`*Tell:*`, then `*Triggers:*` (literal) or `*Pattern-based:*` (structural).

### Vocabulary & word choice

**OverusedVocabularyEs** _(error)_ — overused AI vocabulary; replace with a
plainer or more specific word:
profundizar, profundicemos, ahondar, desentrañar, panorama, paisaje, sinergia,
sinergias, vanguardia, holístico, robusto, integral, fundamental, crucial,
clave, esencial, primordial, imprescindible, vital, innovador, revolucionario,
transformador, disruptivo, multifacético, polifacético, entramado, matiz,
matices, matizado, catalizador, abrumador, meticuloso, meticulosamente, sinnúmero.

**AICompoundPhrasesEs** _(error)_ — clichéd fixed phrases; rewrite with concrete
specifics:
"rico entramado", "rico tapiz", "un rico tapiz de", "juega un papel fundamental",
"juega un papel crucial", "juega un papel clave", "desempeña un papel crucial",
"piedra angular de", "punto de inflexión", "un antes y un después", "a la
vanguardia de", "allanar el camino", "allana el camino", "sienta las bases", "un
testimonio de", "da testimonio de", "arma de doble filo", "la punta del iceberg",
"no exento de desafíos", "no está exento de retos".

### Hedging & throat-clearing

**HedgingPhrasesEs** _(error)_ — throat-clearing; delete and state the point:
"Cabe destacar que", "Cabe señalar que", "Cabe mencionar que", "Cabe resaltar
que", "Cabe subrayar que", "Cabe recordar que", "Cabe preguntarse", "Es
importante destacar que", "Es importante señalar que", "Es importante mencionar
que", "Es importante recordar que", "Es importante tener en cuenta que", "Es
importante recalcar que", "Es fundamental señalar", "Es fundamental comprender",
"Es esencial entender", "Es crucial señalar", "Vale la pena mencionar", "Vale la
pena destacar", "Vale la pena señalar", "Conviene señalar", "Conviene destacar",
"Conviene recordar", "Hay que destacar", "Hay que tener en cuenta", "No hay que
olvidar que", "No debemos olvidar que", "Dicho esto", "Dicho lo anterior",
"Aclarado esto", "En este sentido", "En este contexto", "En esta línea", "Por
así decirlo", "En cierto sentido", "En cierta medida", "Hasta cierto punto", "A
grandes rasgos", "En términos generales", "En líneas generales".

**VagueAttributionsEs** _(error)_ — name the source or drop the claim:
"los expertos afirman", "los expertos sugieren", "los expertos coinciden", "los
expertos advierten", "los expertos recomiendan", "según los expertos", "muchos
expertos", "algunos expertos", "los estudios demuestran", "los estudios
sugieren", "los estudios indican", "diversos estudios", "numerosos estudios",
"las investigaciones sugieren", "la investigación demuestra", "los especialistas
señalan", "diversos analistas", "algunos observadores".

**FalseBalanceEs** _(warning)_ — take a position or cut the hedge:
"ambos lados del argumento", "ambas posturas tienen méritos", "cada perspectiva
tiene su valor", "es importante considerar todas las perspectivas", "un enfoque
equilibrado", "encontrar un equilibrio", "la respuesta no es sencilla", "no hay
una respuesta sencilla", "es un tema complejo", "depende de varios factores",
"depende de muchos factores", "varía según el contexto", "caso por caso".

### Promotional / marketing register

**PromotionalPufferyEs** _(error)_ — neutral, specific language instead:
"enclavado en", "ubicado en el corazón de", "en el corazón de", "en pleno
corazón de", "rica historia", "rico patrimonio cultural", "rica y diversa",
"comunidad vibrante", "cultura vibrante", "vibrante ecosistema", "belleza
natural", "un referente en", "un faro de", "un emblema de", "una joya escondida",
"un claro ejemplo", "reconocido por su", "célebre por su", "ampliamente
reconocido como", "se ha consolidado como", "se ha posicionado como", "se ha
convertido en un referente", "sigue evolucionando", "sigue creciendo", "dejó una
huella imborrable", "dejando una huella imborrable", "un legado duradero", "un
legado perdurable".

**MarketingHeadingsEs** _(error)_ — strip puffery, name the topic:
"La guía definitiva", "Todo lo que necesitas saber", "Domina", "Dominando", "El
poder de", "La magia de", "El futuro de", "El arte de", "La ciencia de", "Por
qué elegir", "Descubre el secreto".

**UrgencyInflationEs** _(error)_ — delete or show stakes concretely:
"no se puede subestimar", "no puede subestimarse", "no se puede exagerar", "más
importante que nunca", "más relevante que nunca", "más necesario que nunca", "más
crucial que nunca", "nunca ha sido tan importante", "hoy más que nunca", "en un
mundo cada vez más complejo", "en un mundo cada vez más digital", "en un mundo
cada vez más interconectado", "en la era digital", "en un punto de inflexión",
"en una encrucijada", "en un momento decisivo".

**AbsoluteAssertionsEs** _(warning)_ — verify or soften:
"la única forma de", "la única manera de", "la única solución", "el único
camino", "lo más importante es", "por encima de todo", "no cabe duda de que",
"sin lugar a dudas", "que no quepa duda".

### Rhetorical structure & cadence

**ContrastiveFormulasEs** _(error)_ — *Pattern-based.* The Spanish
contrastive-tricolon / negation formula; state the positive directly:
"no se trata solo de… sino de…", "no solo… sino también…", "no es (solamente)
una cuestión de… sino de…", "no es X, es Y", "más que X, es Y".

**VerbTricolonEs** _(warning)_ — *Pattern-based.* Three parallel verbs/nouns in
series ("analiza, optimiza y transforma"); vary the count.

**StackedAnaphoraEs** _(warning)_ — *Pattern-based.* Repeated identical sentence
openings across consecutive sentences ("Cada… Cada… Cada…").

**RhetoricalDevicesEs** _(error)_ — colon-label flourishes; rephrase plainly:
"La clave:", "El problema:", "La pregunta:", "El resultado:", "La conclusión:",
"La lección:", "El punto:", "La prueba:", "Pregúntate:".

**RhetoricalSelfAnswerEs** _(warning)_ — *Pattern-based.* Posing and immediately
answering one's own question: "¿La razón? …", "¿El motivo? …", "¿El resultado?
…", "¿Por qué? Porque…".

**NarrativePivotsEs** _(error)_ — state the point directly:
"algo cambió", "todo cambió", "y entonces todo cambió", "eso lo cambió todo",
"esto lo cambia todo", "marcó un antes y un después", "fue un punto de
inflexión", "y ahí lo entendí", "y entonces me di cuenta", "todo cobró sentido",
"cambió las reglas del juego".

**ParticipialPaddingEs** _(error)_ — gerund padding; delete or make concrete:
"destacando su importancia", "subrayando su relevancia", "resaltando la
importancia", "reflejando una tendencia", "demostrando su compromiso",
"consolidando su posición", "reforzando su papel", "poniendo de manifiesto",
"dejando patente", "fomentando un sentido de", "garantizando una experiencia
fluida".

**DespiteChallengesEs** _(error)_ — engage substantively or remove the hedge:
"a pesar de sus desafíos", "a pesar de estos retos", "a pesar de las
limitaciones", "pese a los obstáculos", "si bien existen desafíos", "aunque
persisten retos".

**OrganicConsequenceEs** _(error)_ — say it was designed that way:
"surge de forma natural", "surge de manera natural", "emerge de forma orgánica",
"se desprende naturalmente", "es una consecuencia natural", "fluye de manera
natural", "se deriva naturalmente".

### Filler, padding & metacommentary

**FillerPhrasesEs** _(error)_ — delete; adds no meaning:
"una amplia gama de", "una amplia variedad de", "un sinfín de", "una gran
cantidad de", "una multitud de", "un sinnúmero de", "innumerables", "con el fin
de", "con el objetivo de", "con el propósito de", "de cara a", "a fin de",
"debido al hecho de que", "dado el hecho de que", "a pesar del hecho de que", "el
hecho de que", "es evidente que", "está claro que", "resulta evidente que".

**MetacommentaryEs** _(error)_ — delete or replace with substance:
"Esto importa porque", "Esto es importante porque", "Esta distinción es
importante", "Permíteme explicar", "Déjame explicarte", "Vamos a analizar",
"Analicemos", "Exploremos", "Veamos", "Profundicemos en", "La clave aquí es", "El
punto aquí es", "La idea aquí es", "En esencia", "En el fondo", "Piénsalo como",
"Aquí es donde se pone interesante".

**RestatementMarkersEs** _(error)_ — trust the original phrasing:
"En otras palabras", "Dicho de otro modo", "Dicho de otra manera", "Es decir",
"O sea", "Para ser más precisos", "Más concretamente", "Para decirlo claramente",
"En pocas palabras", "Dicho de forma sencilla".

**SequencingMarkersEs** _(warning)_ — use natural transitions or a real list:
"En primer lugar", "En segundo lugar", "En tercer lugar", "Por último", "Por una
parte", "Por otra parte", "Primeramente", "Seguidamente", "Finalmente".

**ConclusionMarkersEs** _(error)_ — delete and end on the final point:
"En conclusión", "En resumen", "En síntesis", "Para concluir", "Para finalizar",
"En definitiva", "En última instancia", "A fin de cuentas", "Al fin y al cabo",
"En suma", "Resumiendo", "Para cerrar".

**FormalTransitionsEs** _(warning)_ — prefer a simpler connector (y, pero, así
que):
"Además", "Asimismo", "Por consiguiente", "En consecuencia", "Por lo tanto", "Por
ende", "No obstante", "Por el contrario", "En contraste", "De igual manera", "Del
mismo modo", "Igualmente", "Es más", "De hecho", "En particular", "Concretamente",
"Notablemente", "Fundamentalmente", "Como resultado".

**FormalRegisterEs** _(warning)_ — plainer everyday word:
"utilizar" (→ usar), "implementar", "facilitar", "optimizar", "maximizar",
"minimizar", "priorizar", "potenciar", "fomentar", "propiciar", "conlleva",
"posibilitar", "materializar", "evidenciar", "visibilizar", "dinamizar".

**OpeningClichesEs** _(error)_ — start with the actual point:
"En el mundo actual", "En la era digital", "En un mundo cada vez más", "Hoy en
día", "En los últimos años", "A lo largo de la historia", "Desde tiempos
inmemoriales", "Desde los albores de", "En el vertiginoso mundo de", "En el
cambiante panorama de", "Imagina un mundo donde", "¿Alguna vez te has
preguntado", "Cuando se trata de", "En el ámbito de", "En el campo de".

**ClosingPleasantriesEs** _(error)_ — end with actual content:
"Espero que esto te ayude", "Espero que esto sea útil", "Espero que te sirva",
"Espero haber aclarado", "No dudes en preguntar", "No dudes en contactar", "Si
tienes alguna pregunta, no dudes", "Quedo a tu disposición", "Estoy aquí para
ayudarte", "Si necesitas algo más, házmelo saber".

### Headings

**WrapUpHeadingsEs** _(error)_ — AI-style wrap-up headers; delete or rename to
the topic:
"En resumen", "Conclusión", "Conclusiones", "Reflexiones finales",
"Consideraciones finales", "Pensamientos finales", "Para concluir", "En
definitiva", "El panorama general", "Para llevar".

**ExplainerHeadingsEs** _(warning)_ — name what you're explaining instead:
"Lo que aprenderás", "Lo que veremos", "Qué esperar", "Una mirada más cercana",
"Por qué importa", "Por qué es importante", "Cómo funciona", "Bajo el capó",
"Desmitificando".

### Punctuation

**EmDashUsageEs** _(warning — note higher false-positive risk)_ — em/en-dash
detected: "—", "–", "--". **Caveat in header:** Spanish uses the raya (—)
legitimately for dialogue and parenthetical asides; this fires far more false
positives in Spanish than English. Downgraded to `warning` and the agent must be
extra conservative. Inverted marks (¿ ¡) are normal Spanish, never a tell.

### Tone & self-reference

**SelfReferenceEs** _(error)_ — rewrite to work without the cross-reference:
"como se mencionó anteriormente", "como se mencionó antes", "como ya se ha
mencionado", "como hemos visto", "como vimos anteriormente", "como veremos",
"como se señaló", "como se indicó previamente", "tal como se mencionó",
"recordemos que", "como ya dijimos".

**AIDisclaimerEs** _(error)_ — leaked model disclaimers (rare, but a strong tell
in copy-pasted/translated text):
"Como modelo de lenguaje", "Como inteligencia artificial", "Como IA", "No tengo
acceso a", "Mi conocimiento se limita a", "fecha de corte".

**SycophancyMarkersEs** _(error)_ — delete; sounds robotic:
"Excelente pregunta", "Gran pregunta", "Qué buena pregunta", "Me alegra que
preguntes", "Estaré encantado de ayudarte", "Con mucho gusto", "Por supuesto",
"Tienes toda la razón", "Es un excelente punto", "Una idea fantástica".

---

## Work items

### 1. Author `ai-content-review/assets/rules/es-tells.md`

Render the draft above in the exact shape of `ai-tells.md`: a header block, then
`## Category` sections, then `### RuleName _(severity: …)_` / `*Tell:*` /
`*Triggers:*` entries. The header must state explicitly:

- **Hand-authored**, not generated by `gen_rule_catalog.py` — no upstream Spanish
  source exists. (This is the invariant-4 exception.)
- Category taxonomy is **inspired by** vale-ai-tells (credit it), but the Spanish
  phrase content is **original** — so `VALE-AI-TELLS-LICENSE.txt` (which covers
  `ai-tells.md`) does **not** automatically cover this file's content. Settle the
  new content's license (see Open questions) before shipping.
- Same heuristic-framing caveats as the English catalog: candidates not proof;
  over-flags formal/academic/translated Spanish; judge in context.
- **Regional-variation limitation** stated outright (Spain vs. Latin America;
  v1 is a general/neutral set).
- The em-dash caveat from the Punctuation section above.

### 2. Wire catalog selection into `ai-content-review/scripts/build_package.py`

Current copy line:

```python
shutil.copy(ASSETS / "rules" / "ai-tells.md", out_dir / "rules.md")
```
— `ai-content-review/scripts/build_package.py:138`

Changes:

- Add `-l/--lang {en,es}` arg, default `en`. Map: `{"en": "ai-tells.md", "es":
  "es-tells.md"}`. Copy the selected file to `out_dir / "rules.md"` — the
  in-package filename stays `rules.md` either way, so `prompt.md` /
  `output-spec.md` need no change.
- `manifest.json` (built at `build_package.py:149`): add `"catalog":
  "es-tells.md"` and make `rules_source` reflect the Spanish provenance line
  (not the vale-ai-tells MIT URL) when `-l es`. Currently `rules_source` is
  hardcoded at `:156`.
- License copy at `build_package.py:139` (`VALE-AI-TELLS-LICENSE.txt`): keep it
  for the structure-inspiration credit, and additionally copy whatever new notice
  step 1's licensing decision produces when `-l es`.
- Keep `-l` purely file selection — no scoring, no detection. Same kind of
  static-asset choice `convert()` already makes by file extension. Stays inside
  the "script never judges" invariant.

### 3. Update `ai-content-review/SKILL.md` (the LIVE one — see Repo reality)

- First port the missing "ask report language" step from the root duplicate into
  the live file (pre-existing bug noted above), so both language questions live
  in one place.
- Step "Locate the document" gains: ask the user (or infer if obvious) the
  document's language; pass `-l es` to the build command when Spanish.
- Make the **two distinct language questions** explicit so a future editor doesn't
  collapse them: *document language* picks the **catalog** (`-l`); *report
  language* picks the **output** (`report.md`). A Spanish document can still get
  an English report, or vice versa.
- "What's bundled" mentions `es-tells.md` alongside `ai-tells.md`.
- "Important framing" notes the Spanish catalog's different provenance
  (hand-authored, regional-variation gap, em-dash caveat).

### 4. Update `CLAUDE.md`

- Add a Key Files row for `assets/rules/es-tells.md`, marked as the **exception**
  to "catalog is generated" — maintained by hand, not `gen_rule_catalog.py`,
  because no upstream source exists.
- Under Design decisions: Spanish catalog is a deliberate, scoped exception, not
  a precedent for hand-editing `ai-tells.md` itself.
- Invariants/Gotchas: `-l` is plumbing, not judgment — keep it that way if
  extended to more languages.

### 5. Sanity checks

No automated suite exists. Add a Spanish smoke test beside the English one.
Invoke the **nested** script and let it auto-route output to `data/processed/`:

```bash
printf '# Título\n\nCabe destacar que esto juega un papel fundamental en el panorama actual.\n' > /tmp/t-es.md
python3 ai-content-review/scripts/build_package.py /tmp/t-es.md -o /tmp/t-es-pkg -l es
ls /tmp/t-es-pkg                                      # rules.md present
grep -qi "cabe destacar" /tmp/t-es-pkg/rules.md \
  || echo "MISSING: catalog has no match for a known Spanish tell"
grep -q '"catalog": "es-tells.md"' /tmp/t-es-pkg/manifest.json \
  || echo "MISSING: manifest did not record the Spanish catalog"
```

Then build a package with `-l es` against a real Spanish AI-drafted sample, run
the review by hand, and confirm findings cite real Spanish-language tells rather
than silently falling back to an empty/English list.

## Sequencing

1. Author `es-tells.md` from the draft above (step 1), incl. licensing/provenance
   header. The only step with real content judgment.
2. Code change to `build_package.py` (step 2) — small, isolated.
3. Doc updates to live `SKILL.md` + `CLAUDE.md` (steps 3–4), including the
   root-duplicate cleanup / port.
4. Smoke test (step 5).

## Open questions (decide before/while building)

- **Licensing of new Spanish content.** No repo-wide `LICENSE` file exists. Decide
  what covers original `es-tells.md` phrase content before shipping — can't
  silently inherit the vale-ai-tells MIT notice for text it never wrote.
- **Root vs. nested duplicates.** Resolve the stale `./SKILL.md` and `./ai-tells.md`
  copies as part of this work or separately — but the report-language bug shows
  the duplication is already causing edits to miss the live files. Recommend
  deleting the root copies (or making them symlinks) so there's one source of
  truth before adding a second catalog into the mix.
- **Regional variation.** Spain vs. Latin American Spanish differ in register and
  stock phrases. V1 ships a neutral set and documents the gap; decide later
  whether regional sub-sections are needed.
- **Auto language detection.** Deferred (manual `-l` only). If wanted later, the
  seam is `convert()` in `build_package.py` — a light heuristic (stopword
  frequency, or `langdetect` as an extra dep) could pre-select `-l` unless
  overridden. Phase-2.
- **Mixed-language / code-switched documents.** Out of scope — would need both
  catalogs loaded at once, which `rules.md`'s single-file convention doesn't
  support. Flag as a known limitation.
