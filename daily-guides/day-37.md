# Day 37 - Rolling Deployments

| | |
|---|---|
| **Date** | 26 Sep 2026 |
| **Phase** | 4 - Continuous Delivery |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- VMSS and Kubernetes rolling updates (concepts)

## Hands-on lab (20-30 min)

1. Compare rolling vs blue-green vs canary in a table in docs
2. No need for AKS yet

## Commands / code

```bash
# Strategy | Downtime | Complexity | Rollback
# Rolling | Low | Medium | Slower
# Blue-green | Near-zero | Medium | Fast swap
# Canary | Near-zero | Higher | Stop ramp
```

## LinkedIn post (copy-paste)

```
Rolling deploys change the tires while the car is moving — thrilling, and occasionally stupid.

Day 37 of #100DaysOfAzureDevOps. Rolling deployments.

VMSS and Kubernetes rolling updates replace instances in batches. The car never fully stops. That is the appeal. It is also how you run two versions of the API at once and discover they disagree about a database column. I have lived through rolling deploys that were "zero downtime" and still half-broken for twenty minutes because mixed versions were not in the design.

No AKS yet. Today is a comparison table in docs: rolling vs blue-green vs canary. Downtime, complexity, rollback speed. Pick with eyes open, not with a blog title.

Patterns I keep seeing

1. Rolling: low downtime, slower rollback
• Batches go healthy before the next batch
• Rollback means rolling forward to old bits — also in batches
• Mixed versions are a feature until a breaking change arrives

2. Blue-green: near-zero cutover, fast switch
• You paid for two worlds
• Rollback is the switch, not a second rolling movie

3. Canary: near-zero, higher operational complexity
• Stop the ramp if the bird dies
• Needs metrics that isolate the new slice

4. Compatibility is the hidden requirement
• Rolling demands N and N-1 can coexist
• If they cannot, rolling is how you schedule a partial outage

What I am doing in today's lab

I am writing a markdown table: Strategy | Downtime | Complexity | Rollback — Rolling, Blue-green, Canary. No AKS cluster today. The table has to be specific enough that I could defend a choice in a design review without hand-waving.

Thrilling is not a strategy. If N and N-1 cannot coexist, do not roll. Switch or flag.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-37-rolling-deployments

Tomorrow: Approval gates and environments — I am the approver on prod.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 37 — Rolling Deployments` (max 58 chars)
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
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 12 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 12 of 33 (rewrite with your real experience)
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

**Approval gates**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
