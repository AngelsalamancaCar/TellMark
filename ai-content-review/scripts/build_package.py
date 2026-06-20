#!/usr/bin/env python3
"""
build_package.py — assemble a self-contained AI-content review package.

Pipeline:
  source document  --(liteparse)-->  layout text  -->  line-anchored document.md
                                                   +    rules.md / prompt.md / output-spec.md
                                                   +    manifest.json / README.md
The package folder can then be handed to any agent harness (Claude CLI, etc.)
to run the review. This script never judges the text — it only prepares.

Usage:
  python build_package.py [INPUT] [-o OUTPUT_DIR]
  INPUT may be a PDF / DOCX / PPTX / image (parsed with liteparse) or a
  .txt / .md file (used as-is, no liteparse needed).
  If INPUT is omitted, the single file found in data/source/ is used
  automatically. Either way, the package defaults to
  data/processed/<input-name>-review-package unless -o overrides it.
"""
import argparse, hashlib, json, os, re, shutil, subprocess, sys, datetime, pathlib

SKILL_ROOT = pathlib.Path(__file__).resolve().parent.parent
REPO_ROOT = SKILL_ROOT.parent
ASSETS = SKILL_ROOT / "assets"
DATA_SOURCE = REPO_ROOT / "data" / "source"
DATA_PROCESSED = REPO_ROOT / "data" / "processed"
PASSTHROUGH = {".txt", ".md", ".markdown", ".text"}

# Catalog selection by document language. Pure file-selection — no detection,
# no scoring. The chosen file is always copied into the package as `rules.md`,
# so prompt.md / output-spec.md reference it generically and need no change.
CATALOGS = {
    "en": {
        "rules": "ai-tells.md",
        "license": "VALE-AI-TELLS-LICENSE.txt",
        "source": "vale-ai-tells / ai-tells (https://github.com/tbhb/vale-ai-tells, MIT)",
        "name": "English",
    },
    "es": {
        "rules": "es-tells.md",
        # The structure credit (vale-ai-tells, MIT) plus the original-content notice.
        "license": "VALE-AI-TELLS-LICENSE.txt",
        "extra_license": "ES-TELLS-NOTICE.txt",
        "source": "es-tells (hand-authored for this project; taxonomy inspired by "
                  "vale-ai-tells, MIT; content original — see ES-TELLS-NOTICE.txt)",
        "name": "Spanish",
    },
}


def pick_auto_input() -> pathlib.Path:
    """Locate the single document waiting in data/source/."""
    if not DATA_SOURCE.is_dir():
        sys.exit(f"ERROR: no INPUT given and {DATA_SOURCE} does not exist.")
    candidates = sorted(
        p for p in DATA_SOURCE.iterdir() if p.is_file() and not p.name.startswith(".")
    )
    if not candidates:
        sys.exit(f"ERROR: no INPUT given and {DATA_SOURCE} is empty.")
    if len(candidates) > 1:
        listing = "\n".join(f"  - {p.name}" for p in candidates)
        sys.exit(
            f"ERROR: no INPUT given and {DATA_SOURCE} has multiple files; "
            f"pass one explicitly:\n{listing}"
        )
    return candidates[0].resolve()


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def liteparse_version() -> str:
    for args in (["lit", "--version"], ["lit", "-V"]):
        try:
            out = subprocess.run(args, capture_output=True, text=True, timeout=20)
            if out.returncode == 0 and out.stdout.strip():
                return out.stdout.strip()
        except (FileNotFoundError, subprocess.SubprocessError):
            pass
    return "unknown"


def convert(input_path: pathlib.Path, workdir: pathlib.Path) -> str:
    """Return layout-preserved plain text for the input document."""
    if input_path.suffix.lower() in PASSTHROUGH:
        return input_path.read_text(encoding="utf-8", errors="replace")

    if shutil.which("lit") is None:
        sys.exit(
            "ERROR: liteparse ('lit') not found on PATH.\n"
            "Install it with:  pip install liteparse\n"
            "(Office formats also need LibreOffice; images need ImageMagick.)\n"
            "Or pre-extract the text yourself and pass a .txt/.md file instead."
        )
    out_txt = workdir / "liteparse.txt"
    proc = subprocess.run(
        ["lit", "parse", str(input_path), "--format", "text", "-o", str(out_txt)],
        capture_output=True, text=True,
    )
    if proc.returncode != 0:
        sys.exit(f"ERROR: liteparse failed:\n{proc.stderr or proc.stdout}")
    return out_txt.read_text(encoding="utf-8", errors="replace")


def anchor(text: str) -> str:
    """Line-number every line; mark page breaks (form-feed) as [p<n>]."""
    pages = text.split("\f")
    multipage = len(pages) > 1
    lines_out, n = [], 0
    for pi, page in enumerate(pages, 1):
        if multipage:
            lines_out.append(f"\n[p{pi}]")
        for raw in page.splitlines():
            n += 1
            lines_out.append(f"L{n}\t{raw.rstrip()}")
    return "\n".join(lines_out).strip() + "\n"


def fill(template: str, mapping: dict) -> str:
    for k, v in mapping.items():
        template = template.replace("{" + k + "}", v)
    return template


def main():
    ap = argparse.ArgumentParser(description="Build an AI-content review package.")
    ap.add_argument(
        "input", nargs="?",
        help="document to review (pdf/docx/pptx/image/txt/md); "
             "omit to auto-pick the single file in data/source/",
    )
    ap.add_argument("-o", "--output", help="output directory "
                                             "(default: data/processed/<name>-review-package)")
    ap.add_argument("-l", "--lang", choices=sorted(CATALOGS), default="en",
                    help="document language -> tell catalog to use (default: en). "
                         "'es' selects the hand-authored Spanish catalog. "
                         "This picks which static catalog to copy; it does no "
                         "language detection and no scoring.")
    args = ap.parse_args()
    catalog = CATALOGS[args.lang]

    auto = args.input is None
    src = pick_auto_input() if auto else pathlib.Path(args.input).resolve()
    if not src.is_file():
        sys.exit(f"ERROR: input not found: {src}")

    name = src.stem
    out_dir = pathlib.Path(args.output).resolve() if args.output \
        else DATA_PROCESSED / f"{name}-review-package"
    out_dir.mkdir(parents=True, exist_ok=True)
    work = out_dir / ".work"
    work.mkdir(exist_ok=True)

    raw = src.read_bytes()
    text = convert(src, work)
    document_md = (
        f"# Document under review: {src.name}\n\n"
        f"Lines are anchored as `L<n>`; quote these in findings.\n\n"
        f"---\n\n{anchor(text)}"
    )
    (out_dir / "document.md").write_text(document_md, encoding="utf-8")

    # Copy the static criteria + prompt + spec into the package.
    shutil.copy(ASSETS / "rules" / catalog["rules"], out_dir / "rules.md")
    shutil.copy(ASSETS / "rules" / catalog["license"], out_dir / catalog["license"])
    if catalog.get("extra_license"):
        shutil.copy(ASSETS / "rules" / catalog["extra_license"], out_dir / catalog["extra_license"])
    prompt = fill(
        (ASSETS / "templates" / "prompt.md").read_text(encoding="utf-8"),
        {"LANG_NAME": catalog["name"]},
    )
    (out_dir / "prompt.md").write_text(prompt, encoding="utf-8")
    shutil.copy(ASSETS / "templates" / "output-spec.md", out_dir / "output-spec.md")

    readme = fill(
        (ASSETS / "templates" / "package-readme.md").read_text(encoding="utf-8"),
        {"DOC_NAME": src.name, "PACKAGE_DIR": str(out_dir)},
    )
    (out_dir / "README.md").write_text(readme, encoding="utf-8")

    manifest = {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "source_file": src.name,
        "source_sha256": sha256(raw),
        "document_md_sha256": sha256(document_md.encode()),
        "converter": "liteparse" if src.suffix.lower() not in PASSTHROUGH else "passthrough",
        "liteparse_version": liteparse_version() if src.suffix.lower() not in PASSTHROUGH else None,
        "lang": args.lang,
        "catalog": catalog["rules"],
        "rules_source": catalog["source"],
        "line_count": document_md.count("\n"),
    }
    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    shutil.rmtree(work, ignore_errors=True)
    print(f"Package ready: {out_dir}")
    for f in sorted(p.name for p in out_dir.iterdir()):
        print(f"  - {f}")


if __name__ == "__main__":
    main()
