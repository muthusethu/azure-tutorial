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
Functions are micro-managers that only wake up when work arrives — and still send you a bill for the nap.

Day 33 of #100DaysOfAzureDevOps. Deploying to Azure Functions.

Consumption plans feel like free until a timer fires more than you thought, or a runaway retry turns "serverless" into a line item. I have seen teams love Functions for the right reason (event-shaped work) and the wrong reason ("we do not want to think about hosts"). You still think about hosts. You just think about them as plans: Consumption vs Premium vs dedicated.

If quota is tight, a read-only lab is honest. Deploying a timer or HTTP sample on Consumption is the default. AzureFunctionApp@2 is the CD task. The package is still a zip you built in CI.

Patterns I keep seeing

1. Pick the plan for the sleep pattern
• Consumption: scale to zero, cold starts, pay per execution
• Premium: pre-warmed, VNet, a bill that does not nap as hard

2. HTTP and timer are different operational stories
• HTTP is a public or gateway-shaped surface
• Timer is a cron you will forget is running until Cost Management reminds you

3. CD is still a package
• AzureFunctionApp@2, appType functionApp, package glob on the zip
• Do not "publish from Visual Studio" as the source of truth if the pipeline exists

4. Quota and cost are lab design
• Create on Consumption or read the blade if the subscription cannot
• Delete the Function App when the proof is done

What I am doing in today's lab

I am creating a Function App on Consumption (or reading the experience if quota is tight), deploying a timer or HTTP sample from the pipeline, triggering it once, and checking that I know how to stop or delete it so the nap does not keep billing.

Serverless sleeps. Billing does not always. Know which plan you bought.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-33-deploying-to-azure-functions

Tomorrow: Deployment slots and swap — staging as a dressing room.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 33 — Deploying to Azure Functions` (max 58 chars)
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

**Deployment slots**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
