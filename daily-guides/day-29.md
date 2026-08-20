# Day 29 - Pipeline Variables, Groups & Secrets

| | |
|---|---|
| **Date** | 18 Sep 2026 |
| **Phase** | 3 - Continuous Integration |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Runtime vs compile-time vars
- Variable groups; Key Vault link preview

## Hands-on lab (20-30 min)

1. Create variable group `lab-common`
2. Store a dummy secret (not real passwords)
3. Reference $(myVar) in pipeline

## Commands / code

```bash
variables:
- group: lab-common
steps:
- script: echo "App name is $(appName)"
  displayName: Use variable
```

## LinkedIn post (copy-paste)

```
Day 29 of #100DaysOfAzureDevOps

Secrets in YAML are postcards - variable groups and Key Vault are envelopes

Today's topic: **Pipeline Variables, Groups & Secrets**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Phase 3 mini project.

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

**Phase 3 mini project**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
