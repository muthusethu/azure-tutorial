# Day 36 — Canary Releases

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 4 - Continuous Delivery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

A percentage is not a canary. A watch plus a named abort is. Averages hide a dying bird

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Mechanism | What moves | Azure lab knob |
| --- | --- | --- |
| Slot traffic % | Fraction of requests to staging slot | App Service Testing in production (Standard+) |
| Feature flag | Code path on/off per user/cohort | App Configuration / your own flag — no fleet split |
| Revision weight | Later: Container Apps / API Management | Not required today |
| Abort | 0% / flag off / swap back | Must be named before the ramp starts |
| Watch | 5xx, latency, a business heartbeat on the canary only | Do not watch the blended average |

## Step-by-step lab

1. Write docs/canary-plan-day36.md for your webapp: 5% → watch 15 min → 25% → watch → 100% or abort.
2. Name the abort metric in that file (example: 5xx rate on the canary slot, or a failed heartbeat). If you cannot name it, you do not have a canary.
3. Portal → Web app → Deployment slots → Testing in production (if present). Note whether routing % exists on your SKU.
4. If routing exists: send 5% to staging for a few minutes, then 0%. Do not leave a split overnight.
5. Add one sentence: flag vs traffic split — which one this lab would use and why (not both).
6. State that blended averages are forbidden as the watch. Isolated canary metrics only.

## Done when

- [ ] Abort metric is written, not 'we will see'
- [ ] Ramp times are on the page
- [ ] Know Testing-in-prod is SKU-gated
- [ ] Did not leave a traffic split running

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-36-canary-releases
```

## Next

**Day 37** — Rolling deployments — change tires while moving; N and N-1 must coexist or you scheduled a partial outage.
