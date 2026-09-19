# Day 67 — Compliance Scanning in Pipelines

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 7 - Security, Compliance & Governance |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Secret scan, SCA, SAST — publish SARIF; fail on high; a ignored scan is décor

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Scan | When it runs | What 'done' is |
| --- | --- | --- |
| Secret scanning | On the repo / PR (gitleaks, ADO secret scanning, GitHub push protection) | Build fails if a key-shaped string lands. Day 64 is wasted otherwise |
| SCA (dependencies) | On restore (pip-audit, npm audit, NuGet) | Lockfile + fail on high/critical. A lockfile without a scan is a list |
| SAST | On source (language analyzer if you have one) | Findings next to the commit. If you have no task, document the gap |
| SARIF | Static Analysis Results Interchange Format — JSON the tools emit | Publish the file (e.g. CodeAnalysisLogs). Humans and portals both ingest it |
| Collector products | Microsoft Defender for DevOps / Microsoft Security DevOps task can gather SARIF | A concept: one publisher of results. Not a marketplace shopping lab |

## Step-by-step lab

1. Add a secret-scan step (gitleaks in Docker is enough). --exit-code 1. Publish a SARIF file as an artifact if the tool can emit it.
2. Add a dependency scan on restore for whatever the sample app uses (npm audit --audit-level=high, pip-audit, etc.). Decide fail vs warn in a markdown file — not in your head.
3. Optional: Microsoft Security DevOps / Defender for DevOps as a SARIF collector — only if it is already easy. The concept is 'tools → SARIF → pipeline'. Do not spend the lab on a marketplace tour.
4. Run on a branch. If you need to prove fail, use a throwaway file with a clearly fake credential pattern and delete that commit. Do not commit Day 64's vault value.
5. Confirm results are visible without opening raw logs (summary, artifact, or annotations). continueOnError must be off for the secret step.
6. Write docs/scan-day67.md: tools used, fail criteria, SARIF yes/no. Tomorrow the Security stage wraps this.

## Done when

- [ ] Secret scan can fail the job
- [ ] Knows SAST vs SCA vs secrets as three jobs, not one brand
- [ ] SARIF treated as the interchange format, not a product name
- [ ] Fail criteria written; continueOnError not used as a gate

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-67-compliance-scanning-in-pipelines
```

## Next

**Day 68** — DevSecOps shift-left — Security stage before Deploy, not a final boss
