# Initialize the journals convention

These instructions run inside a repository that needs the planning harness.
The harness tree (this repo, already cloned to a temp directory by the
bootstrap) is the source for every template and skill. Reference that clone
root as the harness tree.

Install into the current repository:

- `journals/README.md` — the planning contract (layout, status grammar,
  workflow, entry format).
- `AGENTS.md` — the entry point that makes AI harnesses follow the contract.
- `.agents/` scratch (gitignored) and `.gitignore` coverage.
- `skills/ste-writing/` copied from the harness tree.
- `journals/harness/00-harness-install.md` — the record of this install,
  written after the work with `Status: Executed.`

## Authorization and scope

The user's invocation of the installer is the explicit instruction to execute
the install. The no-same-session-execution gate does not block this install;
the `00` entry is written after the work as a record, not before it as a
plan. The invocation authorizes the install and nothing else — no code
changes, no commits, no other files.

Write every generated file in the ste-writing style: active voice, short
sentences, one name for one thing.

## Phase 1 — Probe

Gather these facts in one pass before writing anything:

- Is this a git work tree? (`git rev-parse --is-inside-work-tree`)
- Does `journals/` exist?
- Do `AGENTS.md` or `CLAUDE.md` exist? If yes, do they define a planning or
  journaling workflow?
- Does `.gitignore` exist? Does it cover `.agents/` and `**/.pi-subagents/*`?
- Is there a docs directory? Check `docs/`, `doc/`, `Assets/Docs/`.
- Does `skills/` exist? Does `skills/ste-writing` exist?
- Build and test facts for the *Project specifics* section: `Makefile`,
  `package.json` scripts, CI config (`.github/workflows/`, `.gitlab-ci.yml`),
  README build instructions. Only record what you verify.
- Today's date.

## Phase 2 — Stop conditions, then state and proceed

Stop and ask before writing anything if:

1. `journals/` exists — a convention may already be installed.
2. An existing `AGENTS.md` or `CLAUDE.md` defines a planning or journaling
   workflow — do not overwrite a convention.
3. This is not a git work tree — ask whether to proceed without the git
   hygiene steps.
4. `skills/ste-writing` already exists — ask whether to keep or replace it.

If no stop condition holds, state the file list in one short block and
proceed in the same turn. The invocation is the confirmation; do not wait
for another.

## Phase 3 — Install

### 3.1 Write `journals/README.md`

Copy `templates/journals-README.md` from the harness tree to
`journals/README.md`. If the probe found a docs directory, add one row to
the *Where things go* table: `| `<docs-dir>/` | Stable context that entries
reference | yes |`.

### 3.2 Write or merge `AGENTS.md`

If no `AGENTS.md` exists, copy `templates/AGENTS.md` from the harness tree
to `AGENTS.md`. If one exists without a planning workflow (no stop
condition), merge the *Planning workflow*, *Session rhythm*, *Confirm before
acting*, and *Skills* sections from the template into it and leave
everything else untouched. Report what you inserted.

Fill *Where truth lives* from the probe — include only rows that point at
files you verified to exist. Candidates: `CONTRIBUTING.md` (git flow,
tests), an architecture or conventions doc, CI config, the docs directory.
Keep at least the planning-contract row.

Fill *Project specifics* with verified build and test commands only — one
line each. If you verified none, omit the section.

### 3.3 Git hygiene

Ensure `.gitignore` covers `.agents/` and `**/.pi-subagents/*`. Create
`.gitignore` if it does not exist. Create `.agents/` with an empty
`.gitkeep` in it.

### 3.4 Install the ste-writing skill

Copy `skills/ste-writing/` from the harness tree into `skills/ste-writing/`.
If `skills/` already holds other skills, leave them alone. If the skill is
missing from the harness tree, report it and continue — the README *Style*
section already carries the by-hand rule.

## Phase 4 — Record

Write `journals/harness/00-harness-install.md` now, after the work. Use the
entry format from the README you just wrote. `Status: Executed.` — bare, no
date in the status line. Fill every section from the probe and the install
that just ran. Adjust the gap rows to what the probe actually found. Drop
the *Decisions* section unless a real choice was made (merge versus create,
a fallback taken). The execution log names what landed, any fallbacks, and
the verification results.

## Phase 5 — Verify and present

Check, then report:

- `journals/README.md` exists and carries the two-tier status grammar.
- `AGENTS.md` exists (or was merged) with the planning workflow and confirm
  gate.
- `.gitignore` covers both patterns; `.agents/.gitkeep` exists.
- `skills/ste-writing/SKILL.md` exists.
- `journals/harness/00-harness-install.md` exists with `Status: Executed.`
  and a filled execution log.
- `git status` lists exactly the files you created or edited — nothing else.

Do not commit. Present the summary: files created, files merged, fallbacks
taken, and anything the user should decide (for example, a `CLAUDE.md` that
now needs a pointer to `AGENTS.md`).
