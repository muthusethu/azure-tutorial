# Day 60 - Mini Project + Recap (Phase 6)

| | |
|---|---|
| **Date** | 19 Oct 2026 |
| **Phase** | 6 - Containers & Kubernetes |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Containerize app + deploy via CI/CD (ACI/Container Apps/AKS - one path)

## Hands-on lab (20-30 min)

1. Prefer Container Apps or ACI if AKS cost bites
2. Recap post with architecture one-liner

## Commands / code

```bash
# Done = image in ACR + one successful deploy path automated
```

## LinkedIn post (copy-paste)

```
Phase 6 recap: package once, run anywhere — but "anywhere" still has a bill.

Day 60 of #100DaysOfAzureDevOps. Mini project and recap for Phase 6 — containers and Kubernetes.

Dockerfile, ACR, pipeline build/push, ACI as fast-food, Kubernetes vocabulary, optional AKS, Helm, a glance at HPA. The mini project is one path: containerize the app, put the image in ACR, deploy via CI/CD. Prefer Container Apps or ACI if AKS cost bites. Architecture one-liner in the recap.

"Run anywhere" is a slogan. Anywhere with a registry pull, a CPU, and an invoice is the adult version.

What I am keeping from Phase 6

1. Image in ACR is the artifact now
• Not only a zip. A tagged image from the pipeline
• latest is not the promotion ID

2. One deploy path, automated
• ACI or Container Apps or AKS — one
• Three half-paths is not a recap. It is a buffet

3. Helm or manifests in Git
• No sticky-note kubectl as the process
• values.yaml for env differences

4. Cost is part of the architecture one-liner
• If AKS exists, destroy date is in the recap
• If I skipped AKS, that is an architecture decision, not a failure

What I am doing in today's lab

I am finishing image-in-ACR plus one successful automated deploy path, writing a one-line architecture, and killing ACI/AKS leftovers. Done = image in ACR + one successful deploy path automated. The bill should not include a forgotten gym.

Package once. Run on a path you can pay for and tear down. Slogans do not get invoices.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-60-mini-project-recap-phase-6

Tomorrow: Entra ID fundamentals — tenants, app registrations, identity as the bouncer list.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 60 — Phase 6 Mini Project & Recap` (max 58 chars)
3. Paste the text above (press **Enter** between sections so line breaks stay)

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

**Entra ID fundamentals**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
