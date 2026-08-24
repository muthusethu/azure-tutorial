# Day 7 - Azure Boards Deep Dive

| | |
|---|---|
| **Date** | 27 Aug 2026 |
| **Phase** | 1 - Azure & DevOps Foundations |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Work items: Epic -> Feature -> User Story -> Task/Bug
- Backlogs, sprints, Kanban boards, queries, dashboards
- Docs: https://learn.microsoft.com/azure/devops/boards/get-started/what-is-azure-boards

## Hands-on lab (20-30 min)

1. In `azure-100-labs`, create Epic '100 Days Learning'
2. Add Feature 'Phase 1 Foundations' + 3 User Stories for Days 8-10
3. Move one story across To Do -> Doing -> Done on the board
4. Create a simple query: Work Item Type = User Story AND State <> Done

## Commands / code

```bash
# Example story titles:
# - Explore Azure Test Plans
# - Create Azure Artifacts feed
# - Stand up end-to-end mini project
```

## LinkedIn post (copy-paste)

**Post 1 of 2 today.** Production story is a **separate** post — [Note 2](../publish/production-grade/notes.md).

```
Day 7 of #100DaysOfAzureDevOps

Azure Boards is not a wall of tickets.
It is a map of flow — or a museum of work that never finished.

Epic → Feature → Story → Task is useful.
A board with 40 items in Doing is a confession.

WIP limits feel rude until production teaches you:
context-switching is how bugs hide.

Lab today: Epic for the 100-day journey, stories for Phase 1,
one item moved To Do → Doing → Done, plus a “not done” query.

Tomorrow: Azure Test Plans basics.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5-10 real comments on other Azure/DevOps posts.

## Reminder — 2nd LinkedIn post (production track)

**Today you publish TWO separate LinkedIn posts.** The daily lesson above is post 1 only.

| | Post 1 — #100DaysOfAzureDevOps | Post 2 — #ProductionGradeAzure |
|---|-------------------------------|----------------------------------|
| **When** | ~10:00 IST | ~17:00–19:00 IST (after some engagement on post 1) |
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 2 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 2 of 33 (rewrite with your real experience)
- [ ] Record URLs in [`publish/production-grade/LINKS.md`](../publish/production-grade/LINKS.md)

Run: `python scripts/production_reminder.py`

## Done checklist

- [ ] Learned the topic (docs or short video)
- [ ] Completed the lab steps
- [ ] Ran / saved the commands or code
- [ ] Published LinkedIn post
- [ ] Engaged with 5-10 community comments
- [ ] Deleted spare Azure resources if any (cost control)

## Tomorrow

**Azure Test Plans basics**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
