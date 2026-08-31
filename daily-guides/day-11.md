# Day 11 — Git Fundamentals for DevOps Engineers

| | |
|---|---|
| **Date** | 31 Aug 2026 |
| **Phase** | 2 — Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Master the foundational Git architecture (Working Tree → Staging Index → Local Commit → Remote Repository), commit object graphs (DAG), and core CLI hygiene essential for automated CI/CD pipelines. Publish Day 11 on LinkedIn with the PDF handout.

## Learn (20–30 min)

- The 4 Areas of Git: Working Directory, Staging Area (Index), Local Repository (.git), Remote Repository (Azure Repos)
- Git internals simplified: Blobs (content), Trees (directory structure), Commits (metadata + pointer to root tree), Branches (lightweight movable pointers to commit SHAs)
- Essential workflow commands: `status`, `add`, `commit`, `branch`, `checkout`/`switch`, `merge`, `log --oneline --graph`
- Why atomic, clean commits matter for CI/CD, bisecting bugs, and PR reviews
- Docs: [Git documentation](https://git-scm.com/doc) and [Azure Repos Git tutorial](https://learn.microsoft.com/azure/devops/repos/git/what-is-git)

## Hands-on lab (20–30 min)

1. Open your terminal in the cloned `azure-100-labs` repository:
   ```bash
   cd azure-100-labs
   git status
   ```
2. Create and switch to a new feature branch:
   ```bash
   git switch -c feature/day11-git-notes
   ```
3. Create a structured notes folder and file:
   ```bash
   mkdir -p notes
   echo "# Day 11: Git Mental Model & 4 Areas" > notes/day-11-git-model.md
   ```
4. Stage and commit atomically:
   ```bash
   git add notes/day-11-git-model.md
   git commit -m "docs: add Day 11 git mental model notes"
   ```
5. Inspect commit log and branch topology:
   ```bash
   git log --oneline --graph --decorate -n 5
   ```
6. Push feature branch to Azure Repos remote:
   ```bash
   git push -u origin feature/day11-git-notes
   ```

## Commands / code

```bash
# Inspection & Log navigation
git status
git log --oneline --graph --decorate -n 10
git diff
git diff --staged

# Branch management
git switch -c feature/<branch-name>   # modern create & switch
git switch main                      # switch back
git branch -a                        # list local and remote branches

# Pushing with upstream tracking
git push -u origin <branch-name>
```

## LinkedIn post (copy-paste)

**Important:** After pasting into LinkedIn, press Enter between sections so line breaks stay visible.

```
Day 11 of #100DaysOfAzureDevOps

Phase 2 begins today: Azure Repos & Git Mastery.

Most developers treat Git like a magic backup utility:
`git add .` → `git commit -m "fix"` → `git push --force` → pray.

In DevOps and CI/CD, Git is not just version control.
It is the source of truth for your infrastructure, the trigger for your automated pipelines, and the audit trail for production compliance.

If you don't understand Git's 4 areas, you will battle merge conflicts and corrupted pipelines:

1. Working Directory — the actual files you edit on disk.
2. Staging Area (Index) — the preparation zone where you curate atomic changes.
3. Local Repository (.git) — committed snapshots packaged into an immutable directed acyclic graph (DAG).
4. Remote Repository (Azure Repos) — shared collaboration hub that triggers CI builds on push.

A branch in Git is not a heavy copy of your codebase.
It is literally a 41-byte text file containing a SHA-1 pointer to a commit.

When your commits are clean and atomic:
• Automated CI builds test exact, isolated changes.
• Git bisect pinpoints production bugs in seconds.
• Code reviews stay small and meaningful.

Lab today in azure-100-labs:
Branch creation, staging curation, atomic commit logging with graphical trees, and upstream remote tracking on Azure Repos.

One-liner:
Git doesn't store file diffs; it stores snapshots.
Treat your commit history like production code, not an afterthought.

Tomorrow: Branching strategies for CI/CD — Trunk-based vs GitFlow.

(Document attached: Day 11 Git Fundamentals Handout PDF)

Lab notes + PDF also here:
https://bit.ly/45WLoJm

#100DaysOfAzureDevOps #Azure #DevOps #Git #AzureRepos #CloudComputing #LearningInPublic
```

### Attach with the post (PDF handout)

Attach this document on LinkedIn (document / PDF upload):

- [`../days/day-11-git-fundamentals/handout.pdf`](../days/day-11-git-fundamentals/handout.pdf)

### How to post

1. LinkedIn → **document** → upload `days/day-11-git-fundamentals/handout.pdf`
2. Paste the text above (press **Enter** between sections so line breaks stay visible)
3. **Document title:** `Day 11 — Git Fundamentals for DevOps` (max 58 chars on LinkedIn)

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5–10 real comments on other Azure/DevOps posts.

## Done checklist

- [ ] Understood Git's 4 stages (Working Tree, Staging, Local Repo, Remote)
- [ ] Created feature branch `feature/day11-git-notes` in `azure-100-labs`
- [ ] Staged and committed atomic changes
- [ ] Pushed with upstream tracking to Azure Repos
- [ ] Published LinkedIn post with PDF handout
- [ ] Engaged with 5–10 community comments

## Tomorrow

**Day 12 — Branching Strategies (Trunk-Based vs GitFlow & Release Branches)**

---

*Personal learning guide — views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
