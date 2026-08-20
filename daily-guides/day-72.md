# Day 72 - Log Analytics Workspace & KQL

| | |
|---|---|
| **Date** | 31 Oct 2026 |
| **Phase** | 8 - Monitoring & Observability |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Workspace setup, KQL basics

## Hands-on lab (20-30 min)

1. Run 3 KQL queries: Heartbeat or AzureActivity samples
2. Save a query

## Commands / code

```bash
AzureActivity
| where TimeGenerated > ago(1d)
| summarize count() by OperationNameValue
| top 10 by count_
```

## LinkedIn post (copy-paste)

```
Day 72 of #100DaysOfAzureDevOps

KQL is SQL's cousin who lives in the cloud and judges your where-clauses

Today's topic: **Log Analytics Workspace & KQL**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Application Insights.

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

**Application Insights**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
