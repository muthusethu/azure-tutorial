# Day 92 — Capstone Project 2 - Containers Path

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 10 - Portfolio & Public Launch |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Same public demo, container tuxedo — not a new Netflix clone

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Box | Personal Azure object | Pin |
| --- | --- | --- |
| Dockerfile | capstone/Dockerfile in the same repo | Non-root user if you can; no secrets in layers |
| CI build | Docker@2 or docker build in the pipeline | Tag $(Build.BuildId), not latest-as-truth |
| Registry | Azure Container Registry Basic (or destroy after) | acr login from the service connection |
| Runtime default | Container Apps consumption or App Service containers | Same /health contract as Day 91 |
| AKS | Optional only | Destroy the cluster tonight if you create it |
| GitOps (optional) | Manifest points at the digest | Day 88 rule: no cowboy kubectl |

## Step-by-step lab

1. Add capstone/Dockerfile that serves the same /health contract. No secrets in ENV. Build locally only to debug, not to publish.
2. Create or reuse a personal ACR. Note the login server in capstone/README.md.
3. Extend the pipeline: docker build, tag $(Build.BuildId), docker push to ACR. Service connection does the auth.
4. Deploy that image to Container Apps or App Service for containers. Confirm /health shows the new build id.
5. Update the README diagram with Registry + runtime boxes. Five-minute demo still has to work.
6. If you opened AKS, write the destroy command in the README and run it when the screenshot exists.
7. Do not start a new streaming-platform repo.

## Done when

- [ ] Dockerfile in the same capstone repo
- [ ] Pipeline builds and pushes to personal ACR with Build.BuildId
- [ ] Same app URL/contract as Day 91, now from a container
- [ ] AKS destroyed if you created it; latest is not the promotion story
- [ ] README diagram includes registry + runtime

## LinkedIn

Post draft: [`../../daily-guides/day-92.md`](../../daily-guides/day-92.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-92-capstone-project-2-containers-path
```

## Next

**Day 93** — Capstone 3 — IaC for two environments of the same public demo, then destroy non-prod
