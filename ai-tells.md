# AI-content tell catalog (criteria for review)

> Source: **vale-ai-tells** by tbhb — the `ai-tells` style pack (60 rules), adapted into a readable criteria catalog. Original: https://github.com/tbhb/vale-ai-tells (MIT License, © 2025-2026 Tony Burns). These are *heuristic signals*, not proof of authorship. Many are legitimate in some registers (especially creative or marketing writing). Judge every candidate in context.

## How to use this catalog

Each entry is a **criterion**: a pattern that frequently signals AI-generated or AI-polished prose. For each you get the tell, its default severity, and example triggers. Literal phrase lists are verbatim from the source; pattern-based entries describe a structural shape rather than fixed words. Scan the document for these, then decide case by case whether each hit is a genuine tell.

## Categories

- **Vocabulary & word choice** — OverusedVocabulary, OverusedVocabularyVerbs, AIAdjectiveNounPairs, AICompoundPhrases, StrategyBuzzwords, ResonateOveruse, ShipOveruse, UnpackExplore, GrowthMetaphors, FigurativeLands
- **Hedging & throat-clearing** — HedgingPhrases, DefensiveHedges, RedundantPrecaution, VagueAttributions, FalseBalance, ColloquialAssessments
- **Promotional / marketing register** — PromotionalPuffery, MarketingHeadings, UrgencyInflation, AbsoluteAssertions, EmphaticCopula, FalseExclusivity
- **Rhetorical structure & cadence** — VerbTricolon, VerbTricolonDensity, ParallelStaccato, StackedAnaphora, ContrastiveNegation, ContrastiveFormulas, RhetoricalDevices, RhetoricalSelfAnswer, MicDrop, NarrativePivots, ParticipialPadding, OrganicConsequence, DespiteChallenges, AffirmativeFormulas
- **Filler, padding & metacommentary** — EmptyPadding, EmptyPaddingStacked, FillerPhrases, Metacommentary, StructureAnnouncements, ListIntroductions, RestatementMarkers, SequencingMarkers, ConclusionMarkers, FormalTransitions, FormalRegister, OpeningCliches, ClosingPleasantries, ServesAsDodge, AnthropomorphicJustification
- **Headings** — AnnouncementHeadings, ExplainerHeadings, MicDropHeadings, WrapUpHeadings
- **Punctuation** — EmDashUsage, SemicolonUsage, ColonUsage
- **Tone & self-reference** — SelfReference, SycophancyMarkers


## Vocabulary & word choice

### OverusedVocabulary  _(severity: error)_
*Tell:* AI vocabulary: '%s'. Replace with a more specific or common word.
*Triggers:*
“delve”, “delves”, “delving”, “delved”, “tapestry”, “multifaceted”, “underscores”, “pivotal”,
“intricate”, “intricacies”, “groundbreaking”, “transformative”, “seamless”, “seamlessly”, “robust”,
“streamline”, “streamlines”, “streamlining”, “elevate”, “elevates”, “elevating”, “bolster”,
“bolsters”, “bolstering”, “underpins”, “underpin”, “underpinning”, “underscoring”, “pivoting”,
“reimagine”, “reimagining”, “reimagines”, “elucidate”, “elucidates”, “elucidating”, “synergy”,
“synergies”, “synergistic”, “holistic”, “holistically”, “paradigm”, “paradigms”, “unparalleled”,
“testament”, “cornerstone”, “cornerstones”, “catalyst”, “catalyze”, “catalyzing”, “meticulous”,
“meticulously”, “nuanced”, “interplay”, “aforementioned”, “myriad”, “plethora”, “burgeoning”,
“nascent”, “ubiquitous”, “encompasses”  _(+117 more in source)_

### OverusedVocabularyVerbs  _(severity: error)_
*Tell:* AI vocabulary (verb form): '%s'. Replace with a direct verb.
*Pattern-based:* 1 structural pattern(s) — match the shape described above, not fixed wording.

### AIAdjectiveNounPairs  _(severity: warning)_
*Tell:* AI adjective-noun pair: '%s %s'. Use concrete description instead.
*Pattern-based:* 2 structural pattern(s) — match the shape described above, not fixed wording.

### AICompoundPhrases  _(severity: error)_
*Tell:* AI fingerprint: '%s'. Rewrite with concrete specifics instead of this clichéd phrase.
*Triggers:*
“rich tapestry”, “rich tapestries”, “tapestry of”, “intricate tapestry”, “complex and multifaceted”,
“multifaceted and complex”, “intricate interplay”, “delicate balance”, “delicate interplay”,
“dynamic interplay”, “crucial role”, “played a crucial role”, “plays a crucial role”, “vital role”,
“pivotal role”, “key role”, “instrumental role”, “cutting-edge”, “game-changer”, “game-changing”,
“paradigm shift”, “sea change”, “tipping point”, “watershed moment”, “double-edged sword”, “slippery
slope”, “tip of the iceberg”, “at the forefront”, “on the cutting edge”, “paving the way”, “laid the
groundwork”, “lays the groundwork”, “sets the stage”, “set the stage”, “a testament to”, “stands as
a testament”, “serve as a reminder”, “serves as a reminder”, “it remains to be seen”, “only time
will tell”, “the jury is still out”, “takes center stage”, “take center stage”, “took center stage”,
“paints a picture of”, “paint a picture of”, “painted a picture of”, “is not without its
challenges”, “are not without their challenges”, “is not without challenges”, “whether we like it or
not”, “whether you like it or not”, “a cornerstone of”, “the transformative power of”, “deeply
rooted in”, “deeply rooted”, “the hallmark of”, “a hallmark of”, “moving the needle”, “moves the
needle”  _(+53 more in source)_
*Pattern-based:* 6 structural pattern(s) — match the shape described above, not fixed wording.

### StrategyBuzzwords  _(severity: error)_
*Tell:* AI strategy buzzword: '%s'. Describe the actual mechanism or advantage plainly.
*Pattern-based:* 13 structural pattern(s) — match the shape described above, not fixed wording.

### ResonateOveruse  _(severity: error)_
*Tell:* AI overused verb: '%s'. Name what connects and why, or disable this rule for physics or audio writing.
*Pattern-based:* 1 structural pattern(s) — match the shape described above, not fixed wording.

### ShipOveruse  _(severity: error)_
*Tell:* AI overused word: '%s'. Name the specific action or object. Disable this rule for maritime or logistics writing.
*Pattern-based:* 1 structural pattern(s) — match the shape described above, not fixed wording.

### UnpackExplore  _(severity: error)_
*Tell:* AI explainer prompt: '%s'. Explain it directly instead of announcing it.
*Triggers:*
“Let's unpack”, “Let me unpack”, “Let's break this down”, “Let me break this down”, “Let's take a
closer look at”, “Let me take a closer look at”, “Let's dive into”, “Let me dive into”, “Let's walk
through”, “Let me walk through”, “Let's dig into”, “Let me dig into”, “Let's examine”, “Let me
examine”, “Let's explore”

### GrowthMetaphors  _(severity: error)_
*Tell:* AI growth metaphor: '%s'. Say what literally happens, or disable this rule for medical or nature writing.
*Pattern-based:* 11 structural pattern(s) — match the shape described above, not fixed wording.

### FigurativeLands  _(severity: error)_
*Tell:* AI overused verb: '%s'. Name the literal action: is merged or is routed to. Disable this rule for aviation or nature prose.
*Pattern-based:* 1 structural pattern(s) — match the shape described above, not fixed wording.


## Hedging & throat-clearing

### HedgingPhrases  _(severity: error)_
*Tell:* AI hedge: '%s'. Delete this throat-clearing and state your point directly.
*Triggers:*
“It's important to note that”, “It is important to note that”, “It is important to understand”, “It
is important to consider”, “It is important to recognize”, “It is important to acknowledge”, “It is
important to emphasize”, “It is important to highlight”, “It is important to mention”, “It's worth
noting that”, “It is worth noting that”, “It's worth mentioning that”, “It is worth mentioning
that”, “It is worth emphasizing that”, “It is worth highlighting that”, “It is worth pointing out
that”, “It is worth remembering that”, “It is essential to note”, “It is essential to understand”,
“It is essential to recognize”, “It is essential to acknowledge”, “It is essential to emphasize”,
“It is crucial to note”, “It is crucial to understand”, “It is crucial to recognize”, “It is
critical to note”, “It is critical to understand”, “It is critical to recognize”, “It is necessary
to note”, “It is necessary to understand”, “It is necessary to recognize”, “It should be noted
that”, “It should be emphasized that”, “It should be mentioned that”, “It bears mentioning”, “It
goes without saying”, “Needless to say”, “Generally speaking”, “Broadly speaking”, “For the most
part”, “By and large”, “All things considered”, “That being said”, “That said”, “With that said”,
“Having said that”, “On the other hand”, “At the same time”, “To be sure”, “To some extent”, “In
some ways”, “In many ways”, “In a sense”, “As such”, “As it were”, “One thing is clear”, “One thing
is certain”, “One thing is for sure”, “One thing is for certain”, “This much is clear”  _(+19 more in source)_

### DefensiveHedges  _(severity: error)_
*Tell:* AI defensive hedge: '%s'. State your point directly without pre-defending it.
*Pattern-based:* 34 structural pattern(s) — match the shape described above, not fixed wording.

### RedundantPrecaution  _(severity: error)_
*Tell:* AI cliché: '%s'. Name the specific safeguard or cut the phrase.
*Triggers:*
“belt and suspenders”, “belt-and-suspenders”

### VagueAttributions  _(severity: error)_
*Tell:* AI vague attribution: '%s'. Name the specific source or delete the claim.
*Triggers:*
“experts argue”, “experts suggest”, “experts believe”, “experts say”, “experts agree”, “experts
warn”, “experts note”, “experts predict”, “experts contend”, “experts recommend”, “experts have
noted”, “experts have argued”, “experts have suggested”, “experts have warned”, “industry reports
suggest”, “industry reports indicate”, “industry reports show”, “industry experts”, “industry
observers”, “industry analysts”, “observers have cited”, “observers have noted”, “observers note”,
“critics argue”, “critics suggest”, “critics contend”, “critics have noted”, “critics have argued”,
“some critics argue”, “some experts argue”, “some experts suggest”, “some experts believe”, “some
analysts”, “some observers”, “some researchers”, “many experts”, “many analysts”, “many observers”,
“many researchers”, “studies show that”, “studies suggest that”, “studies indicate that”, “studies
have shown that”, “studies have found that”, “research shows that”, “research suggests that”,
“research indicates that”, “research has shown that”, “research has found that”, “several studies”,
“several experts”, “several analysts”, “several observers”, “numerous studies”, “numerous experts”,
“a growing body of research”, “a growing body of evidence”, “a growing number of experts”, “the
evidence suggests”, “the data suggests”  _(+1 more in source)_

### FalseBalance  _(severity: error)_
*Tell:* AI evasion: '%s'. Take a clear position or remove the hedge.
*Triggers:*
“both sides of the argument”, “both sides present valid points”, “there are valid points on both
sides”, “each perspective has merit”, “each side has merit”, “it's important to consider all
perspectives”, “important to consider the perspectives”, “consider all stakeholders”, “perspectives
of all stakeholders”, “a balanced approach”, “strike a balance”, “find a balance”, “nuanced
understanding”, “nuanced approach”, “the answer is not straightforward”, “not a simple answer”,
“there is no simple answer”, “the issue is complex”, “this is a complex issue”, “depends on various
factors”, “depends on many factors”, “varies depending on”, “context-dependent”, “situation-
dependent”, “case-by-case basis”

### ColloquialAssessments  _(severity: error)_
*Tell:* AI colloquial assessment: '%s'. State the assessment directly.
*Pattern-based:* 22 structural pattern(s) — match the shape described above, not fixed wording.


## Promotional / marketing register

### PromotionalPuffery  _(severity: error)_
*Tell:* AI puffery: '%s'. Use neutral, specific language.
*Triggers:*
“nestled in the”, “nestled in a”, “nestled between”, “nestled among”, “nestled alongside”, “nestled
within”, “in the heart of”, “at the heart of”, “rich cultural heritage”, “rich history and”, “rich
and diverse”, “rich and vibrant”, “vibrant community”, “vibrant culture”, “vibrant ecosystem”,
“vibrant atmosphere”, “natural beauty”, “natural beauty of”, “a hub for”, “a hub of”, “a dynamic
hub”, “a thriving hub”, “a cultural hub”, “a beacon of”, “a beacon for”, “a treasure trove of”, “a
treasure trove for”, “a shining example”, “a prime example”, “a masterclass in”, “a testament to
the”, “a testament to its”, “renowned for its”, “renowned for their”, “renowned for her”, “renowned
for his”, “widely regarded as”, “widely recognized as”, “widely considered”, “is home to”, “has
emerged as a”, “has emerged as the”, “has established itself as”, “continues to evolve”, “continues
to thrive”, “continues to grow”, “continues to inspire”, “left an indelible mark”, “left an
indelible impact”, “leaving an indelible mark”, “left a lasting impact”, “left a lasting
impression”, “leaving a lasting impact”, “a lasting legacy”, “enduring legacy”, “enduring impact”,
“an enduring legacy”

### MarketingHeadings  _(severity: error)_
*Tell:* AI marketing heading: '%s'. Strip the puffery and name the topic plainly.
*Triggers:*
“The Ultimate Guide”, “Everything You Need to Know”, “Mastering”, “Unlocking”, “The Power of”, “The
Magic of”, “Why Choose”, “The Future of”, “The Art of”, “The Science of”, “A Game-Changer”,
“Revolutionizing”

### UrgencyInflation  _(severity: error)_
*Tell:* AI urgency: '%s'. Delete it or show the stakes concretely.
*Triggers:*
“cannot be overstated”, “can't be overstated”, “cannot be understated”, “can't be understated”,
“cannot be emphasized enough”, “can't be emphasized enough”, “more important than ever”, “more
critical than ever”, “more relevant than ever”, “more urgent than ever”, “more necessary than ever”,
“more essential than ever”, “more vital than ever”, “more pressing than ever”, “more significant
than ever”, “has never been more important”, “has never been more critical”, “has never been more
urgent”, “has never been more relevant”, “has never been more necessary”, “has never been more
essential”, “has never been more vital”, “has never been more pressing”, “has never been more
significant”, “have never been more important”, “have never been more critical”, “have never been
more urgent”, “have never been more relevant”, “the stakes have never been higher”, “the stakes are
higher than ever”, “the stakes couldn't be higher”, “the stakes are enormous”, “the stakes are
immense”, “at a crossroads”, “at an inflection point”, “at a pivotal moment”, “at a critical
juncture”, “at a defining moment”, “at a turning point in history”, “at a critical moment in
history”, “at a pivotal moment in history”, “in an increasingly complex world”, “in an increasingly
digital world”, “in an increasingly connected world”, “in an increasingly competitive world”, “in an
increasingly polarized world”, “in an increasingly uncertain world”, “in an increasingly fast-paced
world”, “in an increasingly globalized world”, “in an increasingly data-driven world”, “in an
increasingly automated world”, “in an ever more complex world”, “in an ever more connected world”

### AbsoluteAssertions  _(severity: error)_
*Tell:* AI overreach: '%s'. Verify this claim or soften it.
*Triggers:*
“the only way to”, “the only real solution”, “the only way forward”, “the single most important”,
“the most important thing is”, “above all else”, “above everything else”, “more than anything else”,
“there is no better”, “there is no other way”, “there can be no doubt”, “make no mistake”, “make no
mistake about it”, “there's no denying”, “there is no denying”

### EmphaticCopula  _(severity: error)_
*Tell:* AI emphasis: '%s'. Remove the italics. Emphasizing a copula rarely adds meaning.
*Triggers:*
“ _is_”, “ _are_”, “ _was_”, “ _were_”, “ _the_”, “ _and_”, “ _not_”, “ _or_”
*Pattern-based:* 8 structural pattern(s) — match the shape described above, not fixed wording.

### FalseExclusivity  _(severity: error)_
*Tell:* AI false exclusivity: '%s'. State the point directly without claiming insider knowledge.
*Triggers:*
“nobody talks about”, “no one talks about”, “nobody mentions”, “no one mentions”, “nobody is talking
about”, “no one is talking about”, “nobody discusses”, “no one discusses”, “the part nobody
mentions”, “the part no one mentions”, “the part nobody talks about”, “the part no one talks about”,
“what nobody tells you”, “what no one tells you”, “what nobody mentions”, “what no one mentions”,
“what most people miss”, “what most people don't”, “what most people overlook”, “what most people
forget”, “the dirty secret”, “the dirty little secret”, “the open secret”, “the uncomfortable
truth”, “the inconvenient truth”, “the elephant in the room”, “the unspoken truth”, “the unspoken
reality”, “the hidden truth”, “the hidden cost”, “the hidden costs”, “the silent killer”, “here's
what most people miss”, “here's what nobody tells you”, “here's what no one tells you”


## Rhetorical structure & cadence

### VerbTricolon  _(severity: error)_
*Tell:* AI tricolon: '%s'. Three parallel verbs in series. Restructure or vary the count.
*Pattern-based:* 24 structural pattern(s) — match the shape described above, not fixed wording.

### VerbTricolonDensity  _(severity: error)_
*Tell:* AI tricolon: multiple verb tricolons in one paragraph (found %s). Rewrite some with two or four items.

### ParallelStaccato  _(severity: error)_
*Tell:* AI staccato: '%s'. Combine these clipped parallel sentences or vary the structure.
*Pattern-based:* 8 structural pattern(s) — match the shape described above, not fixed wording.

### StackedAnaphora  _(severity: error)_
*Tell:* AI anaphora: '%s'. Vary the sentence openings or combine into a single statement.
*Pattern-based:* 53 structural pattern(s) — match the shape described above, not fixed wording.

### ContrastiveNegation  _(severity: error)_
*Tell:* AI contrast by negation: '%s'. State the positive directly without the trailing negation.
*Pattern-based:* 2 structural pattern(s) — match the shape described above, not fixed wording.

### ContrastiveFormulas  _(severity: error)_
*Tell:* AI contrast: '%s'. State the positive claim directly without the 'not X, but Y' formula.
*Pattern-based:* 120 structural pattern(s) — match the shape described above, not fixed wording.

### RhetoricalDevices  _(severity: error)_
*Tell:* AI rhetoric: '%s'. Remove it or rephrase as a plain statement.
*Triggers:*
“The test:”, “The test is:”, “The litmus test:”, “A good test:”, “The acid test:”, “Ask yourself:”,
“Ask yourself whether”, “Ask yourself if”, “The question to ask:”, “The question to ask is:”, “The
price:”, “The catch:”, “The kicker:”, “The upshot:”, “The tradeoff:”, “The trade-off:”, “The
trick:”, “The cost:”, “The downside:”, “The flip side:”, “The bottom line:”, “The takeaway:”, “The
result:”, “The answer:”, “The reason:”, “The lesson:”, “The moral:”, “The point:”, “The pitch:”,
“The fix:”, “The payoff:”
*Pattern-based:* 5 structural pattern(s) — match the shape described above, not fixed wording.

### RhetoricalSelfAnswer  _(severity: error)_
*Tell:* AI rhetorical self-answer: '%s'. State the point directly instead of posing and answering your own question.
*Pattern-based:* 44 structural pattern(s) — match the shape described above, not fixed wording.

### MicDrop  _(severity: error)_
*Tell:* AI mic-drop: '%s'. Integrate the point into the surrounding text or cut it.
*Pattern-based:* 63 structural pattern(s) — match the shape described above, not fixed wording.

### NarrativePivots  _(severity: error)_
*Tell:* AI narrative pivot: '%s'. State your point directly.
*Triggers:*
“something shifted”, “something changed”, “something clicked”, “something snapped”, “everything
changed”, “everything shifted”, “everything clicked”, “and then everything changed”, “and then it
clicked”, “and then it hit me”, “that changed everything”, “that changes everything”, “this changes
everything”, “this changed everything”, “and that made all the difference”, “and that makes all the
difference”, “but then something interesting happened”, “but then something unexpected happened”,
“but then I realized”, “and that's when it hit me”, “and that's when I realized”, “it was a turning
point”, “it was an inflection point”, “it was a watershed moment”, “it was a game-changer”, “it was
a wake-up call”, “a light bulb went off”, “a lightbulb went off”, “the penny dropped”, “it all came
together”, “it all made sense”, “things started to click”, “things fell into place”, “changed the
game”, “changes the game”, “changing the game”, “change the game”, “changed the game forever”,
“changes the game forever”, “changed everything forever”, “changed the landscape”, “changes the
landscape”, “rewrote the rules”, “rewrites the rules”, “rewriting the rules”, “rewrote the
playbook”, “rewrites the playbook”, “rewriting the playbook”, “flipped the script”, “flips the
script”, “flipping the script”, “moved the goalposts”, “shifted the paradigm”

### ParticipialPadding  _(severity: error)_
*Tell:* AI participial padding: '%s'. Delete it or make the point concrete.
*Triggers:*
“highlighting its importance”, “highlighting its significance”, “highlighting its role”,
“highlighting the importance”, “highlighting the need”, “highlighting the growing”, “underscoring
its importance”, “underscoring its significance”, “underscoring its role”, “underscoring the
importance”, “underscoring the need”, “underscoring its commitment”, “emphasizing the importance”,
“emphasizing the need”, “emphasizing its role”, “emphasizing its commitment”, “reflecting broader
trends”, “reflecting broader changes”, “reflecting a broader”, “reflecting the broader”, “reflecting
its commitment”, “reflecting a growing”, “reflecting the growing”, “symbolizing its”, “symbolizing
the”, “contributing to its”, “contributing to the development”, “contributing to the growth”,
“contributing to the overall”, “contributing to a more”, “contributing to the region”, “showcasing
its”, “showcasing the”, “showcasing a”, “demonstrating its commitment”, “demonstrating its
dedication”, “demonstrating a commitment”, “demonstrating the importance”, “underscoring its
enduring”, “underscoring its lasting”, “reinforcing its position”, “reinforcing its role”,
“reinforcing its commitment”, “reinforcing the importance”, “solidifying its position”, “solidifying
its role”, “solidifying its place”, “cementing its position”, “cementing its role”, “cementing its
place”, “ensuring a seamless”, “ensuring a smooth”, “ensuring a more”, “fostering a sense of”,
“fostering a culture of”, “fostering a more”, “fostering an environment”, “cultivating a sense of”,
“cultivating a culture of”, “shaping the future”  _(+8 more in source)_

### OrganicConsequence  _(severity: error)_
*Tell:* AI inevitability: '%s'. Say the choice was designed that way.
*Triggers:*
“falls out naturally”, “fell out naturally”, “fall out naturally”, “emerges naturally”, “emerged
naturally”, “emerge naturally”, “emerges organically”, “emerged organically”, “arises naturally”,
“arose naturally”, “arise naturally”, “arises organically”, “flows naturally”, “flowed naturally”,
“flow naturally”, “a natural consequence”, “the natural consequence”, “a natural result”, “the
natural result”, “naturally follows”, “naturally leads to”, “naturally results in”, “follows
naturally from”, “results naturally from”

### DespiteChallenges  _(severity: error)_
*Tell:* AI despite-formula: '%s'. Engage with the challenges substantively or remove the hedge.
*Triggers:*
“despite its challenges”, “despite these challenges”, “despite the challenges”, “despite this
challenge”, “despite these limitations”, “despite its limitations”, “despite the limitations”,
“despite these drawbacks”, “despite its drawbacks”, “despite these obstacles”, “despite its
obstacles”, “despite these hurdles”, “despite its hurdles”, “despite these setbacks”, “despite its
setbacks”, “despite these concerns”, “despite its concerns”, “despite facing challenges”, “despite
facing numerous”, “despite facing significant”, “while challenges remain”, “while these challenges”,
“while significant challenges”, “challenges notwithstanding”, “obstacles notwithstanding”,
“limitations notwithstanding”

### AffirmativeFormulas  _(severity: error)_
*Tell:* AI affirmation: '%s'. Cut the flourish and state the point plainly.
*Pattern-based:* 65 structural pattern(s) — match the shape described above, not fixed wording.


## Filler, padding & metacommentary

### EmptyPadding  _(severity: error)_
*Tell:* AI empty modifier: '%s %s'. Delete the modifier and keep the noun.
*Pattern-based:* 2 structural pattern(s) — match the shape described above, not fixed wording.

### EmptyPaddingStacked  _(severity: error)_
*Tell:* AI empty modifier: '%s %s %s'. Delete the modifier and keep the noun.
*Pattern-based:* 3 structural pattern(s) — match the shape described above, not fixed wording.

### FillerPhrases  _(severity: error)_
*Tell:* AI filler: '%s'. Delete this phrase. It adds no meaning.
*Triggers:*
“a wide range of”, “a broad range of”, “a variety of”, “a myriad of”, “a plethora of”, “a wealth
of”, “an abundance of”, “a multitude of”, “countless”, “numerous”, “innumerable”, “in order to”,
“for the purpose of”, “with the aim of”, “with a view to”, “so as to”, “serves to”, “tends to”, “has
the potential to”, “has the ability to”, “is capable of”, “is able to”, “due to the fact that”,
“owing to the fact that”, “in light of the fact that”, “given the fact that”, “despite the fact
that”, “regardless of the fact that”, “the fact that”, “it is clear that”, “it is evident that”, “it
is apparent that”, “it is obvious that”, “it can be seen that”, “it can be observed that”, “and
honestly”, “and honestly,”, “honestly,”, “to be honest,”, “and frankly”, “and frankly,”, “frankly,”,
“and truthfully”, “truthfully,”, “if i'm being honest”, “if i'm being frank”, “to be frank,”, “to
tell you the truth”, “the truth is,”, “in all honesty”, “in all honesty,”, “quite honestly”, “quite
frankly”, “i'll be honest”, “i will be honest”, “to be perfectly honest”, “to be completely honest”,
“to be totally honest”, “to be brutally honest”, “to be 100% honest”  _(+7 more in source)_
*Pattern-based:* 3 structural pattern(s) — match the shape described above, not fixed wording.

### Metacommentary  _(severity: error)_
*Tell:* AI metacommentary: '%s'. Delete it or replace it with substantive content.
*Triggers:*
“This matters because”, “This is important because”, “This distinction matters”, “This difference
matters”, “This framing matters”, “This choice matters”, “This detail matters”, “This nuance
matters”, “This subtlety matters”, “Let me explain”, “Let's explore”, “Let's examine”, “Let's
consider”, “Let's look at”, “Let's break down”, “Let's unpack”, “Let's dive into”, “The key here
is”, “The point here is”, “The idea here is”, “The insight here is”, “The takeaway here is”, “The
important thing here is”, “This is the insight”, “This is the key”, “This is the point”, “This is
the takeaway”, “This is the crucial”, “This is the critical”, “This is the important”, “In the real
world”, “At its core”, “At its heart”, “At its most basic”, “At its most basic level”, “At its most
fundamental”, “At its most fundamental level”, “At its simplest”, “At their core”, “At their heart”,
“Think of it as”, “Think of this as”, “This is where it gets interesting”, “This is where things get
interesting”
*Pattern-based:* 36 structural pattern(s) — match the shape described above, not fixed wording.

### StructureAnnouncements  _(severity: error)_
*Tell:* AI structure announcement: '%s'. Present the content instead of narrating that you're about to.
*Triggers:*
“key takeaway”, “key takeaways”, “the takeaway is”, “the takeaway here is”, “main takeaway”, “main
takeaways”, “quick recap”, “a quick recap”, “to recap”, “to recap briefly”, “quick summary”, “a
quick summary”, “quick overview”, “a quick overview”, “to put it plainly”, “to put this in
perspective”

### ListIntroductions  _(severity: error)_
*Tell:* AI list intro: '%s'. Skip the announcement and present the content directly.
*Triggers:*
“Below you'll find”, “Below you will find”, “Here's a breakdown of”, “Here is a breakdown of”,
“Here's an overview of”, “Here is an overview of”, “Here's a summary of”, “Here is a summary of”,
“Here's everything you need to know”, “Here is everything you need to know”, “Here's what you need
to know about”, “Here is what you need to know about”, “The following sections will”, “The following
guide will”, “The following tutorial will”, “The following walkthrough will”

### RestatementMarkers  _(severity: error)_
*Tell:* AI restatement: '%s'. Delete it and trust your original phrasing.
*Triggers:*
“In other words”, “Simply put”, “Put simply”, “Put differently”, “To put it simply”, “To put it
another way”, “Said differently”, “To state it plainly”, “To state this plainly”, “To be more
precise”, “To be more specific”, “To be more exact”, “Or rather”, “More precisely”, “More
specifically”, “More accurately”, “To clarify”, “To rephrase”, “To restate”, “What I mean is”, “What
this means is”, “What that means is”, “In plainer terms”, “In plain terms”, “In plain English”, “In
simpler terms”, “In simple terms”, “To put it another way”, “To put it more simply”, “To put it more
directly”

### SequencingMarkers  _(severity: error)_
*Tell:* AI sequencing: '%s'. Use natural transitions or write an actual list.
*Triggers:*
“Firstly”, “Secondly”, “Thirdly”, “Fourthly”, “Fifthly”, “Lastly”, “The first takeaway”, “The second
takeaway”, “The third takeaway”, “The fourth takeaway”, “The first lesson”, “The second lesson”,
“The third lesson”, “The first key”, “The second key”, “The third key”, “The first thing to note”,
“The second thing to note”, “The first point”, “The second point”, “The third point”, “The first
reason”, “The second reason”, “The third reason”, “The first challenge”, “The second challenge”,
“The third challenge”, “The first step is”, “The second step is”, “The third step is”, “The first
benefit”, “The second benefit”, “The third benefit”, “The first advantage”, “The second advantage”,
“The third advantage”

### ConclusionMarkers  _(severity: error)_
*Tell:* AI conclusion: '%s'. Delete this and end on your final point.
*Triggers:*
“In conclusion”, “In summary”, “To summarize”, “To sum up”, “To conclude”, “In closing”,
“Ultimately”, “All in all”, “At the end of the day”, “When all is said and done”, “The bottom line
is”, “In the final analysis”, “Taking everything into account”, “Taking all of this into account”,
“Overall”, “On the whole”, “By way of conclusion”

### FormalTransitions  _(severity: error)_
*Tell:* AI transition: '%s'. Delete it, or use a simpler connector like 'and', 'but', or 'so'.
*Triggers:*
“Moreover”, “Furthermore”, “Additionally”, “Consequently”, “Subsequently”, “Nevertheless”,
“Nonetheless”, “Conversely”, “Accordingly”, “Hence”, “Thus”, “Therefore”, “Thereby”, “Henceforth”,
“Likewise”, “Similarly”, “In addition”, “In contrast”, “On the contrary”, “By contrast”, “As a
result”, “For instance”, “For example”, “In particular”, “Specifically”, “Notably”, “Importantly”,
“Significantly”, “Crucially”, “Essentially”, “Fundamentally”, “With that in mind”, “With this in
mind”, “To that end”, “In turn”, “Building on this”, “Building on that”, “That's why”, “This is
why”, “Which is why”, “That's because”, “This is because”, “What's more”, “What is more”, “Not to
mention”, “To that point”, “On that note”, “On a related note”, “Case in point”, “A case in point”,
“Of note”, “Worth noting”, “Along the same lines”, “In the same vein”, “By extension”, “To top it
off”, “That's not all”, “Better yet”, “Even better”, “Equally important”  _(+8 more in source)_

### FormalRegister  _(severity: error)_
*Tell:* AI formalism: '%s'. Use a plainer everyday word (e.g., 'use', 'help', 'start').
*Triggers:*
“utilize”, “utilizes”, “utilizing”, “utilized”, “utilization”, “facilitate”, “facilitates”,
“facilitating”, “facilitated”, “facilitation”, “implement”, “implements”, “implementing”,
“implementation”, “commence”, “commences”, “commencing”, “commenced”, “terminate”, “terminates”,
“terminating”, “terminated”, “ascertain”, “ascertains”, “ascertaining”, “endeavour”, “endeavours”,
“endeavouring”, “methodology”, “methodologies”, “framework”, “frameworks”, “conceptualize”,
“conceptualizes”, “conceptualizing”, “operationalize”, “operationalizes”, “operationalizing”,
“prioritize”, “prioritizes”, “prioritizing”, “incentivize”, “incentivizes”, “incentivizing”,
“optimize”, “optimizes”, “optimizing”, “maximize”, “maximizes”, “maximizing”, “minimize”,
“minimizes”, “minimizing”

### OpeningCliches  _(severity: error)_
*Tell:* AI opening: '%s'. Start with your actual point instead of this generic lead-in.
*Triggers:*
“In today's rapidly evolving”, “In today's fast-paced”, “In today's digital age”, “In today's ever-
changing”, “In today's interconnected”, “In the realm of”, “In the world of”, “In the landscape of”,
“In the ever-evolving landscape”, “In an era where”, “In an age where”, “In this day and age”,
“Embarking on a journey”, “Embark on a journey”, “Embarking on this journey”, “As we navigate”, “As
we delve into”, “As we explore”, “When it comes to”, “Picture this”, “Imagine a world where”, “Have
you ever wondered”, “In recent years”, “Throughout history”, “Since the dawn of”, “From time
immemorial”, “Before we dive in”, “Before we dive into”, “By the end of this article”, “By the end
of this guide”, “By the end of this post”, “By the end of this tutorial”, “By the end of this
section”, “This guide will walk you through”, “This article will walk you through”, “This post will
walk you through”, “This guide will help you”, “This article will help you”, “This post will help
you”, “Welcome to this guide”, “Welcome to this overview”, “Welcome to this exploration”, “Welcome
to this deep dive”, “Without further ado”, “Without further ado, let's”, “Without further ado,
here's”, “Gone are the days”, “Gone are the days when”, “Gone are the days of”, “Whether you're a”,
“Whether you're an”, “Whether you're just”, “Whether you're new”, “Whether you're already”, “Whether
you're looking”, “Whether you're trying”, “Whether you're someone”, “You might be wondering”, “You
may be wondering”, “You're probably wondering”  _(+32 more in source)_

### ClosingPleasantries  _(severity: error)_
*Tell:* AI closing: '%s'. Delete it and end with your actual content.
*Triggers:*
“I hope this helps”, “I hope this was helpful”, “I hope this is helpful”, “I hope this proves
helpful”, “I hope this will be helpful”, “Hope this helps”, “Hope this was helpful”, “I hope this
clears things up”, “I hope this cleared things up”, “I hope this answers your question”, “I hope
that answers your question”, “I hope this helps clarify”, “I hope this gives you a better
understanding”, “I hope you find this helpful”, “I hope you found this helpful”, “I hope you find
this useful”, “I hope you found this useful”, “I hope this is what you were looking for”, “I hope
this pointed you in the right direction”, “I hope this sheds some light”, “I hope this makes things
clearer”, “Hopefully this helps”, “Hopefully this is helpful”, “Feel free to ask”, “Feel free to
reach out”, “Feel free to let me know”, “Feel free to contact”, “Feel free to ask questions”, “Feel
free to ask if you”, “Feel free to ask if there”, “Feel free to drop”, “Please feel free to ask”,
“Please feel free to reach out”, “Don't hesitate to ask”, “Don't hesitate to reach out”, “Don't
hesitate to contact”, “Don't hesitate to get in touch”, “Don't hesitate to drop”, “Please don't
hesitate to ask”, “Please don't hesitate to reach out”, “Please don't hesitate to contact”, “Let me
know if you have any questions”, “Let me know if you have further questions”, “Let me know if you
have any other questions”, “Let me know if you have additional questions”, “Let me know if you need
anything else”, “Let me know if you need further clarification”, “Let me know if you need any
clarification”, “Let me know if you'd like more information”, “Let me know if you'd like me to
elaborate”, “Let me know if you'd like me to clarify”, “Let me know if you'd like me to expand”,
“Let me know if there's anything else”, “Let me know if there's anything I can help with”, “Let me
know if anything is unclear”, “Let me know if that makes sense”, “Let me know if you want me to”,
“If you have any questions, feel free”, “If you have any further questions”, “If you have any
additional questions”  _(+39 more in source)_

### ServesAsDodge  _(severity: error)_
*Tell:* AI copula dodge: '%s'. Use 'is' or 'are' instead of this inflated construction.
*Triggers:*
“serves as a”, “serves as an”, “serves as the”, “served as a”, “served as an”, “served as the”,
“serving as a”, “serving as an”, “serving as the”, “stands as a”, “stands as an”, “stands as the”,
“stood as a”, “stood as an”, “stood as the”, “standing as a”, “standing as an”, “standing as the”,
“marks a pivotal”, “marks a significant”, “marks a crucial”, “marks a key”, “marks a turning”,
“marks a critical”, “marks a major”, “marks a defining”, “marks a new”, “represents a significant”,
“represents a pivotal”, “represents a crucial”, “represents a key”, “represents a major”,
“represents a fundamental”, “represents a paradigm”, “boasts a vibrant”, “boasts a rich”, “boasts a
diverse”, “boasts a wide”, “boasts a unique”, “boasts a thriving”, “boasts an impressive”, “features
a wide”, “features a rich”, “features a diverse”, “features a unique”, “features a vibrant”, “offers
a unique”, “offers a wide”, “offers a comprehensive”, “offers a diverse”
*Pattern-based:* 1 structural pattern(s) — match the shape described above, not fixed wording.

### AnthropomorphicJustification  _(severity: error)_
*Tell:* AI cliché: '%s'. Say what you mean directly.
*Triggers:*
“earned its keep”, “earned its place”, “earned its spot”, “paid for itself”, “paid dividends”, “paid
its rent”, “paying its rent”, “carrying its weight”, “pulling its weight”, “punching above its
weight”, “worth its weight”, “doing the heavy lifting”, “doing a lot of heavy lifting”, “doing the
legwork”, “do the heavy lifting”, “load-bearing”, “load bearing”, “doing the work”, “doing the real
work”, “doing the actual work”, “doing the hard work”, “doing the important work”, “doing most of
the work”, “standing on its own”, “holding its own”, “speaking for itself”, “justify its existence”,
“justifying its existence”, “doing harm”, “doing no harm”, “without doing harm”, “causing harm”,
“without causing harm”
*Pattern-based:* 48 structural pattern(s) — match the shape described above, not fixed wording.


## Headings

### AnnouncementHeadings  _(severity: error)_
*Tell:* AI announcement heading: '%s'. Cut the heading or rename it to the topic.
*Triggers:*
“What You'll Learn”, “What You Will Learn”, “What We'll Cover”, “What We Will Cover”, “What to
Expect”, “What We're Building”, “What We Are Building”, “Here's What You'll Get”, “Here's What You
Get”

### ExplainerHeadings  _(severity: error)_
*Tell:* AI explainer heading: '%s'. Name what you're explaining instead.
*Triggers:*
“Deep Dive”, “Under the Hood”, “Demystifying”, “Why It Matters”, “Why This Matters”, “Why It
Exists”, “Why This Exists”, “What It Solves”, “What This Solves”, “What It Does”, “What This Does”,
“A Closer Look”, “The Inner Workings”

### MicDropHeadings  _(severity: error)_
*Tell:* AI mic-drop: '%s'. Use a descriptive heading instead.
*Pattern-based:* 6 structural pattern(s) — match the shape described above, not fixed wording.

### WrapUpHeadings  _(severity: error)_
*Tell:* AI wrap-up heading: '%s'. Delete the section or rename the heading to the topic.
*Triggers:*
“Final Thoughts”, “Closing Thoughts”, “Parting Thoughts”, “Wrapping Up”, “Wrap-Up”, “Wrap Up”,
“Putting It All Together”, “Bringing It All Together”, “Tying It All Together”, “The Big Picture”,
“The Bottom Line”, “The Takeaway”, “Final Word”, “Last Word”, “Final Take”


## Punctuation

### EmDashUsage  _(severity: error)_
*Tell:* AI punctuation: em-dash detected. Use a comma, period, or parentheses instead.
*Triggers:*
“—”, “–”, “--”

### SemicolonUsage  _(severity: error)_
*Tell:* AI punctuation: '%s'. Replace the semicolon with a period or two sentences.
*Pattern-based:* 1 structural pattern(s) — match the shape described above, not fixed wording.

### ColonUsage  _(severity: error)_
*Tell:* AI punctuation: '%s'. Lowercase the word after the colon unless it is a proper noun.
*Pattern-based:* 1 structural pattern(s) — match the shape described above, not fixed wording.


## Tone & self-reference

### SelfReference  _(severity: error)_
*Tell:* AI cross-reference: '%s'. Rewrite the passage to work without the cross-reference.
*Triggers:*
“as mentioned above”, “as mentioned earlier”, “as mentioned before”, “as noted above”, “as noted
earlier”, “as noted before”, “as discussed above”, “as discussed earlier”, “as discussed before”,
“as stated above”, “as stated earlier”, “as stated before”, “as outlined above”, “as outlined
earlier”, “as described above”, “as described earlier”, “as referenced above”, “as referenced
earlier”, “as we saw”, “as we saw above”, “as we saw earlier”, “as we'll see”, “as we'll explore”,
“as we'll discuss”, “as we discussed”, “as we explored”, “as we covered”, “as covered above”, “as
covered earlier”, “as shown above”, “as shown earlier”, “as explained above”, “as explained
earlier”, “as we noted”, “recall that”, “remember that”, “as previously mentioned”, “as previously
noted”, “as previously discussed”, “as previously stated”, “as previously described”, “as I
mentioned”, “as I noted”, “as I discussed”, “as I said”, “as I explained”

### SycophancyMarkers  _(severity: error)_
*Tell:* AI sycophancy: '%s'. Delete this. It sounds robotic and insincere.
*Triggers:*
“Great question”, “Excellent question”, “That's a great question”, “That's an excellent question”,
“What a great question”, “Fantastic question”, “Wonderful question”, “I'm glad you asked”, “I'm
happy to help”, “I'd be happy to help”, “I'd be glad to help”, “Absolutely”, “Certainly”, “Of
course”, “Without a doubt”, “You're absolutely right”, “You make an excellent point”, “That's a
wonderful idea”, “That's a fantastic point”, “I couldn't agree more”
