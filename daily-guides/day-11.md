# Day 11 - Git Fundamentals

| | |
|---|---|
| **Date** | 31 Aug 2026 |
| **Phase** | 2 - Azure Repos & Git Mastery |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Mental model: working tree -> staging -> commit -> remote
- init, clone, add, commit, branch, merge, status, log
- Book: Pro Git ch.1-3 (skim) https://git-scm.com/book/en/v2

## Hands-on lab (20-30 min)

1. In lab repo: create file `notes/day11.md`, commit, push
2. Create branch `feature/day11-notes`, edit, merge to main via local merge OR PR tomorrow
3. Practice `git status` and `git log --oneline -5` until muscle memory

## Commands / code

```bash
git status
git checkout -b feature/day11-notes
mkdir -p notes
echo "Day 11: Git mental model" > notes/day11.md
git add notes/day11.md
git commit -m "docs: day 11 git fundamentals notes"
git push -u origin feature/day11-notes
```

## LinkedIn post (copy-paste)

```
Day 11 of #100DaysOfAzureDevOps

Git is time travel with extra anxiety - commits are save points; branches are parallel universes you can still mess up

Today's topic: **Git Fundamentals**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Branching strategies.

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

**Branching strategies**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
