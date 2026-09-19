# Day 7 — Azure Boards Deep Dive

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 1 - Azure & DevOps Foundations |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Epic to Task is a planning graph. WIP limits keep the board honest.

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Type | Parent / child | This series example |
| --- | --- | --- |
| Epic | Top of the tree | 100 Days Learning |
| Feature | Child of Epic | Phase 1 Foundations |
| User Story | Child of Feature; AB# links to PRs later | Explore Azure Test Plans |
| Task | Child of Story; hours optional | Create test plan, add 2 cases |
| Bug | Can hang off Story or backlog | Use when a lab step actually fails |
| Issue (Agile) | Impediment, not a delivery item | Skip unless blocked on SKU/trial |

## Step-by-step lab

1. Boards → Work items → New Work Item → Epic → Title 100 Days Learning → Save. Note the ID.
2. New Feature Phase 1 Foundations → Add link → Parent → the Epic. Save.
3. Create 3 User Stories as children of the Feature: Explore Azure Test Plans; Create Azure Artifacts feed; Stand up end-to-end mini project.
4. Boards → Boards → drag one story New/To Do → Active/Doing → Closed/Done. Watch the column counts.
5. Board settings (gear) → Columns → Doing → WIP limit 3. Save.
6. Boards → Queries → New query → Work Item Type = User Story AND State <> Closed → Save as Open stories.
7. Open one story → Related Work. You will link a PR here in Phase 2. Do not invent fake employer sprints.

## Done when

- [ ] Can explain Epic → Feature → User Story → Task
- [ ] Hierarchy exists in azure-100-labs
- [ ] One story moved to Done on the board; WIP set on Doing
- [ ] Saved query: User Story AND State <> Closed

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-07-azure-boards
```

## Next

**Day 8** — Azure Test Plans basics
