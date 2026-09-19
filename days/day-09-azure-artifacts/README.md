# Day 9 — Azure Artifacts

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 1 - Azure & DevOps Foundations |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

The pantry. Pipelines cook. Without a feed you re-buy flour every build.

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Piece | What it is | Lab setting |
| --- | --- | --- |
| Feed | Private registry scoped to org or project | day09-packages, project-scoped |
| Upstream nuget.org | Proxy + cache of public NuGet | Enable on create |
| Upstream npmjs | Proxy + cache of public npm | Enable on create |
| View @local | Default: every push lands here | Do not skip; this is the inbox |
| View @prerelease / @release | Promotion without changing the version | Use in Phase 3, not today |
| Retention | Max versions / days to keep | Leave default; 2 GB free tier is enough |

## Step-by-step lab

1. azure-100-labs → Artifacts → Create Feed.
2. Name day09-packages. Scope: Project azure-100-labs (not organization). Visibility: members of this project.
3. Check Include packages from common public sources (nuget.org, npmjs). Create.
4. Feed settings → Views. Note @local, @prerelease, @release. Do not delete them.
5. Connect to feed → NuGet → copy the packageSources URL. Paste into notes/artifacts-day09.md locally.
6. Connect to feed → npm → copy the registry= https://pkgs.dev.azure.com/.../npm/registry/ line.
7. Permissions tab: you are Owner. Do not add work users. Empty package list is success for today.

## Done when

- [ ] Can explain feed vs upstream vs view (@local/@release)
- [ ] day09-packages exists, project-scoped, upstreams on
- [ ] Feed URL saved in notes (NuGet and/or npm)
- [ ] No PAT, password, or nupkg committed

## LinkedIn

Post draft: [`../../daily-guides/day-09.md`](../../daily-guides/day-09.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-09-azure-artifacts
```

## Next

**Day 10** — Mini project + recap
