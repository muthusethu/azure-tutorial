# Day 80 — Mini Project + Recap (Phase 8)

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 8 - Monitoring & Observability |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Deploy is not done — observable is done

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Piece | Azure object | Proof today |
| --- | --- | --- |
| Flashlight | Azure Monitor / metrics on the App Service or Container App | You can see CPU/HTTP without guessing |
| Camera | Application Insights (microsoft.insights/components) | A request or exception appears after a hit |
| Scream | Metric alert + Action Group (email to you) | Forced 5xx or availability fail pages you |
| Storyboard | Azure dashboard or App Insights workbook, 3 tiles | Failure, requests, cost or pipeline health |
| Culture | Pipeline Analytics + runbook from Days 76/79 | Red has an owner; 2am has a page |

## Step-by-step lab

1. Pick one deployed lab app (App Service or Container Apps) on the personal sub. Note its resource group in docs/phase8-recap.md.
2. Confirm Application Insights is connected (or create one microsoft.insights/components and wire the app).
3. Create one metric or log alert + Action Group that emails your personal inbox. Portal → Monitor → Alerts.
4. Pin a three-tile dashboard: requests or availability, failures/exceptions, and either cost or pipeline pass rate.
5. Force a reversible failure (stop the web app, hit a /fail route, or swap to a broken slot). Start a timer.
6. Confirm you can see the failure in Insights/dashboard and/or the alert within five minutes. Write the elapsed time — or write that you could not, and what was missing.
7. Link the Day 76 health note, Day 77 deletes, Day 78 Advisor row, and Day 79 runbook. Recap without fake MTTR.

## Done when

- [ ] App Insights + one alert + one dashboard exist on the personal app
- [ ] Forced a reversible failure and recorded whether it showed within 5 minutes
- [ ] docs/phase8-recap.md links Days 76–79 artifacts
- [ ] No invented MTTR percentage
- [ ] Leftover paid SKUs still deleted from Day 77

## LinkedIn

Post draft: [`../../daily-guides/day-80.md`](../../daily-guides/day-80.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-80-mini-project-recap-phase-8
```

## Next

**Day 81** — Multi-repo vs monorepo — an ADR for this lab, not a trending blog title
