# Day 35 - Blue-Green Deployments

| | |
|---|---|
| **Date** | 24 Sep 2026 |
| **Phase** | 4 - Continuous Delivery |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Concept + App Service implementation; AKS later
- Rollback story

## Hands-on lab (20-30 min)

1. Map blue-green onto slots: blue=prod, green=staging
2. Write rollback steps in `/docs/rollback.md`

## Commands / code

```bash
# docs/rollback.md
# 1. Swap back staging/production
# 2. Verify health endpoint
# 3. Keep previous artifact for 7 days
```

## LinkedIn post (copy-paste)

```
Blue-green means two worlds; only one takes traffic — rollback is a light switch, not an archaeology dig.

Day 35 of #100DaysOfAzureDevOps. Blue-green deployments.

The idea is older than App Service slots: two complete environments, one VIP or hostname taking traffic. Blue is live. Green is the candidate. Flip. If green is sick, flip back. I have been in change windows where "rollback" meant rebuild the previous bits from a laptop because nobody kept the last known good. That is archaeology. Blue-green is a light switch if you paid for the second world and kept the previous artifact.

On App Service, slots are the cheap map: blue = production slot, green = staging. AKS comes later. Today I write rollback steps I would actually follow.

Patterns I keep seeing after a decade in delivery

1. Two worlds, one traffic pointer
• Do not call a single-slot deploy "blue-green" because it sounds senior
• If there is no idle world, there is no switch — there is a hope

2. Rollback is a written procedure
• Swap back staging/production
• Verify a health endpoint, not a feeling
• Keep the previous artifact for a defined window (I am writing 7 days for the lab)

3. Health has to mean ready, not process-up
• A 200 from / that does not touch a dependency is a vanity light
• The switch is only safe if green was smoked as a user would

4. Cost is the reason teams fake it
• A second environment is real money
• Slots on a capable SKU are the lab-sized version of the pattern

What I am doing in today's lab

I am mapping blue-green onto slots (blue=prod, green=staging) and writing /docs/rollback.md with three steps: swap back, verify health, keep the previous artifact for 7 days. If I cannot swap today because of SKU, the document still has to exist. A rollback that lives only in my head is not a rollback.

Keep two worlds or admit you have one. Archaeology is not a rollback strategy.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-35-blue-green-deployments

Tomorrow: Canary releases — 5% / 25% / 100% or abort.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 35 — Blue-Green Deployments` (max 58 chars)
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

**Canary releases**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
