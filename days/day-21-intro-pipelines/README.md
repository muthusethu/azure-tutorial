# Day 21 — Intro to Azure Pipelines

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | Phase 3 — Continuous Integration |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Create the first YAML pipeline: trigger, hosted agent, one echo step.

## High-level architecture (summary)

Open **[handout.pdf](./handout.pdf)** for complete tables. Short version:

| Piece | Role |
|:------|:-----|
| **YAML in Git** | The contract — reviewed with the code |
| **Agent pool** | Who executes (hosted vs self-hosted) |
| **Run** | The receipt — logs you can audit |

## Learn

- [What is Azure Pipelines?](https://learn.microsoft.com/azure/devops/pipelines/get-started/what-is-azure-pipelines)

## Step-by-step lab

1. New pipeline → Azure Repos Git → `azure-100-labs`
2. Commit `azure-pipelines.yml` (`ubuntu-latest`, echo Hello)
3. Run once; confirm image in the log
4. Write `docs/pipelines-day21.md`

## Done when

- [ ] Pipeline run succeeded
- [ ] YAML lives in Git (not only Classic)
- [ ] Notes captured

## LinkedIn

Post draft: [`../../daily-guides/day-21.md`](../../daily-guides/day-21.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://bit.ly/4iWaf7t
```

(Full path: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-21-intro-pipelines)

## Next

**Day 22** — Microsoft-hosted vs self-hosted agents.
