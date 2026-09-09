# Day 20 — Phase 2 Mini Project & Recap

| | |
|---|---|
| **Date** | 9 Sep 2026 |
| **Phase** | 2 — Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Close Phase 2 with one end-to-end Git proof on `azure-100-labs`: feature branch → PR (policies + linked work item) → squash merge → delete branch. Document “How we use Git here” in the README. Publish Day 20 on LinkedIn with the PDF handout.

## Learn (20–30 min)

- Phase 2 map (Days 11–19): fundamentals → branching → Azure Repos → PRs → advanced Git → hooks → forks/permissions → migration → branch policies
- Capstone is not new theory — it is proving the workflow sticks under your own policies
- Docs refresh: [Pull requests](https://learn.microsoft.com/azure/devops/repos/git/pull-requests) · [Branch policies](https://learn.microsoft.com/azure/devops/repos/git/branch-policies)

## Hands-on lab (20–30 min)

1. Confirm Day 19 policies still on `main` (reviewers, linked work items, squash-only)
2. End-to-end happy path:
   ```bash
   git switch main
   git pull
   git switch -c feature/day20-phase2-recap
   ```
3. Add a short **How we use Git here** section to `README.md` (point to `docs/branching-strategy.md` / `docs/branch-policies.md` if present)
4. Commit, push, open PR with a linked work item, complete **squash** merge, delete the branch
5. Optional proof: open a second PR **without** a work item — confirm policy blocks completion
6. Write `docs/phase-2-recap.md` (bullet list of Days 11–20 takeaways)

## Commands / code

```bash
git switch -c feature/day20-phase2-recap
# Edit README.md — add "How we use Git here"
git add README.md
git commit -m "docs: document how we use Git here"
git push -u origin feature/day20-phase2-recap
# Azure DevOps: create PR → link work item → squash merge → delete branch
```

## LinkedIn post (copy-paste)

**Important:** After pasting into LinkedIn, press Enter between sections so line breaks stay visible.

```
Day 20 of #100DaysOfAzureDevOps

Yesterday: branch policies — `main` became a contract, not a suggestion.
Today: Phase 2 mini project & recap — prove the full Git loop still works under that contract.

Phase 2 was never “learn git commands.”
It was: collaboration with receipts, policies, and fewer 2 AM archaeology sessions.

What we covered in Phase 2 (Days 11–20):

1. Git fundamentals
Clone, commit, push, history as the audit trail — not “save file.”

2. Branching strategies
ADR for main + features + squash; stop inventing a new flow every sprint.

3. Azure Repos hygiene
Default branch, README, .gitignore — empty repos are not “ready.”

4. Pull requests & review
Review is a product decision, not a courtesy merge click.

5. Advanced Git
Rebase/squash with intent; history hygiene without rewriting shared truth carelessly.

6. Hooks & pre-commit
Local guardrails before the PR ever opens.

7. Forks & permissions
Who can write vs who can propose — least privilege for source.

8. Migration
History moves; secrets, CI, and apps do not. Hygiene decides the rest.

9. Branch policies
Reviewers, work items, squash-only — bypass is break-glass, not a habit.

Lab today in azure-100-labs:
Ran the full loop — feature branch → PR (linked work item) → squash merge → delete branch — and documented How we use Git here.

One-liner for Phase 2:
Git mastery is not memorizing flags.
It is making the safe path the easy path.

Tomorrow: Intro to Azure Pipelines — Phase 3 begins (CI/CD).

(Document attached: Day 20 Phase 2 Capstone & Recap PDF)

Lab notes + PDF also here:
https://bit.ly/4r4WN3m

#100DaysOfAzureDevOps #Azure #DevOps #Git #AzureRepos #CloudComputing #LearningInPublic
```

### Attach with the post (PDF handout)

Attach this document on LinkedIn (document / PDF upload):

- [`../days/day-20-phase-2-recap/handout.pdf`](../days/day-20-phase-2-recap/handout.pdf)

### How to post

1. LinkedIn → **document** → upload `days/day-20-phase-2-recap/handout.pdf`
2. Paste the text above (press **Enter** between sections so line breaks stay visible)
3. **Document title:** `Day 20 — Phase 2 Mini Project & Recap` (max 58 chars on LinkedIn)

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5–10 real comments on other Azure/DevOps posts.

## Done checklist

- [ ] End-to-end PR path completed under branch policies
- [ ] README “How we use Git here” updated
- [ ] `docs/phase-2-recap.md` written
- [ ] Published LinkedIn post with PDF handout
- [ ] Engaged with 5–10 community comments

## Tomorrow

**Day 21 — Intro to Azure Pipelines** (Phase 3 begins)

---

*Personal learning guide — views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
