#!/usr/bin/env python3
"""journal-lint.py — advisory lint for journal entries under schema 1.

Linter law: this tool reports claims that do not resolve. It never writes
files, generates content, scores, ranks, or gates. Findings print one per
line as `<path>:<line> <class> <code> <message>`, then a summary line.

Exit codes: 1 when errors exist, 2 on a schema-version notice, 0 otherwise.
Notes never fail the run.

Usage (from the repo root):

    python3 skills/journal-craft/journal-lint.py

Inputs: the `journals/` tree and `journals/README.md`. The README carries the
schema footer (`Schema: N. Adopted: <date>.`) and the optional `Modifiers:`
line. A footer declaring a schema newer than SCHEMA_VERSION prints a notice
and exits 2 without running the checks. Entries dated before the adoption
date are legacy: every check still runs, but each finding on a legacy entry
is a note, never an error. Without an adoption date nothing is legacy.

Checks:
  J01  filenames (<NN>-<slug>.md, two digits), lowest number is 00 per
       directory (error); numbering gaps after the first entry (note)
  J02  heading parses as "# Journal <area>/<NN> — <description>" and the
       <area>/<NN> matches the file's directory and filename number
  J03  status line is the second non-empty line; primary from the closed
       set; modifiers base or declared; supersession targets resolve
  J04  date/depends line present and parseable; date is ISO 8601; every
       dependency resolves to an entry; "none" is legal
  J05  every "## Decisions" item matches "N. **DN — name.**", sequential
       from 1; bulleted or bold-led items without that numbering are
       unnumbered decision prose (note on legacy entries)
  J06  entry path nests at most one line level under an area (two or
       three path components under journals/)
  J07  dates are ISO 8601 everywhere they appear (the Date line itself is
       J04's; J07 skips it)
  J08  journals/README.md carries the "Schema: N. Adopted: <date>." footer
       with a valid date

Deterministic: two runs on the same tree print identical output. Python 3
standard library only; no network.
"""

import re
import sys
from datetime import date
from pathlib import Path

SCHEMA_VERSION = 1

PRIMARY_STATES = ("Materialized", "Decided", "Executed")
BASE_MODIFIERS = ("Provisional", "On hold")

ENTRY_FILENAME_RE = re.compile(r"^(\d{2})-(.+)\.md$")
HEADING_RE = re.compile(r"^# Journal (.+)/(\d{2}) — (.+)$")
STATUS_RE = re.compile(r"^Status:\s*(.*?)\s*\.\s*$")
SUPERSEDED_RE = re.compile(r"^Superseded by (.+)$")
AREA_REF_RE = re.compile(r"^(.+)/(\d{2})$")
DATE_PREFIX_RE = re.compile(r"^Date:")
DATE_LINE_RE = re.compile(
    r"^Date:\s*(\d{4}-\d{2}-\d{2})\s*\.\s*Depends on:\s*(.*?)\s*\.\s*$")
FOOTER_RE = re.compile(
    r"^\s*Schema:\s*(\d+)\s*\.\s*Adopted:\s*(\d{4}-\d{2}-\d{2})\s*\.\s*$")
# Anchored at column zero: an indented Modifiers line in journals/README.md
# is a documentation example, not a declaration.
MODIFIERS_LINE_RE = re.compile(r"^Modifiers:\s*(.*?)\s*\.?\s*$")
SECTION_HEADING_RE = re.compile(r"^## ")
DECISIONS_HEADING_RE = re.compile(r"^## Decisions\s*$")
NUMBERED_ITEM_RE = re.compile(r"^\s*(\d+)[.)]\s+")
DECISION_ITEM_RE = re.compile(r"^(\d+)[.)]\s+\*\*D(\d+)\s+—\s+\S")
# A line that starts a bold-led item (optionally bulleted) attempts to be a
# decision item; without the "N. " number it is unnumbered decision prose.
# Mid-line "**D<k>" mentions (inline code, citations) are not item starts.
UNNUMBERED_ITEM_RE = re.compile(r"^(?:[-*+]\s+)?\*\*")
ISO_TOKEN_RE = re.compile(r"(?<!\d)(\d{4}-\d{2}-\d{2})(?!\d)")
# Dotted dates read day.month.year; the day and month bounds keep
# version-like tokens (3.14.1592) from matching.
NON_ISO_DATE_RE = re.compile(
    r"\b(\d{4}/\d{1,2}/\d{1,2}"
    r"|\d{1,2}/\d{1,2}/\d{4}"
    r"|(?:0?[1-9]|[12]\d|3[01])\.(?:0?[1-9]|1[0-2])\.\d{4}"
    r"|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.? \d{1,2},? \d{4})\b")

EXCERPT_MAX = 64


def excerpt(line):
    s = line.strip()
    if len(s) > EXCERPT_MAX:
        return s[:EXCERPT_MAX - 3] + "..."
    return s


def iso_date(s):
    """Return a datetime.date for a strict YYYY-MM-DD string, else None."""
    if not ISO_TOKEN_RE.fullmatch(s):
        return None
    try:
        return date(int(s[0:4]), int(s[5:7]), int(s[8:10]))
    except ValueError:
        return None


def display_dir(rel_dir_parts):
    return "journals/" + "/".join(rel_dir_parts) if rel_dir_parts else "journals"


def discover_entries(journals):
    if not journals.is_dir():
        return []
    entries = []
    for p in sorted(journals.rglob("*.md")):
        if p.name == "README.md" or not p.is_file():
            continue
        rel = p.relative_to(journals)
        if any(part.startswith(".") for part in rel.parts):
            continue
        entries.append((p, rel))
    return entries


def lint_readme(readme):
    """Parse journals/README.md.

    Returns (findings, declared_modifiers, adopted_iso, notice). The notice
    is set only when the footer declares a schema newer than SCHEMA_VERSION.
    """
    findings = []
    declared = []
    adopted_iso = None
    notice = None
    if not readme.is_file():
        findings.append({
            "path": "journals/README.md", "line": 0, "code": "J08",
            "cls": "error",
            "msg": 'journals/README.md not found: no schema footer '
                   '("Schema: N. Adopted: YYYY-MM-DD."), adoption date, or '
                   "declared modifiers",
        })
        return findings, declared, adopted_iso, notice
    try:
        text = readme.read_text(encoding="utf-8")
    except OSError:
        findings.append({
            "path": "journals/README.md", "line": 0, "code": "J08",
            "cls": "error",
            "msg": "journals/README.md cannot be read; schema footer and "
                   "declared modifiers unchecked",
        })
        return findings, declared, adopted_iso, notice
    for lineno, line in enumerate(text.splitlines(), 1):
        fm = FOOTER_RE.match(line)
        if fm and adopted_iso is None and notice is None:
            version = int(fm.group(1))
            adopted_iso = fm.group(2)
            if version > SCHEMA_VERSION:
                notice = (
                    f"notice: journals/README.md:{lineno} declares schema "
                    f"{version}, adopted {adopted_iso}; this lint understands "
                    f"schema {SCHEMA_VERSION}")
                continue
            if iso_date(adopted_iso) is None:
                findings.append({
                    "path": "journals/README.md", "line": lineno, "code": "J08",
                    "cls": "error",
                    "msg": f"schema footer adoption date is not a valid ISO 8601 "
                           f"date: {adopted_iso}",
                })
        mm = MODIFIERS_LINE_RE.match(line)
        if mm:
            for name in mm.group(1).split(","):
                name = name.strip()
                if name and name not in declared:
                    declared.append(name)
    if adopted_iso is None and notice is None:
        findings.append({
            "path": "journals/README.md", "line": 0, "code": "J08",
            "cls": "error",
            "msg": 'schema footer missing or malformed (expected '
                   '"Schema: N. Adopted: YYYY-MM-DD.")',
        })
    return findings, declared, adopted_iso, notice


def lint_entry(p, rel, adopted, declared, index):
    """Lint one entry file. Returns (findings, legacy)."""
    rel_dir_parts = rel.parts[:-1]
    rel_dir = "/".join(rel_dir_parts)
    findings = []
    legacy = False

    def add(code, line, msg, cls="error"):
        if cls == "error" and legacy:
            cls = "note"
        findings.append({"path": p.as_posix(), "line": line, "code": code,
                         "cls": cls, "msg": msg})

    try:
        text = p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        add("J02", 1, "entry file is not valid UTF-8; heading unreadable")
        return findings, legacy
    except OSError:
        add("J02", 1, "entry file cannot be read; checks skipped")
        return findings, legacy
    lines = text.splitlines()

    # J04 (part 1) — locate and parse the date line first: the entry date
    # decides legacy status, which downgrades later findings to notes.
    entry_date = None
    date_lineno = None
    date_line = None
    for i, line in enumerate(lines):
        if DATE_PREFIX_RE.match(line):
            date_lineno, date_line = i + 1, line
            break
    if date_line is None:
        add("J04", 0, 'date line missing (expected '
                      '"Date: <YYYY-MM-DD>. Depends on: <area>/<NN>.")')
    else:
        dm = DATE_LINE_RE.match(date_line)
        if not dm:
            add("J04", date_lineno, f"date line does not parse: {excerpt(date_line)}")
        else:
            entry_date = iso_date(dm.group(1))
            if entry_date is None:
                add("J04", date_lineno,
                    f"date is not a valid ISO 8601 date: {dm.group(1)}")

    if adopted is not None and entry_date is not None and entry_date < adopted:
        legacy = True

    # J04 (part 2) — dependency targets.
    if date_line is not None:
        dm = DATE_LINE_RE.match(date_line)
        if dm:
            deps = dm.group(2).strip()
            if deps == "none":
                pass
            else:
                for item in (s.strip() for s in deps.split(",")):
                    if not item:
                        add("J04", date_lineno,
                            f"date line does not parse: {excerpt(date_line)}")
                        continue
                    am = AREA_REF_RE.match(item)
                    if not am:
                        add("J04", date_lineno,
                            f'dependency does not parse as "<area>/<NN>": {item}')
                    elif (am.group(1), am.group(2)) not in index:
                        add("J04", date_lineno,
                            f"dependency does not resolve: {item}")

    # J06 — one line level under an area: two components (area + file) or
    # three (area + line + file). One or four-plus components is an error.
    if len(rel.parts) not in (2, 3):
        add("J06", 1,
            f"entry path must nest at most one line level under an area "
            f"(two or three path components under journals/), found "
            f"{len(rel.parts)}")

    # J02 — heading parses and matches the file's path.
    heading = lines[0] if lines else ""
    hm = HEADING_RE.match(heading)
    if not hm:
        shown = excerpt(heading) if heading.strip() else "(missing)"
        add("J02", 1, 'heading does not parse as '
                      '"# Journal <area>/<NN> — <description>": '
                      f"{shown}")
    else:
        heading_area, heading_nn = hm.group(1), hm.group(2)
        fnm = ENTRY_FILENAME_RE.match(p.name)
        if fnm is None:
            add("J02", 1, f'heading parses but the filename lacks the '
                          f'"<NN>-" prefix ("<NN>-<slug>.md"): {p.name}')
        elif heading_area != rel_dir or heading_nn != fnm.group(1):
            add("J02", 1, f"heading does not match entry path: expected "
                          f"{rel_dir}/{fnm.group(1)}, found "
                          f"{heading_area}/{heading_nn}")

    # J03 — status line is the second non-empty line.
    nonempty = [(i + 1, line) for i, line in enumerate(lines) if line.strip()]
    if len(nonempty) < 2:
        add("J03", nonempty[-1][0] if nonempty else max(len(lines), 1),
            'status line missing (the second non-empty line must be '
            '"Status: ...")')
    else:
        status_lineno, status_line = nonempty[1]
        sm = STATUS_RE.match(status_line)
        if not sm or not sm.group(1).strip():
            add("J03", status_lineno,
                f"status line does not parse: {excerpt(status_line)}")
        else:
            items = [it.strip() for it in sm.group(1).strip().split(",")]
            primary, modifiers = items[0], items[1:]
            if primary not in PRIMARY_STATES:
                add("J03", status_lineno,
                    f"unknown primary state: {primary} (expected one of "
                    f"{', '.join(PRIMARY_STATES)})")
            for it in modifiers:
                if not it:
                    add("J03", status_lineno,
                        f"status line does not parse: {excerpt(status_line)}")
                elif it in PRIMARY_STATES:
                    add("J03", status_lineno, f"primary state must come first: {it}")
                elif it in BASE_MODIFIERS or it in declared:
                    continue
                else:
                    um = SUPERSEDED_RE.match(it)
                    if not um:
                        add("J03", status_lineno, f"unknown status modifier: {it}")
                        continue
                    ref = um.group(1).strip()
                    am = AREA_REF_RE.match(ref)
                    if not am:
                        add("J03", status_lineno,
                            f'supersession target does not parse as '
                            f'"<area>/<NN>": {ref}')
                    elif (am.group(1), am.group(2)) not in index:
                        add("J03", status_lineno,
                            f"supersession target does not resolve: {ref}")

    # J05 — Decisions numbering.
    dec_start = None
    for i, line in enumerate(lines):
        if DECISIONS_HEADING_RE.match(line):
            dec_start = i
            break
    if dec_start is not None:
        section = []
        j = dec_start + 1
        while j < len(lines) and not SECTION_HEADING_RE.match(lines[j]):
            section.append((j + 1, lines[j]))
            j += 1
        seq = 0
        unnumbered = []
        for lineno, line in section:
            s = line.strip()
            if not s:
                continue
            nm = NUMBERED_ITEM_RE.match(line)
            if nm:
                seq += 1
                dm2 = DECISION_ITEM_RE.match(s)
                if not dm2:
                    add("J05", lineno, 'decision item does not match '
                                       '"N. **DN — name.**": '
                                       f"{excerpt(line)}")
                elif int(dm2.group(1)) != seq:
                    add("J05", lineno, f"decision numbering out of sequence: "
                                       f"expected {seq}, found {dm2.group(1)}")
                elif int(dm2.group(2)) != seq:
                    add("J05", lineno, f"decision number D{dm2.group(2)} does "
                                       f"not match item position {seq}")
            elif UNNUMBERED_ITEM_RE.match(s):
                unnumbered.append((lineno, s))
        if unnumbered:
            if legacy:
                add("J05", unnumbered[0][0],
                    "legacy entry: decisions unnumbered", cls="note")
            else:
                for lineno, s in unnumbered:
                    add("J05", lineno, f"decision item is unnumbered: {excerpt(s)}")

    # J07 — dates are ISO 8601 everywhere they appear. The Date line is
    # J04's; J07 skips it to avoid double-reporting.
    for i, line in enumerate(lines):
        if date_lineno is not None and i + 1 == date_lineno:
            continue
        for m in ISO_TOKEN_RE.finditer(line):
            if iso_date(m.group(1)) is None:
                add("J07", i + 1,
                    f"date is not a valid ISO 8601 date: {m.group(1)}")
        for m in NON_ISO_DATE_RE.finditer(line):
            add("J07", i + 1,
                f"date not in ISO 8601 (YYYY-MM-DD): {m.group(1)}")

    return findings, legacy


def lint_numbering(entries, legacy_by_path):
    """J01 — filenames, lowest number 00 per directory, gap notes."""
    findings = []
    dirs = {}
    for p, rel in entries:
        dirs.setdefault(rel.parts[:-1], []).append((p, rel))
    for dir_parts in sorted(dirs):
        matches = []
        for p, rel in sorted(dirs[dir_parts], key=lambda t: t[0].name):
            fm = ENTRY_FILENAME_RE.match(p.name)
            if fm is None:
                cls = "note" if legacy_by_path.get(p.as_posix(), False) else "error"
                findings.append({
                    "path": p.as_posix(), "line": 1, "code": "J01", "cls": cls,
                    "msg": f'filename does not match "<NN>-<slug>.md": {p.name}',
                })
            else:
                matches.append((int(fm.group(1)), p, fm.group(1)))
        if not matches:
            continue
        matches.sort(key=lambda t: t[0])
        lowest_n, lowest_p, lowest_s = matches[0]
        if lowest_n != 0:
            cls = ("note"
                   if legacy_by_path.get(lowest_p.as_posix(), False) else "error")
            findings.append({
                "path": lowest_p.as_posix(), "line": 1, "code": "J01", "cls": cls,
                "msg": f"lowest entry number in {display_dir(dir_parts)} is "
                       f"{lowest_s}, expected 00",
            })
        prev = None
        for n, p, nstr in matches:
            if prev is not None and n > prev + 1:
                missing = ", ".join(f"{k:02d}" for k in range(prev + 1, n))
                findings.append({
                    "path": p.as_posix(), "line": 1, "code": "J01", "cls": "note",
                    "msg": f"numbering gap in {display_dir(dir_parts)}: "
                           f"{missing} missing",
                })
            prev = n
    return findings


def lint_repo(root):
    journals = root / "journals"
    readme_findings, declared, adopted_iso, notice = lint_readme(journals / "README.md")
    if notice is not None:
        return readme_findings, adopted_iso, notice
    adopted = iso_date(adopted_iso) if adopted_iso else None
    entries = discover_entries(journals)
    index = {}
    for p, rel in entries:
        fm = ENTRY_FILENAME_RE.match(p.name)
        if fm:
            index[("/".join(rel.parts[:-1]), fm.group(1))] = p
    findings = list(readme_findings)
    legacy_by_path = {}
    for p, rel in entries:
        entry_findings, legacy = lint_entry(p, rel, adopted, declared, index)
        legacy_by_path[p.as_posix()] = legacy
        findings.extend(entry_findings)
    findings.extend(lint_numbering(entries, legacy_by_path))
    return findings, adopted_iso, notice


def main():
    findings, adopted_iso, notice = lint_repo(Path.cwd())
    if notice is not None:
        print(notice)
        return 2
    findings.sort(key=lambda f: (f["path"], f["line"], f["code"], f["msg"]))
    for f in findings:
        print(f'{f["path"]}:{f["line"]} {f["cls"]:<5} {f["code"]} {f["msg"]}')
    errors = sum(1 for f in findings if f["cls"] == "error")
    notes = sum(1 for f in findings if f["cls"] == "note")
    print(f"summary: {errors} error{'' if errors == 1 else 's'}, "
          f"{notes} note{'' if notes == 1 else 's'} "
          f"(schema {SCHEMA_VERSION}, adopted {adopted_iso or 'date not found'})")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
