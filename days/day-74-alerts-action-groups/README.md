# Day 74 — Alerts & Action Groups

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 8 - Monitoring & Observability |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

The rule is the condition; the action group is the destination — a rule with nobody to email is performance art

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Piece | What it is | Lab choice |
| --- | --- | --- |
| Action group | Destination list: email, SMS, webhook, ITSM, ARM | Email yourself (personal). Proof of delivery today |
| Metric alert | Platform metric threshold (CPU, availability) | Something you can provoke on a tiny SKU or availability test |
| Log alert | KQL that returns rows → fire | AzureActivity or App Insights requests failed > N |
| Severity | Sev 0–4 language | Sev 3 for lab. If everything is Sev 0, nothing is |
| Fired vs resolved | State. Noise trains mute | One clean fire beats ten flaps. Delete with the resource |

## Step-by-step lab

1. Monitor → Alerts → Action groups → Create ag-lab-email, short name labag, email receiver = your personal address.
2. Create one alert rule: either a metric you can provoke, a standard availability test on a URL you control, or a log alert on a KQL you can satisfy. Severity 3. Attach ag-lab-email.
3. Fire it (stop the app, exceed CPU on a tiny VM, or generate the log rows). Wait the evaluation window.
4. Confirm the email arrived. If not: spam, action group receiver confirmed, alert Fired state in Portal. The lab is not done until delivery or a written blocker.
5. Note the difference between Fired and a dashboard glance. Live metrics (Day 73) are not this.
6. Write docs/alerts-day74.md: rule name, condition, action group, whether mail arrived. Plan to delete the rule with the resource so it does not flap for a year.

## Done when

- [ ] Action group emails the personal inbox
- [ ] One alert rule attached to that group
- [ ] Tried to receive the email (or documented the blocker)
- [ ] Severity chosen on purpose; delete plan written

## LinkedIn

Post draft: [`../../daily-guides/day-74.md`](../../daily-guides/day-74.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-74-alerts-action-groups
```

## Next

**Day 75** — Dashboards and workbooks — three tiles, not a 30-minute novel
