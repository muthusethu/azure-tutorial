# Day 79 - Incident Management Basics

| | |
|---|---|
| **Date** | 07 Nov 2026 |
| **Phase** | 8 - Monitoring & Observability |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- On-call concepts, runbooks, postmortems

## Hands-on lab (20-30 min)

1. Write a 1-page runbook for 'webapp down' in `/docs/runbook-webapp-down.md`
2. Blameless postmortem template

## Commands / code

```bash
# Symptom -> Checks -> Mitigate -> Communicate -> Postmortem link
```

## LinkedIn post (copy-paste)

```
Postmortems without blame create learning; postmortems with blame create silence.

Day 79 of #100DaysOfAzureDevOps. Incident management basics.

On-call concepts, runbooks, postmortems. I have sat in both kinds of review. The blameless one produced a checklist. The blame one produced quieter Slack and the same outage later. Silence is not reliability.

Write a one-page runbook for "webapp down" in /docs/runbook-webapp-down.md: Symptom → Checks → Mitigate → Communicate → Postmortem link. A template for a blameless write-up. I do not need a real outage to practice the shape. I need the page to exist before 2am.

Patterns I keep seeing

1. Runbooks are for 2am brains
• Short steps, named checks, a health URL
• A novel runbook will not be read in an incident

2. Mitigate is not root cause
• Swap back, scale, disable a flag — stop the bleeding
• Root cause waits until users can log in

3. Communicate is a step, not a side effect
• Who gets a message, what the status is
• Silence while you debug is how rumors fill the gap

4. Blameless is a writing rule
• What happened, what we believed, what we change
• Not who is stupid. That sentence trains people to hide the next incident

What I am doing in today's lab

I am writing the webapp-down runbook and a blameless postmortem template. Symptom → Checks → Mitigate → Communicate → Postmortem. If I have a real lab failure this week, I fill the template once. If not, the empty template still has headings I would not want to invent under stress.

Learn in the write-up. Silence in the write-up is how the outage books a sequel.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-79-incident-management-basics

Tomorrow: Phase 8 mini project — App Insights + one alert + one dashboard.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 79 — Incident Management Basics` (max 58 chars)
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
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 26 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 26 of 33 (rewrite with your real experience)
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

**Phase 8 mini project**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
