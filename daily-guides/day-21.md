# Day 21 - Intro to Azure Pipelines

| | |
|---|---|
| **Date** | 10 Sep 2026 |
| **Phase** | 3 - Continuous Integration |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Agents, pools, parallel jobs
- YAML vs Classic editor
- https://learn.microsoft.com/azure/devops/pipelines/get-started/what-is-azure-pipelines

## Hands-on lab (20-30 min)

1. Create empty pipeline YAML that only runs `echo Hello`
2. Note Microsoft-hosted agent image `ubuntu-latest`
3. Disable Classic if you want YAML-only discipline

## Commands / code

```bash
# azure-pipelines.yml
trigger:
  - main
pool:
  vmImage: ubuntu-latest
steps:
  - script: echo Hello from Day 21
    displayName: Hello
```

## LinkedIn post (copy-paste)

```
Day 21 of #100DaysOfAzureDevOps

Pipelines are robots that run your build so you can stop being the robot

Today's topic: **Intro to Azure Pipelines**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Microsoft-hosted vs self-hosted agents.

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

**Microsoft-hosted vs self-hosted agents**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
