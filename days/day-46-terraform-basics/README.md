# Day 46 — Terraform Basics

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 5 - Infrastructure as Code |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

init / plan / apply / destroy. State is the mapping from resource addresses to Azure IDs — not a cache

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Verb | What it does | Touches Azure? |
| --- | --- | --- |
| terraform init | Download providers; later: configure backend | No (unless backend init migrates state) |
| terraform plan | Diff: desired config vs state vs reality (refresh) | Read. Does not mutate (except refresh) |
| terraform apply | Execute the plan; write terraform.tfstate | Yes |
| terraform destroy | Plan a teardown; remove from state as it deletes | Yes. Adult ending for a lab |
| terraform.tfstate | Address (azurerm_resource_group.lab) → ARM resource ID | Lose it = ghosts: create already-exists, destroy skips live RGs |

## Step-by-step lab

1. Install Terraform (terraform -version). Confirm it is on PATH.
2. New folder infra/tf-day46/. gitignore terraform.tfstate and .terraform/. Write a resource group only (starter).
3. terraform init then terraform plan. Read the plan. Then terraform apply (type yes or -auto-approve on this disposable RG).
4. az group show -n rg-day46-tf. Confirm reality matches state (terraform state list).
5. Do not delete terraform.tfstate in Explorer. That is how ghosts start.
6. terraform destroy -auto-approve. Confirm the RG is gone. If destroy fails, do not shrug — fix it tonight.

## Done when

- [ ] init → plan → apply → destroy all ran
- [ ] tfstate is gitignored, not deleted as cleanup
- [ ] RG gone at the end of the night
- [ ] Can explain state as ID mapping, not a cache

## LinkedIn

Post draft: [`../../daily-guides/day-46.md`](../../daily-guides/day-46.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-46-terraform-basics
```

## Next

**Day 47** — Terraform with Azure (azurerm) — features {}, CLI auth, RG + storage. No subscription-Owner robot.
