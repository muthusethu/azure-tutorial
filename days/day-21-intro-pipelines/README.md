# Day 21 — Intro to Azure Pipelines

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 3 - Continuous Integration |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

A robot that runs the build so you can stop being the robot

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Piece | YAML / product | What it does |
| --- | --- | --- |
| Pipeline definition | azure-pipelines.yml in Git | Versioned with the code |
| Trigger | trigger: branches include main | Start a run on push |
| Pool | pool.vmImage: ubuntu-latest | Microsoft-hosted agent VM |
| Job | jobs.job (implicit job if only steps) | Unit of agent allocation |
| Step | script / task / checkout | Process on the agent |
| Run / logs | Pipelines → Runs → Job log | The product you actually debug |

## Step-by-step lab

1. Pipelines → Create Pipeline → Azure Repos Git → azure-100-labs → Starter pipeline.
2. Replace the body with the YAML in this handout. Save as /azure-pipelines.yml (repo root) on a feature branch or main via PR.
3. Run pipeline. Open the job log. Find the image / Agent name / Agent.OS lines — that is hosted proof.
4. Confirm YAML has pool: vmImage: ubuntu-latest (not pool: Default).
5. Org settings → Agent pools / Parallel jobs. Note Microsoft-hosted vs any Default pool. Do not register an agent today.
6. Optional: Project settings → Pipelines → Settings → disable creation of classic build/release if the toggle exists.
7. PR the YAML if main is policy-protected. Keep the first green run ID in notes.

## Done when

- [ ] Can name trigger, pool, job, step, run log
- [ ] Green run on ubuntu-latest with Hello in the log
- [ ] YAML lives in Git (not only Classic GUI)
- [ ] Did not register a self-hosted agent

## LinkedIn

Post draft: [`../../daily-guides/day-21.md`](../../daily-guides/day-21.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-21-intro-pipelines
```

## Next

**Day 22** — Microsoft-hosted vs self-hosted agents
