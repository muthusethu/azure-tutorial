# Day 3 — Azure Resource Manager (ARM) Basics

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 1 - Azure & DevOps Foundations |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Every Portal click is an ARM call — tags, locks, providers

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Layer | ARM job | Lab command / type |
| --- | --- | --- |
| Client | Portal / az / PowerShell / SDK / pipeline | az group create, az lock create |
| ARM control plane | AuthN/Z, validate schema, orchestrate | management.azure.com REST |
| Management group | Policy + RBAC above subscriptions | Skip for personal lab; know it exists |
| Subscription | Quota, billing, RBAC assignment scope | az account show |
| Resource group | Deploy scope + delete scope + tag rollup | Microsoft.Resources/resourceGroups |
| Resource provider | Microsoft.Storage, Microsoft.Web, Microsoft.Compute | az provider list --query [].namespace |

## Step-by-step lab

1. az group create -n rg-day03-lab -l centralindia --tags Project=100Days Owner=personal Env=lab
2. portal.azure.com → rg-day03-lab → Tags. Confirm the three tags. Cost Management → Cost analysis → Group by Tag: Project.
3. az lock create --name cannot-delete --lock-type CanNotDelete --resource-group rg-day03-lab
4. az group delete -n rg-day03-lab --yes  (expect failure while locked). Read the error; do not force anything else.
5. az lock list --resource-group rg-day03-lab -o table → az lock delete --name cannot-delete --resource-group rg-day03-lab
6. az provider list --query [].namespace -o tsv | more  (Windows: findstr Microsoft). Note Microsoft.Resources / Microsoft.Web.
7. az group delete -n rg-day03-lab --yes --no-wait. Confirm az group show -n rg-day03-lab fails.

## Done when

- [ ] Can explain ARM as the control plane behind Portal and CLI
- [ ] Applied Project/Owner/Env tags on rg-day03-lab
- [ ] Proved CanNotDelete blocks az group delete
- [ ] Removed the lock and deleted the RG

## LinkedIn

Post draft: [`../../daily-guides/day-03.md`](../../daily-guides/day-03.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-03-arm-basics
```

## Next

**Day 4** — DevOps principles & culture
