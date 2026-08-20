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
Day 25 of #100DaysOfAzureDevOps

Node CI without caching is watching paint dry while paying Microsoft for the privilege

Today's topic: **CI Pipeline for a Node.js App**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: CI for Python.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no "DM me for freelance".
- After posting: leave 5-10 real comments on other Azure/DevOps posts.

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
