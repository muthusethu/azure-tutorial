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
Remote state with locking stops two applies from playing tug-of-war with production.

Day 48 of #100DaysOfAzureDevOps. Terraform modules and remote state.

Local state on a laptop is a lab. Two people applying with two local states is a fork of reality. Remote state in Azure Storage, with locking, is how grown-ups share memory. I have seen two applies in the same hour create duplicate resources and a third that could not destroy either. Tug-of-war.

Modules are the other half: reuse without copy-paste. Backend azurerm: resource group, storage account, container, key. Note the cost of the state account. Destroy carefully — destroying the state account before the workload is how you orphan the world.

What I keep seeing

1. Backend is the shared brain
• backend "azurerm" with rg, account, container, key = lab.tfstate
• Migrate with terraform init when you add the backend — do not copy files like a raccoon

2. Locking is the point
• Blob lease lock stops concurrent applies
• If someone force-unlocks because they are impatient, they just volunteered to be the incident

3. Modules beat copy-paste
• A storage module with inputs beats three nearly identical main.tf files
• Module versioning is later; today is the split

4. Destroy order matters
• Workload first, state account last, and only if I am done with the lab
• Deleting state storage while resources exist is amnesia on purpose

What I am doing in today's lab

I am creating storage for state (noting it costs), configuring the azurerm backend, migrating state, applying through the backend once, then destroying the workload carefully. I am not force-unlocking anything. If a lock exists, I wait or I investigate.

Share memory. Lock the door. Two applies at once is not speed. It is a race with prod as the prize.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-48-terraform-modules-remote-state

Tomorrow: IaC in pipelines — plan in CI, apply behind an approval.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 48 — Terraform Modules & State` (max 58 chars)
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

**IaC in pipelines**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
