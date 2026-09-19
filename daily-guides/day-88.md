# Day 88 - GitOps with Flux/Argo CD

| | |
|---|---|
| **Date** | 16 Nov 2026 |
| **Phase** | 9 - Advanced & Enterprise |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Git as source of truth for cluster state

## Hands-on lab (20-30 min)

1. Read GitOps principles; optional local Flux quickstart
2. Compare to Azure Pipelines push model

## Commands / code

```bash
# Git desired state -> controller reconciles cluster
# PR to change prod; no kubectl cowboy moves
```

## LinkedIn post (copy-paste)

```
GitOps means the cluster stops being a petting zoo for kubectl.

Day 88 of #100DaysOfAzureDevOps. GitOps with Flux or Argo CD.

Git as the desired state. A controller reconciles the cluster. A PR changes prod. No cowboy kubectl. I have been the cowboy. It is fun until three cowboys ride at once. GitOps is how the zoo gets a lock on the gate.

Read GitOps principles. Optional local Flux quickstart. Compare to Azure Pipelines push (Day 57). Push CD applies from a job. GitOps pulls from Git. Both can be mature. Mixing cowboy kubectl with either is the petting zoo.

What I keep seeing

1. Desired state is Git, not a memory
• If it is not in the repo, the cluster will drift back or fight you
• Hotfix via kubectl is a debt with interest

2. Controllers close the loop
• Flux/Argo reconcile
• A pipeline that only pushes still needs something to notice drift

3. PRs are the change window
• Review, then merge, then the cluster follows
• Prod access for humans can shrink

4. Optional quickstart, mandatory comparison
• Local Flux if I have time and a cluster
• Written comparison to Azure Pipelines push if I do not

What I am doing in today's lab

I am reading GitOps principles, optionally running a local Flux quickstart, and writing push-vs-pull in a short note. I will not kubectl into a reconciled cluster to "just fix it" as a habit, even in a lab. The zoo stays closed.

If the cluster is a petting zoo, Git is not the source of truth. The last cowboy is.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-88-gitops-with-flux-argo-cd

Tomorrow: Scaling DevOps for large teams — five platform capabilities for a 50-dev org.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 88 — GitOps with Flux / Argo CD` (max 58 chars)
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
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 29 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 29 of 33 (rewrite with your real experience)
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

**Scaling DevOps for large teams**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
