# Day 71 - Azure Monitor Fundamentals

| | |
|---|---|
| **Date** | 30 Oct 2026 |
| **Phase** | 8 - Monitoring & Observability |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Metrics, logs, activity log, diagnostics

## Hands-on lab (20-30 min)

1. Enable diagnostics on a lab resource to Log Analytics (or note cost and skip retention)

## Commands / code

```bash
# Portal: Monitor -> Overview
# Enable Diagnostic settings on App Service / KV
```

## LinkedIn post (copy-paste)

```
If you cannot see it, you cannot fix it — Monitor is the flashlight, not the fix.

Day 71 of #100DaysOfAzureDevOps. Azure Monitor fundamentals.

Metrics, logs, activity log, diagnostic settings. A flashlight does not patch the hole. It tells you which wall is wet. I have been in war rooms where nobody had diagnostics enabled, so we argued from Portal screenshots and feelings. The fix was later. The seeing should have been first.

Enable diagnostics on a lab resource to Log Analytics — or note the cost and skip long retention. Activity log is the control-plane diary. Metrics are the pulse. Logs are the sentences. I am not building a SIEM today. I am turning on a light.

Patterns I keep seeing after a decade in delivery

1. Metrics vs logs vs activity
• Metrics: CPU, length of a queue, availability
• Logs: the story in rows
• Activity: who changed what in ARM

2. Diagnostics are opt-in more often than people think
• App Service / Key Vault / NSG — pick one lab resource
• Without diagnostic settings, the workspace is an empty room

3. Retention is a bill
• Lab: short retention or skip if cost is tight
• Infinite logs is not maturity. It is a storage hobby

4. Monitor is not the product fix
• A pretty chart of 500s is still 500s
• The flashlight's job is to end the argument about reality

What I am doing in today's lab

I am opening Monitor → Overview, enabling diagnostic settings on one lab resource (App Service or Key Vault) to a workspace if cost allows, and writing which signal I would use to detect "it is down." If I skip the workspace, I still map metrics vs logs vs activity on paper.

Turn on the light before you argue. Monitor does not heal. It stops the guessing.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-71-azure-monitor-fundamentals

Tomorrow: Log Analytics and KQL — AzureActivity, top operations, a saved query.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 71 — Azure Monitor Fundamentals` (max 58 chars)
3. Paste the text above (press **Enter** between sections so line breaks stay)

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5-10 real comments on other Azure/DevOps posts.

## Done checklist

- [ ] Learned the topic (docs or short video)
- [ ] Completed the lab steps
- [ ] Ran / saved the commands or code
- [ ] Published LinkedIn post
- [ ] Engaged with 5-10 community comments
- [ ] Deleted spare Azure resources if any (cost control)

## Tomorrow

**Log Analytics & KQL**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
