# Day 39 — Multi-environment Pipeline

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 4 - Continuous Delivery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Promote the artifact, not the vibes. dependsOn is the chain. Prod does not get a second compile

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Stage | Job type | Consumes |
| --- | --- | --- |
| CI (or reuse resources.pipelines) | job: Build + PublishPipelineArtifact@1 | Source. Produces artifact drop |
| Dev | deployment:  environment: dev | download: current  artifact: drop |
| Staging | deployment:  dependsOn: Dev | The same drop. Different app settings |
| Prod | deployment:  environment: prod  dependsOn: Staging | The same drop. Approvals check from Day 38 |
| Config | App settings / variable groups per env | Not a new zip. Bits stay identical |

## Step-by-step lab

1. Pipelines → Environments → New → staging (empty). Keep prod's Approvals check from Day 38.
2. Write pipelines/multi-env.yml: stages Dev → Staging → Prod with dependsOn chain. Each is a deployment job.
3. CI publishes drop. Each env stage downloads it (download: current artifact: drop). No compile/publish in those stages.
4. Dev and Staging can echo if you are not spending. Prod must wait on the environment: prod approval.
5. Run once. Graph should show Dev, then Staging, then waiting on Approve — not three independent builds.
6. If any stage runs npm/dotnet/mvn, delete those steps. Config differences belong in variable groups, not a second artifact.

## Done when

- [ ] dependsOn chain is Dev → Staging → Prod
- [ ] Every env stage downloads drop; none rebuild
- [ ] Prod waited on the Approvals check
- [ ] Can explain why a second compile is a second dice roll

## LinkedIn

Post draft: [`../../daily-guides/day-39.md`](../../daily-guides/day-39.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-39-multi-environment-pipeline
```

## Next

**Day 40** — Phase 4 mini project — green path with visible brakes, same artifact, recap without heroics.
