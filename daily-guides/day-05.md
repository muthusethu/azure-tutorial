# Day 5 — Azure DevOps Services Overview

| | |
|---|---|
| **Date** | 25 Aug 2026 |
| **Phase** | 1 — Azure & DevOps Foundations |
| **Time box** | 60–90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Understand what each Azure DevOps service does, how they connect, and where your daily work starts. Publish Day 5 lesson on LinkedIn with the PDF handout.

## Learn (20–30 min)

- Five core services: Boards, Repos, Pipelines, Test Plans, Artifacts
- Typical flow: plan work -> commit code -> run CI/CD -> validate quality -> consume package
- Azure DevOps and GitHub can complement each other (you can use both)
- Docs: <https://learn.microsoft.com/azure/devops/user-guide/what-is-azure-devops>

## Hands-on lab (20–30 min)

1. Create a personal org at <https://dev.azure.com> (example: `yourname-100days`)
2. Create project `day05-overview` (Agile process, private)
3. Open each hub once: Boards -> Repos -> Pipelines -> Test Plans -> Artifacts
4. Create one sample work item in Boards
5. Initialize repo in Repos with a README
6. Open Pipelines and walk through New Pipeline wizard (no run required today)

## Commands / code

```bash
# No CLI required today.
# Useful bookmarks:
# https://dev.azure.com/<your-org>
# https://dev.azure.com/<your-org>/day05-overview
#
# Hubs:
# Boards | Repos | Pipelines | Test Plans | Artifacts
```

## LinkedIn post (copy-paste)

**Important:** After pasting into LinkedIn, press Enter between sections so line breaks stay visible.

```
Day 5 of #100DaysOfAzureDevOps

Yesterday was CALMS and DORA.
Today is the control room: Azure DevOps services.

A lot of beginners open Azure DevOps and feel like it is one giant product.
In practice, it is five focused services that work as one delivery system:

• Boards — plan and track work
• Repos — store and review code
• Pipelines — build, test, and deploy
• Test Plans — structure manual/exploratory testing
• Artifacts — manage package feeds

Simple flow:
Plan -> Code -> Build/Deploy -> Validate -> Distribute

Lab today:
Created a personal org, project, opened all five hubs,
created one work item, initialized repo, and explored pipeline setup.

One-liner:
Azure DevOps is not “one tool.”
It is a connected workflow from idea to production.

Tomorrow: Setting up an Azure DevOps organization in a clean, repeatable way.

(Document attached: Day 5 Azure DevOps Services handout PDF)

Lab notes + PDF also here:
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-05-azure-devops-services

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### Attach with the post (PDF handout)

Attach this document on LinkedIn (document / PDF upload):

- [`../days/day-05-azure-devops-services/handout.pdf`](../days/day-05-azure-devops-services/handout.pdf)

**How to post on LinkedIn:** Start a post -> **document** icon -> upload `handout.pdf` -> paste the text above -> title e.g. `Day 5 — Azure DevOps Services Overview`.

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5–10 real comments on other Azure/DevOps posts.

## Done checklist

- [ ] Learned the topic (docs or short video)
- [ ] Completed the lab steps
- [ ] Saved the hub map (Boards/Repos/Pipelines/Test Plans/Artifacts)
- [ ] Published LinkedIn post with PDF handout
- [ ] Engaged with 5–10 community comments
- [ ] Deleted spare Azure resources if any (cost control)

## Tomorrow

**Setting up an Azure DevOps organization**

---

*Personal learning guide — views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
