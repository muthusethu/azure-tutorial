# Day 75 - Dashboards & Workbooks

| | |
|---|---|
| **Date** | 03 Nov 2026 |
| **Phase** | 8 - Monitoring & Observability |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Custom dashboards, workbooks for stakeholders

## Hands-on lab (20-30 min)

1. Pin 3 tiles: availability, failures, cost
2. Share dashboard with yourself only

## Commands / code

```bash
# Portal -> Dashboard -> New -> pin charts from App Insights
```

## LinkedIn post (copy-paste)

```
A dashboard is a storyboard — if it needs a 30-min explanation, it is a novel, not a dashboard.

Day 75 of #100DaysOfAzureDevOps. Dashboards and workbooks.

Stakeholders will not read your KQL. They will glance at a storyboard. Three tiles: availability, failures, cost. If I need a guided tour, I built a novel. I have presented both. The novel loses the room.

Portal dashboard, pin charts from App Insights and Cost Management if I can. Share with myself only. Workbooks are the version with narrative and parameters; I can peek. Today is three tiles that tell a true short story.

Patterns I keep seeing

1. Three tiles, three questions
• Are we up?
• Are we erroring?
• Are we spending by accident?

2. Pin from the real blades
• App Insights charts, not a screenshot pasted as art
• Cost: even a lab sparkline keeps the habit honest

3. Share scope is identity again
• Myself only
• A public dashboard of a lab is still a data leak if I pin the wrong thing

4. Workbooks later for guided ops
• Literacy: parameters, steps, a runbook in portal form
• If the storyboard is already a novel, I cut tiles — I do not add chapters

What I am doing in today's lab

I am creating a dashboard, pinning availability, failures, and cost, and not sharing it beyond myself. If I do not have App Insights data, I pin what I do have and label a tile "no data yet" rather than inventing a healthy green.

Storyboard. Glanceable. If it needs a TED talk, it is not a dashboard.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-75-dashboards-workbooks

Tomorrow: Pipeline monitoring — a red build ignored for a week is culture, not YAML.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 75 — Dashboards & Workbooks` (max 58 chars)
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

**Pipeline monitoring**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
