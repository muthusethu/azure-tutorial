# Day 90 — Mini Project + Recap (Phase 9)

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 9 - Advanced & Enterprise |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Enterprise is reuse plus guardrails, not more YAML copy-paste

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Day | Artifact | Still true? |
| --- | --- | --- |
| 81 | ADR: lab stays monorepo | Unless you changed it on purpose |
| 82–90 | templates/ consumed by two pipelines | Definition of done today |
| 83 | Marketplace: one spice or written zero | No mystery publishers |
| 84 | Jenkins map on paper | Guarantees, not blue balls |
| 85–88 | Risks, DR drill, LZ sketch, GitOps note | Paper architecture counts |
| 89 | Five paved-road capabilities | Templates are the road, not a mural |

## Step-by-step lab

1. Finish templates/ so one file is the build contract (projectPath and any SDK pin).
2. Create or update two sample pipelines that both call that template with different paths (even if the second only echoes).
3. Run both pipelines. Capture two green run IDs in docs/phase9-recap.md.
4. Grep the repo for duplicated restore/build steps outside the template. Extract or list as leftover homework.
5. Re-read the Day 81 ADR. Still monorepo unless you wrote a new decision.
6. Link Days 83–89 notes (marketplace, Jenkins map, multi-cloud risks, DR, landing zone, GitOps, catalog).
7. Do not add a third unique pipeline to look enterprise.

## Done when

- [ ] One template, two consumers, two green run IDs written down
- [ ] No secret defaults in the template
- [ ] docs/phase9-recap.md links the Phase 9 paper artifacts
- [ ] Did not duplicate YAML just to go green
- [ ] Posted the LinkedIn document

## LinkedIn

Post draft: [`../../daily-guides/day-90.md`](../../daily-guides/day-90.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-90-mini-project-recap-phase-9
```

## Next

**Day 91** — Capstone 1 — a thin public demo slice you can walk in five minutes, not a new ecommerce
