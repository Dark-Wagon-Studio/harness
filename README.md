# harness

One-stop installer source for the DWS base agent layer: the templates a
repo commits, the skills it uses, and the installer prompt that wires
them together. Base layer always installs. Skills and modules are opt-in.
AI coding agents read it. One clone holds every dependency.

## Layout

| Path | What it is |
|---|---|
| `templates/journals-README.md` | The planning contract, committed as `journals/README.md` |
| `templates/AGENTS.md` | The AI entry point, committed as `AGENTS.md` |
| `skills/ste-writing/` | The STE prose skill (canonical home, mandated) |
| `skills/jtbd-coach/` | The JTBD coaching skill (canonical home, optional at install) |
| `modules/godot-project/` | The Godot 4 project module (Godot conventions + class-API docs regen, optional at install) |
| `prompts/harness-init.md` | The installer instructions |

## Install (manual)

1. Copy `templates/journals-README.md` to `journals/README.md`.
2. Copy `templates/AGENTS.md` to `AGENTS.md`. If the repo already has an
   `AGENTS.md`, merge the *Planning workflow*, *Session rhythm*, *Confirm
   before acting*, *Docs lifecycle*, and *Skills* sections instead.
3. Copy `skills/ste-writing/` to `skills/ste-writing/`.
4. Optionally copy `skills/jtbd-coach/` to `skills/jtbd-coach/` and add
   its row (text in `prompts/harness-init.md`, Phase 3.5) to the *Skills*
   table in `AGENTS.md`.
5. Optionally, for Godot projects, copy `modules/godot-project/` and
   follow its manifest (`modules/godot-project/README.md`). The installer
   adds `c3-godot-docs-gen` to the target repo's `pyproject.toml`, runs
   `uv sync` to materialize the venv, applies Godot conventions to
   `AGENTS.md`, drops `regen_godot_docs.sh` at the repo root, appends
   `docs/godot-api/` to `.gitignore`, and runs a first-time regen via
   `uv run`. Requires `godot` and `uv` on `PATH`.
6. Add `.agents/` and `**/.pi-subagents/*` to `.gitignore`. Create
   `.agents/.gitkeep`.
7. Record the install as `journals/harness/00-harness-install.md` with
   `Status: Executed.`

## Versioning

Not versioned. Installs track `main`.
