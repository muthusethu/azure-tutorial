# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Generate 100 day-by-day Azure DevOps learning guides."""

from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "daily-guides"

# date, topic, learn bullets, lab steps, code block (optional), post hook idea, tomorrow
DAYS = [
    # Phase 1
    (
        1,
        "21 Aug 2026",
        "Cloud Computing & Azure Fundamentals",
        [
            "IaaS vs PaaS vs SaaS - who owns the OS, platform, and app",
            "Azure global infrastructure: geographies, regions, paired regions",
            "Availability Zones vs Availability Sets (high-level)",
            "Skim: https://learn.microsoft.com/azure/cloud-adoption-framework/ready/azure-setup-guide/regions",
        ],
        [
            "Create/confirm a personal Microsoft account (not work SSO)",
            "Open Azure Portal ? Subscriptions ? note subscription name + ID",
            "Create a Cost Management budget alert (e.g. ?500 or $20)",
            "Create resource group `rg-day01-lab` in Central India (or nearest)",
            "Browse: create a free-tier resource page but do NOT deploy yet",
            "Delete nothing critical - just confirm you can navigate Portal",
        ],
        """# No code today - navigation only.
# Optional: open Cloud Shell and run:
az account show --output table
az group list --output table""",
        "restaurant metaphor: IaaS kitchen / PaaS shared kitchen / SaaS takeout; region=city; zone=building",
        "Azure Portal, CLI & PowerShell basics",
    ),
    (
        2,
        "22 Aug 2026",
        "Azure Portal, CLI & PowerShell Basics",
        [
            "When to use Portal vs CLI vs PowerShell",
            "Install Azure CLI; sign-in with `az login`",
            "Resource groups, subscriptions, naming conventions (rg-, app-, pip-)",
            "Docs: https://learn.microsoft.com/cli/azure/install-azure-cli",
        ],
        [
            "Install Azure CLI on your personal PC",
            "Run `az login` and select personal subscription",
            "Create RG `rg-day02-lab` via CLI",
            "Create the same RG shape via Portal once (compare clicks vs commands)",
            "List and delete the RG (or leave empty and delete tomorrow)",
        ],
        """# Install: https://aka.ms/installazurecliwindows
az login
az account set --subscription "<your-subscription-name-or-id>"
az group create --name rg-day02-lab --location centralindia
az group show --name rg-day02-lab --output jsonc
az group delete --name rg-day02-lab --yes --no-wait""",
        "Portal is the map; CLI is GPS with coordinates; PowerShell is the Swiss-army knife - pick the tool by job size",
        "Azure Resource Manager (ARM) basics",
    ),
    (
        3,
        "23 Aug 2026",
        "Azure Resource Manager (ARM) Basics",
        [
            "Resource providers, management groups, subscriptions, RGs",
            "Tags for cost + ownership; resource locks (CanNotDelete)",
            "ARM is the control plane - every Portal click becomes an ARM call",
            "Docs: https://learn.microsoft.com/azure/azure-resource-manager/management/overview",
        ],
        [
            "Create `rg-day03-lab` with tags: Project=100Days, Owner=personal, Env=lab",
            "Add a CanNotDelete lock, try deleting (should fail), remove lock, delete RG",
            "List resource providers: `az provider list --query [].namespace -o tsv | more`",
        ],
        """az group create -n rg-day03-lab -l centralindia \\
  --tags Project=100Days Owner=personal Env=lab
az lock create --name cannot-delete --lock-type CanNotDelete \\
  --resource-group rg-day03-lab
# Try: az group delete -n rg-day03-lab --yes   # should fail while locked
az lock delete --name cannot-delete --resource-group rg-day03-lab
az group delete -n rg-day03-lab --yes --no-wait""",
        "Tags are sticky notes for Finance; locks are duct tape so nobody deletes prod by accident",
        "DevOps principles & culture",
    ),
    (
        4,
        "24 Aug 2026",
        "DevOps Principles & Culture",
        [
            "CALMS: Culture, Automation, Lean, Measurement, Sharing",
            "DevOps lifecycle vs Agile (complement, not replace)",
            "DORA metrics: deployment frequency, lead time, CFR, MTTR",
            "Article: https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance",
        ],
        [
            "Write 5 lines in a notebook: where your current team is weak on CALMS",
            "Pick one DORA metric you could measure for a personal lab project",
            "No Azure spend today - concepts only + LinkedIn post",
        ],
        """# Optional personal scorecard (fill honestly 1-5)
# Culture: _
# Automation: _
# Lean: _
# Measurement: _
# Sharing: _""",
        "DevOps is not a job title with a fancy laptop sticker - CALMS + DORA are how you tell if the sticker is lying",
        "Azure DevOps Services overview",
    ),
    (
        5,
        "25 Aug 2026",
        "Azure DevOps Services Overview",
        [
            "Boards, Repos, Pipelines, Test Plans, Artifacts - how they connect",
            "Azure DevOps vs GitHub (high-level; you will use both)",
            "Docs: https://learn.microsoft.com/azure/devops/user-guide/what-is-azure-devops",
        ],
        [
            "Create personal org at https://dev.azure.com (e.g. yourname-100days)",
            "Create project `day05-overview` (Agile process, private)",
            "Open each hub once: Boards ? Repos ? Pipelines ? Test Plans ? Artifacts",
            "Screenshot the left nav for your notes (do not post screenshots of private data)",
        ],
        """# No CLI required. Bookmark:
# https://dev.azure.com/<your-org>/<your-project>
# Hubs to click: Overview, Boards, Repos, Pipelines, Test Plans, Artifacts""",
        "Azure DevOps is five apps pretending to be one - Boards plan, Repos store, Pipelines ship, Tests prove, Artifacts package",
        "Setting up an Azure DevOps organization",
    ),
    (
        6,
        "26 Aug 2026",
        "Setting Up an Azure DevOps Org",
        [
            "Organizations, projects, process templates (Agile / Scrum / CMMI)",
            "Permissions: Project Collection Admins vs Contributors",
            "Keep this org personal-only",
        ],
        [
            "In org settings: check Overview, Users, Permissions",
            "Create project `azure-100-labs` (this becomes your home project for 100 days)",
            "Invite nobody from work. Use personal Microsoft account only",
            "Set project description: 'Personal 100DaysOfAzureDevOps labs - views my own'",
        ],
        """# Azure DevOps CLI (optional install: az extension add --name azure-devops)
az extension add --name azure-devops
az devops configure --defaults organization=https://dev.azure.com/<your-org> project=azure-100-labs
az devops project list -o table""",
        "Your Azure DevOps org is a gym membership - empty projects don't build muscle; daily reps do",
        "Azure Boards deep dive",
    ),
    (
        7,
        "27 Aug 2026",
        "Azure Boards Deep Dive",
        [
            "Work items: Epic ? Feature ? User Story ? Task/Bug",
            "Backlogs, sprints, Kanban boards, queries, dashboards",
            "Docs: https://learn.microsoft.com/azure/devops/boards/get-started/what-is-azure-boards",
        ],
        [
            "In `azure-100-labs`, create Epic '100 Days Learning'",
            "Add Feature 'Phase 1 Foundations' + 3 User Stories for Days 8-10",
            "Move one story across To Do ? Doing ? Done on the board",
            "Create a simple query: Work Item Type = User Story AND State <> Done",
        ],
        """# Example story titles:
# - Explore Azure Test Plans
# - Create Azure Artifacts feed
# - Stand up end-to-end mini project""",
        "Boards without WIP limits are sticky-note chaos with better fonts - limit work in progress or the board owns you",
        "Azure Test Plans basics",
    ),
    (
        8,
        "28 Aug 2026",
        "Azure Test Plans Basics",
        [
            "Manual test cases, test plans vs suites, exploratory testing",
            "When teams actually use Test Plans vs automated tests in CI",
            "Docs: https://learn.microsoft.com/azure/devops/test/overview",
        ],
        [
            "Enable Test Plans if needed (Basic + Test Plans trial / included SKUs vary)",
            "Create Test Plan 'Day08 Smoke' with one suite 'Portal checks'",
            "Add 2 manual test cases: 'Login to Portal', 'Create RG via CLI'",
            "Mark one Passed, one Blocked - note the workflow",
        ],
        """# Test case outline (paste into Azure DevOps Test Case steps):
# 1. Open portal.azure.com
# 2. Confirm correct personal directory
# 3. Expected: subscription visible, no work tenant""",
        "A test plan is a shared checklist so 'it works on my machine' stops being a personality trait",
        "Azure Artifacts",
    ),
    (
        9,
        "29 Aug 2026",
        "Azure Artifacts",
        [
            "Feeds, views, upstream sources (NuGet, npm, Maven, Python)",
            "Why private feeds beat 'copy DLLs in email'",
            "Docs: https://learn.microsoft.com/azure/devops/artifacts/start-using-azure-artifacts",
        ],
        [
            "Create feed `day09-packages` (project-scoped)",
            "Enable upstream sources for nuget.org and npmjs (if prompted)",
            "Note feed URL - you will use it in Phase 3 CI",
            "Do not publish secrets. Empty feed is fine for today",
        ],
        """# Later (Phase 3) you will connect like:
# nuget.config ? packageSources ? your Azure Artifacts feed URL
# For today: copy Feed settings ? Connect to feed ? save URL in notes""",
        "Artifacts are the pantry - Pipelines cook dinner; without a feed you keep re-buying the same flour every build",
        "Mini project + recap",
    ),
    (
        10,
        "30 Aug 2026",
        "Mini Project + Recap (Phase 1)",
        [
            "Stand up a complete Azure DevOps project end-to-end",
            "Recap Phase 1 for LinkedIn (what stuck, what was confusing)",
        ],
        [
            "Ensure project `azure-100-labs` has: 1 Epic, backlog items, empty Git repo, Artifacts feed",
            "Initialize repo with README (see code)",
            "Create dashboard widget: query chart of your Phase 1 stories",
            "Delete leftover RGs from Days 1-3 if any still exist",
        ],
        """# In azure-100-labs ? Repos ? Files ? Initialize with README
# Or locally:
git clone https://dev.azure.com/<org>/azure-100-labs/_git/azure-100-labs
cd azure-100-labs
echo "# Azure 100 Labs" > README.md
echo "Personal learning repo for #100DaysOfAzureDevOps" >> README.md
git add README.md && git commit -m "docs: bootstrap lab repo" && git push""",
        "Phase 1 recap: cloud models, Portal/CLI, ARM, CALMS/DORA, and the five Azure DevOps hubs - foundations before pipelines",
        "Git fundamentals",
    ),
    # Phase 2
    (
        11,
        "31 Aug 2026",
        "Git Fundamentals",
        [
            "Mental model: working tree ? staging ? commit ? remote",
            "init, clone, add, commit, branch, merge, status, log",
            "Book: Pro Git ch.1-3 (skim) https://git-scm.com/book/en/v2",
        ],
        [
            "In lab repo: create file `notes/day11.md`, commit, push",
            "Create branch `feature/day11-notes`, edit, merge to main via local merge OR PR tomorrow",
            "Practice `git status` and `git log --oneline -5` until muscle memory",
        ],
        """git status
git checkout -b feature/day11-notes
mkdir -p notes
echo "Day 11: Git mental model" > notes/day11.md
git add notes/day11.md
git commit -m "docs: day 11 git fundamentals notes"
git push -u origin feature/day11-notes""",
        "Git is time travel with extra anxiety - commits are save points; branches are parallel universes you can still mess up",
        "Branching strategies",
    ),
    (
        12,
        "01 Sep 2026",
        "Branching Strategies",
        [
            "Git Flow vs GitHub Flow vs trunk-based development",
            "When teams should recommend trunk-based + short PRs",
            "Article: https://trunkbaseddevelopment.com/",
        ],
        [
            "Write a 1-page ADR in repo: `docs/branching-strategy.md` choosing one strategy for this lab",
            "Document: main protected, feature/* short-lived, no develop branch for this project",
        ],
        """# docs/branching-strategy.md
# Decision: GitHub Flow (trunk-based lite)
# - main is always deployable
# - feature/* branches < 2 days
# - PR required; squash merge
# - No long-lived release branches in this lab""",
        "Git Flow is a wedding seating chart; trunk-based is a food truck - pick complexity that matches team size",
        "Azure Repos setup",
    ),
    (
        13,
        "02 Sep 2026",
        "Azure Repos Setup",
        [
            "Repo creation, default branch, folder structure standards",
            "Repo policies overview (deep dive day 19)",
        ],
        [
            "Set default branch to `main`",
            "Create folders: `/src`, `/docs`, `/pipelines`, `/infra`",
            "Add `.gitignore` for your language (dotnet/node/python)",
        ],
        """# .gitignore (Node example)
node_modules/
dist/
.env
*.log
.DS_Store""",
        "A messy repo root is a messy brain - /src /docs /pipelines /infra saves future-you from archaeology",
        "Pull requests & code review",
    ),
    (
        14,
        "03 Sep 2026",
        "Pull Requests & Code Review",
        [
            "PR templates, reviewers, linked work items, review etiquette",
            "Docs: https://learn.microsoft.com/azure/devops/repos/git/pull-requests",
        ],
        [
            "Add `.azuredevops/pull_request_template.md`",
            "Open PR from a feature branch; link a work item",
            "Self-review checklist: title, description, screenshots/none, test plan",
        ],
        """# .azuredevops/pull_request_template.md
## What
-
## Why
-
## Test plan
- [ ] Local build
- [ ] Linked work item
## Risk
- Low / Med / High""",
        "A PR without a description is a mystery novel where the murderer is 'I was in a hurry'",
        "Advanced Git",
    ),
    (
        15,
        "04 Sep 2026",
        "Advanced Git",
        [
            "Rebase vs merge, cherry-pick, squash, interactive rebase, conflicts",
            "Never rebase shared main; rebase your feature onto main",
        ],
        [
            "Create conflicting edits on purpose on two branches; resolve conflict",
            "Practice squash merge via Azure DevOps PR settings (or local soft reset)",
            "Write 5 lines: when you choose merge commit vs squash vs rebase",
        ],
        """git fetch origin
git checkout feature/day15
git rebase origin/main
# fix conflicts ? git add . ? git rebase --continue
git push --force-with-lease""",
        "Rebase rewrites history; merge preserves the plot twists - choose based on whether your teammates are watching that timeline",
        "Git hooks & pre-commit",
    ),
    (
        16,
        "05 Sep 2026",
        "Git Hooks & Pre-commit Checks",
        [
            "Client-side hooks; pre-commit framework; commit message conventions",
            "https://pre-commit.com/",
        ],
        [
            "Add a simple pre-commit config OR a sample `commit-msg` hook that requires 'dayNN:' prefix for this lab",
            "Make a bad commit message and watch it fail (then fix)",
        ],
        """# .git/hooks/commit-msg (sample; chmod +x on mac/linux)
#!/bin/sh
grep -qE '^(docs|feat|fix|chore|day)(\\(.+\\))?: .+' "$1" || {
  echo "Commit message must look like: feat: short description"
  exit 1
}""",
        "Hooks are the bouncer at the commit club - ugly messages do not get past the velvet rope",
        "Fork workflows & permissions",
    ),
    (
        17,
        "06 Sep 2026",
        "Fork Workflows & Repo Permissions",
        [
            "Fork-based contribution vs branch permissions inside one repo",
            "Granular repo permissions in Azure DevOps",
        ],
        [
            "Review Project Settings ? Repositories ? Security for Contributors",
            "Document: contributors can contribute, cannot force-push main",
            "Optional: create GitHub mirror of the same learning notes (public later)",
        ],
        """# Notes only - no mandatory code
# Project Settings ? Repositories ? [repo] ? Security
# Deny: Force push on main for Contributors""",
        "Permissions are seatbelts - annoying until the day someone force-pushes main into the sun",
        "Migrating repos to Azure Repos",
    ),
    (
        18,
        "07 Sep 2026",
        "Migrating Repos to Azure Repos",
        [
            "Import from GitHub/GitLab; history preservation",
            "TFVC mention only - you will stay on Git",
        ],
        [
            "Create empty repo `imported-sample`",
            "Import a small public GitHub repo OR push an existing local git history",
            "Verify `git log` still shows old commits",
        ],
        """# Option A: Azure DevOps ? Repos ? Import
# Option B:
git clone --bare https://github.com/<user>/<small-repo>.git
cd <small-repo>.git
git push --mirror https://dev.azure.com/<org>/azure-100-labs/_git/imported-sample""",
        "Migrations are moving apartments - history is the furniture; leave the broken IKEA shelf (secrets) behind",
        "Repo security",
    ),
    (
        19,
        "08 Sep 2026",
        "Repo Security",
        [
            "Branch policies: reviewers, work items, build validation, status checks",
            "Docs: https://learn.microsoft.com/azure/devops/repos/git/branch-policies",
        ],
        [
            "On `main`: require 1 reviewer (yourself ok for lab), require linked work item",
            "Limit merge types to squash",
            "Try pushing directly to main - should fail if policy set correctly",
        ],
        """# Azure DevOps UI:
# Repos ? Branches ? main ? Branch policies
# - Require a minimum number of reviewers: 1
# - Check for linked work items: Required
# - Limit merge types: Squash merge""",
        "Branch policies are parental controls for adults who still push to main at 11:58pm",
        "Phase 2 mini project",
    ),
    (
        20,
        "09 Sep 2026",
        "Mini Project + Recap (Phase 2)",
        [
            "Configure branch policy + full PR workflow on sample repo",
            "Publish Phase 2 recap",
        ],
        [
            "End-to-end: branch ? commit ? PR ? review notes ? squash merge ? delete branch",
            "Confirm policies blocked a non-compliant PR once",
            "Update README with 'How we use Git here' section",
        ],
        """git checkout -b feature/day20-recap
echo "## Git workflow\\nSee docs/branching-strategy.md" >> README.md
git add README.md && git commit -m "docs: document git workflow"
git push -u origin feature/day20-recap
# Open PR in Azure DevOps, complete squash merge""",
        "Phase 2 recap: Git is not 'save file' - it is collaboration with receipts, policies, and fewer 2am disasters",
        "Intro to Azure Pipelines",
    ),
]

# Continue days 21-100 with condensed but complete generators
PHASE_EXTRA = []


def entertaining_post(day, date, topic, hook, tomorrow):
    return f"""Day {day} of #100DaysOfAzureDevOps

{hook}

Today's topic: **{topic}**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: {tomorrow}.

#Azure #DevOps #CloudComputing #100DaysOfCode"""


def render(day, date, topic, learn, lab, code, hook, tomorrow, phase):
    learn_md = "\n".join(f"- {x}" for x in learn)
    lab_md = "\n".join(f"{i}. {x}" for i, x in enumerate(lab, 1))
    post = entertaining_post(day, date, topic, hook, tomorrow)
    return f"""# Day {day} - {topic}

| | |
|---|---|
| **Date** | {date} |
| **Phase** | {phase} |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

{learn_md}

## Hands-on lab (20-30 min)

{lab_md}

## Commands / code

```bash
{code.strip()}
```

## LinkedIn post (copy-paste)

```
{post}
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

**{tomorrow}**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
"""


def phase_for(day: int) -> str:
    names = [
        (1, 10, "1 - Azure & DevOps Foundations"),
        (11, 20, "2 - Azure Repos & Git Mastery"),
        (21, 30, "3 - Continuous Integration"),
        (31, 40, "4 - Continuous Delivery"),
        (41, 50, "5 - Infrastructure as Code"),
        (51, 60, "6 - Containers & Kubernetes"),
        (61, 70, "7 - Security, Compliance & Governance"),
        (71, 80, "8 - Monitoring & Observability"),
        (81, 90, "9 - Advanced & Enterprise"),
        (91, 100, "10 - Portfolio & Public Launch"),
    ]
    for a, b, n in names:
        if a <= day <= b:
            return n
    return "?"


# Days 21-100 curriculum tuples (compact)
MORE = [
    (21, "10 Sep 2026", "Intro to Azure Pipelines",
     ["Agents, pools, parallel jobs", "YAML vs Classic editor", "https://learn.microsoft.com/azure/devops/pipelines/get-started/what-is-azure-pipelines"],
     ["Create empty pipeline YAML that only runs `echo Hello`", "Note Microsoft-hosted agent image `ubuntu-latest`", "Disable Classic if you want YAML-only discipline"],
     """# azure-pipelines.yml
trigger:
  - main
pool:
  vmImage: ubuntu-latest
steps:
  - script: echo Hello from Day 21
    displayName: Hello""",
     "Pipelines are robots that run your build so you can stop being the robot",
     "Microsoft-hosted vs self-hosted agents"),
    (22, "11 Sep 2026", "Microsoft-hosted vs Self-hosted Agents",
     ["When to self-host", "Scale sets, capabilities, trade-offs"],
     ["Compare hosted vs self-hosted in docs", "List agent pools in org settings", "Decide: hosted for all 100-day labs unless you need private network"],
     """# Prefer for labs:
pool:
  vmImage: ubuntu-latest
# Self-hosted later when you need VPN / licensed software""",
     "Hosted agents are Uber; self-hosted is owning the car - insurance and parking included",
     "YAML pipeline basics"),
    (23, "12 Sep 2026", "YAML Pipeline Basics",
     ["Triggers, stages, jobs, steps, syntax", "https://learn.microsoft.com/azure/devops/pipelines/yaml-schema"],
     ["Expand hello pipeline into stages Build ? Test (Test can be echo)", "Add a PR trigger", "Read pipeline run logs end-to-end"],
     """trigger:
  branches:
    include: [ main ]
pr:
  branches:
    include: [ main ]
stages:
- stage: Build
  jobs:
  - job: BuildJob
    pool: {{ vmImage: ubuntu-latest }}
    steps:
    - script: echo Building...
- stage: Test
  dependsOn: Build
  jobs:
  - job: TestJob
    pool: {{ vmImage: ubuntu-latest }}
    steps:
    - script: echo Testing...""".replace("{{", "{").replace("}}", "}"),
     "YAML pipelines are Lego instructions written by someone who enjoys whitespace arguments",
     "CI pipeline for a .NET app"),
    (24, "13 Sep 2026", "CI Pipeline for a .NET App",
     ["dotnet restore/build/test/publish", "Pipeline artifacts"],
     ["Create `/src/SampleApi` minimal Web API OR use `dotnet new webapi`", "Add pipeline restore?build?test?publish", "Publish pipeline artifact"],
     """# pipelines/dotnet-ci.yml
trigger:
  paths:
    include: [ src/SampleApi/** ]
pool:
  vmImage: ubuntu-latest
steps:
- task: UseDotNet@2
  inputs:
    packageType: sdk
    version: 8.x
- script: |
    dotnet restore src/SampleApi
    dotnet build src/SampleApi -c Release --no-restore
    dotnet test src/SampleApi -c Release --no-build || true
  displayName: Build
- task: PublishBuildArtifacts@1
  inputs:
    PathtoPublish: src/SampleApi/bin/Release
    ArtifactName: drop""",
     ".NET CI is the same ritual every time: restore, build, test, publish - skip one and production finds it for you",
     "CI for Node.js"),
    (25, "14 Sep 2026", "CI Pipeline for a Node.js App",
     ["npm ci/build/test", "Cache node_modules"],
     ["Add tiny Node app under `/src/sample-node`", "Pipeline with Cache@2 and npm test"],
     """# src/sample-node/package.json - minimal
# {{ "name": "sample-node", "scripts": {{ "test": "node -e \\"console.log('ok')\\"" }} }}
steps:
- task: NodeTool@0
  inputs: {{ versionSpec: 20.x }}
- task: Cache@2
  inputs:
    key: 'npm | "$(Agent.OS)" | src/sample-node/package-lock.json'
    path: src/sample-node/node_modules
- script: |
    cd src/sample-node
    npm ci
    npm test
  displayName: npm ci & test""".replace("{{", "{").replace("}}", "}"),
     "Node CI without caching is watching paint dry while paying Microsoft for the privilege",
     "CI for Python"),
    (26, "15 Sep 2026", "CI Pipeline for a Python App",
     ["pip, pytest, ruff/flake8"],
     ["Add `/src/sample-python` with pytest", "Pipeline: install, lint, pytest"],
     """steps:
- task: UsePythonVersion@0
  inputs: {{ versionSpec: 3.11 }}
- script: |
    python -m pip install --upgrade pip
    pip install pytest ruff
    cd src/sample-python
    ruff check . || true
    pytest -q
  displayName: Lint & test""".replace("{{", "{").replace("}}", "}"),
     "pytest is the friend who tells you the truth before your users do",
     "CI for Java/Maven"),
    (27, "16 Sep 2026", "CI Pipeline for a Java/Maven App",
     ["Maven lifecycle, unit tests, packaging"],
     ["Optional: skip deep Java if not your stack - read a sample Maven pipeline instead", "Or `mvn -B test` on a tiny archetype project"],
     """steps:
- task: JavaToolInstaller@0
  inputs:
    versionSpec: 17
    jdkArchitectureOption: x64
    jdkSourceOption: PreInstalled
- script: mvn -B -f src/sample-java/pom.xml test
  displayName: Maven test""",
     "Maven phases are a train: compile ? test ? package - jumping off early dumps jars on the tracks",
     "Multi-stage YAML"),
    (28, "17 Sep 2026", "Multi-stage YAML Pipelines",
     ["dependsOn, conditions, matrix, parallel"],
     ["Add matrix for Node 18/20 OR python versions", "Add condition: succeeded() on deploy stage stub"],
     """strategy:
  matrix:
    node18: {{ version: 18.x }}
    node20: {{ version: 20.x }}
steps:
- task: NodeTool@0
  inputs:
    versionSpec: $(version)""".replace("{{", "{").replace("}}", "}"),
     "Matrix builds are cloning yourself across versions so 'works on my Node' becomes 'works on these Nodes'",
     "Variables, groups & secrets"),
    (29, "18 Sep 2026", "Pipeline Variables, Groups & Secrets",
     ["Runtime vs compile-time vars", "Variable groups; Key Vault link preview"],
     ["Create variable group `lab-common`", "Store a dummy secret (not real passwords)", "Reference $(myVar) in pipeline"],
     """variables:
- group: lab-common
steps:
- script: echo "App name is $(appName)"
  displayName: Use variable""",
     "Secrets in YAML are postcards - variable groups and Key Vault are envelopes",
     "Phase 3 mini project"),
    (30, "19 Sep 2026", "Mini Project + Recap (Phase 3)",
     ["CI for multi-language sample OR one solid language + stub others"],
     ["Pick your primary stack; green build on main", "Recap post: YAML anatomy + one war story from today"],
     """# Keep pipelines/ under repo; badge optional later
# Goal: one green CI run you can screenshot (no secrets in screenshot)""",
     "Phase 3 recap: CI is a seatbelt you wear before the crash, not after",
     "Release pipelines overview"),
    (31, "20 Sep 2026", "Release Pipelines Overview",
     ["Classic release vs multi-stage YAML CD"],
     ["Prefer YAML CD for labs", "Create environment `dev` in Pipelines ? Environments"],
     """stages:
- stage: DeployDev
  jobs:
  - deployment: Deploy
    environment: dev
    strategy:
      runOnce:
        deploy:
          steps:
          - script: echo Deploying to dev""",
     "Classic releases are the old mall; YAML CD is the street you actually live on now",
     "Deploy to App Service"),
    (32, "21 Sep 2026", "Deploying to Azure App Service",
     ["Web App deploy, zip deploy, slots overview"],
     ["Create free/F1 App Service plan + webapp in personal RG", "Deploy hello app from pipeline", "Delete RG tonight if cost-sensitive"],
     """- task: AzureWebApp@1
  inputs:
    azureSubscription: <service-connection>
    appName: <webapp-name>
    package: $(Pipeline.Workspace)/drop/**/*.zip""",
     "App Service is PaaS comfort food - less drama than VMs, still enough knobs to burn dinner",
     "Deploy to Azure Functions"),
    (33, "22 Sep 2026", "Deploying to Azure Functions",
     ["Consumption vs Premium", "Function app CD"],
     ["Create Function App (Consumption) OR read-only lab if quota tight", "Deploy a timer/http sample"],
     """- task: AzureFunctionApp@2
  inputs:
    azureSubscription: <service-connection>
    appType: functionApp
    appName: <function-name>
    package: $(System.DefaultWorkingDirectory)/**/*.zip""",
     "Functions are micro-managers that only wake up when work arrives - and still send you a bill for the nap",
     "Deployment slots"),
    (34, "23 Sep 2026", "Deployment Slots & Swap Strategies",
     ["Staging slots, swap, warm-up, auto-swap"],
     ["If SKU allows: create staging slot, deploy, swap", "Document warm-up path"],
     """# Portal: Web App ? Deployment slots ? Add slot `staging`
# Swap staging ? production after smoke test""",
     "Slots are dressing rooms for production - try the outfit on before walking the runway",
     "Blue-green deployments"),
    (35, "24 Sep 2026", "Blue-Green Deployments",
     ["Concept + App Service implementation; AKS later", "Rollback story"],
     ["Map blue-green onto slots: blue=prod, green=staging", "Write rollback steps in `/docs/rollback.md`"],
     """# docs/rollback.md
# 1. Swap back staging/production
# 2. Verify health endpoint
# 3. Keep previous artifact for 7 days""",
     "Blue-green means two worlds; only one takes traffic - rollback is a light switch, not an archaeology dig",
     "Canary releases"),
    (36, "25 Sep 2026", "Canary Releases",
     ["Gradual traffic, feature flags, health"],
     ["Design a canary plan on paper for your webapp", "Optional: App Service testing in production / traffic routing if available"],
     """# Canary checklist
# - 5% traffic ? watch errors 15 min
# - 25% ? watch
# - 100% or abort""",
     "Canaries in coal mines and canaries in prod share a job: die early so the rest of us don't",
     "Rolling deployments"),
    (37, "26 Sep 2026", "Rolling Deployments",
     ["VMSS and Kubernetes rolling updates (concepts)"],
     ["Compare rolling vs blue-green vs canary in a table in docs", "No need for AKS yet"],
     """# Strategy | Downtime | Complexity | Rollback
# Rolling | Low | Medium | Slower
# Blue-green | Near-zero | Medium | Fast swap
# Canary | Near-zero | Higher | Stop ramp""",
     "Rolling deploys change the tires while the car is moving - thrilling, and occasionally stupid",
     "Approval gates"),
    (38, "27 Sep 2026", "Approval Gates & Environments",
     ["Pre/post approvals, checks, environment resources"],
     ["Add approval check on `prod` environment (you as approver)", "Run pipeline; practice Approve / Reject"],
     """# Pipelines ? Environments ? prod ? Checks ? Approvals
# Approvers: you (personal account)""",
     "Approvals are speed bumps before prod - annoying until the day they stop a 3am self-own",
     "Multi-environment pipeline"),
    (39, "28 Sep 2026", "Multi-environment Pipeline",
     ["Dev ? QA ? Staging ? Prod with gates"],
     ["YAML with 3 stages; approvals on last", "Promote same artifact, do not rebuild"],
     """stages:
- stage: Dev
  jobs: [ ... deploy ... ]
- stage: Staging
  dependsOn: Dev
  jobs: [ ... ]
- stage: Prod
  dependsOn: Staging
  jobs:
  - deployment: ProdDeploy
    environment: prod""",
     "Promote the artifact, not the vibes - rebuilds between envs invent 'works in staging' ghosts",
     "Phase 4 mini project"),
    (40, "29 Sep 2026", "Mini Project + Recap (Phase 4)",
     ["E2E CI/CD with approvals across 3 environments"],
     ["Green path Dev?Staging?Prod (prod can be echo if no budget)", "Recap post"],
     """# Success = one pipeline run with visible approvals and logs saved""",
     "Phase 4 recap: shipping is a pipeline with brakes, not a YOLO button",
     "IaC concepts"),
    (41, "30 Sep 2026", "IaC Concepts",
     ["Declarative vs imperative", "Idempotency, drift"],
     ["Write `docs/iac-why.md` with examples of drift you have seen", "Pick primary tool for Phase 5: **Bicep OR Terraform** (one)"],
     """# Decision record
# Tool: Terraform | Bicep
# Reason: ________""",
     "If it is not in code, it is a rumor - IaC turns 'someone clicked prod' into a diff",
     "ARM templates basics"),
    (42, "01 Oct 2026", "ARM Templates Basics",
     ["Template structure; deploy via CLI", "Treat as literacy, not your main tool"],
     ["Deploy a tiny Storage Account ARM template", "Then delete RG"],
     """az deployment group create -g rg-day42 -n stor -f infra/storage.json""",
     "ARM JSON is the broccoli of Azure - nutritious, rarely anyone's favorite",
     "ARM parameters & outputs"),
    (43, "02 Oct 2026", "ARM Parameters & Outputs",
     ["Parameter files, variables, nested templates"],
     ["Add parameters file; output storage endpoint", "Skim only if you chose Terraform as primary"],
     """az deployment group create -g rg-day43 -f main.json -p @main.parameters.json""",
     "Parameters are the dials; hardcoding names is how labs become landfills",
     "Bicep fundamentals"),
    (44, "03 Oct 2026", "Bicep Fundamentals",
     ["Why Bicep over ARM JSON", "Resource declarations"],
     ["If Bicep track: `az bicep install` and deploy storage", "If Terraform track: read Bicep sample only (30 min)"],
     """// main.bicep
param location string = resourceGroup().location
resource stg 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: 'st${uniqueString(resourceGroup().id)}'
  location: location
  sku: { name: 'Standard_LRS' }
  kind: 'StorageV2'
}""",
     "Bicep is ARM with the JSON horror filed down - same control plane, less eye strain",
     "Bicep modules"),
    (45, "04 Oct 2026", "Bicep Modules & Deployment",
     ["Modules, what-if, deployment stacks"],
     ["Run `az deployment group what-if`", "Split storage into a module"],
     """az deployment group what-if -g rg-day45 -f main.bicep""",
     "what-if is a dress rehearsal - read the diff before the audience (prod) arrives",
     "Terraform basics"),
    (46, "05 Oct 2026", "Terraform Basics",
     ["Providers, state, plan/apply/destroy"],
     ["Install Terraform", "Local state lab: RG only", "Always `destroy` at end of night"],
     """terraform init
terraform plan
terraform apply -auto-approve
terraform destroy -auto-approve""",
     "Terraform state is the memory of your infra - lose it and you are arguing with ghosts",
     "Terraform with Azure"),
    (47, "06 Oct 2026", "Terraform with Azure (azurerm)",
     ["Provider auth, common resources"],
     ["Auth via Azure CLI (`az login`)", "Create RG + storage with azurerm"],
     """provider "azurerm" {
  features {}
}
resource "azurerm_resource_group" "lab" {
  name     = "rg-day47-tf"
  location = "Central India"
}""",
     "azurerm is Terraform's Azure dialect - same ideas, different accent",
     "Terraform modules & remote state"),
    (48, "07 Oct 2026", "Terraform Modules & Remote State",
     ["Modules, Azure Storage backend, locking"],
     ["Create storage for state (note cost)", "Configure backend; migrate state", "Destroy carefully"],
     """terraform {
  backend "azurerm" {
    resource_group_name  = "rg-tfstate"
    storage_account_name = "<unique>"
    container_name       = "tfstate"
    key                  = "lab.tfstate"
  }
}""",
     "Remote state with locking stops two applies from playing tug-of-war with production",
     "IaC in pipelines"),
    (49, "08 Oct 2026", "IaC in Pipelines",
     ["Plan in CI, apply with approval"],
     ["Pipeline: terraform plan ? publish plan ? apply on approval"],
     """- script: terraform plan -out=tfplan
- script: terraform apply -auto-approve tfplan
  condition: and(succeeded(), eq(variables['apply'], 'true'))""",
     "IaC without a pipeline is homework; IaC in a pipeline is how grown-ups change prod",
     "Phase 5 mini project"),
    (50, "09 Oct 2026", "Mini Project + Recap (Phase 5)",
     ["Provision an environment via your chosen IaC in a pipeline"],
     ["One RG + one storage or webapp skeleton", "Destroy after screenshot", "Recap: why you picked Bicep or Terraform"],
     """# Definition of done: plan+apply from pipeline once; destroy once""",
     "Phase 5 recap: click-ops is a hobby; IaC is how you sleep",
     "Docker fundamentals"),
    (51, "10 Oct 2026", "Docker Fundamentals",
     ["Images, containers, Dockerfile, layer caching"],
     ["Install Docker Desktop (personal PC)", "Build/run a hello Dockerfile for your sample app"],
     """# Dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY . .
CMD ["npm", "start"]""",
     "Containers are shipping containers for processes - same app, fewer 'works on my laptop' customs checks",
     "Azure Container Registry"),
    (52, "11 Oct 2026", "Azure Container Registry (ACR)",
     ["Registries, tags, ACR Tasks"],
     ["Create Basic ACR", "docker tag + push", "Delete images you do not need"],
     """az acr create -g rg-day52 -n <uniqueacr> --sku Basic
az acr login -n <uniqueacr>
docker tag myapp:latest <uniqueacr>.azurecr.io/myapp:day52
docker push <uniqueacr>.azurecr.io/myapp:day52""",
     "ACR is a private closet for images - public Docker Hub is the thrift store",
     "Build & push in pipelines"),
    (53, "12 Oct 2026", "Build & Push Images in Pipelines",
     ["Docker tasks, multi-stage builds, scanning intro"],
     ["Pipeline builds image and pushes to ACR", "Use service connection"],
     """- task: Docker@2
  inputs:
    containerRegistry: acr-connection
    repository: myapp
    command: buildAndPush
    Dockerfile: **/Dockerfile
    tags: |
      $(Build.BuildId)
      latest""",
     "If humans push images by hand, humans will push the wrong tag on a Friday",
     "Azure Container Instances"),
    (54, "13 Oct 2026", "Azure Container Instances (ACI)",
     ["Serverless containers, quick deploys"],
     ["Run your image in ACI once", "Delete after test - ACI can surprise-bill"],
     """az container create -g rg-day54 -n hello-aci \\
  --image <acr>.azurecr.io/myapp:latest --registry-login-server <acr>.azurecr.io \\
  --registry-username <user> --registry-password <pass> --dns-name-label <unique> --ports 80""",
     "ACI is container fast-food - no cluster gym membership required",
     "Kubernetes fundamentals"),
    (55, "14 Oct 2026", "Kubernetes Fundamentals",
     ["Pods, Deployments, Services, namespaces", "Prefer concepts + kind/minikube if AKS cost is high"],
     ["Write a Deployment+Service YAML for your app", "Apply on local kind/minikube OR read-only if no cluster"],
     """apiVersion: apps/v1
kind: Deployment
metadata: {{ name: myapp }}
spec:
  replicas: 1
  selector: {{ matchLabels: {{ app: myapp }} }}
  template:
    metadata: {{ labels: {{ app: myapp }} }}
    spec:
      containers:
      - name: myapp
        image: <acr>.azurecr.io/myapp:latest
        ports: [{{ containerPort: 80 }}]""".replace("{{", "{").replace("}}", "}"),
     "Kubernetes is an airport for containers - powerful, expensive, and overkill for a lemonade stand",
     "AKS setup"),
    (56, "15 Oct 2026", "AKS Setup",
     ["Cluster, node pools, kubenet vs CNI"],
     ["Optional: create smallest AKS OR skip to Azure Container Apps path", "If created: schedule destroy same weekend"],
     """# Cost warning: AKS is not a daily-delete toy
az aks create -g rg-day56 -n aks-lab --node-count 1 --generate-ssh-keys""",
     "AKS is a gym membership for orchestration - easy to start, painful if you forget to cancel",
     "Deploy to AKS via pipelines"),
    (57, "16 Oct 2026", "Deploying to AKS via Pipelines",
     ["kubectl/Helm tasks, service connections"],
     ["If no AKS: practice kubectl against local cluster", "Pipeline applies manifests"],
     """- task: KubernetesManifest@1
  inputs:
    action: deploy
    namespace: default
    manifests: k8s/*.yml""",
     "CD to Kubernetes without Git is sticky-note ops wearing a hoodie",
     "Helm basics"),
    (58, "17 Oct 2026", "Helm Charts Basics",
     ["Chart structure, values.yaml, releases"],
     ["`helm create myapp` and package values for image tag", "Install/upgrade/uninstall once"],
     """helm create charts/myapp
helm upgrade --install myapp charts/myapp --set image.tag=$(Build.BuildId)""",
     "Helm is templating for YAML mountains - values.yaml is where environments stop being copy-paste crimes",
     "AKS scaling & networking"),
    (59, "18 Oct 2026", "AKS Scaling, Monitoring & Networking",
     ["HPA, cluster autoscaler, ingress, network policies - survey"],
     ["Read HPA docs; write when you would use HPA vs more replicas fixed", "Skip deep CNI labs if time-boxed"],
     """# HorizontalPodAutoscaler sketch
# scale on cpu 70% between 1 and 5 replicas""",
     "Autoscaling without metrics is superstition with YAML",
     "Phase 6 mini project"),
    (60, "19 Oct 2026", "Mini Project + Recap (Phase 6)",
     ["Containerize app + deploy via CI/CD (ACI/Container Apps/AKS - one path)"],
     ["Prefer Container Apps or ACI if AKS cost bites", "Recap post with architecture one-liner"],
     """# Done = image in ACR + one successful deploy path automated""",
     "Phase 6 recap: package once, run anywhere - but 'anywhere' still has a bill",
     "Entra ID fundamentals"),
    (61, "20 Oct 2026", "Azure AD (Entra ID) Fundamentals",
     ["Tenants, users, groups, app registrations"],
     ["In personal tenant: register an app `day61-lab`", "Note client ID; create a secret only in Key Vault tomorrow - or use cert later"],
     """# Portal: Entra ID ? App registrations ? New registration
# Redirect URI: optional for lab""",
     "Entra ID is the bouncer list for Azure - if identity is wrong, every other control is cosplay",
     "RBAC deep dive"),
    (62, "21 Oct 2026", "RBAC Deep Dive",
     ["Built-in roles, custom roles, scope"],
     ["Assign yourself Reader on a lab RG via CLI", "Compare Contributor vs Owner mentally"],
     """az role assignment create --assignee <your-upn> \\
  --role Reader --scope /subscriptions/<sub>/resourceGroups/rg-day62""",
     "Owner is a flamethrower; prefer Reader/Contributor scoped to the RG, not the subscription",
     "Service connections & SPNs"),
    (63, "22 Oct 2026", "Service Connections & Service Principals",
     ["SPNs, workload identity federation, least privilege"],
     ["Create Azure RM service connection in Azure DevOps (automatic)", "Prefer WIF over long-lived secrets when possible"],
     """# Project Settings ? Service connections ? Azure Resource Manager
# Workload identity federation (manual/automatic)""",
     "Service principals are robot employees - give them a badge scoped to one floor, not master keys",
     "Azure Key Vault"),
    (64, "23 Oct 2026", "Azure Key Vault",
     ["Secrets, keys, certs", "Access policies vs RBAC"],
     ["Create Key Vault; add secret `DemoSecret`", "Grant your user Secrets User via RBAC"],
     """az keyvault create -g rg-day64 -n <uniquekv> --enable-rbac-authorization true
az keyvault secret set --vault-name <uniquekv> --name DemoSecret --value 'not-a-real-password'""",
     "Key Vault is the hotel safe - secrets in repo chat history are postcards from an incident",
     "Key Vault in pipelines"),
    (65, "24 Oct 2026", "Integrating Key Vault with Pipelines",
     ["Key Vault task; variable groups linked to KV"],
     ["Link variable group to Key Vault", "Print length of secret in pipeline, never the value"],
     """- task: AzureKeyVault@2
  inputs:
    azureSubscription: <sc>
    KeyVaultName: <uniquekv>
    SecretsFilter: DemoSecret
- script: echo "Secret length ${{#DemoSecret}}"  # use correct macro syntax in ADO""".replace("{#", "{#"),
     "Pipelines that need secrets should fetch them - not store them in variable screenshots",
     "Azure Policy"),
    (66, "25 Oct 2026", "Azure Policy & Governance",
     ["Policy definitions, initiatives, compliance", "Skip Blueprints - retired; use Policy + landing zone ideas"],
     ["Assign a built-in policy like 'Require a tag on resource groups' to lab subscription/RG", "See compliance blade"],
     """# Portal: Policy ? Assignments ? Assign policy
# Or: az policy assignment create ...""",
     "Policy is the grown-up saying 'no untagged RGs' so Finance does not hunt you with spreadsheets",
     "Compliance scanning in pipelines"),
    (67, "26 Oct 2026", "Compliance Scanning in Pipelines",
     ["SAST, dependency scanning, secret scanning"],
     ["Add a secret scan task or GitHub push protection on mirror", "Fail build on high vulnerabilities if tool available"],
     """# Example mindset
# - dependency scan on restore
# - secret scan on repo
# - publish results as pipeline summary""",
     "Shift-left security means finding the fire in the kitchen, not on the evening news",
     "DevSecOps shift-left"),
    (68, "27 Oct 2026", "DevSecOps - Shift-left Security",
     ["Embed gates early"],
     ["Add a pipeline stage `Security` before `Deploy`", "Document fail criteria"],
     """stages: [Build, Security, Deploy]
# Security job exits non-zero on critical CVEs""",
     "Security as a final boss stage is how you ship late - put checks next to the commit",
     "Secure pipeline design"),
    (69, "28 Oct 2026", "Secure Pipeline Design",
     ["Least privilege agents, approvals, protected branches"],
     ["Audit: who can edit pipelines? who can approve prod?", "Remove any broad Owner SPN from lab if over-permissioned"],
     """# Checklist
# - separate service connections per env
# - no secret echo
# - main locked
# - prod approval required""",
     "A secure pipeline is boring on purpose - drama belongs in Netflix, not release logs",
     "Phase 7 mini project"),
    (70, "29 Oct 2026", "Mini Project + Recap (Phase 7)",
     ["Secure pipeline with Key Vault + a policy"],
     ["One demo pipeline fetching a secret; RG tag policy on", "Recap"],
     """# Done = secret not in YAML; policy visible; approvals on""",
     "Phase 7 recap: speed without security is just a faster incident",
     "Azure Monitor fundamentals"),
    (71, "30 Oct 2026", "Azure Monitor Fundamentals",
     ["Metrics, logs, activity log, diagnostics"],
     ["Enable diagnostics on a lab resource to Log Analytics (or note cost and skip retention)"],
     """# Portal: Monitor ? Overview
# Enable Diagnostic settings on App Service / KV""",
     "If you cannot see it, you cannot fix it - Monitor is the flashlight, not the fix",
     "Log Analytics & KQL"),
    (72, "31 Oct 2026", "Log Analytics Workspace & KQL",
     ["Workspace setup, KQL basics"],
     ["Run 3 KQL queries: Heartbeat or AzureActivity samples", "Save a query"],
     """AzureActivity
| where TimeGenerated > ago(1d)
| summarize count() by OperationNameValue
| top 10 by count_""",
     "KQL is SQL's cousin who lives in the cloud and judges your where-clauses",
     "Application Insights"),
    (73, "01 Nov 2026", "Application Insights Integration",
     ["Instrumentation, dependencies, live metrics"],
     ["Create App Insights; connect to sample app or use portal demo", "Generate traffic; view failures map"],
     """# Add connection string via Key Vault / app settings - never commit it""",
     "App Insights is a GoPro on your app - embarrassing, invaluable",
     "Alerts & action groups"),
    (74, "02 Nov 2026", "Alerts & Action Groups",
     ["Metric/log alerts, action groups"],
     ["Create action group email-to-self", "Alert on CPU or availability test"],
     """# Monitor ? Alerts ? Create alert rule
# Action group: email yourself (personal)""",
     "Alerts without action groups are screams into the void - polite, useless",
     "Dashboards & workbooks"),
    (75, "03 Nov 2026", "Dashboards & Workbooks",
     ["Custom dashboards, workbooks for stakeholders"],
     ["Pin 3 tiles: availability, failures, cost", "Share dashboard with yourself only"],
     """# Portal ? Dashboard ? New ? pin charts from App Insights""",
     "A dashboard is a storyboard - if it needs a 30-min explanation, it is a novel, not a dashboard",
     "Pipeline monitoring"),
    (76, "04 Nov 2026", "Pipeline Monitoring & Analytics",
     ["Build/release analytics, flaky insights"],
     ["Open Analytics views for pipelines", "Note failure rate this week"],
     """# Azure DevOps ? Pipelines ? Analytics / Insights""",
     "A red pipeline ignored for a week is a culture problem wearing a YAML costume",
     "Cost management"),
    (77, "05 Nov 2026", "Cost Management & Optimization",
     ["Budgets, alerts, right-sizing"],
     ["Review Cost Analysis for lab subscription", "Tighten budget alert", "Kill orphan resources"],
     """az group list -o table
# delete unused RGs
az group delete -n <old-rg> --yes --no-wait""",
     "The best Azure skill is deleting things - empty RGs are silent subscriptions eating money",
     "Advisor & WAF"),
    (78, "06 Nov 2026", "Azure Advisor & Well-Architected Framework",
     ["5 pillars; recommendations"],
     ["Open Advisor; accept or dismiss one recommendation with a note why"],
     """# Pillars: Reliability, Security, Cost, Operational Excellence, Performance""",
     "Well-Architected is a report card - Advisor is the teacher who already knows you skipped networking homework",
     "Incident management basics"),
    (79, "07 Nov 2026", "Incident Management Basics",
     ["On-call concepts, runbooks, postmortems"],
     ["Write a 1-page runbook for 'webapp down' in `/docs/runbook-webapp-down.md`", "Blameless postmortem template"],
     """# Symptom ? Checks ? Mitigate ? Communicate ? Postmortem link""",
     "Postmortems without blame create learning; postmortems with blame create silence",
     "Phase 8 mini project"),
    (80, "08 Nov 2026", "Mini Project + Recap (Phase 8)",
     ["Observability stack for a deployed app"],
     ["App Insights + 1 alert + 1 dashboard", "Recap"],
     """# Done = you can detect a forced failure within 5 minutes""",
     "Phase 8 recap: deploy is not done - observable is done",
     "Multi-repo & monorepo"),
    (81, "09 Nov 2026", "Multi-repo & Monorepo Strategies",
     ["Trade-offs; pipeline design"],
     ["Write ADR: this lab stays monorepo for samples", "List when you would split repos for a client"],
     """# Monorepo: shared pipelines, atomic PRs
# Multi-repo: clear ownership, harder cross-cutting changes""",
     "Repo strategy is politics with folders - pick the drama you can afford",
     "Pipeline templates"),
    (82, "10 Nov 2026", "Pipeline Templates & Reusable YAML",
     ["templates, extends, parameters"],
     ["Extract a `templates/build.yml` and reuse from main pipeline"],
     """# templates/build.yml
parameters:
- name: projectPath
  type: string
steps:
- script: echo Building ${{{{ parameters.projectPath }}}}""".replace("{{{{", "{{").replace("}}}}", "}}"),
     "Copy-paste YAML is how organizations invent 14 slightly different ways to be broken",
     "Extensions & marketplace"),
    (83, "11 Nov 2026", "Azure DevOps Extensions & Marketplace",
     ["Useful third-party tasks; install carefully"],
     ["Browse Marketplace; install one reputable extension OR document why you install zero"],
     """# Prefer Microsoft-maintained tasks for labs
# Third-party: check publisher, permissions, last update""",
     "Marketplace extensions are spices - a pinch helps; a handful ruins the stew and the security review",
     "Jenkins to Azure Pipelines"),
    (84, "12 Nov 2026", "Migrating Jenkins to Azure Pipelines",
     ["Map Jenkinsfile concepts to YAML"],
     ["Translate a sample Jenkinsfile (agent, stages, post) into Azure YAML on paper"],
     """# Jenkins stage ? Azure stage/job
# credentials ? variable group / Key Vault
# agents ? pools""",
     "Jenkins migrations succeed when you migrate pipelines, not nostalgia",
     "Hybrid & multi-cloud CI/CD"),
    (85, "13 Nov 2026", "Hybrid & Multi-cloud CI/CD",
     ["Patterns to AWS/GCP from Azure Pipelines - survey only"],
     ["Write risks: secrets, identity, network", "Do not actually deploy to AWS unless personal account ready"],
     """# Pattern: build once in ADO ? deploy with cloud-specific tasks
# Prefer one cloud deep over two clouds shallow in this 100 days""",
     "Multi-cloud is insurance and complexity - buy it for a reason, not a slide",
     "DR & backup"),
    (86, "14 Nov 2026", "Disaster Recovery & Backup",
     ["Backup policies, geo-redundancy, drills"],
     ["Enable soft delete on Key Vault if not on", "Document RPO/RTO targets for your lab app (even if fictional)"],
     """# RPO: how much data loss OK?
# RTO: how fast back online?
# Drill: restore once or it is fiction""",
     "Backups you never restore are fan fiction",
     "Azure Landing Zones"),
    (87, "15 Nov 2026", "Azure Landing Zones",
     ["Enterprise-scale, hub-spoke - concepts"],
     ["Read CAF landing zone overview", "Sketch hub-spoke on paper for a fake company"],
     """# Hub: shared networking/firewall
# Spokes: workloads
# Management groups + policy""",
     "Landing zones are city planning for Azure - skip them and you get shantytowns of resource groups",
     "GitOps with Flux/Argo"),
    (88, "16 Nov 2026", "GitOps with Flux/Argo CD",
     ["Git as source of truth for cluster state"],
     ["Read GitOps principles; optional local Flux quickstart", "Compare to Azure Pipelines push model"],
     """# Git desired state ? controller reconciles cluster
# PR to change prod; no kubectl cowboy moves""",
     "GitOps means the cluster stops being a petting zoo for kubectl",
     "Scaling DevOps for large teams"),
    (89, "17 Nov 2026", "Scaling DevOps for Large Teams",
     ["Governance, self-service, internal developer portals"],
     ["List 5 platform capabilities you would offer a 50-dev org", "Map to Azure DevOps + templates"],
     """# Self-service catalog ideas:
# - app pipeline template
# - RG + budget bootstrap
# - golden paths docs""",
     "Platform engineering is DevOps that productized the paved road",
     "Phase 9 mini project"),
    (90, "18 Nov 2026", "Mini Project + Recap (Phase 9)",
     ["Reusable pipeline template as the 'enterprise' artifact"],
     ["Publish `templates/` used by 2 sample pipelines", "Recap"],
     """# Done = one template, two consumers, one green run each""",
     "Phase 9 recap: enterprise is reuse + guardrails, not more YAML copy-paste",
     "Capstone 1"),
    (91, "19 Nov 2026", "Capstone Project 1 - E2E App CI/CD",
     ["Reuse earlier app; harden CI/CD", "Do NOT start a giant ecommerce from zero"],
     ["Define MVP: one app, CI, CD to App Service/Container Apps, README diagram", "Work in `capstone/` folder"],
     """# Scope control
# In: one service, tests, pipeline, env promotion
# Out: payments, recommendations ML, 12 microservices""",
     "Capstones fail from ambition - ship a thin vertical slice you can demo in 5 minutes",
     "Capstone 2"),
    (92, "20 Nov 2026", "Capstone Project 2 - Containers Path",
     ["Containerize capstone; ACR + deploy", "AKS optional"],
     ["Dockerfile + pipeline build/push + deploy", "Continue same app as Day 91"],
     """# Same repo - add /Dockerfile and k8s or containerapp yaml""",
     "Day 92 is the same app in a container tuxedo - not a new Netflix clone",
     "Capstone 3"),
    (93, "21 Nov 2026", "Capstone Project 3 - IaC Multi-env",
     ["Terraform/Bicep for dev+staging", "Wire to pipeline"],
     ["Infra for the same capstone; two environments", "Destroy non-prod when done"],
     """# infra/ + pipelines/infra.yml with plan/apply approvals""",
     "Infra as code for your demo is the difference between a toy and a portfolio piece",
     "GitHub portfolio setup"),
    (94, "22 Nov 2026", "GitHub Portfolio Setup",
     ["Clean READMEs, diagrams, pinned repos"],
     ["Push sanitized capstone to personal GitHub", "README: problem, architecture, how to run, screenshots"],
     """# README sections
# Problem | Architecture | Pipelines | Security | Cost notes | License""",
     "GitHub is your shop window - pinned repos with vague names are closed blinds",
     "Personal site / case studies"),
    (95, "23 Nov 2026", "Personal Site / Blog for Case Studies",
     ["Publish write-up of capstone"],
     ["GitHub Pages or Dev.to article linking the repo", "No employer content"],
     """# Title: How I built a small Azure DevOps CI/CD demo in public""",
     "A case study translates YAML into a story a non-terminal human can trust",
     "AZ-400 review"),
    (96, "24 Nov 2026", "AZ-400 Certification Review",
     ["Map 100 days to exam objectives; gap-fill"],
     ["Download skills outline; tick what you practiced", "Schedule gap study, not the whole exam cram tonight"],
     """# https://learn.microsoft.com/credentials/certifications/exams/az-400/
# Gaps ? weekend study list""",
     "AZ-400 rewards people who built things - your labs are the study guide you already wrote",
     "Mock interview prep"),
    (97, "25 Nov 2026", "Mock Interview Prep",
     ["Common Azure DevOps scenario questions"],
     ["Answer out loud 5 questions; record yourself once", "Topics: branching, YAML, secrets, rollback, DORA"],
     """# Q: How do you promote the same artifact across envs?
# Q: Secret in a PR - what do you do?
# Q: Pipeline red on Friday 5pm - what's your playbook?""",
     "Interviews are pipelines for your career - rehearse the happy path and the failure path",
     "Professional profile setup"),
    (98, "26 Nov 2026", "Professional Profile Setup",
     ["Toptal/Braintrust/Upwork - only after policy check"],
     ["Read employer moonlighting policy BEFORE creating paid profiles", "Draft profile offline; activate only if allowed"],
     """# Checklist
# - policy reviewed
# - portfolio links ready
# - no IBM customer targeting
# - personal equipment only""",
     "Profiles are loud - make sure your contract allows the volume before you hit publish",
     "Outreach & pricing"),
    (99, "27 Nov 2026", "Outreach Templates & Pricing",
     ["Templates without spammy CTAs on LinkedIn series", "Pricing ranges are references only"],
     ["Write 2 DM templates focused on solving a DevOps pain, not 'hire me'", "Note your rate band privately"],
     """# Template vibe:
# 'Saw you are hiring for Azure Pipelines - I published a public CI/CD walkthrough here: <link>. Happy to answer questions.'""",
     "Pricing is a boundary - undercharging buys stress, overcharging without proof buys silence",
     "Launch day"),
    (100, "28 Nov 2026", "Launch Day + Next 100 Days",
     ["Publish portfolio, plan next cycle", "Celebrate without leaking employer info"],
     ["Pin GitHub repos", "Post Day 100 recap", "Write 5 goals for next 100 days (cert, deeper AKS, or client-ready offer - policy permitting)"],
     """# Day 100 checklist
# - portfolio live
# - capstone README polished
# - LinkedIn recap live
# - resources destroyed / budgets set
# - next-100 plan in /docs/next-100.md""",
     "Day 100 is not the finish line - it is the first public proof you can ship learning on purpose",
     "Keep going"),
]


def fix_code(code: str) -> str:
    # cleanup accidental braces from generation
    return code


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    all_days = list(DAYS) + MORE
    assert len(all_days) == 100, len(all_days)

    index_rows = []
    for item in all_days:
        day, date, topic, learn, lab, code, hook, tomorrow = item
        phase = phase_for(day)
        text = render(day, date, topic, learn, lab, fix_code(code), hook, tomorrow, phase)
        path = OUT / f"day-{day:02d}.md"
        path.write_text(text, encoding="utf-8")
        index_rows.append((day, date, topic, path.name))

    # README index
    lines = [
        "# 100-Day Azure DevOps - Daily Guides",
        "",
        "One document per day: **learn ? lab ? code ? LinkedIn post ? checklist**.",
        "",
        "LinkedIn tone: educational + entertaining. No sales CTAs. Personal accounts only.",
        "",
        "| Day | Date | Topic | Guide |",
        "|-----|------|-------|-------|",
    ]
    for day, date, topic, name in index_rows:
        lines.append(f"| {day} | {date} | {topic} | [{name}](./{name}) |")
    lines += [
        "",
        "## How to use",
        "",
        "1. Open today's `day-XX.md`.",
        "2. Do Learn + Lab inside the time box.",
        "3. Copy the LinkedIn post; edit one line so it sounds like you.",
        "4. Tick the checklist; delete spare Azure resources.",
        "",
        "## Tooling (personal)",
        "",
        "- Azure subscription + budget alert",
        "- Azure DevOps org",
        "- Git + Azure CLI",
        "- GitHub (portfolio later)",
        "- Docker / Terraform or Bicep when those phases start",
        "",
        "*Generated for personal learning. Not legal advice.*",
        "",
    ]
    (OUT / "README.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {len(all_days)} day guides to {OUT}")


if __name__ == "__main__":
    main()
