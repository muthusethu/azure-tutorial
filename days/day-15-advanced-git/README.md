# Day 15 — Advanced Git (Rebase, Squash & History Hygiene)

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | Phase 2 — Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Practice rebase vs merge, squash merges, conflict resolution, and safe force-push hygiene for CI/CD.

## High-level architecture (summary)

Open **[handout.pdf](./handout.pdf)** for complete tables. Short version:

| Operation | Effect on history | When to use |
|:----------|:------------------|:------------|
| **Merge** | Keeps topology + merge commit | Preserve exact integration story |
| **Rebase** | Rewrites SHAs; linearizes | Clean feature branch onto latest main |
| **Squash** | Many commits → one | Ship one coherent change to main |
| **Cherry-pick** | Copy one commit | Hotfix onto another line |

**Safety rule:** rebase features, never shared `main`. Push with `--force-with-lease`.

## Learn

- [Git rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)
- [Squash merge in Azure Repos](https://learn.microsoft.com/azure/devops/repos/git/merging-with-squash)

## Step-by-step lab

1. `git switch -c feature/day15-rebase-lab`
2. Make 2–3 commits; rebase onto `origin/main`
3. Resolve conflicts if any → `git rebase --continue`
4. `git push --force-with-lease`
5. Document merge vs squash vs rebase in `docs/merge-strategy.md`

## Done when

- [ ] Feature rebased onto latest main
- [ ] Used `--force-with-lease`
- [ ] Merge strategy notes committed

## LinkedIn

Post draft: [`../../daily-guides/day-15.md`](../../daily-guides/day-15.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://bit.ly/4ykI3zU
```

(Full path: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-15-advanced-git)

## Next

**Day 16** — Git hooks & pre-commit.
