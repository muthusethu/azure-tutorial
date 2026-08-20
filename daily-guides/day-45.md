# Day 45 - Bicep Modules & Deployment

| | |
|---|---|
| **Date** | 04 Oct 2026 |
| **Phase** | 5 - Infrastructure as Code |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Modules, what-if, deployment stacks

## Hands-on lab (20-30 min)

1. Run `az deployment group what-if`
2. Split storage into a module

## Commands / code

```bash
az deployment group what-if -g rg-day45 -f main.bicep
```

## LinkedIn post (copy-paste)

```
Day 45 of #100DaysOfAzureDevOps

what-if is a dress rehearsal - read the diff before the audience (prod) arrives

Today's topic: **Bicep Modules & Deployment**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Terraform basics.

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

**Terraform basics**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
