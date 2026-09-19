# Day 28 - Multi-stage YAML Pipelines

| | |
|---|---|
| **Date** | 17 Sep 2026 |
| **Phase** | 3 - Continuous Integration |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- dependsOn, conditions, matrix, parallel

## Hands-on lab (20-30 min)

1. Add matrix for Node 18/20 OR python versions
2. Add condition: succeeded() on deploy stage stub

## Commands / code

```bash
strategy:
  matrix:
    node18: { version: 18.x }
    node20: { version: 20.x }
steps:
- task: NodeTool@0
  inputs:
    versionSpec: $(version)
```

## LinkedIn post (copy-paste)

```
Matrix builds are cloning yourself across versions so "works on my Node" becomes "works on these Nodes."

Day 28 of #100DaysOfAzureDevOps. Multi-stage YAML pipelines.

A single-stage pipeline is a to-do list. Multi-stage is a workflow with memory: Build, then Test, then a deploy stub that should not run if Test failed. Matrix is the move that stops the most expensive sentence in engineering: it works on my version.

I have seen production Node 18 fail a library that staging ran on 20 because nobody asked CI to clone the job. strategy.matrix is not showing off. It is renting two of you for the price of YAML.

Patterns from real delivery

1. Stages need dependsOn and conditions
• Test depends on Build
• A deploy stub with condition: succeeded() so a red test does not "deploy" an echo to nowhere

2. Matrix is a version conversation in code
• node18: 18.x and node20: 20.x (or two Python versions)
• NodeTool@0 reads $(version) from the matrix — one job definition, two realities

3. Parallel is a gift with a bill
• Matrix jobs run in parallel if you have parallelism
• That is faster feedback and more hosted minutes — know which you are buying

4. A deploy stage can be a stub today
• echo is legal if the condition is real
• Wiring fake success on a failed build is how YAML lies in production later

What I am doing in today's lab

I am adding a matrix for Node 18/20 (or two Python versions) and a deploy-stage stub that only runs on succeeded(). Then I will fail a test on purpose once to watch the stub stay still. If it still runs, the condition is theater.

Clone the job across the versions you claim to support. Otherwise you support a laptop.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-28-multi-stage-yaml-pipelines

Tomorrow: Pipeline variables, groups, and secrets — envelopes, not postcards.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 28 — Multi-stage YAML Pipelines` (max 58 chars)
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
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 9 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 9 of 33 (rewrite with your real experience)
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

**Variables, groups & secrets**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
