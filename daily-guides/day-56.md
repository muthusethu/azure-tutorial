# Day 56 - AKS Setup

| | |
|---|---|
| **Date** | 15 Oct 2026 |
| **Phase** | 6 - Containers & Kubernetes |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Cluster, node pools, kubenet vs CNI

## Hands-on lab (20-30 min)

1. Optional: create smallest AKS OR skip to Azure Container Apps path
2. If created: schedule destroy same weekend

## Commands / code

```bash
# Cost warning: AKS is not a daily-delete toy
az aks create -g rg-day56 -n aks-lab --node-count 1 --generate-ssh-keys
```

## LinkedIn post (copy-paste)

```
Day 56 of #100DaysOfAzureDevOps

AKS is a gym membership for orchestration - easy to start, painful if you forget to cancel

Today's topic: **AKS Setup**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Deploy to AKS via pipelines.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no "DM me for freelance".
- After posting: leave 5-10 real comments on other Azure/DevOps posts.

## Done checklist

- [ ] Learned the topic (docs or short video)
- [ ] Completed the lab steps
- [ ] Ran / saved the commands or code
- [ ] Published LinkedIn post
- [ ] Engaged with 5-10 community comments
- [ ] Deleted spare Azure resources if any (cost control)

## Tomorrow

**Deploy to AKS via pipelines**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
