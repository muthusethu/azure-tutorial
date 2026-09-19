# Day 20 — Mini Project + Recap (Phase 2)

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 2 - Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Branch, PR, policy, squash — Git with receipts, not 'save file'

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Capability | Days | Proof |
| --- | --- | --- |
| Four Git areas + objects | 11 | notes/day11.md + git log |
| Branching ADR | 12 | docs/branching-strategy.md = GitHub Flow |
| Layout + gitignore | 13 | /src /docs /pipelines /infra |
| PR template + AB# | 14 | .azuredevops/pull_request_template.md |
| Rebase/conflict literacy | 15 | Resolved conflict; no force on main |
| Client hooks vs policies | 16–19 | commit-msg + main policies |

## Step-by-step lab

1. Confirm Branch policies on main (reviewer, work item, squash). If missing, restore Day 19.
2. git switch main && git pull && git switch -c feature/day20-recap
3. Append README section How we use Git here with a link to docs/branching-strategy.md
4. git add README.md && git commit -m "docs: document git workflow" && git push -u origin feature/day20-recap
5. Open PR → fill template → link a User Story → squash complete → tick delete source branch.
6. Try a non-compliant PR (no work item) or push to main; confirm it is blocked. Close/abandon the bad PR.
7. Repos → Branches: stale feature/* deleted. Update Boards story to Done.

## Done when

- [ ] Can describe the required path to main without saying 'just push'
- [ ] README documents the Git workflow + ADR
- [ ] A non-compliant PR or direct push was blocked once
- [ ] Happy-path squash merge completed; source branch deleted

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-20-phase-2-recap
```

## Next

**Day 21** — Intro to Azure Pipelines
