# Day 16 - Git Hooks & Pre-commit Checks

| | |
|---|---|
| **Date** | 05 Sep 2026 |
| **Phase** | 2 - Azure Repos & Git Mastery |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Client-side hooks; pre-commit framework; commit message conventions
- https://pre-commit.com/

## Hands-on lab (20-30 min)

1. Add a simple pre-commit config OR a sample `commit-msg` hook that requires 'dayNN:' prefix for this lab
2. Make a bad commit message and watch it fail (then fix)

## Commands / code

```bash
# .git/hooks/commit-msg (sample; chmod +x on mac/linux)
#!/bin/sh
grep -qE '^(docs|feat|fix|chore|day)(\(.+\))?: .+' "$1" || {
  echo "Commit message must look like: feat: short description"
  exit 1
}
```

## LinkedIn post (copy-paste)

```
Day 16 of #100DaysOfAzureDevOps

Hooks are the bouncer at the commit club - ugly messages do not get past the velvet rope

Today's topic: **Git Hooks & Pre-commit Checks**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Fork workflows & permissions.

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

**Fork workflows & permissions**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
