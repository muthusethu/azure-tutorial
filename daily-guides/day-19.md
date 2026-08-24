# Day 19 - Repo Security

| | |
|---|---|
| **Date** | 08 Sep 2026 |
| **Phase** | 2 - Azure Repos & Git Mastery |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Branch policies: reviewers, work items, build validation, status checks
- Docs: https://learn.microsoft.com/azure/devops/repos/git/branch-policies

## Hands-on lab (20-30 min)

1. On `main`: require 1 reviewer (yourself ok for lab), require linked work item
2. Limit merge types to squash
3. Try pushing directly to main - should fail if policy set correctly

## Commands / code

```bash
# Azure DevOps UI:
# Repos -> Branches -> main -> Branch policies
# - Require a minimum number of reviewers: 1
# - Check for linked work items: Required
# - Limit merge types: Squash merge
```

## LinkedIn post (copy-paste)

```
Day 19 of #100DaysOfAzureDevOps

Branch policies are parental controls for adults who still push to main at 11:58pm

Today's topic: **Repo Security**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Phase 2 mini project.

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
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 6 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 6 of 33 (rewrite with your real experience)
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

**Phase 2 mini project**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
