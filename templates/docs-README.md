# docs/ — derived doc artifacts

Doc artifacts live here: design specs, reference docs. Not journals, not
scratch, not plans. Authored artifacts derive from decisions recorded in
`journals/`. Generated reference docs derive from the tool that builds them.

## Model

Journals are the immutable primitive. Every authored doc here is a
projection of decisions recorded in `journals/`. When a doc and a journal
entry disagree, the entry wins. Fix the doc, or supersede the entry with
a new one.

## Layout

The link graph, top down:

    README.md          — repo root. Generic: what this repo is for humans. Links to docs/index.md.
    docs/README.md     — this file. The authoring contract.
    docs/index.md      — the entrypoint. "Things you need to know, start here." Links every topic doc.
    docs/<topic>.md    — a topic doc.
    docs/<generated>/  — generated reference (engine API, etc.), gitignored. Not part of the graph.

The entrypoint is `docs/index.md`. Navigation follows links, not
directories.

No subdirectories for authored docs. A topic doc appears when its topic
first needs one. One name for one thing: a topic has one doc and one
filename.

## Links

- Link between docs with relative path markdown links:
  `[retreat](./retreat.md)`. The link graph replaces hierarchy.
- Keep filenames stable. A rename breaks links. If a name must change,
  fix every link in the same change.
- Markdown links stay inside `docs/`. Cite journal entries and code
  paths as prose — `journals/combat/01 §4`, `rust/src/sim/mod.rs` — not
  as links.
- Cite a section as `docs/<topic>.md §3`.

## Provenance

- An authored doc opens with `Derived from:` — the journal entries whose
  decisions it reflects. Add per-section provenance when sections come
  from different entries.
- An authored doc cites journal entries for provenance. A journal entry
  cites a doc for current state only, never as authority.
- `docs/index.md` is the entrypoint. It carries `Derived from:` and links
  when it first projects a journal entry; an empty stub has neither.

## Format contract

- H1, then a blockquote thesis: one breath stating what the doc governs.
  State intent. Do not argue it. Argument lives in journals.
- Numbered sections (`## 3. Retreat`). The section is the citation unit.
- Atomic blocks: **bold noun phrase** → one sentence, max. The block is
  the unit of retrieval. Use prose only where no block form carries the
  signal.
- Tables for anything comparative or enumerable: stats, slots,
  protocols, curves.
- Fenced blocks for formulas, pseudocode, layouts.
- No argumentation paragraphs. No bridging text between sections. Link
  related docs. Do not restate them.
- No decorative `---`. Headers separate sections already.
- Prefer whole-file rewrites over patch edits.
- Prose within blocks follows `skills/ste-writing/`.

## Lifecycle

- Update an authored doc in place when an executed entry changes the
  model it describes. Do it in the same execution.
- Trivial fixes — typo, broken link — apply directly.
- No history sections, no changelogs. Git and journals hold history.
