# Day 14 — Pull Requests & Code Review

| | |
|---|---|
| **Date** | 3 Sep 2026 |
| **Phase** | 2 — Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Practice the Pull Request (PR) workflow in Azure Repos: templates, linked work items, review etiquette, and a self-review checklist. Publish Day 14 on LinkedIn with the PDF handout.

## Learn (20–30 min)

- What a PR is: a request to merge changes with review, discussion, and optional build validation
- PR anatomy: title, description, reviewers, work item links, commits, files changed
- PR templates (`.azuredevops/pull_request_template.md`) — force clarity before merge
- Review etiquette: comment on code and risk, not on the person; prefer questions over commands
- Linked work items: Boards ↔ Repos traceability (AB#123 or UI link)
- Docs: [Pull requests in Azure Repos](https://learn.microsoft.com/azure/devops/repos/git/pull-requests)

## Hands-on lab (20–30 min)

1. In your local `azure-100-labs` clone (or continue from Day 12/13 feature branch):
   ```bash
   git switch main
   git pull
   git switch -c feature/day14-pr-template
   ```
2. Create a PR template:
   ```bash
   mkdir -p .azuredevops
   ```
3. Add `.azuredevops/pull_request_template.md` (see Commands section)
4. Commit and push:
   ```bash
   git add .azuredevops/pull_request_template.md
   git commit -m "chore: add pull request template"
   git push -u origin feature/day14-pr-template
   ```
5. In Azure Repos → **Pull requests** → **New pull request**:
   - Source: `feature/day14-pr-template` → Target: `main`
   - Fill the template (What / Why / Test plan / Risk)
   - Link a User Story or Task from Boards
   - Complete a self-review of the Files tab before inviting reviewers

## Commands / code

```markdown
# .azuredevops/pull_request_template.md

## What
-

## Why
-

## Test plan
- [ ] Local build / sanity check
- [ ] Linked work item
- [ ] No secrets or .env files in the diff

## Risk
- Low / Med / High

## Notes for reviewers
-
```

## LinkedIn post (copy-paste)

**Important:** After pasting into LinkedIn, press Enter between sections so line breaks stay visible.

```
Day 14 of #100DaysOfAzureDevOps

Yesterday: Azure Repos setup — folders, .gitignore, remote hygiene.
Today: the human gate before merge — Pull Requests & code review.

A PR without a description is not "agile."
It is unpaid archaeology for every reviewer who opens it.

In Azure Repos, a good pull request is more than a merge button:

1. Clear title
What changed — not "fix" or "update."

2. Description that answers three questions
• What changed?
• Why now?
• How did you verify it?

3. Linked work item
Boards ↔ Repos. AB#123 is not bureaucracy — it is the audit trail.

4. Self-review before you assign reviewers
Open the Files tab. Pretend you did not write it.
Catch the debug log, the leftover TODO, the .env you almost pushed.

5. Review etiquette that scales
• Comment on risk and clarity, not personality
• Prefer questions: "What happens if X is null?"
• Approve when ready — not when polite

PR templates force the first four.
Culture enforces the fifth.

Lab today in azure-100-labs:
Added .azuredevops/pull_request_template.md, opened a PR to main, linked a work item, and ran a self-review checklist before merge.

One-liner:
A PR is a contract between the author and the team.
If the contract is empty, do not expect a safe merge.

Tomorrow: Advanced Git — rebase, squash, and history hygiene.

(Document attached: Day 14 Pull Requests & Code Review handout PDF)

Lab notes + PDF also here:
https://bit.ly/3TcZSlk

#100DaysOfAzureDevOps #Azure #DevOps #Git #AzureRepos #CodeReview #CloudComputing #LearningInPublic
```

### Attach with the post (PDF handout)

Attach this document on LinkedIn (document / PDF upload):

- [`../days/day-14-pull-requests/handout.pdf`](../days/day-14-pull-requests/handout.pdf)

### How to post

1. LinkedIn → **document** → upload `days/day-14-pull-requests/handout.pdf`
2. Paste the text above (press **Enter** between sections so line breaks stay visible)
3. **Document title:** `Day 14 — Pull Requests & Code Review` (max 58 chars on LinkedIn)

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5–10 real comments on other Azure/DevOps posts.

## Done checklist

- [ ] Understood PR anatomy and review etiquette
- [ ] Added `.azuredevops/pull_request_template.md`
- [ ] Opened a PR, linked a work item, completed self-review
- [ ] Published LinkedIn post with PDF handout
- [ ] Engaged with 5–10 community comments

## Tomorrow

**Day 15 — Advanced Git (rebase, squash, history hygiene)**

---

*Personal learning guide — views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
