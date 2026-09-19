# Day 66 — Azure Policy & Governance

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 7 - Security, Compliance & Governance |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Definitions assign effects (Deny, Audit, …) at a scope — Blueprints are retired, initiatives are bundles

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Object | What it is | Lab move |
| --- | --- | --- |
| Definition | JSON: if/then. Built-in 'Require a tag on resource groups' | Use a built-in. Do not author custom JSON on day one |
| Initiative (policy set) | Bundle of definitions, one assignment | Literacy. Assign one definition today |
| Assignment | Definition/initiative + scope (MG / sub / RG) + parameters + effect overlay sometimes | Assign at lab RG or personal sub — not a work MG |
| Compliance blade | Compliant / non-compliant / not started | Create a violating RG and watch the state — then delete it |
| Blueprints | Retired. Do not learn a dead product to sound enterprise | Policy + landing-zone ideas are the current sentence |

## Step-by-step lab

1. Portal → Policy → Definitions. Search Require a tag on resource groups. Open it and read the effect (typically Deny) and the parameter tagName.
2. Policy → Assignments → Assign policy. Scope = personal sub or rg-day66. Parameter tagName=env. Note whether you leave Deny or set Audit for the experiment.
3. Try az group create -n rg-day66-nopolicy -l eastus with no env tag. If Deny: create fails. If Audit: create succeeds and Compliance shows non-compliant.
4. Create a compliant RG with --tags env=lab. Open Compliance blade. Screenshot states without any employer MG names.
5. Delete the non-compliant/junk RG. Do not leave Policy nagging a leftover forever. Optional CLI: az policy assignment create with the built-in definition ID.
6. Write docs/policy-day66.md: effect you used, what you observed, initiative vs definition in one line, Blueprints = retired.

## Done when

- [ ] Can name Deny vs Audit vs AuditIfNotExists vs DeployIfNotExists
- [ ] One built-in assignment visible on the compliance blade
- [ ] Proved the effect with a tagged vs untagged RG
- [ ] Junk RG deleted; Blueprints not in the notes as current

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-66-azure-policy-governance
```

## Next

**Day 67** — Compliance scanning in pipelines — SARIF as a format, not a product tour
