# Day 53 - Build & Push Images in Pipelines

| | |
|---|---|
| **Date** | 12 Oct 2026 |
| **Phase** | 6 - Containers & Kubernetes |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Docker tasks, multi-stage builds, scanning intro

## Hands-on lab (20-30 min)

1. Pipeline builds image and pushes to ACR
2. Use service connection

## Commands / code

```bash
- task: Docker@2
  inputs:
    containerRegistry: acr-connection
    repository: myapp
    command: buildAndPush
    Dockerfile: **/Dockerfile
    tags: |
      $(Build.BuildId)
      latest
```

## LinkedIn post (copy-paste)

```
If humans push images by hand, humans will push the wrong tag on a Friday.

Day 53 of #100DaysOfAzureDevOps. Build and push images in pipelines.

Friday, 5:40pm, someone typed :latest when they meant the git SHA. I have been in that sentence. Docker@2 buildAndPush with tags $(Build.BuildId) and, if I must, latest as a convenience pointer — not as the promotion identity. Service connection to ACR. Multi-stage Dockerfile if the build needs a compiler the runtime does not.

Scanning is an intro today, not a platform. The pipeline is the point: the agent builds, the registry receives, a human does not copy-paste a tag from Slack.

Patterns I keep seeing

1. The pipeline is the only publisher
• Docker@2, containerRegistry: acr-connection, command: buildAndPush
• Laptop docker push in prod is how Friday tags happen

2. Tag with the build, not with a mood
• $(Build.BuildId) is boring and unique enough for a lab
• latest as a second tag is optional; promoting by latest is not

3. Multi-stage builds keep runtime thin
• Build in a fat image, copy the output into a slim one
• Shipping gcc into production is a hobby

4. Scan is a preview, not a vibe
• Know that image scanning exists
• A green push is not a CVE report. Later phases will be rude about that

What I am doing in today's lab

I am adding a pipeline that builds the Dockerfile, pushes to ACR with Build.BuildId (and latest if I want the pointer), using a service connection. I will not docker push from my PC for this proof. If the connection cannot push, I fix the identity, I do not enable admin and paste a password into a variable.

Humans are bad at Friday tags. Robots are consistent. Let the pipeline own the closet key.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-53-build-push-images-in-pipelines

Tomorrow: Azure Container Instances — container fast-food, delete after the test.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 53 — Build & Push Images in CI` (max 58 chars)
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

**Azure Container Instances**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
