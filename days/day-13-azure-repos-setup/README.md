# Day 13 — Azure Repos Setup & Repository Hygiene

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | Phase 2 — Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Configure `azure-100-labs` with standard folder layout, `.gitignore`, remote hygiene, and basic permission awareness — ready for PRs and pipelines in upcoming days.

## High-level architecture (summary)

Open **[handout.pdf](./handout.pdf)** for complete tables. Short version:

| Area | Purpose | Lab Action |
|:-----|:--------|:-----------|
| **Default branch** | Single deployable line (`main`) | Verify in Project settings |
| **Folder layout** | Predictable structure for code, docs, CI, IaC | `/src`, `/docs`, `/pipelines`, `/infra` |
| **`.gitignore`** | Block secrets, artifacts, IDE noise | Add on day one |
| **Remotes** | HTTPS/SSH clone and push targets | `git remote -v`, feature branch push |
| **Permissions** | Readers / Contributors / Admins | Least privilege; policies on Day 19 |

## Learn

- [Create a new Git repo in Azure Repos](https://learn.microsoft.com/azure/devops/repos/git/create-new-repo)
- [Ignore files in Azure Repos](https://learn.microsoft.com/azure/devops/repos/git/ignore-files)

## Step-by-step lab

1. Verify default branch = `main` in Azure Repos settings
2. `git switch -c feature/day13-repo-setup`
3. Create folders: `src/`, `docs/`, `pipelines/`, `infra/`
4. Add `.gitignore` and `docs/repo-structure.md`
5. Commit and push to Azure Repos
6. Review repo permissions (Contributors vs Readers)

## Done when

- [ ] Standard folder layout exists in `azure-100-labs`
- [ ] `.gitignore` committed (no secrets or build artifacts tracked)
- [ ] Feature branch pushed; remote verified

## LinkedIn

Post draft: [`../../daily-guides/day-13.md`](../../daily-guides/day-13.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://bit.ly/4xyn8cz
```

(Full path: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-13-azure-repos-setup)

## Next

**Day 14** — Pull requests & code review.
