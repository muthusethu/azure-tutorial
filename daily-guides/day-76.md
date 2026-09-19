# Day 76 - Pipeline Monitoring & Analytics

| | |
|---|---|
| **Date** | 04 Nov 2026 |
| **Phase** | 8 - Monitoring & Observability |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Build/release analytics, flaky insights

## Hands-on lab (20-30 min)

1. Open Analytics views for pipelines
2. Note failure rate this week

## Commands / code

```bash
# Azure DevOps -> Pipelines -> Analytics / Insights
```

## LinkedIn post (copy-paste)

```
A red pipeline ignored for a week is a culture problem wearing a YAML costume.

Day 76 of #100DaysOfAzureDevOps. Pipeline monitoring and analytics.

Build analytics, release analytics, flaky tests. Azure DevOps will show failure rate if I look. I have been on teams where main was red from Monday to Thursday because "it is always like that." That is not YAML. That is a culture that trained itself to ignore the fire alarm.

Open Pipelines analytics/insights. Note this week's failure rate. If I have few runs, I still look at the last ten and write which failed and why. Flakes get names or they get ignored forever.

What I keep seeing

1. Failure rate is a DORA cousin
• A number I can say out loud
• Zero runs is not 100% success. It is darkness

2. Flakes are incidents on installment
• Re-run until green is how you teach the team to ignore red
• Name the flake or delete the test. Do not live with a coin flip

3. Duration is a cost
• Hosted minutes, feedback delay
• A 40-minute CI that used to be 8 is a product problem

4. Insights are only useful if someone owns red
• Today: I own my lab pipelines
• If I leave a red run "for later," I am practicing the culture I am complaining about

What I am doing in today's lab

I am opening Azure DevOps → Pipelines → Analytics/Insights, noting failure rate this week (or last N runs), and fixing or documenting any red I am ignoring. Costume off. If it is red, it is mine.

Red is a signal. A week of mute is a culture. YAML is just the fabric.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-76-pipeline-monitoring-analytics

Tomorrow: Cost management — delete orphan RGs, tighten the budget alert.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 76 — Pipeline Monitoring` (max 58 chars)
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
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 25 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 25 of 33 (rewrite with your real experience)
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

**Cost management**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
