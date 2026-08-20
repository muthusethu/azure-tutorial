# Day 10 - Mini Project + Recap (Phase 1)

| | |
|---|---|
| **Date** | 30 Aug 2026 |
| **Phase** | 1 - Azure & DevOps Foundations |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Stand up a complete Azure DevOps project end-to-end
- Recap Phase 1 for LinkedIn (what stuck, what was confusing)

## Hands-on lab (20-30 min)

1. Ensure project `azure-100-labs` has: 1 Epic, backlog items, empty Git repo, Artifacts feed
2. Initialize repo with README (see code)
3. Create dashboard widget: query chart of your Phase 1 stories
4. Delete leftover RGs from Days 1-3 if any still exist

## Commands / code

```bash
# In azure-100-labs -> Repos -> Files -> Initialize with README
# Or locally:
git clone https://dev.azure.com/<org>/azure-100-labs/_git/azure-100-labs
cd azure-100-labs
echo "# Azure 100 Labs" > README.md
echo "Personal learning repo for #100DaysOfAzureDevOps" >> README.md
git add README.md && git commit -m "docs: bootstrap lab repo" && git push
```

## LinkedIn post (copy-paste)

```
Day 10 of #100DaysOfAzureDevOps

Phase 1 recap: cloud models, Portal/CLI, ARM, CALMS/DORA, and the five Azure DevOps hubs - foundations before pipelines

Today's topic: **Mini Project + Recap (Phase 1)**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Git fundamentals.

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

**Git fundamentals**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
