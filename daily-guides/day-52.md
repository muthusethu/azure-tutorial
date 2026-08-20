# Day 52 - Azure Container Registry (ACR)

| | |
|---|---|
| **Date** | 11 Oct 2026 |
| **Phase** | 6 - Containers & Kubernetes |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Registries, tags, ACR Tasks

## Hands-on lab (20-30 min)

1. Create Basic ACR
2. docker tag + push
3. Delete images you do not need

## Commands / code

```bash
az acr create -g rg-day52 -n <uniqueacr> --sku Basic
az acr login -n <uniqueacr>
docker tag myapp:latest <uniqueacr>.azurecr.io/myapp:day52
docker push <uniqueacr>.azurecr.io/myapp:day52
```

## LinkedIn post (copy-paste)

```
Day 52 of #100DaysOfAzureDevOps

ACR is a private closet for images - public Docker Hub is the thrift store

Today's topic: **Azure Container Registry (ACR)**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Build & push in pipelines.

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

**Build & push in pipelines**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
