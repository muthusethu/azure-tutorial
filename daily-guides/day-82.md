# Day 82 - Pipeline Templates & Reusable YAML

| | |
|---|---|
| **Date** | 10 Nov 2026 |
| **Phase** | 9 - Advanced & Enterprise |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- templates, extends, parameters

## Hands-on lab (20-30 min)

1. Extract a `templates/build.yml` and reuse from main pipeline

## Commands / code

```bash
# templates/build.yml
parameters:
- name: projectPath
  type: string
steps:
- script: echo Building ${{ parameters.projectPath }}
```

## LinkedIn post (copy-paste)

```
Day 82 of #100DaysOfAzureDevOps

Copy-paste YAML is how organizations invent 14 slightly different ways to be broken

Today's topic: **Pipeline Templates & Reusable YAML**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Extensions & marketplace.

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

**Extensions & marketplace**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
