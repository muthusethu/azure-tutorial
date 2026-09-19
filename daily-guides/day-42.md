# Day 42 - ARM Templates Basics

| | |
|---|---|
| **Date** | 01 Oct 2026 |
| **Phase** | 5 - Infrastructure as Code |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Template structure; deploy via CLI
- Treat as literacy, not your main tool

## Hands-on lab (20-30 min)

1. Deploy a tiny Storage Account ARM template
2. Then delete RG

## Commands / code

```bash
az deployment group create -g rg-day42 -n stor -f infra/storage.json
```

## LinkedIn post (copy-paste)

```
ARM JSON is the broccoli of Azure — nutritious, rarely anyone's favorite.

Day 42 of #100DaysOfAzureDevOps. ARM templates basics.

Every Portal click still becomes an ARM call. Bicep compiles to ARM. Terraform talks to the same control plane. If I refuse to read JSON templates, I will one day debug a failed deployment by staring at an error that only makes sense if I know schema, resources, and apiVersions.

This is literacy, not my main tool. Deploy a tiny Storage Account template. Delete the resource group. Feel the broccoli. Then decide I do not have to eat a bucket of it every day.

What I keep seeing

1. Template structure is boring and load-bearing
• $schema, contentVersion, parameters, variables, resources, outputs
• Skip resources and you have a comment file

2. apiVersion is a contract
• Wrong version, surprise properties
• Copy-paste from an old blog is how you deploy 2016 into 2026

3. CLI is the honest deploy
• az deployment group create -g rg-day42 -n stor -f infra/storage.json
• Portal "export template" is a start; it is also a nest of defaults you did not choose

4. Delete is part of the lab
• Empty or leftover storage still bills
• rg-day42 should not survive the night without a reason

What I am doing in today's lab

I am deploying a tiny Storage Account ARM template with az deployment group create, confirming the resource exists, then deleting the RG. I am not falling in love with JSON. I am making sure I can read the broccoli.

Nutritious, not favorite. Still eat a forkful so Bicep and Terraform errors make sense.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-42-arm-templates-basics

Tomorrow: ARM parameters and outputs — dials instead of hardcoded names.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 42 — ARM Templates Basics` (max 58 chars)
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

**ARM parameters & outputs**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
