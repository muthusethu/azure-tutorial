# Day 07 — Azure Boards Deep Dive

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Plan the 100-day journey in Azure Boards: hierarchy, board flow, and a reusable query.

## High-level architecture (summary)

Open **[handout.pdf](./handout.pdf)** for tables. Short version:

| Level | Purpose |
|-------|---------|
| **Epic** | Large initiative (e.g. 100 Days Learning) |
| **Feature** | Phase or theme (e.g. Phase 1 Foundations) |
| **User Story** | One finishable outcome |
| **Task / Bug** | Steps or defects |

**Flow:** Backlog → Sprint / Board columns → Done

## Learn

- [What is Azure Boards?](https://learn.microsoft.com/azure/devops/boards/get-started/what-is-azure-boards)

## Step-by-step lab

1. Open project `azure-100-labs` → **Boards**
2. Create Epic `100 Days Learning`
3. Add Feature `Phase 1 Foundations`
4. Add 3 User Stories (Days 8–10 topics)
5. Move one story To Do → Doing → Done
6. Query: Work Item Type = User Story AND State <> Done

## Done when

- [ ] Hierarchy exists in Boards  
- [ ] One story completed on the board  
- [ ] “Open stories” query saved or noted  

## LinkedIn

Post draft: [`../../daily-guides/day-07.md`](../../daily-guides/day-07.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://bit.ly/45RGZXX
```

(Full path: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-07-azure-boards)

## Next

**Day 08** — Azure Test Plans basics.
