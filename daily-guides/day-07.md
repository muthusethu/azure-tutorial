# Day 7 — Azure Boards Deep Dive

| | |
|---|---|
| **Date** | 27 Aug 2026 |
| **Phase** | 1 — Azure & DevOps Foundations |
| **Time box** | 60–90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Use Azure Boards to plan the 100-day journey: hierarchy, backlog, board flow, and a simple query. Publish Day 7 on LinkedIn with the PDF handout.

## Learn (20–30 min)

- Work items: Epic → Feature → User Story → Task / Bug
- Backlogs, sprints, Kanban columns, queries, dashboards
- WIP limits — why “Doing” should not become a parking lot
- Docs: [What is Azure Boards?](https://learn.microsoft.com/azure/devops/boards/get-started/what-is-azure-boards)

## Hands-on lab (20–30 min)

1. In `azure-100-labs`, open **Boards**
2. Create Epic: `100 Days Learning`
3. Add Feature: `Phase 1 Foundations`
4. Add 3 User Stories (e.g. Days 8–10 topics)
5. Move one story **To Do → Doing → Done** on the board
6. Create a query: Work Item Type = User Story **AND** State <> Done

## Commands / code

```bash
# Example story titles under Phase 1:
# - Explore Azure Test Plans
# - Create Azure Artifacts feed
# - Stand up end-to-end mini project
#
# Optional: save query as "Open stories" for reuse
```

## LinkedIn post (copy-paste)

**Important:** After pasting into LinkedIn, press Enter between sections so line breaks stay visible.

```
Day 7 of #100DaysOfAzureDevOps

Yesterday we set up the org and home project.
Today we make the board tell the truth.

Azure Boards is not a wall of tickets.
It is a map of flow — or a museum of work that never finished.

Hierarchy that actually helps:

• Epic — the big journey (100 days of learning)
• Feature — a phase or theme
• User Story — one deliverable you can finish
• Task / Bug — the small steps or fixes

A board with 40 items in Doing is not “busy.”
It is a confession that WIP has no limit.

Lab today in azure-100-labs:
Epic for the 100-day series, Feature for Phase 1,
three User Stories, one item moved To Do → Doing → Done,
plus a query for “stories not done yet.”

One-liner:
Backlog = what we might do.
Board = what we are doing now.
Query = what we forgot to close.

Tomorrow: Azure Test Plans basics.

(Document attached: Day 7 Azure Boards handout PDF)

Lab notes + PDF also here:
https://bit.ly/45RGZXX

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### Attach with the post (PDF handout)

Attach this document on LinkedIn (document / PDF upload):

- [`../days/day-07-azure-boards/handout.pdf`](../days/day-07-azure-boards/handout.pdf)

### How to post

1. LinkedIn → **document** → upload `days/day-07-azure-boards/handout.pdf`
2. Paste the text above (press **Enter** between sections so line breaks stay visible)
3. **Document title:** `Day 7 — Azure Boards Deep Dive` (max 58 chars on LinkedIn)

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5–10 real comments on other Azure/DevOps posts.

## Done checklist

- [ ] Learned Epic → Feature → Story → Task/Bug
- [ ] Created hierarchy in `azure-100-labs`
- [ ] Moved one story across the board
- [ ] Saved a “not done” query
- [ ] Published LinkedIn post with PDF handout
- [ ] Engaged with 5–10 community comments

## Tomorrow

**Azure Test Plans basics**

---

*Personal learning guide — views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
