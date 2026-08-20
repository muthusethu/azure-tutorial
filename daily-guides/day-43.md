# Day 43 - ARM Parameters & Outputs

| | |
|---|---|
| **Date** | 02 Oct 2026 |
| **Phase** | 5 - Infrastructure as Code |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Parameter files, variables, nested templates

## Hands-on lab (20-30 min)

1. Add parameters file; output storage endpoint
2. Skim only if you chose Terraform as primary

## Commands / code

```bash
az deployment group create -g rg-day43 -f main.json -p @main.parameters.json
```

## LinkedIn post (copy-paste)

```
Day 43 of #100DaysOfAzureDevOps

Parameters are the dials; hardcoding names is how labs become landfills

Today's topic: **ARM Parameters & Outputs**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Bicep fundamentals.

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

**Bicep fundamentals**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
