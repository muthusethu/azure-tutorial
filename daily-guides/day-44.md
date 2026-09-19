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
Bicep is ARM with the JSON horror filed down — same control plane, less eye strain.

Day 44 of #100DaysOfAzureDevOps. Bicep fundamentals.

Bicep is not a different Azure. It is ARM with a language that does not make you count braces for sport. resource declarations, params, uniqueString for names that must be globally unique. After years of JSON templates, the first Bicep file feels like someone turned the lights on.

If I chose Terraform as primary, I still read a Bicep sample for thirty minutes. Azure-native teams will send me .bicep files. Illiteracy is not a brand.

What I keep seeing

1. Same resource types, calmer syntax
• Microsoft.Storage/storageAccounts@2023-01-01
• sku and kind in a block instead of a nest of quotes

2. uniqueString is how you stop name collisions
• name: 'st${uniqueString(resourceGroup().id)}'
• Hardcoded stmyname123 is a landfill ticket from Day 43

3. location should be a param
• param location string = resourceGroup().location
• A second region should not require a fork of the file

4. Install the compiler
• az bicep install
• Then deploy storage if this is my track; otherwise read the sample and still type the resource block once

What I am doing in today's lab

If Bicep is my track: az bicep install and deploy a storage account from main.bicep. If Terraform is my track: thirty minutes on the sample, still write the resource block so my hands know it. Either way I delete the RG when the proof is done.

Same control plane. Less eye strain. File down the horror, do not pretend ARM went away.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-44-bicep-fundamentals

Tomorrow: Bicep modules and what-if — dress rehearsal before prod.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 44 — Bicep Fundamentals` (max 58 chars)
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

**Bicep modules**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
