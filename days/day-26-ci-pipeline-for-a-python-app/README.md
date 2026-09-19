# Day 26 — CI Pipeline for a Python App

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 3 - Continuous Integration |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Pin the interpreter, then make ruff and pytest run on the agent — not on your laptop

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Piece | YAML / file | What it proves |
| --- | --- | --- |
| Interpreter | UsePythonVersion@0  versionSpec: '3.11' | Not leftover python3 on ubuntu-latest |
| Lockfile | requirements.txt (pytest, ruff pinned) | Next clone does not hunt a wiki |
| Lint | ruff check src/sample-python | Style + a class of bugs; own exit code |
| Tests | pytest -q --junitxml=$(Build.StagingDirectory)/junit.xml | Behavior. Do not merge with lint |
| Receipt | PublishTestResults@2 on that junit.xml | The run has evidence, not only a green job |

## Step-by-step lab

1. In the lab repo create src/sample-python/app.py (a tiny function) and tests/test_app.py with one pytest that asserts it.
2. Add src/sample-python/requirements.txt with pytest==8.* and ruff pinned. Commit on a feature branch — do not put secrets in the file.
3. Pipelines → New pipeline → Azure Repos Git → azure-100-labs. Point at pipelines/python-ci.yml (starter below).
4. Run once. Open the job log: confirm UsePythonVersion printed 3.11, ruff ran, pytest collected ≥1 item.
5. If ruff is noisy, keep || true for this lab only and write that debt in docs/python-ci-day26.md. Do not leave it unexplained.
6. Optional: add PublishTestResults@2. Confirm the Tests tab on the run shows the case. Screenshot no secrets.

## Done when

- [ ] UsePythonVersion@0 pinned 3.11 in the log — not 'whatever the image had'
- [ ] At least one pytest collected and passed on the agent
- [ ] requirements.txt is committed; no passwords in YAML
- [ ] Posted the LinkedIn document (personal account, no employer)

## LinkedIn

Post draft: [`../../daily-guides/day-26.md`](../../daily-guides/day-26.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-26-ci-pipeline-for-a-python-app
```

## Next

**Day 27** — CI for Java/Maven — JavaToolInstaller@0, the Maven lifecycle train, and mvn -B test.
