# Day 67 - Compliance Scanning in Pipelines

| | |
|---|---|
| **Date** | 26 Oct 2026 |
| **Phase** | 7 - Security, Compliance & Governance |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- SAST, dependency scanning, secret scanning

## Hands-on lab (20-30 min)

1. Add a secret scan task or GitHub push protection on mirror
2. Fail build on high vulnerabilities if tool available

## Commands / code

```bash
# Example mindset
# - dependency scan on restore
# - secret scan on repo
# - publish results as pipeline summary
```

## LinkedIn post (copy-paste)

```
Shift-left security means finding the fire in the kitchen, not on the evening news.

Day 67 of #100DaysOfAzureDevOps. Compliance scanning in pipelines.

SAST, dependency scanning, secret scanning. The kitchen is the pull request. The evening news is a leaked key in a public gist. I have seen both. Adding a scan that publishes a summary and fails on high if the tool allows it is the lab. Perfect coverage is not. A scan you ignore is décor.

Mindset: dependency scan on restore, secret scan on the repo, results as a pipeline summary. GitHub push protection on a mirror if that is what I have. Azure DevOps tasks vary; the habit does not.

Patterns I keep seeing

1. Secrets first — they are already a fire
• Scan the repo; fail if a key-shaped string lands
• Yesterday's Key Vault work is wasted if today's commit contains DemoSecret's cousin

2. Dependencies are the supply chain
• Restore/install is when you learn you pulled a CVE
• A lockfile without a scan is a list, not a control

3. SAST is the slow cousin that still matters
• If I have a task, I run it
• If I do not, I document the gap instead of pretending

4. Publish results where humans look
• Pipeline summary, not a log line 4,000 down
• Fail on high if the tool can; warnings-only is how kitchens burn politely

What I am doing in today's lab

I am adding a secret scan task or enabling push protection on a personal mirror, failing the build on high vulnerabilities if the tool allows, and capturing a summary. If the marketplace task is too spicy (Day 83 energy), I still run an open-source scanner in a script. The fire drill is the point.

Find it in the kitchen. Evening news is for people who skipped the PR.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-67-compliance-scanning-in-pipelines

Tomorrow: DevSecOps shift-left — Security stage before Deploy.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 67 — Compliance Scanning in CI` (max 58 chars)
3. Paste the text above (press **Enter** between sections so line breaks stay)

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5-10 real comments on other Azure/DevOps posts.

## Reminder — 2nd LinkedIn post (production track)

**Today you publish TWO separate LinkedIn posts.** The daily lesson above is post 1 only.

| | Post 1 — #100DaysOfAzureDevOps | Post 2 — #ProductionGradeAzure |
|---|-------------------------------|----------------------------------|
| **When** | ~10:00 IST | ~17:00–19:00 IST (after some engagement on post 1) |
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 22 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 22 of 33 (rewrite with your real experience)
- [ ] Record URLs in [`publish/production-grade/LINKS.md`](../publish/production-grade/LINKS.md)

Run: `python scripts/production_reminder.py`

## Done checklist

- [ ] Learned the topic (docs or short video)
- [ ] Completed the lab steps
- [ ] Ran / saved the commands or code
- [ ] Published LinkedIn post
- [ ] Engaged with 5-10 community comments
- [ ] Deleted spare Azure resources if any (cost control)

## Tomorrow

**DevSecOps shift-left**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
