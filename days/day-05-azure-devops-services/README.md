# Day 5 — Azure DevOps Services Overview

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 1 - Azure & DevOps Foundations |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Five hubs pretending to be one product — plan, store, ship, prove, package

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Step | Hub | Artifact you should see |
| --- | --- | --- |
| 1 Plan | Boards | User Story / Bug with State, Area, Iteration |
| 2 Store | Repos | Git commit SHA on refs/heads/main |
| 3 Review | Repos PRs | PR linked to work item via AB#id |
| 4 Ship | Pipelines | YAML run: jobs, steps, logs, artifacts |
| 5 Prove | Test Plans | Test case + run result Pass/Fail/Blocked |
| 6 Package | Artifacts | Feed views @local / @prerelease / @release |

## Step-by-step lab

1. https://dev.azure.com → create organization (personal Microsoft account). Skip any work-directory invite.
2. New project → Name day05-overview → Visibility Private → Process Agile → Create.
3. Left nav → Boards → Work items → New User Story 'Touch all five hubs'. Save.
4. Repos → Files → Initialize with a README. Note the clone URL https://dev.azure.com/<org>/day05-overview/_git/day05-overview
5. Pipelines → Create Pipeline → Azure Repos Git → select the repo → inspect the YAML starter. Cancel without saving if you want Day 21 to be the first YAML.
6. Test Plans hub → open once (enable trial if prompted). Artifacts → open once. Do not post screenshots of emails or tenant names.
7. Bookmark https://dev.azure.com/<org>/day05-overview. Tomorrow you create the long-lived project azure-100-labs.

## Done when

- [ ] Can name all five hubs and what each produces
- [ ] Personal org exists; project day05-overview is private Agile
- [ ] Opened Boards, Repos, Pipelines, Test Plans, Artifacts once
- [ ] No work org screenshots, no employer users invited

## LinkedIn

Post draft: [`../../daily-guides/day-05.md`](../../daily-guides/day-05.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-05-azure-devops-services
```

## Next

**Day 6** — Setting up an Azure DevOps organization
