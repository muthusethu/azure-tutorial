# Day 24 — CI Pipeline for a .NET App

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 3 - Continuous Integration |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

restore, build, test, publish — skip one and production finds it

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Step | Command / task | Output |
| --- | --- | --- |
| SDK pin | UseDotNet@2 packageType sdk version 8.x | dotnet --version on ubuntu-latest |
| Restore | dotnet restore src/SampleApi/SampleApi.csproj | NuGet assets; can use day09-packages later |
| Build | dotnet build -c Release --no-restore | bin/Release/net8.0 |
| Test | dotnet test -c Release --no-build --logger trx | trx on Test Results tab if published |
| Publish app | dotnet publish -c Release -o $(Build.ArtifactStagingDirectory)/api | Runnable output, not the full src tree |
| Publish artifact | PublishPipelineArtifact@1 artifactName drop | Consumable by a later deploy stage |

## Step-by-step lab

1. Local SDK 8: dotnet new webapi -n SampleApi -o src/SampleApi && dotnet new xunit -n SampleApi.Tests -o src/SampleApi.Tests && dotnet add src/SampleApi.Tests/SampleApi.Tests.csproj reference src/SampleApi/SampleApi.csproj. One Assert.True is enough.
2. Commit on feature/day24-dotnet-ci. Do not commit bin/ obj/.
3. Add pipelines/dotnet-ci.yml (code below). Pipelines → New pipeline → Existing YAML → this file. Or extend azure-pipelines.yml with a path filter.
4. Push a PR. Confirm UseDotNet@2 logs SDK 8.x, restore, build, test, publish artifact drop.
5. Open the run → Artifacts → drop. Confirm published output, not the whole repo.
6. If tests were skipped, add at least one test project before calling CI done. Do not leave || true.
7. Squash merge when green. Hosted pool only.

## Done when

- [ ] src/SampleApi exists and builds on ubuntu-latest
- [ ] Pipeline pins SDK 8.x with UseDotNet@2
- [ ] Artifact drop is publish output, not raw bin/
- [ ] No || true hiding test failures — red tests fail the job

## LinkedIn

Post draft: [`../../daily-guides/day-24.md`](../../daily-guides/day-24.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-24-ci-pipeline-for-a-net-app
```

## Next

**Day 25** — CI for Node.js
