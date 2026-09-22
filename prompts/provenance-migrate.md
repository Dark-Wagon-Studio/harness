# Migrate doc provenance from headers to section From lines

Run this in a target whose topic docs or `docs/index.md` still open with a
`Derived from:` header. Two preconditions hold first. Reconcile brings
both:

- The target's `docs/README.md` carries the §Provenance section from
  `templates/docs-README.md`.
- The target's `skills/orientation/` is the current harness copy, so the
  lint knows `From` lines and O09.

A doc recut is a design act. Run this procedure as the execution of a
journal entry in the target. The invocation does not authorize the recut
by itself. Materialize the entry first, with the audit table from step 2,
and execute it only on the user's instruction.

## Source rule

An entry is a source of a section when one of these holds:

- Its execution wrote rule text that the section still holds.
- The section cites one of its decisions as a rule.

These are not sources:

- An edit that renames words and changes no rule.
- A blank line, a heading, or a table separator.
- Prose that tells what an entry once did.
- An entry with a `Superseded by` modifier. Cite the successor that
  carries the decision.

## Steps

1. **List.** For each topic doc, list the numbered sections. Mark the
   sections that already open with a `From` line. Do not audit
   `docs/index.md` or a single-source doc: a doc whose whole body derives
   from the entries that commissioned it. Step 5 rules both.
2. **Audit.** For each section:
   1. Run `git blame` on the section's line range. Group the lines by
      commit. Skip blank lines and table separators.
   2. Map each commit to its journal entry. Use the commit header ref,
      or the entry that the commit message names.
   3. Read the diff of each candidate commit on this doc. Apply the
      source rule.
   4. Add the entries the section cites as rules.
   5. Record one row in the entry's audit table: doc, section, sources.

   If a section has no source, stop and escalate it to the user. If a
   superseded citation has no successor that names the decision as
   carried, escalate it. Do not pick a source in silence.
3. **Write From lines.** Open each numbered section with
   `From <entry>[, <entry>].` from the audit table. The line starts with
   plain `From ` at column 0, and a blank line follows it. Correct an
   existing `From` line that names a superseded entry, misses a source, or
   runs into the section body without a blank line.
4. **Replace superseded citations.** In `From` lines and inline decision
   citations, replace each superseded entry with the successor that
   carries the decision.
5. **Remove headers.** Delete the `Derived from:` line from each topic
   doc and from `docs/index.md`. A single-source doc keeps its header and
   gets no `From` lines.
6. **Check.**
   - Each numbered section of each topic doc opens with a `From` line,
     except in single-source docs.
   - The diff changes only headers, `From` lines, and superseded
     citations. No rule text changes.
   - `python3 skills/orientation/orientation-lint.py` reports no new
     error. O09 warns only on a `From` citation escalated in step 2.
7. **Record.** Append to the entry's execution log the changes to the
   audit table found during execution, the escalations, and the lint
   counts.
