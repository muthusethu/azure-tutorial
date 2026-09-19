# Day 92 - Capstone Project 2 - Containers Path

| | |
|---|---|
| **Date** | 20 Nov 2026 |
| **Phase** | 10 - Portfolio & Public Launch |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Containerize capstone; ACR + deploy
- AKS optional

## Hands-on lab (20-30 min)

1. Dockerfile + pipeline build/push + deploy
2. Continue same app as Day 91

## Commands / code

```bash
# Same repo - add /Dockerfile and k8s or containerapp yaml
```

## LinkedIn post (copy-paste)

```
Day 92 is the same app in a container tuxedo — not a new Netflix clone.

Day 92 of #100DaysOfAzureDevOps. Capstone project 2 — containers path.

Containerize the capstone. ACR plus deploy. AKS optional. Same app as Day 91. A tuxedo is a costume change, not a new actor. I have seen people throw away a working zip deploy to start "real microservices" in week two of a capstone. They shipped neither.

Dockerfile, pipeline build/push, deploy via the path I already trust (Container Apps, App Service containers, or k8s YAML). Add /Dockerfile and k8s or containerapp yaml in the same repo.

What I keep seeing

1. Same repo, new packaging
• The code did not become a platform overnight
• The image is the artifact now — Build.BuildId tag, not latest-as-truth

2. AKS is still optional
• If cost bites, Container Apps or App Service
• A tuxedo that requires a forgotten cluster is a gym membership in silk

3. Pipeline must push
• No laptop docker push as the capstone story
• Day 53's Friday tag still applies in a nicer folder

4. README gains a box
• Registry + runtime
• The 5-minute demo still has to work

What I am doing in today's lab

I am adding a Dockerfile, a pipeline that builds and pushes to ACR, and a deploy of the same app. AKS only if I will destroy it. Netflix clones are out of scope with extra neon. Tuxedo on. Same actor.

Package the slice. Do not replace the slice with a streaming empire.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-92-capstone-project-2-containers-path

Tomorrow: Capstone 3 — Bicep or Terraform for two environments, destroy non-prod.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 92 — Capstone 2: Containers Path` (max 58 chars)
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

**Capstone 3**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
