# Day 14 — Pull Requests & Code Review

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | Phase 2 — Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Practice Azure Repos pull requests: PR templates, linked work items, self-review checklist, and review etiquette.

## High-level architecture (summary)

Open **[handout.pdf](./handout.pdf)** for complete tables. Short version:

| PR Element | Purpose |
|:-----------|:--------|
| **Title** | One-line summary of the change |
| **Description** | What / Why / How verified |
| **Template** | Forces structure (`.azuredevops/pull_request_template.md`) |
| **Work item link** | Boards ↔ Repos traceability |
| **Self-review** | Author checks Files tab before assigning reviewers |
| **Review comments** | Risk & clarity — not personality |

## Learn

- [Pull requests in Azure Repos](https://learn.microsoft.com/azure/devops/repos/git/pull-requests)

## Step-by-step lab

1. `git switch -c feature/day14-pr-template`
2. Create `.azuredevops/pull_request_template.md`
3. Commit and push
4. Open PR → `main`, fill template, link work item
5. Self-review Files tab before inviting reviewers

## Done when

- [ ] PR template exists in the repo
- [ ] PR opened with description + linked work item
- [ ] Self-review completed

## LinkedIn

Post draft: [`../../daily-guides/day-14.md`](../../daily-guides/day-14.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://bit.ly/3TcZSlk
```

(Full path: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-14-pull-requests)

## Next

**Day 15** — Advanced Git (rebase, squash, history hygiene).
