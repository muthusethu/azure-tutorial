# Day 44 - Bicep Fundamentals

| | |
|---|---|
| **Date** | 03 Oct 2026 |
| **Phase** | 5 - Infrastructure as Code |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Why Bicep over ARM JSON
- Resource declarations

## Hands-on lab (20-30 min)

1. If Bicep track: `az bicep install` and deploy storage
2. If Terraform track: read Bicep sample only (30 min)

## Commands / code

```bash
// main.bicep
param location string = resourceGroup().location
resource stg 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: 'st${uniqueString(resourceGroup().id)}'
  location: location
  sku: { name: 'Standard_LRS' }
  kind: 'StorageV2'
}
```

## LinkedIn post (copy-paste)

```
Day 44 of #100DaysOfAzureDevOps

Bicep is ARM with the JSON horror filed down - same control plane, less eye strain

Today's topic: **Bicep Fundamentals**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Bicep modules.

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

**Bicep modules**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
