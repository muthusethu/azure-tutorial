# Day 21 — Intro to Azure Pipelines

| | |
|---|---|
| **Date** | 10 Sep 2026 |
| **Phase** | 3 — Continuous Integration |
| **Time box** | 60–90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Stand up the first YAML pipeline in `azure-100-labs`: trigger on `main`, Microsoft-hosted `ubuntu-latest`, one `echo` step that proves CI is a file in Git — not a wizard you click once. Publish Day 21 on LinkedIn with the PDF handout.

## Learn (20–30 min)

- What a pipeline is: YAML in the repo + an agent that runs it + a run history you can audit
- YAML vs Classic: YAML is versioned with the code; Classic lives in the service and drifts
- Agents and pools: Microsoft-hosted (cattle) vs self-hosted (pets) — deep dive tomorrow
- Parallel jobs: how many runs can execute at once on your org
- Docs: [What is Azure Pipelines?](https://learn.microsoft.com/azure/devops/pipelines/get-started/what-is-azure-pipelines)

## Hands-on lab (20–30 min)

1. Azure DevOps → **Pipelines** → **New pipeline** → Azure Repos Git → `azure-100-labs`
2. Starter YAML (or commit the file below on a feature branch, then PR — policies still apply)
3. Confirm:
   - `trigger: - main`
   - `pool: vmImage: ubuntu-latest`
   - One script step: `echo Hello from Day 21`
4. Run once. Open the job log. Confirm the Microsoft-hosted image name.
5. Optional: Org settings → **Pipelines** → disable Classic designer if you want YAML-only discipline
6. Write `docs/pipelines-day21.md` (what YAML vs Classic means for this repo)

## Commands / code

```yaml
# azure-pipelines.yml
trigger:
  - main

pool:
  vmImage: ubuntu-latest

steps:
  - script: echo Hello from Day 21
    displayName: Hello
```

## LinkedIn post (copy-paste)

**Important:** After pasting into LinkedIn, press Enter between sections so line breaks stay visible.

```
Day 21 of #100DaysOfAzureDevOps

Yesterday we closed Phase 2 — Git with receipts and policies.
Today Phase 3 begins: Azure Pipelines — CI as code, not as a wizard.

A pipeline is not “the build button in Azure DevOps.”
It is a YAML file in the repo, an agent that executes it, and a run you can audit later.

Three ideas I treat as the floor on Day 1 of CI:

1. YAML in Git
The pipeline is reviewed like any other change.
Classic editor is convenient. It is also configuration that lives outside the PR.

2. An agent actually runs it
Microsoft-hosted `ubuntu-latest` is cattle — fresh VM, then gone.
Self-hosted is a pet. Tomorrow we compare them honestly.

3. A run is evidence
Green or red, the log is the receipt.
If nobody can find the run, you do not have CI. You have folklore.

Lab today in azure-100-labs:
Committed azure-pipelines.yml (trigger on main, ubuntu-latest, echo Hello from Day 21), ran it once, and wrote down YAML vs Classic for this repo.

One-liner:
Pipelines are not robots that replace engineers.
They are the contract that stops you from being the robot.

Tomorrow: Microsoft-hosted vs self-hosted agents.

(Document attached: Day 21 Intro to Azure Pipelines handout PDF)

Lab notes + PDF also here:
https://bit.ly/4iWaf7t

#100DaysOfAzureDevOps #Azure #DevOps #AzurePipelines #CICD #CloudComputing #LearningInPublic
```

### Attach with the post (PDF handout)

Attach this document on LinkedIn (document / PDF upload):

- [`../days/day-21-intro-pipelines/handout.pdf`](../days/day-21-intro-pipelines/handout.pdf)

### How to post

1. LinkedIn → **document** → upload `days/day-21-intro-pipelines/handout.pdf`
2. Paste the text above (press **Enter** between sections so line breaks stay visible)
3. **Document title:** `Day 21 — Intro to Azure Pipelines` (max 58 chars on LinkedIn)

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5–10 real comments on other Azure/DevOps posts.

## Done checklist

- [ ] `azure-pipelines.yml` in the lab repo and a successful run
- [ ] Confirmed Microsoft-hosted `ubuntu-latest` in the job log
- [ ] `docs/pipelines-day21.md` written
- [ ] Published LinkedIn post with PDF handout
- [ ] Engaged with 5–10 community comments

## Tomorrow

**Day 22 — Microsoft-hosted vs Self-hosted Agents**

---

*Personal learning guide — views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
