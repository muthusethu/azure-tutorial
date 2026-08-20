# Day 3 - Azure Resource Manager (ARM) Basics

| | |
|---|---|
| **Date** | 23 Aug 2026 |
| **Phase** | 1 - Azure & DevOps Foundations |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Resource providers, management groups, subscriptions, RGs
- Tags for cost + ownership; resource locks (CanNotDelete)
- ARM is the control plane - every Portal click becomes an ARM call
- Docs: https://learn.microsoft.com/azure/azure-resource-manager/management/overview

## Hands-on lab (20-30 min)

1. Create `rg-day03-lab` with tags: Project=100Days, Owner=personal, Env=lab
2. Add a CanNotDelete lock, try deleting (should fail), remove lock, delete RG
3. List resource providers: `az provider list --query [].namespace -o tsv | more`

## Commands / code

```bash
az group create -n rg-day03-lab -l centralindia \
  --tags Project=100Days Owner=personal Env=lab
az lock create --name cannot-delete --lock-type CanNotDelete \
  --resource-group rg-day03-lab
# Try: az group delete -n rg-day03-lab --yes   # should fail while locked
az lock delete --name cannot-delete --resource-group rg-day03-lab
az group delete -n rg-day03-lab --yes --no-wait
```

## LinkedIn post (copy-paste)

```
Day 3 of #100DaysOfAzureDevOps

Tags are sticky notes for Finance; locks are duct tape so nobody deletes prod by accident

Today's topic: **Azure Resource Manager (ARM) Basics**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: DevOps principles & culture.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5-10 real comments on other Azure/DevOps posts.

## Done checklist

- [ ] Learned the topic (docs or short video)
- [ ] Completed the lab steps
- [ ] Ran / saved the commands or code
- [ ] Published LinkedIn post
- [ ] Engaged with 5-10 community comments
- [ ] Deleted spare Azure resources if any (cost control)

## Tomorrow

**DevOps principles & culture**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
