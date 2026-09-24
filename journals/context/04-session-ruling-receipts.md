# Journal context/04 — session ruling receipts (schema 3)

Status: Executed.
Date: 2026-09-24. Depends on: context/02, context/03.
Schema: 3.

## Goal

An entry states a session ruling in the repo's voice: "The user ruled X."
The restatement is the author's interpretation. It carries no evidence. The
session's words die with the session, because no transcript lands in the
repo. This entry defines **schema 3**. Schema 3 is schema 2 plus one
element: the ruling receipt. A receipt quotes the user's words, verbatim,
next to the claim they support.

The line opened with an ask for "a clause in AGENTS.md where journal
entries/plans would include quotes from the user's request if applicable",
and moved to this repo by ruling:

> "@~/Workspace/dws/harness is the upstream convention. propose adding it
> there first."
> — the user, 2026-09-24

The form was ruled on before execution. The user ruled on 2026-09-24:
"there are no strict rules on the quote behavior except that it fits
within the schema, it's fully up to the harness materializing the entry."
The receipt's shape is the author's choice. This entry carries one inline
fragment above, one quote line above, and quotes the rulings that shaped
it. All three shapes are schema 3 at work.

## Current state (evidence, verified 2026-09-24)

| Site | Holds |
|---|---|
| monsoon `journals/` | 26 ruling-claim lines in 17 entries. All restatements. Zero receipts (grep for "the user ruled/asked/granted", verified 2026-09-24) |
| `journals/README.md:111-153` | the entry format. No element quotes the session |
| `templates/journals-README.md:109-151` | the same format, for targets |
| `skills/ste-writing/SKILL.md:8` | the exemption list: code, identifiers, command syntax. Speech is absent |
| `skills/journal-craft/journal-lint.py:66` | `SCHEMA_MAX = 2`. Checks J01 to J09. None touch quoted speech |
| `.agents/`, `.pi-subagents/` | gitignored scratch. No transcript is committed anywhere |

A ruling claim names the user as the source of a decision. Monsoon's
corpus holds them in this shape: "The user ruled growth for the early-game
offer", "The user asked for the preview, one button for both directions".
The claim asserts. The words that made the ruling appear nowhere. context/03
gave doc sections provenance through `From` lines. The journal side has no
counterpart.

## Gap inventory

| Gap | Severity | Dimension |
|---|---|---|
| A ruling claim carries no evidence. The restatement is interpretation. | high | conventions |
| The user's words are not retained. After the session dies, the phrasing cannot be recovered. | medium | conventions |
| A restatement can drift from the ask. Nothing catches the drift. | medium | conventions |
| ste-writing may rewrite a quote. The rewrite destroys the evidence. | medium | conventions |
| A quote and a restatement disagreeing leaves two voices with one authority. | medium | conventions |
| A forged receipt cannot be told from a real one by any deterministic check. | medium | tooling |

## Decisions

1. **D1 — a session ruling carries a receipt, in the author's chosen
   form.** When Goal or a Decision rests on what the user said in session,
   the entry quotes those words verbatim, next to the claim. Two shapes
   serve:

   - the key part, inline, in quotation marks;
   - the whole ruling, set out as a quote line with its date:

       > "<the user's words>"
       > — the user, <YYYY-MM-DD>

   No rule fixes the choice. The agent that materializes the entry picks
   the shape that serves the record: the inline fragment for the common
   case, the quote line when the phrasing or the scope is itself the
   evidence. The restatement may stand beside either shape. The receipt
   adds evidence. It does not replace the repo voice.
2. **D2 — quote live text only.** An entry quotes only words still
   present, verbatim, in the session context. A fragment is a verbatim
   fragment, not a paraphrase in quotation marks. When the phrasing is not
   recoverable, the entry states the ruling in repo voice and marks the
   restatement as such. A reconstructed quote is a forged receipt. It
   claims an authority it does not have. This rule is honesty, not
   mechanics. No lint enforces it. The contract states it.
3. **D3 — the entry governs.** The receipt is evidence of the ask. The
   Decisions are the ruling. When the two disagree, the decisions stand,
   and the disagreement is a defect: either the decision misread the ask,
   or the ask moved. Fix it by amending the entry or by a later entry. Two
   voices never share one authority.
4. **D4 — ste-writing exempts verbatim quotes.** A quote's value is its
   exact form. The skill's exemption list gains quoted speech, beside
   identifiers and command syntax.
5. **D5 — receipts attach to rulings.** The receipt serves the claim that
   carries authority: a ruling, a reversal, a scope grant, a refusal. An
   entry with no session ruling carries no receipt. Where a ruling claim
   ends and ordinary genesis begins is judgment, and the judgment sits
   with the author, per D1.
6. **D6 — capture the receipt at plan time.** The words are most
   recoverable when they are fresh. A plan that will be materialized
   captures its receipts while it is drafted. Materialization copies them
   in. journal-craft's writing rules state this.
7. **D7 — schema 3 is schema 2 plus the receipt.** The ledger appends one
   line at adoption. An entry declares `Schema: 3.` only after the ledger
   holds it. Schema 3 adds no error-level rule. Schema 2 checking does not
   change.
8. **D8 — the lint adds no receipt check.** The form is the author's
   choice, so no fixed grammar exists to check. The lint rises to schema 3
   and changes one rule: J07 skips quote lines, because verbatim speech
   may carry a date the contract did not write. An inline fragment with a
   malformed date stays under J07. The author resolves it by choosing what
   sits inside the quotation marks. The lint does not check that a ruling
   claim has a receipt: claim detection over prose is not deterministic,
   and the linter law reports only what resolves. The lint cannot verify
   that a quote is genuine. It never pretends to.
9. **D9 — this entry declares `Schema: 3.` and carries its own receipts.**
   Self-host. The defining entry is written under the schema it defines.
   Until adoption, the current lint reports one note on this entry and
   skips its other checks. That note is the correct state: proposed, not
   adopted.

## Execution phases

Ordered. Phase 1 defines the contract. Phases 2 to 7 follow it. Phase 8
gates the close.

### Phase 1 — `journals/README.md`

1. §Entry format notes: add one note, **Ruling receipts**, with the two
   shapes from D1, the freedom from D1, and the rules from D2, D3, and D5.
2. §Style: add the sentence "Quoted user speech keeps its exact form."
3. Append `Schema: 3. Adopted: <date>.` directly under the last `Schema:`
   line. Compute the date per context/02 D8, as amended: the latest of
   today, one day after the newest undeclared entry, and one day after the
   last ledger date. Computed today, that yields 2026-09-24. Do not edit a
   line that exists.

### Phase 2 — `templates/journals-README.md`

Mirror Phase 1 steps 1 and 2. The template ledger ships one line,
`Schema: 3. Adopted: <YYYY-MM-DD>.`, replacing the schema-2 placeholder
line. A fresh target starts at schema 3.

### Phase 3 — `skills/journal-craft/SKILL.md`

1. Writing rules: add the receipt rule, both shapes, the freedom, the
   honesty rule from D2, and the capture-at-plan-time rule from D6.
2. Change "schema 2" to "schema 3" in the heading of §Writing rules and in
   the front-matter `description`.

### Phase 4 — `skills/journal-craft/journal-lint.py`

1. Rename `SCHEMA_MAX = 2` to `SCHEMA_MAX = 3`.
2. J07 skips lines that open with `>`: quote lines carry verbatim speech,
   and a date inside one is evidence, not a contract date.
3. Docstring: name schema 3, and state the J07 exemption with its reason.
4. No new check. Exit codes do not change.

### Phase 5 — `skills/ste-writing/SKILL.md`

The scope sentence gains quoted speech: the skill does not apply to code,
identifiers, command syntax, or verbatim quotes.

### Phase 6 — `AGENTS.md`, `templates/AGENTS.md`

Both Skills tables, the `journal-craft` row: "against schema 2" becomes
"against schema 3".

### Phase 7 — `prompts/harness-init.md`, `prompts/harness-reconcile.md`

1. Init: entries the installer writes carry `Schema: 3.`, the install
   record included.
2. Reconcile, step 1: the copy list gains `skills/ste-writing/`. The
   mandated skills are ste-writing, journal-craft, and orientation. Other
   skills stay alone. The lint-before-ledger reason keeps its scope: it
   guards journal-craft.
3. Reconcile, step 2(c): the append writes the line for the newest schema
   the template adopts, not a number written into the prompt. Same for the
   placeholder deletion in step 2(e).
4. Reconcile, step 2(g): the sync list gains the schema-3 receipt
   surfaces: the §Entry format **Ruling receipts** note and the §Style
   quoted-speech sentence.
5. Reconcile, opening: a ledger below the template's highest is the
   reconcile condition, not only a schema-1 ledger.

### Phase 8 — Verify and close

1. Run `python3 skills/journal-craft/journal-lint.py`. Expect zero errors
   and zero notes.
2. Run `python3 skills/orientation/orientation-lint.py`. Expect zero
   errors.
3. Run both lints twice. Outputs must match.
4. Append the outcome to this entry's Execution log.

## Verification

- The ledger holds three lines, ascending. The schema-2 line is
  byte-identical to the line that exists today.
- This entry lints as schema 3 with zero findings. The pre-adoption note
  is gone.
- Scratch checks, discarded after the run: a quote line holding a
  non-ISO date reports no J07 finding. The same date in an inline quote
  reports one J07 error. A schema-2 entry holding the quote line reports
  nothing new.
- A ruling claim with no receipt reports no finding. The decline is
  stated, not silent.
- `grep -rn "SCHEMA_MAX = 2" skills/` returns nothing.
- `git status` lists exactly the files in the table below, plus this entry.

## Files this entry will touch

| File | Action |
|---|---|
| `journals/README.md` | edit (Phase 1) |
| `templates/journals-README.md` | edit (Phase 2) |
| `skills/journal-craft/SKILL.md` | edit (Phase 3) |
| `skills/journal-craft/journal-lint.py` | edit (Phase 4) |
| `skills/ste-writing/SKILL.md` | edit (Phase 5) |
| `AGENTS.md` | edit (Phase 6) |
| `templates/AGENTS.md` | edit (Phase 6) |
| `prompts/harness-init.md` | edit (Phase 7) |
| `prompts/harness-reconcile.md` | edit (Phase 7) |

## Risk & rollback

- **Forged receipts.** D2 is honesty and no lint enforces it. A determined
  forgery passes. The linter law reports what resolves. Genuineness never
  resolves from text. The contract states the rule and accepts the
  residual.
- **Clutter.** A full-prompt receipt buries the ruling it receipts. D1
  answers it: the form is the author's choice, the inline fragment is the
  common case, and the quote line serves when the phrasing is the
  evidence. The contract shows both shapes and states the freedom. It does
  not police the choice.
- **Two voices.** D3 settles precedence before the ambiguity can root.
- **Installed targets.** A target on schema 2 keeps working. The lint
  rises to schema 3 and keeps checking schema 2 unchanged. Schema 3 adds
  no error-level rule, so nothing new can fail. Reconcile moves a target
  when the user runs it.
- **Intimacy.** Quoted speech lands verbatim in the record, tone and typos
  included. The restatement already landed the content. A repo that does
  not want the words stays on schema 2.
- **Rollback.** A git revert in harness. The ledger line appends and never
  edits, so the revert restores schema 2 exactly.

## Non-goals

- No rewrite of any entry that exists. The schema-2 corpus stays
  receiptless.
- No fixed quote grammar, in the contract or in the lint. The form is the
  author's choice.
- No presence check in the lint. Natural-language claim detection is not
  deterministic.
- No quote of agent output. The agent's voice is already the entry's
  voice. Only the user's words are absent and worth receipting.
- No transcript capture. No session log is committed. The receipt is a
  selected quote, not an archive.
- No change to status grammar, decision numbering, dependency edges, or
  the schema-2 rules.
- No retroactive adoption. Targets adopt schema 3 through reconcile, when
  the user runs it.

## Execution log

2026-09-24. Executed on instruction, in the session that materialized the
entry. The user first amended it by ruling: receipts carry no fixed form.
The amendment landed before execution, while the entry was still
Provisional and uncommitted. All eight phases ran.

- Amendment: D1 states the author's freedom, with the inline fragment as
  the common case and the quote line as the exception. D5 loosened from a
  gate to guidance. The planned J10 form check is gone: no fixed grammar
  exists to check. The lint's one rule change became the J07 quote-line
  exemption.
- Phases 1 and 2: `journals/README.md` and
  `templates/journals-README.md` carry the **Ruling receipts** note, the
  §Style quoted-speech sentence, and the ledger at schema 3. The harness
  ledger appended `Schema: 3. Adopted: 2026-09-24.` Computed per context/02
  D8: latest of today 2026-09-24, 2026-09-19 (day after context/01, the
  newest undeclared entry), and 2026-09-21 (day after the last ledger
  date). The schema-1 and schema-2 lines are untouched. The template ships
  one placeholder line, `Schema: 3. Adopted: <YYYY-MM-DD>.`
- Phase 3: `skills/journal-craft/SKILL.md` gained the ruling-receipts
  writing rule. The heading and the `description` name schema 3.
- Phase 4: `SCHEMA_MAX = 3`. J07 skips lines that open with `>`, with the
  reason in a comment and in the docstring. No new check.
- Phase 5: `skills/ste-writing/SKILL.md` exempts verbatim quotes beside
  code, identifiers, and command syntax.
- Phase 6: both `AGENTS.md` Skills rows name schema 3.
- Phase 7: `prompts/harness-reconcile.md` gained the ste-writing copy in
  step 1, the newest-schema wording in 2(c) and 2(e), the receipt surfaces
  in 2(g), and the below-template-highest condition in the opening.
  `prompts/harness-init.md` needed no edit: its Phase 4 reads the schema
  version from the ledger the install just wrote, so a fresh install
  carries `Schema: 3.` through the template. The entry's Phase 7 item 1
  landed as a no-op. Gap filled and stated here rather than decided
  silently.
- Phase 8: `python3 skills/journal-craft/journal-lint.py` exits 0 with
  zero findings, summary "repo schema 3, adopted 2026-09-24, lint
  understands schema 3". `python3 skills/orientation/orientation-lint.py`
  exits 0 with zero findings. Both double runs print identical output. The
  pre-adoption J09 note on this entry is gone.

Scratch checks, all discarded after the run:

- A schema-3 entry holding a quote line with a month-name date reports no
  J07 finding. The exemption holds.
- A schema-3 entry holding a slash-form date inside an inline quote
  reports one J07 error. Inline quotes stay under the rule.
- A schema-2 entry holding the same quote line reports nothing new. The
  exemption is unconditional and misfires on no schema.

Writing this log hit the D8 residual once: the scratch-check sentences
first named the malformed dates inline, and the lint flagged them. The
fix was the one D8 allows: choose what sits inside the quotation marks.

`grep -rn "SCHEMA_MAX = 2" skills/` returns nothing. `git status` lists
the eight files in the table plus this entry, and `.zcodeignore`. That
file is the AI session tooling's own artifact, present before this line
of work began its edits and outside the entry's scope. It stays out of
the commit.
