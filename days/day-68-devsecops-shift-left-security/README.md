# Day 68 — DevSecOps - Shift-left Security

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 7 - Security, Compliance & Governance |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Build → Security → Deploy, with dependsOn — a parallel 'security job' is a race, not a gate

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Stage | Job | Gate |
| --- | --- | --- |
| Build | Compile / Docker@2 push to ACR | Must succeed before scans that need the image/artifact |
| Security | Day 67 scans + any image scan. Exit non-zero on written criteria | dependsOn: Build. Deploy must not start on failure |
| Deploy | ACI/AKS/App Service | dependsOn: Security. condition: succeeded() |
| PR validation | Same Security jobs on pull requests when you can | Main-only scans are how badness waits for merge |
| continueOnError | A confession on the Security job | If present, you have a dashboard of regret, not shift-left |

## Step-by-step lab

1. Reshape the pipeline into stages: Build, Security, Deploy. Security dependsOn Build. Deploy dependsOn Security with condition succeeded().
2. Move secret scan / SCA into Security. Keep fail-closed on secrets.
3. Write docs/security-gates-day68.md: fail criteria (secret=fail, critical=fail, high=…). Two sentences, not a novel.
4. Force a failure once (exit 1 in a throwaway step, or a fake finding). Confirm Deploy is skipped. If Deploy still runs, fix dependsOn/condition before anything else.
5. If PR pipelines exist, add the Security job there. Main-only is a note in the doc as a gap, not a boast.
6. Do not add continueOnError to look green on LinkedIn. Restore the pipeline to a passing dummy after the forced-fail proof.

## Done when

- [ ] Three stages in that order with dependsOn
- [ ] Forced failure skipped Deploy
- [ ] Fail criteria written in markdown
- [ ] continueOnError not on the Security gate

## LinkedIn

Post draft: [`../../daily-guides/day-68.md`](../../daily-guides/day-68.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-68-devsecops-shift-left-security
```

## Next

**Day 69** — Secure pipeline design — boring on purpose: approvals, locks, scoped connections
