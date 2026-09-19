# Day 91 - Capstone Project 1 - E2E App CI/CD

| | |
|---|---|
| **Date** | 19 Nov 2026 |
| **Phase** | 10 - Portfolio & Public Launch |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Reuse earlier app; harden CI/CD
- Do NOT start a giant ecommerce from zero

## Hands-on lab (20-30 min)

1. Define MVP: one app, CI, CD to App Service/Container Apps, README diagram
2. Work in `capstone/` folder

## Commands / code

```bash
# Scope control
# In: one service, tests, pipeline, env promotion
# Out: payments, recommendations ML, 12 microservices
```

## LinkedIn post (copy-paste)

```
Capstones fail from ambition — ship a thin vertical slice you can demo in 5 minutes.

Day 91 of #100DaysOfAzureDevOps. Capstone project 1 — end-to-end app CI/CD.

Reuse the earlier app. Harden CI/CD. Do not start a giant ecommerce from zero. I have watched capstones die under payments, recommendation ML, and twelve microservices that never took a single request. Ambition. The slice is one service, tests, pipeline, environment promotion, a README diagram.

Work in capstone/. MVP: one app, CI, CD to App Service or Container Apps. In: tests, pipeline, env promotion. Out: payments, ML, a fleet. A 5-minute demo is a design constraint, not a lack of seriousness.

Patterns I keep seeing after a decade in delivery

1. Reuse beats rewrite
• The sample from CI/CD phases is the product
• A new repo named shop-clone is how Day 100 arrives with nothing to pin

2. Vertical slice means a user-shaped path
• Build → test → artifact → deploy → URL
• Horizontal "all the YAML in the world" is not a demo. It is a junk drawer

3. README diagram is part of the build
• If I cannot draw it, I cannot demo it in five minutes
• Boxes: repo, pipeline, env, app

4. Scope control is a written list
• In / Out in capstone/README
• When I want to add a microservice, I read the Out list out loud

What I am doing in today's lab

I am defining the MVP in capstone/: one app, CI, CD to App Service or Container Apps, README diagram. I am not scaffolding payments. If the old pipeline is dusty, I harden it here — that is the work. Thin slice, demo-able.

Five minutes. One path. Ambition can wait for a product that has users.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-91-capstone-project-1-e2e-app-ci-cd

Tomorrow: Capstone 2 — same app in a container tuxedo.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 91 — Capstone 1: E2E App CI/CD` (max 58 chars)
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
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 30 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 30 of 33 (rewrite with your real experience)
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

**Capstone 2**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
