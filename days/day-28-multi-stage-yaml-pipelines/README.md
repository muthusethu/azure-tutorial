# Day 28 — Multi-stage YAML Pipelines

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 3 - Continuous Integration |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Stages remember order. Matrix clones the job. A deploy stub that ignores Test is theater

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Object | Owns | Typical keys |
| --- | --- | --- |
| stage | A gate in the workflow | dependsOn, condition, jobs, variables |
| job | One agent lease | pool, strategy.matrix, steps, dependsOn (other jobs) |
| deployment | CD job + environment history | environment, strategy.runOnce.deploy (Day 31+) |
| matrix | N clones of the same job | strategy.matrix: py311 / py312 → $(python.version) |
| condition | Whether the stage/job runs | succeeded() default after dependsOn; always() is explicit |

## Step-by-step lab

1. Open pipelines/python-ci.yml (or node). Split it into stages Build and Test. Test must set dependsOn: Build.
2. On the Build (or Test) job add strategy.matrix for two versions (3.11/3.12 or Node 18.x/20.x). NodeTool@0 / UsePythonVersion@0 reads $(version).
3. Add stage Publish with dependsOn: Test and condition: succeeded() and a single script: echo stub — not a real deploy.
4. Run on main or a PR. Confirm the run graph shows two matrix legs, then Publish.
5. Break a test on purpose (assert 1 == 0), push, watch Publish stay skipped. If it still runs, the condition is theater — fix it.
6. Revert the broken test. Write one paragraph in docs/multistage-day28.md: dependsOn vs condition vs matrix.

## Done when

- [ ] Can point at dependsOn and condition: succeeded() in your YAML
- [ ] Matrix ran two versions (or you noted hosted parallelism queued them)
- [ ] A failed Test skipped Publish once
- [ ] docs/multistage-day28.md exists on the personal repo

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-28-multi-stage-yaml-pipelines
```

## Next

**Day 29** — Variables, groups, and secrets — runtime $( ), compile-time ${{ }}, and why secrets in YAML are postcards.
