# Day 75 — Dashboards & Workbooks

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 8 - Monitoring & Observability |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

A dashboard is a storyboard: up, erroring, spending — if it needs a TED talk it is a novel

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Surface | What it is | Share / identity |
| --- | --- | --- |
| Azure dashboard | Pinned tiles from real blades (App Insights, Cost, metrics) | Share with yourself only in this lab. Public = leak risk |
| Workbook | Narrative + parameters + queries. A runbook in portal form | Literacy today. Do not add chapters because the storyboard is already long |
| App Insights view | Failures / availability as source of pins | Pin the live chart, not a PNG of last Tuesday |
| Cost Management tile | Are we spending by accident? | Lab sparkline keeps the habit honest |
| ADO dashboard | Pipeline widgets — different product (Day 76 energy) | Do not mix it into the Azure storyboard unless labeled |

## Step-by-step lab

1. Portal → Dashboard → New. Name it azure-100-lab. Privacy: private / share with yourself only.
2. Pin tile 1 — availability (App Insights availability test or a metric that means 'up'). If you have no test, pin what you do have and label the gap.
3. Pin tile 2 — failures / failed requests. If empty because the app is dark, write 'no data yet' in the tile title rather than inventing healthy green.
4. Pin tile 3 — cost (Cost Management, lab RG). Even a small sparkline counts.
5. Open Workbooks in Monitor or App Insights. Peek at a template (parameters, steps). Do not paste a 12-step novel onto the dashboard. One sentence in the doc: workbook = guided ops, dashboard = glance.
6. Write docs/dashboard-day75.md: the three questions, share scope, and that Day 76 is pipeline analytics in Azure DevOps — a different storyboard.

## Done when

- [ ] Dashboard with three tiles mapped to up / erroring / spending
- [ ] Shared with yourself only
- [ ] Empty data labeled honestly
- [ ] Knows workbook vs dashboard in one sentence

## LinkedIn

Post draft: [`../../daily-guides/day-75.md`](../../daily-guides/day-75.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-75-dashboards-workbooks
```

## Next

**Day 76** — Pipeline monitoring and analytics — a red pipeline ignored for a week is a culture problem
