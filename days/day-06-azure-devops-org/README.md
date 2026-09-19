# Day 6 — Setting Up an Azure DevOps Org

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 1 - Azure & DevOps Foundations |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Org is the tenancy. Project is the gym. Empty projects build no muscle.

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Layer | Controls | Lab choice |
| --- | --- | --- |
| Organization | Users, OAuth apps, agent pools, billing, Policies | Personal MSA owner only |
| Project | Boards/Repos/Pipelines/Test/Artifacts isolation | azure-100-labs (private) |
| Process | Work item types + states (Agile/Scrum/Basic/CMMI) | Agile for this series |
| Team | Backlog, area, iteration, board columns | Default project team is enough |
| Repo | Git (default) vs TFVC (do not use TFVC here) | Git, default branch main (Day 13) |
| Parallel jobs | Microsoft-hosted vs self-hosted job SKUs | Free Microsoft-hosted minute pool |

## Step-by-step lab

1. https://dev.azure.com/<your-org> → Organization settings (bottom left) → Overview. Note org name and owner email.
2. Organization settings → Users. Confirm only your personal Microsoft account. Remove any work guest.
3. Organization settings → Permissions → Project Collection Administrators. You only.
4. New project → Name azure-100-labs → Private → Process Agile → Create.
5. Project settings → Overview → Description: Personal 100DaysOfAzureDevOps labs - views are my own.
6. az extension add --name azure-devops && az devops configure --defaults organization=https://dev.azure.com/<your-org> project=azure-100-labs
7. az devops project list -o table && az devops project show --project azure-100-labs -o jsonc

## Done when

- [ ] Can explain organization vs project vs process template
- [ ] azure-100-labs exists, private, Agile
- [ ] No work accounts in Org settings → Users
- [ ] az devops configure defaults point at this org + project

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-06-azure-devops-org
```

## Next

**Day 7** — Azure Boards deep dive
