# Day 33 - Deploying to Azure Functions

| | |
|---|---|
| **Date** | 22 Sep 2026 |
| **Phase** | 4 - Continuous Delivery |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Consumption vs Premium
- Function app CD

## Hands-on lab (20-30 min)

1. Create Function App (Consumption) OR read-only lab if quota tight
2. Deploy a timer/http sample

## Commands / code

```bash
- task: AzureFunctionApp@2
  inputs:
    azureSubscription: <service-connection>
    appType: functionApp
    appName: <function-name>
    package: $(System.DefaultWorkingDirectory)/**/*.zip
```

## LinkedIn post (copy-paste)

```
Day 33 of #100DaysOfAzureDevOps

Functions are micro-managers that only wake up when work arrives - and still send you a bill for the nap

Today's topic: **Deploying to Azure Functions**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Deployment slots.

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

**Deployment slots**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
