# Day 53 — Build & Push Images in Pipelines

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 6 - Containers & Kubernetes |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

The agent builds, ACR receives, a human does not copy-paste a tag from Slack

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Dimension | docker push from PC | Docker@2 buildAndPush |
| --- | --- | --- |
| Who authenticates | Your user via az acr login | Service connection (AcrPush). Not the admin password in a variable |
| Tag | Whatever you typed. Friday :latest happens here | $(Build.BuildId) plus optional latest pointer |
| Dockerfile | Whatever is on disk, dirty or not | What Git has on that commit. Multi-stage if the build needs a compiler |
| Scan | Optional local Trivy if you remember | Intro only today: a scan step can fail the job. Day 67 is the gate |
| Audit | No Build.BuildId, no commit SHA on the tag | Repo + build number is the receipt |

## Step-by-step lab

1. Project Settings → Service connections → New → Docker Registry / Azure Container Registry. Use the personal ACR. Prefer identity over registry admin. Name it acr-connection.
2. Confirm the identity has AcrPush on that registry (or RG). If the wizard created Owner on the subscription, that is a finding — tighten before you call the lab done.
3. Add azure-pipelines.yml with pool vmImage ubuntu-latest and Docker@2 command buildAndPush, repository myapp, tags $(Build.BuildId) and optionally latest. Dockerfile path from the repo root.
4. Run the pipeline. In ACR, confirm the Build.BuildId tag and digest. Do not docker push from the PC for this proof.
5. Optional intro: a Trivy (or similar) step that prints CVEs but does not yet fail the whole CD path. Scanning as a gate is Day 67.
6. Write docs/pipeline-push-day53.md: service connection name, build id tag, digest. If the job failed on auth, fix the identity — do not flip admin-enabled true.

## Done when

- [ ] Pipeline, not the laptop, produced the tag in ACR
- [ ] Tag includes Build.BuildId; latest is at most a pointer
- [ ] Service connection has AcrPush — admin user still off
- [ ] docs/pipeline-push-day53.md has the digest

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-53-build-push-images-in-pipelines
```

## Next

**Day 54** — Azure Container Instances — a URL without a cluster gym membership
