# Day 64 — Azure Key Vault

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 7 - Security, Compliance & Governance |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Secrets, keys, certs — RBAC on the vault is the door; Contributor on the RG is not

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Thing | What it holds | Who reads it |
| --- | --- | --- |
| Secret | Connection strings, dummy DemoSecret | Key Vault Secrets User (data plane). Not RG Contributor |
| Key | Cryptographic keys (encrypt/sign) | Key Vault Crypto User / Officer — different role |
| Certificate | TLS material, often with a key + secret projection | Cert roles; do not treat it as 'just a secret' |
| Access policies (legacy) | Vault-level policy entries per identity | Do not mix with RBAC on the same vault as a hobby |
| RBAC (modern) | --enable-rbac-authorization true. Data-plane roles on vault or secret | Control plane (vault resource) vs data plane (secret get) are different |

## Step-by-step lab

1. az group create -n rg-day64 -l eastus. az keyvault create -g rg-day64 -n <uniquekv> --enable-rbac-authorization true --sku standard.
2. Assign yourself Key Vault Secrets Officer on the vault resource ID (need set). Optional: also Secrets User if you want the read-only role in notes.
3. az keyvault secret set --vault-name <uniquekv> --name DemoSecret --value 'not-a-real-password'. az keyvault secret show --query name (not the value in any screenshot).
4. Confirm RG Contributor alone is not the story: the data-plane role is why show works. Write that sentence.
5. Do not enable access-policy mode. Do not put DemoSecret in the repo. Soft-delete literacy: note that delete is recoverable.
6. Write docs/kv-day64.md: vault name, RBAC vs access policies, Secrets User vs Officer vs Contributor. Pipeline integration is tomorrow.

## Done when

- [ ] RBAC vault exists; DemoSecret is a dummy
- [ ] Can explain why Contributor on the RG does not get secret GET
- [ ] No secret value in Git, chat, or LinkedIn
- [ ] docs/kv-day64.md records vault name and roles

## LinkedIn

Post draft: [`../../daily-guides/day-64.md`](../../daily-guides/day-64.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-64-azure-key-vault
```

## Next

**Day 65** — Key Vault in pipelines — fetch at runtime, print length never the value
