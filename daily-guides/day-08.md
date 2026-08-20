# Day 8 - Azure Test Plans Basics

| | |
|---|---|
| **Date** | 28 Aug 2026 |
| **Phase** | 1 - Azure & DevOps Foundations |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Manual test cases, test plans vs suites, exploratory testing
- When freelancers actually use Test Plans vs automated tests in CI
- Docs: https://learn.microsoft.com/azure/devops/test/overview

## Hands-on lab (20-30 min)

1. Enable Test Plans if needed (Basic + Test Plans trial / included SKUs vary)
2. Create Test Plan 'Day08 Smoke' with one suite 'Portal checks'
3. Add 2 manual test cases: 'Login to Portal', 'Create RG via CLI'
4. Mark one Passed, one Blocked - note the workflow

## Commands / code

```bash
# Test case outline (paste into Azure DevOps Test Case steps):
# 1. Open portal.azure.com
# 2. Confirm correct personal directory
# 3. Expected: subscription visible, no work tenant
```

## LinkedIn post (copy-paste)

```
Day 8 of #100DaysOfAzureDevOps

A test plan is a shared checklist so 'it works on my machine' stops being a personality trait

Today's topic: **Azure Test Plans Basics**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Azure Artifacts.

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

**Azure Artifacts**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
