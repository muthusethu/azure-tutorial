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
Day 28 of #100DaysOfAzureDevOps

Matrix builds are cloning yourself across versions so 'works on my Node' becomes 'works on these Nodes'

Today's topic: **Multi-stage YAML Pipelines**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Variables, groups & secrets.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

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

**Variables, groups & secrets**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
