# Day 23 - YAML Pipeline Basics

| | |
|---|---|
| **Date** | 12 Sep 2026 |
| **Phase** | 3 - Continuous Integration |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Triggers, stages, jobs, steps, syntax
- https://learn.microsoft.com/azure/devops/pipelines/yaml-schema

## Hands-on lab (20-30 min)

1. Expand hello pipeline into stages Build -> Test (Test can be echo)
2. Add a PR trigger
3. Read pipeline run logs end-to-end

## Commands / code

```bash
trigger:
  branches:
    include: [ main ]
pr:
  branches:
    include: [ main ]
stages:
- stage: Build
  jobs:
  - job: BuildJob
    pool: { vmImage: ubuntu-latest }
    steps:
    - script: echo Building...
- stage: Test
  dependsOn: Build
  jobs:
  - job: TestJob
    pool: { vmImage: ubuntu-latest }
    steps:
    - script: echo Testing...
```

## LinkedIn post (copy-paste)

```
Day 23 of #100DaysOfAzureDevOps

YAML pipelines are Lego instructions written by someone who enjoys whitespace arguments

Today's topic: **YAML Pipeline Basics**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: CI pipeline for a .NET app.

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

**CI pipeline for a .NET app**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
