# Day 15 — Advanced Git

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 2 - Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Rebase rewrites history. Merge keeps the plot twists. Know who is watching the timeline.

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Operation | Graph result | Safe on |
| --- | --- | --- |
| Merge commit | New commit with two parents | Shared branches if policy allows |
| Squash merge (ADO PR) | One new commit on main; feature SHAs dropped | feature/* → main (this lab default) |
| Rebase onto main | Replay your commits; new SHAs | Local feature/* only, then force-with-lease |
| Fast-forward | Pointer move, no extra commit | When feature is linear on main |
| Cherry-pick | Copy a commit SHA onto another branch | Hotfix one commit, not a whole feature |
| Soft reset | Move branch, keep index/worktree | Rewrite last local commit before push |

## Step-by-step lab

1. git switch main && git pull. Create feature/day15-a and feature/day15-b from the same SHA.
2. On day15-a: edit docs/day15-conflict.md line 1 to 'alpha'. Commit. Push.
3. On day15-b: edit the same file line 1 to 'bravo'. Commit.
4. git fetch origin && git rebase origin/main (if main moved) then rebase/merge day15-a into day15-b until conflict appears.
5. Resolve conflict in the editor. git add docs/day15-conflict.md && git rebase --continue (or git commit if you used merge).
6. If you rebased a branch already on origin: git push --force-with-lease. Never push --force to main.
7. Write 5 lines in docs/day15-when.md: when you choose merge commit vs squash vs rebase. Commit on the feature branch.

## Done when

- [ ] Can explain rebase vs merge vs squash with the parent graph
- [ ] Resolved a real conflict (markers gone)
- [ ] Used --force-with-lease on a feature branch, never on main
- [ ] Wrote when-to-choose notes in the repo

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-15-advanced-git
```

## Next

**Day 16** — Git hooks & pre-commit
