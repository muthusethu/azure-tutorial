# Day 69 — Secure Pipeline Design

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 7 - Security, Compliance & Governance |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Who can edit YAML can ship — branch policy, env approvals, one connection per environment

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Control | Where | Failure if missing |
| --- | --- | --- |
| Branch policy on main | Repos → Branches → min reviewers + required build | A Contributor pushes to main and skips Security |
| Who can edit pipelines | Project → Pipelines security / repo ACL | Approvals are a speed bump around a hole — anyone rewrites Deploy |
| Environment approval | Pipelines → Environments → lab/prod → Approvals | deployment: job goes to prod from a feature branch unattended |
| Service connection scope | lab-sc → rg-lab. prod-sc → rg-prod. Not one azure Owner | Day 63 master key with a friendly name |
| Agent threat model | Hosted ubuntu-latest for these labs | Self-hosted with org-wide creds is lateral movement as a hobby |

## Step-by-step lab

1. Audit: Project Settings → Permissions / Pipelines. Who can edit pipeline YAML? Write the list (it may be only you). If Contributors can rewrite prod stages, note it as a finding.
2. Repos → Branches → main: require a pull request (even if you are the only reviewer in a personal org). Required check = the pipeline with Security.
3. Pipelines → Environments → create lab. Add an Approval (your user). Change Deploy to a deployment job with environment: lab.
4. Inspect lab-sc (and any second connection). Remove subscription Owner if present. Confirm it cannot see a RG you did not intend. Separate names if you already have a prod-shaped RG.
5. Re-check no secret echo / system.debug on Key Vault jobs. Tick a checklist file docs/secure-pipeline-day69.md: connections per env, no secret echo, main locked, approval on.
6. Do not use an employer org for this audit. Boring is the outcome.

## Done when

- [ ] Can name who can edit pipelines and who can approve lab
- [ ] main has a PR policy; Deploy uses environment: lab
- [ ] lab-sc is not subscription Owner
- [ ] docs/secure-pipeline-day69.md checklist ticked

## LinkedIn

Post draft: [`../../daily-guides/day-69.md`](../../daily-guides/day-69.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-69-secure-pipeline-design
```

## Next

**Day 70** — Phase 7 mini project — secret not in YAML, policy visible, approvals on
