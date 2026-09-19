# Day 41 - IaC Concepts

| | |
|---|---|
| **Date** | 30 Sep 2026 |
| **Phase** | 5 - Infrastructure as Code |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Declarative vs imperative
- Idempotency, drift

## Hands-on lab (20-30 min)

1. Write `docs/iac-why.md` with examples of drift you have seen
2. Pick primary tool for Phase 5: **Bicep OR Terraform** (one)

## Commands / code

```bash
# Decision record
# Tool: Terraform | Bicep
# Reason: ________
```

## LinkedIn post (copy-paste)

```
If it is not in code, it is a rumor — IaC turns "someone clicked prod" into a diff.

Day 41 of #100DaysOfAzureDevOps. IaC concepts.

Click-ops is how every environment I have inherited started: a portal session, a naming convention that lasted three resources, and a story about "the storage account that was always there." If it is not in code, it is a rumor. Infrastructure as Code is how the rumor becomes a pull request.

Declarative vs imperative. Idempotency. Drift. Today I write why IaC, pick a primary tool for Phase 5 — Bicep or Terraform, one, not both as a personality — and I write down drift I have actually seen: a firewall rule someone "just added," a SKU bump, a lock that existed only in production.

Patterns I keep seeing

1. Declarative says what; imperative says how
• Bicep/ARM/Terraform: desired state, the engine converges
• A shell script of az commands is a recipe that forgets deletions

2. Idempotency is the adult test
• Apply twice, same world
• If the second apply creates a second of everything, you have a script, not IaC

3. Drift is the portal's revenge
• Someone clicked, the file did not change, production is now a fork
• What-if / plan exist to see the fork before you overwrite a human's surprise

4. One primary tool for this phase
• Bicep if I want Azure-native and ARM literacy
• Terraform if I want state, modules, and a tool that travels
• Both as "I will learn everything" is how I learn neither

What I am doing in today's lab

I am writing docs/iac-why.md with examples of drift I have seen, and a decision record: Tool: Terraform | Bicep, Reason: ______. I will still touch the other tool for literacy. The primary is the one that will provision the mini project.

Rumors do not rollback. Diffs do. Put the environment in a file.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-41-iac-concepts

Tomorrow: ARM templates basics — deploy a tiny Storage Account, then delete the RG.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 41 — Infrastructure as Code Concepts` (max 58 chars)
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

**ARM templates basics**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
