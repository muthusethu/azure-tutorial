# Day 89 — Scaling DevOps for Large Teams

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 9 - Advanced & Enterprise |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Platform engineering is DevOps that productized the paved road

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Capability | What a developer gets | You already have the seed |
| --- | --- | --- |
| App pipeline template | One YAML call, pinned SDK | Day 82 templates/build.yml |
| RG + budget bootstrap | Named RG + a budget alert | Day 77 Cost Management |
| Secret fetch | Key Vault reference, not a .env in Git | Phase 7 variable group / KV |
| Env promotion | Same artifact, approvals on staging/prod | Day 39 / Environments |
| Golden-path docs | How to open a PR that ships | docs/ that pipelines actually use |
| Optional sixth | Project scaffold (repo + pipeline file) | azure-100-labs as the example path |

## Step-by-step lab

1. List five platform capabilities in docs/platform-catalog-day89.md that you would want as the 50th developer.
2. Map each row to Azure DevOps: template path, Environment, variable group, budget, or docs file.
3. Include pipeline template, RG+budget bootstrap, golden-path docs, plus two you care about (secret fetch, env promotion).
4. Write one 'ticket theater' example you are replacing (e.g. 'please make a pipeline').
5. Add a versioning note: how a template change reaches consumers without a Friday surprise.
6. Do not invent a customer, a headcount chart, or a sales pitch. The catalog is the lab.

## Done when

- [ ] Five capabilities listed and mapped to Azure DevOps + templates
- [ ] Hypothetical catalog only — no logos, no customers
- [ ] docs/platform-catalog-day89.md committed
- [ ] Ticket theater vs paved road written once
- [ ] Posted the LinkedIn document

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-89-scaling-devops-for-large-teams
```

## Next

**Day 90** — Phase 9 recap — one template, two consumers, one green run each
