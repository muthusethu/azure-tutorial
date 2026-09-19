# Day 33 — Deploying to Azure Functions

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 4 - Continuous Delivery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Event-shaped work, a plan that can sleep, and a different CD task — still not a Visual Studio publish as source of truth

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Dimension | Function App | App Service web app |
| --- | --- | --- |
| Resource | Microsoft.Web/sites  kind functionapp | kind app (Day 32) |
| Unit of work | Trigger: httptrigger, timerTrigger, queue | HTTP site / always a web process |
| Plan | Consumption (Y1), Flex, Premium EP1, or dedicated | F1/B1/S1… you picked a SKU |
| Scale to zero | Consumption yes (cold start) | F1 unloads; paid SKUs stay warmer |
| CD task | AzureFunctionApp@2  appType: functionApp | AzureWebApp@1 |
| Package | Zip of function bits from CI drop | Zip of the web app from the same drop idea |

## Step-by-step lab

1. az group create -n rg-day33-lab -l centralindia. Create a storage account (Functions requires one) + a Consumption Function App, or stop at the portal error and write the quota note.
2. If you create: use a tiny HTTP sample (func init / existing hello). Package a zip in CI — do not treat Visual Studio publish as the source of truth.
3. Add AzureFunctionApp@2 with azureSubscription: azure-100-sc, appType: functionApp, appName, package glob on the zip.
4. Trigger the HTTP function once (browser or curl). Confirm 200/output. If timer sample: fire once, then disable it.
5. Project Settings → confirm the service connection scope. Do not leave a subscription-Owner robot from Day 32 unused on this RG.
6. az functionapp delete or az group delete -n rg-day33-lab --yes --no-wait after the proof. Naps still meter.

## Done when

- [ ] Can explain Consumption vs Premium without saying 'serverless is free'
- [ ] CD uses AzureFunctionApp@2 on a CI zip (or a written quota skip)
- [ ] Timer/HTTP not left running overnight
- [ ] RG deleted or budget-watched

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-33-deploying-to-azure-functions
```

## Next

**Day 34** — Deployment slots — staging as a dressing room, warm-up, swap. F1 will refuse; that is data.
