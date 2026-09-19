# Day 97 — Mock Interview Prep

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 10 - Portfolio & Public Launch |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Rehearse the happy path and the failure path — interviews are pipelines too

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Question | Happy path (say this) | Failure path (also say this) |
| --- | --- | --- |
| Promote the same artifact across envs? | One CI build; Environments download that artifact/digest | If you rebuild in prod, go back to Day 39 |
| Secret landed in a PR? | Rotate, treat the PR as an incident, rewrite history if needed | 'Delete the line and merge' leaves the secret in Git |
| Pipeline red Friday 17:00? | Who is affected, revert vs fix-forward with a clock | YOLO to prod to paint the dashboard green |
| Branching for this repo? | Trunk + PRs + path filters (your ADR) | A branching novel you cannot draw |
| Rollback after a bad deploy? | Redeploy last Build.BuildId / swap slot | Hotfix on main with no last-good |

## Step-by-step lab

1. Write the five questions in docs/mock-interview-day97.md with 4-bullet answers: artifact promotion, secret in a PR, Friday red pipeline, branching, rollback.
2. Add DORA: name the four metrics in one sentence each. Do not invent numbers you never measured.
3. Answer all five out loud. Record yourself once (phone voice memo is enough).
4. Listen once. If you ramble, tighten the bullets and say the weak answer again.
5. For any 'I do not know', write where you would look and what you would verify.
6. Do not include workplace-identifying stories. The capstone is the exhibit.

## Done when

- [ ] Five answers written as 4-bullet cards
- [ ] Recorded and listened once
- [ ] Happy path and failure path both spoken
- [ ] No invented DORA numbers, no employer-identifying story
- [ ] docs/mock-interview-day97.md on the personal repo

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-97-mock-interview-prep
```

## Next

**Day 98** — Professional profile setup — policy first, volume second
