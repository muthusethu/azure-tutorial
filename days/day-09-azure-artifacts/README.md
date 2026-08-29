# Day 09 — Azure Artifacts

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Create a project-scoped Azure Artifacts feed with upstream sources enabled, configure feed views (@local, @prerelease, @release), and connect client tooling (npm / NuGet).

## High-level architecture (summary)

Open **[handout.pdf](./handout.pdf)** for complete tables. Short version:

| Concept | Purpose |
|---------|---------|
| **Feed** | Container for packages (NuGet, npm, Maven, Python, Universal) |
| **Upstream Sources** | Cache public packages locally (resilience against external outages) |
| **Feed Views** | Release gates (`@local` → `@prerelease` → `@release`) without re-versioning |
| **Retention Policy** | Automatically clean up old package versions to manage storage |

**Dependency Flow:** Developer / CI ↔ Azure Artifacts Feed ↔ Upstream Public Registries (nuget.org / npmjs.org)

## Learn

- [Azure Artifacts overview](https://learn.microsoft.com/azure/devops/artifacts/start-using-azure-artifacts)

## Step-by-step lab

1. Open `azure-100-labs` → **Artifacts**
2. Create Feed `day09-packages` (project-scoped)
3. Enable upstream sources for **nuget.org** and **npmjs**
4. Review feed views (`@local`, `@prerelease`, `@release`)
5. Click **Connect to feed** → review `.npmrc` / `nuget.config` snippet
6. Save feed URL for Phase 3 CI/CD automation

## Done when

- [ ] You can explain Feeds vs Upstream Sources vs Feed Views
- [ ] Feed `day09-packages` exists in `azure-100-labs`
- [ ] Upstream caching is enabled and client configuration understood

## LinkedIn

Post draft: [`../../daily-guides/day-09.md`](../../daily-guides/day-09.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://bit.ly/4xDxqIc
```

(Full path: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-09-azure-artifacts)

## Next

**Day 10** — Phase 1 Capstone Mini Project & Recap.
