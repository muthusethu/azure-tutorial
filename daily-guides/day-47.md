# Day 47 - Terraform with Azure (azurerm)

| | |
|---|---|
| **Date** | 06 Oct 2026 |
| **Phase** | 5 - Infrastructure as Code |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Provider auth, common resources

## Hands-on lab (20-30 min)

1. Auth via Azure CLI (`az login`)
2. Create RG + storage with azurerm

## Commands / code

```bash
provider "azurerm" {
  features {}
}
resource "azurerm_resource_group" "lab" {
  name     = "rg-day47-tf"
  location = "Central India"
}
```

## LinkedIn post (copy-paste)

```
Day 47 of #100DaysOfAzureDevOps

azurerm is Terraform's Azure dialect - same ideas, different accent

Today's topic: **Terraform with Azure (azurerm)**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Terraform modules & remote state.

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

**Terraform modules & remote state**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
