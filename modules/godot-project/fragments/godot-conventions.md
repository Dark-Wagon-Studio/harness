## Godot 4 conventions

This repo runs on Godot 4. The rules below apply to scripts, scenes, and `.tres`
resources. They follow the version of Godot declared in `project.godot`.

**Compose, do not inherit.** Build behavior from small pieces you wire together.
Do not build it from a class tree you extend. The scene is the unit of
composition. Prefer small composable scenes wired through export vars and
signals over deep `extends` chains that reach into parent state. An export var
is dependency injection through the editor. The scene takes its dependencies as
arguments instead of grabbing global state. A scene that owns its inputs and
emits its outputs composes freely. A script that reaches up the tree or into an
autoload does not.

- Prefer smaller classes over god classes.
- Use `%` for unique-name access. Set `unique_name_in_owner = true` in the
  `.tscn` for any node referenced by `%`.
- Pick a random array element with `array.pick_random()`. Do not use a random
  index.
- Prefer `.tscn` prefabs over nodes created in code.
- Build styles in `.tscn`, not in code.
- Use export vars for prefab references. Do not use `preload` or `load`.
- Prefer guard clauses wherever possible.
- Add a prefab to the tree before setup. `@onready` and `is_node_ready()` gates
  fire only after `add_child`.
- Read existing scene files before editing scenes. Follow the project's Godot 4
  formatting for scripts, scenes, and `.tres`.

### Comment mechanics

GDScript doc comments carry why, not what. They live on the contract surface —
classes, public methods, and `@export` vars.

- Doc comments on classes, public methods, and exported vars only.
- Keep a function doc comment to ≤4 short lines. One line for intent, up to
  three for non-obvious contract or gimmick.
- No "Step 1 / Step 2 / Step 3" comments. Refactor into named helpers and
  document those instead.
- No comments that repeat the variable name or type.
- No trailing `# explanation` on obvious lines.
- Self-check: if deleting a comment leaves a future agent no worse at the why,
  delete it.
- No bug-fix logs in code. Put that in the commit message.
- No caller-awareness in definitions. State intent, contract, and non-obvious
  behavior. Let callers document their own usage.
- No base-class awareness of subclasses.
- No "Note:" or "TODO:" without a tracking issue. Convert to an issue file or
  delete.

### Gimmicks worth a comment (≤4 lines, explain why not what)

- A non-obvious formula (weighted randomness, custom math, tier curves).
- A workaround or Godot quirk (signal ordering, `@onready` race, autoload init
  order, `is_node_ready()` gating).
- A UI layout hack (`SIZE_SHRINK_CENTER`, theme overrides) where the why is not
  obvious.
- A constraint not visible from the code.

### One disambiguating example

- BAD:
  `## Drop the cache on each open — re-instantiating entries is
  cheap and avoids carrying stale state across runs.`
- GOOD: (delete — the line below already does this.)

### `:=` walrus inference

- Explicitly type the result when the right-hand side is a cross-class call.
  GDScript's parser can fail to infer through a forward class reference, and the
  parse error points at unrelated files. Prefer `var x: int = ...` over
  `var x := ...` when the call crosses module boundaries.

### Error checking

- `godot` is on `PATH`. Reach it as a bare command.
- `godot --headless --quit-after 2` loads the full project and exits cleanly.
- Keep `stdout` and `stderr` strictly separate. Never append `2>&1` to a `godot`
  command.
- Pair every `--headless` with `--quit` or `--quit-after` on the same line.
- Run `godot --headless --editor --quit-after 5` after a brand-new `class_name`
  to refresh the global registry.
