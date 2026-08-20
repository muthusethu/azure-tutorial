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
Day 26 of #100DaysOfAzureDevOps

pytest is the friend who tells you the truth before your users do

Today's topic: **CI Pipeline for a Python App**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: CI for Java/Maven.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

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
