# Initialize the DWS base agent layer

These instructions run inside a repository that needs the DWS base agent layer.
The harness tree (this repo, already cloned to a temp directory by the
bootstrap) is the source for every template, skill, and module. Reference that
clone root as the harness tree.

The base layer always installs:

- `journals/README.md` — the planning contract (layout, status grammar,
  workflow, entry format).
- `AGENTS.md` — the entry point that makes AI harnesses follow the contract.
- `.agents/` scratch (gitignored) and `.gitignore` coverage.
- `skills/ste-writing/` — copied from the harness tree.

Opt-in layer. The installer asks before any of these land:

- `skills/jtbd-coach/` — opt-in skill. Default: no.
- `modules/godot-project/` — opt-in module for Godot projects (Godot 4
  conventions for `AGENTS.md` plus a class-API docs regen pipeline). Default:
  no.

Record the install at:

- `journals/harness/00-harness-install.md` — written after the work with
  `Status: Executed.` Records base + applied modules + the godot-module decision
  (opted in, declined, or deps missing).

The manifests the installer reads to apply each module live alongside the
module's files in the harness tree — for the godot-project module, see
`modules/godot-project/README.md`.

## Authorization and scope

The user's invocation of the installer is the explicit instruction to execute
the install. The no-same-session-execution gate does not block this install. The
`00` entry is written after the work as a record, not before it as a plan. The
invocation authorizes the install and nothing else — no code changes, no
commits, no other files.

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
- Did the invocation already decide jtbd-coach (explicit include or exclude)?
  Does `skills/jtbd-coach` exist in the target?
- Does `project.godot` exist at the repo root? Godot project detection. Gates
  the godot-project module.
- Does `pyproject.toml` exist at the repo root? Gates how the godot-project
  module adds `c3-godot-docs-gen` (create from scratch versus append to an
  existing `[project]` block).
- Are `godot` and `uv` on `PATH`? (`command -v godot`, `command -v uv`.)
- Does `docs/godot-api/` already exist?
- Build and test facts for the _Project specifics_ section: `Makefile`,
  `package.json` scripts, CI config (`.github/workflows/`, `.gitlab-ci.yml`),
  README build instructions. Only record what you verify.
- Today's date.

## Phase 2 — Stop conditions, then state and proceed

Stop and ask before writing anything if:

1. `journals/` exists — a convention may already be installed.
2. An existing `AGENTS.md` or `CLAUDE.md` defines a planning or journaling
   workflow — do not overwrite a convention.
3. This is not a git work tree — ask whether to proceed without the git hygiene
   steps.
4. `skills/ste-writing` or `skills/jtbd-coach` already exists — ask whether to
   keep or replace it.

### jtbd-coach gate

The invocation authorizes the core install, not the optional skill. At this
confirm point ask one bounded question, unless the invocation already decided
it:

Also install the optional jtbd-coach skill? Default: no.

If a stop condition above holds, fold this question into that stop. An unclear
answer means no. Carry the decision to Phase 3.5.

A "keep" answer for a pre-existing `skills/jtbd-coach` counts as yes for the
AGENTS.md row and no for the directory copy: keep the existing files, append the
row only if it is missing.

### godot-project gate

If `project.godot` exists at the repo root, the target is a Godot project. Ask
at this confirm point, unless the invocation already decided it:

Also apply the opt-in godot-project module? Default: no. If yes, the installer
adds Godot conventions to `AGENTS.md`, drops `regen_godot_docs.sh` at the repo
root, appends `docs/godot-api/` to `.gitignore`, and runs a first-time regen.

If `project.godot` does not exist, the module does not apply. The gate does not
ask.

If a stop condition above holds, fold this question into that stop. An unclear
answer means no. Carry the decision to Phase 3.6.

When `godot` or `uv` are not on `PATH`, the regen pipeline cannot run. State the
missing dep. Ask one bounded question:

Install the missing toolchain now, or proceed without the regen?

Both answers apply the module. The regen runs only when the toolchain sits on
`PATH`. If the regen cannot run, Phase 3.6 records a deps-missing fallback and
continues with the files-only install.

If no stop condition holds, state the file list in one short block and proceed
in the same turn. The invocation is the confirmation. Do not wait for another.

## Phase 3 — Install

### 3.1 Write `journals/README.md`

Copy `templates/journals-README.md` from the harness tree to
`journals/README.md`. If the probe found a docs directory, add one row to the
_Where things go_ table:
`|`<docs-dir>/`| Stable context that entries
reference | yes |`.

### 3.2 Write or merge `AGENTS.md`

If no `AGENTS.md` exists, copy `templates/AGENTS.md` from the harness tree to
`AGENTS.md`. If one exists without a planning workflow (no stop condition),
merge the _Planning workflow_, _Session rhythm_, _Confirm before acting_, _Docs
lifecycle_, and _Skills_ sections from the template into it and leave everything
else untouched. Report what you inserted.

Fill _Where truth lives_ from the probe — include only rows that point at files
you verified to exist. Candidates: `CONTRIBUTING.md` (git flow, tests), an
architecture or conventions doc, CI config, the docs directory. Keep at least
the planning-contract row.

Fill _Project specifics_ with verified build and test commands only — one line
each. If you verified none, omit the section.

### 3.3 Git hygiene

Make `.gitignore` cover `.agents/` and `**/.pi-subagents/*`. Create `.gitignore`
if it does not exist. Create `.agents/` with an empty `.gitkeep` in it.

### 3.4 Install the ste-writing skill

Copy `skills/ste-writing/` from the harness tree into `skills/ste-writing/`. If
`skills/` already holds other skills, leave them alone. If the skill is missing
from the harness tree, report it and continue — the README _Style_ section
already carries the by-hand rule.

### 3.5 Install jtbd-coach (opt-in only)

If the Phase 2 decision is yes, copy `skills/jtbd-coach/` from the harness tree
into `skills/jtbd-coach/`, then append this row to the _Skills_ table in the
`AGENTS.md` written or merged in 3.2:

| `jtbd-coach` | Coach product decisions through Jobs-to-be-Done: reframe
feature requests into jobs, write job stories, run switch interviews, score
opportunities. Optional — loaded on demand. |

If the decision is no, install nothing. Say in the final summary that the skill
can be added later by copying `skills/jtbd-coach/` from a harness clone and
adding the row.

If the target's merged `AGENTS.md` carries its own skills table instead of the
one from the template, append the row there. If the skill is missing from the
harness tree, report it and continue — mirror the 3.4 fallback.

### 3.6 Apply the godot-project module (opt-in only)

If the Phase 2 decision is yes, read `modules/godot-project/README.md` from the
harness tree as the manifest. Apply in this order:

1. Insert `modules/godot-project/fragments/godot-conventions.md` into the
   `AGENTS.md` written or merged in 3.2, after the `## Skills` section. The
   fragment is a complete `## Godot 4 conventions` section. Insert it verbatim.
2. Insert `modules/godot-project/fragments/project-context.md` into the same
   `AGENTS.md`, after the section added in step 1. The fragment is a complete
   `## Project context` section. Insert it verbatim.
3. Append the two rows in `modules/godot-project/fragments/where-truth-lives-rows.md`
   to the existing `## Where truth lives` table in the `AGENTS.md` written or
   merged in 3.2: `| Engine version | project.godot |` and
   `| Godot class API | docs/godot-api/ |`. Skip when both rows are already
   present.
4. Copy `modules/godot-project/regen_godot_docs.sh` from the harness tree to the
   target repo root and run `chmod +x`.
5. Add `c3-godot-docs-gen` as a Python dep in the target repo's
   `pyproject.toml`. Read the file when it exists and append
   `"c3-godot-docs-gen"` (without a version pin when the file already holds a
   `[project]` block, since the project's resolver policy already governs
   versions) to `[project].dependencies`. Skip when the string is already there.
   Create the file from scratch with this shape when `pyproject.toml` does not
   yet exist:
   ```toml
   [project]
   name = "<repo-dir-name>"
   version = "0.0.1"
   requires-python = ">=3.11"
   dependencies = ["c3-godot-docs-gen"]
   ```
   Use the repo's directory basename for `name`. Do not overwrite an existing
   `[project]` block.
6. Append the line in `modules/godot-project/gitignore` to the target
   `.gitignore`. Create the file first if step 3.3 did not.
7. Run `uv sync` to materialize the venv. Skip when `uv.lock` is already in sync
   with the updated `pyproject.toml`. Fall back to the files-only install and
   record a deps-missing gap when `uv` is not on `PATH` or sync fails. Mirror
   the 3.4 fallback.
8. Run the first-time regen when `godot` is on `PATH` and the venv resolves the
   tool: `godot --doctool <tmpdir>` then
   `uv run c3-godot-docs-gen --index <flat-tmpdir> docs/godot-api`. Fall back to
   the files-only install and record the dep gap when a dep is missing. Mirror
   the 3.4 fallback.

If the decision is no, install nothing. Say in the final summary that the module
can be added later by copying `modules/godot-project/` from a harness clone and
applying the manifest.

If the target's `AGENTS.md` was merged rather than created, the fragments still
insert after the `## Skills` anchor — same as for jtbd-coach in 3.5.

## Phase 4 — Record

Write `journals/harness/00-harness-install.md` now, after the work. Use the
entry format from the README you just wrote. `Status: Executed.` — bare, no date
in the status line. Fill every section from the probe and the install that just
ran. Adjust the gap rows to what the probe actually found. Drop the _Decisions_
section unless a real choice was made (merge versus create, a fallback taken,
the jtbd-coach gate ran, or the godot-project gate ran — opted in, declined, or
kept a pre-existing copy). The execution log names what landed, any fallbacks,
and the verification results.

When the godot-project module ran, record:

- The gate decision (opted in, declined, deps missing).
- The probe results for `project.godot`, `pyproject.toml`, `godot` on `PATH`,
  `uv` on `PATH`, and prior `docs/godot-api/` existence.
- Whether `pyproject.toml` got created from scratch or amended.
- Whether `uv sync` resolved the venv.
- Whether the first-time regen ran or got skipped.
- The dep gap, if any, that caused the skip.

## Phase 5 — Verify and present

Check, then report:

- `journals/README.md` exists and carries the two-tier status grammar.
- `AGENTS.md` exists (or was merged) with the planning workflow and confirm
  gate.
- `.gitignore` covers both patterns. `.agents/.gitkeep` exists.
- `skills/ste-writing/SKILL.md` exists.
- If jtbd-coach was opted in: `skills/jtbd-coach/SKILL.md` exists and the
  AGENTS.md Skills table carries its row. If not: neither exists.
- `journals/harness/00-harness-install.md` exists with `Status: Executed.` and a
  filled execution log.
- If the godot-project module ran:
  - `AGENTS.md` carries the `## Godot 4 conventions` section.
  - `AGENTS.md` carries the `## Project context` section.
  - `## Where truth lives` lists `Engine version` and `Godot class API` as new
    rows.
  - `regen_godot_docs.sh` sits at the repo root, executable.
  - `pyproject.toml` declares `c3-godot-docs-gen` as a dep.
  - `docs/godot-api/` contains `index.md` plus class files (or, on a
    deps-missing skip, does not yet exist).
  - `.gitignore` carries the `docs/godot-api/` line.
- `git status` lists exactly the files you created or edited — nothing else.

Do not commit. Present the summary: files created, files merged, fallbacks
taken, the godot-module decision and regen outcome, and anything the user should
decide (for example, a `CLAUDE.md` that now needs a pointer to `AGENTS.md`).
