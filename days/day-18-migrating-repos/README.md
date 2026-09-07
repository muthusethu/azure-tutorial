# Day 18 — Migrating Repos to Azure Repos

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | Phase 2 — Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Import or mirror-push a Git repository into Azure Repos with history preserved, then verify commits, branches, and tags.

## High-level architecture (summary)

Open **[handout.pdf](./handout.pdf)** for complete tables. Short version:

| Method | How | When to use |
|:-------|:----|:------------|
| **Import UI** | Azure Repos clones from source URL | Simple public/private Git sources |
| **Bare + mirror** | `git clone --bare` → `git push --mirror` | Full control of all refs |

**Survives migration:** commits, branches, tags  
**Does not auto-migrate:** CI secrets, webhooks, PR discussions, host-specific apps

## Learn

- [Import a Git repo](https://learn.microsoft.com/azure/devops/repos/git/import-git-repository)

## Step-by-step lab

1. Create empty Azure Repos repo `imported-sample`
2. Import via UI **or** bare clone + `git push --mirror`
3. Clone and verify `git log` / branches / tags
4. Document checklist in `docs/repo-migration-checklist.md`

## Done when

- [ ] History visible in Azure Repos
- [ ] Default branch set to `main`
- [ ] Migration checklist written

## LinkedIn

Post draft: [`../../daily-guides/day-18.md`](../../daily-guides/day-18.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://bit.ly/3UVLPkD
```

(Full path: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-18-migrating-repos)

## Next

**Day 19** — Repo security (branch policies).
