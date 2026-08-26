# Day 6 — Setting Up an Azure DevOps Organization

| | |
|---|---|
| **Date** | 26 Aug 2026 |
| **Phase** | 1 — Azure & DevOps Foundations |
| **Time box** | 60–90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Set up a clean personal Azure DevOps organization and a home project for the rest of the 100 days. Publish Day 6 on LinkedIn with the PDF handout.

## Learn (20–30 min)

- Organization vs project vs process template (Agile / Scrum / Basic / CMMI)
- Who can do what: Project Collection Administrators vs Project Admins vs Contributors
- Personal-only rule: no work tenants, no work invites, no employer data
- Docs: [Plan your organizational structure](https://learn.microsoft.com/azure/devops/user-guide/plan-your-azure-devops-org-structure)

## Hands-on lab (20–30 min)

1. Open your personal org at `https://dev.azure.com/<your-org>` (create one if Day 5 was skipped)
2. Org settings → Overview: note org name and owner
3. Org settings → Users / Permissions: confirm only your personal account
4. Create project `azure-100-labs` (Agile, private) — this becomes your home project
5. Project Settings → Overview: set description to `Personal 100DaysOfAzureDevOps labs — views are my own`
6. Optional: `az devops` CLI defaults for this org + project

## Commands / code

```bash
# Optional Azure DevOps CLI
az extension add --name azure-devops
az login
az devops configure --defaults organization=https://dev.azure.com/<your-org> project=azure-100-labs
az devops project list -o table
az devops project show --project azure-100-labs -o table
```

## LinkedIn post (copy-paste)

**Important:** After pasting into LinkedIn, press Enter between sections so line breaks stay visible.

```
Day 6 of #100DaysOfAzureDevOps

Yesterday we mapped the five hubs.
Today we build the house those hubs live in.

An Azure DevOps organization is not “just an account.”
It is the boundary for:
• who can sign in
• which projects exist
• which process template shapes your boards
• who is Collection Admin vs Contributor

Wrong setup early = messy permissions and mixed personal/work later.

What I set up today (personal only):

• Org overview checked — name, owner, no surprise users
• Permissions reviewed — Collection Admins are minimal
• Project created: azure-100-labs (Agile, private)
• Description set so future-me remembers this is a lab, not production

Process templates in one line:
Agile / Scrum / Basic / CMMI = how work items are shaped.
For this series: Agile is enough.

One-liner:
Org = tenancy and access.
Project = where the work lives.
Keep both personal, clean, and boring.

Tomorrow: Azure Boards deep dive — Epics, Features, Stories, and WIP that does not lie.

(Document attached: Day 6 Azure DevOps Org Setup handout PDF)

Lab notes + PDF also here:
https://bit.ly/4ivofF7

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### Attach with the post (PDF handout)

Attach this document on LinkedIn (document / PDF upload):

- [`../days/day-06-azure-devops-org/handout.pdf`](../days/day-06-azure-devops-org/handout.pdf)

### How to post

1. LinkedIn → **document** → upload `days/day-06-azure-devops-org/handout.pdf`
2. Paste the text above (press **Enter** between sections so line breaks stay visible)
3. **Document title:** `Day 6 — Azure DevOps Org Setup` (max 58 chars on LinkedIn)

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5–10 real comments on other Azure/DevOps posts.

## Done checklist

- [ ] Learned org vs project vs process template
- [ ] Confirmed personal-only users on the org
- [ ] Created `azure-100-labs` project
- [ ] Published LinkedIn post with PDF handout
- [ ] Engaged with 5–10 community comments

## Tomorrow

**Azure Boards deep dive**

---

*Personal learning guide — views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
