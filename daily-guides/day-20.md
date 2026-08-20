# Day 20 - Mini Project + Recap (Phase 2)

| | |
|---|---|
| **Date** | 09 Sep 2026 |
| **Phase** | 2 - Azure Repos & Git Mastery |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Configure branch policy + full PR workflow on sample repo
- Publish Phase 2 recap

## Hands-on lab (20-30 min)

1. End-to-end: branch -> commit -> PR -> review notes -> squash merge -> delete branch
2. Confirm policies blocked a non-compliant PR once
3. Update README with 'How we use Git here' section

## Commands / code

```bash
git checkout -b feature/day20-recap
echo "## Git workflow\nSee docs/branching-strategy.md" >> README.md
git add README.md && git commit -m "docs: document git workflow"
git push -u origin feature/day20-recap
# Open PR in Azure DevOps, complete squash merge
```

## LinkedIn post (copy-paste)

```
Day 20 of #100DaysOfAzureDevOps

Phase 2 recap: Git is not 'save file' - it is collaboration with receipts, policies, and fewer 2am disasters

Today's topic: **Mini Project + Recap (Phase 2)**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Intro to Azure Pipelines.

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

**Intro to Azure Pipelines**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
