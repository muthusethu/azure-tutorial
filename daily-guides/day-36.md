# Day 36 - Canary Releases

| | |
|---|---|
| **Date** | 25 Sep 2026 |
| **Phase** | 4 - Continuous Delivery |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Gradual traffic, feature flags, health

## Hands-on lab (20-30 min)

1. Design a canary plan on paper for your webapp
2. Optional: App Service testing in production / traffic routing if available

## Commands / code

```bash
# Canary checklist
# - 5% traffic -> watch errors 15 min
# - 25% -> watch
# - 100% or abort
```

## LinkedIn post (copy-paste)

```
Canaries in coal mines and canaries in prod share a job: die early so the rest of us don't.

Day 36 of #100DaysOfAzureDevOps. Canary releases.

Canary is not a percentage because percentages are fashionable. It is a small slice of real traffic, watched hard, with an abort that is faster than a debate. I have seen "canary" mean "we deployed to one server and went to lunch." That is not a canary. That is an unattended experiment on customers.

App Service testing-in-production / traffic routing is the optional Azure knob. Feature flags are another. Today's mandatory work is a paper plan: 5% → watch errors 15 minutes → 25% → watch → 100% or abort. If I cannot name the abort signal, I do not have a canary. I have a vibe.

What I keep seeing

1. Ramp is a schedule with watches, not a slider
• 5% traffic, watch errors for 15 minutes
• 25%, watch again
• 100% only if the watches were boring

2. Abort is a first-class step
• Name the metric: 5xx rate, latency, a business heartbeat
• If abort is "we will see," the canary cannot die early — users will

3. Flags versus traffic splits
• A feature flag can hide a path without splitting the fleet
• Traffic split can send 5% of users to a new slot or revision
• Pick one for the lab plan; mixing both without a diagram is how you gaslight yourself

4. Health during the watch
• Look at the canary's errors, not the average of old+new
• Averages hide a dying bird

What I am doing in today's lab

I am designing a canary plan on paper for the webapp, and optionally looking at App Service testing in production / traffic routing if the SKU allows. The checklist is 5% → 15 min → 25% → 100% or abort. If I skip Azure knobs today, the paper still has to name the abort.

If the canary cannot die, it cannot save anyone. Write the abort before the ramp.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-36-canary-releases

Tomorrow: Rolling deployments — changing tires while the car is moving.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 36 — Canary Releases` (max 58 chars)
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

**Rolling deployments**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
