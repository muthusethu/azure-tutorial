# Day 34 - Deployment Slots & Swap Strategies

| | |
|---|---|
| **Date** | 23 Sep 2026 |
| **Phase** | 4 - Continuous Delivery |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Staging slots, swap, warm-up, auto-swap

## Hands-on lab (20-30 min)

1. If SKU allows: create staging slot, deploy, swap
2. Document warm-up path

## Commands / code

```bash
# Portal: Web App -> Deployment slots -> Add slot `staging`
# Swap staging -> production after smoke test
```

## LinkedIn post (copy-paste)

```
Slots are dressing rooms for production — try the outfit on before walking the runway.

Day 34 of #100DaysOfAzureDevOps. Deployment slots and swap strategies.

Swapping a slot is the closest App Service gets to a rehearsal. Warm the staging slot, hit a smoke URL, swap. If the outfit rips, swap back. I have watched teams treat swap as a fancy copy-paste and skip warm-up, then blame "Azure" for a cold-start outage they scheduled.

Not every SKU has slots. That is not a trivia question. It is why yesterday's F1 plan may refuse today's lab. Document the warm-up path anyway. Auto-swap is a power tool; I am not turning it on until smoke is real.

What I keep seeing

1. Staging is not production with a nickname
• Slot settings can stick (connection strings, flags) so the swap does not carry the wrong config
• If config is identical by accident, you have not learned slots — you have copied them

2. Warm-up is the point
• Hit the staging URL until the app is actually ready
• Swap of a cold process is a self-inflicted brownout

3. Swap is two-way
• staging → production after smoke
• production → staging is the rollback, not a conference-call archaeology dig

4. Auto-swap needs a grown-up smoke
• If smoke is "I looked at the log," do not auto-swap
• Document the warm-up path even if the SKU blocks the slot today

What I am doing in today's lab

If the SKU allows it, I am adding a staging slot, deploying to it, smoking it, and swapping. If it does not, I am writing the warm-up path and the SKU note so I do not pretend the lab passed. Portal: Web App → Deployment slots → Add slot staging.

Walk the runway only after the dressing room mirror. Swap is a rehearsal tool, not a personality.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-34-deployment-slots-swap-strategies

Tomorrow: Blue-green deployments — two worlds, one traffic, a written rollback.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 34 — Deployment Slots & Swap` (max 58 chars)
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
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 11 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 11 of 33 (rewrite with your real experience)
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

**Blue-green deployments**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
