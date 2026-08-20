# Day 32 - Deploying to Azure App Service

| | |
|---|---|
| **Date** | 21 Sep 2026 |
| **Phase** | 4 - Continuous Delivery |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Web App deploy, zip deploy, slots overview

## Hands-on lab (20-30 min)

1. Create free/F1 App Service plan + webapp in personal RG
2. Deploy hello app from pipeline
3. Delete RG tonight if cost-sensitive

## Commands / code

```bash
- task: AzureWebApp@1
  inputs:
    azureSubscription: <service-connection>
    appName: <webapp-name>
    package: $(Pipeline.Workspace)/drop/**/*.zip
```

## LinkedIn post (copy-paste)

```
Day 32 of #100DaysOfAzureDevOps

App Service is PaaS comfort food - less drama than VMs, still enough knobs to burn dinner

Today's topic: **Deploying to Azure App Service**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Deploy to Azure Functions.

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

**Deploy to Azure Functions**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
