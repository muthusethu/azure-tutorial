# Day 72 — Log Analytics Workspace & KQL

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 8 - Monitoring & Observability |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

A workspace is a database for telemetry — TimeGenerated is part of every honest question

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Piece | What it is | Lab table |
| --- | --- | --- |
| Workspace | The store. Retention and access live here | law-lab from Day 71 |
| Table | AzureActivity, Heartbeat, KV audit, App traces — schema differs | AzureActivity is friendly even when Heartbeat is empty (no VMs) |
| KQL | where / summarize / join / top. SQL's cousin in the cloud | Always filter TimeGenerated. Unbounded queries wait and pay |
| Saved query | Workspace notebook so tomorrow-you does not reinvent the where | Save one query by name |
| Empty result | A result. New labs are quiet | Do not fake a graph. Enable Day 71 diagnostics first |

## Step-by-step lab

1. Portal → Log Analytics workspace law-lab → Logs. Confirm you are not in an employer workspace.
2. Run query 1: AzureActivity | where TimeGenerated > ago(1d) | summarize count() by OperationNameValue | top 10 by count_.
3. Run query 2: a where on a specific OperationNameValue you saw, or AzureActivity | take 10 if the lab is quiet — still a result.
4. Run query 3: Heartbeat | take 5. If empty, write 'no VMs onboarded' — do not pretend. Optionally query the Key Vault audit table if Day 71 sent AuditEvent.
5. Save one query with a name (e.g. lab-azureactivity-topops). Screenshot results without tenant gossip.
6. Write docs/kql-day72.md: the three queries, which tables were empty, and why TimeGenerated is mandatory.

## Done when

- [ ] Three queries ran against the personal workspace
- [ ] One query saved
- [ ] Can explain why Heartbeat may be empty and AzureActivity still useful
- [ ] Every query used a TimeGenerated filter (or take with a reason)

## LinkedIn

Post draft: [`../../daily-guides/day-72.md`](../../daily-guides/day-72.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-72-log-analytics-workspace-kql
```

## Next

**Day 73** — Application Insights — a GoPro on the app, connection string not in git
