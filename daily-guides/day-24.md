# Day 24 - CI Pipeline for a .NET App

| | |
|---|---|
| **Date** | 13 Sep 2026 |
| **Phase** | 3 - Continuous Integration |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- dotnet restore/build/test/publish
- Pipeline artifacts

## Hands-on lab (20-30 min)

1. Create `/src/SampleApi` minimal Web API OR use `dotnet new webapi`
2. Add pipeline restore -> build -> test -> publish
3. Publish pipeline artifact

## Commands / code

```bash
# pipelines/dotnet-ci.yml
trigger:
  paths:
    include: [ src/SampleApi/** ]
pool:
  vmImage: ubuntu-latest
steps:
- task: UseDotNet@2
  inputs:
    packageType: sdk
    version: 8.x
- script: |
    dotnet restore src/SampleApi
    dotnet build src/SampleApi -c Release --no-restore
    dotnet test src/SampleApi -c Release --no-build || true
  displayName: Build
- task: PublishBuildArtifacts@1
  inputs:
    PathtoPublish: src/SampleApi/bin/Release
    ArtifactName: drop
```

## LinkedIn post (copy-paste)

```
.NET CI is the same ritual every time: restore, build, test, publish — skip one and production finds it for you.

Day 24 of #100DaysOfAzureDevOps. CI pipeline for a .NET app.

I have lost count of how many "the API is down" threads ended with a missing restore, a Debug build in a Release slot, or tests that were commented out because they were slow. The ritual is boring on purpose. restore, build, test, publish. Then an artifact that the next environment can actually deploy.

UseDotNet@2 pins the SDK so the agent image does not surprise you. Path filters keep the pipeline from rebuilding the universe when someone edits a README. None of this is clever. All of it is how .NET teams stop being the person who compiled from their laptop into production.

Patterns from a decade of delivery

1. Pin the SDK
• UseDotNet@2 with 8.x (or whatever the repo actually builds)
• "It compiled on the agent last month" is not a version strategy

2. Restore is not optional theater
• dotnet restore, then build -c Release --no-restore
• Skipping restore to "save time" is how you get a random package graph

3. Test before you publish, even if today the test is thin
• dotnet test on the same configuration you ship
• || true in a lab is honesty; in production it is a lie you scheduled

4. Publish an artifact, do not rebuild later
• PublishBuildArtifacts (or PublishPipelineArtifact) from bin/Release
• The CD stage should consume drop, not invoke dotnet build again

What I am doing in today's lab

I am creating a minimal Web API under /src/SampleApi (dotnet new webapi), adding a pipeline that restores, builds, tests, and publishes, and storing the drop as a pipeline artifact. Path trigger stays on src/SampleApi/** so the rest of the repo can be noisy.

Skip a step of the ritual and you are not being agile. You are postponing the finding to a user.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-24-ci-pipeline-for-a-net-app

Tomorrow: CI for Node.js — npm ci, Cache@2, and stopping the paint-dry restore.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 24 — CI Pipeline for a .NET App` (max 58 chars)
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

**CI for Node.js**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
