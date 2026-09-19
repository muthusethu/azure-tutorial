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
Key Vault is the hotel safe — secrets in repo chat history are postcards from an incident.

Day 64 of #100DaysOfAzureDevOps. Azure Key Vault.

Secrets, keys, certificates. Access policies vs RBAC. The hotel safe is not glamorous. It is why a connection string does not live in azure-pipelines.yml, a wiki, or a screenshot in a team chat. I have searched git history for a secret that was "removed" and still sat in an old commit. Postcards. They travel.

Create a vault with RBAC authorization. Secret DemoSecret with value not-a-real-password. Grant myself Key Vault Secrets User. unique vault names. This is still a lab value, not a real password.

What I keep seeing

1. RBAC on the vault is the modern door
• az keyvault create ... --enable-rbac-authorization true
• Access policies still exist; I am not mixing both as a hobby

2. Secrets User is enough to read secrets
• I do not need vault Owner to fetch DemoSecret
• Owner on the vault is another flamethrower

3. Dummy values only
• DemoSecret = not-a-real-password
• A real password in a learning vault that I will screenshot is a contradiction

4. Soft delete exists for a reason
• Literacy: deleted secrets can be recovered
• Purge protection is a real-world conversation; I note it, I do not skip the dummy secret

What I am doing in today's lab

I am creating a Key Vault, setting DemoSecret to a dummy value, granting my user Secrets User via RBAC, and proving I can read it in Portal or CLI. I am not pasting the value into the LinkedIn screenshot, the repo, or a chat.

Hotel safe. Not a postcard. If git ever saw it, rotate — do not "delete the line" and call it done.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-64-azure-key-vault

Tomorrow: Key Vault in pipelines — print length, never the value.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 64 — Azure Key Vault` (max 58 chars)
3. Paste the text above (press **Enter** between sections so line breaks stay)

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5-10 real comments on other Azure/DevOps posts.

## Reminder — 2nd LinkedIn post (production track)

**Today you publish TWO separate LinkedIn posts.** The daily lesson above is post 1 only.

| | Post 1 — #100DaysOfAzureDevOps | Post 2 — #ProductionGradeAzure |
|---|-------------------------------|----------------------------------|
| **When** | ~10:00 IST | ~17:00–19:00 IST (after some engagement on post 1) |
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 21 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 21 of 33 (rewrite with your real experience)
- [ ] Record URLs in [`publish/production-grade/LINKS.md`](../publish/production-grade/LINKS.md)

Run: `python scripts/production_reminder.py`

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
