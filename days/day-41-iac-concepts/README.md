# Day 41 — IaC Concepts

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 5 - Infrastructure as Code |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

If it is not in code, it is a rumor. Declarative desired state, idempotent apply, drift is the Portal's revenge

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Style | What you write | Engine |
| --- | --- | --- |
| Imperative script | az group create; az storage account create … | You. Second run often duplicates or errors |
| Declarative ARM/Bicep | resources: desired JSON/Bicep | ARM control plane. Deployment history in Azure |
| Declarative Terraform | resource "azurerm_*" | Plan/apply + state file mapping address → Azure ID |
| Click-ops | Portal clicks | A rumor. No PR, no diff, no rollback of intent |
| Idempotency test | Apply twice | Same world. If you get two of everything, it was a script |

## Step-by-step lab

1. Write docs/iac-why.md: one drift you have actually seen (SKU bump, extra firewall rule, lock only in prod) — keep it generic, no client names.
2. Decision record in the same file: Tool: Bicep | Terraform. Reason: one paragraph. Not 'both'.
3. Add a two-line glossary: declarative = desired state; idempotent = apply twice, one world.
4. List the complementary tool as literacy only (ARM JSON if Bicep; Bicep sample if Terraform).
5. Do not deploy anything yet. Day 42 is broccoli (ARM). Day 44/46 is the primary track.
6. Commit the ADR on a personal branch. Invite nobody.

## Done when

- [ ] Primary tool chosen with a reason, not a personality
- [ ] Drift example written without employer/client names
- [ ] Can define declarative vs imperative in one sentence each
- [ ] No Azure spend today

## LinkedIn

Post draft: [`../../daily-guides/day-41.md`](../../daily-guides/day-41.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-41-iac-concepts
```

## Next

**Day 42** — ARM templates basics — $schema, apiVersion, az deployment group create. Literacy, not a love affair.
