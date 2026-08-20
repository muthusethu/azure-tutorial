# Day 53 - Build & Push Images in Pipelines

| | |
|---|---|
| **Date** | 12 Oct 2026 |
| **Phase** | 6 - Containers & Kubernetes |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Docker tasks, multi-stage builds, scanning intro

## Hands-on lab (20-30 min)

1. Pipeline builds image and pushes to ACR
2. Use service connection

## Commands / code

```bash
- task: Docker@2
  inputs:
    containerRegistry: acr-connection
    repository: myapp
    command: buildAndPush
    Dockerfile: **/Dockerfile
    tags: |
      $(Build.BuildId)
      latest
```

## LinkedIn post (copy-paste)

```
Day 53 of #100DaysOfAzureDevOps

If humans push images by hand, humans will push the wrong tag on a Friday

Today's topic: **Build & Push Images in Pipelines**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Azure Container Instances.

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

**Azure Container Instances**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
