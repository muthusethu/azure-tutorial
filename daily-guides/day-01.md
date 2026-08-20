# Day 1 — Cloud Computing & Azure Fundamentals

| | |
|---|---|
| **Date** | 21 Aug 2026 |
| **Phase** | 1 — Azure & DevOps Foundations |
| **Time box** | 60–90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Understand IaaS vs PaaS vs SaaS, regions, and availability zones. Confirm your personal Azure subscription works. Publish Day 1 LinkedIn post.

## Learn (20–30 min)

- IaaS vs PaaS vs SaaS — who owns the OS, platform, and app
- Azure global infrastructure: geographies, regions, paired regions
- Availability Zones vs Availability Sets (high-level)
- Skim: [Azure regions overview](https://learn.microsoft.com/azure/reliability/regions-overview)

## Hands-on lab (20–30 min)

1. Confirm a **personal** Microsoft account (not work SSO).
2. Open [Azure Portal](https://portal.azure.com) → **Subscriptions** → note subscription name + ID.
3. Create a **Cost Management** budget alert (e.g. Rs 500 or $20).
4. Create resource group `rg-day01-lab` in **Central India** (or your nearest region).
5. Browse a free-tier create blade (App Service / Storage) but **do not deploy** yet.
6. Optional: open Cloud Shell and run the commands below.

## Commands / code

```bash
# Optional Cloud Shell / local Azure CLI
az account show --output table
az group create --name rg-day01-lab --location centralindia
az group list --output table
```

## LinkedIn post (copy-paste)

```
Day 1 of #100DaysOfAzureDevOps

Imagine your app is a restaurant.

IaaS is renting the whole kitchen.
You buy the stove, hire the chef, clean the grease trap, and still get yelled at when the soup is cold.
(Azure VMs. Maximum control. Maximum "why is this on fire.")

PaaS is a shared kitchen with a manager.
You cook. They fix the oven, pay the electricity, and pretend the dishwasher never breaks.
(App Service, Functions, Azure SQL. You own the recipe, not the building.)

SaaS is ordering takeout.
You open the app, tap "biryani," and complain about delivery time.
(Microsoft 365, GitHub. You configure. You do not build the kitchen.)

Now the map part that people skip:

A region is the city your restaurant is in.
Central India is not East US. Different customers. Different laws. Different "why is this so slow."

An availability zone is a different building in the same city, with its own power and network.
If Building A floods, Building B still serves lunch.
That is zone redundancy — not "pray and redeploy."

One-liner for Day 1:

Region = which city.
Zone = which building.
IaaS / PaaS / SaaS = who is holding the spatula when dinner goes wrong.

Tomorrow: Portal vs CLI vs PowerShell —
the three ways to order from Azure, and why clicking buttons alone will not save you.

(Document attached: Day 1 architecture + step-by-step lab PDF)

Lab notes + PDF also here:
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-01-cloud-fundamentals

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### Attach with the post (PDF handout)

Attach this document on LinkedIn (document / PDF upload):

- [`../days/day-01-cloud-fundamentals/handout.pdf`](../days/day-01-cloud-fundamentals/handout.pdf)

It includes:
1. High-level architecture (IaaS/PaaS/SaaS shared responsibility)
2. Region vs Availability Zone diagram
3. Step-by-step lab checklist
4. Optional CLI commands

**How to post on LinkedIn:** Start a post → click the **document** icon (not only photo) → upload `day-01-handout.pdf` → paste the post text above → title the document e.g. `Day 1 — Azure Fundamentals (Architecture + Lab)`.

### Posting tips

- Publish from your **personal** account (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5–10 real comments on other Azure/DevOps posts.

## Done checklist

- [ ] Learned IaaS/PaaS/SaaS + regions/zones
- [ ] Personal Azure subscription confirmed
- [ ] Budget alert created
- [ ] Resource group `rg-day01-lab` created (optional keep or delete)
- [ ] LinkedIn Day 1 published **with PDF handout attached**
- [ ] Engaged with 5–10 community comments

## Tomorrow

**Day 2 — Azure Portal, CLI & PowerShell Basics** → open [`day-02.md`](./day-02.md)

---

*Personal learning guide — views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
