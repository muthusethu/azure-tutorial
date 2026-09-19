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
Pipelines that need secrets should fetch them — not store them in variable screenshots.

Day 65 of #100DaysOfAzureDevOps. Integrating Key Vault with pipelines.

AzureKeyVault@2 pulls secrets at runtime. Variable groups can link to a vault. The log should show asterisks. The step that prints length, never the value, is how I prove the fetch without mailing the postcard. I have seen "debug: true" turn a masked secret into a lesson for the whole company.

Link a variable group to Key Vault, or use the task with SecretsFilter: DemoSecret. Echo the length. If the value appears, I failed the lab even if the pipeline is green.

Patterns I keep seeing

1. Fetch at runtime
• AzureKeyVault@2 with the service connection and vault name
• Do not copy the secret into a pipeline variable "so it is easier"

2. Linked variable groups are a second door
• Group linked to Key Vault for DemoSecret
• Same rule: no screenshots of the value blade

3. Print length, not letters
• A lab-safe proof
• echo of the secret is how you practice incidents

4. Masking is not magic if you concatenate
• Some log tricks leak
• Do not get clever. Length is enough

What I am doing in today's lab

I am linking a variable group to Key Vault (or using AzureKeyVault@2), running a step that prints the length of DemoSecret, and reading the log for leaks. Green plus a visible secret is a red lab. I fix that before I sleep.

Fetch. Mask. Never souvenir the value. The pipeline is not a scrapbook.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-65-integrating-key-vault-with-pipelines

Tomorrow: Azure Policy — require a tag so Finance does not hunt with spreadsheets.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 65 — Key Vault in Pipelines` (max 58 chars)
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

**Azure Policy**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
