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
KQL is SQL's cousin who lives in the cloud and judges your where-clauses.

Day 72 of #100DaysOfAzureDevOps. Log Analytics workspace and KQL.

A workspace is a database for telemetry. KQL is how you ask it questions without exporting to Excel to "just filter." I have watched people screenshot 10,000 rows. The cousin is judging. summarize, where TimeGenerated, top 10. Save a query so tomorrow-you is not reinventing the where-clause.

Three queries: AzureActivity is a friendly start even when Heartbeat is empty. ago(1d), count by OperationNameValue. If the workspace is new and quiet, that is data too — I note it instead of faking a graph.

What I keep seeing

1. Time is always part of the question
• where TimeGenerated > ago(1d)
• Unbounded queries are how you wait and pay

2. summarize is the adult SELECT
• count() by OperationNameValue
• top 10 by count_ — a ranking, not a dump

3. Save the query
• A useful KQL that lives only in a chat will die
• Workspace saved queries are the notebook

4. Empty is a result
• No Heartbeat if I never onboarded VMs
• AzureActivity on a quiet lab sub may be thin — I run it anyway and say what I see

What I am doing in today's lab

I am running three KQL queries (AzureActivity sample plus two variations), saving one, and screenshotting results without tenant gossip. If the workspace has no logs, I enable a diagnostic from Day 71 first rather than inventing a table.

Ask the cousin a precise question. Excel is not a Log Analytics strategy.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-72-log-analytics-workspace-kql

Tomorrow: Application Insights — GoPro on the app, connection string not in git.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 72 — Log Analytics & KQL` (max 58 chars)
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

**Application Insights**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
