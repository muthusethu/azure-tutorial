# Day 42 — ARM Templates Basics

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 5 - Infrastructure as Code |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Every Portal click is still an ARM call. JSON is broccoli: nutritious, rarely anyone's favorite

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Key | Role | Lab value |
| --- | --- | --- |
| $schema | JSON schema for validation | 2019-04-01/deploymentTemplate.json# |
| contentVersion | Your version, not apiVersion | 10.0.0.1 |
| parameters / variables | Dials and locals (deep dive Day 43) | Can be empty today |
| resources[] | type + apiVersion + name + properties | Microsoft.Storage/storageAccounts@2023-01-01 |
| outputs | Handshake to the next stack | Optional today; required tomorrow |
| mode | Incremental (default) vs Complete | Complete can delete extras. Do not use Complete on a busy RG |

## Step-by-step lab

1. az group create -n rg-day42-lab -l centralindia on the personal subscription.
2. Save infra/storage.json (starter). Confirm type Microsoft.Storage/storageAccounts and a real apiVersion.
3. az deployment group create -g rg-day42-lab -n stor -f infra/storage.json. Wait for Succeeded.
4. az storage account list -g rg-day42-lab -o table. Note the unique name ARM computed.
5. Open the deployment in Portal → RG → Deployments → stor. That history is ARM's receipt (no Terraform state here).
6. az group delete -n rg-day42-lab --yes --no-wait. Broccoli does not need to live in Cost Management.

## Done when

- [ ] Can name $schema, contentVersion, resources, apiVersion
- [ ] One successful az deployment group create
- [ ] Know Incremental vs Complete well enough to fear Complete
- [ ] rg-day42-lab deleted

## LinkedIn

Post draft: [`../../daily-guides/day-42.md`](../../daily-guides/day-42.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-42-arm-templates-basics
```

## Next

**Day 43** — ARM parameters and outputs — dials in a .parameters.json, handshake via outputs, not hardcoded landfill names.
