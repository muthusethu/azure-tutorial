# Day 12 - Branching Strategies

| | |
|---|---|
| **Date** | 01 Sep 2026 |
| **Phase** | 2 - Azure Repos & Git Mastery |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Git Flow vs GitHub Flow vs trunk-based development
- When teams should recommend trunk-based + short PRs
- Article: https://trunkbaseddevelopment.com/

## Hands-on lab (20-30 min)

1. Write a 1-page ADR in repo: `docs/branching-strategy.md` choosing one strategy for this lab
2. Document: main protected, feature/* short-lived, no develop branch for this project

## Commands / code

```bash
# docs/branching-strategy.md
# Decision: GitHub Flow (trunk-based lite)
# - main is always deployable
# - feature/* branches < 2 days
# - PR required; squash merge
# - No long-lived release branches in this lab
```

## LinkedIn post (copy-paste)

```
Day 12 of #100DaysOfAzureDevOps

Git Flow is a wedding seating chart; trunk-based is a food truck - pick complexity that matches team size

Today's topic: **Branching Strategies**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Azure Repos setup.

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

**Azure Repos setup**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
