# Day 6 - Setting Up an Azure DevOps Org

| | |
|---|---|
| **Date** | 26 Aug 2026 |
| **Phase** | 1 - Azure & DevOps Foundations |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Organizations, projects, process templates (Agile / Scrum / CMMI)
- Permissions: Project Collection Admins vs Contributors
- Keep this org personal-only

## Hands-on lab (20-30 min)

1. In org settings: check Overview, Users, Permissions
2. Create project `azure-100-labs` (this becomes your home project for 100 days)
3. Invite nobody from work. Use personal Microsoft account only
4. Set project description: 'Personal 100DaysOfAzureDevOps labs - views my own'

## Commands / code

```bash
# Azure DevOps CLI (optional install: az extension add --name azure-devops)
az extension add --name azure-devops
az devops configure --defaults organization=https://dev.azure.com/<your-org> project=azure-100-labs
az devops project list -o table
```

## LinkedIn post (copy-paste)

```
Day 6 of #100DaysOfAzureDevOps

Your Azure DevOps org is a gym membership - empty projects don't build muscle; daily reps do

Today's topic: **Setting Up an Azure DevOps Org**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Azure Boards deep dive.

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

**Azure Boards deep dive**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
