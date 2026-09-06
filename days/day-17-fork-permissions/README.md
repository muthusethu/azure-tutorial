# Day 17 — Fork Workflows & Repo Permissions

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | Phase 2 — Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Compare fork vs shared-repo workflows and document least-privilege Azure Repos permissions for `azure-100-labs`.

## High-level architecture (summary)

Open **[handout.pdf](./handout.pdf)** for complete tables. Short version:

| Model | How it works | Best for |
|:------|:-------------|:---------|
| **Shared repo** | Feature branches + PRs in one repo | Internal teams |
| **Fork** | Work in fork → PR to upstream | OSS / external contributors |

| Role | Typical power | Risk if over-granted |
|:-----|:--------------|:---------------------|
| **Readers** | View | Low |
| **Contributors** | Push / PR | Force push, bypass policies |
| **Project Admins** | Settings + security | Accidental wide-open access |

## Learn

- [Set Git repository permissions](https://learn.microsoft.com/azure/devops/repos/git/set-git-repository-permissions)
- [Forks in Azure Repos](https://learn.microsoft.com/azure/devops/repos/git/forks)

## Step-by-step lab

1. Project settings → Repositories → Security
2. Confirm Contributors can contribute; force push denied for main
3. `git switch -c feature/day17-repo-permissions`
4. Add `docs/repo-permissions.md` ADR
5. Commit, push, open PR

## Done when

- [ ] Fork vs shared-repo difference is clear
- [ ] Permissions ADR committed
- [ ] Force-push risk understood for Contributors

## LinkedIn

Post draft: [`../../daily-guides/day-17.md`](../../daily-guides/day-17.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://bit.ly/3UE039L
```

(Full path: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-17-fork-permissions)

## Next

**Day 18** — Migrating repos to Azure Repos.
