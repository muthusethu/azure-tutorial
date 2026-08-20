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
Day 42 of #100DaysOfAzureDevOps

ARM JSON is the broccoli of Azure - nutritious, rarely anyone's favorite

Today's topic: **ARM Templates Basics**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: ARM parameters & outputs.

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

**ARM parameters & outputs**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
