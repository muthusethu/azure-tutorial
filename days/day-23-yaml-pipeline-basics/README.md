# Day 23 — YAML Pipeline Basics

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 3 - Continuous Integration |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

trigger, pr, stages, jobs, steps — Lego instructions that care about whitespace

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Key | Meaning | Lab value |
| --- | --- | --- |
| trigger | CI on push to listed branches | branches.include: [main] |
| pr | Validation on PRs targeting listed branches | branches.include: [main] |
| stages | Ordered groups; default one implicit stage | Build then Test |
| jobs | Agent allocation unit; can dependOn | BuildJob, TestJob |
| pool | vmImage or name | ubuntu-latest on each job |
| steps | script, bash, pwsh, task, checkout, template | echo is enough today |

## Step-by-step lab

1. Edit azure-pipelines.yml (or pipelines/ci.yml and retarget the pipeline) on feature/day23-yaml.
2. Add trigger.branches.include: [main] AND pr.branches.include: [main].
3. Add stages: Build (echo Building) then Test dependsOn: Build (echo Testing). Each job pool: vmImage: ubuntu-latest.
4. Push and open a PR to main. Confirm the pipeline appears on the PR Checks tab.
5. Pipelines → latest run → expand both stages. Read every step log. Note stage names in the graph.
6. If policies require a work item, link one. Squash merge when green.
7. Do not add a self-hosted pool name. Do not add secrets.

## Done when

- [ ] Can name trigger, pr, stage, job, step, dependsOn
- [ ] PR to main queued a validation run
- [ ] Test stage ran after Build in the logs
- [ ] Both jobs used ubuntu-latest

## LinkedIn

Post draft: [`../../daily-guides/day-23.md`](../../daily-guides/day-23.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-23-yaml-pipeline-basics
```

## Next

**Day 24** — CI pipeline for a .NET app
