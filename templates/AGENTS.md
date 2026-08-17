# AGENTS.md

Entry point for AI work in this repo. Read this first.

## Planning workflow

Every line of work runs: plan, materialize, execute.

1. **Plan.** Work the problem in conversation or in `.agents/<topic>/`
   (gitignored scratch). Plans are not authoritative.
2. **Materialize.** Write the plan to `journals/<area>/<NN>-<slug>.md`
   following `journals/README.md`. An entry is a record of intent, not an
   instruction to act. Do not execute an entry in the session that wrote it,
   unless the user explicitly says to implement it or has granted autonomy
   for the line of work. Default to stopping after materialization.
3. **Execute.** Carry out the entry against the code. Append the outcome to
   its *Execution log* in the same file.

Trivial, low-risk changes (typo, comment, import fix, formatting) skip this
workflow. State what you are doing and proceed.

The workflow rule above is stricter than the confirm gate below, and it
governs. Silence never authorizes execution of a journal entry.

## Session rhythm

Two modes. A session runs in one mode.

- **Plan mode.** The session opens on a problem and no entry exists. It ends
  when the entry is materialized.
- **Execute mode.** The session opens on a journal entry. The entry is the
  contract. Implement it, fill gaps the entry did not foresee, and escalate
  those gaps rather than deciding alone.

Both modes run one cycle: **lookahead → scout → synthesis → discuss → act →
review and fix**. Scout means short, bounded investigation — one question
per scout. Discuss is core in plan mode and an exception in execute mode.

## Confirm before acting

Before acting on anything that is not a direct instruction, stand in one of
two states:

1. The user confirmed it.
2. You stated a default and the user did not contest it. Write "I will do X
   unless you say otherwise, because Y" and give the user a chance to
   override.

If neither holds, stop and ask. Do not decide in silence and proceed.

## Skills

Skills live in `skills/` at the repo root. They are harness-agnostic — load
them by reading the `SKILL.md`.

| Skill | Use |
|---|---|
| `ste-writing` | Rewrite engineering prose (journal entries, docs, PR text, comments) into STE. Mandated for journal entries and for new or edited text in root-level docs. |

## Where truth lives

| Topic | Source |
|---|---|
| Planning contract | `journals/README.md` |
