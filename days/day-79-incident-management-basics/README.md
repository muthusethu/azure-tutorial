# Day 79 — Incident Management Basics

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 8 - Monitoring & Observability |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Write the runbook before 2am, and write the review without blame

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Stage | Output you write | Not this |
| --- | --- | --- |
| Detect | Alert / health URL / user report timestamp | Waiting for a feeling that 'it seems down' |
| Checks | Ordered probes: DNS, App Service state, App Insights failures | A 12-page novel nobody opens |
| Mitigate | Swap slot, scale, revert pipeline, disable a flag | Root-cause essay while users are still down |
| Communicate | Who gets a status line, what is true now | Silent debug while rumors fill the gap |
| Postmortem | What happened, what we believed, what changes | Who is stupid — that sentence trains silence |

## Step-by-step lab

1. Create docs/runbook-webapp-down.md with headings: Symptom → Checks → Mitigate → Communicate → Postmortem link.
2. Fill Checks with concrete probes: Portal App Service status, https://<app>.azurewebsites.net/health, App Insights failures, last pipeline deploy.
3. Fill Mitigate with last-good artifact / slot swap / stop-start — not a root-cause paragraph.
4. Add docs/postmortem-template.md: Summary, Timeline, What we believed, What was true, What we change, Follow-ups. No blame section.
5. If you had a real lab failure this week, fill the template once. If not, leave headings plus one fictional timeline labeled FICTION.
6. Link the two files from README or docs/index. A page that cannot be found at 2am does not exist.

## Done when

- [ ] docs/runbook-webapp-down.md has the five headings and at least one real CLI/URL check
- [ ] docs/postmortem-template.md is blameless (no 'who failed' section)
- [ ] Mitigate is separate from root cause
- [ ] No employer outage story
- [ ] Posted the LinkedIn document

## LinkedIn

Post draft: [`../../daily-guides/day-79.md`](../../daily-guides/day-79.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-79-incident-management-basics
```

## Next

**Day 80** — Phase 8 recap — App Insights + one alert + one dashboard, and a forced failure you can see in five minutes
