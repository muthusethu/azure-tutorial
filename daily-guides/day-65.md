# Day 65 - Integrating Key Vault with Pipelines

| | |
|---|---|
| **Date** | 24 Oct 2026 |
| **Phase** | 7 - Security, Compliance & Governance |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Key Vault task; variable groups linked to KV

## Hands-on lab (20-30 min)

1. Link variable group to Key Vault
2. Print length of secret in pipeline, never the value

## Commands / code

```bash
- task: AzureKeyVault@2
  inputs:
    azureSubscription: <sc>
    KeyVaultName: <uniquekv>
    SecretsFilter: DemoSecret
- script: echo "Secret length ${{#DemoSecret}}"  # use correct macro syntax in ADO
```

## LinkedIn post (copy-paste)

```
Day 65 of #100DaysOfAzureDevOps

Pipelines that need secrets should fetch them - not store them in variable screenshots

Today's topic: **Integrating Key Vault with Pipelines**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Azure Policy.

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

**Azure Policy**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
