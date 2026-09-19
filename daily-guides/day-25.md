# Day 25 - CI Pipeline for a Node.js App

| | |
|---|---|
| **Date** | 14 Sep 2026 |
| **Phase** | 3 - Continuous Integration |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- npm ci/build/test
- Cache node_modules

## Hands-on lab (20-30 min)

1. Add tiny Node app under `/src/sample-node`
2. Pipeline with Cache@2 and npm test

## Commands / code

```bash
# src/sample-node/package.json - minimal
# { "name": "sample-node", "scripts": { "test": "node -e \"console.log('ok')\"" } }
steps:
- task: NodeTool@0
  inputs: { versionSpec: 20.x }
- task: Cache@2
  inputs:
    key: 'npm | "$(Agent.OS)" | src/sample-node/package-lock.json'
    path: src/sample-node/node_modules
- script: |
    cd src/sample-node
    npm ci
    npm test
  displayName: npm ci & test
```

## LinkedIn post (copy-paste)

```
Node CI without caching is watching paint dry while paying Microsoft for the privilege.

Day 25 of #100DaysOfAzureDevOps. CI pipeline for a Node.js app.

npm install on a cold agent is a small tax that becomes a lifestyle. I have sat through pipelines that spent four minutes downloading the same packages the team downloaded an hour earlier. Cache@2 is not a micro-optimization for a conference talk. It is how you stop paying hosted-agent minutes to re-download left-pad's entire family tree.

The other habit: npm install in CI when the lockfile exists. npm ci is the one that respects the lock. If CI uses npm install, you do not have a lockfile. You have a suggestion.

What usually goes wrong

1. npm ci, not npm install, when package-lock.json exists
• ci fails if the lock is stale — that is a feature
• install will quietly mutate the graph and still go green

2. Cache the right key
• Cache@2 key: npm | Agent.OS | package-lock.json
• Cache node_modules (or the npm cache) — not the entire repo
• Wrong key = cache never hits and you still wait

3. Pin Node like you pin .NET
• NodeTool@0 with 20.x (or the engines field you actually mean)
• ubuntu-latest Node floating is how "works on my 18" becomes "fails on 22"

4. A tiny app is enough
• Today's sample-node can have a test script that prints ok
• The point is the pipeline shape, not a fake product

What I am doing in today's lab

I am adding a tiny Node app under /src/sample-node, wiring NodeTool@0, Cache@2 keyed off package-lock.json, then npm ci and npm test. If the cache hits, the log should show it. If it misses, I want to know why, not shrug.

Pay for compute that does work. Do not pay for compute that re-downloads the internet.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-25-ci-pipeline-for-a-node-js-app

Tomorrow: CI for Python — pip, ruff, pytest on a tiny sample.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 25 — CI Pipeline for a Node.js App` (max 58 chars)
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
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 8 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 8 of 33 (rewrite with your real experience)
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

**CI for Python**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
