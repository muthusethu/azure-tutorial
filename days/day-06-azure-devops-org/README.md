# Day 06 — Setting Up an Azure DevOps Organization

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Create a clean personal Azure DevOps org and a home project (`azure-100-labs`) for the rest of the series.

## High-level architecture (summary)

Open **[handout.pdf](./handout.pdf)** for tables. Short version:

| Layer | What it is |
|-------|------------|
| **Organization** | Tenancy: users, billing/access boundary, collection settings |
| **Project** | Container for Boards, Repos, Pipelines, Test Plans, Artifacts |
| **Process template** | Shape of work items (Agile / Scrum / Basic / CMMI) |
| **Permissions** | Collection Admin vs Project Admin vs Contributor |

**Rule:** personal Microsoft account only. No work invites.

## Learn

- [Plan your organizational structure](https://learn.microsoft.com/azure/devops/user-guide/plan-your-azure-devops-org-structure)

## Step-by-step lab

1. Open `https://dev.azure.com/<your-org>`
2. Org settings → Overview + Users/Permissions (personal only)
3. Create project `azure-100-labs` (Agile, private)
4. Set project description: `Personal 100DaysOfAzureDevOps labs — views are my own`
5. Optional: configure `az devops` defaults

## Done when

- [ ] You can explain org vs project in one sentence each  
- [ ] `azure-100-labs` exists and is private  
- [ ] No work accounts were invited  

## LinkedIn

Post draft: [`../../daily-guides/day-06.md`](../../daily-guides/day-06.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://bit.ly/4ivofF7
```

(Full path: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-06-azure-devops-org)

## Next

**Day 07** — Azure Boards deep dive.
