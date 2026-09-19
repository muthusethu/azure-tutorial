# Day 10 — Mini Project + Recap (Phase 1)

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 1 - Azure & DevOps Foundations |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Five hubs + ARM hygiene in one personal project before Git gets serious

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Track | Days | Proof in azure-100-labs |
| --- | --- | --- |
| Cloud models | 1 | Can name IaaS/PaaS/SaaS + region vs AZ |
| Clients + ARM | 2–3 | az group + tags/locks understood; lab RGs gone |
| CALMS / DORA | 4 | docs/calms-dora-day04.md (local or in repo) |
| Five hubs | 5–9 | Boards tree, Test Plan, Artifacts feed |
| Org hygiene | 6 | Personal org; PCA = you; project private Agile |
| Git bootstrap | 10 | README on default branch; clone URL works |

## Step-by-step lab

1. Boards: confirm Epic 100 Days Learning, Feature Phase 1 Foundations, at least 3 stories. Fix if missing.
2. Repos → Files. If empty: Initialize with a README. If clone exists, skip to the git commands below.
3. Locally: git clone https://dev.azure.com/<org>/azure-100-labs/_git/azure-100-labs && add README content && git push.
4. Overview → Dashboards → New dashboard Phase 1 Command Center → add Chart for work items using query Open stories.
5. Artifacts: confirm feed day09-packages. Test Plans: confirm Day08 Smoke still exists.
6. az group list --query "[?starts_with(name, 'rg-day')].{name:name, loc:location}" -o table → delete leftovers.
7. Write 5 lines in README: what stuck, what was confusing. Personal voice. No client names.

## Done when

- [ ] Can recap IaaS/PaaS/SaaS, ARM tags/locks, CALMS, DORA, five hubs
- [ ] azure-100-labs has Git README + Boards tree + Artifacts feed + Test Plan
- [ ] Dashboard widget exists from a real query
- [ ] No leftover rg-day* resource groups (or listed why kept)

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-10-phase-1-recap
```

## Next

**Day 11** — Git fundamentals
