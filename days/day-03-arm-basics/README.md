# Day 03 — Azure Resource Manager (ARM) Basics

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Understand **ARM** as Azure’s control plane. Practice **tags** and **resource locks**.

## High-level architecture (summary)

Open **[handout.pdf](./handout.pdf)** for diagrams. Short version:

| Concept | Role |
|---------|------|
| **You** | Decide the change (Portal / CLI / PowerShell) |
| **ARM** | Control plane — authz, validation, orchestration |
| **Resource providers** | Create/update the actual resource |
| **Tags** | Metadata for cost, owner, environment |
| **Locks** | Prevent accidental delete/change |

**Hierarchy:** Management group → Subscription → Resource group → Resource

## Learn

- [ARM overview](https://learn.microsoft.com/azure/azure-resource-manager/management/overview)

## Step-by-step lab

```bash
az group create -n rg-day03-lab -l centralindia \
  --tags Project=100Days Owner=personal Env=lab

az lock create --name cannot-delete --lock-type CanNotDelete \
  --resource-group rg-day03-lab

# Expect failure while locked:
# az group delete -n rg-day03-lab --yes

az lock delete --name cannot-delete --resource-group rg-day03-lab
az group delete -n rg-day03-lab --yes --no-wait
```

## Done when

- [ ] You can explain ARM vs Portal/CLI in one sentence  
- [ ] You applied tags and a CanNotDelete lock  
- [ ] You cleaned up the lab RG  

## LinkedIn

Post draft: [`../../daily-guides/day-03.md`](../../daily-guides/day-03.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-03-arm-basics
```

## Next

**Day 04** — DevOps principles & culture (CALMS / DORA).
