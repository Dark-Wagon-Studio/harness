# Opportunity Score Sheet

Score desired outcomes from survey data. One row per outcome statement.

## The rule

Ratings come from surveys only. Respondents must actually do the job, and
each rates importance and satisfaction from 1 to 10. Never convert
qualitative text into numbers. A row without ratings stays blocked.

## Formula

    Opportunity = Importance + max(Importance − Satisfaction, 0)

- Importance 9, Satisfaction 3 → 9 + 6 = 15. Underserved, high-value.
- Importance 9, Satisfaction 8 → 9 + 1 = 10. Well served.
- Importance 3, Satisfaction 9 → 3 + 0 = 3. Overserved at best.

## Sheet

| # | Desired outcome statement | Importance (1–10) | Satisfaction (1–10) | Opportunity |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

## Statement quality gate

Before a row earns scores, its statement must pass:

- Syntax: minimize/increase + performance metric + object + contextual
  clarifier.
- Solution-free: no products, technologies, or features.
- Measurable: time, likelihood, or number.
- Bound to one job-map step.

## Survey source

- Who was surveyed (job executors only):
- Sample size (N):
- Dates:
- Instrument:

- Treat results from a small sample as tentative, not settled.
- Treat any score from an unlisted or invented source as a violation, not a
  data point.
