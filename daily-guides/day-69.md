# Day 69 - Secure Pipeline Design

| | |
|---|---|
| **Date** | 28 Oct 2026 |
| **Phase** | 7 - Security, Compliance & Governance |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Least privilege agents, approvals, protected branches

## Hands-on lab (20-30 min)

1. Audit: who can edit pipelines? who can approve prod?
2. Remove any broad Owner SPN from lab if over-permissioned

## Commands / code

```bash
# Checklist
# - separate service connections per env
# - no secret echo
# - main locked
# - prod approval required
```

## LinkedIn post (copy-paste)

```
A secure pipeline is boring on purpose — drama belongs in Netflix, not release logs.

Day 69 of #100DaysOfAzureDevOps. Secure pipeline design.

Least privilege agents, approvals, protected branches. The audit is personal: who can edit pipelines? who can approve prod? Is there a broad Owner SPN leftover from a lab? I have reviewed pipelines that could push to production from a feature branch with a PAT that never expired. That is a series. It should not be my series.

Checklist: separate service connections per env, no secret echo, main locked, prod approval required. Boring. Correct.

Patterns I keep seeing

1. Who can edit YAML is who can ship
• If Contributors can rewrite the prod stage, approvals are a speed bump around a hole
• Branch policies on main: PR, required checks

2. Separate connections per environment
• Dev connection cannot touch prod RG
• One connection to rule them all is Day 63's master key again

3. Agents are part of the threat model
• Hosted is isolated-enough for these labs
• Self-hosted with org-wide access is a lateral-movement hobby

4. No secret echo, still
• system.debug on a secret job is how Netflix writes itself
• I re-check Day 65 habits

What I am doing in today's lab

I am auditing who can edit pipelines and who can approve prod, removing any over-permissioned Owner SPN from the lab if I created one, locking main if it is not locked, and ticking the checklist in a file. If I cannot answer "who can ship," I do not have a secure pipeline. I have hope.

Bore the attacker. Bore your future self. Keep the drama in fiction.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-69-secure-pipeline-design

Tomorrow: Phase 7 mini project — secret not in YAML, policy visible, approvals on.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 69 — Secure Pipeline Design` (max 58 chars)
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

**Phase 7 mini project**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
