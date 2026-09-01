# Day 12 — Branching Strategies for CI/CD

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | Phase 2 — Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Compare GitFlow, GitHub Flow, and Trunk-Based Development; document your branching decision as an ADR in `azure-100-labs`.

## High-level architecture (summary)

Open **[handout.pdf](./handout.pdf)** for complete tables. Short version:

| Model | Branch Structure | Best For | Main Risk |
|:------|:-----------------|:---------|:----------|
| **GitFlow** | main + develop + feature/release/hotfix | Scheduled releases, multi-version prod | Late integration, merge debt |
| **GitHub Flow** | main + short feature/* | Continuous delivery, one prod line | main must stay green |
| **Trunk-Based** | main (+ branches < 1 day) | High velocity, mature CI | Requires flags + discipline |

**Lab choice for azure-100-labs:** GitHub Flow — protected `main`, `feature/*` < 2 days, PR + squash merge.

## Learn

- [Trunk-Based Development](https://trunkbaseddevelopment.com/)
- [Azure Repos branching guidance](https://learn.microsoft.com/azure/devops/repos/git/git-branching-guidance)

## Step-by-step lab

1. `git switch -c feature/day12-branching-adr`
2. Create `docs/branching-strategy.md` ADR
3. Document: protected main, short feature branches, PR required, no develop branch
4. Commit, push, and open PR in Azure Repos

## Done when

- [ ] You can explain when to use GitFlow vs GitHub Flow vs Trunk-Based
- [ ] ADR exists in `docs/branching-strategy.md`
- [ ] Feature branch pushed to Azure Repos

## LinkedIn

Post draft: [`../../daily-guides/day-12.md`](../../daily-guides/day-12.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://bit.ly/46xX1GJ
```

(Full path: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-12-branching-strategies)

## Next

**Day 13** — Azure Repos setup (remotes, permissions, repo hygiene).
