# Day 68 - DevSecOps - Shift-left Security

| | |
|---|---|
| **Date** | 27 Oct 2026 |
| **Phase** | 7 - Security, Compliance & Governance |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Embed gates early

## Hands-on lab (20-30 min)

1. Add a pipeline stage `Security` before `Deploy`
2. Document fail criteria

## Commands / code

```bash
stages: [Build, Security, Deploy]
# Security job exits non-zero on critical CVEs
```

## LinkedIn post (copy-paste)

```
Security as a final boss stage is how you ship late — put checks next to the commit.

Day 68 of #100DaysOfAzureDevOps. DevSecOps — shift-left security.

A stage named Security that runs after everyone wanted to go home is a boss fight. People skip it, mark it optional, or "temporarily" continueOnError. Shift-left means Build, then Security, then Deploy — and Security exits non-zero on critical CVEs so Deploy never starts.

I have been on trains where security was a weekly meeting. The meeting always lost to the release date. A pipeline stage with fail criteria in a doc is ruder and kinder.

What I keep seeing

1. Order is a control
• stages: Build, Security, Deploy
• Security that runs in parallel with Deploy is a race, not a gate

2. Fail criteria are written
• Critical CVE = fail
• Secret detected = fail
• Medium = warn in the lab if I must, not silent

3. continueOnError is a confession
• If Security has it, I do not have shift-left
• I have a dashboard of regret

4. Left means next to the commit
• PR validation includes the security job when I can
• Main-only scans are how badness waits for merge

What I am doing in today's lab

I am adding a pipeline stage Security before Deploy, documenting fail criteria in a short markdown file, and running once with a forced failure (or a dummy critical) to watch Deploy stay still. If Deploy still runs, the dependsOn/condition is theater.

Do not save security for the final boss. Put it next to the commit so the release date cannot vote it off the island.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-68-devsecops-shift-left-security

Tomorrow: Secure pipeline design — least privilege, locked main, no secret echo.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 68 — DevSecOps Shift-left Security` (max 58 chars)
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

**Secure pipeline design**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
