# Day 62 — RBAC Deep Dive

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 7 - Security, Compliance & Governance |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Role + assignee + scope — Owner at subscription is blast radius, not speed

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Role | Can | Cannot |
| --- | --- | --- |
| Reader | List/read resources in scope | PUT/PATCH/DELETE; cannot grant roles |
| Contributor | Create/change/delete resources in scope | Grant roles (not Owner). Cannot always do data-plane secrets without extra roles |
| Owner | Contributor plus assign roles. The flamethrower | Escape the tenant. Still not 'God' over another directory |
| User Access Administrator | Assign roles only | A substitute for Contributor. Different job |
| Custom role | Actions[] you list. Last mile when built-ins are too wide/narrow | A lab toy for a Reader test |

## Step-by-step lab

1. az group create -n rg-day62 -l eastus. Write the resource ID: /subscriptions/<sub>/resourceGroups/rg-day62.
2. az role assignment create --assignee <your-upn> --role Reader --scope that RG ID. az role assignment list --scope … -o table.
3. Compare in notes: Reader vs Contributor vs Owner in one paragraph you could say out loud. Do not assign yourself Owner on the subscription to 'feel the difference'.
4. Optional proof: with only Reader, a write should fail (or reason about it if you also have higher roles inherited from the subscription — then say so honestly).
5. Note: Contributor does not grant Key Vault Secrets User on an RBAC vault. That surprise is Day 64.
6. Remove the extra assignment if it is noise, or keep Reader on rg-day62 as the muscle memory. Write docs/rbac-day62.md. No work-tenant screenshots.

## Done when

- [ ] Can recite role + assignee + scope as the triple
- [ ] Reader assignment on a lab RG exists or existed with a CLI receipt
- [ ] Will not recommend subscription Owner for a pipeline
- [ ] Knows Contributor ≠ Key Vault secret read on RBAC vaults

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-62-rbac-deep-dive
```

## Next

**Day 63** — Service connections and service principals — robot badges, not master keys
