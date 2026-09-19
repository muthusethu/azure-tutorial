# Day 65 — Integrating Key Vault with Pipelines

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 7 - Security, Compliance & Governance |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Three doors: AzureKeyVault@2, linked variable groups, App Service Key Vault references — pick on purpose

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Door | Who fetches | What the pipeline log should show |
| --- | --- | --- |
| AzureKeyVault@2 | The job, via service connection with Secrets User on the vault | *** and a length you print. Never the letters |
| Variable group linked to KV | Library group authorized to the pipeline; ADO maps secret names to $(DemoSecret) | Same masking. Do not screenshot the Library value blade |
| Key Vault reference | App Service / Function app settings: @Microsoft.KeyVault(SecretUri=…) | Pipeline need not see it. The app identity needs Secrets User |
| Pipeline variable (plain) | You pasted the secret into ADO | A screenshot away from an incident. Not a door — a mailbox |
| ARM/Bicep getSecret | Deployment identity at deploy time | Fine for resource wiring; still not a YAML literal |

## Step-by-step lab

1. Grant the service connection's SP Key Vault Secrets User on the vault (data plane). Confirm lab-sc is the Azure RM connection, not the client ID pasted into YAML.
2. Pipelines → Library → Variable group kv-lab. Link secrets from the Key Vault (DemoSecret). Authorize this pipeline. That is door 2 — you may use it instead of (or in addition to) the task, but pick one as the proof.
3. Add AzureKeyVault@2 (door 1) with azureSubscription: lab-sc, KeyVaultName, SecretsFilter: DemoSecret, RunAsPreJob: true.
4. Next step: bash that prints only ${#VAL} with env VAL: $(DemoSecret). Read the log. If DemoSecret's letters appear, you failed — fix masking before sleep.
5. Write one sentence in docs/kv-pipeline-day65.md about Key Vault references (@Microsoft.KeyVault(SecretUri=…)) as door 3 for apps — pipeline may never see that value.
6. No Library screenshots of the secret value. Dummy value stays dummy.

## Done when

- [ ] Pipeline fetched DemoSecret at runtime via task and/or linked group
- [ ] Log shows length or ***, never the dummy letters as a souvenir
- [ ] Can name all three doors: task, linked group, app Key Vault reference
- [ ] SP has Secrets User; RG Contributor was not the fix

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-65-integrating-key-vault-with-pipelines
```

## Next

**Day 66** — Azure Policy — deny/audit so Finance is not your bouncer
