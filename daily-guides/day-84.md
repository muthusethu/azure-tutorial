# Day 84 - Migrating Jenkins to Azure Pipelines

| | |
|---|---|
| **Date** | 12 Nov 2026 |
| **Phase** | 9 - Advanced & Enterprise |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Map Jenkinsfile concepts to YAML

## Hands-on lab (20-30 min)

1. Translate a sample Jenkinsfile (agent, stages, post) into Azure YAML on paper

## Commands / code

```bash
# Jenkins stage -> Azure stage/job
# credentials -> variable group / Key Vault
# agents -> pools
```

## LinkedIn post (copy-paste)

```
Jenkins migrations succeed when you migrate pipelines, not nostalgia.

Day 84 of #100DaysOfAzureDevOps. Migrating Jenkins to Azure Pipelines.

Jenkinsfile has a shape: agent, stages, post, credentials. Azure YAML has a mapping, not a religion. I have seen migrations that rebuilt the Jenkins UI in Azure DevOps because someone missed the blue ball. Nostalgia. The work is mapping stages to jobs, credentials to variable groups or Key Vault, agents to pools.

Today is paper: translate a sample Jenkinsfile. I am not standing up Jenkins. I am proving I can leave it without lying about feature parity.

What I keep seeing

1. agent → pool
• Jenkins label vs vmImage or a self-hosted pool
• "We need the same snowflake agent" might be true; it might be nostalgia

2. stages → stages/jobs
• post { always } becomes a job condition or a later stage
• Do not require identical names. Require identical guarantees

3. credentials → envelopes
• Jenkins credential store is not a reason to put secrets in YAML
• Variable group / Key Vault from Phase 7

4. Plugins are the trap
• Every Jenkins plugin is a negotiation
• If the plugin was the product, write that down — do not hide it in "the YAML is not ready"

What I am doing in today's lab

I am translating a sample Jenkinsfile (agent, stages, post) into Azure YAML on paper: stage→job, credentials→group/Key Vault, agents→pools. If I do not have an old Jenkinsfile, I write a tiny one first so the mapping is real, not abstract.

Migrate the guarantees. Leave the blue ball to memory. Nostalgia does not compile.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-84-migrating-jenkins-to-azure-pipelines

Tomorrow: Hybrid and multi-cloud CI/CD — insurance and complexity, survey only.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 84 — Jenkins to Azure Pipelines` (max 58 chars)
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

**Hybrid & multi-cloud CI/CD**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
