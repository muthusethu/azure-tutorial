# Day 70 — Mini Project + Recap (Phase 7)

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 7 - Security, Compliance & Governance |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Speed without security is just a faster incident — identity, then RBAC, then the hotel safe

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Layer | Object | Done looks like |
| --- | --- | --- |
| Identity | Entra tenant, day61-lab appId | Personal directory; no secret in git |
| RBAC | Reader/Contributor at RG, not Owner at sub | Scope sentence you can say out loud |
| Robot badge | lab-sc = WIF service connection + SP | Not the same object as the app registration blade |
| Safe | Key Vault RBAC + DemoSecret dummy + pipeline fetch | Length in logs, not letters |
| Guardrails | Policy Deny/Audit + Security stage + approvals | Compliance blade + Deploy skipped on red scan |

## Step-by-step lab

1. Run one pipeline that fetches DemoSecret (length only) and has stages Build → Security → Deploy with environment: lab approval.
2. Confirm Policy assignment from Day 66 still exists (or re-assign require tag). Compliance blade shows the lab scope.
3. Confirm lab-sc is WIF, not Owner at subscription, and has Secrets User on the vault.
4. Confirm main is PR-protected and no secret values live in YAML/Library screenshots.
5. Write docs/phase7-recap.md: bouncer list → scoped badges → hotel safe → Policy effect → Security stage. Screenshot without secret values.
6. Tear down junk RGs from the policy experiment if they remain. Keep the vault only if you still need it for Phase 8 — else delete dummy secrets first.

## Done when

- [ ] Secret not in YAML; policy visible; approvals on
- [ ] Can explain app registration vs service connection vs RBAC scope
- [ ] Owner SPN leftover removed or documented as absent
- [ ] Phase 7 recap doc on the personal repo

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-70-mini-project-recap-phase-7
```

## Next

**Day 71** — Azure Monitor fundamentals — the flashlight, not the fix
