# Day 30 — Mini Project + Recap (Phase 3)

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 3 - Continuous Integration |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Same spine in every language: install, build, test, publish a drop — secrets stay in the group

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Day | Object you should still be able to draw | Keep |
| --- | --- | --- |
| 21–22 | pool: vmImage vs named self-hosted pool | Hosted ubuntu-latest until a private-network constraint |
| 23 + 28 | trigger/pr → stages → jobs → steps; dependsOn; matrix | Sketch from memory or you copied |
| 24–27 | .NET / Node / Python / Maven CI tasks | One primary stack green; others may stay stubs |
| 29 | Library group + secret mask | No passwords in azure-pipelines.yml |
| Handoff | PublishPipelineArtifact@1 name: drop | CD (Phase 4) must download this, not rebuild |

## Step-by-step lab

1. Choose primary stack (.NET Day 24, Node 25, Python 26, or Maven 27). Delete or ignore the other pipelines if they distract — do not keep red mains.
2. Ensure that pipeline publishes an artifact named drop (PublishPipelineArtifact@1 or PublishBuildArtifacts@1). Run on main until green.
3. Open the run → Artifacts and confirm drop exists. That object is the Phase 4 input.
4. Write docs/phase3-recap.md: (1) YAML anatomy in one line, (2) one war story from this week (cache miss, skipped test, almost-echoed secret).
5. Screenshot the green run with no variable values. Save it locally — do not commit secrets or org URLs you would not post.
6. Pipelines folder is the source of truth. If Classic UI still holds a leftover, leave it unused.

## Done when

- [ ] One green CI on main for the primary stack
- [ ] Artifact drop is visible on that run
- [ ] docs/phase3-recap.md has anatomy + one war story
- [ ] No secrets in YAML or screenshots

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-30-mini-project-recap-phase-3
```

## Next

**Day 31** — Release pipelines overview — Classic is literacy; YAML CD is a deployment job + environment: dev.
