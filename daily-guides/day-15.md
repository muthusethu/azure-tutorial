# Day 15 — Advanced Git (Rebase, Squash & History Hygiene)

| | |
|---|---|
| **Date** | 4 Sep 2026 |
| **Phase** | 2 — Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Master rebase vs merge, squash merges, cherry-pick, conflict resolution, and safe history hygiene for CI/CD. Publish Day 15 on LinkedIn with the PDF handout.

## Learn (20–30 min)

- **Merge:** preserves full branch topology; creates a merge commit
- **Rebase:** replays your commits on top of another tip; linear history; rewrites SHAs
- **Squash:** collapses many WIP commits into one clean commit (PR squash merge)
- **Cherry-pick:** apply a single commit onto another branch (hotfixes)
- Golden rule: never rebase a shared/published branch others already pulled — rebase your feature onto `main`, then `--force-with-lease`
- Docs: [Git branching and merging](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) · [Azure Repos merge strategies](https://learn.microsoft.com/azure/devops/repos/git/merging-with-squash)

## Hands-on lab (20–30 min)

1. Update local main and create a feature branch:
   ```bash
   git switch main
   git pull
   git switch -c feature/day15-rebase-lab
   ```
2. Make 2–3 small commits on the feature branch (notes file is fine)
3. Meanwhile (or simulate): update `main` with another change so histories diverge
4. Rebase your feature onto latest main:
   ```bash
   git fetch origin
   git rebase origin/main
   # if conflicts: fix → git add <files> → git rebase --continue
   ```
5. Push safely:
   ```bash
   git push --force-with-lease -u origin feature/day15-rebase-lab
   ```
6. Open a PR and choose **Squash merge** (or document why merge commit is preferred)
7. Write 5 lines in `docs/merge-strategy.md`: when merge vs squash vs rebase

## Commands / code

```bash
# Rebase feature onto main (safe pattern)
git fetch origin
git switch feature/day15-rebase-lab
git rebase origin/main
git push --force-with-lease

# Abort if things go wrong
git rebase --abort

# Soft squash locally (alternative to PR squash)
git reset --soft origin/main
git commit -m "docs: day 15 advanced git notes"

# Cherry-pick a hotfix commit onto main
git cherry-pick <commit-sha>
```

## LinkedIn post (copy-paste)

**Important:** After pasting into LinkedIn, press Enter between sections so line breaks stay visible.

```
Day 15 of #100DaysOfAzureDevOps

Yesterday: Pull Requests — the human gate before merge.
Today: Advanced Git — rebase, squash, and history hygiene.

Most teams argue about Git commands.
Production teams argue about history contracts.

Three tools. Three jobs. Do not mix them up.

1. Merge
• Preserves the full branch story
• Creates a merge commit
• Best when you need the exact integration history

2. Rebase
• Replays your commits on top of latest main
• Linear history, new SHAs
• Best for cleaning your feature branch before PR
• Never rebase a shared branch others already pulled

3. Squash
• Collapses 12 WIP commits into one reviewable change
• Best for "feature arrives as one coherent unit on main"
• Azure Repos PR squash merge does this cleanly

The rule that prevents weekend archaeology:

• Rebase your feature onto main
• Squash (or keep atomic commits) before merge
• Push with --force-with-lease — never blind --force
• Never rewrite main's published history

Conflicts are not failure.
They are proof two people touched the same truth.
Resolve them once, with tests, before the pipeline does it for you at 2 AM.

Lab today in azure-100-labs:
Rebased feature/day15-rebase-lab onto origin/main, resolved conflicts, pushed with --force-with-lease, and documented merge vs squash vs rebase in an ADR.

One-liner:
Rebase rewrites history. Merge preserves the plot.
Choose based on whether teammates already depend on that timeline.

Tomorrow: Git hooks & pre-commit — local gates before the server gates.

(Document attached: Day 15 Advanced Git handout PDF)

Lab notes + PDF also here:
https://bit.ly/4ykI3zU

#100DaysOfAzureDevOps #Azure #DevOps #Git #AzureRepos #CICD #CloudComputing #LearningInPublic
```

### Attach with the post (PDF handout)

Attach this document on LinkedIn (document / PDF upload):

- [`../days/day-15-advanced-git/handout.pdf`](../days/day-15-advanced-git/handout.pdf)

### How to post

1. LinkedIn → **document** → upload `days/day-15-advanced-git/handout.pdf`
2. Paste the text above (press **Enter** between sections so line breaks stay visible)
3. **Document title:** `Day 15 — Advanced Git: Rebase & Squash` (max 58 chars on LinkedIn)

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5–10 real comments on other Azure/DevOps posts.

## Done checklist

- [ ] Explained merge vs rebase vs squash in one sentence each
- [ ] Rebased a feature branch onto `origin/main`
- [ ] Used `--force-with-lease` (not blind `--force`)
- [ ] Documented merge strategy choice in `docs/merge-strategy.md`
- [ ] Published LinkedIn post with PDF handout
- [ ] Engaged with 5–10 community comments

## Tomorrow

**Day 16 — Git Hooks & Pre-commit**

---

*Personal learning guide — views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
