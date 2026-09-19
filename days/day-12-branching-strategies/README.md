# Day 12 — Branching Strategies

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 2 - Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Git Flow is a seating chart. Trunk-based is a food truck. Pick for ship cadence.

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Model | Refs you keep | Merge / release |
| --- | --- | --- |
| Git Flow | main + develop + feature/* + release/* + hotfix/* | release/* cut; merge to main AND develop |
| GitHub Flow | main + short feature/* | PR to main; deploy main |
| Trunk-based | main; branches hours not days; maybe release/* tags | Small PRs; feature flags if needed |
| This lab | main protected (Day 19) + feature/* < 2 days | Squash PR; no develop branch |
| TFVC / release branches forever | long-lived release/2024.09 | Out of scope — you stay on Git |
| Environment branches (dev/qa/prod) | Three eternally diverging mains | Avoid; promote artifacts not branches |

## Step-by-step lab

1. git switch main && git pull && git switch -c feature/day12-branching-adr
2. Create docs/branching-strategy.md with Decision: GitHub Flow (trunk-based lite).
3. Document: main always deployable; feature/* < 2 days; PR required; squash merge; no develop/release/hotfix long lives.
4. List 3 reasons Git Flow is rejected for this lab (solo, no multi-version prod, want short lead time).
5. git add docs/branching-strategy.md && git commit -m "docs: add branching strategy ADR" && git push -u origin feature/day12-branching-adr
6. Azure Repos → Pull requests → New PR into main. Title: docs: branching ADR. You may complete it or leave for Day 14 template.
7. Repos → Branches. Confirm there is no develop. If you created one by habit, delete it after merging any needed commits.

## Done when

- [ ] Can contrast Git Flow vs GitHub Flow vs trunk-based with branch names
- [ ] docs/branching-strategy.md is on a feature branch (or merged)
- [ ] No develop branch in azure-100-labs
- [ ] ADR says squash + short feature/*

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-12-branching-strategies
```

## Next

**Day 13** — Azure Repos setup
