# Day 31 — Release Pipelines Overview

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 4 - Continuous Delivery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Classic is the old mall. YAML CD is a deployment job, an environment, and runOnce.deploy

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Object | YAML | Why it exists |
| --- | --- | --- |
| Classic Release | UI designer, not in the repo | Brownfield literacy. Not the lab default |
| stage | stage: DeployDev | A gate. Can dependOn CI / previous env |
| deployment job | deployment: Deploy  (not job:) | Environment checks attach here |
| environment | environment: dev | Azure DevOps record: history, checks, resources |
| strategy | runOnce.deploy.steps | Smallest CD. rolling/canary come later as ideas |
| bits | download: current  artifact: drop | Consume Phase 3. Rebuilding here invents ghosts |

## Step-by-step lab

1. Pipelines → Environments → New environment → name: dev → create with no resources. This is an Azure DevOps object, not a folder on disk.
2. Add pipelines/cd-dev.yml (starter below): stage DeployDev, deployment job, environment: dev, download drop if CI published it, else echo.
3. If drop is missing, run the Phase 3 CI once so current has an artifact — or keep echo-only and note the gap.
4. Run the pipeline. Open Environments → dev → deployments and confirm this run is listed.
5. Pipelines → Releases (Classic). Open it once. Write one line: why labs stay on YAML. Do not create a Classic release.
6. docs/cd-yaml-day31.md: deployment vs job, environment, download: current.

## Done when

- [ ] Environment dev exists under Pipelines → Environments
- [ ] A deployment job (not a regular job) targeted it
- [ ] YAML does not rebuild the app in Deploy
- [ ] Classic was viewed, not adopted

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-31-release-pipelines-overview
```

## Next

**Day 32** — Deploy to Azure App Service — F1 plan, AzureWebApp@1, the zip you already published.
