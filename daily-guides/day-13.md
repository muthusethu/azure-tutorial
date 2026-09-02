# Day 13 — Azure Repos Setup & Repository Hygiene

| | |
|---|---|
| **Date** | 2 Sep 2026 |
| **Phase** | 2 — Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Configure `azure-100-labs` as a production-ready Azure Repos repository: default branch, standard folder layout, `.gitignore`, remote configuration, and basic permission awareness. Publish Day 13 on LinkedIn with the PDF handout.

## Learn (20–30 min)

- Azure Repos vs GitHub: same Git protocol, integrated with Boards, Pipelines, and PR policies
- Default branch naming (`main`), repo settings, and clone URLs (HTTPS vs SSH)
- Standard monorepo layout: `/src`, `/docs`, `/pipelines`, `/infra` — why structure beats chaos
- `.gitignore` essentials: never commit secrets, build artifacts, or local IDE noise
- Permissions overview: Readers, Contributors, Project Admins (branch policies deep dive on Day 19)
- Docs: [Create a new Git repo in Azure Repos](https://learn.microsoft.com/azure/devops/repos/git/create-new-repo) · [Ignore files](https://learn.microsoft.com/azure/devops/repos/git/ignore-files)

## Hands-on lab (20–30 min)

1. In Azure DevOps → **Repos** → **Project settings** → verify default branch is `main`
2. Locally in your `azure-100-labs` clone:
   ```bash
   git switch main
   git pull
   git switch -c feature/day13-repo-setup
   ```
3. Create standard folder structure:
   ```bash
   mkdir -p src docs pipelines infra notes
   touch src/.gitkeep docs/.gitkeep pipelines/.gitkeep infra/.gitkeep
   ```
4. Add a `.gitignore` (Node + general DevOps lab example):
   ```bash
   # Create .gitignore — see Commands section below
   ```
5. Add a short `docs/repo-structure.md` explaining each folder's purpose
6. Commit and push:
   ```bash
   git add .
   git commit -m "chore: standardize repo layout and gitignore"
   git push -u origin feature/day13-repo-setup
   ```
7. In Azure Repos → **Project settings** → **Repositories** → confirm repo permissions (Contributors can push to feature branches; `main` protection comes on Day 19)

## Commands / code

```bash
# .gitignore (Node + general lab)
node_modules/
dist/
build/
.env
.env.*
*.log
.DS_Store
.vscode/
__pycache__/
*.pyc
bin/
obj/

# docs/repo-structure.md skeleton
# /src      — application source code
# /docs     — ADRs, guides, architecture notes
# /pipelines — YAML pipeline definitions (Phase 3)
# /infra    — IaC templates (Phase 4+)
# /notes    — daily learning notes from #100DaysOfAzureDevOps

# Verify remote
git remote -v
git branch -a
```

## LinkedIn post (copy-paste)

**Important:** After pasting into LinkedIn, press Enter between sections so line breaks stay visible.

```
Day 13 of #100DaysOfAzureDevOps

Yesterday: branching strategies — GitFlow vs GitHub Flow vs Trunk-Based.
Today: how do you set up Azure Repos so the repo stays clean six months from now?

A messy repo root is not a personality trait.
It is a tax on every future PR, pipeline, and onboarding session.

Azure Repos is Git under the hood — but it lives inside your DevOps project, wired to Boards, Pipelines, and branch policies.

Setup decisions that pay off early:

1. Default branch = main
One production line. Clear default for clones, PRs, and pipeline triggers.

2. Standard folder layout
• /src — application code
• /docs — ADRs, architecture, runbooks
• /pipelines — CI/CD YAML (Phase 3)
• /infra — IaC templates (Phase 4+)

Future you should not grep the repo wondering where things live.

3. .gitignore on day one
Never commit node_modules/, .env, build artifacts, or IDE folders.
Secrets in git history do not un-commit themselves.

4. Remote hygiene
Know your clone URL (HTTPS or SSH), verify `git remote -v`, and push feature branches — not direct commits to main.

5. Permissions awareness
Readers view. Contributors push (with policies). Admins change settings.
Least privilege applies to repos too.

Lab today in azure-100-labs:
Standardized folder layout, added .gitignore, documented repo structure, and pushed feature/day13-repo-setup to Azure Repos.

One-liner:
Repo structure is infrastructure.
Set it up like you mean to maintain it.

Tomorrow: Pull requests & code review — the human gate before merge.

(Document attached: Day 13 Azure Repos Setup handout PDF)

Lab notes + PDF also here:
https://bit.ly/4xyn8cz

#100DaysOfAzureDevOps #Azure #DevOps #Git #AzureRepos #CloudComputing #LearningInPublic
```

### Attach with the post (PDF handout)

Attach this document on LinkedIn (document / PDF upload):

- [`../days/day-13-azure-repos-setup/handout.pdf`](../days/day-13-azure-repos-setup/handout.pdf)

### How to post

1. LinkedIn → **document** → upload `days/day-13-azure-repos-setup/handout.pdf`
2. Paste the text above (press **Enter** between sections so line breaks stay visible)
3. **Document title:** `Day 13 — Azure Repos Setup & Hygiene` (max 58 chars on LinkedIn)

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5–10 real comments on other Azure/DevOps posts.

## Done checklist

- [ ] Verified default branch is `main` in Azure Repos
- [ ] Created `/src`, `/docs`, `/pipelines`, `/infra` folder structure
- [ ] Added `.gitignore` and `docs/repo-structure.md`
- [ ] Pushed `feature/day13-repo-setup` to Azure Repos
- [ ] Published LinkedIn post with PDF handout
- [ ] Engaged with 5–10 community comments

## Tomorrow

**Day 14 — Pull Requests & Code Review**

---

*Personal learning guide — views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
