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
azurerm is Terraform's Azure dialect — same ideas, different accent.

Day 47 of #100DaysOfAzureDevOps. Terraform with Azure (azurerm).

The azurerm provider is how Terraform speaks ARM without you writing ARM. provider "azurerm" { features {} }. Auth today is Azure CLI: az login on a personal account, personal subscription. I have seen service principals with Owner at subscription scope used "just for Terraform." That is not a dialect. That is a master key in a language file.

Lab shape: resource group plus storage. Central India or the region I actually use. Names that can collide will. Destroy still exists.

Patterns I keep seeing

1. Provider block is the accent
• features {} is required even when empty
• Pin provider versions in real work; floating latest is a surprise engine

2. Auth via CLI for labs
• az login, then Terraform uses that context
• Tomorrow's professional version is a scoped identity, not my user forever

3. Resources map 1:1 with Azure types
• azurerm_resource_group, then a storage account in that group
• If the plan creates a second RG, my reference is wrong — I read the plan

4. Region is a variable waiting to happen
• location = "Central India" is fine in a lab
• Hardcoding it in six modules is how you migrate with a prayer

What I am doing in today's lab

I am authenticating with az login, writing a tiny azurerm config that creates rg-day47-tf and a storage account, applying, verifying in Portal or CLI, then destroying. No subscription-Owner robot. Personal user, personal sub, short life.

Same ideas as ARM/Bicep. Different accent. Do not give the dialect a master key to practice grammar.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-47-terraform-with-azure-azurerm

Tomorrow: Terraform modules and remote state — locking so two applies cannot tug-of-war.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 47 — Terraform with Azure` (max 58 chars)
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

**Terraform modules & remote state**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
