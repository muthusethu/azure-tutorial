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
Day 77 of #100DaysOfAzureDevOps

The best Azure skill is deleting things - empty RGs are silent subscriptions eating money

Today's topic: **Cost Management & Optimization**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Advisor & WAF.

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

**Advisor & WAF**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
