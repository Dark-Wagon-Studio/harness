# Journal context/00 — schema 1 and the orientation layer

Status: Materialized.
Date: 2026-09-18. Depends on: none.

## Goal

Give harness three things, as one coherent layer:

1. **Schema 1** — a hard envelope for journal entries, carried by the planning
   contract and checked by an advisory lint. Qualified decision IDs, a declared
   status-modifier set, parseable dependency and supersession edges, a footer
   that declares the schema version and adoption date, and grandfathering that
   never rewrites a legacy entry.
2. **The orientation layer** — a `Repository map` priors section in `AGENTS.md`
   (zones, vocabulary bridge, authority procedure), a nested `AGENTS.md` stub
   for monorepo subtrees, and a curation workflow that maintains them.
3. **Two base-layer skills** — `journal-craft` (schema authoring plus its lint)
   and `orientation` (map curation plus a claim-resolution lint plus the
   measured evidence record that justifies the constraints).

Harness self-hosts its own contracts: this execution installs the revised
templates onto harness itself, and this entry is the first journal entry to
live under schema 1.

Two design laws govern every component:

- **Linter law.** Every deterministic tool in harness is an advisory lint. It
  reports claims that do not resolve. It never generates content, never scores,
  never ranks, and never gates. No CI enforcement exists anywhere in this layer.
- **Easy-route law.** A convention ships only with the machinery that makes
  compliance the low-effort path: skeleton defaults, probe-scaffolded drafts,
  trigger-proposed diffs that a human accepts. Discipline is the thing being
  optimized. The harness's job is to make the disciplined move the lazy one.

The pilot deployment is **monsoon**. That deployment is a separate entry in
monsoon's own journal and is not part of this execution.

## Current state (evidence, verified 2026-09-18)

### The harness tree

Verified by listing and reading every file. Harness contains:

- `README.md` — layout table, manual install steps, and the line "Not
  versioned. Installs track main."
- `templates/journals-README.md` — the planning contract. Entry format is a
  shape, not a schema: heading, status line, date line, section headings. The
  modifier set is "extensible by the project" with no declaration mechanism.
  Decisions carry no IDs. Nothing in the format is machine-checkable.
- `templates/AGENTS.md` — behavioral contract only: planning workflow, session
  rhythm, confirm gate, skills table (one row: `ste-writing`), docs lifecycle,
  where-truth-lives table. It carries no priors: no zone map, no vocabulary, no
  authority-resolution procedure.
- `templates/docs-README.md`, `templates/docs-index.md` — the docs authoring
  contract and entrypoint stub. Provenance is `Derived from:` headers with no
  resolution check.
- `skills/ste-writing/` — `SKILL.md` plus `ste-lint.py`. The pattern to follow:
  a skill is a `SKILL.md` with `name` and `description` frontmatter, an
  advisory self-lint, and the explicit statement that a checker fixes form and
  cannot make a hollow paragraph true.
- `skills/jtbd-coach/` — opt-in skill. Not touched by this entry.
- `modules/godot-project/` — opt-in module: fragments inserted into AGENTS.md,
  where-truth-lives rows appended, a regen script. Not touched by this entry.
- `prompts/harness-init.md` — the installer: Phase 1 probe, Phase 2 stop
  conditions and gates, Phase 3 install steps (3.1 journals README, 3.2 AGENTS
  merge, 3.2b docs, 3.3 git hygiene, 3.4 ste-writing, 3.5 jtbd, 3.6 godot),
  Phase 4 record, Phase 5 verify.
- No `journals/`, no root `AGENTS.md`, no `docs/` of its own. `.gitignore`
  covers `.agents/` and `**/.pi-subagents/*`.

One inconsistency: installer step 3.2 says "Fill _Project specifics_" but
`templates/AGENTS.md` carries no such section. This entry resolves it: the
Repository map scaffold replaces that instruction.

### Measured evidence (research digest)

Source: the dws agent-context research program, completed 2026-09-18. Full
record at `~/Workspace/dws/agent-context-hypotheses.md` and
`~/Workspace/dws/.agents/context-research/synthesis/` (both may be ephemeral).
All numbers are aggregates. No transcript content is quoted here.

| # | Finding | Number | Pass |
|---|---|---|---|
| E1 | Orientation tax: fresh sessions pay a fixed warm-up of reads before task work. Ladder repeats across sessions (brief → README → index → docs → entries). | ~12 reads; most-read files 83 / 49 / 29 times; replicated 5 of 6 repos | P1 |
| E2 | Reads dominate pattern search roughly 2:1. Counterexample: a flat 10-entry corpus runs 0.97:1, search-heavy. Behavior follows corpus shape, not agent nature. | 5 of 6 repos read-first | P1 |
| E3 | Zoning prior: agents path-scope pattern searches by hand, every session, and no artifact encodes the zones. | 84–100% in 5 of 6 repos | P1 |
| E4 | Write-side defects: decisions as unnumbered prose, parallel ID namespaces with live collisions (`R5` means two different things), dead pointers to moved paths, status modifiers drifting past the documented set, docs surfacing only a quarter of entries. | 31/37 and 88% unnumbered in two repos; 7 namespaces; 16 dead pointers; 5 vs 3 modifiers; ~25% doc reach | P2 |
| E5 | Naive lexical search reaches current authority on roughly two-thirds of representative queries. Misses decompose into four classes: vocabulary mismatch, identifier collision, authority-token mismatch, dead-path resolution. Vocabulary mismatch dominates everywhere. | 63–75% reach, 6 of 6 corpora | P3 |
| E6 | Index files mixed into the grep corpus are harmful: zero misses rescued, regressions in every corpus, noise up to +249%. Maps work read-first-whole or not at all. | 6 of 6 corpora | P3 |
| E7 | A glossary keyed to corpus words closes zero paraphrase queries. The bridge must be inbound: query word → corpus word. | 0/8 in every corpus | P3 |
| E8 | Agent-in-the-loop: fresh agents solved every fixed-pattern "miss" with plain grep and reading. Zero misdirection. Retrieval correctness is not the binding constraint for competent agents on bounded queries. | 26/26 trials | P5 |
| E9 | Map-first consumption: no correctness gain, no cost gain. A 27 KB map costs ~7k input tokens per trial plus follow-on reads. | 3 query pairs, consistent direction | P5 |
| E10 | Generated maps decay same-day. The study's own index was stale within hours; the eval's own ground truth aged past its anchors. | 5 trials flagged; same-day | P5 |
| E11 | External: developer-written context files measure +4% success and −20 to −29% runtime. Machine-generated ones measure −3%. | 438-instance study | brief |
| E12 | Drift concentrates at area seams and is journaled. Two decay layers: spatial (where things live, cheap to verify) and authority (what is current, must point at records). Dead pointers accumulate where move-prose is weak. | 6 of 6 corpora | P4 |
| E13 | Harness delivery seams (per-agent memory injection, missions store, refinement overlays) are dormant. Missions are write-only telemetry. | 8 of 8 beds; 515/515 records empty payload | P6 |

### Reading of the evidence

The journals are already a memory system. The failures are packaging, delivery,
and decay. For competent agents, retrieval correctness is not binding (E8), so
nothing in this layer exists to fix correctness. The measured costs are
orientation (E1, E3), decay (E10, E12), and write-side defect classes (E4, E5).

Generated standing artifacts are the worst option available: stale same-day
(E10), harmful as search fodder (E6), and the external evidence prices
generated context below nothing (E11). Therefore this layer ships no
generation. The durable lever is write-side discipline made cheap: the entry
emits its own structure (schema), a human-curated priors section carries what
every session otherwise reconstructs by search (the map), and linters check
that curated claims resolve. `AGENTS.md` is the delivery channel that already
exists: every session reads it at start, by construction.

## Gap inventory

| Gap | Severity | Dimension |
|---|---|---|
| Entry format is a shape, not a schema. Unnumbered decisions are invisible to ID lookup. 31/37 entries in the baseline repo carry unnumbered prose. | high | conventions |
| Status modifiers are open-ended with no declaration. Drift measured at 5 used vs 3 documented. | high | conventions |
| No qualified decision citation. Seven parallel namespaces with a live collision in the baseline repo. | high | conventions |
| AGENTS.md template carries no priors. Sessions pay a ~12-read warm-up ladder reconstructing them. | high | docs |
| The zoning prior is rebuilt by hand every session (84–100% of searches path-scoped). No artifact holds it. | high | docs |
| No inbound vocabulary bridge. Corpus-keyed glossaries measured useless (0/8). | medium | docs |
| No maintenance trigger for repo-specific sections. Seam files decay fastest and nothing notices. | medium | tooling |
| No claim-resolution check for curated files (AGENTS.md paths, docs links, Derived-from targets). | medium | tooling |
| Installer scaffolds behavior but not priors; references a "Project specifics" section the template lacks. | medium | installer |
| Schema needs a version identity while harness itself stays unversioned. | low | installer |

## Decisions

1. **D1 — Linter law.** All deterministic code shipped by harness is advisory
   lint: it reports claims that do not resolve, in `path:line code message`
   form. It never writes files, generates content, computes scores or metrics,
   or gates anything. Basis: E6, E10, E11, and the program's own flagship
   instrument producing a confident wrong answer when read as an authority.
2. **D2 — Easy-route law.** Every convention in this layer ships with the
   machinery that makes compliance the low-effort path. Schemas ride on
   skeletons the writer already copies. Maps ride on probe-scaffolded drafts
   and trigger-proposed diffs a human accepts. Basis: E1, E3, E11.
3. **D3 — Schema 1 envelope.** The planning contract gains a machine-checkable
   envelope: qualified decision IDs, declared modifiers, parseable dependency
   and supersession edges, a schema footer, and adoption-date grandfathering.
   The prose body stays free. Enforcement is the journal-craft lint run at
   materialization time. Basis: E4, E5, E12.
4. **D4 — Entry-local decision IDs.** Decisions number from 1 inside their
   entry, written `1. **D1 — short name.** sentence.` and cited
   `<area>/<NN> D<k>`. No global namespace, no registry. The entry qualifies
   the number. Basis: E4, E5.
5. **D5 — Declared modifiers.** A repo extends the modifier set with one
   `Modifiers:` line in its `journals/README.md`. The lint accepts only the
   base set plus declared names. Basis: E4.
6. **D6 — Repository map as the priors section.** `AGENTS.md` carries zones,
   an inbound vocabulary bridge, and the authority-resolution procedure. It
   never carries decisions, answers, or generated text. Root budget 40 lines.
   Human-curated only: deterministic derivation of map content is rejected.
   Basis: E1, E3, E7, E11.
7. **D7 — Two base-layer skills.** `journal-craft` and `orientation` always
   install. They follow the ste-writing pattern: SKILL.md plus advisory lint.
   Basis: D1, D2.
8. **D8 — Nested AGENTS.md stub.** Subtrees may carry a nested file with local
   zones and vocabulary only, 15 lines or fewer. The agent harness loads the
   whole ancestor chain at session start, so nested files tax every session in
   the subtree. Basis: E12 (seam decay), pi context-file loading semantics.
9. **D9 — Schema integer versioning inside an unversioned harness.** Each
   repo's `journals/README.md` footer states `Schema: N`. Harness stays
   unversioned as a product. The lints embed the highest schema they
   understand and report when they meet a newer one.
10. **D10 — Pilot is monsoon, recorded elsewhere.** This entry changes harness
    only. Monsoon deploys via its own journal entry. No repo is retrofitted by
    this work.

## Execution phases

Ordered. Phases 1 and 2 revise templates before any self-hosting or install
logic references them.

### Phase 1 — Revise `templates/journals-README.md` (schema 1)

Six edits. Anchor text is quoted from the current file.

1. In §Status, replace the modifier bullet:

   Old: `Modifiers — optional, comma-separated, extensible by the project:`

   New: `Modifiers — optional, comma-separated. The base set is:`

   Then, directly under the examples paragraph at the end of §Status, add:

   ```
   A project extends the modifier set by declaring it. Add one line to this
   README, directly under the examples above:

       Modifiers: <name>, <name>.

   The journal-craft lint accepts the base set plus the declared names, and
   nothing else.
   ```

2. In the §Entry format skeleton, replace the date line:

   Old: `Date: <YYYY-MM-DD>. Depends on: <prior entries or docs, if any>.`

   New: `Date: <YYYY-MM-DD>. Depends on: <area>/<NN>, <area>/<NN>.`

   Add one note line to the notes list under the skeleton: `Use
   "Depends on: none." when the entry stands alone. Every dependency is an
   area-qualified entry path.`

3. In the same notes list, extend the Decisions note:

   Old: `- **Decisions** — only when a cross-cutting choice needs recording.
     Drop the section when there is none.`

   New: `- **Decisions** — only when a cross-cutting choice needs recording.
     Drop the section when there is none. When present, number every item:
     "1. **D1 — short name.** The decision sentence." Numbers run from 1
     inside the entry.`

4. In §Layout, extend the citation paragraph. After "The number is only
   meaningful together with its directory.", add: `Cite a decision as
   "<area>/<NN> D<k>", for example "gameplay/02 D3". Never cite a bare
   decision ID. The entry qualifies it.`

5. In §Workflow step 2 (Materialize), append: `Run the journal-craft lint
   ("skills/journal-craft/") before landing the entry. Fix every error it
   reports.`

6. Add a final §Schema section at the end of the file:

   ```
   ## Schema

   This contract carries a schema version. The footer below states it.

   Schema: 1. Adopted: <YYYY-MM-DD>.

   The installer fills the adoption date. Entries dated before the adoption
   date are legacy. The lint reports legacy findings as notes. No one rewrites
   a legacy entry to satisfy the schema. Entries dated on or after the
   adoption date follow schema 1 in full.
   ```

   In the template, the `Adopted:` value stays the placeholder
   `<YYYY-MM-DD>`. Installers and self-hosting fill it.

### Phase 2 — Revise `templates/AGENTS.md`, add `templates/AGENTS-nested.md`

Edits to `templates/AGENTS.md`:

1. Replace the Skills table with three rows:

   ```
   | Skill           | Use                                                                                                                                     |
   | --------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
   | `ste-writing`   | Rewrite engineering prose (journal entries, docs, PR text, comments) into STE. Mandated for journal entries and for new or edited text in `docs/` and root-level docs. |
   | `journal-craft` | Write and check journal entries against schema 1: qualified decision IDs, status grammar, dependency edges. Mandated when materializing or editing a journal entry. |
   | `orientation`   | Curate the Repository map (zones, vocabulary bridge, authority procedure) and check curated claims. Runs on area moves, new jargon, and lint findings. |
   ```

2. Insert a new `## Repository map` section between `## Skills` and
   `## Docs lifecycle`:

   ```
   ## Repository map

   Priors for orientation: where things live and how words map. Sessions read
   this at start instead of reconstructing it by search. The `orientation`
   skill maintains it: the skill proposes diffs, a human accepts.

   | Area | Holds |
   | --- | --- |

   ### Vocabulary bridge

   Inbound direction: what a person asks, what the record calls it.

   | You might say | The record says |
   | --- | --- |

   ### Resolving authority

   1. Read the entry's `Status:` line. Follow "Superseded by <area>/<NN>" to
      the successor.
   2. Entries outrank docs and code. When they disagree, fix the derived
      artifact or supersede the entry.

   This section carries where things live and how words map. It never carries
   decisions, answers, or generated text. Keep the root map within 40 lines.
   Nested `AGENTS.md` files stay within 15.
   ```

   The install-time scaffold fills the tables. Empty tables are legal until
   the repo grows content.

3. In §Docs lifecycle, append: `Provenance targets must resolve. The
   "orientation" lint checks "Derived from:" targets and doc links.`

4. In §Where truth lives, append one row: `| Entry schema |
   journals/README.md |`

New file `templates/AGENTS-nested.md`:

```
# AGENTS.md (nested)

Entry point for AI work in this subtree. The root `AGENTS.md` carries the
workflow and the repository map. This file adds only what is local.

## Local map

| Area | Holds |
| --- | --- |

### Local vocabulary

| You might say | The record says |
| --- | --- |

Rules: 15 lines or fewer in total. No workflow text, no decisions, no answers.
All paths are repo-root relative. Maintain with the `orientation` skill: it
proposes, a human accepts.
```

### Phase 3 — Self-host harness contracts

Harness installs its own revised layer. The repo that ships the contracts
lives under them.

1. Copy the revised `templates/journals-README.md` to `journals/README.md`.
   Fill the footer: `Schema: 1. Adopted: <execution date>.` Omit the
   `Modifiers:` line (harness declares no extensions).
2. Copy the revised `templates/AGENTS.md` to `AGENTS.md`. Fill the Repository
   map from the harness tree:
   - Zones: one row per top-level directory (`templates/`, `skills/`,
     `modules/`, `prompts/`, `journals/`), one line each on what it holds.
   - Vocabulary bridge: carry the pairs the tree actually uses, for example
     "harness tree" (the clone an installer reads) versus "target" (the repo
     being installed into), and "lint tier" (advisory check, never a gate).
   - Authority steps: keep the template text verbatim.
   Propose the filled map in-session. The user accepts or amends before it
   lands. This is the propose-accept protocol of the orientation skill,
   applied once.
3. Verify `.gitignore` covers `.agents/` and `**/.pi-subagents/*`. It does
   today. Append nothing unless the check fails.
4. `skills/` is already the canonical home. No copy is needed.

This entry (context/00) is dated 2026-09-18. It must satisfy the schema the
same day the footer declares. Check it with the lint in Phase 8.

### Phase 4 — Add `skills/journal-craft/`

Two files.

`skills/journal-craft/SKILL.md`:

```
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
```

`skills/journal-craft/journal-lint.py` — write from this spec:

- Python 3, standard library only. No network. Deterministic: two runs on the
  same tree print identical output. Embed `SCHEMA_VERSION = 1`.
- Inputs: the `journals/` tree and `journals/README.md` (schema footer,
  optional `Modifiers:` line). Read the adoption date and declared modifiers
  from the README.
- Checks:

  | Code | Check | Failure class |
  |---|---|---|
  | J01 | Filename matches `<NN>-<slug>.md`, two digits. The lowest number in each directory is `00`. Gaps after the first entry are notes. | error / note |
  | J02 | Heading parses as `# Journal <area>/<NN> — <description>` and matches the file's path. | error |
  | J03 | Status line is the second non-empty line. Primary is from the closed set. Modifiers are base or declared. `Superseded by <area>/<NN>` targets exist. | error |
  | J04 | Date/Depends line present. Date is ISO 8601. Every `Depends on` target exists. `none` is legal. | error |
  | J05 | Every `## Decisions` item matches `N. **DN — name.**`. Numbers sequential from 1, unique within the entry. Legacy entries with unnumbered decision prose: note. | error / note |
  | J06 | Entry path nests at most one level under an area (two path components under `journals/`). | error |
  | J07 | Front-matter dates are ISO 8601 everywhere they appear. | error |
  | J08 | `journals/README.md` carries the `Schema: N. Adopted: <date>.` footer. Footer version above the lint's `SCHEMA_VERSION` prints a notice and exits 2. | error / notice |

- Grandfathering: every check classifies each finding as error (entry dated on
  or after adoption) or note (dated before). The summary states both counts.
- Output format, one finding per line, then a summary line:

  ```
  <path>:<line> error J03 status line does not parse: <excerpt>
  <path>:<line> note  J05 legacy entry: decisions unnumbered
  summary: 2 errors, 1 note (schema 1, adopted 2026-09-18)
  ```

- Exit codes: 1 when errors exist, 2 on schema-version notice, 0 otherwise.
  Notes never fail the run.

### Phase 5 — Add `skills/orientation/`

Three files.

`skills/orientation/SKILL.md`:

```
---
name: orientation
description: Curate the Repository map in AGENTS.md (zones, vocabulary bridge, authority procedure) and check curated claims against the tree. Use when an area is created, moved, or renamed, when a term keeps causing confusion, when orientation-lint reports a claim that does not resolve, or when a nested AGENTS.md is considered.
---

# orientation

`AGENTS.md` carries priors: where things live, how words map, how authority
resolves. Sessions read it at start. The map replaces the warm-up search. This
skill maintains the map and checks it.

The map is human-curated. Tools in this skill check claims and propose diffs.
A human accepts every change. Nothing generates map content beyond scaffolds
the user accepts line by line.

## What belongs in the map

1. Zones: one row per area, what lives there.
2. Vocabulary bridge, inbound direction only: the words a person or agent
   says, mapped to the words the record uses.
3. Authority procedure: the steps to find what is current. Never the current
   answers themselves.

## What never belongs

Decisions, answers, summaries, pre-fetched content, generated text. When a
journal entry owns a fact, the map points at the place, never the content.
Budgets: root map 40 lines or fewer. Nested `AGENTS.md` files 15 lines or
fewer in total.

## Triggers

Run this skill when:

- an area is created, moved, or renamed,
- a term causes a repeated confusion between query words and record words,
- orientation-lint reports a claim that does not resolve,
- a new recurring citation form or namespace appears.

## Protocol

1. Surface the fact: what changed, or what fails to resolve.
2. Draft the smallest diff that keeps the map true.
3. The human accepts, edits, or rejects. No unaccepted writes.

## Checking

Run `python3 skills/orientation/orientation-lint.py` from the repo root. It
checks path claims in every Repository map, relative links and
`Derived from:` targets in `docs/`, citation forms, and budgets. Errors are
claims that do not resolve. Fix the claim or strike it.

## Why the constraints hold

`references/evidence.md` records the measured basis for every constraint in
this skill. Read it before loosening any of them.
```

`skills/orientation/orientation-lint.py` — write from this spec:

- Python 3, standard library only. Deterministic. Same output shape and exit
  semantics as the journal lint (errors exit 1; budget and duplication
  findings are warnings and never fail).
- File discovery: prefer `git ls-files` (tracked files only, which excludes
  generated and ignored trees). Fall back to a walk that skips `.git`,
  `.agents`, `.pi`, `.pi-subagents`, `node_modules`, `.venv`, `docs/godot-api`,
  and any `docs/<generated>/` named in the repo's docs README.
- Checks:

  | Code | Check | Class |
  |---|---|---|
  | O01 | Every backticked path in a `## Repository map` or `## Local map` table resolves from the repo root. | error |
  | O02 | Vocabulary bridge rows that cite a path or entry: the citation resolves. | error |
  | O03 | Every `<area>/<NN>` citation inside map tables and the where-truth-lives table resolves to a journal entry. | error |
  | O04 | Root map section is 40 lines or fewer. Nested `AGENTS.md` files are 15 lines or fewer. | warning |
  | O05 | Nested map rows that duplicate root rows. | warning |
  | O06 | Relative markdown links in `docs/*.md` resolve. | error |
  | O07 | Every `Derived from:` target in `docs/*.md` resolves to a journal entry. | error |
  | O08 | A file carrying a Repository map carries the negative-list line ("It never carries decisions, answers, or generated text."). | warning |

- Output format matches the journal lint: `<path>:<line> <class> O<NN>
  <message>`, then a summary line with counts.

`skills/orientation/references/evidence.md`:

```
# Evidence record — orientation layer constraints

Curated digest of the dws agent-context research program (completed
2026-09-18). Source of record: `~/Workspace/dws/agent-context-hypotheses.md`
and `.agents/context-research/synthesis/` at the dws root. Those paths are
ephemeral. This file is the durable copy. Aggregates only.

- Orientation tax: fresh sessions pay a fixed warm-up (~12 reads) before task
  work, replicated in 5 of 6 repos. The map section exists to delete this
  cost, not to improve correctness.
- Zoning: 84–100% of pattern searches are path-scoped by hand, every session,
  in 5 of 6 repos. Zones belong in the map because no other artifact holds
  them.
- Vocabulary bridge direction: glossaries keyed to corpus words closed 0/8
  paraphrase queries in every corpus tested. Only the inbound direction
  (query word → record word) can bridge. Hence the bridge table's direction.
- Map content stays human-curated: developer-written context measures +4%
  success and −20 to −29% runtime. Machine-generated context measures −3%.
  Deterministic derivation was considered and rejected: untested, and any
  standing derived artifact acquires authority it cannot defend.
- Generated maps decay same-day (measured on the study's own index). No
  generation ships in this layer. Maintenance is trigger-based curation.
- Index files as grep fodder are harmful (zero misses rescued, noise up to
  +249%, 6 of 6 corpora). This layer therefore ships no index files at all.
- Agent retrieval correctness is not binding: fresh agents solved 26/26
  fixed-pattern "misses" with grep alone. Nothing here tries to fix search.
- Drift concentrates at area seams and is journaled. Nested AGENTS.md files
  are seam artifacts: they stay small (15 lines) and are maintained on the
  orientation skill's move trigger.
- All deterministic tools here are linters (claim resolution, advisory). The
  research program's own flagship instrument produced a confident wrong
  answer when read as an authority. Instruments advise. Humans decide.

Read this file before loosening any constraint in the orientation skill. If
new evidence contradicts a row, change the row and say why, in place.
```

### Phase 6 — Extend the installer, add the reconcile prompt

Edits to `prompts/harness-init.md`:

1. Phase 1 probe, add three facts:
   - Does `journals/README.md` carry a `Schema:` footer or a `Modifiers:`
     line? (A convention may already be installed — Phase 2 stop conditions
     already govern this. The probe fact is for the footer fill.)
   - Nested `AGENTS.md` files anywhere in the tree? List them.
   - The `journals/` area directories, for map scaffolding.
2. Step 3.1, append: fill the footer placeholder `<YYYY-MM-DD>` in the copied
   `journals/README.md` with today's date. The adoption date grandfathers any
   pre-existing corpus.
3. Step 3.2, replace the "Fill _Project specifics_" paragraph with a scaffold
   instruction: draft Repository map zone rows from the probed journals areas
   (an empty corpus yields empty tables, which are legal). Propose the
   scaffold in-session. The user accepts, amends, or defers the tables. The
   vocabulary bridge starts empty. The where-truth-lives fill from the probe
   stays as written.
4. New step 3.4b: copy `skills/journal-craft/` from the harness tree. Missing
   from the harness tree: report and continue, mirroring the 3.4 fallback.
5. New step 3.4c: copy `skills/orientation/`. Same fallback.
6. In the 3.2 merge list, add the _Repository map_ section to the sections
   merged from the template.
7. Phase 4, append to what the install entry records: the schema adoption
   date, and the map scaffold outcome (accepted, amended, or deferred empty).
8. Phase 5 verify, add:
   - `journals/README.md` carries the schema footer with the install date.
   - `skills/journal-craft/SKILL.md` and `skills/orientation/SKILL.md` exist.
   - `AGENTS.md` carries a `## Repository map` section. Empty tables are
     legal at install.
   - Both lints run from the repo root. Expect zero errors. Legacy findings
     on a pre-existing corpus are notes.
   - Mention `templates/AGENTS-nested.md` in the final summary as available
     for subtrees. Do not install it unless the user asks.

New file `prompts/harness-reconcile.md`:

```
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
6. Record `journals/harness/NN-harness-reconcile.md` with `Status: Executed.`,
   naming what landed and the adoption date.

## Limits

Never rewrite a legacy entry. Never generate map content beyond scaffolded
zone rows the user accepted. No commits.
```

### Phase 7 — Update `README.md`

1. Layout table, add four rows:

   ```
   | `templates/AGENTS-nested.md` | The nested AGENTS.md stub for monorepo subtrees |
   | `skills/journal-craft/` | The journal schema skill (canonical home, mandated) |
   | `skills/orientation/` | The Repository map curation skill (canonical home, mandated) |
   | `prompts/harness-reconcile.md` | The upgrade prompt for repos with an older base layer |
   ```

2. Manual install steps: insert after the ste-writing copy — copy
   `skills/journal-craft/` and `skills/orientation/`, fill the schema footer
   date, and scaffold the Repository map. Add a closing pointer: existing
   installs upgrade via `prompts/harness-reconcile.md`.
3. Replace the versioning section with:

   ```
   ## Versioning

   Not versioned as a product. Installs track `main`. One exception: the
   journal entry schema carries an integer, stated in each repo's
   `journals/README.md` footer (`Schema: 1`). The lints embed the highest
   schema they understand and report when they meet a newer one.
   ```

4. Add a short Design section after Layout:

   ```
   ## Design

   Two laws govern this repo. Every deterministic tool is an advisory lint:
   it reports claims that do not resolve, and never generates, scores, or
   gates. And every convention ships with the machinery that makes compliance
   the low-effort path. Harness ships no index builders, no metrics, no
   generated maps, no CI gates. The measured basis lives in
   `skills/orientation/references/evidence.md`.
   ```

### Phase 8 — Lint harness, close the loop

1. Run `python3 skills/journal-craft/journal-lint.py` from the harness root.
   Expect zero errors. This entry (context/00) is dated on the adoption day
   and must pass in full: heading, status line, date/depends line, decision
   numbering D1–D10.
2. Run `python3 skills/orientation/orientation-lint.py`. Expect zero errors.
   Fix any unresolved claim the Phase 3 map carries.
3. Append the outcome to this entry's Execution log: what landed, lint
   results, any deviation and why.

## Verification

- Both lints run from the harness root with exit 0 and zero errors.
- This entry passes journal-lint as a post-adoption entry.
- Every anchor edit from Phases 1, 2, 6, and 7 is present: grep for
  `Schema: 1`, `Modifiers:`, `Repository map`, `D<k>` citation grammar,
  the three-row Skills table, the reconcile pointer, and the Design section.
- The installer references sections that exist in the templates it copies:
  `## Repository map` in `templates/AGENTS.md`, the footer block in
  `templates/journals-README.md`, both new skill directories.
- `templates/AGENTS-nested.md`, `prompts/harness-reconcile.md`, and both
  skills exist at the paths the README layout table names.
- Harness `AGENTS.md` exists, carries the map, and its zone rows resolve.
- Determinism: each lint run twice prints identical output.
- `git status` lists exactly the files below. Nothing else.

## Files this entry will touch

| File | Action |
|---|---|
| `templates/journals-README.md` | edit (Phase 1) |
| `templates/AGENTS.md` | edit (Phase 2) |
| `templates/AGENTS-nested.md` | new (Phase 2) |
| `journals/README.md` | new, self-host (Phase 3) |
| `AGENTS.md` | new, self-host with filled map (Phase 3) |
| `skills/journal-craft/SKILL.md` | new (Phase 4) |
| `skills/journal-craft/journal-lint.py` | new (Phase 4) |
| `skills/orientation/SKILL.md` | new (Phase 5) |
| `skills/orientation/orientation-lint.py` | new (Phase 5) |
| `skills/orientation/references/evidence.md` | new (Phase 5) |
| `prompts/harness-init.md` | edit (Phase 6) |
| `prompts/harness-reconcile.md` | new (Phase 6) |
| `README.md` | edit (Phase 7) |

## Risk & rollback

- Template revisions are the main risk: installed repos track `main` and
  reconcile from it. Rollback is a git revert in harness. Installed repos are
  untouched until someone runs the reconcile prompt in them.
- The lints are new code with exact specs but no tests. Phase 8 runs them on
  harness itself. The entry is deliberately schema-clean so a lint bug shows
  as a false positive, not a hidden pass. Fix the lint, not the entry, when
  the spec and the entry disagree — the spec is D3–D5.
- Curated maps can go semantically stale while every claim still resolves.
  This is accepted, not solved: the orientation skill's triggers are the
  guard. No deterministic tool can catch a true claim that stopped being the
  right claim.
- Schema adoption confusion: the footer date decides legacy versus current.
  One date, one source, no ambiguity. Repos that reconcile later simply adopt
  later.
- Evidence paths at the dws root may vanish. The durable copy is
  `skills/orientation/references/evidence.md`. This entry's digest is the
  second copy.

## Non-goals

- No deployment to monsoon or any other repo. The pilot is a separate journal
  entry in monsoon.
- No retrofit of legacy entries anywhere, ever.
- No index builders, corpus miners, metrics, coverage numbers, or generated
  docs or maps. No standing measurement regime of any kind.
- No CI gates, no enforcement beyond advisory lint and human acceptance.
- No changes to `ste-writing`, `jtbd-coach`, or `modules/godot-project`.
- No per-agent memory seam work (MEMORY.md, missions, overlays). Dormant
  seams stay dormant.
- No `docs/` tree for harness itself in this entry.
- The research program's scratch stays outside harness, at the dws root.

## Execution log

2026-09-18. Executed. All eight phases landed.

- Phases 1, 2, 6, and 7: every ordered edit applied; every anchor matched.
- Phase 3: journals/README.md self-hosted with `Schema: 1. Adopted:
  2026-09-18.` and no `Modifiers:` line. `.gitignore` already covered both
  patterns; nothing appended. The Repository map was proposed filled per
  the Phase 3 protocol. The user chose empty tables. Root `AGENTS.md` is
  therefore byte-identical to `templates/AGENTS.md`. Zone-row verification
  is vacuous until the tables fill. The `orientation` skill fills them
  later.
- Phases 4 and 5: both skills created. The SKILL.md files and evidence.md
  are byte-verbatim from this entry. Both lints written from spec.
- Phase 8: journal-lint reports 0 errors, 0 notes. orientation-lint reports
  0 errors, 0 warnings. Both print identical output on double runs. This
  entry passes in full as a post-adoption entry.

Reviewed fixes (fresh-context review round, then one fix pass):

- journal-lint J06 first rejected line-nested entries that the planning
  contract legalizes. Fixed: two or three components under `journals/`, at
  most one line level under an area. The risk clause held — the lint was
  fixed, not the entry.
- The declared-modifiers parser read the indented `Modifiers:` example in
  journals/README.md as a declaration. The regex now anchors at column 0.
- journal-lint: dotted dates bounded to real day and month values, so
  version-like tokens pass; unreadable files report findings instead of
  tracebacks; the J02 message names the filename when the filename is the
  defect.
- orientation-lint: backticked `Derived from:` targets are checked;
  templates/ is skipped in nested AGENTS.md discovery; O08 fires on any
  file carrying a Repository map without the negative-list line; O05
  covers vocabulary rows.
- Coherence fixes, inside files this entry touches: the installer
  always-installs list names journal-craft and orientation; the README
  manual merge list names the Repository map; the README intro no longer
  implies every skill is opt-in.

Known, deferred:

- templates/AGENTS-nested.md is 18 lines against its own 15-line rule. The
  Phase 2 block is ordered verbatim, so this entry ships it as written. An
  installed stub earns an O04 warning until a later entry trims it.
- `git status` carries this entry file itself alongside the touched-file
  table. The table lists what the phases touch; the entry is the actor.
