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
Day 24 of #100DaysOfAzureDevOps

.NET CI is the same ritual every time: restore, build, test, publish - skip one and production finds it for you

Today's topic: **CI Pipeline for a .NET App**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: CI for Node.js.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no "DM me for freelance".
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
