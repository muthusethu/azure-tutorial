# Day 12 — Branching Strategies for CI/CD

| | |
|---|---|
| **Date** | 1 Sep 2026 |
| **Phase** | 2 — Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Compare GitFlow, GitHub Flow, and Trunk-Based Development; choose a branching model that matches team size and release cadence; document the decision as an Architecture Decision Record (ADR) in `azure-100-labs`. Publish Day 12 on LinkedIn with the PDF handout.

## Learn (20–30 min)

- **GitFlow:** `main` + `develop` + `feature/*`, `release/*`, `hotfix/*` — suited to scheduled releases and multiple versions in production
- **GitHub Flow:** single long-lived `main`, short-lived `feature/*` branches, PR + merge — suited to continuous delivery with one production line
- **Trunk-Based Development:** everyone commits to `main` (or very short branches < 1 day), feature flags hide incomplete work — suited to high-velocity teams with strong CI
- Trade-offs: merge complexity, release predictability, pipeline design, and team coordination overhead
- Docs: [Trunk-Based Development](https://trunkbaseddevelopment.com/) · [Azure Repos branching guidance](https://learn.microsoft.com/azure/devops/repos/git/git-branching-guidance)

## Hands-on lab (20–30 min)

1. In your local `azure-100-labs` clone, create a feature branch:
   ```bash
   git switch main
   git pull
   git switch -c feature/day12-branching-adr
   ```
2. Create an ADR documenting your lab branching strategy:
   ```bash
   mkdir -p docs
   ```
3. Add `docs/branching-strategy.md` with your chosen model (recommended for this lab: **GitHub Flow / trunk-based lite**):
   - `main` is always deployable
   - `feature/*` branches live < 2 days
   - PR required before merge; squash merge preferred
   - No long-lived `develop` or `release/*` branches in this project
4. Commit and push:
   ```bash
   git add docs/branching-strategy.md
   git commit -m "docs: add branching strategy ADR for azure-100-labs"
   git push -u origin feature/day12-branching-adr
   ```
5. Open a Pull Request in Azure Repos (merge tomorrow when we cover PR workflows, or merge locally today if you prefer).

## Commands / code

```bash
# Example ADR skeleton — docs/branching-strategy.md

# Branching Strategy — azure-100-labs
# Status: Accepted
# Decision: GitHub Flow (trunk-based lite)

## Context
Personal learning repo for #100DaysOfAzureDevOps. Solo contributor, frequent small commits, CI planned in Phase 3.

## Decision
- main: protected default branch, always deployable
- feature/*: short-lived (< 2 days), one topic per branch
- PR required; squash merge to keep history clean
- No develop, release/, or hotfix/ branches for this lab

## Consequences
+ Simple mental model, fast feedback, easy bisect
- Not suited for multi-version production support without adaptation
```

## LinkedIn post (copy-paste)

**Important:** After pasting into LinkedIn, press Enter between sections so line breaks stay visible.

```
Day 12 of #100DaysOfAzureDevOps

Yesterday: Git fundamentals — commits, branches, and the 4 areas.
Today: which branching strategy actually fits your delivery model?

There is no universal "best" branching model.
There is only the model that matches your release cadence, team size, and CI maturity.

Three models teams debate constantly:

1. GitFlow
• Branches: main + develop + feature/* + release/* + hotfix/*
• Best for: scheduled releases, multiple versions in production, compliance-heavy environments
• Cost: merge complexity, long-lived branches, integration pain late in the cycle

2. GitHub Flow
• Branches: main + short-lived feature/*
• Best for: continuous delivery, one production line, small-to-mid teams
• Cost: main must stay green; requires strong CI and small PRs

3. Trunk-Based Development
• Branches: main (or branches < 1 day), feature flags for incomplete work
• Best for: high-velocity teams, mature automated testing, frequent deploys
• Cost: demands discipline — no "I'll merge it next sprint"

The mistake I see in production:
Teams copy GitFlow from a blog post written for a 200-person org,
then wonder why their 5-person team spends Friday resolving merge conflicts.

Rule of thumb:
• Fewer long-lived branches = fewer surprise integrations
• If main is not deployable, fix CI before adding more branch types
• Document the decision — future you (and new teammates) will thank you

Lab today in azure-100-labs:
Wrote a branching strategy ADR — GitHub Flow for this lab: protected main, short feature branches, PR + squash merge, no develop branch.

One-liner:
Branching strategy is a delivery decision, not a Git trivia question.
Pick complexity that matches how often you actually ship.

Tomorrow: Azure Repos setup — remotes, permissions, and repo hygiene.

(Document attached: Day 12 Branching Strategies handout PDF)

Lab notes + PDF also here:
https://bit.ly/46xX1GJ

#100DaysOfAzureDevOps #Azure #DevOps #Git #AzureRepos #CICD #CloudComputing #LearningInPublic
```

### Attach with the post (PDF handout)

Attach this document on LinkedIn (document / PDF upload):

- [`../days/day-12-branching-strategies/handout.pdf`](../days/day-12-branching-strategies/handout.pdf)

### How to post

1. LinkedIn → **document** → upload `days/day-12-branching-strategies/handout.pdf`
2. Paste the text above (press **Enter** between sections so line breaks stay visible)
3. **Document title:** `Day 12 — Branching Strategies for CI/CD` (max 58 chars on LinkedIn)

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5–10 real comments on other Azure/DevOps posts.

## Done checklist

- [ ] Compared GitFlow, GitHub Flow, and Trunk-Based Development
- [ ] Created `docs/branching-strategy.md` ADR in `azure-100-labs`
- [ ] Pushed feature branch `feature/day12-branching-adr`
- [ ] Published LinkedIn post with PDF handout
- [ ] Engaged with 5–10 community comments

## Tomorrow

**Day 13 — Azure Repos Setup (remotes, permissions, repo hygiene)**

---

*Personal learning guide — views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
