# harness

All-in-one installer source for the journals planning convention: the
templates a repo commits, the skills it uses, and the installer prompt that
wires them together. Built for AI coding agents (pi, Claude Code, and
similar). One clone holds every dependency.

## Layout

| Path | What it is |
|---|---|
| `templates/journals-README.md` | The planning contract, committed as `journals/README.md` |
| `templates/AGENTS.md` | The AI entry point, committed as `AGENTS.md` |
| `skills/ste-writing/` | The STE prose skill (canonical home) |
| `skills/jtbd-coach/` | The JTBD coaching skill (canonical home, optional at install) |
| `prompts/journals-init.md` | The installer instructions the pi bootstrap executes |

## Install (manual)

1. Copy `templates/journals-README.md` to `journals/README.md`.
2. Copy `templates/AGENTS.md` to `AGENTS.md`. If the repo already has an
   `AGENTS.md`, merge the *Planning workflow*, *Session rhythm*, *Confirm
   before acting*, and *Skills* sections instead.
3. Copy `skills/ste-writing/` to `skills/ste-writing/`.
4. Optionally copy `skills/jtbd-coach/` to `skills/jtbd-coach/` and add its
   row (text in `prompts/journals-init.md`, Phase 3.5) to the *Skills*
   table in `AGENTS.md`.
5. Add `.agents/` and `**/.pi-subagents/*` to `.gitignore`. Create
   `.agents/.gitkeep`.
6. Record the install as `journals/harness/00-harness-install.md` with
   `Status: Executed.`

## Install (pi)

Run `/journals-init` from the thin bootstrap prompt. It clones this repo to
a temp directory, executes `prompts/journals-init.md` against the target
repository, and removes the temp clone when it finishes.

## Versioning

Not versioned. Installs track `main`.
