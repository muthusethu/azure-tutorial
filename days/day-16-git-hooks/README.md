# Day 16 — Git Hooks & Pre-commit Checks

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 2 - Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

The bouncer at the commit club — ugly messages do not pass the rope

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Hook / check | Runs on | Can be bypassed? |
| --- | --- | --- |
| commit-msg (client) | git commit, reads $1 message file | Yes: --no-verify |
| pre-commit (client) | Before the commit object exists | Yes: --no-verify |
| pre-push (client) | Before objects send to origin | Yes: --no-verify |
| pre-commit.com framework | Dev machine via .pre-commit-config.yaml | Yes if not installed |
| Azure Repos branch policy | Server: PR cannot complete | No (unless you are admin bypass) |
| Pipeline build validation | CI job on the PR | No if required on the branch |

## Step-by-step lab

1. From repo root: copy the sample commit-msg to .git/hooks/commit-msg (Windows Git Bash: the hooks folder under .git).
2. On Windows, if the file is not executable, run the hook via Git Bash. Keep LF line endings.
3. git switch -c feature/day16-hooks && echo test > notes/day16.md && git add notes/day16.md
4. git commit -m "bad message" → expect the hook to reject (no type prefix).
5. git commit -m "docs: day 16 hook notes" → expect success.
6. Optional: add .pre-commit-config.yaml with repo: pre-commit-hooks, hook trailing-whitespace; pip install pre-commit && pre-commit install.
7. Push the markdown + any pre-commit config. Do not commit .git/hooks (it is not in the tree).

## Done when

- [ ] Can explain client hook vs branch policy vs pipeline check
- [ ] A bad commit message was rejected by commit-msg
- [ ] A conventional message succeeded and was pushed
- [ ] Understood --no-verify bypasses client hooks

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-16-git-hooks
```

## Next

**Day 17** — Fork workflows & permissions
