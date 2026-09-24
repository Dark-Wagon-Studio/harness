# Reconcile an installed DWS base agent layer

Run this in a repo that already carries an older base layer: a
`journals/README.md` without a schema ledger or with a ledger below the
template's highest, an `AGENTS.md` without a Repository map, or a
`docs/README.md` whose §Provenance still opens every authored doc with
`Derived from:`. The invocation authorizes this reconcile and nothing else.
A step whose target is already current is a no-op.

## Probe

- `journals/README.md`: schema ledger? Which versions does it already adopt?
  `Modifiers:` line? Which status modifiers does the corpus already use (scan
  status lines, list distinct modifiers)?
- Does `journals/README.md` §Entry format show the `Schema: <N>.` line?
- The newest `Date:` among entries that carry no `Schema:` line. Step 2 dates
  its adoption after it.
- `AGENTS.md`: Repository map section? Skills table rows?
- `skills/`: which of ste-writing, journal-craft, orientation exist?
- Nested `AGENTS.md` files? `docs/` present with a README?
- `docs/README.md` §Provenance: does it still say a topic doc opens with
  `Derived from:`? Which topic docs and which `docs/index.md` carry a
  `Derived from:` header?
- The location of any prior harness install or reconcile entry, for the
  record area.

## Steps

1. Copy `skills/journal-craft/`, `skills/orientation/`, and
   `skills/ste-writing/` from the harness tree into the target, overwriting
   the target's copies. Leave *other* skills alone. Do this before step 2,
   always, even when the target already has these: a target must never hold
   a ledger line that its own lint is too old to read. An old lint reads
   the first `Schema:` line it finds, reports the schema below the one the
   repo claims, and never runs the entry checks. Nothing warns you. The
   ste-writing copy carries no lint, but it carries the quoted-speech
   exemption the receipt contract depends on.
   A copy can also destroy. A target may hold local evolution the harness
   tree lacks: its own toolchain wiring, its own checks. Diff each skill
   against the harness tree before and after the copy. Restore every
   target-only addition, keep the harness delta, and record both in the
   reconcile record.
2. Update `journals/README.md`. Work through every sub-step. None of them is
   made redundant by another.

   a. Add a `Modifiers:` line naming the modifiers the corpus already uses.
      Omit it when the corpus uses none beyond the base set. Skip this
      sub-step when a `Modifiers:` line exists. Never drop one.
   b. Compute the adoption date. Take the latest of three dates: today, one
      day after the newest entry that carries no `Schema:` line, and one day
      after the last date in the existing ledger. The second rule stops the
      date from landing on an entry already in the record, which would demand
      a `Schema:` line that nobody may add. The third keeps the ledger
      ascending, which the lint requires. A target whose earlier install ran
      on its own adoption date hits the third rule.
   c. Append the line for the newest schema the template adopts — today
      `Schema: 3. Adopted: <date>.` — directly under the last `Schema:`
      line, above any prose that follows it. When no `Schema:` line exists,
      write the ledger into a `## Schema` section. When a line already adopts
      that schema, skip this append only, and continue with (d) through (g):
      the ledger is append-only and never repeats a version.
   d. Never edit a `Schema:` line that exists. A schema-1 line stays, so every
      entry behind it keeps its schema-1 status and its error-level checks.
   e. Replace the §Schema prose with the text from
      `templates/journals-README.md`: the append-only rule, the strict-ascent
      rule, the three-step resolution with its two exceptions, the
      record-versus-draft rule, and the adoption-date rule. Keep the ledger
      lines the repo already has. Delete the template's own placeholder line
      for the newest schema, `Schema: 3. Adopted: <YYYY-MM-DD>.` — an
      unfilled placeholder does not match what the lint parses, so a stale
      one sits in the contract and the lint never reports it. Drop the
      sentence "The installer fills the adoption date": it is false in a
      reconciled repo.
   f. In §Entry format, add `Schema: <N>.` to the shape block after the
      `Date:` line, and add the **Schema line** note. Take both from
      `templates/journals-README.md`. Skip whichever of the two the file
      already has. Adding a second copy of either is a defect the lint cannot
      see, and it leaves the canonical shape block showing two `Schema:`
      lines while the lint errors on any entry that declares twice.
   g. Bring the rest of the contract up to the rules the newly-copied lint
      enforces at error level. The target may predate any of them. Sync these
      from `templates/journals-README.md`, and only these:

      - §Entry format notes: the `Depends on: none.` and area-qualified
        dependency rule (J04), and the `"1. **D1 — short name.**"` decision
        numbering rule (J05).
      - §Entry format notes: the **Ruling receipts** note, and §Style: the
        quoted-speech sentence — both when the target's ledger adopts
        schema 3 or higher, appended now or already present.
      - §Layout: the decision citation grammar, `<area>/<NN> D<k>`.
      - §Status: the modifier-declaration prose and the `Modifiers:` line
        contract.
      - §Workflow: "Run the journal-craft lint before landing the entry. Fix
        every error it reports."

      Change nothing else in the file. Keep the repo's own wording wherever
      it already states the rule. The target's prose differs from the
      template throughout, and most of that difference is the target's to
      keep.
3. Merge the `## Repository map` section into `AGENTS.md` after `## Skills`.
   Scaffold zone rows from the `journals/` tree. Propose the scaffold. The
   user accepts or amends. The vocabulary bridge starts empty.
4. Update the Skills table in `AGENTS.md`. Add the `journal-craft` and
   `orientation` rows when missing. When a `journal-craft` row exists and
   names an older schema, replace it with the row text from
   `templates/AGENTS.md`. `AGENTS.md` is the first file a session reads. A
   row that still says "schema 1" against a schema-2 lint misdirects every
   session that reads it. In §Docs lifecycle, replace the lint sentence
   that names only "Derived from:" targets with the sentence from
   `templates/AGENTS.md`, which names `From` and `Derived from:` targets.
5. Sync the docs provenance contract when the target has a
   `docs/README.md`. In §Provenance, replace the bullets that came from the
   template with the template's bullets. Keep the bullets the target added
   for its own doc kinds. A target rule that gives a doc kind a header
   naming its commissioning entries is a single-source rule. It matches
   the template and stays. Add the `From` line rule from the template's
   §Lifecycle when it is missing. Do not edit
   topic docs or `docs/index.md`. A doc recut is a design act. When the
   probe found `Derived from:` headers on topic docs or the index, tell the
   user to run `prompts/provenance-migrate.md` through a journal entry of
   their own.
6. Run both lints from the repo root. Legacy findings are notes. Fix only
   findings on files this reconcile touched. Then report the change in
   finding counts to the user, errors and notes separately. When a target had
   no ledger before this run, the new adoption date grandfathers its whole
   corpus, and every error-level finding on it becomes an advisory note. That
   is the intended effect of adopting a schema over an existing corpus, and
   the user decides whether to accept it.
7. Record the reconcile under the area of the prior harness install or
   reconcile entry. Ask one bounded question only when no prior entry exists:
   record under which journal area? Default: `meta`. The entry is
   `journals/<area>/<NN>-harness-reconcile.md` with `Status: Executed.`,
   naming what landed, the adoption date, the record-area choice, and the
   finding counts from step 6. `NN` is the next free number in that area. Use
   the entry format from the README you just wrote, including the `Schema:`
   line. Read the version the ledger gives for this entry's own date.

## Limits

Never rewrite a legacy entry. Never add a `Schema:` line to an entry already
in the record, whatever its date. This does not bind the reconcile record you
write in step 7: that entry is yours to write, and it carries the line. Never
edit a ledger line that exists. Never sync contract sections beyond the ones
step 2(g) names. In `docs/README.md`, sync only §Provenance and the
§Lifecycle `From` line rule. In `AGENTS.md`, sync only the Skills table
and the lint sentence of step 4. Never edit a topic doc or
`docs/index.md`. Never generate map content beyond scaffolded zone rows
the user accepted. No commits.
