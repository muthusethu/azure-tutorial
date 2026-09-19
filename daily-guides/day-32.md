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
App Service is PaaS comfort food — less drama than VMs, still enough knobs to burn dinner.

Day 32 of #100DaysOfAzureDevOps. Deploying to Azure App Service.

I have spent years around VMs that needed patching, agents, and a load balancer that someone named after a pet. App Service removes a pile of that drama. It does not remove configuration, SKU choice, or the zip that is not the zip you thought you published.

Today is a Free/F1 plan, a webapp in a personal resource group, AzureWebApp@1, and a service connection that must not be over-privileged later. Cost-sensitive means the RG dies tonight. Comfort food still goes stale if you leave it on the counter.

What usually happens

1. Zip deploy is a contract
• package: $(Pipeline.Workspace)/drop/**/*.zip must match what CI published
• Wrong glob = a successful task that deployed nothing useful

2. Service connection is identity
• azureSubscription in AzureWebApp@1 is the robot's badge
• If that badge is Owner on the subscription, the lab is teaching the wrong lesson

3. SKU is a budget decision
• F1/free for a hello app
• Slots and some networking need a higher plan — do not discover that after the deploy is "done"

4. Delete is a skill
• Personal RG, personal subscription, delete tonight if cost-sensitive
• Orphan App Service plans are quiet invoices

What I am doing in today's lab

I am creating a free/F1 App Service plan and webapp in a personal RG, deploying a hello app from the pipeline with AzureWebApp@1, confirming the URL responds, and deleting the RG tonight if I do not need it for slots later this week.

PaaS is comfort. The knobs are still hot. Deploy the zip you published, then clean up the kitchen.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-32-deploying-to-azure-app-service

Tomorrow: Deploy to Azure Functions — Consumption vs Premium, timer or HTTP sample.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 32 — Deploying to Azure App Service` (max 58 chars)
3. Paste the text above (press **Enter** between sections so line breaks stay)

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

**Deploy to Azure Functions**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
