# Day 71 — Azure Monitor Fundamentals

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 8 - Monitoring & Observability |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Metrics are the pulse, logs are the sentences, activity is who changed ARM — diagnostics are opt-in

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Signal | What it answers | Where it lives |
| --- | --- | --- |
| Metrics | CPU, availability, queue length — numbers on a time axis | Platform metrics on the resource. Near-real-time, cheap-ish |
| Logs | The story in rows you query with KQL | Log Analytics workspace, only after diagnostic settings (or agents) send them |
| Activity log | Control plane: who PUT/DELETE this RG / vault / AKS | Subscription activity. Not the app's 500s |
| Diagnostic settings | The pipe: resource → workspace / storage / event hub | Opt-in. Without them the workspace is an empty room |
| Insights blades | App Insights, Container Insights, VM Insights — packaged views | Still Monitor. They do not patch the hole |

## Step-by-step lab

1. Portal → Monitor → Overview. Click through Metrics, Activity log, Logs. Write one sentence each: pulse vs diary vs sentences.
2. Create or reuse a Log Analytics workspace in a lab RG (law-lab) if cost allows. If you skip, still complete the paper map and say why.
3. On one resource (Key Vault or App Service) → Diagnostic settings → send Audit / HTTP logs + AllMetrics to law-lab. Category vs category group: pick what the blade offers.
4. Generate a control-plane event (tag the resource). Activity log should show your user. That is not an app failure.
5. Write docs/monitor-day71.md: which signal you would use to detect 'it is down', retention choice, resource id of the diagnostic setting.
6. Do not onboard the whole subscription. Do not start a 90-day retention experiment. KQL is tomorrow.

## Done when

- [ ] Can separate metrics, logs, and activity log without mixing them
- [ ] One diagnostic setting exists — or a written cost skip plus the paper map
- [ ] Knows diagnostics are opt-in
- [ ] docs/monitor-day71.md names the 'it is down' signal

## LinkedIn

Post draft: [`../../daily-guides/day-71.md`](../../daily-guides/day-71.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-71-azure-monitor-fundamentals
```

## Next

**Day 72** — Log Analytics and KQL — ask a precise question, stop screenshotting 10,000 rows
