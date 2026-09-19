# Day 40 - Mini Project + Recap (Phase 4)

| | |
|---|---|
| **Date** | 29 Sep 2026 |
| **Phase** | 4 - Continuous Delivery |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- E2E CI/CD with approvals across 3 environments

## Hands-on lab (20-30 min)

1. Green path Dev?Staging?Prod (prod can be echo if no budget)
2. Recap post

## Commands / code

```bash
# Success = one pipeline run with visible approvals and logs saved
```

## LinkedIn post (copy-paste)

```
Phase 4 recap: shipping is a pipeline with brakes, not a YOLO button.

Day 40 of #100DaysOfAzureDevOps. Mini project and recap for Phase 4 — Continuous Delivery.

This phase was App Service, Functions, slots, blue-green, canary, rolling, approvals, and multi-env promotion. The spine is the same: an artifact from CI, an environment object, a strategy for how traffic meets bits, and a brake someone can actually pull.

I have watched "just deploy it" work until it did not. YOLO is a button. Delivery is a path with stages, checks, and a rollback that is not a scavenger hunt. Today's definition of done is one pipeline run with visible approvals and logs saved.

What I am keeping from Phase 4

1. CD is YAML, environments, and a strategy
• Classic mall is literacy; the street we live on is multi-stage YAML
• environment: dev/prod is how history shows up

2. Traffic strategies are choices with costs
• Slots/swap ≈ dressing room
• Blue-green ≈ light switch if you paid for two worlds
• Canary ≈ die early
• Rolling ≈ mixed versions on purpose

3. Brakes are approvals plus rollback docs
• Reject must work
• rollback.md must exist even if prod is an echo

4. Same artifact through the chain
• The recap is not complete if Prod rebuilt
• Ghosts from Day 39 still count as a miss

What I am doing in today's lab

I am running a green path Dev → Staging → Prod (prod may be echo if there is no budget), capturing approvals in the run, saving logs, and writing a recap without heroics. Success is a boring screenshot of a pipeline that waited for me.

Ship with brakes. A YOLO button is not courage. It is unpaid incident duty.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-40-mini-project-recap-phase-4

Tomorrow: IaC concepts — declarative vs imperative, drift, pick Bicep or Terraform.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 40 — Phase 4 Mini Project & Recap` (max 58 chars)
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
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 13 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 13 of 33 (rewrite with your real experience)
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

**IaC concepts**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
