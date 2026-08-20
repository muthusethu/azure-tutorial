# Day 64 - Azure Key Vault

| | |
|---|---|
| **Date** | 23 Oct 2026 |
| **Phase** | 7 - Security, Compliance & Governance |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Secrets, keys, certs
- Access policies vs RBAC

## Hands-on lab (20-30 min)

1. Create Key Vault; add secret `DemoSecret`
2. Grant your user Secrets User via RBAC

## Commands / code

```bash
az keyvault create -g rg-day64 -n <uniquekv> --enable-rbac-authorization true
az keyvault secret set --vault-name <uniquekv> --name DemoSecret --value 'not-a-real-password'
```

## LinkedIn post (copy-paste)

```
Day 64 of #100DaysOfAzureDevOps

Key Vault is the hotel safe - secrets in repo chat history are postcards from an incident

Today's topic: **Azure Key Vault**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Key Vault in pipelines.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

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

**Key Vault in pipelines**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
