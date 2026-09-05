# Day 16 — Git Hooks & Pre-commit Checks

| | |
|---|---|
| **Date** | 5 Sep 2026 |
| **Phase** | 2 — Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Understand client-side Git hooks vs server-side policy gates, add a `commit-msg` convention check, and learn why local hooks are courtesy while Azure Repos branch policies are the real lock. Publish Day 16 on LinkedIn with the PDF handout.

## Learn (20–30 min)

- Client-side hooks: `pre-commit`, `commit-msg`, `pre-push` (live in `.git/hooks/` — not versioned by default)
- Framework option: [pre-commit.com](https://pre-commit.com/) for shared, installable hooks
- Conventional commit messages: `feat:`, `fix:`, `docs:`, `chore:`
- Critical DevOps truth: hooks can be skipped with `--no-verify` — put real gates on the server (PR build, branch policy, secret scan)
- Docs: [Git Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) · [Azure Repos branch policies](https://learn.microsoft.com/azure/devops/repos/git/branch-policies) (preview for Day 19)

## Hands-on lab (20–30 min)

1. In `azure-100-labs`:
   ```bash
   git switch main
   git pull
   git switch -c feature/day16-commit-hook
   ```
2. Create a sample `commit-msg` hook script in the repo for documentation (and optionally install locally):
   ```bash
   mkdir -p scripts/git-hooks
   ```
3. Add `scripts/git-hooks/commit-msg` (see Commands) and `docs/git-hooks.md` explaining:
   - How to install: copy to `.git/hooks/commit-msg` and make executable
   - Why `--no-verify` exists and why CI must still enforce quality
4. Install locally (Windows PowerShell example):
   ```powershell
   Copy-Item scripts/git-hooks/commit-msg .git/hooks/commit-msg
   ```
5. Prove it works:
   - Bad message → should fail: `git commit --allow-empty -m "bad message"`
   - Good message → should pass: `git commit --allow-empty -m "docs: add day 16 hook notes"`
6. Commit the hook script + docs, push the feature branch, open a PR

## Commands / code

```bash
# scripts/git-hooks/commit-msg
#!/bin/sh
# Require Conventional Commits-style messages for this lab
msg=$(head -n1 "$1")
echo "$msg" | grep -qE '^(feat|fix|docs|chore|refactor|test|ci)(\(.+\))?: .+' || {
  echo "Invalid commit message."
  echo "Use: feat: short description"
  echo "Allowed types: feat|fix|docs|chore|refactor|test|ci"
  exit 1
}
```

```powershell
# Install hook (Windows)
Copy-Item scripts\git-hooks\commit-msg .git\hooks\commit-msg

# Test (should fail)
git commit --allow-empty -m "bad message"

# Test (should pass)
git commit --allow-empty -m "docs: add day 16 hook notes"
```

## LinkedIn post (copy-paste)

**Important:** After pasting into LinkedIn, press Enter between sections so line breaks stay visible.

```
Day 16 of #100DaysOfAzureDevOps

Yesterday: Advanced Git — rebase, squash, history hygiene.
Today: Git hooks & pre-commit checks — local gates before the server gates.

A beautiful wiki that says "always run the linter" is not a control.
It is a suggestion.

Git hooks are scripts that run at lifecycle moments:
• pre-commit — before a snapshot is created
• commit-msg — validate the message format
• pre-push — last local chance before the remote sees it

They catch ugly messages, secrets in staged files, and broken formatting early.

But production taught a hard lesson:

Hooks that live only on a laptop can be skipped.
`--no-verify` exists.
Someone will use it under deadline pressure.

So treat hooks correctly:

1. Local hooks = developer courtesy (fast feedback)
2. Shared hook configs (pre-commit framework) = team consistency
3. Server gates = the real lock
   Azure Repos branch policies, required PR builds, secret scanning

If quality only exists as a local script, you do not have quality.
You have optimism.

Lab today in azure-100-labs:
Added a commit-msg hook requiring Conventional Commits, documented install steps, proved a bad message fails, and pushed feature/day16-commit-hook.

One-liner:
Local hooks are courtesy.
Branch policy is the lock.

Tomorrow: Fork workflows & permissions — who can push what, and why least privilege matters.

(Document attached: Day 16 Git Hooks & Pre-commit handout PDF)

Lab notes + PDF also here:
https://bit.ly/4gCudTt

#100DaysOfAzureDevOps #Azure #DevOps #Git #AzureRepos #Automation #CloudComputing #LearningInPublic
```

### Attach with the post (PDF handout)

Attach this document on LinkedIn (document / PDF upload):

- [`../days/day-16-git-hooks/handout.pdf`](../days/day-16-git-hooks/handout.pdf)

### How to post

1. LinkedIn → **document** → upload `days/day-16-git-hooks/handout.pdf`
2. Paste the text above (press **Enter** between sections so line breaks stay visible)
3. **Document title:** `Day 16 — Git Hooks & Pre-commit Checks` (max 58 chars on LinkedIn)

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5–10 real comments on other Azure/DevOps posts.

## Done checklist

- [ ] Explained client hooks vs server/branch policy gates
- [ ] Added `scripts/git-hooks/commit-msg` + docs
- [ ] Verified bad commit message fails locally
- [ ] Pushed feature branch / opened PR
- [ ] Published LinkedIn post with PDF handout
- [ ] Engaged with 5–10 community comments

## Tomorrow

**Day 17 — Fork Workflows & Permissions**

---

*Personal learning guide — views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
