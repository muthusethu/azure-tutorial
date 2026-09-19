# Day 52 - Azure Container Registry (ACR)

| | |
|---|---|
| **Date** | 11 Oct 2026 |
| **Phase** | 6 - Containers & Kubernetes |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Registries, tags, ACR Tasks

## Hands-on lab (20-30 min)

1. Create Basic ACR
2. docker tag + push
3. Delete images you do not need

## Commands / code

```bash
az acr create -g rg-day52 -n <uniqueacr> --sku Basic
az acr login -n <uniqueacr>
docker tag myapp:latest <uniqueacr>.azurecr.io/myapp:day52
docker push <uniqueacr>.azurecr.io/myapp:day52
```

## LinkedIn post (copy-paste)

```
ACR is a private closet for images — public Docker Hub is the thrift store.

Day 52 of #100DaysOfAzureDevOps. Azure Container Registry.

Public Hub is fine for base images you trust and for toys. Pushing an app image that contains your bits (and sometimes your accidentally copied .env) to a public registry is how a thrift store becomes a data leak. ACR is a private closet: tags, maybe ACR Tasks later, Basic SKU for the lab.

docker tag, docker push, az acr login. Unique registry names because they are globally unique, like storage. Delete images you do not need. Basic ACR still bills. Closets overflow.

What I keep seeing

1. Private by default for app images
• az acr create ... --sku Basic
• Hub for bases; ACR for myapp:day52

2. Tags are pointers, not comments
• myapp:day52 and later Build.BuildId
• :latest is a moving sign. Do not promote latest as if it were immutable

3. Login is identity
• az acr login -n <uniqueacr>
• Admin user enabled "for convenience" is a password in a drawer

4. Garbage collection is a habit
• Delete images you do not need
• Untagged manifests pile up like unread mail

What I am doing in today's lab

I am creating a Basic ACR in rg-day52, logging in, tagging myapp:latest as <uniqueacr>.azurecr.io/myapp:day52, pushing, confirming the repository in Portal, and deleting extra tags. If the name collides, I pick another unique name — I do not reuse a registry I do not own.

Put app images in a closet. The thrift store is for bases you intended to be public.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-52-azure-container-registry-acr

Tomorrow: Build and push images in pipelines — humans will push the wrong Friday tag.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 52 — Azure Container Registry (ACR)` (max 58 chars)
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
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 17 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 17 of 33 (rewrite with your real experience)
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

**Build & push in pipelines**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
