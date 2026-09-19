# Day 38 — Approval Gates & Environments

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 4 - Continuous Delivery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Checks hang on the Environment. A deployment job is the hook. Slack thumbs-up is not an audit trail

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Object | Where you create it | What it does |
| --- | --- | --- |
| Environment | Pipelines → Environments → prod | History, checks, optional resource links |
| Check: Approvals | Environment → ⋮ → Approvals and checks | Pre-deploy: named users/groups must Approve |
| Other checks | Business hours, REST, invoke Azure Function, exclusive lock | Literacy. Lab = Approvals |
| deployment job | deployment: ProdDeploy  environment: prod | The only job type checks reliably attach to |
| YAML approver list | Does not live in YAML | UI on the Environment. Review the object, not a comment |

## Step-by-step lab

1. Pipelines → Environments → New → name: prod (create empty). Open Approvals and checks → + → Approvals → add your personal account → Create.
2. Point a deployment job at environment: prod (extend Day 31 YAML or a tiny echo pipeline). Regular job: will not do.
3. Run the pipeline. Confirm it waits on Approval. Click Approve. Confirm deploy steps run.
4. Run again. Click Reject. Confirm the job fails/stops and does not execute the deploy script.
5. If Reject still deploys, the check is on a different Environment than the job. Fix the name; rerun.
6. Save both run URLs in docs/approvals-day38.md. That is the audit trail Slack never was.

## Done when

- [ ] Environment prod has an Approvals check with your personal account
- [ ] A deployment job waited; Approve ran the echo
- [ ] Reject stopped the deploy script
- [ ] Both run URLs recorded; no work accounts invited

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-38-approval-gates-environments
```

## Next

**Day 39** — Multi-environment pipeline — Dev → Staging → Prod, same drop, approvals on the last stage.
