# Day 11 — Git Fundamentals

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 2 - Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Working tree, index, commit DAG, remote — four areas, one SHA

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Area | On disk | Command that moves data |
| --- | --- | --- |
| Working tree | Your files (notes/day11.md) | edit; git status shows unstaged |
| Index / staging | .git/index | git add notes/day11.md |
| Local repo | .git/objects commit/tree/blob | git commit -m "docs: ..." |
| Remote | Azure Repos refs/heads/* | git push -u origin feature/day11-notes |
| HEAD | Pointer to branch or detached SHA | git switch / git checkout |
| Ref | .git/refs/heads/main (41-byte SHA + newline) | git branch -v |

## Step-by-step lab

1. git clone (if needed) && git remote -v. Confirm origin is the personal Azure Repos URL, not a work GitHub.
2. git status && git switch -c feature/day11-notes
3. mkdir notes (Windows: mkdir notes) && write notes/day11.md with the four-area map in your words.
4. git add notes/day11.md && git status (should show staged, not a pile of junk).
5. git commit -m "docs: day 11 git fundamentals notes"
6. git log --oneline --decorate --graph -5 && git push -u origin feature/day11-notes
7. Azure Repos → Branches → see feature/day11-notes. Optional: merge locally to main or wait for Day 14 PR.

## Done when

- [ ] Can name working tree, index, local repo, remote
- [ ] feature/day11-notes exists on Azure Repos with one intentional commit
- [ ] git log --oneline shows the SHA
- [ ] origin is the personal azure-100-labs repo

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-11-git-fundamentals
```

## Next

**Day 12** — Branching strategies
