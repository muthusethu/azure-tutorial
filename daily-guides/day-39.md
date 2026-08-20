# Day 39 - Multi-environment Pipeline

| | |
|---|---|
| **Date** | 28 Sep 2026 |
| **Phase** | 4 - Continuous Delivery |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Dev -> QA -> Staging -> Prod with gates

## Hands-on lab (20-30 min)

1. YAML with 3 stages; approvals on last
2. Promote same artifact, do not rebuild

## Commands / code

```bash
stages:
- stage: Dev
  jobs: [ ... deploy ... ]
- stage: Staging
  dependsOn: Dev
  jobs: [ ... ]
- stage: Prod
  dependsOn: Staging
  jobs:
  - deployment: ProdDeploy
    environment: prod
```

## LinkedIn post (copy-paste)

```
Day 39 of #100DaysOfAzureDevOps

Promote the artifact, not the vibes - rebuilds between envs invent 'works in staging' ghosts

Today's topic: **Multi-environment Pipeline**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Phase 4 mini project.

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

**Phase 4 mini project**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
