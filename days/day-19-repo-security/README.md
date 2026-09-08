# Day 19 — Repo Security (Branch Policies)

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | Phase 2 — Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Protect `main` with Azure Repos branch policies and prove the PR-only path works.

## High-level architecture (summary)

Open **[handout.pdf](./handout.pdf)** for complete tables. Short version:

| Control | Answers | Example |
|:--------|:--------|:--------|
| **Repo permissions** | Who can access | Readers / Contributors / Admins |
| **Branch policies** | How `main` changes | PR required, reviewers, work items, squash |

**Lab baseline on `main`:** 1 reviewer · linked work item required · squash-only merges

## Learn

- [Branch policies](https://learn.microsoft.com/azure/devops/repos/git/branch-policies)

## Step-by-step lab

1. Branches → `main` → Branch policies
2. Enable reviewers, linked work items, squash-only
3. Prove direct push to `main` fails
4. Merge via PR on `feature/day19-branch-policies`
5. Document in `docs/branch-policies.md`

## Done when

- [ ] Policies live on `main`
- [ ] PR path verified
- [ ] Bypass treated as break-glass only

## LinkedIn

Post draft: [`../../daily-guides/day-19.md`](../../daily-guides/day-19.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://bit.ly/4zSQtjo
```

(Full path: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-19-repo-security)

## Next

**Day 20** — Phase 2 mini project & recap.
