# Day 19 — Repo Security (Branch Policies)

| | |
|---|---|
| **Date** | 8 Sep 2026 |
| **Phase** | 2 — Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Protect `main` in Azure Repos with branch policies: required reviewers, linked work items, limited merge types, and (optionally) build validation. Prove that direct pushes to `main` are blocked. Publish Day 19 on LinkedIn with the PDF handout.

## Learn (20–30 min)

- Branch policies vs repo permissions: permissions say *who*; policies say *how* changes land on `main`
- Core policies: minimum reviewers, linked work items, comment resolution, build validation, status checks
- Merge type limits: squash / rebase / merge commit — pick one strategy for clean history
- Bypass policies: treat as break-glass, not a daily shortcut
- Docs: [Branch policies and settings](https://learn.microsoft.com/azure/devops/repos/git/branch-policies)

## Hands-on lab (20–30 min)

1. Azure Repos → **Branches** → `main` → **Branch policies**
2. Enable at minimum:
   - Require a minimum number of reviewers: **1** (yourself OK for solo lab)
   - Check for linked work items: **Required**
   - Limit merge types: **Squash merge** only (matches your Day 12 ADR)
3. Optional (if you have a YAML pipeline later): Require a build to pass before merging
4. Prove the lock:
   ```bash
   git switch main
   git pull
   # Attempt a direct commit/push to main — should be rejected by policy
   echo "policy test" >> POLICY_TEST.md
   git add POLICY_TEST.md
   git commit -m "docs: should fail without PR"
   git push origin main
   ```
5. Clean path: create `feature/day19-branch-policies`, push, open PR with linked work item, complete via squash
6. Document settings in `docs/branch-policies.md`

## Commands / code

```text
Azure DevOps UI path:
Repos → Branches → main → ··· → Branch policies

Minimum lab baseline:
- Require reviewers: 1
- Linked work items: Required
- Limit merge types: Squash
- (Later) Build validation: required CI pipeline
```

## LinkedIn post (copy-paste)

**Important:** After pasting into LinkedIn, press Enter between sections so line breaks stay visible.

```
Day 19 of #100DaysOfAzureDevOps

Yesterday: migrating repos — history moved, hygiene decided the rest.
Today: Repo security — branch policies that protect `main` after the move.

Permissions answer: who can access the repo.
Branch policies answer: what must be true before `main` changes.

Without policies, `main` is a suggestion.
With policies, `main` is a contract.

Minimum policies I treat as non-negotiable on `main`:

1. Require a pull request
No direct push. No “quick fix” on Friday night.

2. Minimum reviewers
Even one reviewer beats rubber-stamp solitude on a team repo.
(Solo lab: set 1 and still practice the PR path.)

3. Linked work items
Boards ↔ Repos. If it is not tracked, it is tribal knowledge.

4. Limit merge types
Pick squash (or your ADR) and enforce it — stop mixed history styles.

5. Build validation (when CI exists)
Red builds do not merge. Green is necessary, not sufficient — but it is a floor.

The dangerous escape hatch:
“Bypass policies” for a few admins.
Useful in true emergencies.
Poisonous as a habit.

Lab today in azure-100-labs:
Enabled branch policies on main (reviewers, linked work items, squash-only), proved direct push fails, and merged a PR the correct way.

One-liner:
Branch policies are not bureaucracy.
They are how you stop 2 AM from becoming archaeology.

Tomorrow: Phase 2 mini project & recap — Git mastery checkpoint.

(Document attached: Day 19 Repo Security handout PDF)

Lab notes + PDF also here:
https://bit.ly/4zSQtjo

#100DaysOfAzureDevOps #Azure #DevOps #Git #AzureRepos #Security #CloudComputing #LearningInPublic
```

### Attach with the post (PDF handout)

Attach this document on LinkedIn (document / PDF upload):

- [`../days/day-19-repo-security/handout.pdf`](../days/day-19-repo-security/handout.pdf)

### How to post

1. LinkedIn → **document** → upload `days/day-19-repo-security/handout.pdf`
2. Paste the text above (press **Enter** between sections so line breaks stay visible)
3. **Document title:** `Day 19 — Repo Security & Branch Policies` (max 58 chars on LinkedIn)

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5–10 real comments on other Azure/DevOps posts.

## Done checklist

- [ ] Branch policies enabled on `main`
- [ ] Direct push to `main` blocked (or documented why not in solo admin case)
- [ ] PR path with linked work item + squash merge verified
- [ ] `docs/branch-policies.md` written
- [ ] Published LinkedIn post with PDF handout
- [ ] Engaged with 5–10 community comments

## Tomorrow

**Day 20 — Phase 2 Mini Project & Recap**

---

*Personal learning guide — views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
