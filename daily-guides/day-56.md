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
AKS is a gym membership for orchestration — easy to start, painful if you forget to cancel.

Day 56 of #100DaysOfAzureDevOps. AKS setup.

az aks create with one node is still a control plane, a node VM, and a billing relationship. I have seen "just a lab cluster" survive a quarter because destroy was nobody's job. Cost warning is not flavor text. AKS is not a daily-delete toy.

Optional: smallest AKS, or skip to Azure Container Apps as a path. If I create it, I schedule destroy the same weekend. kubenet vs CNI is a survey, not a thesis. Node pools exist. One node is enough to feel kubectl against Azure.

What I keep seeing

1. Create is the easy button
• az aks create -g rg-day56 -n aks-lab --node-count 1 --generate-ssh-keys
• The hard button is remembering it exists on day 59

2. Network plugin is a fork in the road
• kubenet vs Azure CNI: IP usage, network policy, complexity
• Survey today; do not rebuild the cluster three times to feel thorough

3. Skip is a valid engineering choice
• Container Apps / ACI if cost bites
• Skipping AKS is cheaper than a forgotten node

4. Destroy is scheduled, not hoped
• Calendar: this weekend
• If I cannot name the destroy date, I should not create the cluster

What I am doing in today's lab

I am either creating the smallest AKS and putting destroy on the calendar the same weekend, or skipping to a Container Apps mental path and writing why. I am not leaving a one-node cluster "for later phases" without a date. Later phases can recreate.

Gym memberships you forget still bill. Orchestrate on purpose, cancel on a date.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-56-aks-setup

Tomorrow: Deploy to AKS via pipelines — manifests, not sticky-note kubectl.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 56 — AKS Setup` (max 58 chars)
3. Paste the text above (press **Enter** between sections so line breaks stay)

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

**Deploy to AKS via pipelines**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
