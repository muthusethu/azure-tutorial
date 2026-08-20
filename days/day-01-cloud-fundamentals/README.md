# Day 01 — Cloud Computing & Azure Fundamentals

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Understand **IaaS vs PaaS vs SaaS**, **regions**, and **availability zones**. Set up a personal Azure budget alert and first resource group.

## High-level architecture (summary)

Open **[handout.pdf](./handout.pdf)** for diagrams. Short version:

| Concept | Meaning | Metaphor |
|---------|---------|----------|
| **IaaS** | You manage OS + app | Rent the whole kitchen |
| **PaaS** | You manage app; platform managed | Shared kitchen with a manager |
| **SaaS** | You configure/use the product | Order takeout |
| **Region** | Geography / set of datacenters | City |
| **Availability Zone** | Separate datacenter in a region | Different building, same city |

**One-liner:** Region = city · Zone = building · IaaS/PaaS/SaaS = who holds the spatula.

## Learn

- [Azure regions overview](https://learn.microsoft.com/azure/reliability/regions-overview)
- Shared responsibility across cloud service models

## Step-by-step lab

1. Sign in to [Azure Portal](https://portal.azure.com) with a **personal** account (not work SSO).
2. **Subscriptions** → note name and ID.
3. **Cost Management** → create a budget alert (e.g. Rs 500 or $20).
4. Create resource group `rg-day01-lab` in **Central India** (or nearest region).
5. Optional — Cloud Shell / Azure CLI:

```bash
az account show --output table
az group create --name rg-day01-lab --location centralindia
az group list --output table
```

6. Browse a free-tier create blade if you want, but do not deploy costly resources yet.

## Done when

- [ ] You can explain IaaS / PaaS / SaaS with one example each  
- [ ] You can explain Region vs Availability Zone  
- [ ] Budget alert exists  
- [ ] `rg-day01-lab` exists (or you know how to create it)

## LinkedIn

Use the post draft in [`../../daily-guides/day-01.md`](../../daily-guides/day-01.md) and attach **[handout.pdf](./handout.pdf)** as a LinkedIn document.

```
Handout: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-01-cloud-fundamentals
```

Hashtags: `#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic`

## Next

**Day 02** — Azure Portal vs CLI vs PowerShell.
