# Day 73 — Application Insights Integration

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 8 - Monitoring & Observability |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Instrumentation + connection string — dependencies tell you which friend is slow

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Piece | Job | Secret handling |
| --- | --- | --- |
| App Insights resource | Workspace-based component (classic is legacy) | Create in rg-day73; tie to law-lab |
| Connection string | SDK send target (InstrumentationKey is old news) | App setting or Key Vault reference. Never commit |
| SDK / auto-instrumentation | Requests, exceptions, dependencies, live metrics | Runtime. A portal resource with no SDK is an empty GoPro |
| Dependencies | HTTP/SQL/Redis map of who you wait on | A slow app with clean CPU is often a slow friend |
| Live metrics | Incident stream | Not the only alert; wallpaper is Day 74's problem |

## Step-by-step lab

1. az monitor app-insights component create (or Portal) in rg-day73, linked to law-lab. Copy the connection string into the vault or a local password manager — not the repo.
2. Connect the sample app (SDK, Application Insights agent, or App Service auto-instrumentation). If you cannot, still create the resource and walk the blades with data honestly labeled.
3. Generate traffic. Open Failures and Performance. Click a dependency if one exists. Note one request duration.
4. Confirm git grep does not find InstrumentationKey or APPLICATIONINSIGHTS_CONNECTION_STRING values.
5. Optional: add the connection string as a Key Vault reference on an App Service you already have. App identity needs Secrets User.
6. Write docs/appi-day73.md: resource name, whether SDK or demo, that empty Failures means dark not reliable.

## Done when

- [ ] App Insights resource exists and is workspace-based
- [ ] Connection string not in the repo
- [ ] Generated traffic or honestly labeled empty/demo
- [ ] Can explain dependencies vs live metrics vs failures map

## LinkedIn

Post draft: [`../../daily-guides/day-73.md`](../../daily-guides/day-73.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-73-application-insights-integration
```

## Next

**Day 74** — Alerts and action groups — screams need an inbox
