# Day 82 — Pipeline Templates & Reusable YAML

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 9 - Advanced & Enterprise |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

One contract beats fourteen slightly different broken builds

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Knob | YAML | Use today |
| --- | --- | --- |
| Step template | - template: templates/build.yml | Extract restore/build/test once |
| parameters | parameters: - name: projectPath type: string | The contract. No secret defaults |
| extends | extends: template: templates/pipeline.yml | Literacy: template owns stages; lab can stay steps |
| Template repo ref | resource: repo + ref: refs/tags/v1 | Later; same repo templates/ is enough |
| Each: / insert | ${{ each p in parameters.projects }} | Skip until two consumers exist (Day 90) |

## Step-by-step lab

1. Create templates/build.yml with a required parameter projectPath (string) and a step that builds or echoes that path.
2. Point the main pipeline at it: steps: - template: templates/build.yml with parameters.projectPath.
3. Run the pipeline once on ubuntu-latest. The log must show the parameter value.
4. If two sample apps already exist, call the same template twice with different paths. If not, one caller today; two consumers on Day 90.
5. Search the repo for duplicated npm ci / dotnet publish / docker build. If still duplicated, you rearranged — extract the rest.
6. Write docs/templates-day82.md: contract (parameter names) and the rule 'Node version changes in one file'.

## Done when

- [ ] templates/build.yml exists with a required projectPath
- [ ] Main pipeline calls the template; log shows the path
- [ ] No secret defaults in the template
- [ ] Call site is boring (one template line)
- [ ] Posted the LinkedIn document

## LinkedIn

Post draft: [`../../daily-guides/day-82.md`](../../daily-guides/day-82.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-82-pipeline-templates-reusable-yaml
```

## Next

**Day 83** — Marketplace extensions — a pinch of spice, or a written reason to install zero
