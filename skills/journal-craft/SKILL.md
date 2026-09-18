---
name: journal-craft
description: Write and check journal entries against schema 1 - qualified decision IDs, status grammar, dependency and supersession edges, grandfathering. Use when materializing a journal entry, editing one, checking entries with the lint, or citing a decision.
---

# journal-craft

Journal entries follow the schema in the repo's `journals/README.md`. This
skill writes entries that comply and checks entries that exist. The check is a
lint. It reports claims that do not resolve. It never rewrites, scores, or
gates.

## Writing rules (schema 1)

- Filename: `<NN>-<slug>.md`. Numbering starts at `00` in each directory.
- Front matter, in order:
  1. `# Journal <area>/<NN> — <one-line description>`
  2. `Status: <primary>[, <modifier>[, ...]].` Primary is one of Materialized,
     Decided, Executed. Modifiers come from the base set (Provisional,
     On hold, Superseded by `<area>/<NN>`) or the repo's declared
     `Modifiers:` line in `journals/README.md`.
  3. `Date: <YYYY-MM-DD>. Depends on: <area>/<NN>, <area>/<NN>.` Use
     `Depends on: none.` when the entry stands alone.
- Decisions: number every item in `## Decisions` as
  `1. **D1 — short name.** The decision sentence.` Numbers run from 1 inside
  the entry. Drop the section when no cross-cutting choice needs recording.
- Citation grammar: `<area>/<NN> §<k>` for a section, `<area>/<NN> D<k>` for a
  decision. Never cite a bare ID. The entry qualifies it.

## Checking

Run `python3 skills/journal-craft/journal-lint.py` from the repo root before
landing an entry. Fix every error. Notes on legacy entries (dated before the
adoption date in `journals/README.md`) are information, not work.

## Grandfathering

`journals/README.md` closes with `Schema: 1. Adopted: <date>.` Entries dated
before that day are legacy. The lint reports them as notes. Never rewrite a
legacy entry to satisfy the schema.
