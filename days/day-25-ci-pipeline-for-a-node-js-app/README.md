# Day 25 — CI Pipeline for a Node.js App

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 3 - Continuous Integration |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

npm ci + Cache@2 — stop paying hosted minutes to watch paint dry

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Step | Task / command | Why |
| --- | --- | --- |
| Runtime pin | NodeTool@0 versionSpec 20.x | Not whatever ubuntu-latest shipped this week |
| Cache key | Cache@2 key: npm | $(Agent.OS) | package-lock.json | Restore node_modules when lockfile unchanged |
| Install | npm ci (not npm install) | Fails if lockfile is out of sync — that is a feature |
| Test | npm test | Even a one-line Node assert counts |
| Optional build | npm run build if you have it | Skip if the lab app is a script |
| Lockfile | package-lock.json committed | Cache@2 key is useless without it |

## Step-by-step lab

1. mkdir src/sample-node && create package.json with name sample-node, scripts.test running node --test or a one-liner. npm install locally to produce package-lock.json.
2. Confirm .gitignore has node_modules/. Commit package.json + package-lock.json only on feature/day25-node-ci.
3. Add pipelines/node-ci.yml with NodeTool@0, Cache@2, npm ci, npm test.
4. Create a pipeline pointing at pipelines/node-ci.yml. Run it twice: first run may be a cache miss; second should hit Cache@2 if lockfile unchanged.
5. Open the Cache@2 log: look for Cache restored from / Cache saved. That is the receipt.
6. PR + squash merge. Do not put a PAT in .npmrc.
7. Optional: Connect to feed day09-packages later — not required for the hello test.

## Done when

- [ ] src/sample-node has package.json + package-lock.json; node_modules is gitignored
- [ ] Pipeline uses NodeTool@0 20.x and npm ci (not npm install)
- [ ] Cache@2 key includes the lockfile; second run can restore
- [ ] npm test is green on ubuntu-latest

## LinkedIn

Post draft: [`../../daily-guides/day-25.md`](../../daily-guides/day-25.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-25-ci-pipeline-for-a-node-js-app
```

## Next

**Day 26** — CI for Python
