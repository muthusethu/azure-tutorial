# Day 91 — Capstone Project 1 - E2E App CI/CD

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 10 - Portfolio & Public Launch |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

A public demo slice you can walk in five minutes — not a new ecommerce

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Box | Personal Azure object | What a stranger sees |
| --- | --- | --- |
| Repo | Personal Azure Repos or GitHub: capstone/ | README diagram + /health source |
| CI | Azure Pipeline on ubuntu-latest | Restore, test, publish zip/artifact |
| Artifact | PublishPipelineArtifact@1 named drop | Same bytes that will be promoted |
| Dev env | Azure App Service F1 or Container Apps consumption | https://<app>-dev.azurewebsites.net/health |
| Staging | Second slot or second app + Environment approval | Same artifact, different URL |
| Identity | Project-scoped service connection | No user PAT in YAML |

## Step-by-step lab

1. Create capstone/README.md with In/Out lists and a four-box diagram: repo → pipeline → environment → App Service (or Container Apps).
2. Reuse an earlier lab app or a tiny new demo-shipboard that returns { status, env, buildId } on GET /health. One service only.
3. Add or harden azure-pipelines.yml: trigger on capstone/**, ubuntu-latest, test, PublishPipelineArtifact@1.
4. Deploy that artifact to a personal F1 App Service or consumption Container App. Record the public /health URL.
5. Add a staging promotion path (slot or second app) that reuses the same artifact. Approval can be you.
6. Walk the demo in five minutes: PR or push → green run → URL shows the build id. If you cannot, cut scope.
7. No payments, no ML, no 12 services. If you want to add one, read the Out list out loud.

## Done when

- [ ] capstone/ exists with In/Out and a diagram
- [ ] Public /health (or equivalent) on a personal Azure app
- [ ] CI publishes an artifact; staging reuses it
- [ ] No employer code, no ecommerce scaffold
- [ ] Five-minute demo path written in the README

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-91-capstone-project-1-e2e-app-ci-cd
```

## Next

**Day 92** — Capstone 2 — the same public demo in a container tuxedo, not a Netflix clone
