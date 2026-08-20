# Day 54 - Azure Container Instances (ACI)

| | |
|---|---|
| **Date** | 13 Oct 2026 |
| **Phase** | 6 - Containers & Kubernetes |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Serverless containers, quick deploys

## Hands-on lab (20-30 min)

1. Run your image in ACI once
2. Delete after test - ACI can surprise-bill

## Commands / code

```bash
az container create -g rg-day54 -n hello-aci \
  --image <acr>.azurecr.io/myapp:latest --registry-login-server <acr>.azurecr.io \
  --registry-username <user> --registry-password <pass> --dns-name-label <unique> --ports 80
```

## LinkedIn post (copy-paste)

```
Day 54 of #100DaysOfAzureDevOps

ACI is container fast-food - no cluster gym membership required

Today's topic: **Azure Container Instances (ACI)**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Kubernetes fundamentals.

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

**Kubernetes fundamentals**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
