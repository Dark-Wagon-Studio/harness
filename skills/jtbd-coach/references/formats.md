# Formats: Job Statements and Job Stories

Two statement formats do different work. The core functional job (ODI) is
for market and investment analysis. The job story (Klement/Intercom) is for
feature design and discovery.

## Core functional job statement (ODI)

> **Verb + Object + [optional contextual clarifier]**

- "Align team members on project goals" (not "use Slack to align the team").
- "Listen to music while on the go" (clarifier distinguishes a different job
  from "listen to music in a recording studio").

Two hard rules, scoped to this format:

1. **Solution-free.** No products, brands, technologies, channels, or
   features. If the solution vanished tomorrow, the job must survive it.
2. **Outcome-free.** No quality adjectives or performance metrics ("fast",
   "reliable", "cheap", "easily"). Performance belongs in desired outcomes.

| Invalid | Valid | Why |
|---|---|---|
| "Use an AI dashboard to track sales" | "Monitor sales performance" | Solution named |
| "Send Slack messages to keep the team updated" | "Inform team members of project updates" | Brand + channel |
| "Quickly organize project information" | "Organize project information" | Outcome leaked into job |

## Job story (Klement / Intercom)

> **When** [situation], **I want to** [motivation], **so I can** [expected
> outcome].

Unlike the ODI job statement, the job story *carries* situation and
motivation, including emotional and social content.

Example: "When I am on my way to an early-morning meeting, I want to quickly
get a hot coffee without waiting in line, so I can arrive on time and feel
composed."

Valid/invalid pairs:

| Invalid | Valid | Why |
|---|---|---|
| "As a commuter, I want a coffee app, so that I can order coffee." | "When I am running early to a meeting, I want to skip the coffee line, so I can arrive on time and composed." | User story in disguise. No situation, no motivation |
| "When I open the app, I want to see a dashboard, so I can see data." | "When I start my review day, I want to see which accounts changed since yesterday, so I can triage before standup." | Names UI, not progress |
| "When I am bored, I want entertainment, so I can be happy." | "When I have 10 minutes between tasks, I want a puzzle that ends on its own, so I can return to work without losing my place." | Too vague to design against |

## Job story vs user story

- User story: "As a [persona], I want [feature], so that [benefit]." Focus:
  **who**.
- Job story: "When [situation], I want to [motivation], so I can
  [outcome]." Focus: **why and under what circumstance**.

Same person, different circumstances, different jobs. The situation, not
the persona, selects the behavior.

## The three dimensions

Every job operates on three dimensions at once. Check all three:

| Dimension | Question | Car example |
|---|---|---|
| Functional | What practical task? | Get to work reliably |
| Emotional | How do they want to feel? | Safe, confident, in control |
| Social | How do they want to be seen? | Successful, responsible |

A product serving only the functional dimension gets commoditized. The
dominant products serve all three simultaneously.

Use [the template](../assets/job-story-template.md) when the user wants
fill-in stories rather than coaching prose.
