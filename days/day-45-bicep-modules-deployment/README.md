# Day 45 — Bicep Modules & Deployment

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 5 - Infrastructure as Code |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Modules are boundaries. what-if is the dress rehearsal. A Delete you did not expect is an incident that has not happened yet

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Object | File | Call site |
| --- | --- | --- |
| Module | infra/modules/storage.bicep | params: prefix, sku, location |
| App | infra/main.bicep | module stg 'modules/storage.bicep' = { name: 'storage', params: { ... } } |
| what-if | CLI against main.bicep | az deployment group what-if — Create/Ignore/Modify/Delete |
| Deployment stacks | Literacy: track + prune | Not required for the lab apply |
| ARM still underneath | Compiled JSON per module | Errors still speak resource IDs |

## Step-by-step lab

1. Split storage into infra/modules/storage.bicep. main.bicep only calls the module.
2. az group create -n rg-day45-lab -l centralindia.
3. az deployment group what-if -g rg-day45-lab -f infra/main.bicep. Read every Delete/Modify line out loud.
4. If what-if matches intent: az deployment group create -g rg-day45-lab -f infra/main.bicep. Run what-if again — expect NoChange.
5. If a Delete appears that you did not expect: stop. Do not 'just apply'.
6. az group delete -n rg-day45-lab --yes --no-wait.

## Done when

- [ ] Storage lives in a module, not an inlined blob forever
- [ ] what-if run before create
- [ ] Second what-if is idle (idempotent) or you stopped on surprise Delete
- [ ] RG deleted

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-45-bicep-modules-deployment
```

## Next

**Day 46** — Terraform basics — init, plan, apply, destroy. State is memory; lose it and you argue with ghosts.
