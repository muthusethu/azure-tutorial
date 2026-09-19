# Day 73 - Application Insights Integration

| | |
|---|---|
| **Date** | 01 Nov 2026 |
| **Phase** | 8 - Monitoring & Observability |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Instrumentation, dependencies, live metrics

## Hands-on lab (20-30 min)

1. Create App Insights; connect to sample app or use portal demo
2. Generate traffic; view failures map

## Commands / code

```bash
# Add connection string via Key Vault / app settings - never commit it
```

## LinkedIn post (copy-paste)

```
App Insights is a GoPro on your app — embarrassing, invaluable.

Day 73 of #100DaysOfAzureDevOps. Application Insights integration.

Instrumentation, dependencies, live metrics. A GoPro will record you dropping the ball. That is the point. I have shipped apps whose only telemetry was IIS logs and a prayer. Failures map, dependency arrows, a request that took 8 seconds because it waited on a DNS mistake — you see it when the SDK is in the app and the connection string is not in git.

Create Application Insights. Connect to the sample app or use a portal demo. Generate traffic. Look at failures. Connection string via Key Vault or app settings. Never commit it.

Patterns I keep seeing

1. Connection string is a secret
• App settings or Key Vault
• A connection string in source is a postcard with a camera attached

2. Dependencies tell the truth
• HTTP, SQL, Redis — the map of who you wait on
• A slow app with a clean CPU is often a slow friend

3. Live metrics are for the incident, not the wallpaper
• Use them when you are in it
• Do not require a human to stare at live metrics as the only alert

4. Generate traffic or you will admire an empty GoPro
• Hit the sample, fail on purpose once if I can
• Empty failures blade is not "we are reliable." It is "we are dark"

What I am doing in today's lab

I am creating Application Insights, pointing the sample (or portal demo) at it, generating traffic, opening the failures map, and confirming the connection string is not in the repo. If I cannot instrument the app today, I still create the resource and walk the blades with demo data honestly labeled as demo.

Embarrassing video is how you stop dropping the ball. No camera, no coaching.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-73-application-insights-integration

Tomorrow: Alerts and action groups — screams need a destination.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 73 — Application Insights` (max 58 chars)
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
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 24 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 24 of 33 (rewrite with your real experience)
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

**Alerts & action groups**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
