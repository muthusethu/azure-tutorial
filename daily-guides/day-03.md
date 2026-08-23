# Day 3 — Azure Resource Manager (ARM) Basics

| | |
|---|---|
| **Date** | 23 Aug 2026 |
| **Phase** | 1 — Azure & DevOps Foundations |
| **Time box** | 60–90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Understand ARM as Azure’s control plane. Practice **tags** and **resource locks**. Publish Day 3 on LinkedIn with the PDF handout.

## Learn (20–30 min)

- Resource providers, management groups, subscriptions, resource groups
- Tags for cost + ownership; locks (`CanNotDelete`, `ReadOnly`)
- Every Portal click and every `az` command becomes an ARM request
- Docs: [Azure Resource Manager overview](https://learn.microsoft.com/azure/azure-resource-manager/management/overview)

## Hands-on lab (20–30 min)

1. Create `rg-day03-lab` with tags: `Project=100Days`, `Owner=personal`, `Env=lab`
2. Add a `CanNotDelete` lock → try delete (should fail) → remove lock → delete RG
3. Optional: `az provider list --query [].namespace -o tsv | more`

## Commands / code

```bash
az group create -n rg-day03-lab -l centralindia \
  --tags Project=100Days Owner=personal Env=lab

az lock create --name cannot-delete --lock-type CanNotDelete \
  --resource-group rg-day03-lab

# This should FAIL while the lock exists:
# az group delete -n rg-day03-lab --yes

az lock delete --name cannot-delete --resource-group rg-day03-lab
az group delete -n rg-day03-lab --yes --no-wait
```

## LinkedIn post (copy-paste)

**Important:** After pasting into LinkedIn, press Enter between sections so line breaks stay visible.

```
Day 3 of #100DaysOfAzureDevOps

Yesterday we talked to Azure with Portal, CLI, and PowerShell.

Today: who is actually listening?

Azure Resource Manager (ARM).

Think of ARM as the restaurant’s head office.
You (Portal / CLI / PowerShell) place the order.
ARM checks the menu, the kitchen rules, and who is allowed to cook.
Then the resource providers do the real work.

A few words that stop sounding abstract once you break something:

• Management group → subscription → resource group → resource
  (folders inside folders, with bills at the subscription level)

• Resource providers
  The kitchens behind the names — Microsoft.Storage, Microsoft.Web, …

• Tags
  Sticky notes for Finance and future-you.
  Project=100Days beats “what is this RG from March?”

• Locks
  Duct tape on the delete button.
  CanNotDelete = “ask me again when you are awake.”

Lab today: tagged a resource group, locked it, tried to delete it
(failed on purpose), unlocked, cleaned up.

One-liner:

Portal/CLI/PowerShell = how you talk.
ARM = who enforces the rules.
Tags = sticky notes.
Locks = duct tape.

Tomorrow: DevOps principles & culture —
CALMS and DORA, without the buzzword fog.

(Document attached: Day 3 — ARM basics)

Lab notes + PDF:
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-03-arm-basics

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### Attach with the post (PDF handout)

- [`../days/day-03-arm-basics/handout.pdf`](../days/day-03-arm-basics/handout.pdf)

LinkedIn → **document** → upload PDF → title: `Day 3 — ARM Basics (Architecture + Lab)` → paste post → publish.

### Posting tips

- Personal account only; no employer name; no hiring CTAs.
- X is paused — LinkedIn + GitHub only for now.
- Leave 5–10 real comments on other Azure/DevOps posts.

## Done checklist

- [ ] Can explain ARM in one sentence
- [ ] Created tagged RG + CanNotDelete lock demo
- [ ] LinkedIn Day 3 published with PDF + line breaks intact
- [ ] Engaged with community comments
- [ ] Lab RG deleted

## Tomorrow

**Day 4 — DevOps principles & culture** → [`day-04.md`](./day-04.md)

---

*Personal learning guide — views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
