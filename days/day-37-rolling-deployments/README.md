# Day 37 — Rolling Deployments

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 4 - Continuous Delivery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Batches replace instances while traffic still flows. Rollback is another movie — not a light switch

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Platform | Knob | Mixed versions? |
| --- | --- | --- |
| VMSS | upgradePolicy mode: Rolling; maxBatchInstancePercent; pauseTimeBetweenBatches | Yes, during the wave |
| AKS Deployment | strategy.rollingUpdate maxUnavailable / maxSurge | Yes, until the ReplicaSet drains |
| App Service | Instance replacement / restart — not the same as VMSS rolling | Usually a new zip on the fleet, not a designed N/N-1 wave |
| Slots / blue-green | Not rolling — idle world + flip | No mix on the live pointer |
| Canary | Not rolling — % of traffic, maybe one slot | Old + new by request share |

## Step-by-step lab

1. Create docs/deploy-strategies-day37.md with a table: Strategy | Downtime | Complexity | Rollback | Mixed versions? for Rolling, Blue-green, Canary, In-place.
2. Fill every cell with something specific (swap, maxUnavailable, 5% ramp) — not 'low' / 'high' alone.
3. Write one scenario where rolling is wrong (breaking API or breaking schema) and which strategy you would pick instead.
4. Skim Learn: VMSS rolling upgrade OR Kubernetes rolling updates. Note one knob name in the doc (maxBatchInstancePercent or maxUnavailable).
5. Do not create AKS or a scale set for this lab. Cost is not a badge.
6. Cross-link docs/rollback.md (Day 35) and docs/canary-plan-day36.md so the three docs agree.

## Done when

- [ ] Table exists with rollback + mixed-version columns
- [ ] Can explain why breaking changes forbid rolling
- [ ] No AKS/VMSS created for a metaphor
- [ ] Docs agree with Days 35–36

## LinkedIn

Post draft: [`../../daily-guides/day-37.md`](../../daily-guides/day-37.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-37-rolling-deployments
```

## Next

**Day 38** — Approval gates and environments — checks live on the Environment, not in Slack.
