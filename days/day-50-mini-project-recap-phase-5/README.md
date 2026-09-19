# Day 50 — Mini Project + Recap (Phase 5)

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 5 - Infrastructure as Code |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Click-ops is a hobby. IaC is how you sleep: one tool, plan then apply from a pipeline, destroy when the demo ends

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Day | Object | Keep |
| --- | --- | --- |
| 41 | Declarative vs imperative; drift; one primary tool | ADR in docs/iac-why.md |
| 42–43 | ARM JSON literacy: apiVersion, -p @params, outputs | Broccoli you can read when deploys fail |
| 44–45 | Bicep resources, modules, what-if | Dress rehearsal before apply |
| 46–48 | Terraform verbs, azurerm, backend + lock + modules | State is memory; separate rg-tfstate |
| 49–50 | Plan artifact + gated apply in YAML | No laptop-as-prod; destroy after screenshot |

## Step-by-step lab

1. Provision one RG plus one storage account or a webapp skeleton using the Day 41 primary tool, from the Day 49 pipeline (brake on).
2. Save a screenshot of the green plan+apply run (no secrets, no work tenant). Note the deployment name or tf apply ID in docs/phase5-recap.md.
3. Write why you picked Bicep or Terraform in that recap. 'Both' is not a reason.
4. Destroy once via the same tool (pipeline apply of destroy or terraform destroy / az group delete). Confirm Portal is empty for that RG.
5. az group list -o table. Delete leftover rg-day42-lab … rg-day49-lab if any. rg-tfstate last, only if you are done with it.
6. Tomorrow is Docker — do not keep storage accounts as souvenirs.

## Done when

- [ ] plan+apply from pipeline once on personal Azure
- [ ] Destroy once; leftovers listed or gone
- [ ] Written reason for Bicep or Terraform (one)
- [ ] Recap stays personal: no employer or client names

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-50-mini-project-recap-phase-5
```

## Next

**Day 51** — Docker fundamentals — images, containers, layer cache. Same app, fewer 'works on my laptop' customs checks.
