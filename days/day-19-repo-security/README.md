# Day 19 — Repo Security

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 2 - Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Branch policies are parental controls for adults who still push to main at 11:58pm

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Policy | Azure Repos setting | Lab value |
| --- | --- | --- |
| Minimum reviewers | Require a minimum number of reviewers | 1 (yourself OK) |
| Linked work items | Check for linked work items | Required |
| Merge types | Limit merge types | Allow squash only |
| Comment resolution | Check for comment resolution | Optional today; on in real teams |
| Build validation | Build pipeline must succeed | Add after Day 21 YAML exists |
| Status checks | External GitHub/ADO statuses | Skip unless you add one |

## Step-by-step lab

1. Repos → Branches → … on main → Branch policies.
2. Require a minimum number of reviewers: 1. Allow requestors to approve their own changes (solo lab).
3. Check for linked work items: Required.
4. Limit merge types: uncheck Merge / Rebase / Semi-linear; leave Squash merge checked.
5. Save. Locally: git switch main && echo bypass > notes/should-fail.txt && git add && git commit -m "docs: should be blocked" && git push origin main
6. Expect rejected by policy. Delete the local commit: git reset --hard origin/main (only if push failed and commit is local).
7. Open a PR from a feature branch with a linked work item and squash-complete it to prove the happy path.

## Done when

- [ ] main requires 1 reviewer and a linked work item
- [ ] Merge types limited to squash
- [ ] Direct git push origin main failed
- [ ] A compliant PR still merges

## LinkedIn

Post draft: [`../../daily-guides/day-19.md`](../../daily-guides/day-19.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-19-repo-security
```

## Next

**Day 20** — Phase 2 mini project
