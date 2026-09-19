# Day 32 — Deploying to Azure App Service

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 4 - Continuous Delivery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

PaaS comfort food: Microsoft.Web/serverfarms + sites, zip deploy, then delete the kitchen if it costs

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Resource | Type / SKU | Pipeline hook |
| --- | --- | --- |
| Plan | Microsoft.Web/serverfarms  sku F1 (Free) | Always-on off; unloads. Fine for hello |
| Web app | Microsoft.Web/sites  kind app | appName in AzureWebApp@1 |
| Bits | zip / folder from artifact drop | package: $(Pipeline.Workspace)/**/*.zip |
| Identity | ARM service connection (azureSubscription) | Robot badge. Not Owner on the subscription |
| Runtime | linuxFxVersion or windows stack | Must match what CI published (dotnet/node/python) |

## Step-by-step lab

1. az login on the personal account. az group create -n rg-day32-lab -l centralindia (or your nearest region).
2. Create a Free F1 Linux plan + webapp with a globally unique name (starter CLI). Do not use a work subscription.
3. Project Settings → Service connections → Azure Resource Manager → scoped to rg-day32-lab (or the subscription if you must). Name it azure-100-sc.
4. Wire AzureWebApp@1 to azure-100-sc, appName, and the drop zip from CI. Run once. Hit https://<app>.azurewebsites.net.
5. If the site is still the default page, the glob missed. List files on the agent; fix package; rerun. Do not rebuild in the deploy job.
6. Cost-sensitive: az group delete -n rg-day32-lab --yes --no-wait. Slots (Day 34) need Standard — recreate then, not on F1.

## Done when

- [ ] Personal RG + F1 webapp deployed from the pipeline zip
- [ ] Service connection is not a story about subscription Owner
- [ ] No rebuild in the deploy job
- [ ] RG deleted or a written reason to keep it until Day 34

## LinkedIn

Post draft: [`../../daily-guides/day-32.md`](../../daily-guides/day-32.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-32-deploying-to-azure-app-service
```

## Next

**Day 33** — Deploy to Azure Functions — Consumption vs Premium, AzureFunctionApp@2, still a zip from CI.
