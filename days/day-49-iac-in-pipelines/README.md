# Day 49 — IaC in Pipelines

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 5 - Infrastructure as Code |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Plan in CI on a clean agent. Apply the plan you reviewed — not a second plan nobody saw

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Stage | Command | Output |
| --- | --- | --- |
| CI Plan | terraform plan -out=tfplan  (or az deployment group what-if) | Reviewed diff + binary/json plan file |
| Publish | PublishPipelineArtifact@1  artifact: tfplan | The exact plan Apply must consume |
| Apply | terraform apply tfplan   after approval / apply=true | Mutates Azure. Same plan, not a fresh one |
| Bicep track | what-if in Plan; deployment create in Apply | Same brake. No 'it worked on my laptop' |
| Identity | azure-100-sc scoped to the lab RG | Not Owner on the subscription |

## Step-by-step lab

1. Pipeline stage Plan: terraform init -input=false, terraform plan -out=tfplan (Bicep: what-if). Publish tfplan (or the what-if log).
2. Stage Apply dependsOn Plan, condition succeeded(), and either environment: prod approval or eq(variables['apply'], 'true').
3. Apply step: terraform apply -input=false tfplan (download the artifact first). Do not run a new plan there.
4. Queue once with apply=false / no approval path — confirm Apply skipped. Queue again with the brake released.
5. If the apply changes something the published plan did not show, stop. Versions or backend drifted.
6. Destroy via pipeline or local after the screenshot. Do not leave rg-day49-lab.

## Done when

- [ ] Plan ran on the agent, not only on the laptop
- [ ] Apply consumed the published plan file
- [ ] A skipped Apply run exists (brake worked)
- [ ] Service connection is not subscription Owner

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-49-iac-in-pipelines
```

## Next

**Day 50** — Phase 5 mini project — one RG + storage or webapp skeleton from the chosen IaC in a pipeline, then destroy.
