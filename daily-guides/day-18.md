# Day 18 - Migrating Repos to Azure Repos

| | |
|---|---|
| **Date** | 07 Sep 2026 |
| **Phase** | 2 - Azure Repos & Git Mastery |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Import from GitHub/GitLab; history preservation
- TFVC mention only - you will stay on Git

## Hands-on lab (20-30 min)

1. Create empty repo `imported-sample`
2. Import a small public GitHub repo OR push an existing local git history
3. Verify `git log` still shows old commits

## Commands / code

```bash
# Option A: Azure DevOps -> Repos -> Import
# Option B:
git clone --bare https://github.com/<user>/<small-repo>.git
cd <small-repo>.git
git push --mirror https://dev.azure.com/<org>/azure-100-labs/_git/imported-sample
```

## LinkedIn post (copy-paste)

```
Day 18 of #100DaysOfAzureDevOps

Migrations are moving apartments - history is the furniture; leave the broken IKEA shelf (secrets) behind

Today's topic: **Migrating Repos to Azure Repos**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Repo security.

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

**Repo security**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
