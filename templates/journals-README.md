# Journals

The decision trail for lines of work. Each journal entry is a plan that was
materialized into the record.

## Plan versus journal entry

A **plan** is the working artifact while you collaborate on a piece of work.
It lives in conversation or in `.agents/` (mid-session scratch). It is not
authoritative.

A **journal entry** is a plan committed under `journals/`. It is
authoritative. It is part of the record.

Materializing a plan turns it into a journal entry.

## Where things go

| Path | Holds | Committed |
|---|---|---|
| `journals/` | Materialized plans — the decision trail | yes |
| `docs/` | Derived doc artifacts — design specs, reference | yes |
| `.agents/` | Mid-session scratch — working plans, handoffs, digests | no |
| `.pi-subagents/` | Subagent output (auto-written) | no |

Put the decision trail in `journals/`. Put scratch in `.agents/`. Do not put
scratch or subagent output in `journals/`.

## Layout

One directory per line of work. One file per materialized plan. Numbered
within each directory:

    journals/<area>/<NN>-<slug>.md
    journals/<area>/<line>/<NN>-<slug>.md

Top-level directories are areas. An area exists when its first entry needs
one. Do not seed empty areas. An area may hold one level of sub-directories,
each a line of work within it. Nesting is one level deep, at most. The `NN-`
prefix restarts at `00` in every directory and orders the entries within it.

Entries may sit directly under an area (`journals/gameplay/01-...`) or under a
line (`journals/gameplay/combat-feel/01-...`). Put cross-cutting or foundation
work at the area level. Put a focused sub-effort in its own line directory.

Cite an entry by its path and number, with an optional section — for example,
`journals/gameplay/02 §4` or `journals/gameplay/combat-feel/01 §4`. Do not
cite a bare `journals/01`. The number is only meaningful together with its
directory.

## Status

Each entry opens with a status line:

    Status: <primary>[, <modifier>[, ...]].

Primary states — exactly one, always first:

- **Materialized** — on disk, not yet executed.
- **Decided** — a decision artifact, not a build task. No execution follows.
- **Executed** — carried out. The execution log records what happened.

Modifiers — optional, comma-separated, extensible by the project:

- **Provisional** — not yet firm. May be revised or withdrawn.
- **On hold** — parked. No work until it moves.
- **Superseded by `<area>/<NN>`** — replaced by a later entry. Keep the
  entry. It is still the record of what was once decided.

Examples: `Status: Materialized.` · `Status: Decided, Superseded by
infra/02.` · `Status: Executed.`

Dates do not belong in the status line. The `Date:` line dates the entry;
the execution log dates the work.

## Workflow: plan, then materialize, then execute

1. **Plan.** Collaborate on the work. Produce a plan. The plan lives in
   conversation or in `.agents/` until you materialize it.
2. **Materialize.** Write the plan to `journals/<area>/<NN>-<slug>.md` using
   the format below. This is a separate turn from execution.
3. **Execute.** Carry out the entry against the code only after the user
   instructs execution. Then append the outcome to the same file under
   *Execution log*.

Do not change code for a line of work until the journal entry exists under
`journals/`.

An entry on disk is not permission to execute it — a materialized entry is a
record of intent, not an instruction to act. Do not begin execution in the
same session (or turn) that wrote the entry unless the user explicitly says
to implement it, or has granted autonomy for the line of work. Default to
stopping after materialization and confirming before any code changes.

Trivial, obvious, low-risk changes (typo, comment, import fix, formatting)
skip this workflow. State what you are doing and proceed.

## Entry format

An entry follows this shape:

    # Journal <area>/<NN> — <one-line description>

    Status: <primary>[, <modifier>[, ...]].
    Date: <YYYY-MM-DD>. Depends on: <prior entries or docs, if any>.

    ## Goal
    ## Current state (evidence, verified <date>)
    ## Gap inventory
    ## Decisions
    ## Execution phases
    ## Verification
    ## Files this entry will touch
    ## Risk & rollback
    ## Non-goals
    ## Execution log

Notes:

- **Current state** — what the repo does today. Date the evidence. Link the
  context docs and prior entries that bear on it.
- **Gap inventory** — one row per gap, with severity and a dimension that
  fits the project (for example: code, ui, docs, infra).
- **Decisions** — only when a cross-cutting choice needs recording. Drop the
  section when there is none.
- **Execution phases** — ordered. Mark dependencies between them.
- **Verification** — the definition of done.
- **Execution log** — append to the same file once the work is done. Do not
  keep it in a separate file.

Name actual files, paths, and contracts in every section.

## Style

Write entries with the `ste-writing` skill (`skills/ste-writing/`): active
voice, short sentences, one name for one thing. If the skill is not
installed, apply that rule by hand.
