# Day 17 — Fork Workflows & Repo Permissions

| | |
|---|---|
| **Date** | 6 Sep 2026 |
| **Phase** | 2 — Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Compare fork-based contribution vs shared-repo feature branches, review Azure Repos security (Readers / Contributors / Project Admins), and document least-privilege rules for `main`. Publish Day 17 on LinkedIn with the PDF handout.

## Learn (20–30 min)

- **Shared-repo workflow:** everyone clones the same repo; feature branches + PRs into `main` (your lab default)
- **Fork workflow:** contributor forks → works in their copy → PR back to upstream (common for open source / external vendors)
- Azure Repos permissions: Readers, Contributors, Project Administrators; identity vs group assignment
- Dangerous permissions: Force push, Delete repository, Bypass policies
- Docs: [Azure Repos permissions](https://learn.microsoft.com/azure/devops/repos/git/set-git-repository-permissions) · [Forks](https://learn.microsoft.com/azure/devops/repos/git/forks)

## Hands-on lab (20–30 min)

1. In Azure DevOps → **Project settings** → **Repositories** → select `azure-100-labs`
2. Open **Security** and review:
   - Contributors: Contribute = Allow; Force push = Deny (or not set / inherited Deny on `main` via branch policy later)
   - Readers: Read only
3. Create branch and document your permission ADR:
   ```bash
   git switch main && git pull
   git switch -c feature/day17-repo-permissions
   mkdir -p docs
   ```
4. Add `docs/repo-permissions.md` covering:
   - Shared-repo vs fork: which you use for this lab and why
   - Contributors may push feature branches, not rewrite `main`
   - Force push Denied for Contributors
   - Who may change repo security (Project Admins only)
5. Commit, push, open PR

## Commands / code

```markdown
# docs/repo-permissions.md (ADR skeleton)

# Repo permissions — azure-100-labs
## Decision
Shared-repo + feature branches (not forks) for this personal lab.

## Permission baseline
| Identity | Contribute | Force push | Manage permissions |
|----------|------------|------------|--------------------|
| Readers | No | No | No |
| Contributors | Yes (feature/*) | Deny | No |
| Project Admins | Yes | Controlled | Yes |

## Why
Least privilege. Force-push on main is an incident, not a shortcut.
```

## LinkedIn post (copy-paste)

**Important:** After pasting into LinkedIn, press Enter between sections so line breaks stay visible.

```
Day 17 of #100DaysOfAzureDevOps

Yesterday: Git hooks — local courtesy vs server locks.
Today: Fork workflows & repo permissions — who can push what.

Permissions are seatbelts.
Annoying until someone force-pushes `main` into the sun.

Two contribution models:

1. Shared-repo workflow
• One Azure Repos project, many feature branches
• PRs into protected main
• Best for: internal teams who share ownership

2. Fork workflow
• Contributor works in their fork
• Opens PR back to upstream
• Best for: open source, vendors, external collaborators
• Isolation: their experiments never touch your default branch directly

Azure Repos security layers you should actually read:

• Readers — view only
• Contributors — push code (with policies)
• Project Admins — change settings and permissions

The permissions that cause real incidents:

• Force push on main
• Bypass branch policies
• Delete repository
• Manage permissions for everyone

Least privilege is not bureaucracy.
It is how you keep history and pipelines trustworthy.

Lab today in azure-100-labs:
Reviewed Repository Security for Contributors, documented a permissions ADR (shared-repo model, force push denied), and pushed feature/day17-repo-permissions.

One-liner:
Access is a production control.
If everyone is Admin, nobody is protected.

Tomorrow: Migrating repos to Azure Repos — moving history without losing trust.

(Document attached: Day 17 Fork Workflows & Permissions handout PDF)

Lab notes + PDF also here:
https://bit.ly/3UE039L

#100DaysOfAzureDevOps #Azure #DevOps #Git #AzureRepos #Security #CloudComputing #LearningInPublic
```

### Attach with the post (PDF handout)

Attach this document on LinkedIn (document / PDF upload):

- [`../days/day-17-fork-permissions/handout.pdf`](../days/day-17-fork-permissions/handout.pdf)

### How to post

1. LinkedIn → **document** → upload `days/day-17-fork-permissions/handout.pdf`
2. Paste the text above (press **Enter** between sections so line breaks stay visible)
3. **Document title:** `Day 17 — Fork Workflows & Permissions` (max 58 chars on LinkedIn)

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5–10 real comments on other Azure/DevOps posts.

## Done checklist

- [ ] Compared fork vs shared-repo contribution models
- [ ] Reviewed Azure Repos Security for Contributors / Readers
- [ ] Documented permissions ADR in `docs/repo-permissions.md`
- [ ] Published LinkedIn post with PDF handout
- [ ] Engaged with 5–10 community comments

## Tomorrow

**Day 18 — Migrating Repos to Azure Repos**

---

*Personal learning guide — views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
