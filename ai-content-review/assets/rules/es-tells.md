# Catálogo de indicios de contenido AI en español (criterios de revisión)

> **Hand-authored, NOT generated.** Unlike `ai-tells.md` (which
> `gen_rule_catalog.py` regenerates from upstream vale-ai-tells YAML), this
> Spanish catalog has **no upstream source** and is maintained by direct editing.
> Its **category taxonomy is inspired by** vale-ai-tells by tbhb
> (https://github.com/tbhb/vale-ai-tells, MIT, © 2025-2026 Tony Burns), but the
> Spanish phrase content is **original to this project** and is not covered by
> `VALE-AI-TELLS-LICENSE.txt` — see `ES-TELLS-NOTICE.txt` for its license.
>
> These are *heuristic signals*, **not proof of authorship**. Many are perfectly
> normal in formal, academic, journalistic, or translated Spanish. The catalog
> **over-flags formal and non-native writing** — judge every candidate in context
> and weigh clustering, not isolated hits.
>
> **Known limitations.** (1) *Regional variation:* this is a general/neutral
> Spanish set; Spain and Latin American registers differ and some stock phrases
> are region-specific. (2) *Punctuation:* the raya (—) is standard in Spanish for
> dialogue and parenthetical asides, so the em-dash signal fires many more false
> positives than in English — it is downgraded to a warning and must be applied
> very conservatively. Inverted marks (¿ ¡) are normal Spanish, never a tell.

## How to use this catalog

Each entry is a **criterion**: a pattern that frequently signals AI-generated or
AI-polished Spanish prose. For each you get the tell, its default severity, and
example triggers. `*Triggers:*` lists are literal phrases; `*Pattern-based:*`
entries describe a structural shape rather than fixed words. Scan the document,
then decide case by case whether each hit is a genuine tell.

## Categories

- **Vocabulary & word choice** — OverusedVocabularyEs, AICompoundPhrasesEs
- **Hedging & throat-clearing** — HedgingPhrasesEs, VagueAttributionsEs, FalseBalanceEs
- **Promotional / marketing register** — PromotionalPufferyEs, MarketingHeadingsEs, UrgencyInflationEs, AbsoluteAssertionsEs
- **Rhetorical structure & cadence** — ContrastiveFormulasEs, VerbTricolonEs, StackedAnaphoraEs, RhetoricalDevicesEs, RhetoricalSelfAnswerEs, NarrativePivotsEs, ParticipialPaddingEs, DespiteChallengesEs, OrganicConsequenceEs
- **Filler, padding & metacommentary** — FillerPhrasesEs, MetacommentaryEs, RestatementMarkersEs, SequencingMarkersEs, ConclusionMarkersEs, FormalTransitionsEs, FormalRegisterEs, OpeningClichesEs, ClosingPleasantriesEs
- **Headings** — WrapUpHeadingsEs, ExplainerHeadingsEs
- **Punctuation** — EmDashUsageEs
- **Tone & self-reference** — SelfReferenceEs, AIDisclaimerEs, SycophancyMarkersEs


## Vocabulary & word choice

### OverusedVocabularyEs  _(severity: error)_
*Tell:* AI vocabulary: '%s'. Replace with a plainer or more specific word.
*Triggers:*
“profundizar”, “profundicemos”, “ahondar”, “desentrañar”, “panorama”, “paisaje”,
“sinergia”, “sinergias”, “vanguardia”, “holístico”, “robusto”, “integral”,
“fundamental”, “crucial”, “clave”, “esencial”, “primordial”, “imprescindible”,
“vital”, “innovador”, “revolucionario”, “transformador”, “disruptivo”,
“multifacético”, “polifacético”, “entramado”, “matiz”, “matices”, “matizado”,
“catalizador”, “abrumador”, “meticuloso”, “meticulosamente”, “sinnúmero”

### AICompoundPhrasesEs  _(severity: error)_
*Tell:* AI fingerprint: '%s'. Rewrite with concrete specifics instead of this clichéd phrase.
*Triggers:*
“rico entramado”, “rico tapiz”, “un rico tapiz de”, “juega un papel fundamental”,
“juega un papel crucial”, “juega un papel clave”, “desempeña un papel crucial”,
“piedra angular de”, “punto de inflexión”, “un antes y un después”, “a la
vanguardia de”, “allanar el camino”, “allana el camino”, “sienta las bases”, “un
testimonio de”, “da testimonio de”, “arma de doble filo”, “la punta del
iceberg”, “no exento de desafíos”, “no está exento de retos”


## Hedging & throat-clearing

### HedgingPhrasesEs  _(severity: error)_
*Tell:* AI hedge: '%s'. Delete this throat-clearing and state your point directly.
*Triggers:*
“Cabe destacar que”, “Cabe señalar que”, “Cabe mencionar que”, “Cabe resaltar
que”, “Cabe subrayar que”, “Cabe recordar que”, “Cabe preguntarse”, “Es
importante destacar que”, “Es importante señalar que”, “Es importante mencionar
que”, “Es importante recordar que”, “Es importante tener en cuenta que”, “Es
importante recalcar que”, “Es fundamental señalar”, “Es fundamental comprender”,
“Es esencial entender”, “Es crucial señalar”, “Vale la pena mencionar”, “Vale la
pena destacar”, “Vale la pena señalar”, “Conviene señalar”, “Conviene destacar”,
“Conviene recordar”, “Hay que destacar”, “Hay que tener en cuenta”, “No hay que
olvidar que”, “No debemos olvidar que”, “Dicho esto”, “Dicho lo anterior”,
“Aclarado esto”, “En este sentido”, “En este contexto”, “En esta línea”, “Por
así decirlo”, “En cierto sentido”, “En cierta medida”, “Hasta cierto punto”, “A
grandes rasgos”, “En términos generales”, “En líneas generales”

### VagueAttributionsEs  _(severity: error)_
*Tell:* AI vague attribution: '%s'. Name the specific source or delete the claim.
*Triggers:*
“los expertos afirman”, “los expertos sugieren”, “los expertos coinciden”, “los
expertos advierten”, “los expertos recomiendan”, “según los expertos”, “muchos
expertos”, “algunos expertos”, “los estudios demuestran”, “los estudios
sugieren”, “los estudios indican”, “diversos estudios”, “numerosos estudios”,
“las investigaciones sugieren”, “la investigación demuestra”, “los especialistas
señalan”, “diversos analistas”, “algunos observadores”

### FalseBalanceEs  _(severity: warning)_
*Tell:* AI evasion: '%s'. Take a clear position or remove the hedge.
*Triggers:*
“ambos lados del argumento”, “ambas posturas tienen méritos”, “cada perspectiva
tiene su valor”, “es importante considerar todas las perspectivas”, “un enfoque
equilibrado”, “encontrar un equilibrio”, “la respuesta no es sencilla”, “no hay
una respuesta sencilla”, “es un tema complejo”, “depende de varios factores”,
“depende de muchos factores”, “varía según el contexto”, “caso por caso”


## Promotional / marketing register

### PromotionalPufferyEs  _(severity: error)_
*Tell:* AI puffery: '%s'. Use neutral, specific language.
*Triggers:*
“enclavado en”, “ubicado en el corazón de”, “en el corazón de”, “en pleno
corazón de”, “rica historia”, “rico patrimonio cultural”, “rica y diversa”,
“comunidad vibrante”, “cultura vibrante”, “vibrante ecosistema”, “belleza
natural”, “un referente en”, “un faro de”, “un emblema de”, “una joya
escondida”, “un claro ejemplo”, “reconocido por su”, “célebre por su”,
“ampliamente reconocido como”, “se ha consolidado como”, “se ha posicionado
como”, “se ha convertido en un referente”, “sigue evolucionando”, “sigue
creciendo”, “dejó una huella imborrable”, “dejando una huella imborrable”, “un
legado duradero”, “un legado perdurable”

### MarketingHeadingsEs  _(severity: error)_
*Tell:* AI marketing heading: '%s'. Strip the puffery and name the topic plainly.
*Triggers:*
“La guía definitiva”, “Todo lo que necesitas saber”, “Domina”, “Dominando”, “El
poder de”, “La magia de”, “El futuro de”, “El arte de”, “La ciencia de”, “Por
qué elegir”, “Descubre el secreto”

### UrgencyInflationEs  _(severity: error)_
*Tell:* AI urgency: '%s'. Delete it or show the stakes concretely.
*Triggers:*
“no se puede subestimar”, “no puede subestimarse”, “no se puede exagerar”, “más
importante que nunca”, “más relevante que nunca”, “más necesario que nunca”, “más
crucial que nunca”, “nunca ha sido tan importante”, “hoy más que nunca”, “en un
mundo cada vez más complejo”, “en un mundo cada vez más digital”, “en un mundo
cada vez más interconectado”, “en la era digital”, “en un punto de inflexión”,
“en una encrucijada”, “en un momento decisivo”

### AbsoluteAssertionsEs  _(severity: warning)_
*Tell:* AI overreach: '%s'. Verify this claim or soften it.
*Triggers:*
“la única forma de”, “la única manera de”, “la única solución”, “el único
camino”, “lo más importante es”, “por encima de todo”, “no cabe duda de que”,
“sin lugar a dudas”, “que no quepa duda”


## Rhetorical structure & cadence

### ContrastiveFormulasEs  _(severity: error)_
*Tell:* AI contrast: '%s'. State the positive claim directly without the 'no X, sino Y' formula.
*Pattern-based:* the Spanish contrastive-negation / tricolon formula. Match the
shape, not fixed wording. Typical shapes: “no se trata solo de… sino de…”, “no
solo… sino también…”, “no es (solamente) una cuestión de… sino de…”, “no es X,
es Y”, “más que X, es Y”.

### VerbTricolonEs  _(severity: warning)_
*Tell:* AI tricolon: '%s'. Three parallel verbs or nouns in series. Restructure or vary the count.
*Pattern-based:* three coordinated parallel items (e.g. “analiza, optimiza y transforma”).

### StackedAnaphoraEs  _(severity: warning)_
*Tell:* AI anaphora: '%s'. Vary the sentence openings or combine into a single statement.
*Pattern-based:* the same opening word(s) repeated across consecutive sentences (e.g. “Cada… Cada… Cada…”).

### RhetoricalDevicesEs  _(severity: error)_
*Tell:* AI rhetoric: '%s'. Remove it or rephrase as a plain statement.
*Triggers:*
“La clave:”, “El problema:”, “La pregunta:”, “El resultado:”, “La conclusión:”,
“La lección:”, “El punto:”, “La prueba:”, “Pregúntate:”

### RhetoricalSelfAnswerEs  _(severity: warning)_
*Tell:* AI rhetorical self-answer: '%s'. State the point directly instead of posing and answering your own question.
*Pattern-based:* a question immediately answered by the same writer (e.g. “¿La razón? …”, “¿El motivo? …”, “¿Por qué? Porque…”).

### NarrativePivotsEs  _(severity: error)_
*Tell:* AI narrative pivot: '%s'. State your point directly.
*Triggers:*
“algo cambió”, “todo cambió”, “y entonces todo cambió”, “eso lo cambió todo”,
“esto lo cambia todo”, “marcó un antes y un después”, “fue un punto de
inflexión”, “y ahí lo entendí”, “y entonces me di cuenta”, “todo cobró sentido”,
“cambió las reglas del juego”

### ParticipialPaddingEs  _(severity: error)_
*Tell:* AI participial padding: '%s'. Delete it or make the point concrete.
*Triggers:*
“destacando su importancia”, “subrayando su relevancia”, “resaltando la
importancia”, “reflejando una tendencia”, “demostrando su compromiso”,
“consolidando su posición”, “reforzando su papel”, “poniendo de manifiesto”,
“dejando patente”, “fomentando un sentido de”, “garantizando una experiencia
fluida”

### DespiteChallengesEs  _(severity: error)_
*Tell:* AI despite-formula: '%s'. Engage with the challenges substantively or remove the hedge.
*Triggers:*
“a pesar de sus desafíos”, “a pesar de estos retos”, “a pesar de las
limitaciones”, “pese a los obstáculos”, “si bien existen desafíos”, “aunque
persisten retos”

### OrganicConsequenceEs  _(severity: error)_
*Tell:* AI inevitability: '%s'. Say the choice was designed that way.
*Triggers:*
“surge de forma natural”, “surge de manera natural”, “emerge de forma orgánica”,
“se desprende naturalmente”, “es una consecuencia natural”, “fluye de manera
natural”, “se deriva naturalmente”


## Filler, padding & metacommentary

### FillerPhrasesEs  _(severity: error)_
*Tell:* AI filler: '%s'. Delete this phrase. It adds no meaning.
*Triggers:*
“una amplia gama de”, “una amplia variedad de”, “un sinfín de”, “una gran
cantidad de”, “una multitud de”, “un sinnúmero de”, “innumerables”, “con el fin
de”, “con el objetivo de”, “con el propósito de”, “de cara a”, “a fin de”,
“debido al hecho de que”, “dado el hecho de que”, “a pesar del hecho de que”, “el
hecho de que”, “es evidente que”, “está claro que”, “resulta evidente que”

### MetacommentaryEs  _(severity: error)_
*Tell:* AI metacommentary: '%s'. Delete it or replace it with substantive content.
*Triggers:*
“Esto importa porque”, “Esto es importante porque”, “Esta distinción es
importante”, “Permíteme explicar”, “Déjame explicarte”, “Vamos a analizar”,
“Analicemos”, “Exploremos”, “Veamos”, “Profundicemos en”, “La clave aquí es”, “El
punto aquí es”, “La idea aquí es”, “En esencia”, “En el fondo”, “Piénsalo como”,
“Aquí es donde se pone interesante”

### RestatementMarkersEs  _(severity: error)_
*Tell:* AI restatement: '%s'. Delete it and trust your original phrasing.
*Triggers:*
“En otras palabras”, “Dicho de otro modo”, “Dicho de otra manera”, “Es decir”,
“O sea”, “Para ser más precisos”, “Más concretamente”, “Para decirlo
claramente”, “En pocas palabras”, “Dicho de forma sencilla”

### SequencingMarkersEs  _(severity: warning)_
*Tell:* AI sequencing: '%s'. Use natural transitions or write an actual list.
*Triggers:*
“En primer lugar”, “En segundo lugar”, “En tercer lugar”, “Por último”, “Por una
parte”, “Por otra parte”, “Primeramente”, “Seguidamente”, “Finalmente”

### ConclusionMarkersEs  _(severity: error)_
*Tell:* AI conclusion: '%s'. Delete this and end on your final point.
*Triggers:*
“En conclusión”, “En resumen”, “En síntesis”, “Para concluir”, “Para finalizar”,
“En definitiva”, “En última instancia”, “A fin de cuentas”, “Al fin y al cabo”,
“En suma”, “Resumiendo”, “Para cerrar”

### FormalTransitionsEs  _(severity: warning)_
*Tell:* AI transition: '%s'. Delete it, or use a simpler connector like 'y', 'pero', or 'así que'.
*Triggers:*
“Además”, “Asimismo”, “Por consiguiente”, “En consecuencia”, “Por lo tanto”, “Por
ende”, “No obstante”, “Por el contrario”, “En contraste”, “De igual manera”, “Del
mismo modo”, “Igualmente”, “Es más”, “De hecho”, “En particular”, “Concretamente”,
“Notablemente”, “Fundamentalmente”, “Como resultado”

### FormalRegisterEs  _(severity: warning)_
*Tell:* AI formalism: '%s'. Use a plainer everyday word (e.g., 'usar', 'ayudar', 'empezar').
*Triggers:*
“utilizar”, “implementar”, “facilitar”, “optimizar”, “maximizar”, “minimizar”,
“priorizar”, “potenciar”, “fomentar”, “propiciar”, “conlleva”, “posibilitar”,
“materializar”, “evidenciar”, “visibilizar”, “dinamizar”

### OpeningClichesEs  _(severity: error)_
*Tell:* AI opening: '%s'. Start with your actual point instead of this generic lead-in.
*Triggers:*
“En el mundo actual”, “En la era digital”, “En un mundo cada vez más”, “Hoy en
día”, “En los últimos años”, “A lo largo de la historia”, “Desde tiempos
inmemoriales”, “Desde los albores de”, “En el vertiginoso mundo de”, “En el
cambiante panorama de”, “Imagina un mundo donde”, “¿Alguna vez te has
preguntado”, “Cuando se trata de”, “En el ámbito de”, “En el campo de”

### ClosingPleasantriesEs  _(severity: error)_
*Tell:* AI closing: '%s'. Delete it and end with your actual content.
*Triggers:*
“Espero que esto te ayude”, “Espero que esto sea útil”, “Espero que te sirva”,
“Espero haber aclarado”, “No dudes en preguntar”, “No dudes en contactar”, “Si
tienes alguna pregunta, no dudes”, “Quedo a tu disposición”, “Estoy aquí para
ayudarte”, “Si necesitas algo más, házmelo saber”


## Headings

### WrapUpHeadingsEs  _(severity: error)_
*Tell:* AI wrap-up heading: '%s'. Delete the section or rename the heading to the topic.
*Triggers:*
“En resumen”, “Conclusión”, “Conclusiones”, “Reflexiones finales”,
“Consideraciones finales”, “Pensamientos finales”, “Para concluir”, “En
definitiva”, “El panorama general”, “Para llevar”

### ExplainerHeadingsEs  _(severity: warning)_
*Tell:* AI explainer heading: '%s'. Name what you're explaining instead.
*Triggers:*
“Lo que aprenderás”, “Lo que veremos”, “Qué esperar”, “Una mirada más cercana”,
“Por qué importa”, “Por qué es importante”, “Cómo funciona”, “Bajo el capó”,
“Desmitificando”


## Punctuation

### EmDashUsageEs  _(severity: warning)_
*Tell:* AI punctuation: em-dash (raya) detected. In Spanish the raya is standard for dialogue and parenthetical asides — flag only when it clusters with other tells and reads as AI cadence, not normal usage.
*Triggers:*
“—”, “–”, “--”


## Tone & self-reference

### SelfReferenceEs  _(severity: error)_
*Tell:* AI cross-reference: '%s'. Rewrite the passage to work without the cross-reference.
*Triggers:*
“como se mencionó anteriormente”, “como se mencionó antes”, “como ya se ha
mencionado”, “como hemos visto”, “como vimos anteriormente”, “como veremos”,
“como se señaló”, “como se indicó previamente”, “tal como se mencionó”,
“recordemos que”, “como ya dijimos”

### AIDisclaimerEs  _(severity: error)_
*Tell:* AI disclaimer leak: '%s'. A model self-disclaimer left in the text — a strong tell in copy-pasted or translated output.
*Triggers:*
“Como modelo de lenguaje”, “Como inteligencia artificial”, “Como IA”, “No tengo
acceso a”, “Mi conocimiento se limita a”, “fecha de corte”

### SycophancyMarkersEs  _(severity: error)_
*Tell:* AI sycophancy: '%s'. Delete this. It sounds robotic and insincere.
*Triggers:*
“Excelente pregunta”, “Gran pregunta”, “Qué buena pregunta”, “Me alegra que
preguntes”, “Estaré encantado de ayudarte”, “Con mucho gusto”, “Por supuesto”,
“Tienes toda la razón”, “Es un excelente punto”, “Una idea fantástica”
