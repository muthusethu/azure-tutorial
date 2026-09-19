# Day 63 - Service Connections & Service Principals

| | |
|---|---|
| **Date** | 22 Oct 2026 |
| **Phase** | 7 - Security, Compliance & Governance |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- SPNs, workload identity federation, least privilege

## Hands-on lab (20-30 min)

1. Create Azure RM service connection in Azure DevOps (automatic)
2. Prefer WIF over long-lived secrets when possible

## Commands / code

```bash
# Project Settings -> Service connections -> Azure Resource Manager
# Workload identity federation (manual/automatic)
```

## LinkedIn post (copy-paste)

```
Service principals are robot employees — give them a badge scoped to one floor, not master keys.

Day 63 of #100DaysOfAzureDevOps. Service connections and service principals.

Azure DevOps needs an identity to talk to Azure. That robot used to be a secret-based service principal that someone rotated never. Workload identity federation (WIF) is how the robot proves itself without a password in a drawer. I have rotated expired SPN secrets at the worst possible hour. I would like fewer of those hours.

Project Settings → Service connections → Azure Resource Manager. Automatic is fine. Prefer WIF over long-lived secrets when the UI offers it. Least privilege: the connection should not be Owner.

Patterns I keep seeing

1. The connection is the badge
• Pipelines never get my user password
• A service connection with Contributor on one RG is a floor badge

2. WIF over client secrets
• Federation: Azure DevOps presents a token, Entra trusts it
• Long-lived secrets are postcards with a delayed explosion

3. Automatic vs manual
• Automatic is fast and often wider than you think — I will look at what it created
• Manual if I need a tighter SPN I created myself

4. One connection per environment later
• A single prod-or-everything connection is a master key with a friendly name
• Day 69 will be rude about that. Today I start the habit

What I am doing in today's lab

I am creating an Azure RM service connection (automatic is OK), preferring workload identity federation when possible, and checking the role it received. If it is Owner on the subscription, I treat that as a finding, not a convenience.

Robots need badges, not master keys. If it can deploy, it should not also be able to re-own the subscription.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-63-service-connections-service-principals

Tomorrow: Azure Key Vault — hotel safe, not repo chat history.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 63 — Service Connections & SPs` (max 58 chars)
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

**Azure Key Vault**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
