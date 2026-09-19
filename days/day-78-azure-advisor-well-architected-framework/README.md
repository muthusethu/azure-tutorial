# Day 78 — Azure Advisor & Well-Architected Framework

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 8 - Monitoring & Observability |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

A report card only works if you answer one row

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| WAF pillar | Advisor category you will see | Lab example |
| --- | --- | --- |
| Reliability | High Availability / Reliability | Single-region App Service, no backup on a VM disk |
| Security | Security | Open NSG 22/3389, storage without HTTPS-only, missing Defender |
| Cost Optimization | Cost | Idle Standard SKU, unattached disk, forgotten Public IP |
| Operational Excellence | OperationalExcellence | No alerts, no activity-log diagnostic, click-ops only |
| Performance Efficiency | Performance | Wrong SKU for a burst, missing CDN you do not need in a lab |

## Step-by-step lab

1. Write the five pillars in docs/advisor-day78.md: Reliability, Security, Cost Optimization, Operational Excellence, Performance Efficiency.
2. Portal → Advisor (or az advisor recommendation list). Filter to the personal subscription.
3. Pick one recommendation. Copy the category, resource name, and impact into the markdown.
4. Either accept it and make the change (delete, close a port, add a diagnostic), or dismiss it with a written why (not 'not now').
5. If Advisor is empty (new/empty sub), write that, then run az advisor recommendation list -o table as the receipt.
6. Do not generate or post a Well-Architected assessment score you did not actually run.

## Done when

- [ ] Five pillars written without a fake numeric score
- [ ] One Advisor recommendation accepted with a change or dismissed with a reason
- [ ] docs/advisor-day78.md on the personal repo
- [ ] Personal subscription only
- [ ] Posted the LinkedIn document

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-78-azure-advisor-well-architected-framework
```

## Next

**Day 79** — Incident management basics — a 2am runbook and a blameless postmortem template
