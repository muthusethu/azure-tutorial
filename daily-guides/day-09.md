# Day 9 - Azure Artifacts

| | |
|---|---|
| **Date** | 29 Aug 2026 |
| **Phase** | 1 - Azure & DevOps Foundations |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Feeds, views, upstream sources (NuGet, npm, Maven, Python)
- Why private feeds beat 'copy DLLs in email'
- Docs: https://learn.microsoft.com/azure/devops/artifacts/start-using-azure-artifacts

## Hands-on lab (20-30 min)

1. Create feed `day09-packages` (project-scoped)
2. Enable upstream sources for nuget.org and npmjs (if prompted)
3. Note feed URL - you will use it in Phase 3 CI
4. Do not publish secrets. Empty feed is fine for today

## Commands / code

```bash
# Later (Phase 3) you will connect like:
# nuget.config -> packageSources -> your Azure Artifacts feed URL
# For today: copy Feed settings -> Connect to feed -> save URL in notes
```

## LinkedIn post (copy-paste)

```
Day 9 of #100DaysOfAzureDevOps

Artifacts are the pantry - Pipelines cook dinner; without a feed you keep re-buying the same flour every build

Today's topic: **Azure Artifacts**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Mini project + recap.

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

**Mini project + recap**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
