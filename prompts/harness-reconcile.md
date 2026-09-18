# Reconcile an installed DWS base agent layer

Run this in a repo that already carries an older base layer: a
`journals/README.md` without a schema footer, or an `AGENTS.md` without a
Repository map. The invocation authorizes this reconcile and nothing else.

## Probe

- `journals/README.md`: schema footer? `Modifiers:` line? Which status
  modifiers does the corpus already use (scan status lines, list distinct
  modifiers)?
- `AGENTS.md`: Repository map section? Skills table rows?
- `skills/`: which of ste-writing, journal-craft, orientation exist?
- Nested `AGENTS.md` files? `docs/` present with a README?
- The location of any prior harness install or reconcile entry, for the
  record area.

## Steps

1. Copy `skills/journal-craft/` and `skills/orientation/` from the harness
   tree. Leave existing skills alone unless missing.
2. Append to `journals/README.md`: a `Modifiers:` line naming the modifiers
   the corpus already uses (omit when the corpus uses none beyond the base
   set), and the footer `Schema: 1. Adopted: <today>.` Today's date
   grandfathers every existing entry.
3. Merge the `## Repository map` section into `AGENTS.md` after `## Skills`.
   Scaffold zone rows from the `journals/` tree. Propose the scaffold. The
   user accepts or amends. The vocabulary bridge starts empty.
4. Add the Skills table rows for `journal-craft` and `orientation` when
   missing.
5. Run both lints from the repo root. Legacy findings are notes. Fix only
   findings on files this reconcile touched.
6. Record the reconcile under the area of the prior harness install or
   reconcile entry. Ask one bounded question only when no prior entry exists:
   record under which journal area? Default: `meta`. The entry is
   `journals/<area>/<NN>-harness-reconcile.md` with `Status: Executed.`,
   naming what landed, the adoption date, and the record-area choice. `NN`
   is the next free number in that area.

## Limits

Never rewrite a legacy entry. Never generate map content beyond scaffolded
zone rows the user accepted. No commits.
