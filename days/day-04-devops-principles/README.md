# Day 4 — DevOps Principles & Culture

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 1 - Azure & DevOps Foundations |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

CALMS is the habit. DORA is the receipt.

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Letter | What it looks like in Azure DevOps | Red flag |
| --- | --- | --- |
| Culture | Blameless notes in work items / PR comments | First question is 'who deployed?' |
| Automation | YAML pipeline on every main push (Phase 3) | Click-ops at midnight in Portal |
| Lean | Small PRs, WIP limit on Boards Doing column | Big-bang Friday release branch |
| Measurement | DORA four keys tracked weekly, even roughly | Only metric is ticket count |
| Sharing | docs/ in the repo + PR templates (Phase 2) | One person knows the release ritual |
| Not CALMS | Buying Azure DevOps seats with no pipeline | The sticker on the laptop |

## Step-by-step lab

1. Create a local folder ~/azure-100-notes (or C:\labs\azure-100-notes). No work laptop policy files.
2. Write docs/calms-dora-day04.md with a 1-5 score for Culture, Automation, Lean, Measurement, Sharing — last team or yourself, honestly.
3. Circle the weakest letter. Write three sentences: the habit you will build in this 100-day series.
4. Pick ONE DORA metric you can measure later (even 'pipeline runs on main per week'). Write the definition of done.
5. Skim the Four Keys article (Google Cloud blog on DORA). Copy the four names into the markdown — no employer data.
6. Optional: git init the notes folder locally so Day 11 has something real to commit. Do not push to a work remote.

## Done when

- [ ] Can recite CALMS without a slide
- [ ] Can name the four DORA metrics in order
- [ ] Filled a 1-5 scorecard and picked one metric to track
- [ ] No Azure resources created today (cost = 0)

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-04-devops-principles
```

## Next

**Day 5** — Azure DevOps Services overview
