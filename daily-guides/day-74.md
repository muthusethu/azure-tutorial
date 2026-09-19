# Day 74 - Alerts & Action Groups

| | |
|---|---|
| **Date** | 02 Nov 2026 |
| **Phase** | 8 - Monitoring & Observability |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Metric/log alerts, action groups

## Hands-on lab (20-30 min)

1. Create action group email-to-self
2. Alert on CPU or availability test

## Commands / code

```bash
# Monitor -> Alerts -> Create alert rule
# Action group: email yourself (personal)
```

## LinkedIn post (copy-paste)

```
Alerts without action groups are screams into the void — polite, useless.

Day 74 of #100DaysOfAzureDevOps. Alerts and action groups.

A metric alert that emails nobody is performance art. Action groups are the destination: email to myself for the lab. I have inherited alert rules that fired for a year into a disabled mailbox. Polite screams.

Create an action group. Create an alert on CPU, availability test, or a log query I can force. Then fire it once if I can. An alert you have never received is a rumor about the future.

What I keep seeing

1. Action group first
• Email yourself (personal)
• SMS/webhook later — today is proof of delivery

2. Alert on something I can provoke
• Availability test on a URL I control, or CPU on a tiny SKU
• A 5xx alert on an app with no traffic will never graduate from theory

3. Severity is a language
• Sev 0 for "wake me"
• If everything is Sev 0, nothing is

4. Noise trains people to mute
• One alert that fires cleanly beats ten that flap
• I will delete the lab alert when I delete the resource

What I am doing in today's lab

I am creating an action group that emails my personal address, creating one alert rule, and trying to receive it. Monitor → Alerts → Create alert rule. If the email never arrives, the lab is not done. I check spam, then the action group.

Scream at an inbox that exists. The void does not page.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-74-alerts-action-groups

Tomorrow: Dashboards and workbooks — three tiles, not a novel.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 74 — Alerts & Action Groups` (max 58 chars)
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

**Dashboards & workbooks**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
