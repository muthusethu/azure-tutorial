# Day 10 — Phase 1 Capstone Mini Project & Recap

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Celebrate the completion of Phase 1 (Azure & DevOps Foundations). Consolidate all 5 Azure DevOps hubs in `azure-100-labs`, build an overview dashboard, and prepare for Phase 2 (Git & Repos).

## High-level architecture (summary)

Open **[handout.pdf](./handout.pdf)** for complete tables. Short version:

| Phase 1 Focus | Core Components | Key Proof Deliverable |
|:--------------|:----------------|:----------------------|
| **Azure Core** (Days 1–3) | Cloud models, CLI/PWSH, ARM, Governance | Resource hierarchy, Locks, Budget alerts |
| **DevOps Principles** (Day 4) | CALMS, DORA metrics | Deployment Frequency & MTTR mindset |
| **Azure DevOps Suite** (Days 5–10) | Boards, Repos, Pipelines, Test Plans, Artifacts | Project `azure-100-labs`, WIP limits, Test runs, Feeds |

**Hub Integration in `azure-100-labs`:**  
User Story (Boards) ↔ Code Commit (Repos) ↔ Quality Run (Test Plans) ↔ Dependency (Artifacts) ↔ Overview Dashboard

## Learn

- [Azure DevOps documentation](https://learn.microsoft.com/azure/devops/)
- [Dashboards in Azure DevOps](https://learn.microsoft.com/azure/devops/report/dashboards/overview)

## Step-by-step lab

1. Open `azure-100-labs` in Azure DevOps.
2. Verify all Phase 1 hubs are populated:
   - **Boards:** Epic, Feature, and User Stories tracked.
   - **Repos:** Initialized Git repo with `README.md`.
   - **Test Plans:** Test Plan `Phase 1 Smoke Tests` with test cases.
   - **Artifacts:** Feed `day09-packages` with upstream caching enabled.
3. Build **Overview → Dashboards** (`Phase 1 Command Center`):
   - Add Query Tile (Open stories).
   - Add Work Item chart widget.
   - Add Markdown summary widget.
4. Clean up any leftover Azure resource groups to maintain zero idle cost.

## Done when

- [ ] All 5 hubs in `azure-100-labs` are configured and verified
- [ ] `Phase 1 Command Center` dashboard is live
- [ ] No unwanted resources remain running in Azure subscription

## LinkedIn

Post draft: [`../../daily-guides/day-10.md`](../../daily-guides/day-10.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://bit.ly/4gDGA05
```

(Full path: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-10-phase-1-recap)

## Next

**Day 11** — Phase 2 Kickoff: Git Foundations for DevOps Engineers.
