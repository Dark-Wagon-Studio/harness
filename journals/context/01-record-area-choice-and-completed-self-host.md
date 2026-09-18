# Journal context/01 — install-record area becomes the target's choice; harness completes its own base layer

Status: Materialized.
Date: 2026-09-18. Depends on: context/00.

## Goal

Two changes, one theme: harness consumes the contracts it ships.

1. **Parameterized record area.** The installer and the reconcile prompt stop
   fixing the install record to `journals/harness/`. The target repo's own
   taxonomy owns the area. The installer asks one bounded question with a
   drafted default. The default area is `meta`.
2. **Completed self-host.** Harness fills the empty Repository map, installs
   its own `docs/` tree, and closes the small gaps its installer closes in
   every target. context/00 deferred these; this entry lifts the deferrals.

## Current state (evidence, verified 2026-09-18)

Five sites name `journals/harness/` as the record destination inside the
target repo:

| Site | Holds the literal |
|---|---|
| `prompts/harness-init.md:30` | record-at list |
| `prompts/harness-init.md:284` | Phase 4 record step |
| `prompts/harness-init.md:333` | Phase 5 verify bullet |
| `prompts/harness-reconcile.md:31` | step 6 |
| `README.md:63` | manual install step 9 |

`harness` names the installer, not the target. Every install therefore seeds
an area that mirrors the tool, not the repo's own taxonomy.

Self-host state today:

| Contract | State |
|---|---|
| `journals/README.md` schema footer | installed (`Schema: 1. Adopted: 2026-09-18`) |
| Root `AGENTS.md` | present, byte-identical to `templates/AGENTS.md`, map tables empty |
| `docs/` tree | absent (context/00 non-goal) |
| Root `README.md` link to `docs/index.md` | absent |
| `.agents/.gitkeep` | absent |
| `skills/` | canonical home, no copy needed |
| journal-lint, orientation-lint | both exit 0, zero findings, run this day |

context/00 recorded the map deferral: "The user chose empty tables. ...
The `orientation` skill fills them later." The empty map costs every session
the orientation warm-up that context/00 §Gap inventory priced as high. The
absent `docs/` tree leaves orientation-lint checks O06 and O07 with no
surface to check.

## Gap inventory

| Gap | Severity | Dimension |
|---|---|---|
| Install-record area fixed to `harness` at five sites. The target's taxonomy never gets the choice. | high | installer |
| No drafting protocol for the area choice. The installer has no probe or gate for it. | high | installer |
| Repository map tables empty. Sessions pay the search warm-up the map exists to delete. | high | docs |
| No `docs/` tree. Harness ships a docs contract it does not run. O06/O07 stay vacuous. | medium | docs |
| Root `README.md` does not link `docs/index.md`, against installer step 3.2b. | low | docs |
| `.agents/.gitkeep` absent, against installer step 3.3. | low | infra |

## Decisions

1. **D1 — The record area is the target's choice, drafted as `meta`.** The
   installer gains one bounded Phase 2 question: record the install under
   which journal area. The draft rule: the area of a prior harness
   install/reconcile entry when one exists, else `meta`. The user confirms
   or overrides. An unclear answer takes the default. Basis: context/00 D2
   and D6 — taxonomy is curated, machinery proposes, a human accepts.
2. **D2 — The slug keeps the actor's name.** Entries stay
   `<NN>-harness-install` and `<NN>-harness-reconcile` in any area. The slug
   names the event. The area carries the target's taxonomy. Only the area
   varies.
3. **D3 — The area choice is a recorded decision.** The install entry's
   Decisions section names the chosen area. The choice commits the target's
   taxonomy, so it belongs in the record, not only in the file path.
4. **D4 — Harness completes its self-host now.** Fill the map through the
   orientation propose-accept protocol, install the `docs/` tree from
   harness's own templates, add `.agents/.gitkeep`, and link the root
   `README.md`. The repo that ships the contracts runs them. Basis:
   context/00 Phase 3 protocol, `templates/docs-README.md` contract.

## Execution phases

Ordered. Phase 6 gates the close.

### Phase 1 — Parameterize `prompts/harness-init.md`

1. Record-at list (line 30): replace the fixed path with the parameterized
   form. The record lands at `journals/<area>/<NN>-harness-install.md`. The
   area is the target's choice, drafted per D1. A new area starts at `00`.
   An existing area takes its next free number.
2. Phase 1 probe, add two facts: the `journals/` area directories, and any
   prior harness install or reconcile entry with its path.
3. Phase 2, add one bounded question to the gate family: "Record the install
   under which journal area? Default: <draft>." Draft per D1. Fold into a
   stop when one holds. Carry the answer to Phase 4. The answer names an
   area, not a line. One path component.
4. Phase 4 (line 284): replace the fixed path with the chosen area. Add the
   area choice to the decisions the entry records (D3).
5. Phase 5 (line 333): re-word the verify bullet to the parameterized path.

### Phase 2 — Parameterize `prompts/harness-reconcile.md`

1. Probe, add one fact: the location of any prior harness install or
   reconcile entry.
2. Step 6 (line 31): record under the prior entry's area. Ask one bounded
   question only when no prior entry exists. Default `meta`. The number
   probes the next free slot in that area.

### Phase 3 — Re-word `README.md` step 9

State the parameterized path. Name the default and the drafting rule.

### Phase 4 — Fill the Repository map in `AGENTS.md`

Through the orientation skill protocol: propose the filled tables in
session, the user accepts or amends, then land.

- Zones, one row each: `templates/`, `skills/`, `modules/`, `prompts/`,
  `journals/`, and `docs/` after Phase 5.
- Vocabulary bridge, inbound pairs the tree already uses: harness tree
  versus target, base layer versus opt-in module, install versus reconcile,
  lint (advisory, never a gate).
- Authority steps stay verbatim.
- Root map stays within 40 lines.

`templates/AGENTS.md` keeps its empty tables. Targets scaffold their own.

### Phase 5 — `docs/` tree and hygiene

1. Copy `templates/docs-README.md` to `docs/README.md`.
2. Copy `templates/docs-index.md` to `docs/index.md`. Fill `<repo>` with
   `harness`.
3. Append to the root `README.md`, per installer step 3.2b: one line linking
   `docs/index.md`.
4. Create `.agents/.gitkeep`.

### Phase 6 — Verify and close

1. Run `python3 skills/journal-craft/journal-lint.py` from the repo root.
   Expect zero errors.
2. Run `python3 skills/orientation/orientation-lint.py`. Expect zero errors.
3. Run both lints twice. Outputs must match.
4. Append the outcome to this entry's Execution log.

## Verification

- `rg 'journals/harness' README.md prompts/` returns nothing.
- Both lints exit 0 from the repo root. Double runs print identical output.
- `AGENTS.md` map tables hold the filled rows. The root map stays within 40
  lines.
- `docs/README.md` and `docs/index.md` exist. The root `README.md` links
  `docs/index.md`.
- `.agents/.gitkeep` exists.
- `git status` lists exactly the files in the table below. Nothing else.

## Files this entry will touch

| File | Action |
|---|---|
| `prompts/harness-init.md` | edit (Phase 1) |
| `prompts/harness-reconcile.md` | edit (Phase 2) |
| `README.md` | edit (Phase 3, link in Phase 5) |
| `AGENTS.md` | edit, map fill (Phase 4) |
| `docs/README.md` | new (Phase 5) |
| `docs/index.md` | new (Phase 5) |
| `.agents/.gitkeep` | new (Phase 5) |

## Risk & rollback

- **Installer drift.** Installed repos track `main`. This change alters
  installer behavior only, not templates. Corpora that already carry
  `journals/harness/` keep it. Reconcile drafts their area, so continuity
  holds. Rollback is a git revert in harness.
- **Map curation.** A wrong row misdirects sessions until a trigger fixes
  it. The propose-accept protocol and O01 path checks bound this. The risk
  was accepted with the map itself in context/00.
- **Empty docs tree.** The index stub is legal by the contract. No
  generation ships, per the linter law. Topic docs appear when topics need
  them.
- **One more install question.** The area question adds friction. It folds
  into a stop when one holds and carries a default. Bounded cost.

## Non-goals

- No retrofit of existing installs. The pilot keeps its record where it
  lives.
- No edit to `templates/AGENTS.md`. Target maps scaffold at install.
- No topic docs for harness in this entry. The index stays a stub.
- No jtbd-coach row in harness's own Skills table. The canonical home is
  not an opt-in install. The map's `skills/` row covers discovery.
- No installer self-run against harness. Self-host stays manual, as in
  context/00 Phase 3.
- No consolidation of the Phase 2 gates into one block.

## Execution log

2026-09-18. Executed under granted autonomy. All six phases landed.

- Phases 1 through 3: five literal sites parameterized. The record-area
  gate joined the Phase 2 gate family with the draft rule (prior record
  area, else `meta`). The probe gains the prior-record fact. Phase 4
  records the area choice. Reconcile step 6 drafts the prior entry's
  area and asks only when no prior entry exists. README step 9 names the
  default and the draft rule.
- Phase 4: map filled. Six zone rows, six vocabulary pairs, authority
  steps verbatim. The section measures 39 lines against the 40-line
  budget. The propose-accept gate ran under the granted autonomy: the
  parent landed the rows. The review round and the user at commit hold
  the accept side.
- Phase 5: `docs/README.md` and `docs/index.md` installed from harness
  templates. The index fills the repo name. The root `README.md` links
  `docs/index.md`. `.agents/.gitkeep` created.
- Phase 6: journal-lint reports 0 errors, 0 notes. orientation-lint
  reports 0 errors, 0 warnings. Both print identical output on double
  runs. `rg 'journals/harness' README.md prompts/` returns nothing.

Fresh-context review round (two reviewer subagents):

- Fixed: the Authorization section still called the record "the `00`
  entry". It now says "the record entry". README step 9 now names the
  default (`meta`) and the draft rule, as Phase 3 requires.
- `templates/AGENTS.md` keeps its empty tables, as the entry requires.

Known, deferred. The review round surfaced pre-existing installer
 defects outside this entry's scope:

- The godot-module pyproject step has no case for an existing file
  without a `[project]` block.
- The 3.2 merge list omits _Where truth lives_ while ordering row
  appends into it.
- "Proceed in the same turn" conflicts with the 3.2 map scaffold's
  propose-accept wait.
- Step 3.5 can overwrite a kept `skills/jtbd-coach/`. Step 3.4 has no
  keep semantics at all.
- The godot toolchain gate offers an install the authorization scope
  forbids.
- The reconcile probe gathers journals areas nowhere while step 3
  scaffolds from them. Step 2 can duplicate a `Modifiers:` line or a
  footer on a partially modern corpus. Probe facts for ste-writing,
  nested AGENTS.md files, and docs feed no step.
- The `uv.lock` skip check names no command. The godot gitignore append
  lacks an already-present guard. "Both lints" is never expanded. The
  manual README install step 3 lacks the README-missing stub branch.

`git status` carries this entry file itself alongside the touched-file
 table, as in context/00. The entry is the actor. `.agents/.gitkeep` is
untracked by design: `.agents/` is gitignored and the keep file only
holds the directory on disk.
