# Day 84 — Migrating Jenkins to Azure Pipelines

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 9 - Advanced & Enterprise |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Migrate the guarantees, leave the nostalgia

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Jenkins | Azure Pipelines | Guarantee to keep |
| --- | --- | --- |
| agent { label 'linux' } | pool: vmImage: ubuntu-latest (or a named pool) | Same OS / network constraint, not the same snowflake |
| stages { stage('Build') } | stages / jobs / steps | Order and failure isolation |
| post { always { } } | condition: always() on a job or a later stage | Cleanup / publish still runs |
| credentials('id') | Variable group or Azure Key Vault task | Secret not in SCM |
| stash / artifact | PublishPipelineArtifact@1 + download | Same bytes promoted later |
| Jenkins plugin X | Built-in task, script, or a written gap | Do not hide a plugin as 'YAML not ready' |

## Step-by-step lab

1. Write samples/jenkins/Jenkinsfile with agent, three stages (Build, Test, Publish), and a post { always } block. Keep it tiny and fictional.
2. Create docs/jenkins-map-day84.md with a table: Jenkins line → Azure YAML → guarantee kept.
3. Translate to samples/jenkins/azure-pipelines.yml: pool ubuntu-latest, stages/jobs, condition: always() publish, no inline secrets.
4. Map credentials('id') to a variable group name or Key Vault task — write the name, do not put a value in Git.
5. List two Jenkins plugins the sample does not need, and one fictional plugin that would be a real gap (e.g. a licensed scanner).
6. Do not stand up a Jenkins controller. The proof is the mapping, not a blue ball.

## Done when

- [ ] Sample Jenkinsfile and mapped azure-pipelines.yml both exist
- [ ] docs/jenkins-map-day84.md lists agent/stages/post/credentials/plugins
- [ ] No employer Jenkinsfile
- [ ] No Jenkins controller installed for the lab
- [ ] Posted the LinkedIn document

## LinkedIn

Post draft: [`../../daily-guides/day-84.md`](../../daily-guides/day-84.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-84-migrating-jenkins-to-azure-pipelines
```

## Next

**Day 85** — Hybrid and multi-cloud CI/CD — survey the risks; do not buy a second cloud for a slide
