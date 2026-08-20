# Day 31 - Release Pipelines Overview

| | |
|---|---|
| **Date** | 20 Sep 2026 |
| **Phase** | 4 - Continuous Delivery |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Classic release vs multi-stage YAML CD

## Hands-on lab (20-30 min)

1. Prefer YAML CD for labs
2. Create environment `dev` in Pipelines -> Environments

## Commands / code

```bash
stages:
- stage: DeployDev
  jobs:
  - deployment: Deploy
    environment: dev
    strategy:
      runOnce:
        deploy:
          steps:
          - script: echo Deploying to dev
```

## LinkedIn post (copy-paste)

```
Day 31 of #100DaysOfAzureDevOps

Classic releases are the old mall; YAML CD is the street you actually live on now

Today's topic: **Release Pipelines Overview**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Deploy to App Service.

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

**Deploy to App Service**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
