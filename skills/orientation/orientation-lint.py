#!/usr/bin/env python3
"""orientation-lint — advisory claim-resolution lint for the orientation layer.

Checks curated claims: backticked paths in Repository/Local map tables,
vocabulary-bridge citations, `<area>/<NN>` journal citations in map and
where-truth-lives tables, map line budgets, nested-map row duplication,
relative links, `Derived from:` targets, and section `From` targets in
`docs/`, superseded `From` targets, and the map negative-list line.

Advisory only: it reports claims that do not resolve. It never writes,
scores, or gates. Errors exit 1; warnings never fail.

Standard library only. Deterministic: two runs on the same tree print
identical output.
"""

import glob as globmod
import os
import re
import subprocess
import sys

# The fallback walk never enters these (git discovery needs no list).
SKIP_DIR_NAMES = {".git", ".agents", ".pi", ".pi-subagents", "node_modules", ".venv"}
SKIP_DIR_PATHS = {"docs/godot-api"}

BUDGET_ROOT_MAP = 40
BUDGET_NESTED_FILE = 15
NEGATIVE_LIST = "never carries decisions, answers, or generated text"

# <area>/<NN> entry citation: optional journals/ prefix, optional -slug/.md.
# Sentence punctuation after the citation is allowed; a longer path or a
# non-.md extension is not.
REF_RE = re.compile(
    r"(?<![\w./-])(?:journals/)?"
    r"([A-Za-z0-9][A-Za-z0-9_-]*(?:/[A-Za-z0-9][A-Za-z0-9_-]*)*)"
    r"/(\d{2})(?:-[A-Za-z0-9][A-Za-z0-9_-]*)*(?:\.md)?(?![\w/-])(?!\.[A-Za-z0-9])"
)
# A token in citation shape is a journal reference, not a filesystem path.
CITATION_SHAPE = re.compile(
    r"^(?:journals/)?[A-Za-z0-9][A-Za-z0-9_-]*"
    r"(?:/[A-Za-z0-9][A-Za-z0-9_-]*)*/\d{2}(?:-[A-Za-z0-9][A-Za-z0-9_-]*)*(?:\.md)?$"
)
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
EXT_RE = re.compile(r"\.[A-Za-z0-9]+$")
SEP_CELL_RE = re.compile(r"^:?-{2,}:?$")


def find_text(root, rel):
    """Read a repo file; return '' when missing."""
    try:
        with open(os.path.join(root, rel), encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except OSError:
        return ""


def generated_doc_dirs(root):
    """The `docs/<dir>/` names the repo's docs README declares generated."""
    names = set()
    for m in re.finditer(r"\bdocs/([A-Za-z0-9][\w.-]*)/", find_text(root, "docs/README.md")):
        names.add(m.group(1))
    return names


def fallback_walk(root):
    skip_paths = SKIP_DIR_PATHS | {f"docs/{n}" for n in generated_doc_dirs(root)}
    out = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(
            d for d in dirnames
            if d not in SKIP_DIR_NAMES
            and os.path.relpath(os.path.join(dirpath, d), root).replace(os.sep, "/")
            not in skip_paths
        )
        for fn in filenames:
            out.append(os.path.relpath(os.path.join(dirpath, fn), root).replace(os.sep, "/"))
    return sorted(out)


def discover(root):
    """Tracked files via git ls-files; fallback walk when git is unusable."""
    try:
        res = subprocess.run(
            ["git", "-C", root, "ls-files", "-z"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        if res.returncode == 0:
            return sorted(p for p in res.stdout.decode("utf-8", "replace").split("\0") if p)
    except OSError:
        pass
    return fallback_walk(root)


def norm_title(title):
    return re.sub(r"\s+", " ", title.strip().lower().replace("-", " ").replace("_", " "))


def parse_sections(lines):
    """Yield (title, start0, end0) half-open, 0-based, per '## ' section."""
    starts = [(i, ln[3:].strip()) for i, ln in enumerate(lines) if ln.startswith("## ")]
    for k, (i, title) in enumerate(starts):
        end = starts[k + 1][0] if k + 1 < len(starts) else len(lines)
        yield title, i, end


def split_row(line):
    s = line.strip()
    if not s.startswith("|"):
        return None
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s[1:].split("|")]


def is_separator(cells):
    return bool(cells) and all(SEP_CELL_RE.match(c) or not c for c in cells)


def walk_tables(lines, start, end):
    """Yield (in_vocabulary_subsection, rows); rows are (lineno, cells)."""
    sub = ""
    i = start
    while i < end:
        ln = lines[i]
        if ln.startswith("### "):
            sub = norm_title(ln[4:])
            i += 1
        elif ln.lstrip().startswith("|"):
            j, rows = i, []
            while j < end and lines[j].lstrip().startswith("|"):
                cells = split_row(lines[j])
                if cells and not is_separator(cells):
                    rows.append((j + 1, cells))
                j += 1
            yield sub in ("vocabulary bridge", "local vocabulary"), rows
            i = j
        else:
            i += 1


def norm_row(cells):
    return tuple(re.sub(r"\s+", " ", c) for c in cells)


def backticked(text):
    return re.findall(r"`([^`\n]+)`", text)


def looks_like_path(tok):
    if not tok or re.search(r"\s", tok):
        return False
    if any(c in tok for c in "<>*|"):
        return False
    if tok.startswith(("http://", "https://", "mailto:")):
        return False
    return "/" in tok or bool(EXT_RE.search(tok))


def path_resolves(root, tok):
    t = tok.rstrip("/")
    if t.startswith("./"):
        t = t[2:]
    if not t or t.startswith("../"):
        return False
    return os.path.exists(os.path.join(root, t))


def entry_exists(root, area, nn):
    area = area.split("/", 1)[1] if area.startswith("journals/") else area
    base = os.path.join(root, "journals", *area.split("/"))
    for pat in (os.path.join(base, nn + "-*.md"), os.path.join(base, nn + ".md")):
        if globmod.glob(pat):
            return True
    return False


def check_entry_citation(root, rel, lineno, text, code, label, add):
    for m in REF_RE.finditer(text):
        if not entry_exists(root, m.group(1), m.group(2)):
            add(rel, lineno, code, "error",
                f"{label} does not resolve to a journal entry: {m.group(0)}")


def entry_status(root, area, nn):
    """The entry's `Status:` line, or '' when the entry has none."""
    area = area.split("/", 1)[1] if area.startswith("journals/") else area
    base = os.path.join(root, "journals", *area.split("/"))
    paths = sorted(globmod.glob(os.path.join(base, nn + "-*.md")))
    paths += sorted(globmod.glob(os.path.join(base, nn + ".md")))
    for path in paths:
        for line in find_text(root, os.path.relpath(path, root)).splitlines()[:6]:
            if line.startswith("Status:"):
                return line
    return ""


def check_live_from(root, rel, lineno, text, add):
    """A `From` target names the successor, never a superseded entry.

    `Derived from:` headers are exempt: a header records a commission,
    which stays true after the commissioning entry is superseded.
    """
    for m in REF_RE.finditer(text):
        status = entry_status(root, m.group(1), m.group(2))
        if "Superseded by" in status:
            add(rel, lineno, "O09", "warning",
                f"From target is superseded: {m.group(0)} ({status})")


def path_claims(row):
    """Backticked tokens that claim to be repo paths (citations excluded)."""
    return [t for t in backticked(row)
            if looks_like_path(t) and not CITATION_SHAPE.match(t)]


def check_zone_row(root, rel, lineno, cells, add):
    row = " | ".join(cells)
    for tok in path_claims(row):
        if not path_resolves(root, tok):
            add(rel, lineno, "O01", "error", f"backticked path does not resolve: `{tok}`")
    check_entry_citation(root, rel, lineno, row, "O03", "citation", add)


def check_vocab_row(root, rel, lineno, cells, add):
    row = " | ".join(cells)
    for tok in path_claims(row):
        if not path_resolves(root, tok):
            add(rel, lineno, "O02", "error", f"vocabulary citation does not resolve: `{tok}`")
    check_entry_citation(root, rel, lineno, row, "O02", "vocabulary citation", add)


def starts_from_line(line):
    """A section `From` line: `From ` at column 0, then an entry citation."""
    return line.startswith("From ") and REF_RE.match(line, 5) is not None


def ends_from_paragraph(line):
    """A blank line or a block marker closes a `From` paragraph."""
    return line.strip() == "" or line.lstrip().startswith(("|", "-", "*", "#", ">"))


def strip_inline_code(line):
    return re.sub(r"`[^`]*`", "", line)


def check_doc(root, rel, add):
    """O06 relative links, O07 provenance targets, O09 superseded targets."""
    text = find_text(root, rel)
    if not text:
        return
    base = os.path.dirname(rel)
    in_fence = False
    in_from = False
    for i, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            in_from = False
            continue
        if in_fence:
            continue
        # A `From` line may wrap, so its paragraph runs to the next blank
        # line or block marker.
        in_from = starts_from_line(line) or (in_from and not ends_from_paragraph(line))
        # O07 takes its tail from the raw line: strip_inline_code deletes a
        # backticked target before it can be checked.
        derived = (line.split("Derived from:", 1)[1]
                   if "Derived from:" in line else None)
        prose = strip_inline_code(line)
        for m in LINK_RE.finditer(prose):
            tgt = m.group(1)
            if tgt.startswith(("http://", "https://", "mailto:", "#", "/")):
                continue
            tgt = tgt.split("#", 1)[0]
            if not tgt:
                continue
            full = os.path.normpath(os.path.join(root, base, tgt))
            if not os.path.exists(full):
                add(rel, i, "O06", "error", f"relative link does not resolve: {tgt}")
        if derived is not None:
            check_entry_citation(root, rel, i, derived, "O07", "Derived from target", add)
        elif in_from:
            check_entry_citation(root, rel, i, line, "O07", "From target", add)
            check_live_from(root, rel, i, line, add)


def main(argv):
    root = os.path.abspath(argv[0]) if argv else os.getcwd()
    files = discover(root)
    # Shipped templates are not installed nested maps.
    agents = [f for f in files
              if os.path.basename(f) == "AGENTS.md"
              and not f.startswith("templates/")]
    docs = sorted(f for f in files if f.startswith("docs/") and f.endswith(".md"))
    # Root first so nested-row duplication has its comparison set.
    agents = [f for f in agents if f == "AGENTS.md"] + sorted(f for f in agents if f != "AGENTS.md")

    findings = []

    def add(path, line, code, cls, msg):
        findings.append((path, line, code, cls, msg))

    root_zone_rows = None
    root_vocab_rows = None

    for rel in agents:
        text = find_text(root, rel)
        if not text:
            continue
        lines = text.splitlines()
        is_root = rel == "AGENTS.md"
        if not is_root and len(lines) > BUDGET_NESTED_FILE:
            add(rel, 1, "O04", "warning",
                f"nested AGENTS.md exceeds {BUDGET_NESTED_FILE} lines ({len(lines)})")
        flat = re.sub(r"\s+", " ", text)
        for title, s, e in parse_sections(lines):
            t = norm_title(title)
            if t in ("repository map", "local map"):
                if t == "repository map":
                    if is_root and e - s > BUDGET_ROOT_MAP:
                        add(rel, s + 1, "O04", "warning",
                            f"repository map section exceeds {BUDGET_ROOT_MAP} lines ({e - s})")
                    if NEGATIVE_LIST not in flat:
                        add(rel, s + 1, "O08", "warning",
                            "repository map missing the negative-list line")
                for vocab, rows in walk_tables(lines, s, e):
                    if vocab:
                        for lineno, cells in rows:
                            check_vocab_row(root, rel, lineno, cells, add)
                    else:
                        for lineno, cells in rows:
                            check_zone_row(root, rel, lineno, cells, add)
                    # Data rows only: header shapes match across files
                    # by construction and say nothing about the map. Zone
                    # and vocabulary rows compare within their own kind.
                    data_rows = rows[1:]
                    if is_root and t == "repository map":
                        bucket = root_vocab_rows if vocab else root_zone_rows
                        if bucket is None:
                            bucket = set()
                            if vocab:
                                root_vocab_rows = bucket
                            else:
                                root_zone_rows = bucket
                        bucket.update(norm_row(c) for _, c in data_rows)
                    elif not is_root:
                        bucket = root_vocab_rows if vocab else root_zone_rows
                        for lineno, cells in data_rows:
                            if bucket and norm_row(cells) in bucket:
                                add(rel, lineno, "O05", "warning",
                                    "local map row duplicates root map row")
            elif t == "where truth lives":
                for _, rows in walk_tables(lines, s, e):
                    for lineno, cells in rows:
                        check_entry_citation(root, rel, lineno, " | ".join(cells),
                                             "O03", "citation", add)

    for rel in docs:
        check_doc(root, rel, add)

    findings.sort(key=lambda f: (f[0], f[1], f[2]))
    errors = sum(1 for f in findings if f[3] == "error")
    warnings = len(findings) - errors
    for path, line, code, cls, msg in findings:
        print(f"{path}:{line} {cls:<5} {code} {msg}")
    print(f"summary: {errors} error{'' if errors == 1 else 's'}, "
          f"{warnings} warning{'' if warnings == 1 else 's'}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
