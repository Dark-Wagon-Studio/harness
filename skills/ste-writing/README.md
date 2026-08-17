# ste-writing

An agent skill that rewrites prose into ASD-STE100 Simplified Technical English
to remove "AI slop". Works with any harness that reads a `SKILL.md` (pi,
Claude Code, and similar). Two modes: strict (procedures, error messages) and
STE-flavored (general prose, no dictionary lockdown).

## Install

Copy the `ste-writing/` folder from this repo into your repo's skills
directory, or run the
[Dark-Wagon-Studio/harness](https://github.com/Dark-Wagon-Studio/harness)
installer, which installs it with the full journals workflow.

Then load `skills/ste-writing/SKILL.md` when you want the style applied.

## Files

| File | What it is |
|---|---|
| `SKILL.md` | The distilled ASD-STE100 agent skill, two modes |
| `ste-lint.py` | The heuristic anti-slop linter — the machine-checkable subset of STE. Deterministic; the score delta between two texts is the signal |

## Run the linter

```
python3 ste-lint.py your-draft.md
```

Score is violations per 100 words — lower is cleaner. Lint a draft, apply the
skill, then lint it again. The delta between the two scores is the signal.

## The headline numbers

| Condition | Claude sonnet | gpt-5.5 |
|---|---|---|
| baseline | 4.36 | 3.54 |
| banned-words list | 4.21 (-3%) | 2.14 (-40%) |
| Orwell's 6 rules | 2.48 (-43%) | 1.69 (-52%) |
| STE skill | 1.12 (-74%) | 1.76 (-50%) |

Give a model a writing system and slop drops by half or more, on every model
tested. STE was best or tied-best. A banned-words list is the least reliable
fix.

## Limits

Not a certified STE checker. The judgment rules of ASD-STE100 need a human;
this covers the mechanical subset — which is where the slop lives.

Spec: ASD-STE100 Issue 9, free at asd-ste100.org
