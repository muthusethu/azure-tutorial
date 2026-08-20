# Day 35 - Blue-Green Deployments

| | |
|---|---|
| **Date** | 24 Sep 2026 |
| **Phase** | 4 - Continuous Delivery |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Concept + App Service implementation; AKS later
- Rollback story

## Hands-on lab (20-30 min)

1. Map blue-green onto slots: blue=prod, green=staging
2. Write rollback steps in `/docs/rollback.md`

## Commands / code

```bash
# docs/rollback.md
# 1. Swap back staging/production
# 2. Verify health endpoint
# 3. Keep previous artifact for 7 days
```

## LinkedIn post (copy-paste)

```
Day 35 of #100DaysOfAzureDevOps

Blue-green means two worlds; only one takes traffic - rollback is a light switch, not an archaeology dig

Today's topic: **Blue-Green Deployments**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Canary releases.

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

**Canary releases**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
