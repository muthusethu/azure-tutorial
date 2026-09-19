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
Classic releases are the old mall; YAML CD is the street you actually live on now.

Day 31 of #100DaysOfAzureDevOps. Release pipelines overview.

Classic Release pipelines still work. They also hide the workflow in a UI that does not review well and does not travel with the repo. After a decade of delivery, I can still click a Classic stage in my sleep. I do not want my labs, or a future team's source of truth, to live in that mall.

YAML CD is a deployment job, an environment, and a strategy. runOnce. deploy. The environment named dev is not a folder on a laptop. It is an Azure DevOps object you can hang approvals and checks on later this phase.

Patterns I keep seeing

1. Prefer YAML CD for new work
• The pipeline file lives next to the app
• Classic is literacy for brownfield, not the default for a 100-day lab

2. Environments are first-class
• Pipelines → Environments → create dev
• A deployment job targets environment: dev so history is not a buried log

3. strategy.runOnce.deploy is the smallest CD
• steps under deploy run on the agent against that environment
• echo Deploying to dev is a legal first proof — the wiring matters more than the bits today

4. CD consumes CI, it does not impersonate it
• Download the artifact from Day 24–30
• Rebuilding in the release job is how staging and production diverge

What I am doing in today's lab

I am leaving Classic alone for these labs, creating environment dev in Pipelines → Environments, and adding a DeployDev stage with a deployment job that echoes a deploy. Tomorrow the echo becomes App Service. Today the environment object has to exist.

Live on the street that diffs. Visit the mall only when a legacy release still pays the rent.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-31-release-pipelines-overview

Tomorrow: Deploy to Azure App Service — zip deploy from the pipeline.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 31 — Release Pipelines Overview` (max 58 chars)
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
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 10 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 10 of 33 (rewrite with your real experience)
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

**Deploy to App Service**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
