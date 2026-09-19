# Day 61 - Azure AD (Entra ID) Fundamentals

| | |
|---|---|
| **Date** | 20 Oct 2026 |
| **Phase** | 7 - Security, Compliance & Governance |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Tenants, users, groups, app registrations

## Hands-on lab (20-30 min)

1. In personal tenant: register an app `day61-lab`
2. Note client ID; create a secret only in Key Vault tomorrow - or use cert later

## Commands / code

```bash
# Portal: Entra ID -> App registrations -> New registration
# Redirect URI: optional for lab
```

## LinkedIn post (copy-paste)

```
Entra ID is the bouncer list for Azure — if identity is wrong, every other control is cosplay.

Day 61 of #100DaysOfAzureDevOps. Azure AD (Entra ID) fundamentals.

Tenants, users, groups, app registrations. Everything else in Azure assumes this list is right. I have watched beautiful RBAC and Key Vault designs collapse because the app registration was in the wrong tenant or the secret was taped to a wiki. If the bouncer list is wrong, the velvet rope is theater.

Personal tenant. Register an app day61-lab. Note the client ID. I am not putting a client secret in YAML. Tomorrow is Key Vault for secrets, or a certificate later. Redirect URI optional for this lab.

Patterns I keep seeing

1. Tenant is the building
• Work tenant vs personal tenant — labs stay personal
• A registration in the wrong directory is a bug that looks like RBAC

2. App registration is not a user
• It is an identity for an application
• Client ID is public-ish; client secret is not

3. Groups beat one-off assignments at scale
• Literacy: assign to groups
• Lab: I am one user, still do not make the app Owner of the subscription

4. Secrets have a next step
• Do not create a secret I will paste into a pipeline today
• Note the ID; Key Vault is the envelope later this week

What I am doing in today's lab

In the personal tenant I am registering app day61-lab, noting the client ID, and not creating a long-lived secret in a text file. Portal: Entra ID → App registrations → New registration. Redirect URI optional. Screenshot without secrets.

Fix the bouncer list first. Every other Azure control is cosplay if identity is a rumor.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-61-azure-ad-entra-id-fundamentals

Tomorrow: RBAC deep dive — Reader on a lab RG, Owner as a flamethrower.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 61 — Entra ID Fundamentals` (max 58 chars)
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
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 20 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 20 of 33 (rewrite with your real experience)
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

**RBAC deep dive**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
