# Day 23 - YAML Pipeline Basics

| | |
|---|---|
| **Date** | 12 Sep 2026 |
| **Phase** | 3 - Continuous Integration |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Triggers, stages, jobs, steps, syntax
- https://learn.microsoft.com/azure/devops/pipelines/yaml-schema

## Hands-on lab (20-30 min)

1. Expand hello pipeline into stages Build -> Test (Test can be echo)
2. Add a PR trigger
3. Read pipeline run logs end-to-end

## Commands / code

```bash
trigger:
  branches:
    include: [ main ]
pr:
  branches:
    include: [ main ]
stages:
- stage: Build
  jobs:
  - job: BuildJob
    pool: { vmImage: ubuntu-latest }
    steps:
    - script: echo Building...
- stage: Test
  dependsOn: Build
  jobs:
  - job: TestJob
    pool: { vmImage: ubuntu-latest }
    steps:
    - script: echo Testing...
```

## LinkedIn post (copy-paste)

```
YAML pipelines are Lego instructions written by someone who enjoys whitespace arguments.

Day 23 of #100DaysOfAzureDevOps. YAML pipeline basics.

Classic editor pipelines taught a generation to click. YAML taught the next one to argue about indentation. After ten years around release trains, I still prefer the argument. A pipeline you cannot diff in a pull request is a pipeline that will drift the moment two people edit it in the UI on the same afternoon.

Today is literacy, not poetry. Triggers, stages, jobs, steps. A PR trigger so main does not become a dumping ground. Logs read end-to-end so "the build failed" becomes a specific step, not a vibe.

What I keep seeing

1. Schema is a map, not decoration
• trigger and pr decide when the robot wakes up
• stages group jobs; jobs grab an agent; steps are the actual work
• If you cannot point to which layer failed, you will debug the wrong layer

2. dependsOn is a promise
• Test that does not depend on Build will race it and lie
• A missing dependsOn looks like speed until it ships an unbuilt artifact

3. PR triggers are manners
• include: main on pull requests catches the break before merge
• Skipping PR CI is how "it worked on my branch" becomes tomorrow's incident

4. Logs are the product of the pipeline
• displayName is how humans find the step at 1am
• Reading the run once, fully, is cheaper than guessing for a week

What I am doing in today's lab

I am expanding the hello pipeline into stages Build then Test (Test can still be echo), adding a PR trigger on main, and reading the pipeline run logs end-to-end instead of celebrating the green checkbox.

If you cannot explain the YAML out loud, you do not own the pipeline yet. Whitespace is annoying. Undiffable clicks are worse.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-23-yaml-pipeline-basics

Tomorrow: CI pipeline for a .NET app — restore, build, test, publish, artifact.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 23 — YAML Pipeline Basics` (max 58 chars)
3. Paste the text above (press **Enter** between sections so line breaks stay)

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5-10 real comments on other Azure/DevOps posts.

## Done checklist

- [ ] Learned the topic (docs or short video)
- [ ] Completed the lab steps
- [ ] Ran / saved the commands or code
- [ ] Published LinkedIn post
- [ ] Engaged with 5-10 community comments
- [ ] Deleted spare Azure resources if any (cost control)

## Tomorrow

**CI pipeline for a .NET app**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
