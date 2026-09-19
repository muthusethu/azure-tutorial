# Day 85 - Hybrid & Multi-cloud CI/CD

| | |
|---|---|
| **Date** | 13 Nov 2026 |
| **Phase** | 9 - Advanced & Enterprise |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Patterns to AWS/GCP from Azure Pipelines - survey only

## Hands-on lab (20-30 min)

1. Write risks: secrets, identity, network
2. Do not actually deploy to AWS unless personal account ready

## Commands / code

```bash
# Pattern: build once in ADO -> deploy with cloud-specific tasks
# Prefer one cloud deep over two clouds shallow in this 100 days
```

## LinkedIn post (copy-paste)

```
Multi-cloud is insurance and complexity — buy it for a reason, not a slide.

Day 85 of #100DaysOfAzureDevOps. Hybrid and multi-cloud CI/CD.

Azure Pipelines can deploy to other clouds. That sentence is true and expensive. Identity, secrets, network, three consoles, three bills. I have sat through slides titled "multi-cloud strategy" that were really "we might need AWS someday." Insurance. Complexity. Buy it when a constraint is real.

Survey only. Write risks: secrets, identity, network. Do not actually deploy to AWS unless a personal account is ready and I want that bill. Prefer one cloud deep in these 100 days. Pattern: build once in Azure DevOps, deploy with cloud-specific tasks if you must.

Patterns I keep seeing

1. Build once still applies
• The artifact or image is the passport
• Rebuilding per cloud is the ghost from Day 39 with extra stamps

2. Identity does not unify itself
• Entra vs IAM vs another IdP
• A secret copied into two clouds is two postcards

3. Network is the boring blocker
• Hybrid: self-hosted agents, VPN, private endpoints
• A hosted agent cannot see your on-prem by wishing

4. Slides are not constraints
• A reason: data residency, an existing estate, a product on two clouds
• Not a reason: the architecture diagram looks worldly

What I am doing in today's lab

I am writing a one-pager of risks (secrets, identity, network) and the rule for this series: one cloud deep. I am not opening AWS "just to try" unless I already have a personal account and a destroy plan. Survey, not a second gym membership.

Insurance is priced. If you cannot name the risk you are buying, it is a slide.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-85-hybrid-multi-cloud-ci-cd

Tomorrow: Disaster recovery and backup — RPO, RTO, restore or it is fiction.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 85 — Hybrid & Multi-cloud CI/CD` (max 58 chars)
3. Paste the text above (press **Enter** between sections so line breaks stay)

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5-10 real comments on other Azure/DevOps posts.

## Reminder — 2nd LinkedIn post (production track)

**Today you publish TWO separate LinkedIn posts.** The daily lesson above is post 1 only.

| | Post 1 — #100DaysOfAzureDevOps | Post 2 — #ProductionGradeAzure |
|---|-------------------------------|----------------------------------|
| **When** | ~10:00 IST | ~17:00–19:00 IST (after some engagement on post 1) |
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 28 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 28 of 33 (rewrite with your real experience)
- [ ] Record URLs in [`publish/production-grade/LINKS.md`](../publish/production-grade/LINKS.md)

Run: `python scripts/production_reminder.py`

## Done checklist

- [ ] Learned the topic (docs or short video)
- [ ] Completed the lab steps
- [ ] Ran / saved the commands or code
- [ ] Published LinkedIn post
- [ ] Engaged with 5-10 community comments
- [ ] Deleted spare Azure resources if any (cost control)

## Tomorrow

**DR & backup**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
