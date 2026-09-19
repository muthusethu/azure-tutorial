# Day 35 — Blue-Green Deployments

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 4 - Continuous Delivery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Two complete worlds, one pointer. Rollback is a light switch — only if you kept the previous artifact

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Idea | App Service lab map | Not this |
| --- | --- | --- |
| Blue (live) | Production slot + production hostname | A single in-place zip overwrite |
| Green (candidate) | staging slot, smoked, still idle to users | A branch named green with no second host |
| Cutover | Swap (VIP flip) — 100% in one move | A 5% traffic ramp (that is canary, Day 36) |
| Rollback | Swap back; same two worlds | Rebuild last week's commit from a laptop |
| AKS later | Two Deployments + Service/Ingress flip | Not today's cluster bill |

## Step-by-step lab

1. Draw blue = production slot, green = staging, pointer = swap. One box each in docs/rollback.md (or a comment sketch).
2. Write docs/rollback.md with three numbered steps: (1) swap back staging/production, (2) verify a real URL, (3) keep previous pipeline artifact 7 days.
3. If S1+ slots exist from Day 34: deploy N to green, smoke, swap (blue↔green), then swap back using only the doc.
4. Record the artifact run ID you would keep as N-1. CD must download that drop — not rebuild.
5. Add a sentence on schema: if green needs a breaking column, the switch is unsafe until expand/contract.
6. Do not stand up AKS for this metaphor. Slots are the lab-sized two worlds.

## Done when

- [ ] Can distinguish blue-green (100% flip) from canary (ramp)
- [ ] docs/rollback.md has swap, verify, keep artifact
- [ ] Did not call a single-slot deploy blue-green
- [ ] No AKS spend today

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-35-blue-green-deployments
```

## Next

**Day 36** — Canary releases — a small slice of real traffic, a watch, and an abort that is faster than a debate.
