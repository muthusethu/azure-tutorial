# Day 48 - Terraform Modules & Remote State

| | |
|---|---|
| **Date** | 07 Oct 2026 |
| **Phase** | 5 - Infrastructure as Code |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Modules, Azure Storage backend, locking

## Hands-on lab (20-30 min)

1. Create storage for state (note cost)
2. Configure backend; migrate state
3. Destroy carefully

## Commands / code

```bash
terraform {
  backend "azurerm" {
    resource_group_name  = "rg-tfstate"
    storage_account_name = "<unique>"
    container_name       = "tfstate"
    key                  = "lab.tfstate"
  }
}
```

## LinkedIn post (copy-paste)

```
Day 48 of #100DaysOfAzureDevOps

Remote state with locking stops two applies from playing tug-of-war with production

Today's topic: **Terraform Modules & Remote State**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: IaC in pipelines.

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

**IaC in pipelines**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
