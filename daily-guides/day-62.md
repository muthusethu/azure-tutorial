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
Owner is a flamethrower; prefer Reader/Contributor scoped to the RG, not the subscription.

Day 62 of #100DaysOfAzureDevOps. RBAC deep dive.

Built-in roles, custom roles, scope. Scope is the part people skip. Contributor on a resource group is a job. Owner on a subscription is a flamethrower with a smile. I have spent ten years watching "just give them Owner so they are not blocked" become the reason a delete went wider than the incident.

Today I assign myself Reader on a lab RG via CLI and I compare Contributor vs Owner in my notes. Mentally. I do not need to assign Owner to feel the difference. I have seen it.

What I keep seeing

1. Scope is the verb
• Role + assignee + scope
• az role assignment create --role Reader --scope .../resourceGroups/rg-day62

2. Built-ins cover most honesty
• Reader: look
• Contributor: change resources, not grant roles
• Owner: including the ability to grant — the flamethrower

3. Custom roles are a last mile
• Literacy: they exist when built-ins are too wide or too narrow
• Lab: do not invent a custom role for a Reader test

4. Subscription-wide is rarely a lab need
• RG scope is the muscle memory I want
• Subscription Owner for a pipeline is a future incident

What I am doing in today's lab

I am assigning my user Reader on rg-day62 via Azure CLI, verifying I cannot create in that assignment's intent, and writing Contributor vs Owner in one paragraph I could say out loud. Then I remove the assignment if it is leftover noise. Flamethrowers stay on the wall.

Scope the badge to the floor. Owner at the building level is not speed. It is blast radius.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-62-rbac-deep-dive

Tomorrow: Service connections and service principals — robot employees, scoped badges.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 62 — Azure RBAC Deep Dive` (max 58 chars)
3. Paste the text above (press **Enter** between sections so line breaks stay)

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
