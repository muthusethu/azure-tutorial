# Day 8 — Azure Test Plans Basics

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 1 - Azure & DevOps Foundations |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

A shared checklist so 'works on my machine' stops being a personality trait

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Object | What it is | Lab name |
| --- | --- | --- |
| Test Plan | Container for a milestone / sprint | Day08 Smoke |
| Test Suite (static) | Hand-picked cases | Portal checks |
| Requirement-based suite | Auto from a User Story | Optional: suite from Day 7 story |
| Query-based suite | WIQL of test cases | Skip until you have 10+ cases |
| Test Case (work item) | Steps: Action + Expected Result | Login to Portal; Create RG via CLI |
| Test Run / Test Point | Outcome: Passed, Failed, Blocked, Not executed | Web runner, not a pipeline yet |

## Step-by-step lab

1. azure-100-labs → Test Plans. If prompted, start the Test Plans trial on this personal org only.
2. New Test Plan → Name Day08 Smoke → Area = default team. Create.
3. Add suite → Static suite → Portal checks.
4. New Test Case: Login to Portal. Steps: (1) Open portal.azure.com (2) Confirm personal directory. Expected: subscription visible, no work tenant.
5. New Test Case: Create RG via CLI. Steps: az group create -n rg-day08-smoke -l centralindia then az group delete -n rg-day08-smoke --yes --no-wait.
6. Run for web application → mark Login Passed. Mark CLI case Passed or Blocked with a comment if az is missing.
7. Open the test case → Links → add User Story Explore Azure Test Plans (Day 7). Boards should show the test link.

## Done when

- [ ] Can explain Test Plan vs Suite vs Case vs Run
- [ ] Day08 Smoke exists with two cases and at least one executed outcome
- [ ] One case linked to a Boards User Story
- [ ] No work-org Test Plans used

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-08-azure-test-plans
```

## Next

**Day 9** — Azure Artifacts
