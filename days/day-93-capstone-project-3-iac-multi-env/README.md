# Day 93 — Capstone Project 3 - IaC Multi-env

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 10 - Portfolio & Public Launch |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

If a stranger cannot recreate the env from Git, the demo is still a toy

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Box | Personal Azure / Git object | Rule |
| --- | --- | --- |
| Module / file | capstone/infra/ (Bicep or Terraform — same dialect as Phase 5) | Do not switch languages this week for spice |
| Dev parameters | dev.bicepparam or terraform/dev.tfvars | SKU F1 / consumption; short names via uniqueString |
| Staging parameters | stg.bicepparam or terraform/stg.tfvars | Same module, different param file — no infra-prod-FINAL folder |
| State / deploy | Remote state (Day 48) or a pipeline service connection | Local state is a rumor you cannot share |
| Pipeline | pipelines/infra.yml or capstone/infra-pipeline.yml | plan in CI; apply gated by Environment approval |
| App artifact | Still Day 39: promote the image/zip, do not rebuild in staging | Infra apply ≠ app rebuild |

## Step-by-step lab

1. Add capstone/infra/ in the same dialect you used in Phase 5 (Bicep or Terraform). One module: RG + the runtime (App Service plan/app or Container Apps env) + ACR if still needed.
2. Add two parameter files (dev and staging). Different names/SKUs; same module. No copied folder named infra-prod-final-FINAL.
3. Write pipelines/infra.yml (or capstone/infra-pipeline.yml): plan/what-if on every run; apply gated by an Azure DevOps Environment.
4. Apply dev from the pipeline. Wire Day 91/92 app deploy to the outputs (hostname, ACR). Confirm /health.
5. Apply staging only after you read the plan. Promote the same app artifact — do not rebuild.
6. Put destroy steps in capstone/README.md. Destroy non-prod when the screenshot exists. Do not keep two plans as souvenirs.
7. A stranger should recreate the env from the repo without you on a screenshare. If not, the README is the bug.

## Done when

- [ ] capstone/infra/ uses one module and two param files
- [ ] Pipeline prints plan/what-if; apply is gated
- [ ] Same app artifact promoted onto the IaC outputs
- [ ] Non-prod destroy steps are in the README and you ran them (or scheduled tonight)
- [ ] No employer modules, no dialect switch for spice

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-93-capstone-project-3-iac-multi-env
```

## Next

**Day 94** — GitHub portfolio setup — open the blinds with a sanitized README a stranger can follow
