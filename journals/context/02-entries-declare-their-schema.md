# Journal context/02 — journal entries declare their own schema (schema 2)

Status: Executed.
Date: 2026-09-20. Depends on: context/00.
Schema: 2.

## Goal

An entry states the schema it was written under. Today a reader infers that
schema from two facts outside the entry: the footer in `journals/README.md`
and a date comparison. Inference is a heuristic. A declaration is a fact.

This entry defines **schema 2**. Schema 2 is schema 1 plus one rule: an
entry carries a `Schema:` line. The footer stays as the fallback for entries
that carry no line, because nobody rewrites a legacy entry to add one.

## Current state (evidence, verified 2026-09-20)

The schema version lives in one place, at repo scope:

| Site | Holds |
|---|---|
| `journals/README.md:158` | the footer `Schema: 1. Adopted: 2026-09-18.` |
| `journals/README.md:160-163` | the grandfathering rule |
| `templates/journals-README.md:156-163` | the same two, adoption date unfilled |
| `skills/journal-craft/SKILL.md:36-40` | grandfathering, restated for authors |
| `skills/journal-craft/journal-lint.py:55` | `SCHEMA_VERSION = 1` |
| `README.md:74-77` | the one versioned surface in the product |

An entry declares three front-matter lines and no schema:

    # Journal <area>/<NN> — <one-line description>

    Status: <primary>[, <modifier>[, ...]].
    Date: <YYYY-MM-DD>. Depends on: <area>/<NN>.

`journal-lint.py` resolves an entry to schema 1 or to "legacy" by one
comparison: entry date against the single adoption date. Every finding on a
legacy entry drops to a note. The lint holds one global `SCHEMA_VERSION` and
applies it to the whole tree.

Both entries in `journals/context/` date 2026-09-18, the adoption day. Both
are schema 1 by date. Neither says so.

## Gap inventory

| Gap | Severity | Dimension |
|---|---|---|
| An entry does not state its schema. A reader needs the footer and a date comparison to learn it. | high | conventions |
| One footer line holds one adoption date. A second schema bump re-legacies every entry written under the first. | high | conventions |
| The lint infers schema from a date. A backdated or forward-dated entry resolves to the wrong schema, and the lint never says so. | medium | tooling |
| The lint holds one global schema. It cannot check two schema generations in one tree. | medium | tooling |
| A footer newer than the lint stops the whole run. One bad entry should not cost the tree its checks. | low | tooling |
| An entry copied out of its repo loses its schema. Nothing travels with it. | low | conventions |
| A bump dated today collides with an entry written today. The entry resolves to the new schema and draws an error that the no-rewrite rule forbids anyone to fix. | high | installer |
| The reconcile footer step is not idempotent. A second run appends a second line for the same schema. | medium | installer |
| A ledger in ascending order hides its newest line from a lint that takes the first match. An old lint reads a schema-2 repo as schema 1. | medium | tooling |

## Decisions

1. **D1 — An entry declares its schema on its own line.** The grammar is
   `Schema: <N>.` on the fourth front-matter line, directly after the `Date:`
   line. A separate line, not a third field on the `Date:` line: `DATE_LINE_RE`
   and `FOOTER_RE` keep working unchanged, an absent line parses as absent
   instead of forcing a second date-line grammar, and the line mirrors the
   footer it falls back to.
2. **D2 — The footer becomes an append-only adoption ledger.** One line per
   adopted schema, ascending by version and by date:

       Schema: 1. Adopted: 2026-03-01.
       Schema: 2. Adopted: 2026-09-20.

   A bump appends a line. It never edits one. Without the ledger, a bump moves
   the single adoption date forward and turns every compliant entry behind it
   into a legacy entry, which drops its findings to notes. The ledger holds the
   fallback for undeclared entries only. The declaration in D1 outranks it.
3. **D3 — Resolution runs in three steps.** For one entry, the effective
   schema is: (1) the entry's `Schema:` line, when present; (2) otherwise the
   ledger line with the latest adoption date on or before the entry date; (3)
   otherwise legacy, and every finding on the entry drops to a note, as today.
4. **D4 — The declaration is required from schema 2 on.** An entry whose
   effective schema is 2 or higher must carry the line. An entry that resolves
   to schema 1, and any legacy entry, must not be touched. The requirement
   fires from the ledger and is satisfied by the entry, so nothing is circular.
5. **D5 — A forward declaration on one entry is a note.** An entry declaring a
   schema above the lint's maximum gets a note, and the lint skips its other
   checks. The run continues and the exit code does not change. Only the
   ledger keeps the run-wide stop with exit 2, because a ledger the lint does
   not understand invalidates every resolution.
6. **D6 — The lint gates checks on effective schema, not on one global
   number.** `SCHEMA_VERSION` becomes `SCHEMA_MAX`, the highest schema the lint
   understands. A schema-1 repo stays checkable by a schema-2 lint. Schema 2 is
   schema 1 plus one line, so only the new check gates. Keep it that way.
   Divergent per-schema rule sets are a non-goal.
7. **D7 — This entry declares `Schema: 2.` at materialization.** The entry that
   defines schema 2 is written under schema 2 and is the first declaring entry
   in the repo. Under the schema-1 lint the line is an unrecognized extra line
   and passes. After Phase 1 lands the ledger, the line is required and correct.
   The harness runs its own migration on itself.

8. **D8 — An adoption date falls strictly after the newest undeclared
   entry.** A bump computes its date as the later of today and one day after
   the newest date among entries that carry no `Schema:` line. Without this, an
   entry written earlier on the bump day resolves to the new schema, draws the
   J09 "must declare" error, and cannot be fixed, because D4 and the reconcile
   limits forbid touching an entry that exists. Declared entries do not
   constrain the date. They resolve through their own line, not through the
   ledger. For a fresh install the tree is empty and the date is today.
9. **D9 — The ledger append is idempotent and anchored.** A bump appends only
   when no line already declares that version. It appends directly under the
   last `Schema:` line, not at the end of the file. Prose follows the footer in
   `journals/README.md` today. This closes the duplicate-footer defect that
   context/01 recorded against the reconcile step.
10. **D10 — Reconcile copies the skill before it appends the line.** Step 1
    copies `skills/journal-craft/`. Step 2 appends the ledger line. That order
    means a target never holds a ledger its own lint cannot read. The order is
    load-bearing, not incidental, and the prompt states why.

## Execution phases

Ordered. Phase 1 defines the contract. Phases 2 through 6 follow it. Phase 7
gates the close.

### Phase 1 — `journals/README.md`

1. §Entry format, in the shape block: add `Schema: <N>.` as the fourth line.
2. §Entry format notes: add one note. The line states the schema the entry was
   written under. Entries written before schema 2 carry no line.
3. §Schema: replace the body with the ledger, the three-step resolution (D3),
   the requirement (D4), and the no-rewrite rule, unchanged from today.
4. Append the ledger line `Schema: 2. Adopted: 2026-09-20.` directly under
   the existing `Schema: 1. Adopted: 2026-09-18.` line, above the prose that
   follows it. Do not edit the schema-1 line. The date satisfies D8: the newest
   undeclared entry in this repo is context/01, dated 2026-09-18. context/02
   declares its own line and does not constrain the date.

### Phase 2 — `templates/journals-README.md`

Mirror Phase 1 steps 1 through 3. The ledger ships with one line,
`Schema: 2. Adopted: <date>.`, and the installer fills the date. A fresh
target starts at schema 2 and has no schema-1 line.

### Phase 3 — `skills/journal-craft/SKILL.md`

1. Front matter rules: add item 4, the `Schema: <N>.` line, with D1's grammar
   and position.
2. §Grandfathering: restate as resolution. Name the ledger, the three steps,
   and the no-rewrite rule.
3. Change "schema 1" to "schema 2" in the heading of §Writing rules and in the
   front-matter `description`.

### Phase 4 — `skills/journal-craft/journal-lint.py`

1. Rename `SCHEMA_VERSION = 1` to `SCHEMA_MAX = 2`.
2. Add `ENTRY_SCHEMA_RE = re.compile(r"^Schema:\s*(\d+)\s*\.\s*$")`.
3. `lint_readme` collects every `FOOTER_RE` line into a ledger of
   `(version, date, lineno)` instead of taking the first. It returns the
   ledger. J08 gains three cases: a ledger that does not ascend by version is
   an error, a ledger that does not ascend by date is an error, and a repeated
   version is an error. An empty ledger stays the existing J08 error. The
   run-wide notice with exit 2 fires when the highest ledger version exceeds
   `SCHEMA_MAX`. Read the highest version, not the first line, so ledger order
   never changes what the lint concludes.
4. `lint_entry` finds the entry's `Schema:` line by prefix scan across the
   front matter, which ends at the first `## ` heading. It resolves the
   effective schema per D3 before it decides `legacy`, exactly where the date
   comparison sits today.
5. Add check **J09**, entry schema declaration:
   - the line is present but does not parse — error
   - two or more `Schema:` lines in one entry — error
   - the declared version exceeds `SCHEMA_MAX` — note, and skip the entry's
     other checks (D5)
   - the declared version exceeds the highest adopted version in the ledger —
     error, the repo has not adopted it
   - the effective schema is 2 or higher and no line is present — error (D4)
6. Summary line: report the highest adopted version, its adoption date, and
   `SCHEMA_MAX`.
7. Docstring: add J09, restate the inputs, and state the three-step resolution.
8. Exit codes do not change. 1 on errors, 2 on a ledger above `SCHEMA_MAX`, 0
   otherwise.

### Phase 5 — `AGENTS.md`, `templates/AGENTS.md`, `README.md`

1. Both `AGENTS.md` files, Skills table, the `journal-craft` row: "against
   schema 1" becomes "against schema 2".
2. `README.md` §Versioning: state that an entry declares its schema, that the
   ledger in `journals/README.md` is the fallback for undeclared entries, and
   that the lints report a schema above the one they understand.

### Phase 6 — `prompts/harness-init.md` and `prompts/harness-reconcile.md`

1. Init: the footer fill writes one ledger line with the install date. Entries
   the installer writes carry `Schema: 2.`, including the install record. The
   Phase 5 verify bullet names the ledger.
2. Reconcile, probe: record the ledger state. Three cases — no footer, a
   schema-1 footer, a schema-2 ledger.
3. Reconcile, step 2: compute the adoption date per D8, as the later of today
   and one day after the newest undeclared entry. State the computation in the
   step. Then branch. No footer means write one line, which grandfathers the
   whole corpus. A schema-1 footer means append the schema-2 line under it and
   leave the schema-1 line untouched, so no entry loses its schema-1 status. A
   ledger that already declares schema 2 means do nothing (D9).
4. Reconcile, step 1: state that the skill copy precedes the ledger append, and
   why (D10).
5. Reconcile, limits: never add a `Schema:` line to an entry that exists. Never
   edit a ledger line that exists.

### Phase 7 — Verify and close

1. Run `python3 skills/journal-craft/journal-lint.py` from the repo root.
   Expect zero errors.
2. Run `python3 skills/orientation/orientation-lint.py`. Expect zero errors.
3. Run both lints twice. Outputs must match.
4. Append the outcome to this entry's Execution log.

## Verification

- `journals/README.md` carries both ledger lines. The schema-1 line is
  byte-identical to the line that exists today.
- `journals/context/02-entries-declare-their-schema.md` carries `Schema: 2.`
  and lints as a schema-2 entry, not as legacy.
- `journals/context/00-*.md` and `journals/context/01-*.md` carry no `Schema:`
  line, resolve to schema 1 through the ledger, and report zero findings.
- A scratch entry dated today without a `Schema:` line reports one J09 error.
  A scratch entry declaring `Schema: 9.` reports one J09 note and no other
  finding. Delete both after the check.
- A scratch corpus check for the reconcile path: a footer of
  `Schema: 1. Adopted: 2026-03-01.`, one entry dated 2026-02-01, and one dated
  2026-05-01. After the schema-2 line is appended, the first entry reports
  notes and the second reports errors. Neither reports a J09 finding. Discard
  the scratch corpus after the check.
- Appending the schema-2 line a second time is a no-op (D9).
- Both lints exit 0 from the repo root. Double runs print identical output.
- `rg '^SCHEMA_VERSION' skills/` returns nothing.
- `git status` lists exactly the files in the table below. Nothing else.

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
| `prompts/harness-init.md` | edit (Phase 6) |
| `prompts/harness-reconcile.md` | edit (Phase 6) |

## Risk & rollback

- **Ritual cost.** Every new entry carries a number that is almost always the
  repo default. A hand-authored entry will drop it. J09 makes the omission an
  error, not a note, so the lint catches it before the entry lands. The cost is
  one line per entry.
- **Two sources for one fact.** An entry's schema now comes from the entry or
  from the ledger. D3 states the precedence in the contract, not in the tool.
  A reader who never reads the tool still gets the rule.
- **Ledger growth.** One line per schema bump, append-only. At the current rate
  the ledger stays short. Revisit if it passes five lines.
- **Installed targets.** Targets track `main`. A target on schema 1 keeps
  working under a schema-2 lint, because D6 keeps schema-1 checking intact.
  Reconcile appends the schema-2 line when the user runs it. Nothing forces a
  target to move.
- **Old lint, new ledger.** A lint that takes the first footer match reads the
  schema-1 line and never sees the schema-2 line, so it checks a schema-2 repo
  as schema 1 and reports nothing. D10 closes this inside reconcile by copying
  the skill first. The residual case is a lint run from a stale harness tree
  against an already-reconciled target. It under-reports. It never
  mis-reports, because schema 2 is schema 1 plus one line.
- **Rollback.** A git revert in harness. No target holds state this change
  writes, except a ledger line that a schema-1 lint reports as a missing footer
  only if both lines are removed. Reverting removes the appended line and
  restores the schema-1 footer exactly.

## Non-goals

- No rewrite of any entry that exists. context/00 and context/01 stay as they
  are and resolve through the ledger.
- No schema-2 rule beyond the declaration. Schema 2 is schema 1 plus one line.
- No per-schema rule sets in the lint. D6 keeps one rule set, gated in one
  place.
- No schema declaration in `docs/` artifacts or in `orientation-lint.py`. The
  schema governs journal entries only.
- No product version for harness. §Versioning keeps its one exception.
- No retrofit of installed targets beyond what reconcile does when a user runs
  it.
- No change to status grammar, decision numbering, dependency edges, or entry
  numbering.

## Execution log

2026-09-20. Executed on instruction, in the session that materialized the
entry. All seven phases landed. Both lints report zero findings and print
identical output on double runs.

- Phases 1 and 2: `journals/README.md` and `templates/journals-README.md`
  carry the `Schema: <N>.` line in §Entry format, the **Schema line** note,
  and the rewritten §Schema. The harness ledger appended
  `Schema: 2. Adopted: 2026-09-20.` The schema-1 line is untouched. The diff
  on that file adds one ledger line and removes none. The template ships one
  ledger line, `Schema: 2. Adopted: <YYYY-MM-DD>.`
- Phase 3: `skills/journal-craft/SKILL.md` gained front-matter rule 4.
  §Grandfathering became §Schema resolution. The `description` names schema 2.
- Phase 4: `SCHEMA_MAX = 2` replaced `SCHEMA_VERSION`. `lint_readme` returns a
  ledger of `(version, date, iso, lineno)`. Two helpers landed:
  `read_entry_schema` and `resolve_schema`. J08 gained four cases: a bad
  adoption date, a repeated version, versions that do not ascend, and dates
  that do not ascend. J09 landed with five cases. The run-wide notice now
  reads the highest ledger version, not the first line, so ledger order never
  changes what the lint concludes.
- Phase 5: both `AGENTS.md` files name schema 2 and the entry schema line.
  `README.md` §Versioning states the declaration, the ledger, and that the
  lints keep checking older schemas.
- Phase 6: the installer computes the adoption date per D8, writes the
  `Schema:` line into its own install record, and verifies both. The reconcile
  prompt gained the D8 date rule, the D9 idempotent anchored append, and the
  D10 ordering rule with its reason.
- Phase 7: `python3 skills/journal-craft/journal-lint.py` and
  `python3 skills/orientation/orientation-lint.py` both exit 0 with zero
  findings. `grep -rn SCHEMA_VERSION skills/` returns nothing. `git status`
  lists the nine files in the table plus this entry.

Resolution proof on this tree, read through the lint's own helpers:

| Entry | Date | Declares | Resolves to | Legacy |
|---|---|---|---|---|
| context/00 | 2026-09-18 | none | schema 1 | no |
| context/01 | 2026-09-18 | none | schema 1 | no |
| context/02 | 2026-09-20 | 2 | schema 2 | no |

Scratch-corpus checks, all discarded after the run:

- A schema-1 ledger (`Adopted: 2026-03-01.`) with one entry dated 2026-02-01
  and one dated 2026-05-01. The first reports notes. The second reports
  errors. Appending `Schema: 2. Adopted: 2026-09-20.` changed neither. This is
  the D2 guarantee.
- An undeclared entry dated 2026-09-21 reports one J09 error. The same entry
  declaring `Schema: 2.` reports none.
- An entry declaring `Schema: 9.` reports one J09 note and no other finding.
  Its J05 error disappeared, as D5 requires.
- Ledger faults: versions that do not ascend, a repeated version, dates that
  do not ascend, a bad adoption date, and no ledger at all. Each reports its
  J08 error.
- Exit codes: 2 for a ledger above `SCHEMA_MAX`, 1 with errors, 0 when clean.

Gap the entry did not foresee, filled and escalated:

- Reconcile step 2 appended a ledger line but left the target's contract
  text at schema 1. A reconciled target would then run a lint that requires a
  `Schema:` line while its own `journals/README.md` never mentions one. Step 2
  gained sub-steps (e) and (f): replace the §Schema prose and add the line to
  §Entry format, both from `templates/journals-README.md`. This is a judgment
  call made during execution. It needs review.

Fresh-context review round (two reviewer subagents, read-only). One audited
the contract against the tool. One audited the install path against
`/home/san/Workspace/dws/monsoon`, a real target holding 48 entries, a
schema-1 footer, a `Modifiers: In progress.` line, and one entry dated
2026-09-20. Every finding below was reproduced before it was fixed.

Amended decision. D8 was incomplete as written. It constrained the adoption
date against entries only. The lint also requires ledger dates to ascend
strictly, so a bump must clear the previous ledger line as well. **D8 now
reads: an adoption date is the latest of today, one day after the newest
undeclared entry, and one day after the last date in the ledger.** The gap
was reachable, not theoretical: monsoon's own `journals/meta/14` ran on
2026-09-18 and wrote `Adopted: 2026-09-18.`, so any target that ran the
schema-1 install and this reconcile on one day produced a J08 error its own
Limits forbade fixing.

Fixed in `skills/journal-craft/journal-lint.py`:

- J01 ran outside `lint_entry` and still reported errors on an entry that
  declared above `SCHEMA_MAX`, under a note that said "remaining checks
  skipped". This broke D5 and would fail a run for the exact reason D5
  exists. `lint_numbering` now takes the skipped set. A skipped entry keeps
  its place in the number sequence, so no sibling reports a false gap.
- A malformed declaration drew two errors, and the second one was false. The
  "must declare" clause now tests whether the line is absent, not whether the
  version parsed.
- The position rule in D1 was enforced nowhere. J09 now checks that the
  `Schema:` line sits directly after the `Date:` line.
- The front-matter scan ran to end of file on an entry with no section
  heading. It now stops at the blank line that closes the front matter.
- The docstring claimed a forward declaration was "a note on that entry
  alone", which J01 contradicted, and listed four J09 cases against six.

Fixed in the contract, `journals/README.md` and
`templates/journals-README.md`:

- Step 3 of the resolution had two undocumented exceptions. An empty ledger
  and an unparseable date both yield "not legacy". Both are now stated.
- The lint requires dates to ascend strictly. The contract said only
  "Dates ascend". It now says strictly, and says why.
- "Do not add a `Schema:` line to an entry that exists" collided with "fix
  every error before landing the entry", because a draft is already a file on
  disk. The rule now says "already in the record", and states that a draft
  takes the line before it lands. `skills/journal-craft/SKILL.md` carries the
  same correction.

Fixed in `prompts/harness-reconcile.md`:

- Step 1 said "Leave existing skills alone unless missing", which reads as
  "copy only when missing". A target that already holds an older
  `journal-craft` would then get a schema-2 ledger and keep a schema-1 lint,
  which is the state D10 exists to prevent, and it fails silently. The step
  now says to overwrite those two skills and leave *other* skills alone.
- Step 2(b) gained the amended D8 rule.
- Step 2(c) said "do nothing" when schema 2 was already adopted, which reads
  as skipping all of step 2. It now skips the append alone.
- Step 2(e) never said to delete the template's `<YYYY-MM-DD>` placeholder
  ledger line. `FOOTER_RE` cannot parse it, so a surviving placeholder sits
  in the contract and the lint never reports it. The step now deletes it, and
  drops the "The installer fills the adoption date" sentence, which is false
  in a reconciled repo.
- Step 2(f) was the one sub-step with no idempotence guard, against D9. A
  second run appended a second `Schema:` line to the shape block, which the
  lint cannot see.
- Step 2(g) is new. Reconcile synced §Schema and left every other
  error-level rule undocumented in the target. On monsoon that meant the
  contract stayed silent about the decision numbering and dependency rules
  that produce all 59 of its live errors. The step names four sections and
  forbids syncing anything else.
- Step 4 added a Skills row only "when missing", so monsoon's `AGENTS.md`
  would still read "against schema 1" after a correct reconcile. It now
  replaces a row that names an older schema.
- Step 5 now reports the change in finding counts, and names the mass
  downgrade that adopting a schema over a corpus with no ledger causes.
- Step 6 now tells the reconcile record to carry a `Schema:` line, as the
  install record already did.
- Limits: "an entry that exists" became "an entry already in the record", and
  the reconcile record is exempted explicitly.

Fixed in `prompts/harness-init.md`:

- Step 3.1 copied the template over `journals/README.md` unconditionally.
  Simulated on monsoon's corpus, that destroyed the ledger and the
  `Modifiers:` line and took the tree from 59 errors to 0 errors and 243
  notes, exit 0. Total silent loss of checking. The step now branches on the
  probe and routes an existing ledger to reconcile.
- The probe gathered the ledger fact and no step consumed it. Step 3.1 now
  consumes it, and the probe also gathers the last ledger date for the
  amended D8 rule.

Verified after the fixes, on a copy of monsoon's tree under the scratchpad.
monsoon itself was never modified:

- The amended D8 rule computes 2026-09-21 from newest undeclared entry
  2026-09-20, last ledger date 2026-09-18, and today 2026-09-20.
- monsoon's own schema-1 lint on the untouched copy: 59 errors, 206 notes.
- This lint on the reconciled copy: 59 errors, 206 notes. The two finding
  sets are identical line for line. Zero J09 findings. Every error stayed an
  error and every note stayed a note, across 48 real entries. This is the D2
  guarantee measured on a real corpus.

Known, deferred:

- `FOOTER_RE` still matches at any indent (`^\s*`). `MODIFIERS_LINE_RE` is
  anchored at column zero on purpose, so a documentation example never reads
  as a declaration. The ledger now has the same exposure: an indented example
  of a ledger line in a target's `journals/README.md` would be read as a real
  one. No such example exists today in harness or in the template. Anchoring
  `FOOTER_RE` at column zero would break a target whose ledger is indented.
  The change sits outside this entry's scope.
