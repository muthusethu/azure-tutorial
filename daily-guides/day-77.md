# Day 77 - Cost Management & Optimization

| | |
|---|---|
| **Date** | 05 Nov 2026 |
| **Phase** | 8 - Monitoring & Observability |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Budgets, alerts, right-sizing

## Hands-on lab (20-30 min)

1. Review Cost Analysis for lab subscription
2. Tighten budget alert
3. Kill orphan resources

## Commands / code

```bash
az group list -o table
# delete unused RGs
az group delete -n <old-rg> --yes --no-wait
```

## LinkedIn post (copy-paste)

```
The best Azure skill is deleting things — empty RGs are silent subscriptions eating money.

Day 77 of #100DaysOfAzureDevOps. Cost management and optimization.

Budgets, alerts, right-sizing. I have seen more "mystery bills" from leftover labs than from a single large VM that someone at least knew existed. Empty resource groups with a forgotten Public IP, a Basic ACR, an AKS I swore I would kill. Silent eating.

Cost Analysis on the lab subscription. Tighten the budget alert from Day 1 energy. az group list, delete unused. Right-sizing is a sentence I will not fake with invented percentages. I will say what I actually deleted.

Patterns I keep seeing

1. Budgets are promises to future-you
• Alert before the invoice is a personality
• A budget you never look at is a sticker

2. Orphans hide in lists
• az group list -o table
• az group delete -n <old-rg> --yes --no-wait
• Names like rg-day42 that survived Day 50

3. Right-size after you see the graph
• Cost Analysis, filter by RG
• I will not invent a savings number I did not measure

4. Delete is a deploy skill
• Destroy from Terraform/Bicep when that is how it was born
• Portal delete when it was click-ops. Either way, gone

What I am doing in today's lab

I am opening Cost Analysis, tightening a budget alert, listing resource groups, and deleting unused lab RGs. I will mention what I deleted, not a fictional savings percentage. If AKS from Day 56 is still alive, today is its due date if the weekend already passed.

Deletion is cost optimization you can prove. Empty RGs are not free. They are quiet.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-77-cost-management-optimization

Tomorrow: Azure Advisor and Well-Architected — five pillars, one recommendation I actually judge.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 77 — Cost Management` (max 58 chars)
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

**Advisor & WAF**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
