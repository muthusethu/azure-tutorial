# Day 48 — Terraform Modules & Remote State

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 5 - Infrastructure as Code |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Remote state in Azure Storage with a blob lease lock. Two applies at once is a tug-of-war with reality

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Piece | Config | Why |
| --- | --- | --- |
| State RG + account | rg-tfstate / st<unique> / container tfstate | Holds the memory. Note it costs (cheap LRS) |
| backend "azurerm" | resource_group_name, storage_account_name, container_name, key | key = lab.tfstate (path in the container) |
| Lock | Blob lease while apply/plan (depending on version) | Second apply waits or errors — do not force-unlock |
| Module | modules/storage with inputs | Reuse without three nearly identical main.tf files |
| Migrate | Add backend; terraform init — migrate state? yes | Do not copy tfstate like a raccoon |

## Step-by-step lab

1. Create rg-tfstate + a Standard_LRS storage account + blob container tfstate (CLI). This account is the backend, not the app.
2. Add terraform { backend "azurerm" { ... key = "lab.tfstate" } }. terraform init and accept state migration from local.
3. Extract storage (or RG+storage) into modules/storage. Call it from main. terraform plan/apply through the backend once.
4. In Azure Storage, confirm the blob lab.tfstate exists. Do not download it to email.
5. terraform destroy the workload. Leave rg-tfstate until you are sure. If you also delete state storage, do it last.
6. If a lock exists, wait. Do not force-unlock. Write that rule in docs/tf-state-day48.md.

## Done when

- [ ] State lives in Azure Storage, not only on the laptop
- [ ] Workload RG ≠ state RG
- [ ] Did not force-unlock
- [ ] Workload destroyed; state account not deleted first

## LinkedIn

Post draft: [`../../daily-guides/day-48.md`](../../daily-guides/day-48.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-48-terraform-modules-remote-state
```

## Next

**Day 49** — IaC in pipelines — plan on a clean agent, publish the plan, apply only with a brake.
