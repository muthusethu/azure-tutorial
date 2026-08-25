# Day 05 — Azure DevOps Services Overview

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Understand the five Azure DevOps services and how they connect from planning to delivery.

## High-level architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the flow tables. Short version:

| Service | Job |
|---------|-----|
| **Boards** | Plan and track work |
| **Repos** | Store code and manage PR workflow |
| **Pipelines** | Build, test, and deploy |
| **Test Plans** | Capture manual and exploratory testing |
| **Artifacts** | Host versioned package feeds |

**Flow:** Plan -> Code -> Build/Deploy -> Validate -> Distribute

## Learn

- [What is Azure DevOps?](https://learn.microsoft.com/azure/devops/user-guide/what-is-azure-devops)

## Step-by-step lab

1. Create a personal org at `https://dev.azure.com`
2. Create project `day05-overview` (Agile, private)
3. Create one User Story in Boards
4. Initialize repo with README in Repos
5. Open New Pipeline wizard in Pipelines (no run required)
6. Open Test Plans and Artifacts once

## Done when

- [ ] You can explain the role of each hub
- [ ] You created one project and used all five hubs
- [ ] You can describe the end-to-end flow from idea to release

## LinkedIn

Post draft: [`../../daily-guides/day-05.md`](../../daily-guides/day-05.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://bit.ly/4giLVv7
```

(Full path: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-05-azure-devops-services)
## Next

**Day 06** — Setting up an Azure DevOps organization.
