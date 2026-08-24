# Module: godot-project

Opt-in module that adds the Godot 4 project harness to a target repository:
Godot conventions for `AGENTS.md` plus a class-API docs regen pipeline.

## What it is

The Godot 4 project harness. Conventions text the agent consults on every
Godot-specific question, plus a script that regenerates the per-class API docs
from the installed Godot binary.

## External dependencies

The installer probes, the user does not vendor.

- `godot` on `PATH` — runs `--doctool` against the target project.
- `uv` on `PATH` — creates and runs the Python venv that hosts the doc renderer.

`c3-godot-docs-gen` lives as a Python dep in the target repo's `pyproject.toml`.
The installer adds it on apply. The regen script runs it via `uv run`, which
resolves to the project's venv. No global install of the package is needed.

Missing deps gate the module at the Phase 2 confirm point. The agent probes and
reports. The user decides whether to install the toolchain or proceed without
the regen pipeline.

## What it installs in the target repo

1. Inserts the `## Godot 4 conventions` section into the target's `AGENTS.md`
   after the `## Skills` section. Content comes from
   `fragments/godot-conventions.md`.
2. Inserts the `## Project context` section into `AGENTS.md` after the Godot
   conventions section. Content comes from `fragments/project-context.md`.
3. Appends the two rows in `fragments/where-truth-lives-rows.md` to the
   `## Where truth lives` table in `AGENTS.md`:
   `| Engine version | project.godot |` and
   `| Godot class API | docs/godot-api/ |`.
4. Copies `regen_godot_docs.sh` to the target repo root and runs `chmod +x`.
5. Adds `c3-godot-docs-gen` to the target's `pyproject.toml`. Creates the file
   with a minimal `[project]` block listing the dep when `pyproject.toml` does
   not yet exist. Appends the dep to an existing `[project].dependencies` list.
   Skips when the dep is already present.
6. Appends `docs/godot-api/` to the target `.gitignore`.
7. Runs `uv sync` to materialize the venv. Skips when the lockfile is already in
   sync. Falls back to a files-only install when `uv` is missing or sync fails.
   Mirrors the missing-skill fallback in Phase 3.4 of the installer prompt.
8. Runs a first-time regen via `uv run`: `godot --doctool <tmpdir>` then
   `uv run c3-godot-docs-gen --index <flat-tmpdir> docs/godot-api`. Falls back
   to a files-only install when `godot` or the venv cannot resolve the tool.
   Mirrors the missing-skill fallback.

## What it does not vendor

Target-specific or environment-specific facts stay out of the module. The agent
probes at install time. The user fills in over the install's life.

- The exact Godot minor version. Read it from `project.godot`. Do not pin it in
  `AGENTS.md`.
- The test-framework posture — omitted until a framework lands. Add a row to
  `## Project context` when one does.
- The main-scene state — omitted.

## Opt-in gate

The module applies only when:

1. The target is a Godot project — `project.godot` exists at the root.
2. The user opts in at the Phase 2 confirm point.

Default: no. If `project.godot` exists, the installer suggests yes. If `godot`
or `uv` are not on `PATH`, the installer flags the dependency gap and the user
decides whether to install the toolchain or proceed without the regen pipeline.
