# Day 16 — Git Hooks & Pre-commit Checks

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | Phase 2 — Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Add a `commit-msg` hook for Conventional Commits, understand `--no-verify` bypass risk, and separate local courtesy from server-side branch policy locks.

## High-level architecture (summary)

Open **[handout.pdf](./handout.pdf)** for complete tables. Short version:

| Layer | Where it runs | Bypassable? | Role |
|:------|:--------------|:------------|:-----|
| **Local hooks** | `.git/hooks/` | Yes (`--no-verify`) | Fast developer feedback |
| **pre-commit framework** | Shared config in repo | Yes (if not installed) | Team consistency |
| **Branch policies / PR builds** | Azure Repos server | No (if enforced) | Real quality lock |

## Learn

- [Git Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)
- [pre-commit framework](https://pre-commit.com/)

## Step-by-step lab

1. `git switch -c feature/day16-commit-hook`
2. Add `scripts/git-hooks/commit-msg` (Conventional Commits check)
3. Document install steps in `docs/git-hooks.md`
4. Install locally; prove bad message fails, good message passes
5. Commit, push, open PR

## Done when

- [ ] Hook script + docs committed
- [ ] Bad commit message rejected locally
- [ ] You can explain why server gates still matter

## LinkedIn

Post draft: [`../../daily-guides/day-16.md`](../../daily-guides/day-16.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://bit.ly/4gCudTt
```

(Full path: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-16-git-hooks)

## Next

**Day 17** — Fork workflows & permissions.
