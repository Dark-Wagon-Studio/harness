# Journal context/03 — doc provenance moves from the header to the section

Status: Executed.
Date: 2026-09-22. Depends on: context/00.
Schema: 2.

## Goal

Stop the provenance of an authored doc from growing as a list at the top
of the doc. Each numbered section names its own source entries on a
`From` line. Topic docs and `docs/index.md` carry no `Derived from:`
header. The orientation lint checks `From` targets and warns when one is
superseded. Installed targets get the contract and the lint through
reconcile, and they migrate their docs through their own journal entry.

## Current state (evidence, verified 2026-09-22)

Verified on harness main at 813bbbd.

- `templates/docs-README.md` §Provenance: "An authored doc opens with
  `Derived from:` — the journal entries whose decisions it reflects."
  §Lifecycle: "Update an authored doc in place when an executed entry
  changes the model it describes." No rule removes a header entry. The
  harness self-hosted `docs/README.md` is byte-identical.
- The same template gives `docs/index.md` a header "when it first
  projects a journal entry". The index projects no decisions.
- §Format contract already names the section as the citation unit:
  "Numbered sections (`## 3. Retreat`). The section is the citation
  unit."
- `AGENTS.md:110` and `templates/AGENTS.md:98`: "The "orientation" lint
  checks "Derived from:" targets and doc links."
- `skills/orientation/orientation-lint.py` O07 checks `Derived from:`
  targets only. It reads no entry status.
- `prompts/harness-reconcile.md` step 1 overwrites the target's
  `skills/orientation/`. No step touches the target's `docs/README.md`.

Field evidence from the monsoon target, journal entry meta/26 in that
repo (commits 908280c, 9ba9189):

- Header size tracked the commit count on each doc: the index held 30
  entries over 45 commits, the economy doc 12 over 12, the battle doc 11
  over 13.
- Sections that cited nothing depended on the header alone.
- Headers and `From` lines named superseded entries.
- The migration took a per-section audit: `git blame` on the section,
  then a read of each candidate diff. A rename-only edit was not a
  source. One citation had no carrier and escalated to the human.
- Monsoon's first O09 exempted `docs/research/` by path. A research
  header names the entry that commissioned the doc, which stays true
  after supersession. Upstream cannot name a target path.

## Gap inventory

| Gap | Severity | Dimension |
| --- | --- | --- |
| No rule removes a header entry, so headers grow per execution | high | docs |
| The index template carries a header with no decisions under it | medium | docs |
| The lint does not check section provenance or supersession | medium | tools |
| Reconcile has no path for a provenance contract change | medium | infra |
| No procedure migrates a target's existing headers | medium | infra |

## Decisions

1. **D1 — no header on topic docs.** A topic doc carries no
   `Derived from:` line.
2. **D2 — every section opens with a From line.** Each numbered section
   of a topic doc opens with `From <entry>[, <entry>].`, as plain `From `
   at column 0 and its own paragraph. The line may attribute parts after
   the first citation. It names the entries whose decisions the section
   states now. It is not a record of edits. An edit to a section updates
   its line.
3. **D3 — provenance names live entries.** A `From` line and an inline
   decision citation never name an entry with a `Superseded by`
   modifier. They name the successor that carries the decision.
4. **D4 — single-source docs keep a header.** A doc whose whole body
   derives from the entries that commissioned it, such as an
   investigation, opens with `Derived from:` naming those entries, in
   place of section `From` lines. The header records the commission,
   which stays true after supersession.
5. **D5 — the index carries no provenance line.** `docs/index.md`
   projects no decisions. Its bullets may name entries in prose.
6. **D6 — the lint.** A `From` paragraph starts at a line with `From `
   at column 0 and an entry citation. It ends at a blank line, a block
   marker, or a code fence. O07 checks its targets as it checks
   `Derived from:` targets. A new check O09 warns when a `From` target
   carries `Superseded by`. O09 never reads a `Derived from:` header (D4), so the lint names no
   target path. O09 is a warning, never an error.
7. **D7 — reconcile patches the contract, not the docs.** Reconcile
   syncs the §Provenance and §Lifecycle rules into the target's
   `docs/README.md`. It does not recut authored docs. A doc recut is a
   design act, so the target runs it as its own journal entry.
8. **D8 — a migration prompt.** `prompts/provenance-migrate.md` holds
   the procedure a target entry follows: list the sections, find the
   sources, write the `From` lines, replace superseded citations,
   escalate what has no source, remove the headers, and run the lint.
   An entry is a section source when its execution wrote rule text the
   section still holds, or when the section cites one of its decisions
   as a rule. A rename-only edit and a blank line are not sources.

## Execution phases

1. **Contract.** Rewrite §Provenance and add the §Lifecycle rule in
   `templates/docs-README.md` per D1 through D5. Copy the result to the
   harness `docs/README.md`. Write with the `ste-writing` skill.
2. **Entry point.** Change the lint sentence at `AGENTS.md:110` and
   `templates/AGENTS.md:98` to name `From` and `Derived from:` targets.
3. **Lint.** Extend `skills/orientation/orientation-lint.py` per D6.
   Update the §Checking text of `skills/orientation/SKILL.md`.
4. **Reconcile.** In `prompts/harness-reconcile.md`, add a probe for
   `Derived from:` headers on topic docs and the index. Add a step that
   syncs §Provenance and §Lifecycle per D7 and points the user at the
   migration prompt when headers exist. Add the file to the step 5
   touched set.
5. **Migration prompt.** Write `prompts/provenance-migrate.md` per D8.
   List it in the `README.md` file table.
6. **Check and land.** Run the checks in Verification. Commit as
   `harness: section From lines replace doc provenance headers`. Push
   to origin main.

## Verification

- `templates/docs-README.md` and `docs/README.md` are byte-identical.
- `python3 skills/orientation/orientation-lint.py` on the harness tree
  prints the same findings before and after, and two runs print the
  same output.
- A scratch-root test shows O07 reports an unknown `From` target on a
  wrapped line, O09 reports a superseded `From` target, and O09 stays
  silent on a `Derived from:` header that names a superseded entry.
- The lint run against the monsoon tree prints the findings of the
  monsoon copy, minus nothing and plus nothing.
- `python3 skills/journal-craft/journal-lint.py` reports no error on
  this entry.
- A fresh-context review subagent reads the full diff against this
  entry. The executor fixes each finding or records it in the execution
  log.

## Files this entry will touch

- `templates/docs-README.md`, `docs/README.md` — §Provenance,
  §Lifecycle.
- `AGENTS.md`, `templates/AGENTS.md` — the lint sentence.
- `skills/orientation/orientation-lint.py`, `skills/orientation/SKILL.md`.
- `prompts/harness-reconcile.md` — opening condition, probe, steps 4
  and 5, renumbered steps, Limits.
- `prompts/provenance-migrate.md` — new.
- `README.md` — file table row.
- `.gitignore` — `__pycache__/`.
- `journals/context/03-section-provenance.md` — status and log.

## Risk & rollback

- **Old targets.** A target that has not migrated keeps its headers.
  O07 still resolves them, and O09 never reads them, so the new lint
  adds no finding there. Reconcile can copy the lint before the target
  migrates.
- **Longer From lines.** A section can collect sources. The growth stays
  inside one section, next to the change, and D2 removes a source that
  no longer rules the section.
- **Rollback.** `git revert` of the commit.

## Non-goals

- No change to targets from this entry. Monsoon picks up the lint
  through reconcile.
- No lint check for inline citations outside a `From` paragraph.
- No lint check that every numbered section has a `From` line.
- No change to the monsoon commit grammar or its adoption upstream.

## Execution log

**P1 — contract.** `templates/docs-README.md` §Provenance states D1
through D5, and §Lifecycle gains the `From` line update rule. The harness
`docs/README.md` is a byte copy.

**P2 — entry point.** `AGENTS.md` and `templates/AGENTS.md` name `From`
and `Derived from:` targets in the lint sentence.

**P3 — lint.** `orientation-lint.py` starts from the monsoon meta/26 copy.
O09 reads `From` paragraphs only, so the monsoon `docs/research/` path
exemption is gone. `SKILL.md` §Checking names both targets and the O09
warning.

**P4 — reconcile.** A probe line finds header docs. A new step 5 syncs
§Provenance and the §Lifecycle rule. Later steps renumber to 6 and 7,
with their cross-references.

**P5 — migration prompt.** `prompts/provenance-migrate.md` lands with
the D8 source rule and seven steps. `README.md` lists it.

**Review round.** A fresh-context subagent reviewed the diff. It found
seven defects. The executor fixed all seven:

1. The lint read a prose paragraph that started with "From " as
   provenance, so a date-shaped token raised O07. A `From` line now needs an entry
   citation right after `From `.
2. A `From` line glued to body text pulled the body into the check. The
   contract and the migration prompt now require a blank line after the
   `From` line. The lint also ends the paragraph at a block marker.
3. A code fence did not reset the paragraph state. It does now.
4. The single-source exception contradicted "every section opens with a
   From line". D4 now states it as an exception in place of `From`
   lines, and names the commissioning entries, not one entry. The field
   case has two or three.
5. Reconcile did not run on a schema-2 target with a map. Its opening
   condition now includes an old §Provenance, and a current step is a
   no-op.
6. Reconcile step 5 said both "replace" and "keep". It now replaces the
   template bullets and keeps the target's own.
7. A reconciled target kept the old lint sentence in `AGENTS.md`. Step 4
   now syncs it, and Limits names it.

Nits fixed: `entry_status` also reads an entry file without a slug. The
template states the literal `From` form and shows a parts example that
the lint reads. The example uses `journals/combat/01`, not monsoon
wording. Limits wraps and names `docs/index.md`. The migration prompt
states the lint precondition and no longer records the audit table
twice. The executor deleted `__pycache__/`, and
`.gitignore` now names it. One passive in Verification
is active.

A scratch-root test covers the fixes. The prose paragraph, the header,
and the fenced code stay silent. A table closes a `From` paragraph. An
entry file without a slug gets O09. An unknown target gets O07.

**Checks.**

- `templates/docs-README.md` and `docs/README.md` are byte-identical.
- The orientation lint on the harness: 0 errors, 0 warnings, before and
  after. Two runs print the same output.
- The journal lint: 0 errors, 0 notes.
- On the monsoon tree, the harness lint gives the same codes and lines
  as the monsoon copy. The O09 label reads "From target", not
  "provenance target".

**Open, in monsoon.** The contract now requires a blank line after a
`From` line. Monsoon `docs/register.md` §11 to §14 glue the `From` line
to body prose, so the lint reads that prose as part of the `From`
paragraph. The monsoon O09 at `docs/register.md:198` fires on
`journals/game/04 D6` in the §13 body for that reason. Monsoon needs a
small follow-up that splits those four paragraphs when it reconciles.
After the split, that citation leaves the lint's reach. It stays
escalated in monsoon meta/26.
