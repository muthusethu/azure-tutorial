# Day 13 — Azure Repos Setup

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 2 - Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Default branch, folder contract, .gitignore — stop future archaeology

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Path | Owns | Later consumer |
| --- | --- | --- |
| /src | Application code | Day 24 SampleApi, Day 25 sample-node |
| /docs | ADRs, notes | Branching ADR, CALMS scorecard |
| /pipelines | YAML entrypoints | dotnet-ci.yml, node-ci.yml |
| /infra | Bicep/ARM later | Empty .gitkeep is enough today |
| /notes | Daily markdown | day11.md already |
| /.gitignore | What never becomes a blob | bin/, node_modules/, .env |

## Step-by-step lab

1. Repos → Branches. If default is master: … → Set as default branch on main. Update any local: git switch main.
2. git switch -c feature/day13-repo-layout
3. Create folders src, docs, pipelines, infra with .gitkeep files so Git tracks empty dirs.
4. Add a .gitignore (Node + .NET + Python combined is fine). Must include node_modules/, bin/, obj/, .env, *.user.
5. git add src docs pipelines infra .gitignore && git commit -m "chore: repo layout and gitignore" && git push -u origin feature/day13-repo-layout
6. Open PR to main (or merge if policies are still off). Confirm default branch is main after merge.
7. Project settings → Repositories → azure-100-labs → Overview. Note default branch = main. Policies come Day 19.

## Done when

- [ ] Default branch is main
- [ ] src, docs, pipelines, infra exist on the branch/main
- [ ] .gitignore blocks node_modules, bin/obj, .env
- [ ] origin is still the personal Azure Repos URL

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-13-azure-repos-setup
```

## Next

**Day 14** — Pull requests & code review
