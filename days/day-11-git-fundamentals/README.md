# Day 11 — Git Fundamentals for DevOps Engineers

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | Phase 2 — Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Understand the 4 core areas of Git (Working Tree → Staging Index → Local Repo → Remote Repo), Git's immutable DAG object model (Blobs, Trees, Commits), and atomic commit hygiene for CI/CD pipelines.

## High-level architecture (summary)

Open **[handout.pdf](./handout.pdf)** for complete tables. Short version:

| Area | Location | Purpose |
|:-----|:---------|:--------|
| **Working Directory** | Local filesystem | Unstaged live files and ongoing modifications |
| **Staging Area (Index)** | `.git/index` | Selected changes queued for the next atomic commit snapshot |
| **Local Repository** | `.git/objects` | Committed immutable commit DAG snapshots |
| **Remote Repository** | Azure Repos | Shared upstream collaboration hub triggering CI pipelines |

**Git Object Model:**
- **Blob:** File contents hashed with SHA-1.
- **Tree:** Directory listing linking blobs and nested trees.
- **Commit:** Pointer to root tree + author + timestamp + parent commit SHA.
- **Branch:** Lightweight 41-byte pointer (`.git/refs/heads/<name>`) to the tip commit.

## Learn

- [Git Documentation & Pro Git Book](https://git-scm.com/doc)
- [Azure Repos Git Tutorial](https://learn.microsoft.com/azure/devops/repos/git/what-is-git)

## Step-by-step lab

1. Open terminal inside `azure-100-labs` local clone.
2. Create and switch to feature branch: `git switch -c feature/day11-git-notes`
3. Add notes in `notes/day-11-git-model.md`.
4. Stage atomically: `git add notes/day-11-git-model.md`
5. Commit: `git commit -m "docs: add Day 11 git mental model notes"`
6. Push with tracking: `git push -u origin feature/day11-git-notes`
7. Inspect branch topology: `git log --oneline --graph --decorate -n 5`

## Done when

- [ ] You can explain Git's 4 areas and object types (blob, tree, commit, ref)
- [ ] Feature branch created, committed, and pushed to Azure Repos
- [ ] Upstream tracking verified

## LinkedIn

Post draft: [`../../daily-guides/day-11.md`](../../daily-guides/day-11.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://bit.ly/45WLoJm
```

(Full path: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-11-git-fundamentals)

## Next

**Day 12** — Branching Strategies (Trunk-Based vs GitFlow & Release Branching).
