# Day 13 - Azure Repos Setup

| | |
|---|---|
| **Date** | 02 Sep 2026 |
| **Phase** | 2 - Azure Repos & Git Mastery |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Repo creation, default branch, folder structure standards
- Repo policies overview (deep dive day 19)

## Hands-on lab (20-30 min)

1. Set default branch to `main`
2. Create folders: `/src`, `/docs`, `/pipelines`, `/infra`
3. Add `.gitignore` for your language (dotnet/node/python)

## Commands / code

```bash
# .gitignore (Node example)
node_modules/
dist/
.env
*.log
.DS_Store
```

## LinkedIn post (copy-paste)

```
Day 13 of #100DaysOfAzureDevOps

A messy repo root is a messy brain - /src /docs /pipelines /infra saves future-you from archaeology

Today's topic: **Azure Repos Setup**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Pull requests & code review.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5-10 real comments on other Azure/DevOps posts.

## Reminder — 2nd LinkedIn post (production track)

**Today you publish TWO separate LinkedIn posts.** The daily lesson above is post 1 only.

| | Post 1 — #100DaysOfAzureDevOps | Post 2 — #ProductionGradeAzure |
|---|-------------------------------|----------------------------------|
| **When** | ~10:00 IST | ~17:00–19:00 IST (after some engagement on post 1) |
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 4 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 4 of 33 (rewrite with your real experience)
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

**Pull requests & code review**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
