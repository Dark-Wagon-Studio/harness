# Journal context/05 — receipt attribution names the speaker

Status: Executed.
Date: 2026-09-25. Depends on: context/04.
Schema: 3.

## Goal

The receipt example attributes every ruling to "the user". The user asked
for the git name instead, with "the user" as the fallback:

> "consider a proposal for the quote clause in entries to refer to the user
> by their configured git name for the project, and "the user" is just a
> fallback"
> — the user, 2026-09-25

The ask then found its ground: "the entry can echo the commit which
already has the user's name". The echo is stronger than a config lookup.
The name stops being external state and becomes a mirror of the record.
The fallback dies with it, because a commit always carries an author.

The echo still couples the attribution to the commit author, and this
repo's own record breaks that coupling. Eleven commits hold two names for
one speaker: `istamarahsan` (8) and `saniistamar` (3, verified 2026-09-25).
A rename re-signs the same mouth. A target that commits through a bot
identity would stamp the bot on a human's ruling.

The session settled on a rule that keeps the name and drops the coupling.
The user ruled:

> "your sentence accepted. propose again in full"
> — the user, 2026-09-25

The accepted form, as it lands in the contract: the attribution names the
speaker, by whatever name the author knows them. The git identity is one
such name. `the user` stays the default form.

This entry writes that sentence into the contract. It also picks up the
installer-sentence fix that context/04's review round deferred to the next
convention line.

## Current state (evidence, verified 2026-09-25)

| Site | Holds |
|---|---|
| `journals/README.md:150-162` | the receipt note. One attribution example: `> — the user, <YYYY-MM-DD>`. No sentence states what the attribution may name |
| `templates/journals-README.md:150-162` | the same note, mirrored for targets |
| `skills/journal-craft/SKILL.md:28-34` | the receipt writing rule. No attribution sentence |
| `git log --format='%an'` | 8 `istamarahsan`, 3 `saniistamar`. One speaker, two names, eleven commits |
| `journals/README.md:180` | "The installer fills the adoption date." False in this self-hosted repo since the first reconcile. Deferred by context/04's review round |
| `templates/journals-README.md:178` | the same sentence, true where it stands: the installer fills the date at init |
| `skills/journal-craft/journal-lint.py` | no receipt check (context/04 D8). The attribution is uncheckable |

context/04 D1 already leaves the form to the author. Nothing today forbids
a name in an attribution. The contract does not say so, and its only
example shows "the user", so the freedom stays invisible to the writer who
follows the example.

## Gap inventory

| Gap | Severity | Dimension |
|---|---|---|
| The contract never states what a receipt attribution claims: the speaker, not the commit identity | medium | conventions |
| The only example attributes to "the user", so the author's freedom to name stays implicit | medium | conventions |
| The deferred installer sentence stays false in this repo | low | docs |

## Decisions

1. **D1 — the attribution names the speaker.** A receipt's attribution
   names the speaker, by whatever name the author knows them. The git
   identity is one such name. `the user` stays the default form and the
   example: it names the role, and the role does not drift when a name
   does. The refused alternative — the git name as the default, "the
   user" as the fallback — failed on the record. The commit author names
   the committer, and this repo holds two names for one speaker across
   eleven commits. The attribution would follow the config, not the
   person. A bot identity in a target would sign a human's ruling. The
   rule keeps what the echo wanted, the name grounded in the record, and
   drops the coupling: the claim resolves to the person, not the commit.
2. **D2 — no schema bump.** The change adds sentences to the receipt note
   and the Schema section. No entry grammar moves. No lint check moves.
   Every entry lints the same before and after. The ledger tracks what
   the lint can resolve, and nothing checkable changed. The schema-3
   review round set the precedent: contract prose amended with no bump.
3. **D3 — the installer sentence names the self-hosted case.** In
   `journals/README.md` §Schema, "The installer fills the adoption date."
   becomes "In a target, the installer fills the adoption date. A
   self-hosted repo fills its own." The template sentence stays as it is:
   in a target, the installer does fill it. This picks up the deferral
   recorded in context/04's review round.

## Execution phases

Ordered. Phase 1 edits the contract. Phases 2 and 3 mirror it. Phase 4
records the surfaces checked with no edit. Phase 5 gates the close.

### Phase 1 — `journals/README.md`

1. §Entry format, **Ruling receipts** note: after "The form is the
   author's choice.", add, word for word: "The attribution names the
   speaker, by whatever name the author knows them. The git identity is
   one such name. `the user` stays the default form."
2. §Schema: qualify the installer sentence per D3. No other edit.

### Phase 2 — `templates/journals-README.md`

1. Insert the same three sentences at the same place in the mirrored
   receipt note. Word for word.
2. No other edit. The template's installer sentence is true where it
   stands.

### Phase 3 — `skills/journal-craft/SKILL.md`

1. The receipt writing rule gains the same three sentences, after "The
   form is the author's choice."

### Phase 4 — surfaces checked, no edit

1. `prompts/harness-reconcile.md` step 2(g) syncs the receipt note by
   name, so the new sentences reach a target on its next reconcile.
2. `prompts/harness-init.md` copies the template, so a fresh target gets
   them at install.
3. The lint: no change. context/04 D8 stands.
4. `AGENTS.md` and `skills/ste-writing/` hold no receipt surfaces.

### Phase 5 — verify and close

1. Run `python3 skills/journal-craft/journal-lint.py`. Expect zero
   errors and zero notes.
2. Run `python3 skills/orientation/orientation-lint.py`. Expect zero
   errors.
3. Run both lints twice. Outputs must match.
4. Append the outcome to this entry's Execution log.

## Verification

- The three attribution sentences appear word for word in
  `journals/README.md`, `templates/journals-README.md`, and
  `skills/journal-craft/SKILL.md`.
- The example quote line `> — the user, <YYYY-MM-DD>` is unchanged in
  both READMEs.
- The harness §Schema sentence carries the self-host clause. The
  template sentence does not change.
- Scratch check, discarded after the run: a receipt attributed to a name
  (for example `> — saniistamar, 2026-09-25`) reports no lint finding.
  The lint holds no attribution grammar.
- Both lints exit 0 with zero findings. Double runs print identical
  output.
- `git status` lists exactly the three files in the table below, plus
  this entry.

## Files this entry will touch

| File | Action |
|---|---|
| `journals/README.md` | edit (Phase 1) |
| `templates/journals-README.md` | edit (Phase 2) |
| `skills/journal-craft/SKILL.md` | edit (Phase 3) |

## Risk & rollback

- **Wrong name.** A receipt with the wrong name claims that person spoke
  words they did not say. The rule bounds the claim: the name must be one
  the author knows the speaker by. A bot identity is not such a name.
  "the user" is always safe. No lint checks this (context/04 D8). The
  contract states the bound.
- **Mixed corpus.** Entries before this change attribute "the user".
  Later entries may name. The spread is the author's choice, now visible
  in the contract (context/04 D1). No rewrite of entries that exist.
- **Reconcile.** After D3, the harness §Schema sentence differs from the
  template's. Reconcile syncs targets from the template. The harness is
  not a target. No conflict.
- **Rollback.** A git revert in harness. Three files plus this entry.

## Non-goals

- No default flip. "the user" stays the example and the default form.
  The contract sets no order between the name and the role-word.
- No schema bump, no ledger line, no lint change. Attribution stays
  uncheckable.
- No rewrite of entries that exist. context/04's own receipts keep "the
  user".
- No author field and no provenance line for entries. The sentence is
  the whole change.
- No edit to `prompts/`, `AGENTS.md`, or `skills/ste-writing/`.

## Execution log

2026-09-25. Executed on instruction ("finish it."), in the session that
materialized the entry. All five phases ran.

- Phase 1: the receipt note in `journals/README.md` gained the three
  attribution sentences after "The form is the author's choice." The
  §Schema installer sentence now reads "In a target, the installer fills
  the adoption date. A self-hosted repo fills its own."
- Phase 2: `templates/journals-README.md` gained the same sentences at
  the same place, word for word. The template's installer sentence is
  unchanged.
- Phase 3: the receipt writing rule in `skills/journal-craft/SKILL.md`
  gained the same sentences.
- Phase 4: checked, no edit. Reconcile step 2(g) syncs the receipt note
  by name. Init copies the template. The lint holds no attribution
  grammar (context/04 D8). `AGENTS.md` and `skills/ste-writing/` hold no
  receipt surfaces.
- Phase 5: `python3 skills/journal-craft/journal-lint.py` exits 0 with
  zero findings, summary "repo schema 3, adopted 2026-09-24, lint
  understands schema 3". `python3 skills/orientation/orientation-lint.py`
  exits 0 with zero findings. Both double runs print identical output.

Scratch check, discarded after the run: a scratch entry holding a receipt
attributed to a name reported no lint finding. The attribution carries no
grammar, per context/04 D8.

The three attribution sentences grep identical in all three files. The
example quote line `> — the user, <YYYY-MM-DD>` is unchanged in both
READMEs. `git status` lists exactly the three files in the table plus
this entry.
