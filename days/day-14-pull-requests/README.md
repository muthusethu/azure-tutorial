# Day 14 — Pull Requests & Code Review

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 2 - Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

A PR without a description is a mystery novel whose murderer is 'I was in a hurry'

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Piece | Field / location | Lab value |
| --- | --- | --- |
| Source → target | feature/* → main | Never PR into a random long-lived branch |
| Title | Conventional: docs: / feat: / fix: | Matches commit intent |
| Description | .azuredevops/pull_request_template.md | What / Why / Test plan / Risk |
| Work item link | AB#123 in description or Development link | Day 7 User Story |
| Reviewers | Required reviewers (Day 19 policy) | Yourself is OK on a personal org |
| Checks | Build validation later (YAML) | None yet — still review the diff |

## Step-by-step lab

1. git switch main && git pull && git switch -c feature/day14-pr-template
2. Create .azuredevops/pull_request_template.md with What / Why / Test plan / Risk (see code).
3. git add .azuredevops/pull_request_template.md && git commit -m "docs: add pull request template" && git push -u origin feature/day14-pr-template
4. Azure Repos → Pull requests → New pull request → source feature/day14-pr-template → target main.
5. Confirm the template auto-fills. Complete What/Why. Link a Day 7 User Story (Development / work items).
6. Files tab → self-review: title, description, no secrets. Add one comment on the markdown if you want the muscle memory.
7. Complete with squash merge (if allowed) or leave open until Day 19 policies. Delete source branch on complete.

## Done when

- [ ] PR template exists under .azuredevops/
- [ ] Opened a PR into main with What/Why filled
- [ ] Work item linked (AB# or Development link)
- [ ] Self-reviewed the Files tab; no secrets

## LinkedIn

Post draft: [`../../daily-guides/day-14.md`](../../daily-guides/day-14.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-14-pull-requests
```

## Next

**Day 15** — Advanced Git
