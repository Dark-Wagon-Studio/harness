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
checks path claims in every Repository map, relative links, `Derived from:`
targets, and section `From` targets in `docs/`, citation forms, and
budgets. Errors are claims that do not resolve. Fix the claim or strike it.
A warning names a `From` target that is superseded: cite the successor
that carries the decision. A `Derived from:` header records a commission
and never warns.

## Why the constraints hold

`references/evidence.md` records the measured basis for every constraint in
this skill. Read it before loosening any of them.
