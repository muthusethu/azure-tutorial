# Day 08 — Azure Test Plans Basics

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Understand the hierarchy of Azure Test Plans (Plan → Suite → Case → Run) and how manual / exploratory tests link back to Azure Boards work items.

## High-level architecture (summary)

Open **[handout.pdf](./handout.pdf)** for tables. Short version:

| Level | Role |
|-------|------|
| **Test Plan** | Top-level container for a sprint, release, or milestone |
| **Test Suite** | Grouping of test cases (Static, Requirement-based, Query-based) |
| **Test Case** | Discrete test scenario with step-by-step action + expected outcome |
| **Test Run** | Execution instance recording Pass, Fail, Blocked, and bug links |

**Traceability loop:** User Story (Boards) ↔ Test Case (Test Plans) ↔ Test Run ↔ Bug (Boards)

## Learn

- [Azure Test Plans overview](https://learn.microsoft.com/azure/devops/test/overview)

## Step-by-step lab

1. Open `azure-100-labs` → **Test Plans**
2. Create Test Plan `Phase 1 Smoke Tests`
3. Add a Static Suite `Portal & CLI Baseline`
4. Add 2 Test Cases:
   - `TC01: Verify Azure login and personal subscription directory`
   - `TC02: Verify resource group creation via Azure CLI`
5. Execute via Web Runner → mark steps Passed / Blocked
6. Link test case to a User Story in Boards to inspect end-to-end traceability

## Done when

- [ ] You can explain Test Plan vs Suite vs Case vs Run
- [ ] Test Plan and test cases exist in `azure-100-labs`
- [ ] You executed at least one test run and recorded results

## LinkedIn

Post draft: [`../../daily-guides/day-08.md`](../../daily-guides/day-08.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://bit.ly/4zHsGD3
```

(Full path: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-08-azure-test-plans)

## Next

**Day 09** — Azure Artifacts.
