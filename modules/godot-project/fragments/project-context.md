## Project context

- Engine: Godot 4. The exact minor version lives in `project.godot`. Do not
  hardcode a version here.
- `user://` is the save-root convention. The save system picks the exact
  filename when it lands.
- Godot class API docs (Node, Node2D, signals, properties, methods) live at
  `docs/godot-api/` (gitignored). Read the per-class Markdown with the `read`
  tool when a question turns on Godot API specifics. Regenerate with
  `./regen_godot_docs.sh` whenever `project.godot`'s Godot version bumps or
  after a major script surface change.
