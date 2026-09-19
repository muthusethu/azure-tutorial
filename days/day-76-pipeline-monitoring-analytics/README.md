# Day 76 — Pipeline Monitoring & Analytics

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 8 - Monitoring & Observability |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Treat red as a signal you own, not décor you scroll past

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Surface | What it measures | Where you click |
| --- | --- | --- |
| Pipelines → Analytics | Pass rate, duration, failure trend for YAML pipelines | Project → Pipelines → Analytics (or Insights) |
| Test insights / flakes | Tests that pass and fail on the same commit | Run → Tests tab; flaky test report if enabled |
| Release / env history | Which environment ate the last failed deploy | Pipelines → Environments → deployments |
| Job log duration | Which task burned hosted minutes | Run → job → each step elapsed time |
| Board / work item link | Which change shipped with the red run | Run → Related / work items |

## Step-by-step lab

1. Project → Pipelines → Analytics (or Insights). If the blade is empty, open the last 10 runs on your busiest YAML pipeline and tally pass/fail by hand.
2. Write this week's failure rate (or last-N pass count) in docs/pipeline-health-day76.md. Zero runs = write 'darkness', not 100%.
3. Open the newest failed run. Name the failing task and the exception line. If it is a flake, write the test name; do not only click Re-run.
4. On a green run, note the three longest tasks and their elapsed times. Duration is hosted minutes plus feedback delay.
5. If any pipeline is still red, either fix it in this lab or add a one-sentence owner note in the markdown. Costume off.
6. Confirm you are in the personal org (not a work tenant) before any screenshot for the LinkedIn document.

## Done when

- [ ] Can say this week's failure rate (or last-N tally) out loud
- [ ] Named a flake or wrote 'no flake — real fail' with the task name
- [ ] docs/pipeline-health-day76.md exists on the personal repo
- [ ] Did not screenshot an employer org
- [ ] Posted the LinkedIn document (personal account)

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-76-pipeline-monitoring-analytics
```

## Next

**Day 77** — Cost management — Cost Analysis, a tighter budget alert, and deleting leftover lab resource groups
