# Day 40 — Mini Project + Recap (Phase 4)

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 4 - Continuous Delivery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Shipping is a pipeline with brakes: artifact, environments, a traffic strategy, a rollback that is not a scavenger hunt

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Day | Object | Keep |
| --- | --- | --- |
| 31 | deployment job + environment | YAML CD, not Classic as source of truth |
| 32–33 | AzureWebApp@1 vs AzureFunctionApp@2 | Web site vs event + plan that can sleep |
| 34–35 | Slots / swap = dressing room / blue-green pointer | F1 has no slots; rollback.md exists anyway |
| 36–37 | Canary ramp vs rolling batches | Abort metric; N/N-1 compatibility |
| 38–39 | Environment checks + promote drop | Reject works; Prod does not rebuild |

## Step-by-step lab

1. Run pipelines/multi-env.yml (or equivalent) end to end. Approve prod. Save the run URL.
2. Confirm each deploy stage lists the same drop / BuildId. If not, fix YAML before writing the recap.
3. Keep docs/rollback.md, canary-plan, and deploy-strategies. Add docs/phase4-recap.md: artifact, env, strategy, brake.
4. Delete leftover rg-day32-lab / rg-day33-lab / S1 plans unless you have a written reason. Echo prod is a valid budget choice.
5. Screenshot the Approval wait (no variable values). That boring picture is the definition of done.
6. Personal learning recap only. No employer story, no client names.

## Done when

- [ ] One run with visible approval and logs saved
- [ ] Same artifact promoted — no rebuild in CD
- [ ] docs/phase4-recap.md written
- [ ] Cost leftovers deleted or listed

## LinkedIn

Post draft: [`../../daily-guides/day-40.md`](../../daily-guides/day-40.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-40-mini-project-recap-phase-4
```

## Next

**Day 41** — IaC concepts — declarative vs imperative, idempotency, drift, and picking Bicep or Terraform (one).
