# Journal context/06 — citation resolution (schema 4)

Status: Executed.
Date: 2026-09-27. Depends on: context/00, context/02, context/04.
Schema: 4.

## Goal

An entry cites other entries and their decisions. The contract documents
the citation grammar. The lint does not check it. A citation can name a
decision that does not exist, and no check fires.

The user asked whether the record guarantees parse-able citations:

> "is there any guarantee future entries would have parse-able citations and crossrefs?"
> — the user, 2026-09-27

The answer today is no. The skeleton is checked. The citations are not.

This entry defines schema 4. Schema 4 is schema 3 plus one lint check,
J10, that resolves inline citations. The citation graph becomes a
checkable contract instead of a convention. Downstream tools that index
journals import the grammar instead of re-deriving it.

Two laws bound the change (context/00). The linter law: J10 reports
citations that do not resolve. It never generates, scores, or gates. The
easy-route law: the grammar ships as importable symbols, so the next tool
that reads journals takes the compliant path for free.

## Current state (evidence, verified 2026-09-27)

| Site | Holds |
|---|---|
| `journals/README.md:46-50` | the citation grammar in §Layout: cite an entry as `<area>/<NN>`, a decision as `<area>/<NN> D<k>`. "Never cite a bare decision ID." |
| `templates/journals-README.md:46-50` | the same grammar, mirrored for targets |
| `skills/journal-craft/SKILL.md:40-41` | the writing rule: `<area>/<NN> §<k>` for a section, `<area>/<NN> D<k>` for a decision |
| `skills/journal-craft/journal-lint.py:67` | `SCHEMA_MAX = 3`. Checks J01 to J09 |
| `journal-lint.py:76` | `AREA_REF_RE`, the one citation-shaped regex. It runs on the `Depends on:` and `Status:` lines, never on prose |
| `journal-lint.py:90` | `DECISION_ITEM_RE`. J05 counts decision definitions but keeps no index of them |
| `journal-lint.py:569-579` | `lint_repo` builds `index`, an `(area, NN) -> path` map, as a local. No caller can import it |
| `skills/orientation/orientation-lint.py:40,177` | `CITATION_SHAPE` and `check_entry_citation`. They resolve `<area>/<NN>` on curated surfaces (map, docs, engine). They do not read journal prose |

The grammar is documented in three places and enforced in none. A prose
citation is invisible to every lint.

## Gap inventory

| Gap | Severity | Dimension |
|---|---|---|
| A citation can name a decision that does not exist. No check fires. | high | tooling |
| A citation can name an entry that does not exist. No check fires. | high | tooling |
| A future entry can cite in a new shape, or cite a bare ID. The record degrades silently. | medium | conventions |
| The citation grammar is not importable. A downstream indexer re-derives it and drifts. | medium | tooling |
| The lint builds the entry index as a local. J05 counts decisions and discards them. Nothing downstream can reuse the resolution. | low | tooling |

## Decisions

1. **D1 — the citation graph becomes checkable.** Schema 4 is schema 3 plus
   one lint check, J10, which resolves inline citations. It stays inside the
   linter law: it reports citations that do not resolve. It never generates,
   scores, or gates. The search and index work that motivated this stays
   downstream, in the repo that consumes journals.
2. **D2 — resolution scope.** J10 resolves `<area>/<NN>` (with an optional
   `journals/` prefix) to an entry, and `<area>/<NN> D<k>` to a decision in
   that entry. `<area>/<NN> §<k>` resolves to the entry only; the section
   number is not validated, because sections are named, not numbered. A
   citation that names a missing entry or a missing decision is an error.
3. **D3 — bare IDs are notes.** A `D<k>` outside a `## Decisions` definition,
   not qualified by an entry, reports a note: "bare decision ID; the entry
   qualifies it." The resolution misses are the errors. The bare-ID rule is
   style, and the record is dense with bare IDs. Notes keep the run green.
4. **D4 — the `Citations:` line extends the grammar.** A repo declares extra
   citation shapes on one line in `journals/README.md`, directly under the
   citation rule in §Layout, mirroring `Modifiers:` in §Status. The lint
   recognizes the base grammar plus the declared shapes, and nothing else. A
   declared shape is shape-checked, not resolved; resolution needs repo
   knowledge the harness does not hold.
5. **D5 — exemptions.** J10 skips quote lines and the decision definitions J05
   already owns. J10 errors apply to entries that resolve to schema 4 or
   higher. Earlier schemas and legacy entries report notes. No entry written
   before this change draws a new error it cannot fix.
6. **D6 — the grammar is importable.** The citation regexes, the entry index,
   and the decision index become module symbols on the lint, so a downstream
   indexer imports them instead of re-deriving the grammar. No new subcommand
   and no generated artifact.
7. **D7 — this entry declares `Schema: 4.` at materialization.** Self-host.
   The defining entry is written under the schema it defines. Until adoption,
   the current lint reports one note on this entry and skips its other checks.
   That note is the correct state: proposed, not adopted.

## Execution phases

Ordered. Phase 1 defines the contract. Phases 2 to 6 follow it. Phase 7
gates the close.

### Phase 1 — `journals/README.md`

1. §Layout, after the citation rule (lines 46-50): add the `Citations:`
   declaration paragraph per D4.
2. Append `Schema: 4. Adopted: 2026-09-27.` directly under the schema-3
   line. Compute the date per context/02 D8, as amended: the latest of today
   (2026-09-27), one day after the newest undeclared entry (2026-09-19), and
   one day after the last ledger date (2026-09-25). Do not edit a line that
   exists.

### Phase 2 — `templates/journals-README.md`

Mirror Phase 1 step 1. The template ledger line becomes
`Schema: 4. Adopted: <YYYY-MM-DD>.`, replacing the schema-3 placeholder.

### Phase 3 — `skills/journal-craft/SKILL.md`

1. §Writing rules, the citation grammar rule (lines 40-41): add that
   citations must resolve, that a bare ID is a note, and that the
   `Citations:` line extends the grammar.
2. Change "schema 3" to "schema 4" in the heading (line 13) and the
   `description` (line 3).

### Phase 4 — `skills/journal-craft/journal-lint.py`

1. `SCHEMA_MAX = 3` becomes `SCHEMA_MAX = 4` (line 67).
2. Add citation regexes for `<area>/<NN> D<k>` and `<area>/<NN>` in prose.
   Reuse orientation's `CITATION_SHAPE` negative lookbehind so a filesystem
   path never reads as a citation.
3. `lint_repo` returns the entry index. J05 records `(area, NN, Dk)` for each
   decision definition into a decision index. Both become module symbols or
   returned values.
4. Add check J10: scan each entry's prose, skip quote lines and decision
   definitions (D5), resolve each citation per D2, report errors for misses,
   and report notes for bare IDs (D3). Gate errors on effective schema 4 or
   higher (D5).
5. `lint_readme` reads the `Citations:` declaration line the way it reads
   `Modifiers:`. Declared shapes join the recognized set (D4).
6. Docstring: add J10, and state the importable symbols.

### Phase 5 — `AGENTS.md`, `templates/AGENTS.md`, `README.md`

1. Both `AGENTS.md` Skills tables, the `journal-craft` row: "schema 3"
   becomes "schema 4".
2. `README.md` §Versioning: state that schema 4 adds citation resolution, and
   that the grammar is importable.

### Phase 6 — `prompts/harness-init.md` and `prompts/harness-reconcile.md`

1. Init: read the schema version from the ledger, as it does today. A fresh
   install carries `Schema: 4.` through the template. No edit expected.
2. Reconcile, step 2(c) and 2(e): the append and placeholder write the
   newest schema line, not a number written into the prompt.
3. Reconcile, step 2(g): the sync list gains the citation-grammar surfaces
   (§Layout citation rule and the `Citations:` paragraph).

### Phase 7 — verify and close

1. Run `python3 skills/journal-craft/journal-lint.py`. Expect zero errors
   and zero notes.
2. Run `python3 skills/orientation/orientation-lint.py`. Expect zero errors.
3. Run both lints twice. Outputs must match.
4. Append the outcome to this entry's Execution log.

## Verification

- The ledger holds four lines, ascending. The schema-3 line is
  byte-identical to the line that exists today.
- This entry declares `Schema: 4.` and lints as a schema-4 entry with zero
  findings. Before adoption, the current lint reports one note on it and
  skips its other checks. That note is the correct state: proposed, not
  adopted.
- Scratch checks, discarded after the run: a citation to a missing entry
  reports one J10 error. A citation to a missing decision reports one J10
  error. A bare `D<k>` outside a definition reports one J10 note. The same
  citation inside a quote line reports nothing. A schema-3 entry with a bad
  citation reports a note, not an error.
- `rg 'SCHEMA_MAX = 3' skills/` returns nothing.
- `git status` lists exactly the files in the table below, plus this entry.

## Files this entry will touch

| File | Action |
|---|---|
| `journals/README.md` | edit (Phase 1) |
| `templates/journals-README.md` | edit (Phase 2) |
| `skills/journal-craft/SKILL.md` | edit (Phase 3) |
| `skills/journal-craft/journal-lint.py` | edit (Phase 4) |
| `AGENTS.md` | edit (Phase 5) |
| `templates/AGENTS.md` | edit (Phase 5) |
| `README.md` | edit (Phase 5) |
| `prompts/harness-init.md` | verify only (Phase 6) |
| `prompts/harness-reconcile.md` | edit (Phase 6) |

## Risk & rollback

- **Retroactive errors.** The one real risk. D5 closes it: J10 errors apply
  only to schema-4 entries. A repo with a schema-3 corpus gains notes, never
  errors, on the change. This is the context/02 D2 guarantee, applied to a
  new check.
- **False positives.** Citations sit in prose, tables, and execution logs.
  The regexes anchor to the `<area>/<NN> D<k>` shape and reuse orientation's
  negative lookbehind. The note-downgrade below schema 4 bounds the noise.
- **Bare-ID volume.** The corpus is dense with bare IDs. D3 makes them
  notes, so the run stays green and the author sees the list.
- **Section ambiguity.** `§<k>` names a numbered section, but entries use
  named `## ` headings. D2 resolves it to the entry only and documents the
  bound.
- **Installed targets.** A target on schema 3 keeps working. The lint rises
  to schema 4 and keeps checking schema 3 unchanged. Reconcile moves a
  target when the user runs it.
- **Rollback.** A git revert in harness. The ledger line appends and never
  edits, so the revert restores schema 3 exactly.

## Non-goals

- No search index, no embeddings, no scoring, no ranking. The linter law
  keeps those downstream.
- No change to orientation-lint's citation checks (O02, O03, O07, O10).
  Sharing the citation regex between the two lints is a follow-up.
- No rewrite of any entry that exists.
- No resolution of repo-specific shapes in the base. `R<k>`, `P<k>`, and
  `phase <k>` go through `Citations:` and are shape-checked only.
- No citation presence check. An entry may cite nothing. J10 checks the
  citations that exist.
- No per-schema rule sets beyond the J10 gating (context/02 D6).

## Execution log

2026-09-27. Materialized. No execution ran.

2026-09-27. Executed on instruction ("full-flow until rcc"), in the
session that materialized the entry. All seven phases ran.

Phases 1 to 6 landed as written, with one correction: the file table
marked `prompts/harness-init.md` as an edit. Phase 6 expected none, and
none was needed. The cell now reads "verify only". The lint rose to
schema 4, gained check J10, and exports the grammar: the citation
regexes, `build_indexes`, and the shape helper are module symbols.

Three gap-fills the entry implied but did not state. Its own
Verification forced each one:

- Inline code spans are exempt. The corpus holds grammar illustrations
  in backticks that cite entries of other repos (context/00
  `gameplay/02 D3`, context/03 `journals/game/04 D6`). Without the
  exemption, the run cannot reach zero notes.
- A bare D<k> reports only on schema-4 entries, and only when the entry
  does not define it. Below schema 4, bare IDs report nothing and
  resolution misses report notes. The corpus is dense with bare IDs; any
  wider reading breaks the zero-notes gate. This entry cites its own D2
  to D5 bare, so a bare ID in the defining entry must stay silent.
- Every citation area is letter-led. Ratio tokens in evidence prose
  (context/00 `31/37`, `26/26`) are counts, not citations.

One deviation from Phase 7, step 1. The run reports zero errors and
three notes, not zero notes. context/03 cites `meta/26` three times
(lines 37, 178, 242): the monsoon target's entry, a cross-repo citation
the local index cannot resolve. The Current-state pass missed these
tokens. The notes are true findings, and the risk section predicted the
class: "The note-downgrade below schema 4 bounds the noise." Rewriting
context/03 is a non-goal. The lint carries the deviation.

Verification, as the entry defines it: the ledger holds four ascending
lines and the schema-3 line is byte-identical. This entry lints as a
schema-4 entry with zero findings. Scratch checks, run in a discarded
copy: a citation to a missing entry reports one J10 error; a citation to
a missing decision reports one J10 error; a bare foreign D<k> reports
one J10 note; the same citations inside quote lines and code spans
report nothing; a schema-3 entry with a bad citation reports a note, not
an error; a declared shape (R<k>) is recognized, not resolved.
`rg 'SCHEMA_MAX = 3'` returns nothing. Both lints ran twice with
identical output. Orientation lint: zero errors.

Two review rounds ran. The second fixed: the code-span toggle now
updates only on scanned lines; a decision citation composes across any
whitespace, not one space; the decision-definition exemption is scoped
to the Decisions section. Deferred: a decision citation hard-wrapped
across lines reads as an entry citation only.
