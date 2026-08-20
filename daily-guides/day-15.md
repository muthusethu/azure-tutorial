# Day 15 - Advanced Git

| | |
|---|---|
| **Date** | 04 Sep 2026 |
| **Phase** | 2 - Azure Repos & Git Mastery |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Rebase vs merge, cherry-pick, squash, interactive rebase, conflicts
- Never rebase shared main; rebase your feature onto main

## Hands-on lab (20-30 min)

1. Create conflicting edits on purpose on two branches; resolve conflict
2. Practice squash merge via Azure DevOps PR settings (or local soft reset)
3. Write 5 lines: when you choose merge commit vs squash vs rebase

## Commands / code

```bash
git fetch origin
git checkout feature/day15
git rebase origin/main
# fix conflicts -> git add . -> git rebase --continue
git push --force-with-lease
```

## LinkedIn post (copy-paste)

```
Day 15 of #100DaysOfAzureDevOps

Rebase rewrites history; merge preserves the plot twists - choose based on whether your teammates are watching that timeline

Today's topic: **Advanced Git**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Git hooks & pre-commit.

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

**Git hooks & pre-commit**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
