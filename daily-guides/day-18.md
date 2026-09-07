# Day 18 — Migrating Repos to Azure Repos

| | |
|---|---|
| **Date** | 7 Sep 2026 |
| **Phase** | 2 — Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Migrate (or import) a Git repository into Azure Repos with full history preserved, verify commits survive the move, and document a safe migration checklist (secrets, remotes, default branch). Publish Day 18 on LinkedIn with the PDF handout.

## Learn (20–30 min)

- Import options: Azure DevOps **Import repository** UI vs `git push --mirror` from a bare clone
- What migrates: commits, branches, tags — what does not: GitHub Actions secrets, PR comments, some webhooks
- TFVC vs Git: this series stays on Git only
- Post-migration hygiene: set default branch to `main`, update remotes, rotate any leaked credentials found in history
- Docs: [Import a Git repo](https://learn.microsoft.com/azure/devops/repos/git/import-git-repository) · [Push an existing repository](https://learn.microsoft.com/azure/devops/repos/git/share-your-code-in-git-cmdline)

## Hands-on lab (20–30 min)

1. In Azure Repos → create empty repo `imported-sample` (or Import from a small public GitHub URL)
2. Option A — Import UI: Repos → Import → paste a small public Git URL → verify Files + History
3. Option B — Mirror push (if Import is unavailable):
   ```bash
   git clone --bare https://github.com/<user>/<small-public-repo>.git
   cd <small-public-repo>.git
   git push --mirror https://dev.azure.com/<org>/azure-100-labs/_git/imported-sample
   ```
4. Clone the Azure Repos copy and verify history:
   ```bash
   git clone https://dev.azure.com/<org>/azure-100-labs/_git/imported-sample
   cd imported-sample
   git log --oneline -n 10
   git branch -a
   ```
5. Document checklist in `azure-100-labs` under `docs/repo-migration-checklist.md` (on a feature branch)

## Commands / code

```bash
# Mirror migration pattern
git clone --bare https://github.com/<user>/<small-repo>.git
cd <small-repo>.git
git push --mirror https://dev.azure.com/<org>/azure-100-labs/_git/imported-sample

# Verify
git log --oneline --decorate -n 10
git tag
git remote -v
```

## LinkedIn post (copy-paste)

**Important:** After pasting into LinkedIn, press Enter between sections so line breaks stay visible.

```
Day 18 of #100DaysOfAzureDevOps

Yesterday: forks & permissions — who can push what.
Today: Migrating repos to Azure Repos — moving history without losing trust.

A repo migration is not "copy the latest ZIP."
It is moving an audit trail.

What must survive the move:

• Full commit history (authors, dates, SHAs where possible)
• Branches and tags that production still references
• A verified default branch (`main`)

What often breaks if you rush:

• Remotes still pointing at the old host
• CI secrets and service connections left behind
• Webhooks / PR status checks that nobody rewired
• Credentials that lived in git history (they migrate with you)

Two safe patterns:

1. Azure Repos Import
Paste the source Git URL. Let Azure clone history into a new repo.

2. Bare clone + mirror push
`git clone --bare` then `git push --mirror` into an empty Azure Repos repo.
Use when you need full control of remotes and refs.

After migration, do not celebrate yet:

• `git log` — history present?
• `git branch -a` / tags — expected refs present?
• Default branch = main?
• Scan for secrets before opening the repo wider

Lab today:
Imported (or mirror-pushed) a sample repo into Azure Repos as imported-sample, verified commit history, and wrote a migration checklist for azure-100-labs.

One-liner:
Migration moves history.
Hygiene decides whether that history is an asset or a liability.

Tomorrow: Repo security hardening — policies that protect main after the move.

(Document attached: Day 18 Migrating Repos to Azure Repos handout PDF)

Lab notes + PDF also here:
https://bit.ly/3UVLPkD

#100DaysOfAzureDevOps #Azure #DevOps #Git #AzureRepos #CloudComputing #LearningInPublic
```

### Attach with the post (PDF handout)

Attach this document on LinkedIn (document / PDF upload):

- [`../days/day-18-migrating-repos/handout.pdf`](../days/day-18-migrating-repos/handout.pdf)

### How to post

1. LinkedIn → **document** → upload `days/day-18-migrating-repos/handout.pdf`
2. Paste the text above (press **Enter** between sections so line breaks stay visible)
3. **Document title:** `Day 18 — Migrating Repos to Azure Repos` (max 58 chars on LinkedIn)

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5–10 real comments on other Azure/DevOps posts.

## Done checklist

- [ ] Created / imported `imported-sample` in Azure Repos
- [ ] Verified `git log` shows pre-migration commits
- [ ] Documented migration checklist
- [ ] Published LinkedIn post with PDF handout
- [ ] Engaged with 5–10 community comments

## Tomorrow

**Day 19 — Repo Security (branch policies & protections)**

---

*Personal learning guide — views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
