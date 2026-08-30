# Day 10 — Phase 1 Capstone Mini Project & Recap

| | |
|---|---|
| **Date** | 30 Aug 2026 |
| **Phase** | 1 — Azure & DevOps Foundations (Capstone) |
| **Time box** | 60–90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Tie all 10 days of Phase 1 together inside `azure-100-labs`: verify the 5 Azure DevOps hubs (Boards, Repos, Pipelines, Test Plans, Artifacts), create an operational Project Dashboard, and recap key foundations before jumping into Phase 2 (Git & Repos).

## Learn (20–30 min)

### Phase 1 Matrix — What We Mastered (Days 1–10)

| Day | Topic | Key Takeaway |
|:---:|:------|:-------------|
| **01** | Cloud & Azure Fundamentals | Shared responsibility, IaaS vs PaaS vs SaaS, Regions & AZs |
| **02** | Portal, CLI & PowerShell | Management hierarchy (MG → Sub → RG → Resource), automated scripting |
| **03** | ARM & Governance Basics | Declarative infrastructure, Resource Locks, Cost tags & Budget alerts |
| **04** | DevOps Principles & CALMS | Culture, Automation, Lean, Measurement (DORA metrics), Sharing |
| **05** | Azure DevOps 5 Services | Overview of Boards, Repos, Pipelines, Test Plans, Artifacts |
| **06** | Org & Project Setup | Org tenancy, `azure-100-labs` project, Agile process, least-privilege security |
| **07** | Azure Boards Deep Dive | Hierarchy (Epic → Feature → Story → Task), Kanban WIP limits, custom queries |
| **08** | Azure Test Plans Basics | Plans, Suites, Cases, Runs, and the traceability loop to User Stories |
| **09** | Azure Artifacts | Private feeds (`day09-packages`), upstream caching, and feed views |
| **10** | Phase 1 Capstone & Recap | End-to-end integration, project dashboarding, and Phase 2 readiness |

## Hands-on lab (20–30 min)

1. **Verify your `azure-100-labs` project hubs:**
   - **Boards:** Epic `100 Days Learning`, Feature `Phase 1 Foundations`, active User Stories.
   - **Repos:** Initialize default Git repository with a `README.md`.
   - **Test Plans:** Test Plan `Phase 1 Smoke Tests` with baseline test cases.
   - **Artifacts:** Feed `day09-packages` with upstream caching enabled.
2. **Build an Azure DevOps Overview Dashboard:**
   - Go to **Overview → Dashboards** → Create Dashboard: `Phase 1 Command Center`.
   - Add widgets:
     - **Query Tile:** Open User Stories count (from Day 7 query).
     - **Chart for Work Items:** Pie or bar chart by work item State.
     - **Code Tile / Markdown:** Project goals and Phase 2 roadmap links.
3. **Azure Resource Cleanliness Audit:**
   - Run `az group list -o table` in Azure CLI to ensure no leftover lab resource groups are running up costs.

## Commands / code

```bash
# Clone the lab repository to your workstation
git clone https://dev.azure.com/<your-org>/azure-100-labs/_git/azure-100-labs
cd azure-100-labs

# Verify clean bootstrap
echo "# Azure 100 Labs" > README.md
echo "Personal learning repository for #100DaysOfAzureDevOps" >> README.md
git add README.md
git commit -m "docs: bootstrap Phase 1 lab repo"
git push origin main

# Governance / cost safety check
az group list --query "[?starts_with(name, 'rg-lab-')].name" -o table
```

## LinkedIn post (copy-paste)

**Important:** After pasting into LinkedIn, press Enter between sections so line breaks stay visible.

```
Day 10 of #100DaysOfAzureDevOps

10 days ago, we started with a blank Azure subscription and a simple goal: learn Azure DevOps in public, from raw foundations to production reality.

Today marks the completion of Phase 1: Azure & DevOps Foundations.

Before touching complex YAML pipelines or Kubernetes clusters, you have to master the bedrock. If the foundation is shaky, your CI/CD pipeline just automates chaos faster.

What we built and mastered in Phase 1 (Days 1–10):

1. Cloud & Governance Foundations
• IaaS, PaaS, and SaaS shared responsibility models
• Resource hierarchy: Management Groups → Subscriptions → Resource Groups → Resources
• Cost governance: Resource Locks, Tags, and Budget alerts

2. DevOps Culture & Flow
• CALMS framework and DORA metrics (Deployment Frequency, Lead Time, CFR, MTTR)
• Why pipeline "Succeeded" does not mean production health

3. The 5 Azure DevOps Hubs in Action (azure-100-labs)
• Azure Boards: Honest work tracking, Kanban WIP limits, and Epic → Feature → Story hierarchy
• Azure Repos: Clean repo initialization, Git configuration
• Azure Test Plans: Structured test cases, Web Runner, and end-to-end traceability back to User Stories
• Azure Artifacts: Private package feeds, upstream caching resilience against public outages, and feed views

Lab today:
Tied all five hubs together in azure-100-labs, stood up a Phase 1 Command Center dashboard with work item queries, and audited cloud resources for zero cost waste.

One-liner for Phase 1:
Foundations are not the boring part of DevOps.
They are the guardrails that keep your delivery systems alive under pressure.

Tomorrow: We kick off Phase 2 (Days 11–20) — Git & Azure Repos Deep Dive!

(Document attached: Day 10 Phase 1 Capstone & Architecture Recap PDF)

Lab notes + PDF also here:
https://bit.ly/4gDGA05

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### Attach with the post (PDF handout)

Attach this document on LinkedIn (document / PDF upload):

- [`../days/day-10-phase-1-recap/handout.pdf`](../days/day-10-phase-1-recap/handout.pdf)

### How to post

1. LinkedIn → **document** → upload `days/day-10-phase-1-recap/handout.pdf`
2. Paste the text above (press **Enter** between sections so line breaks stay visible)
3. **Document title:** `Day 10 — Phase 1 Capstone & Recap` (max 58 chars on LinkedIn)

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5–10 real comments on other Azure/DevOps posts.

## Done checklist

- [ ] Reviewed Phase 1 topics and takeaways
- [ ] Verified all hubs in `azure-100-labs` (Boards, Repos, Test Plans, Artifacts)
- [ ] Created `Phase 1 Command Center` dashboard in Azure DevOps
- [ ] Verified zero orphan resources in Azure subscription
- [ ] Published LinkedIn post with PDF handout
- [ ] Engaged with 5–10 community comments

## Tomorrow

**Day 11 — Git Foundations for DevOps Engineers (Phase 2 Begins)**

---

*Personal learning guide — views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
