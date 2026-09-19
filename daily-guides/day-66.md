# Day 66 - Azure Policy & Governance

| | |
|---|---|
| **Date** | 25 Oct 2026 |
| **Phase** | 7 - Security, Compliance & Governance |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Policy definitions, initiatives, compliance
- Skip Blueprints - retired; use Policy + landing zone ideas

## Hands-on lab (20-30 min)

1. Assign a built-in policy like 'Require a tag on resource groups' to lab subscription/RG
2. See compliance blade

## Commands / code

```bash
# Portal: Policy -> Assignments -> Assign policy
# Or: az policy assignment create ...
```

## LinkedIn post (copy-paste)

```
Policy is the grown-up saying "no untagged RGs" so Finance does not hunt you with spreadsheets.

Day 66 of #100DaysOfAzureDevOps. Azure Policy and governance.

Policy definitions, initiatives, compliance. Blueprints are retired; I am not learning a dead product to sound enterprise. Policy plus landing-zone ideas are the current sentence. A built-in like "require a tag on resource groups" assigned to the lab subscription or RG is enough to see the compliance blade light up.

I have watched untagged resource groups become a quarterly forensic exercise. Policy is how you stop playing detective with Cost Management exports.

What I keep seeing

1. Built-ins before custom JSON
• Require a tag on resource groups
• Assign, then create an RG without the tag and watch deny or audit

2. Audit vs deny is a culture choice
• Audit: you see sin
• Deny: sin cannot land
• Labs can deny. Production often starts with audit so you do not break a factory

3. Initiatives are bundles
• Literacy: many policies as one assignment
• Lab: one policy, one assignment, one compliance look

4. Scope again
• Assignment at MG / subscription / RG
• A policy at the wrong scope is a rumor that never fires

What I am doing in today's lab

I am assigning a built-in "require a tag on resource groups" to the lab subscription or a lab RG, opening the compliance blade, and creating a test RG that should fail or show non-compliant. Then I clean up so Policy does not nag a junk RG forever.

Let Policy be the grown-up. Spreadsheets are a slow bouncer.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-66-azure-policy-governance

Tomorrow: Compliance scanning in pipelines — SAST, deps, secrets.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 66 — Azure Policy & Governance` (max 58 chars)
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

**Compliance scanning in pipelines**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
