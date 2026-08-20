# Day 62 - RBAC Deep Dive

| | |
|---|---|
| **Date** | 21 Oct 2026 |
| **Phase** | 7 - Security, Compliance & Governance |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Built-in roles, custom roles, scope

## Hands-on lab (20-30 min)

1. Assign yourself Reader on a lab RG via CLI
2. Compare Contributor vs Owner mentally

## Commands / code

```bash
az role assignment create --assignee <your-upn> \
  --role Reader --scope /subscriptions/<sub>/resourceGroups/rg-day62
```

## LinkedIn post (copy-paste)

```
Day 62 of #100DaysOfAzureDevOps

Owner is a flamethrower; prefer Reader/Contributor scoped to the RG, not the subscription

Today's topic: **RBAC Deep Dive**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Service connections & SPNs.

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

**Service connections & SPNs**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
