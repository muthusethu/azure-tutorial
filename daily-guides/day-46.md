# Day 46 - Terraform Basics

| | |
|---|---|
| **Date** | 05 Oct 2026 |
| **Phase** | 5 - Infrastructure as Code |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Providers, state, plan/apply/destroy

## Hands-on lab (20-30 min)

1. Install Terraform
2. Local state lab: RG only
3. Always `destroy` at end of night

## Commands / code

```bash
terraform init
terraform plan
terraform apply -auto-approve
terraform destroy -auto-approve
```

## LinkedIn post (copy-paste)

```
Terraform state is the memory of your infra — lose it and you are arguing with ghosts.

Day 46 of #100DaysOfAzureDevOps. Terraform basics.

init, plan, apply, destroy. The verbs are simple. The state file is the plot. Terraform's memory of what it created lives in state. Lose it, and the next apply will try to create things that already exist, or will refuse to destroy things you can still see in the Portal. I have watched grown teams argue with ghosts for a day because someone deleted terraform.tfstate to "clean up."

Today is local state on purpose: a resource group only, then destroy at the end of the night. Remote state is Day 48. Skipping destroy is how a lab becomes a subscription.

What I keep seeing

1. The four verbs are a ritual
• terraform init — providers
• plan — the diff
• apply — change the world
• destroy — the adult ending

2. State is not a cache
• It is the mapping from resource addresses to Azure IDs
• Delete it and Terraform amnesia begins

3. Plan is the dress rehearsal (again)
• Never apply a mental diff
• If plan surprises you, you do not apply until it does not

4. Destroy tonight
• Local state lab: RG only
• Always destroy at end of night — leftover RGs are how Cost Management becomes a personality test

What I am doing in today's lab

I am installing Terraform, running init/plan/apply on a resource group with local state, confirming the RG in Azure, then terraform destroy -auto-approve. If destroy fails, I do not shrug and leave it. Ghosts start as leftovers.

Protect state like production data. Memory loss in Terraform is not a vibe. It is an outage you scheduled.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-46-terraform-basics

Tomorrow: Terraform with Azure (azurerm) — CLI auth, RG + storage.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 46 — Terraform Basics` (max 58 chars)
3. Paste the text above (press **Enter** between sections so line breaks stay)

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5-10 real comments on other Azure/DevOps posts.

## Reminder — 2nd LinkedIn post (production track)

**Today you publish TWO separate LinkedIn posts.** The daily lesson above is post 1 only.

| | Post 1 — #100DaysOfAzureDevOps | Post 2 — #ProductionGradeAzure |
|---|-------------------------------|----------------------------------|
| **When** | ~10:00 IST | ~17:00–19:00 IST (after some engagement on post 1) |
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 15 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 15 of 33 (rewrite with your real experience)
- [ ] Record URLs in [`publish/production-grade/LINKS.md`](../publish/production-grade/LINKS.md)

Run: `python scripts/production_reminder.py`

## Done checklist

- [ ] Learned the topic (docs or short video)
- [ ] Completed the lab steps
- [ ] Ran / saved the commands or code
- [ ] Published LinkedIn post
- [ ] Engaged with 5-10 community comments
- [ ] Deleted spare Azure resources if any (cost control)

## Tomorrow

**Terraform with Azure**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
