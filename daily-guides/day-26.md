# Day 26 - CI Pipeline for a Python App

| | |
|---|---|
| **Date** | 15 Sep 2026 |
| **Phase** | 3 - Continuous Integration |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- pip, pytest, ruff/flake8

## Hands-on lab (20-30 min)

1. Add `/src/sample-python` with pytest
2. Pipeline: install, lint, pytest

## Commands / code

```bash
steps:
- task: UsePythonVersion@0
  inputs: { versionSpec: 3.11 }
- script: |
    python -m pip install --upgrade pip
    pip install pytest ruff
    cd src/sample-python
    ruff check . || true
    pytest -q
  displayName: Lint & test
```

## LinkedIn post (copy-paste)

```
pytest is the friend who tells you the truth before your users do.

Day 26 of #100DaysOfAzureDevOps. CI pipeline for a Python app.

Python CI looks optional until an import fails in production because the agent had a different implicit package. I have watched teams "just run the script" on a developer laptop, push, and discover that pytest was never in the pipeline because "we will add tests later." Later is a calendar that does not exist.

Today is a small sample: UsePythonVersion@0 at 3.11, pip, ruff, pytest. Lint that is allowed to warn in a lab is still lint you can see. Tests that do not run in CI are documentation of intent, not a safety net.

Patterns I keep seeing

1. Pin the interpreter
• UsePythonVersion@0 with 3.11 (or the version in .python-version)
• The agent image's leftover Python is not your runtime

2. Install tools in the job, not in folklore
• pip install pytest ruff in the pipeline so the next person is not hunting a wiki
• requirements.txt (even a short one) beats "it was on my machine"

3. Lint and test are different signals
• ruff check . catches style and a class of bugs early
• pytest -q tells you behavior; do not conflate them into one exit code you ignore

4. A failing lint in lab can be || true once — not forever
• I am allowing ruff to warn today so the first pipeline exists
• Leaving || true in a real main branch is how quality becomes optional

What I am doing in today's lab

I am adding /src/sample-python with at least one pytest, then a pipeline that upgrades pip, installs pytest and ruff, runs ruff check, and runs pytest -q. Green means the interpreter, the tools, and the tests agreed in CI — not that I ran a file locally.

Users will test your Python if you will not. pytest is cheaper.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-26-ci-pipeline-for-a-python-app

Tomorrow: CI for Java/Maven — lifecycle, tests, and not jumping off the train early.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 26 — CI Pipeline for a Python App` (max 58 chars)
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

**CI for Java/Maven**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
