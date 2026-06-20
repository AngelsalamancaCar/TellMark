#!/usr/bin/env python3
"""
gen_rule_catalog.py — regenerate assets/rules/ai-tells.md from upstream
vale-ai-tells YAML. Maintenance tool only; the catalog ships pre-built.

Usage:
  # clone or download https://github.com/tbhb/vale-ai-tells first
  python3 gen_rule_catalog.py /path/to/vale-ai-tells/styles/ai-tells \
      -o ../assets/rules/ai-tells.md

Requires: pyyaml  (pip install pyyaml)
"""
import argparse, glob, json, os, re, textwrap, pathlib
import yaml

CATS = [
    ("Vocabulary & word choice", ["OverusedVocabulary","OverusedVocabularyVerbs","AIAdjectiveNounPairs","AICompoundPhrases","StrategyBuzzwords","ResonateOveruse","ShipOveruse","UnpackExplore","GrowthMetaphors","FigurativeLands"]),
    ("Hedging & throat-clearing", ["HedgingPhrases","DefensiveHedges","RedundantPrecaution","VagueAttributions","FalseBalance","ColloquialAssessments"]),
    ("Promotional / marketing register", ["PromotionalPuffery","MarketingHeadings","UrgencyInflation","AbsoluteAssertions","EmphaticCopula","FalseExclusivity"]),
    ("Rhetorical structure & cadence", ["VerbTricolon","VerbTricolonDensity","ParallelStaccato","StackedAnaphora","ContrastiveNegation","ContrastiveFormulas","RhetoricalDevices","RhetoricalSelfAnswer","MicDrop","NarrativePivots","ParticipialPadding","OrganicConsequence","DespiteChallenges","AffirmativeFormulas"]),
    ("Filler, padding & metacommentary", ["EmptyPadding","EmptyPaddingStacked","FillerPhrases","Metacommentary","StructureAnnouncements","ListIntroductions","RestatementMarkers","SequencingMarkers","ConclusionMarkers","FormalTransitions","FormalRegister","OpeningCliches","ClosingPleasantries","ServesAsDodge","AnthropomorphicJustification"]),
    ("Headings", ["AnnouncementHeadings","ExplainerHeadings","MarketingHeadings","MicDropHeadings","WrapUpHeadings"]),
    ("Punctuation", ["EmDashUsage","SemicolonUsage","ColonUsage"]),
    ("Tone & self-reference", ["SelfReference","SycophancyMarkers"]),
]
IS_REGEX = re.compile(r'[\\\[\](){}|+*?^$]')


def load_rule(path):
    docs = [d for d in yaml.safe_load_all(open(path)) if isinstance(d, dict) and d.get("extends")]
    return docs[0] if docs else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("styles_dir", help="path to vale-ai-tells/styles/ai-tells")
    ap.add_argument("-o", "--output", default="../assets/rules/ai-tells.md")
    args = ap.parse_args()

    rd = {}
    for f in sorted(glob.glob(os.path.join(args.styles_dir, "*.yml"))):
        d = load_rule(f)
        if not d:
            continue
        name = pathlib.Path(f).stem
        toks = d.get("tokens") or d.get("swap") or []
        if isinstance(toks, dict):
            toks = list(toks.keys())
        literal, patterns = [], []
        for t in toks:
            if isinstance(t, dict):
                patterns.append(t.get("pattern", json.dumps(t)))
            elif isinstance(t, str):
                (patterns if IS_REGEX.search(t) else literal).append(t)
        rd[name] = dict(ext=d.get("extends", ""), msg=(d.get("message") or "").strip(),
                        lvl=d.get("level", ""), literal=literal, patterns=patterns)

    assigned, ordered = set(), []
    for title, names in CATS:
        members = [n for n in names if n in rd and n not in assigned]
        assigned.update(members)
        if members:
            ordered.append((title, members))
    leftover = [n for n in rd if n not in assigned]
    if leftover:
        ordered.append(("Other signals", leftover))

    def wrap(ph):
        return "\n".join(textwrap.wrap('\u201c' + '\u201d, \u201c'.join(ph) + '\u201d', 100))

    o = ["# AI-content tell catalog (criteria for review)\n",
         "> Source: **vale-ai-tells** by tbhb \u2014 the `ai-tells` style pack, adapted into a readable "
         "criteria catalog. Original: https://github.com/tbhb/vale-ai-tells (MIT License, \u00a9 2025-2026 "
         "Tony Burns). These are *heuristic signals*, not proof of authorship. Judge every candidate in context.\n",
         "## Categories\n"]
    o += [f"- **{t}** \u2014 {', '.join(m)}" for t, m in ordered]
    o.append("")
    for title, members in ordered:
        o.append(f"\n## {title}\n")
        for n in members:
            r = rd[n]
            o.append(f"### {n}  _(severity: {r['lvl'] or '\u2014'})_")
            if r["msg"]:
                o.append(f"*Tell:* {r['msg']}")
            if r["literal"]:
                cap = r["literal"][:60]; more = len(r["literal"]) - len(cap)
                o.append("*Triggers:*")
                o.append(wrap(cap) + (f"  _(+{more} more in source)_" if more > 0 else ""))
            if r["patterns"]:
                o.append(f"*Pattern-based:* {len(r['patterns'])} structural pattern(s).")
            o.append("")
    pathlib.Path(args.output).write_text("\n".join(o), encoding="utf-8")
    print(f"Wrote {args.output} ({len(rd)} rules).")


if __name__ == "__main__":
    main()
