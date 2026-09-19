# -*- coding: utf-8 -*-
"""LinkedIn PDF handout specs for Days 76–100 of #100DaysOfAzureDevOps."""

SPECS = {}

SPECS[76] = {
    "topic": "Pipeline Monitoring & Analytics",
    "subtitle": "Treat red as a signal you own, not décor you scroll past",
    "phase": "8 - Monitoring & Observability",
    "tables": [
        {
            "title": "Architecture A — where pipeline health actually lives",
            "columns": ["Surface", "What it measures", "Where you click"],
            "rows": [
                ["Pipelines → Analytics", "Pass rate, duration, failure trend for YAML pipelines", "Project → Pipelines → Analytics (or Insights)"],
                ["Test insights / flakes", "Tests that pass and fail on the same commit", "Run → Tests tab; flaky test report if enabled"],
                ["Release / env history", "Which environment ate the last failed deploy", "Pipelines → Environments → deployments"],
                ["Job log duration", "Which task burned hosted minutes", "Run → job → each step elapsed time"],
                ["Board / work item link", "Which change shipped with the red run", "Run → Related / work items"],
            ],
            "widths": [40, 71, 71],
        },
        {
            "title": "Architecture B — decide from a number, not a vibe",
            "columns": ["Signal", "Default action", "Escalate when"],
            "rows": [
                ["Failure rate this week", "Write the % (or last N runs) in docs/pipeline-health-day76.md", "Main red >1 day with no owner comment"],
                ["Same test fails then passes", "Name the flake or delete the test", "Team habit is 're-run until green'"],
                ["CI duration doubled", "Open the longest task; cache or split", "Feedback >20 min on a personal hello pipeline"],
                ["Zero runs this week", "That is darkness, not 100% success", "You are about to quote a fake pass rate"],
                ["One red run you ignored", "Fix it or write why it stays red", "You catch yourself saying 'it is always like that'"],
            ],
            "widths": [42, 70, 70],
        },
        {
            "title": "Architecture C — pitfalls that train you to mute the alarm",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Costume culture", "Main red Mon–Thu; Slack says 'known'", "Own the run: fix, quarantine, or document"],
                ["Flake installment plan", "Coin-flip tests; everyone clicks Re-run", "Pin the test name; delete or quarantine in YAML"],
                ["Analytics never opened", "Pretty pipeline list, no trend", "Project → Pipelines → Analytics once per week"],
                ["Duration as folklore", "'CI is just slow'", "Sort tasks by elapsed; the 12-min restore is the product"],
                ["Employer org screenshot", "You almost paste a work failure rate", "Personal org only. azure-100-labs project"],
            ],
            "widths": [40, 71, 71],
        },
    ],
    "one_liner": "A red pipeline ignored for a week is a culture problem wearing a YAML costume.",
    "lab_intro": "Personal Azure DevOps org only. Project azure-100-labs. No employer pipeline screenshots.",
    "lab": [
        "Project → Pipelines → Analytics (or Insights). If the blade is empty, open the last 10 runs on your busiest YAML pipeline and tally pass/fail by hand.",
        "Write this week's failure rate (or last-N pass count) in docs/pipeline-health-day76.md. Zero runs = write 'darkness', not 100%.",
        "Open the newest failed run. Name the failing task and the exception line. If it is a flake, write the test name; do not only click Re-run.",
        "On a green run, note the three longest tasks and their elapsed times. Duration is hosted minutes plus feedback delay.",
        "If any pipeline is still red, either fix it in this lab or add a one-sentence owner note in the markdown. Costume off.",
        "Confirm you are in the personal org (not a work tenant) before any screenshot for the LinkedIn document.",
    ],
    "code_title": "Receipt — last runs you can quote without inventing a pass rate",
    "code": (
        "# Azure CLI against the personal org (PAT in AZURE_DEVOPS_EXT_PAT, never committed)\n"
        "az pipelines runs list --org https://dev.azure.com/<your-org> \\\n"
        "  --project azure-100-labs --pipeline-ids <id> --top 10 -o table\n"
        "# Then: Pipelines → Analytics. Write pass/fail + longest task in docs/pipeline-health-day76.md"
    ),
    "checklist": [
        "Can say this week's failure rate (or last-N tally) out loud",
        "Named a flake or wrote 'no flake — real fail' with the task name",
        "docs/pipeline-health-day76.md exists on the personal repo",
        "Did not screenshot an employer org",
        "Posted the LinkedIn document (personal account)",
    ],
    "tomorrow": "Cost management — Cost Analysis, a tighter budget alert, and deleting leftover lab resource groups",
}

SPECS[77] = {
    "topic": "Cost Management & Optimization",
    "subtitle": "The best Azure skill is deleting things you can name",
    "phase": "8 - Monitoring & Observability",
    "tables": [
        {
            "title": "Architecture A — the personal-sub cost stack",
            "columns": ["Control", "Azure object", "What it actually does"],
            "rows": [
                ["Cost Analysis", "Microsoft.CostManagement / Portal Cost Analysis", "Filter by resource group, meter, tag"],
                ["Budget + alert", "Microsoft.Consumption/budgets", "Email/Action Group before the invoice, not after"],
                ["Advisor cost recs", "Microsoft.Advisor recommendations (Cost)", "Idle SKUs, reserved-instance noise; still a list, not a bill"],
                ["Resource graph", "az group list / az resource list", "Orphans: Public IP, Basic ACR, forgotten AKS"],
                ["IaC destroy", "terraform destroy / az deployment ... --mode Complete", "Delete the way you created, or Portal if it was click-ops"],
            ],
            "widths": [36, 73, 73],
        },
        {
            "title": "Architecture B — decide per leftover, not a fictional savings %",
            "columns": ["Finding", "Default", "Do not"],
            "rows": [
                ["RG named rg-dayNN with no lab this week", "az group delete --yes --no-wait", "Invent a 37% savings number you did not measure"],
                ["AKS / Container Apps still running", "Destroy tonight if the weekend already passed", "Leave it 'for the capstone someday'"],
                ["Budget alert still at Day-1 default", "Lower amount or tighten filter to this sub", "Ignore the email because 'it is only a lab'"],
                ["Orphan Public IP / disk", "Delete the resource, then the empty RG", "Keep the RG because empty looks free"],
                ["Created with Terraform/Bicep", "destroy / delete the deployment first", "Portal-delete one child and leave state lying"],
            ],
            "widths": [50, 66, 66],
        },
        {
            "title": "Architecture C — pitfalls that eat a silent subscription",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Empty RG folklore", "No VMs, still a Public IP meter", "az resource list -g <rg> -o table before you shrug"],
                ["Basic ACR / idle AKS", "Small daily drain you forget", "Delete registry or cluster; do not 'right-size' a lab you are not using"],
                ["Budget as a sticker", "Alert never fired; invoice did", "Cost Management → Budgets → edit amount + contact"],
                ["Wrong subscription in CLI", "You listed a work sub by accident", "az account show; switch to the personal sub"],
                ["Destroy skipped 'until later'", "Day 56 RG alive on Day 77", "Today is the due date"],
            ],
            "widths": [40, 71, 71],
        },
    ],
    "one_liner": "The best Azure skill is deleting things — empty RGs are silent subscriptions eating money.",
    "lab_intro": "Personal subscription only. az account show must not be a work tenant. Project azure-100-labs for notes.",
    "lab": [
        "az account show -o table. Confirm the personal subscription name and ID. Stop if it is not yours.",
        "Portal → Cost Management + Billing → Cost Analysis. Filter last 30 days by resource group. Write the top three meters in docs/cost-day77.md (no invented %).",
        "Cost Management → Budgets. Tighten the lab budget alert (amount or filter). Note the new threshold in the markdown.",
        "az group list -o table. Mark every RG that is not part of this week's lab.",
        "Delete unused groups: az group delete -n <old-rg> --yes --no-wait. If born from Terraform/Bicep, destroy from that tool first.",
        "If AKS, a Basic ACR, or a leftover Public IP is still listed, delete it today. Then re-run az group list.",
    ],
    "code_title": "CLI — list, then delete leftovers on the personal subscription",
    "code": (
        "az account show --query \"{name:name,id:id,tenant:tenantId}\" -o table\n"
        "az group list -o table\n"
        "az resource list --query \"[].{rg:resourceGroup,type:type,name:name}\" -o table\n"
        "# After you confirm the RG is a leftover lab:\n"
        "az group delete -n rg-day56-aks --yes --no-wait"
    ),
    "checklist": [
        "az account show is the personal subscription",
        "Wrote top Cost Analysis meters without a fake savings percentage",
        "Budget alert tightened",
        "At least one unused RG deleted, or wrote 'none leftover' with the group list",
        "docs/cost-day77.md on the personal repo",
    ],
    "tomorrow": "Azure Advisor and the Well-Architected pillars — one recommendation, one written decision",
}

SPECS[78] = {
    "topic": "Azure Advisor & Well-Architected Framework",
    "subtitle": "A report card only works if you answer one row",
    "phase": "8 - Monitoring & Observability",
    "tables": [
        {
            "title": "Architecture A — five pillars vs Advisor categories",
            "columns": ["WAF pillar", "Advisor category you will see", "Lab example"],
            "rows": [
                ["Reliability", "High Availability / Reliability", "Single-region App Service, no backup on a VM disk"],
                ["Security", "Security", "Open NSG 22/3389, storage without HTTPS-only, missing Defender"],
                ["Cost Optimization", "Cost", "Idle Standard SKU, unattached disk, forgotten Public IP"],
                ["Operational Excellence", "OperationalExcellence", "No alerts, no activity-log diagnostic, click-ops only"],
                ["Performance Efficiency", "Performance", "Wrong SKU for a burst, missing CDN you do not need in a lab"],
            ],
            "widths": [42, 70, 70],
        },
        {
            "title": "Architecture B — accept or dismiss with a sentence",
            "columns": ["Recommendation", "Default", "Honest dismiss"],
            "rows": [
                ["Idle / leftover SKU", "Accept → delete or downsize today", "'Lab, deleting today' — then delete"],
                ["Enable diagnostic settings", "Accept on the one app you still run", "'Resource dies tonight' + destroy"],
                ["Reserved Instance buy", "Dismiss for a personal lab", "'No 1-year commit on a learning sub'"],
                ["Close management ports", "Accept if a lab VM is still up", "Do not dismiss as 'I know' while 3389 is open"],
                ["Well-Architected score", "Do not post a score you did not run", "Pillars in notes beat a fake 92/100"],
            ],
            "widths": [44, 69, 69],
        },
        {
            "title": "Architecture C — pitfalls that leave homework skipped",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Dismiss without a note", "Recommendation vanishes; disk still bills", "Portal → Advisor → dismiss reason, plus markdown"],
                ["Accept without a change", "Green bookmark, same public IP", "Accept means you change Azure today"],
                ["Work-sub Advisor dump", "You almost paste a company rec list", "Personal subscription only"],
                ["Pillar as a slogan", "'We value security' and an open NSG", "Name the pillar you are trading"],
                ["Fake assessment post", "LinkedIn graphic of a score you invented", "Five pillars + one real Advisor row"],
            ],
            "widths": [40, 71, 71],
        },
    ],
    "one_liner": "Well-Architected is a report card — Advisor is the teacher who already knows you skipped networking homework.",
    "lab_intro": "Personal subscription. Portal Advisor on that sub only. Notes go in azure-100-labs.",
    "lab": [
        "Write the five pillars in docs/advisor-day78.md: Reliability, Security, Cost Optimization, Operational Excellence, Performance Efficiency.",
        "Portal → Advisor (or az advisor recommendation list). Filter to the personal subscription.",
        "Pick one recommendation. Copy the category, resource name, and impact into the markdown.",
        "Either accept it and make the change (delete, close a port, add a diagnostic), or dismiss it with a written why (not 'not now').",
        "If Advisor is empty (new/empty sub), write that, then run az advisor recommendation list -o table as the receipt.",
        "Do not generate or post a Well-Architected assessment score you did not actually run.",
    ],
    "code_title": "CLI — list Advisor rows you can accept or dismiss honestly",
    "code": (
        "az advisor recommendation list -o table\n"
        "az advisor recommendation list --category Cost --query \"[].{impact:extendedProperties,type:shortDescription.problem}\" -o json\n"
        "# Pillars: Reliability | Security | Cost Optimization | Operational Excellence | Performance Efficiency\n"
        "# One row → accept+change or dismiss+sentence in docs/advisor-day78.md"
    ),
    "checklist": [
        "Five pillars written without a fake numeric score",
        "One Advisor recommendation accepted with a change or dismissed with a reason",
        "docs/advisor-day78.md on the personal repo",
        "Personal subscription only",
        "Posted the LinkedIn document",
    ],
    "tomorrow": "Incident management basics — a 2am runbook and a blameless postmortem template",
}

SPECS[79] = {
    "topic": "Incident Management Basics",
    "subtitle": "Write the runbook before 2am, and write the review without blame",
    "phase": "8 - Monitoring & Observability",
    "tables": [
        {
            "title": "Architecture A — the incident loop (lab-sized)",
            "columns": ["Stage", "Output you write", "Not this"],
            "rows": [
                ["Detect", "Alert / health URL / user report timestamp", "Waiting for a feeling that 'it seems down'"],
                ["Checks", "Ordered probes: DNS, App Service state, App Insights failures", "A 12-page novel nobody opens"],
                ["Mitigate", "Swap slot, scale, revert pipeline, disable a flag", "Root-cause essay while users are still down"],
                ["Communicate", "Who gets a status line, what is true now", "Silent debug while rumors fill the gap"],
                ["Postmortem", "What happened, what we believed, what changes", "Who is stupid — that sentence trains silence"],
            ],
            "widths": [32, 80, 70],
        },
        {
            "title": "Architecture B — mitigate first, then learn",
            "columns": ["Situation", "Do now", "Do after users work"],
            "rows": [
                ["App Service HTTP 5xx", "Restart / swap staging slot / last good artifact", "Dump Kudu and write a novel"],
                ["Bad deploy 10 min ago", "Redeploy previous Build.BuildId", "Hotfix on main with no revert path"],
                ["Secret leaked in a run", "Rotate in Key Vault; fail the pipeline", "Leave the value in the log 'until Monday'"],
                ["You do not know yet", "Mitigate with the last known-good + say 'investigating'", "Invent a root cause to look senior"],
                ["Lab has no real outage", "Still write the page — 2am brains need headings", "Skip the template because 'nothing broke'"],
            ],
            "widths": [40, 71, 71],
        },
        {
            "title": "Architecture C — pitfalls that book a sequel outage",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Blame review", "Quieter chat, same outage later", "Facts, beliefs, changes — no names as villains"],
                ["Novel runbook", "Unread wiki during the incident", "One page: Symptom → Checks → Mitigate → Comms → PM"],
                ["Mitigate = RCA", "Users down while you 'find the why'", "Stop the bleeding first"],
                ["No comms step", "People invent a status", "Write who gets a message in the runbook"],
                ["Employer incident paste", "You almost retell a work outage", "Fictional lab app only. No workplace detail"],
            ],
            "widths": [36, 73, 73],
        },
    ],
    "one_liner": "Postmortems without blame create learning; postmortems with blame create silence.",
    "lab_intro": "Personal repo azure-100-labs. Fictional lab app only — no employer incident details.",
    "lab": [
        "Create docs/runbook-webapp-down.md with headings: Symptom → Checks → Mitigate → Communicate → Postmortem link.",
        "Fill Checks with concrete probes: Portal App Service status, https://<app>.azurewebsites.net/health, App Insights failures, last pipeline deploy.",
        "Fill Mitigate with last-good artifact / slot swap / stop-start — not a root-cause paragraph.",
        "Add docs/postmortem-template.md: Summary, Timeline, What we believed, What was true, What we change, Follow-ups. No blame section.",
        "If you had a real lab failure this week, fill the template once. If not, leave headings plus one fictional timeline labeled FICTION.",
        "Link the two files from README or docs/index. A page that cannot be found at 2am does not exist.",
    ],
    "code_title": "Runbook skeleton — short enough for a 2am brain",
    "code": (
        "# docs/runbook-webapp-down.md\n"
        "# Symptom: GET / or /health != 200 for >2 min\n"
        "# Checks:\n"
        "#   az webapp show -g rg-azure100-lab -n app-azure100-lab --query state\n"
        "#   curl -sI https://<app>.azurewebsites.net/health\n"
        "# Mitigate: az webapp deployment slot swap -g ... -n ... --slot staging\n"
        "#        or redeploy artifact $(Build.BuildId) from the last green run\n"
        "# Communicate: status line to yourself + anyone using the lab URL\n"
        "# Postmortem: docs/postmortem-template.md"
    ),
    "checklist": [
        "docs/runbook-webapp-down.md has the five headings and at least one real CLI/URL check",
        "docs/postmortem-template.md is blameless (no 'who failed' section)",
        "Mitigate is separate from root cause",
        "No employer outage story",
        "Posted the LinkedIn document",
    ],
    "tomorrow": "Phase 8 recap — App Insights + one alert + one dashboard, and a forced failure you can see in five minutes",
}

SPECS[80] = {
    "topic": "Mini Project + Recap (Phase 8)",
    "subtitle": "Deploy is not done — observable is done",
    "phase": "8 - Monitoring & Observability",
    "tables": [
        {
            "title": "Architecture A — Phase 8 stack on one personal app",
            "columns": ["Piece", "Azure object", "Proof today"],
            "rows": [
                ["Flashlight", "Azure Monitor / metrics on the App Service or Container App", "You can see CPU/HTTP without guessing"],
                ["Camera", "Application Insights (microsoft.insights/components)", "A request or exception appears after a hit"],
                ["Scream", "Metric alert + Action Group (email to you)", "Forced 5xx or availability fail pages you"],
                ["Storyboard", "Azure dashboard or App Insights workbook, 3 tiles", "Failure, requests, cost or pipeline health"],
                ["Culture", "Pipeline Analytics + runbook from Days 76/79", "Red has an owner; 2am has a page"],
            ],
            "widths": [32, 80, 70],
        },
        {
            "title": "Architecture B — definition of done",
            "columns": ["Question", "Done", "Not done"],
            "rows": [
                ["Can I force a failure I control?", "Stop the app / hit a /fail route / kill the slot", "Waiting for a 'real' outage"],
                ["Do I see it in ≤5 minutes?", "Insight + alert or dashboard tile updates", "Pretty tiles, no signal"],
                ["Does anyone get a scream?", "Action Group email on the personal inbox", "Alert rule with no action"],
                ["Is leftover spend gone?", "Day 77 deletes still hold", "Dashboard on a cluster you forgot to kill"],
                ["Can I tell the Phase 8 story?", "Monitor, KQL-or-Insights, alert, dashboard, analytics, cost, Advisor, runbook", "A screenshot collage with no forced fail"],
            ],
            "widths": [48, 67, 67],
        },
        {
            "title": "Architecture C — recap pitfalls",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Green pipeline = done", "Users would be in the dark", "Observable is the product"],
                ["Dashboard décor", "Three tiles, no alert, no force-fail", "Force the fail; watch the scream"],
                ["Fake MTTR", "You post 'we improved MTTR 40%'", "Write only what you timed today"],
                ["Work app instrumentation", "You open a company Insights resource", "Personal app, personal sub"],
                ["Runbook missing", "You can see the fail and still freeze", "Link Day 79 pages from the recap note"],
            ],
            "widths": [40, 71, 71],
        },
    ],
    "one_liner": "Phase 8 recap: deploy is not done — observable is done.",
    "lab_intro": "Personal subscription + personal Azure DevOps org. One leftover lab app is enough. Do not stand up a new estate.",
    "lab": [
        "Pick one deployed lab app (App Service or Container Apps) on the personal sub. Note its resource group in docs/phase8-recap.md.",
        "Confirm Application Insights is connected (or create one microsoft.insights/components and wire the app).",
        "Create one metric or log alert + Action Group that emails your personal inbox. Portal → Monitor → Alerts.",
        "Pin a three-tile dashboard: requests or availability, failures/exceptions, and either cost or pipeline pass rate.",
        "Force a reversible failure (stop the web app, hit a /fail route, or swap to a broken slot). Start a timer.",
        "Confirm you can see the failure in Insights/dashboard and/or the alert within five minutes. Write the elapsed time — or write that you could not, and what was missing.",
        "Link the Day 76 health note, Day 77 deletes, Day 78 Advisor row, and Day 79 runbook. Recap without fake MTTR.",
    ],
    "code_title": "Force a failure you can reverse — then prove the camera and scream",
    "code": (
        "az webapp stop -g rg-azure100-lab -n app-azure100-lab\n"
        "# Timer starts. Watch App Insights live metrics + the alert Action Group.\n"
        "az monitor metrics alert list -g rg-azure100-lab -o table\n"
        "az webapp start -g rg-azure100-lab -n app-azure100-lab\n"
        "# Done = detect within 5 minutes. Write the number you measured, not a slogan."
    ),
    "checklist": [
        "App Insights + one alert + one dashboard exist on the personal app",
        "Forced a reversible failure and recorded whether it showed within 5 minutes",
        "docs/phase8-recap.md links Days 76–79 artifacts",
        "No invented MTTR percentage",
        "Leftover paid SKUs still deleted from Day 77",
    ],
    "tomorrow": "Multi-repo vs monorepo — an ADR for this lab, not a trending blog title",
}

SPECS[81] = {
    "topic": "Multi-repo & Monorepo Strategies",
    "subtitle": "Repo strategy is politics with folders — pick the drama you can afford",
    "phase": "9 - Advanced & Enterprise",
    "tables": [
        {
            "title": "Architecture A — same product, two folder politics",
            "columns": ["Dimension", "Monorepo", "Multi-repo"],
            "rows": [
                ["Atomic change", "One PR can move API + pipeline + infra together", "Cross-repo PRs and version pins"],
                ["Ownership", "PATH / CODEOWNERS / folder reviews", "Repo permissions and separate service connections"],
                ["CI graph", "Path filters or you rebuild the world", "Per-repo pipeline; 'which commit is prod' meetings"],
                ["Templates", "templates/ sits next to consumers", "Template repo + refs; version lag"],
                ["This 100-day lab", "Default: one repo, many /src samples", "Split only for a written lifecycle/access reason"],
            ],
            "widths": [36, 73, 73],
        },
        {
            "title": "Architecture B — stay or split (no fake clients)",
            "columns": ["Constraint", "Stay monorepo", "Split repos when"],
            "rows": [
                ["Shared samples / learning repo", "azure-100-labs stays one repo", "Never for a blog trend"],
                ["Different release cadence", "Path-filtered pipelines", "Library ships weekly; app ships daily and the CI graph hurts"],
                ["Different access", "CODEOWNERS on folders", "A secret-producing repo must not be cloneable by the whole org"],
                ["Published library, many consumers", "Still OK if versioned in-tree", "External consumers need a versioned package feed"],
                ["'Enterprise means 10 repos'", "Still one repo", "Scatter is not a landing zone"],
            ],
            "widths": [48, 67, 67],
        },
        {
            "title": "Architecture C — pitfalls that look like architecture",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["No path filter", "A README typo rebuilds .NET and Node", "trigger.paths.include on src/<app>"],
                ["Repo sprawl", "Ten repos, one person, tribal clone lists", "ADR: split only on lifecycle or access"],
                ["Template drift", "Each repo has a slightly different Node version", "Day 82 templates — one contract"],
                ["Fake client list", "You invent companies that 'would split'", "Write constraints, not logos"],
                ["Work repo map", "You diagram an employer org", "Personal lab ADR only"],
            ],
            "widths": [36, 73, 73],
        },
    ],
    "one_liner": "Repo strategy is politics with folders — pick the drama you can afford.",
    "lab_intro": "Personal Azure Repos or personal GitHub remote. ADR lives in azure-100-labs. No employer repo maps.",
    "lab": [
        "Read your current repo layout (folders, pipelines). You are documenting reality, not a dream org chart.",
        "Write docs/adr-repo-strategy.md: Decision = this lab stays a monorepo for samples. Status = accepted.",
        "Add a short 'we would split when' list: different lifecycle, different access, a library consumed as a versioned package. No company names.",
        "If you have two sample apps, add a path filter on one pipeline so a change under src/a does not build src/b.",
        "Note the coordination cost you chose: monorepo CI graph vs multi-repo version meetings.",
        "Commit the ADR. Drama you can afford: one repo, path filters, templates next to consumers.",
    ],
    "code_title": "Path filter — a monorepo that does not rebuild the world",
    "code": (
        "trigger:\n"
        "  branches:\n"
        "    include: [main]\n"
        "  paths:\n"
        "    include:\n"
        "      - src/demo-shipboard/**\n"
        "      - templates/**\n"
        "      - azure-pipelines-shipboard.yml\n"
        "pr:\n"
        "  paths:\n"
        "    include:\n"
        "      - src/demo-shipboard/**"
    ),
    "checklist": [
        "ADR says the 100-day repo stays monorepo, with split criteria that are constraints not logos",
        "Path filter exists or you wrote why a single sample does not need one",
        "No employer repo diagram",
        "docs/adr-repo-strategy.md committed",
        "Posted the LinkedIn document",
    ],
    "tomorrow": "Pipeline templates — extract templates/build.yml so you stop inventing a 15th way to be broken",
}

SPECS[82] = {
    "topic": "Pipeline Templates & Reusable YAML",
    "subtitle": "One contract beats fourteen slightly different broken builds",
    "phase": "9 - Advanced & Enterprise",
    "tables": [
        {
            "title": "Architecture A — reuse knobs in Azure Pipelines YAML",
            "columns": ["Knob", "YAML", "Use today"],
            "rows": [
                ["Step template", "- template: templates/build.yml", "Extract restore/build/test once"],
                ["parameters", "parameters: - name: projectPath type: string", "The contract. No secret defaults"],
                ["extends", "extends: template: templates/pipeline.yml", "Literacy: template owns stages; lab can stay steps"],
                ["Template repo ref", "resource: repo + ref: refs/tags/v1", "Later; same repo templates/ is enough"],
                ["Each: / insert", "${{ each p in parameters.projects }}", "Skip until two consumers exist (Day 90)"],
            ],
            "widths": [36, 78, 68],
        },
        {
            "title": "Architecture B — extract vs leave inline",
            "columns": ["Smell", "Extract", "Leave inline"],
            "rows": [
                ["Same npm ci / dotnet publish in 2 files", "templates/build.yml", "One-off pipeline you will delete tonight"],
                ["Node 20 vs 22 pin", "One parameter nodeVersion", "Do not copy the pin into 14 files"],
                ["Env-specific deploy", "Keep deploy in the root pipeline or a deploy.yml", "Do not hide env names as secret defaults"],
                ["extends vs steps", "steps template first", "extends when you need a locked stage graph"],
                ["Clever defaults", "Required parameters", "A default password or PAT in the template"],
            ],
            "widths": [48, 67, 67],
        },
        {
            "title": "Architecture C — pitfalls that fake reuse",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Copy-paste 'standard'", "14 pipelines, 14 forgotten cache keys", "One template, many callers"],
                ["Rearranged, not extracted", "Still duplicated restore/build after 'cleanup'", "Call site is one template line + path"],
                ["Secret in parameters default", "PAT sitting in templates/", "Variable group / Key Vault; required param"],
                ["Unversioned remote template", "@main of a moving repo", "Same-repo path or a tag ref"],
                ["Abstract novel on day one", "20 layers, zero green runs", "echo ${{ parameters.projectPath }} is a legal first cut"],
            ],
            "widths": [44, 69, 69],
        },
    ],
    "one_liner": "Copy-paste YAML is how organizations invent 14 slightly different ways to be broken.",
    "lab_intro": "Personal Azure DevOps project azure-100-labs. Templates live in the same repo. Microsoft-hosted ubuntu-latest.",
    "lab": [
        "Create templates/build.yml with a required parameter projectPath (string) and a step that builds or echoes that path.",
        "Point the main pipeline at it: steps: - template: templates/build.yml with parameters.projectPath.",
        "Run the pipeline once on ubuntu-latest. The log must show the parameter value.",
        "If two sample apps already exist, call the same template twice with different paths. If not, one caller today; two consumers on Day 90.",
        "Search the repo for duplicated npm ci / dotnet publish / docker build. If still duplicated, you rearranged — extract the rest.",
        "Write docs/templates-day82.md: contract (parameter names) and the rule 'Node version changes in one file'.",
    ],
    "code_title": "templates/build.yml plus a boring call site",
    "code": (
        "# templates/build.yml\n"
        "parameters:\n"
        "- name: projectPath\n"
        "  type: string\n"
        "steps:\n"
        "- script: echo Building ${{ parameters.projectPath }}\n"
        "  displayName: Build ${{ parameters.projectPath }}\n"
        "\n"
        "# azure-pipelines.yml (call site)\n"
        "pool:\n"
        "  vmImage: ubuntu-latest\n"
        "steps:\n"
        "- template: templates/build.yml\n"
        "  parameters:\n"
        "    projectPath: src/demo-shipboard"
    ),
    "checklist": [
        "templates/build.yml exists with a required projectPath",
        "Main pipeline calls the template; log shows the path",
        "No secret defaults in the template",
        "Call site is boring (one template line)",
        "Posted the LinkedIn document",
    ],
    "tomorrow": "Marketplace extensions — a pinch of spice, or a written reason to install zero",
}

SPECS[83] = {
    "topic": "Azure DevOps Extensions & Marketplace",
    "subtitle": "A pinch helps; a handful ruins the stew and the security review",
    "phase": "9 - Advanced & Enterprise",
    "tables": [
        {
            "title": "Architecture A — who runs inside your job",
            "columns": ["Source", "Trust default", "Check before install"],
            "rows": [
                ["Built-in tasks", "Prefer for every 100-day lab", "script, DotNetCoreCLI, PublishBuildArtifacts, Docker"],
                ["Microsoft-published extension", "OK if the task is not already built-in", "Publisher = Microsoft, last update, scopes"],
                ["Known OSS publisher", "Maybe — treat as supply chain", "Repo, last release, permissions on install"],
                ["Unknown publisher", "No for labs", "Wide org scopes + years of silence"],
                ["Custom private extension", "Out of scope for this series", "Do not sideload a .vsix you cannot explain"],
            ],
            "widths": [44, 64, 74],
        },
        {
            "title": "Architecture B — install one or install zero",
            "columns": ["Question", "Install", "Write 'zero' when"],
            "rows": [
                ["Is there a built-in task?", "Do not install", "Always — built-in wins for labs"],
                ["Publisher + update date defensible?", "One extension, note the scopes", "Last update years ago or no public repo"],
                ["Scopes on install", "Least privilege; project not org if possible", "Extension wants all pipelines + all repos"],
                ["Feels 'enterprise' to add five tools", "Still one or zero", "Spice dump on a hello pipeline"],
                ["Work Marketplace already full", "Do not screenshot it", "Personal org only"],
            ],
            "widths": [50, 66, 66],
        },
        {
            "title": "Architecture C — pitfalls the security review can taste",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Abandoned spice", "Task last updated 2018, still in YAML", "Remove the task; replace with script/built-in"],
                ["Tenant guest", "Extension can read every pipeline", "Uninstall; document why zero"],
                ["Task name folklore", "Nobody knows who published 'SuperScan'", "Publisher is part of the bill of materials"],
                ["Install to feel busy", "Five extensions, same hello.yml", "Zero + a written reason still finishes the lab"],
                ["Work org extensions list", "You browse the employer Marketplace", "https://marketplace.visualstudio.com in a personal tenant"],
            ],
            "widths": [40, 71, 71],
        },
    ],
    "one_liner": "Marketplace extensions are spices — a pinch helps; a handful ruins the stew and the security review.",
    "lab_intro": "Personal Azure DevOps org. Prefer built-in tasks. Zero installs with a written reason counts as done.",
    "lab": [
        "Org settings → Extensions (or Marketplace from the personal org). List what is already installed. Screenshot nothing from a work org.",
        "Browse Marketplace for one task you actually need (or confirm you need none). Record publisher, last update, and requested scopes.",
        "If publisher/scopes/update are defensible, install that one extension in the personal org. Otherwise install zero.",
        "Write docs/marketplace-day83.md: the one extension and why, or 'zero — built-in tasks cover the lab' plus the scopes you refused.",
        "Open a pipeline YAML and confirm it does not reference a mystery task name you cannot map to a publisher.",
        "Do not sprinkle Replace Tokens / Slack / extra scanners onto a hello pipeline just to look enterprise.",
    ],
    "code_title": "Lab rule — built-in first; third-party is a supply-chain note",
    "code": (
        "# Prefer Microsoft-maintained / built-in tasks in YAML, for example:\n"
        "steps:\n"
        "- task: UseDotNet@2\n"
        "  inputs:\n"
        "    packageType: sdk\n"
        "    version: '8.0.x'\n"
        "- script: dotnet test --configuration Release\n"
        "  displayName: Test (built-in script)\n"
        "# Third-party: document publisher, permissions, last update — or install zero"
    ),
    "checklist": [
        "Either one defensible install or a written zero",
        "Publisher, last update, and scopes recorded",
        "docs/marketplace-day83.md exists",
        "No work-org Marketplace screenshot",
        "Posted the LinkedIn document",
    ],
    "tomorrow": "Jenkins to Azure Pipelines — migrate guarantees, not the blue ball",
}

SPECS[84] = {
    "topic": "Migrating Jenkins to Azure Pipelines",
    "subtitle": "Migrate the guarantees, leave the nostalgia",
    "phase": "9 - Advanced & Enterprise",
    "tables": [
        {
            "title": "Architecture A — Jenkinsfile concepts → Azure YAML",
            "columns": ["Jenkins", "Azure Pipelines", "Guarantee to keep"],
            "rows": [
                ["agent { label 'linux' }", "pool: vmImage: ubuntu-latest (or a named pool)", "Same OS / network constraint, not the same snowflake"],
                ["stages { stage('Build') }", "stages / jobs / steps", "Order and failure isolation"],
                ["post { always { } }", "condition: always() on a job or a later stage", "Cleanup / publish still runs"],
                ["credentials('id')", "Variable group or Azure Key Vault task", "Secret not in SCM"],
                ["stash / artifact", "PublishPipelineArtifact@1 + download", "Same bytes promoted later"],
                ["Jenkins plugin X", "Built-in task, script, or a written gap", "Do not hide a plugin as 'YAML not ready'"],
            ],
            "widths": [44, 74, 64],
        },
        {
            "title": "Architecture B — migrate vs leave on paper",
            "columns": ["Piece", "Migrate today (paper)", "Leave / rewrite"],
            "rows": [
                ["Compile + test + publish", "Map to jobs on ubuntu-latest", "Pixel-identical stage names"],
                ["Shared library (vars/)", "Template repo or templates/", "Groovy DSL as a religion"],
                ["Freestyle click jobs", "Rewrite as YAML; do not clone the UI", "Rebuilding Jenkins screens in ADO"],
                ["On-prem agent label", "Named pool only if a real constraint", "'We need the same snowflake' nostalgia"],
                ["Plugin that was the product", "Write the gap in the mapping table", "Pretend Azure has a 1:1 task"],
            ],
            "widths": [42, 70, 70],
        },
        {
            "title": "Architecture C — pitfalls that stall a migration",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Nostalgia migration", "Blue-ball UI rebuilt in Boards", "Map guarantees; rename stages freely"],
                ["Secret lift-and-shift", "credentials copied into YAML", "Variable group / Key Vault from Phase 7"],
                ["Plugin iceberg", "'YAML not ready' forever", "List plugins; each is a negotiation"],
                ["Standing up Jenkins for the lab", "You install Jenkins to 'be fair'", "A 20-line sample Jenkinsfile on paper is enough"],
                ["Employer Jenkinsfile paste", "Internal job names in the post", "Write a tiny sample; no work SCM"],
            ],
            "widths": [40, 71, 71],
        },
    ],
    "one_liner": "Jenkins migrations succeed when you migrate pipelines, not nostalgia.",
    "lab_intro": "Paper lab on the personal repo. Do not install Jenkins. Do not paste an employer Jenkinsfile.",
    "lab": [
        "Write samples/jenkins/Jenkinsfile with agent, three stages (Build, Test, Publish), and a post { always } block. Keep it tiny and fictional.",
        "Create docs/jenkins-map-day84.md with a table: Jenkins line → Azure YAML → guarantee kept.",
        "Translate to samples/jenkins/azure-pipelines.yml: pool ubuntu-latest, stages/jobs, condition: always() publish, no inline secrets.",
        "Map credentials('id') to a variable group name or Key Vault task — write the name, do not put a value in Git.",
        "List two Jenkins plugins the sample does not need, and one fictional plugin that would be a real gap (e.g. a licensed scanner).",
        "Do not stand up a Jenkins controller. The proof is the mapping, not a blue ball.",
    ],
    "code_title": "Same guarantees — Jenkinsfile fragment vs Azure YAML",
    "code": (
        "# Jenkins (sample only)\n"
        "# agent { label 'linux' }\n"
        "# stage('Test') { sh 'dotnet test' }\n"
        "# post { always { archiveArtifacts '**/TestResults/**' } }\n"
        "\n"
        "pool:\n"
        "  vmImage: ubuntu-latest\n"
        "stages:\n"
        "- stage: Test\n"
        "  jobs:\n"
        "  - job: test\n"
        "    steps:\n"
        "    - script: dotnet test --logger trx\n"
        "      displayName: Test\n"
        "    - task: PublishTestResults@2\n"
        "      condition: always()\n"
        "      inputs:\n"
        "        testResultsFormat: VSTest\n"
        "        testResultsFiles: '**/*.trx'"
    ),
    "checklist": [
        "Sample Jenkinsfile and mapped azure-pipelines.yml both exist",
        "docs/jenkins-map-day84.md lists agent/stages/post/credentials/plugins",
        "No employer Jenkinsfile",
        "No Jenkins controller installed for the lab",
        "Posted the LinkedIn document",
    ],
    "tomorrow": "Hybrid and multi-cloud CI/CD — survey the risks; do not buy a second cloud for a slide",
}

SPECS[85] = {
    "topic": "Hybrid & Multi-cloud CI/CD",
    "subtitle": "Insurance is priced — buy it for a constraint, not a slide",
    "phase": "9 - Advanced & Enterprise",
    "tables": [
        {
            "title": "Architecture A — one pipeline, extra control planes (survey)",
            "columns": ["Layer", "Azure-only (this series)", "Hybrid / extra cloud"],
            "rows": [
                ["Build", "Azure Pipelines + ubuntu-latest", "Still build once; artifact/image is the passport"],
                ["Identity", "Workload identity / service connection to Azure", "Second cloud IAM + a second secret envelope"],
                ["Secrets", "Key Vault + variable group", "Copied cloud keys = two postcards to lose"],
                ["Network", "Public Microsoft-hosted is enough for labs", "Self-hosted pool / VPN / private endpoint for on-prem"],
                ["Deploy task", "AzureWebApp / AzureContainerApps / az", "Cloud-specific task only if a real second target exists"],
            ],
            "widths": [32, 75, 75],
        },
        {
            "title": "Architecture B — when to stay one-cloud-deep",
            "columns": ["Claimed reason", "Default in these 100 days", "Real constraint (later)"],
            "rows": [
                ["Diagram looks worldly", "Stay Azure-only", "Never a reason"],
                ["'We might need AWS someday'", "Stay Azure-only", "An actual second estate you already operate"],
                ["Data residency / existing estate", "Write it as a future constraint", "Legal or already-running second cloud"],
                ["On-prem artifact feed", "Do not fake a VPN in the lab", "Self-hosted agent when a private hop is real"],
                ["Personal AWS account 'just to try'", "Skip unless destroy plan + budget exist", "You accept a second bill and will delete tonight"],
            ],
            "widths": [50, 66, 66],
        },
        {
            "title": "Architecture C — pitfalls that double the blast radius",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Rebuild per cloud", "Two images, two 'latest' tags", "Build once; deploy the same digest"],
                ["Secret photocopy", "AWS key in a variable group next to Azure", "One vault per cloud; never in YAML"],
                ["Hosted agent vs on-prem", "Job fails on a private IP", "That is a Day 22 constraint — not a multi-cloud trophy"],
                ["Slide-driven lab", "You open a second portal to feel senior", "One-pager of risks; zero extra deploys"],
                ["Work multi-cloud map", "Employer AWS + Azure diagram", "Fictional risks only; personal Azure stays the gym"],
            ],
            "widths": [40, 71, 71],
        },
    ],
    "one_liner": "Multi-cloud is insurance and complexity — buy it for a reason, not a slide.",
    "lab_intro": "Survey only. Personal Azure. Do not deploy to AWS/GCP unless you already have a personal account and a destroy plan.",
    "lab": [
        "Write docs/multicloud-risks-day85.md with three sections: secrets, identity, network. Each section gets one real failure mode.",
        "Write the series rule in that file: one cloud deep for Days 1–100 unless a named constraint appears.",
        "Sketch 'build once in Azure DevOps → deploy with a cloud-specific task' as a four-box diagram. The artifact is the passport.",
        "List why a Microsoft-hosted agent cannot see an on-prem feed (Day 22). Hybrid is often a network hop, not a second logo.",
        "Do not create AWS/GCP resources 'to try' unless the personal account and destroy command are already ready. If you skip, write 'did not deploy'.",
        "No employer multi-cloud diagram and no invented customer estate.",
    ],
    "code_title": "Pattern note — build once; do not open a second gym membership",
    "code": (
        "# Pattern (survey, not a second deploy):\n"
        "# 1) Azure Pipelines job on ubuntu-latest builds the image/artifact once\n"
        "# 2) PublishPipelineArtifact@1 or docker push to ONE registry\n"
        "# 3) Only if a real second cloud exists: a later job uses that cloud's deploy task\n"
        "# Prefer one cloud deep in this 100 days.\n"
        "pool:\n"
        "  vmImage: ubuntu-latest\n"
        "steps:\n"
        "- script: echo \"Build once. Passport is the artifact, not a second portal.\"\n"
        "  displayName: Multi-cloud survey reminder"
    ),
    "checklist": [
        "Risks one-pager covers secrets, identity, and network",
        "Series rule written: one cloud deep",
        "Did not open a second cloud 'for the slide' (or destroyed it the same night)",
        "No employer estate diagram",
        "Posted the LinkedIn document",
    ],
    "tomorrow": "Disaster recovery and backup — RPO/RTO as sentences, and a restore that is not fan fiction",
}

SPECS[86] = {
    "topic": "Disaster Recovery & Backup",
    "subtitle": "A backup you never restore is fan fiction",
    "phase": "9 - Advanced & Enterprise",
    "tables": [
        {
            "title": "Architecture A — DR words mapped to Azure knobs",
            "columns": ["Term", "Meaning", "Lab-sized control"],
            "rows": [
                ["RPO", "How much data loss is acceptable", "Write a target (e.g. 24h lab notes) — label it TARGET"],
                ["RTO", "How fast you must be back", "Write a target (e.g. 4h) — measure a drill, do not invent"],
                ["Soft delete", "Recover a deleted secret/blob", "Key Vault enableSoftDelete + secret recover"],
                ["Local HA", "Disk / zone / slot swap", "Not DR. Same-region nicer failure"],
                ["Geo", "GRS/GZRS / paired region", "Costs money; skip buy for a hello lab unless you drill it"],
                ["Drill", "Restore once on purpose", "Recover a dummy secret or restore a backup"],
            ],
            "widths": [32, 70, 80],
        },
        {
            "title": "Architecture B — pick the cheapest proof that is still a restore",
            "columns": ["Need", "Default lab move", "Overkill today"],
            "rows": [
                ["Prove restore exists", "Dummy Key Vault secret: delete → recover", "Paid GRS on a storage account you will kill"],
                ["Vault already soft-delete on", "az keyvault show and record the flag", "Rebuild a vault to tick a box"],
                ["App files", "Redeploy last artifact (that is RTO for compute)", "ASR on a personal VM you do not have"],
                ["'Zero RPO / instant RTO'", "Rewrite as a wish; pick numbers you could fund", "Post those numbers as achievements"],
                ["Same-region backup only", "Call it backup, not DR", "Slide titled 'geo-redundant' with LRS"],
            ],
            "widths": [42, 76, 64],
        },
        {
            "title": "Architecture C — pitfalls that keep the fiction in the policy",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Never restored", "Beautiful backup policy, wrong password on the day", "Drill once; time it"],
                ["Vault in the fire", "Backup in the same region as the app and the laptop notes", "Say so in the doc; do not call it DR"],
                ["Soft delete off (legacy)", "Deleted secret is gone", "az keyvault update / new vault defaults"],
                ["Purge on a drill", "You purge instead of recover", "secret recover; purge is the opposite lesson"],
                ["Work vault screenshot", "Company Key Vault in the post", "Personal vault or skip the screenshot"],
            ],
            "widths": [40, 71, 71],
        },
    ],
    "one_liner": "Backups you never restore are fan fiction.",
    "lab_intro": "Personal subscription. Use a lab Key Vault you already own, or skip geo-SKU spend. Targets are labeled TARGET, not trophies.",
    "lab": [
        "Write RPO and RTO targets for the fictional lab app in docs/dr-day86.md. Label them TARGET. 'Zero / instant' is a wish — rewrite it.",
        "az keyvault list -o table on the personal sub. Pick one lab vault (or record that you have none and stop before buying geo).",
        "az keyvault show -n <vault> --query \"{soft:properties.enableSoftDelete,purge:properties.enablePurgeProtection}\". Soft delete should be true on modern vaults.",
        "Drill: set a dummy secret drill-day86=temp, delete it, then az keyvault secret recover. Write the elapsed time.",
        "State in the markdown whether this is backup (same region) or DR (paired region / second stamp). Do not call LRS a DR plan.",
        "If you cannot restore today, write 'DR plan is still fiction' — that sentence is the lesson.",
    ],
    "code_title": "CLI — a restore with training wheels (Key Vault soft delete)",
    "code": (
        "az keyvault show -n kv-azure100-lab --query \"{soft:properties.enableSoftDelete,purge:properties.enablePurgeProtection}\"\n"
        "az keyvault secret set --vault-name kv-azure100-lab --name drill-day86 --value temp-only\n"
        "az keyvault secret delete --vault-name kv-azure100-lab --name drill-day86\n"
        "az keyvault secret recover --vault-name kv-azure100-lab --name drill-day86\n"
        "az keyvault secret delete --vault-name kv-azure100-lab --name drill-day86\n"
        "# Time the recover. A number you did not measure is not an RTO."
    ),
    "checklist": [
        "RPO/RTO written as TARGETs, not achievements",
        "One restore drill completed, or an explicit 'still fiction' sentence",
        "Soft-delete flag recorded",
        "Did not call same-region backup a DR story",
        "docs/dr-day86.md on the personal repo",
    ],
    "tomorrow": "Azure Landing Zones — city planning on paper for a clearly fictional company",
}

SPECS[87] = {
    "topic": "Azure Landing Zones",
    "subtitle": "City planning for Azure — skip it and resource groups squat",
    "phase": "9 - Advanced & Enterprise",
    "tables": [
        {
            "title": "Architecture A — CAF pieces (sketch, do not deploy an enterprise)",
            "columns": ["Piece", "Job", "What you draw today"],
            "rows": [
                ["Management groups", "Policy and RBAC inheritance", "Root → Platform → Landing zones → Sandboxes"],
                ["Platform sub", "Identity, connectivity, management", "Hub VNet, firewall/DNS box, log sink"],
                ["Landing zone sub", "Workloads", "One spoke VNet per app family"],
                ["Hub-spoke", "Shared network path, not a mesh of accidents", "Peering lines hub↔spoke only"],
                ["Azure Policy", "Guardrails at the MG, not 200 copies", "One assignment note: e.g. allowed locations"],
                ["Identity", "Entra + RBAC from Phase 7", "No landing zone is 'just a VNet'"],
            ],
            "widths": [40, 71, 71],
        },
        {
            "title": "Architecture B — sketch vs stand up",
            "columns": ["Urge", "Do", "Do not"],
            "rows": [
                ["Learn CAF", "Read the landing zone overview on Microsoft Learn", "Deploy enterprise-scale into a personal sub"],
                ["Need a picture", "Paper or docs/landing-zone-day87.md mermaid", "Use a real company logo"],
                ["Policy curiosity", "Name one policy at Sandbox MG", "Assign production policies to a learning sub"],
                ["Hub firewall SKU", "Draw the box; skip the bill", "Buy Azure Firewall Premium for a sketch"],
                ["'Make it real'", "Your existing lab RG is a sandbox spoke in words", "Eight subscriptions to look enterprise"],
            ],
            "widths": [36, 73, 73],
        },
        {
            "title": "Architecture C — shantytown failure modes",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["RG squatters", "One sub, 40 RGs, no MG, public IPs everywhere", "Sandboxes + a delete policy in the sketch"],
                ["Policy at the wrong scope", "200 identical assignments on RGs", "Assign at the management group"],
                ["Hub as a workload dump", "App VMs in the hub", "Spokes hold apps; hub holds shared network"],
                ["Landing zone without identity", "Pretty VNets, Owner everywhere", "RBAC + Entra on the diagram"],
                ["Fake corp simulation", "Invented employees and savings", "Clearly FICTION; no logos, no customers"],
            ],
            "widths": [44, 69, 69],
        },
    ],
    "one_liner": "Landing zones are city planning for Azure — skip them and you get shantytowns of resource groups.",
    "lab_intro": "Paper and Microsoft Learn only. Personal notes. Clearly fictional company — no logos, no customers, no employer map.",
    "lab": [
        "Read the Cloud Adoption Framework landing zone overview on Microsoft Learn (enterprise-scale / management groups / hub-spoke).",
        "Sketch in docs/landing-zone-day87.md: management groups (Platform, Landing zones, Sandboxes), one hub, two spokes.",
        "Label hub: connectivity, DNS, firewall. Label spokes: workloads. Label sandboxes: personal labs like azure-100.",
        "Write one policy you would assign at Sandboxes (e.g. allowed locations = your lab region; deny public IP on non-lab).",
        "Write one sentence: this is FICTION. You are not deploying ALZ Terraform/Bicep into the personal subscription today.",
        "Optional: az account management-group list -o table on the personal tenant. Empty is a valid receipt.",
    ],
    "code_title": "Sketch checklist — city plan, not a second subscription factory",
    "code": (
        "# Hub: shared networking / firewall / DNS\n"
        "# Spokes: workloads (peer to hub only)\n"
        "# Management groups + Azure Policy at the right MG\n"
        "az account management-group list -o table\n"
        "# If empty: you still have a valid paper landing zone.\n"
        "# Do not az deployment sub create an enterprise-scale lab tonight."
    ),
    "checklist": [
        "CAF overview read",
        "Hub-spoke + MG sketch exists and is labeled FICTION",
        "One sandbox policy named",
        "Did not deploy enterprise-scale into the personal sub",
        "No logos, no employer org chart",
    ],
    "tomorrow": "GitOps with Flux or Argo CD — Git as desired state, not a kubectl petting zoo",
}

SPECS[88] = {
    "topic": "GitOps with Flux/Argo CD",
    "subtitle": "The cluster stops being a petting zoo for kubectl",
    "phase": "9 - Advanced & Enterprise",
    "tables": [
        {
            "title": "Architecture A — push CD vs pull GitOps",
            "columns": ["Dimension", "Azure Pipelines push (Day 57)", "Flux / Argo pull"],
            "rows": [
                ["Source of truth", "Pipeline run + what it last applied", "Git commit the controller wants"],
                ["Who talks to the API", "Pipeline job (service connection / kubeconfig)", "In-cluster controller reconciles"],
                ["Change window", "YAML stage + env approval", "PR review, then merge; cluster follows"],
                ["Drift", "Unless you re-run, drift can hide", "Reconcile loop notices and heals or fights you"],
                ["Hotfix temptation", "az / kubectl in a job or from a laptop", "kubectl apply is debt; PR is the path"],
                ["Lab default", "Push is enough for App Service / Container Apps", "GitOps when a cluster is the product"],
            ],
            "widths": [40, 71, 71],
        },
        {
            "title": "Architecture B — when to pull, when to keep pushing",
            "columns": ["Workload", "Default", "Move to GitOps when"],
            "rows": [
                ["App Service / Functions zip", "Push from Azure Pipelines", "Never required"],
                ["Container Apps revision", "Push image tag/digest from CI", "You want the revision YAML in Git as truth"],
                ["AKS / any cluster", "Optional local Flux quickstart", "Multiple people kubectl and the zoo starts"],
                ["Secret objects", "Sealed-secrets / External Secrets / KV CSI", "Plain Secret YAML in a public repo"],
                ["No cluster today", "Written comparison only", "Do not buy AKS just to install Flux"],
            ],
            "widths": [42, 70, 70],
        },
        {
            "title": "Architecture C — petting-zoo failure modes",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Cowboy kubectl", "Three people apply; Git is a rumor", "If it is not in the repo, it will drift back"],
                ["Pipeline push + silent kubectl", "CI green, cluster different", "Pick a source of truth; disable the habit"],
                ["Latest tag in GitOps", "Controller 'reconciles' a moving target", "Immutable digest / Build.BuildId"],
                ["Secrets in the GitOps repo", "Public fork has the connection string", "External Secrets / KV; never raw Secret YAML"],
                ["Flux on a forgotten AKS", "Controller + cluster bill after the lesson", "Local kind/minikube or paper only; destroy AKS"],
            ],
            "widths": [40, 71, 71],
        },
    ],
    "one_liner": "GitOps means the cluster stops being a petting zoo for kubectl.",
    "lab_intro": "Read first. Optional local Flux. Personal Azure only — destroy any AKS you start. No employer cluster kubeconfig.",
    "lab": [
        "Read the GitOps principles (desired state in Git, declarative, pulled, continuously reconciled). Write them in docs/gitops-day88.md.",
        "Write a push-vs-pull table comparing Azure Pipelines apply (Day 57) to Flux/Argo reconcile.",
        "Optional: Flux quickstart on local kind/minikube — not on a leftover paid AKS unless you will destroy it tonight.",
        "Add a sample manifests/gitops/kustomization.yaml (or Flux GitRepository YAML) that points at this personal repo path. Do not apply to a work cluster.",
        "Write the cowboy rule: no kubectl hotfix habit even in a lab. A PR changes desired state.",
        "If you skip the cluster, the written comparison still finishes the lab. Say so in the markdown.",
    ],
    "code_title": "Desired state fragment — a controller would reconcile this, not your laptop",
    "code": (
        "# manifests/gitops/kustomization.yaml (sample; apply only to a personal local cluster)\n"
        "apiVersion: kustomize.config.k8s.io/v1beta1\n"
        "kind: Kustomization\n"
        "resources:\n"
        "  - deployment.yaml\n"
        "images:\n"
        "  - name: demo-shipboard\n"
        "    newName: <youracr>.azurecr.io/demo-shipboard\n"
        "    newTag: \"$(Build.BuildId)\"   # pin a digest in real use; never latest-as-truth\n"
        "# PR to change prod. No kubectl cowboy moves."
    ),
    "checklist": [
        "Push-vs-pull written in docs/gitops-day88.md",
        "Sample manifest or Flux YAML in the personal repo",
        "No work-cluster kubeconfig",
        "Any AKS started for this lab is destroyed, or you used local-only",
        "Posted the LinkedIn document",
    ],
    "tomorrow": "Scaling DevOps for teams — five paved-road capabilities, not a queue that only says no",
}

SPECS[89] = {
    "topic": "Scaling DevOps for Large Teams",
    "subtitle": "Platform engineering is DevOps that productized the paved road",
    "phase": "9 - Advanced & Enterprise",
    "tables": [
        {
            "title": "Architecture A — a 50-dev catalog mapped to Azure DevOps",
            "columns": ["Capability", "What a developer gets", "You already have the seed"],
            "rows": [
                ["App pipeline template", "One YAML call, pinned SDK", "Day 82 templates/build.yml"],
                ["RG + budget bootstrap", "Named RG + a budget alert", "Day 77 Cost Management"],
                ["Secret fetch", "Key Vault reference, not a .env in Git", "Phase 7 variable group / KV"],
                ["Env promotion", "Same artifact, approvals on staging/prod", "Day 39 / Environments"],
                ["Golden-path docs", "How to open a PR that ships", "docs/ that pipelines actually use"],
                ["Optional sixth", "Project scaffold (repo + pipeline file)", "azure-100-labs as the example path"],
            ],
            "widths": [44, 69, 69],
        },
        {
            "title": "Architecture B — ticket theater vs self-service",
            "columns": ["Ask from a 50th developer", "Ticket theater", "Paved road"],
            "rows": [
                ["New app pipeline", "Platform queue, three days", "Copy a template; CI on first PR"],
                ["New RG", "Someone with Owner clicks Portal", "Bootstrap pipeline + budget"],
                ["Prod deploy", "Ping a human in chat", "Environment approval + checks"],
                ["Node version bump", "14 YAML PRs", "One template parameter"],
                ["Exception to policy", "Shadow IT in a personal cloud", "Documented exemption at the MG"],
            ],
            "widths": [44, 69, 69],
        },
        {
            "title": "Architecture C — platforms that do not scale",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Only-no platform", "Queue of refusals; shadow pipelines", "Ship a catalog; version it"],
                ["Wiki mural", "Golden Path.docx nobody's YAML uses", "Guardrails in the template, not only in prose"],
                ["Fake org chart", "Invented VP names and headcount", "Hypothetical 50-dev catalog; no logos"],
                ["Unversioned templates", "Breaking change lands on every app Friday", "Tag the template repo / path + changelog"],
                ["Work portal screenshot", "Internal developer portal of an employer", "List capabilities in markdown only"],
            ],
            "widths": [40, 71, 71],
        },
    ],
    "one_liner": "Platform engineering is DevOps that productized the paved road.",
    "lab_intro": "Hypothetical 50-dev org — hypothetical means hypothetical. Personal repo only. No customer names.",
    "lab": [
        "List five platform capabilities in docs/platform-catalog-day89.md that you would want as the 50th developer.",
        "Map each row to Azure DevOps: template path, Environment, variable group, budget, or docs file.",
        "Include pipeline template, RG+budget bootstrap, golden-path docs, plus two you care about (secret fetch, env promotion).",
        "Write one 'ticket theater' example you are replacing (e.g. 'please make a pipeline').",
        "Add a versioning note: how a template change reaches consumers without a Friday surprise.",
        "Do not invent a customer, a headcount chart, or a sales pitch. The catalog is the lab.",
    ],
    "code_title": "Catalog seed — self-service ideas that already map to this series",
    "code": (
        "# docs/platform-catalog-day89.md (outline)\n"
        "# - app pipeline template     → templates/build.yml (Day 82)\n"
        "# - RG + budget bootstrap    → az group create + consumption budget\n"
        "# - golden path docs         → docs/golden-path.md (PR → CI → env)\n"
        "# - secret fetch             → Key Vault task / variable group\n"
        "# - env promotion            → Environments + approvals; same Build.BuildId\n"
        "# Version the templates. A paved road nobody walks is a mural."
    ),
    "checklist": [
        "Five capabilities listed and mapped to Azure DevOps + templates",
        "Hypothetical catalog only — no logos, no customers",
        "docs/platform-catalog-day89.md committed",
        "Ticket theater vs paved road written once",
        "Posted the LinkedIn document",
    ],
    "tomorrow": "Phase 9 recap — one template, two consumers, one green run each",
}

SPECS[90] = {
    "topic": "Mini Project + Recap (Phase 9)",
    "subtitle": "Enterprise is reuse plus guardrails, not more YAML copy-paste",
    "phase": "9 - Advanced & Enterprise",
    "tables": [
        {
            "title": "Architecture A — Phase 9 artifacts you can point at",
            "columns": ["Day", "Artifact", "Still true?"],
            "rows": [
                ["81", "ADR: lab stays monorepo", "Unless you changed it on purpose"],
                ["82–90", "templates/ consumed by two pipelines", "Definition of done today"],
                ["83", "Marketplace: one spice or written zero", "No mystery publishers"],
                ["84", "Jenkins map on paper", "Guarantees, not blue balls"],
                ["85–88", "Risks, DR drill, LZ sketch, GitOps note", "Paper architecture counts"],
                ["89", "Five paved-road capabilities", "Templates are the road, not a mural"],
            ],
            "widths": [24, 90, 68],
        },
        {
            "title": "Architecture B — done means two green consumers",
            "columns": ["Check", "Pass", "Fail"],
            "rows": [
                ["One template file", "templates/build.yml (or sibling) is the contract", "Two copies of the same steps"],
                ["Two callers", "Two YAML pipelines pass parameters in", "You duplicated YAML to go green"],
                ["Two green runs", "Each consumer has a green build today", "One green, one 'will fix later'"],
                ["Guardrails", "No secrets in the template; hosted pool default", "PAT in parameters.default"],
                ["Path filters", "A change in consumer A does not have to rebuild B", "World rebuild on a README typo"],
            ],
            "widths": [36, 73, 73],
        },
        {
            "title": "Architecture C — recap pitfalls",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Duplicated to go green", "templates/ exists and so do pasted twins", "Delete the twins; call the template"],
                ["Third unique snowflake", "A leftover pipeline still on Node 18", "Extract or admit leftover homework"],
                ["Enterprise font", "Slide language, one consumer", "Reuse + a gate that still bites"],
                ["Guardrail regression", "Template echoes a secret", "Fail the recap; move to KV"],
                ["Work template library", "You export an employer YAML library", "Personal repo only"],
            ],
            "widths": [40, 71, 71],
        },
    ],
    "one_liner": "Phase 9 recap: enterprise is reuse + guardrails, not more YAML copy-paste.",
    "lab_intro": "Personal Azure DevOps project azure-100-labs. Same-repo templates/. Microsoft-hosted ubuntu-latest.",
    "lab": [
        "Finish templates/ so one file is the build contract (projectPath and any SDK pin).",
        "Create or update two sample pipelines that both call that template with different paths (even if the second only echoes).",
        "Run both pipelines. Capture two green run IDs in docs/phase9-recap.md.",
        "Grep the repo for duplicated restore/build steps outside the template. Extract or list as leftover homework.",
        "Re-read the Day 81 ADR. Still monorepo unless you wrote a new decision.",
        "Link Days 83–89 notes (marketplace, Jenkins map, multi-cloud risks, DR, landing zone, GitOps, catalog).",
        "Do not add a third unique pipeline to look enterprise.",
    ],
    "code_title": "Two consumers — one template, two green runs",
    "code": (
        "# azure-pipelines-a.yml\n"
        "pool:\n"
        "  vmImage: ubuntu-latest\n"
        "steps:\n"
        "- template: templates/build.yml\n"
        "  parameters:\n"
        "    projectPath: src/demo-shipboard\n"
        "\n"
        "# azure-pipelines-b.yml\n"
        "pool:\n"
        "  vmImage: ubuntu-latest\n"
        "steps:\n"
        "- template: templates/build.yml\n"
        "  parameters:\n"
        "    projectPath: src/samples/second"
    ),
    "checklist": [
        "One template, two consumers, two green run IDs written down",
        "No secret defaults in the template",
        "docs/phase9-recap.md links the Phase 9 paper artifacts",
        "Did not duplicate YAML just to go green",
        "Posted the LinkedIn document",
    ],
    "tomorrow": "Capstone 1 — a thin public demo slice you can walk in five minutes, not a new ecommerce",
}

SPECS[91] = {
    "topic": "Capstone Project 1 - E2E App CI/CD",
    "subtitle": "A public demo slice you can walk in five minutes — not a new ecommerce",
    "phase": "10 - Portfolio & Public Launch",
    "tables": [
        {
            "title": "Architecture A — public demo-shipboard (not employer work)",
            "columns": ["Box", "Personal Azure object", "What a stranger sees"],
            "rows": [
                ["Repo", "Personal Azure Repos or GitHub: capstone/", "README diagram + /health source"],
                ["CI", "Azure Pipeline on ubuntu-latest", "Restore, test, publish zip/artifact"],
                ["Artifact", "PublishPipelineArtifact@1 named drop", "Same bytes that will be promoted"],
                ["Dev env", "Azure App Service F1 or Container Apps consumption", "https://<app>-dev.azurewebsites.net/health"],
                ["Staging", "Second slot or second app + Environment approval", "Same artifact, different URL"],
                ["Identity", "Project-scoped service connection", "No user PAT in YAML"],
            ],
            "widths": [32, 80, 70],
        },
        {
            "title": "Architecture B — scope control (In vs Out)",
            "columns": ["Idea", "In (MVP)", "Out (ambition)"],
            "rows": [
                ["App shape", "One service: GET / and GET /health return build id + env", "Payments, carts, recommendations ML"],
                ["Topology", "One repo folder capstone/", "12 microservices and a service mesh"],
                ["CI/CD", "Tests + artifact + deploy + README diagram", "Multi-region active-active"],
                ["Data", "In-memory or one small Azure Table/SQLite file", "Cosmos + SQL + Redis 'because production'"],
                ["Reuse", "Harden an earlier 100-day app", "New shop-clone repo on Day 91"],
            ],
            "widths": [32, 80, 70],
        },
        {
            "title": "Architecture C — capstone failure modes",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Ambition spiral", "Empty repo, grand README", "Thin vertical slice: build→test→URL"],
                ["Rebuild per environment", "Dev and staging compile twice", "Promote the same artifact / Build.BuildId"],
                ["Employer app lift", "Internal names, work screenshots", "Public fictional demo only"],
                ["No diagram", "You cannot demo in five minutes", "Four boxes: repo, pipeline, env, app"],
                ["Secret in the repo", "Connection string in appsettings", "Key Vault / pipeline secret; F1 can still read KV refs"],
            ],
            "widths": [40, 71, 71],
        },
    ],
    "one_liner": "Capstones fail from ambition — ship a thin vertical slice you can demo in five minutes.",
    "lab_intro": "Public demo system on a personal subscription and personal org. Work in capstone/. Do not start a giant ecommerce. Do not import employer code.",
    "lab": [
        "Create capstone/README.md with In/Out lists and a four-box diagram: repo → pipeline → environment → App Service (or Container Apps).",
        "Reuse an earlier lab app or a tiny new demo-shipboard that returns { status, env, buildId } on GET /health. One service only.",
        "Add or harden azure-pipelines.yml: trigger on capstone/**, ubuntu-latest, test, PublishPipelineArtifact@1.",
        "Deploy that artifact to a personal F1 App Service or consumption Container App. Record the public /health URL.",
        "Add a staging promotion path (slot or second app) that reuses the same artifact. Approval can be you.",
        "Walk the demo in five minutes: PR or push → green run → URL shows the build id. If you cannot, cut scope.",
        "No payments, no ML, no 12 services. If you want to add one, read the Out list out loud.",
    ],
    "code_title": "MVP pipeline — one service, tests, artifact, deploy",
    "code": (
        "trigger:\n"
        "  paths:\n"
        "    include: [capstone/**]\n"
        "pool:\n"
        "  vmImage: ubuntu-latest\n"
        "stages:\n"
        "- stage: CI\n"
        "  jobs:\n"
        "  - job: build\n"
        "    steps:\n"
        "    - script: |\n"
        "        test -f capstone/README.md\n"
        "        echo CI for demo-shipboard $(Build.BuildId)\n"
        "      displayName: Prove repo + build id\n"
        "    - task: PublishPipelineArtifact@1\n"
        "      inputs:\n"
        "        targetPath: capstone\n"
        "        artifact: drop"
    ),
    "checklist": [
        "capstone/ exists with In/Out and a diagram",
        "Public /health (or equivalent) on a personal Azure app",
        "CI publishes an artifact; staging reuses it",
        "No employer code, no ecommerce scaffold",
        "Five-minute demo path written in the README",
    ],
    "tomorrow": "Capstone 2 — the same public demo in a container tuxedo, not a Netflix clone",
}

SPECS[92] = {
    "topic": "Capstone Project 2 - Containers Path",
    "subtitle": "Same public demo, container tuxedo — not a new Netflix clone",
    "phase": "10 - Portfolio & Public Launch",
    "tables": [
        {
            "title": "Architecture A — package demo-shipboard as an image",
            "columns": ["Box", "Personal Azure object", "Pin"],
            "rows": [
                ["Dockerfile", "capstone/Dockerfile in the same repo", "Non-root user if you can; no secrets in layers"],
                ["CI build", "Docker@2 or docker build in the pipeline", "Tag $(Build.BuildId), not latest-as-truth"],
                ["Registry", "Azure Container Registry Basic (or destroy after)", "acr login from the service connection"],
                ["Runtime default", "Container Apps consumption or App Service containers", "Same /health contract as Day 91"],
                ["AKS", "Optional only", "Destroy the cluster tonight if you create it"],
                ["GitOps (optional)", "Manifest points at the digest", "Day 88 rule: no cowboy kubectl"],
            ],
            "widths": [36, 78, 68],
        },
        {
            "title": "Architecture B — where the tuxedo runs",
            "columns": ["Constraint", "Default", "AKS only when"],
            "rows": [
                ["Cost / time box", "Container Apps or App Service containers", "You will destroy AKS and already know kubectl"],
                ["Need ingress + scale-to-zero", "Container Apps", "You want node pools for a portfolio screenshot"],
                ["Already on zip deploy", "Keep the app; change packaging", "Do not throw away Day 91 to start microservices"],
                ["Laptop docker push", "Forbidden as the capstone story", "Never — the pipeline pushes"],
                ["Image tag", "Build.BuildId or sha digest", "latest as the promotion story"],
            ],
            "widths": [42, 70, 70],
        },
        {
            "title": "Architecture C — tuxedo pitfalls",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["New Netflix clone", "Empty repo, new ambition", "Same actor as Day 91"],
                ["latest-as-truth", "Staging drifted from the green build", "Promote a digest / Build.BuildId"],
                ["Laptop is CI", "docker push from your PC in the README", "Pipeline build/push is the story"],
                ["Forgotten AKS", "Cluster bills after the tuxedo photo", "Destroy; prefer Container Apps"],
                ["Secrets in the image", "ENV PASSWORD= in Dockerfile", "Runtime env / Key Vault; rebuild if it leaked"],
            ],
            "widths": [40, 71, 71],
        },
    ],
    "one_liner": "Day 92 is the same app in a container tuxedo — not a new Netflix clone.",
    "lab_intro": "Same capstone/ app as Day 91. Personal ACR + personal runtime. AKS optional and destroyed if used.",
    "lab": [
        "Add capstone/Dockerfile that serves the same /health contract. No secrets in ENV. Build locally only to debug, not to publish.",
        "Create or reuse a personal ACR. Note the login server in capstone/README.md.",
        "Extend the pipeline: docker build, tag $(Build.BuildId), docker push to ACR. Service connection does the auth.",
        "Deploy that image to Container Apps or App Service for containers. Confirm /health shows the new build id.",
        "Update the README diagram with Registry + runtime boxes. Five-minute demo still has to work.",
        "If you opened AKS, write the destroy command in the README and run it when the screenshot exists.",
        "Do not start a new streaming-platform repo.",
    ],
    "code_title": "Pipeline fragment — build/push the same app, pin the tag",
    "code": (
        "- task: Docker@2\n"
        "  displayName: Build and push demo-shipboard\n"
        "  inputs:\n"
        "    command: buildAndPush\n"
        "    repository: demo-shipboard\n"
        "    dockerfile: capstone/Dockerfile\n"
        "    containerRegistry: acr-azure100-lab\n"
        "    tags: |\n"
        "      $(Build.BuildId)\n"
        "# Runtime: Container Apps / App Service containers pull that tag.\n"
        "# AKS optional. Destroy it. Never latest-as-truth."
    ),
    "checklist": [
        "Dockerfile in the same capstone repo",
        "Pipeline builds and pushes to personal ACR with Build.BuildId",
        "Same app URL/contract as Day 91, now from a container",
        "AKS destroyed if you created it; latest is not the promotion story",
        "README diagram includes registry + runtime",
    ],
    "tomorrow": "Capstone 3 — IaC for two environments of the same public demo, then destroy non-prod",
}

SPECS[93] = {
    "topic": "Capstone Project 3 - IaC Multi-env",
    "subtitle": "If a stranger cannot recreate the env from Git, the demo is still a toy",
    "phase": "10 - Portfolio & Public Launch",
    "tables": [
        {
            "title": "Architecture A — infra for the same public demo, two environments",
            "columns": ["Box", "Personal Azure / Git object", "Rule"],
            "rows": [
                ["Module / file", "capstone/infra/ (Bicep or Terraform — same dialect as Phase 5)", "Do not switch languages this week for spice"],
                ["Dev parameters", "dev.bicepparam or terraform/dev.tfvars", "SKU F1 / consumption; short names via uniqueString"],
                ["Staging parameters", "stg.bicepparam or terraform/stg.tfvars", "Same module, different param file — no infra-prod-FINAL folder"],
                ["State / deploy", "Remote state (Day 48) or a pipeline service connection", "Local state is a rumor you cannot share"],
                ["Pipeline", "pipelines/infra.yml or capstone/infra-pipeline.yml", "plan in CI; apply gated by Environment approval"],
                ["App artifact", "Still Day 39: promote the image/zip, do not rebuild in staging", "Infra apply ≠ app rebuild"],
            ],
            "widths": [36, 86, 60],
        },
        {
            "title": "Architecture B — apply, approve, destroy",
            "columns": ["Step", "Default", "Stop when"],
            "rows": [
                ["plan / what-if", "Always in CI; read Modify/Delete", "The diff recreates a disk or a vault you did not expect"],
                ["apply to dev", "Auto after green plan on main (or manual once)", "You are not on the personal subscription"],
                ["apply to staging", "Environment approval — even if the approver is you", "You click-apply from a laptop and skip the pipeline"],
                ["App deploy", "Reuse Day 91/92 artifact against the new outputs", "A second compile 'to be safe'"],
                ["When the screenshot exists", "Destroy non-prod (dev first)", "Souvenir App Service plans"],
            ],
            "widths": [40, 71, 71],
        },
        {
            "title": "Architecture C — toy vs portfolio pitfalls",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Portal-only env", "Works on your screen, cannot be rebuilt", "Everything in capstone/infra/"],
                ["Copied folders", "infra-dev/ and infra-stg/ drifting", "One module, two param files"],
                ["Dialect tourism", "Bicep Monday, Terraform Wednesday", "Stay on the Phase 5 tool"],
                ["Apply without plan", "'It is only a SKU'", "plan/what-if is mandatory manners"],
                ["Non-prod souvenirs", "Two plans still billing on Day 100", "Destroy steps in the README; run them"],
            ],
            "widths": [40, 71, 71],
        },
    ],
    "one_liner": "Infra as code for your demo is the difference between a toy and a portfolio piece.",
    "lab_intro": "Same public demo-shipboard as Days 91–92. Personal subscription. Destroy non-prod when the proof exists. No employer modules.",
    "lab": [
        "Add capstone/infra/ in the same dialect you used in Phase 5 (Bicep or Terraform). One module: RG + the runtime (App Service plan/app or Container Apps env) + ACR if still needed.",
        "Add two parameter files (dev and staging). Different names/SKUs; same module. No copied folder named infra-prod-final-FINAL.",
        "Write pipelines/infra.yml (or capstone/infra-pipeline.yml): plan/what-if on every run; apply gated by an Azure DevOps Environment.",
        "Apply dev from the pipeline. Wire Day 91/92 app deploy to the outputs (hostname, ACR). Confirm /health.",
        "Apply staging only after you read the plan. Promote the same app artifact — do not rebuild.",
        "Put destroy steps in capstone/README.md. Destroy non-prod when the screenshot exists. Do not keep two plans as souvenirs.",
        "A stranger should recreate the env from the repo without you on a screenshare. If not, the README is the bug.",
    ],
    "code_title": "Infra pipeline — plan in CI, apply behind an approval",
    "code": (
        "trigger:\n"
        "  paths:\n"
        "    include: [capstone/infra/**, pipelines/infra.yml]\n"
        "pool:\n"
        "  vmImage: ubuntu-latest\n"
        "stages:\n"
        "- stage: Plan\n"
        "  jobs:\n"
        "  - job: plan\n"
        "    steps:\n"
        "    - script: |\n"
        "        az deployment group what-if -g rg-shipboard-dev \\\n"
        "          -f capstone/infra/main.bicep -p capstone/infra/dev.bicepparam\n"
        "      displayName: what-if dev (or terraform plan -var-file=dev.tfvars)\n"
        "- stage: ApplyDev\n"
        "  dependsOn: Plan\n"
        "  jobs:\n"
        "  - deployment: apply\n"
        "    environment: capstone-dev\n"
        "    strategy:\n"
        "      runOnce:\n"
        "        deploy:\n"
        "          steps:\n"
        "          - script: echo Apply only after you read the what-if/plan\n"
        "            displayName: Gated apply placeholder"
    ),
    "checklist": [
        "capstone/infra/ uses one module and two param files",
        "Pipeline prints plan/what-if; apply is gated",
        "Same app artifact promoted onto the IaC outputs",
        "Non-prod destroy steps are in the README and you ran them (or scheduled tonight)",
        "No employer modules, no dialect switch for spice",
    ],
    "tomorrow": "GitHub portfolio setup — open the blinds with a sanitized README a stranger can follow",
}

SPECS[94] = {
    "topic": "GitHub Portfolio Setup",
    "subtitle": "Pinned repos with vague names are closed blinds",
    "phase": "10 - Portfolio & Public Launch",
    "tables": [
        {
            "title": "Architecture A — shop window for the public demo",
            "columns": ["Pane", "What goes on personal GitHub", "What never ships"],
            "rows": [
                ["Repo", "Sanitized capstone + selected 100-day samples", "Work tenant URLs, internal project names"],
                ["README", "Problem, Architecture, Pipelines, Security, Cost, License", "Empty README or 'test' / 'new-folder'"],
                ["Diagram", "The four/six boxes from Days 91–93", "Employer network diagrams"],
                ["How to run", "Commands you clicked through as a stranger", "Steps that require a secret you did not document as a placeholder"],
                ["Pins", "Capstone first; one or two supporting repos", "Graveyard forks and untitled gists"],
                ["License", "MIT or another license you mean", "Default leftover with no LICENSE"],
            ],
            "widths": [32, 80, 70],
        },
        {
            "title": "Architecture B — sanitize on the way out",
            "columns": ["Item", "Publish", "Strip"],
            "rows": [
                ["Pipeline YAML", "Yes — ubuntu-latest, template calls, artifact names", "Service connection names that leak a tenant"],
                ["Screenshots", "Green run + /health with a fake build id", "Email addresses, coworker faces, work boards"],
                ["Cost notes", "SKU + 'deleted after' — honesty", "Invented savings percentages"],
                ["Secrets", "Placeholder KEY_VAULT_NAME in docs", "Any real secret, PAT, or connection string"],
                ["Commit history", "New repo or rewritten public history", "Accidental .env from an old commit"],
            ],
            "widths": [36, 73, 73],
        },
        {
            "title": "Architecture C — closed-blind failure modes",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Vague pin", "Repos named test, new-folder, final2", "Rename or write a description that works without the name"],
                ["README theater", "Badges, no how-to-run", "Click your own steps once as a stranger"],
                ["Secret in Git", "KV value or PAT in history", "Rotate; purge if needed; treat as Day 97's incident"],
                ["Unsanitized lift", "Internal hostnames in a screenshot", "Crop or retake on the personal app"],
                ["Pin the graveyard", "12 forks, 0 capstone", "Pin what a stranger should open first"],
            ],
            "widths": [36, 73, 73],
        },
    ],
    "one_liner": "GitHub is your shop window — pinned repos with vague names are closed blinds.",
    "lab_intro": "Personal GitHub account, personal time, sanitized capstone only. No employer content, no work tenant names.",
    "lab": [
        "Create or update a personal GitHub repo for the capstone. If history might contain secrets, start a clean public repo and copy sanitized files.",
        "Write README sections: Problem | Architecture | Pipelines | Security | Cost notes | License | How to run.",
        "Grep the tree for passwords, PATs, tenant IDs, and work hostnames. Remove them. Rotate anything that already leaked.",
        "Add screenshots that show /health and a green pipeline with no email, no coworker, no work board.",
        "Click through How to run once as if you were a stranger. If you get stuck, the README is wrong — fix it.",
        "Pin the capstone on your personal GitHub profile. Unpin vague test repos or give them descriptions.",
        "Cost note: SKUs used and what you already destroyed. No invented savings.",
    ],
    "code_title": "README skeleton — the demo when you are not in the room",
    "code": (
        "# demo-shipboard\n"
        "\n"
        "## Problem\n"
        "Public Azure DevOps CI/CD demo: one service, /health, env promotion.\n"
        "\n"
        "## Architecture\n"
        "Repo → Pipeline (ubuntu-latest) → Artifact/image $(Build.BuildId) → App Service or Container Apps\n"
        "\n"
        "## Pipelines\n"
        "See azure-pipelines.yml and pipelines/infra.yml. Promote the same artifact.\n"
        "\n"
        "## Security\n"
        "No secrets in Git. Key Vault name is a placeholder. Service connections stay in Azure DevOps.\n"
        "\n"
        "## Cost notes\n"
        "F1 / Basic ACR / deleted after screenshots. No invented savings.\n"
        "\n"
        "## License\n"
        "MIT"
    ),
    "checklist": [
        "Sanitized capstone is on personal GitHub",
        "README has Problem, Architecture, Pipelines, Security, Cost, License, How to run",
        "You followed How to run once as a stranger",
        "No secrets, no employer screenshots",
        "Capstone is pinned; vague repos are unpinned or described",
    ],
    "tomorrow": "Personal site or blog — translate the YAML into a story a non-terminal human can trust",
}

SPECS[95] = {
    "topic": "Personal Site / Blog for Case Studies",
    "subtitle": "Translate YAML into a story a non-terminal human can trust",
    "phase": "10 - Portfolio & Public Launch",
    "tables": [
        {
            "title": "Architecture A — one public write-up, one repo",
            "columns": ["Layer", "Job", "Keep it personal"],
            "rows": [
                ["Title", "How I built a small Azure DevOps CI/CD demo in public", "Not a cert you do not have; not a client you do not have"],
                ["Story", "Problem, approach, what you would do differently", "Not 400 lines of YAML pasted into HTML"],
                ["Evidence", "Link the GitHub repo + 1–2 screenshots", "YAML stays in Git"],
                ["Host", "GitHub Pages or one Dev.to article", "Two platforms with half a draft is not a case study"],
                ["Audience", "A human who may never open azure-pipelines.yml first", "Not a prospecting list"],
            ],
            "widths": [32, 80, 70],
        },
        {
            "title": "Architecture B — Pages vs a post",
            "columns": ["Constraint", "Default", "Skip"],
            "rows": [
                ["Want a URL you control", "GitHub Pages from the capstone docs/ or a /site folder", "A custom domain you will not renew"],
                ["Want distribution", "One Dev.to (or equivalent) article linking the repo", "Cross-posting three half-edits"],
                ["No time for a theme", "A single markdown page is enough", "A blog engine rewrite on Day 95"],
                ["Employer case itching", "Do not write it", "Internal diagrams, 'at my company we…'"],
                ["Traffic theater", "Do not invent readers or customers", "Fake '10k users' on a hello /health"],
            ],
            "widths": [42, 76, 64],
        },
        {
            "title": "Architecture C — trust-breaking pitfalls",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["YAML dump", "Readers bounce; no story", "Prose first; link the file"],
                ["Employer leak", "Workplace identifiable detail", "Delete; rewrite as the public demo only"],
                ["Cert flex unpaid", "'AZ-400 certified' before it is true", "Day 96 is review, not a credential"],
                ["Half two sites", "Pages stub + Dev.to stub", "Finish one"],
                ["Theater metrics", "Invented traffic or 'clients'", "Describe labs you actually ran"],
            ],
            "widths": [36, 73, 73],
        },
    ],
    "one_liner": "A case study translates YAML into a story a non-terminal human can trust.",
    "lab_intro": "Personal GitHub Pages or a personal Dev.to (or similar) article. Capstone demo only. No employer content.",
    "lab": [
        "Draft the case study in capstone/docs/case-study.md (or /site): Problem, approach, brakes on the pipeline, image tag, Key Vault, what you would change.",
        "Title it about the public CI/CD demo — not a client case and not a certification you have not earned.",
        "Link the GitHub repo. Paste at most a short YAML fragment; the rest stays in Git.",
        "Publish via GitHub Pages (Settings → Pages) or one Dev.to article. If the host is not live today, the draft must be complete enough to paste tomorrow.",
        "Read the piece once as if you do not know YAML. If a step is missing, add it.",
        "Strip any workplace detail. This series stays a classroom, not a case-study of an employer.",
    ],
    "code_title": "Article outline — story then evidence",
    "code": (
        "# How I built a small Azure DevOps CI/CD demo in public\n"
        "\n"
        "1. Problem: I wanted a demo I can walk in five minutes.\n"
        "2. Approach: one service, tests, artifact, env promotion, then a container + IaC.\n"
        "3. Brakes: approvals, Key Vault, pin Build.BuildId, destroy non-prod.\n"
        "4. Evidence: https://github.com/<you>/demo-shipboard\n"
        "5. What I would do differently next time.\n"
        "# Host: GitHub Pages or one Dev.to post. YAML stays in Git."
    ),
    "checklist": [
        "One complete write-up that links the repo",
        "No employer content, no fake traffic, no unearned cert claim",
        "Published or ready-to-paste tomorrow",
        "YAML is evidence, not the article body",
        "Posted the LinkedIn document",
    ],
    "tomorrow": "AZ-400 review — map these 100 days to the skills outline and write a gap list, not a hero cram",
}

SPECS[96] = {
    "topic": "AZ-400 Certification Review",
    "subtitle": "The labs are the study guide you already wrote — the outline names the missing chapters",
    "phase": "10 - Portfolio & Public Launch",
    "tables": [
        {
            "title": "Architecture A — map 100 days to exam-shaped buckets",
            "columns": ["Outline bucket (typical)", "You already practiced", "Often a gap"],
            "rows": [
                ["Design a DevOps strategy", "Days 4–10, 81, 89 — boards, repos, paved road", "Org-scale governance you only sketched"],
                ["CI / YAML / agents", "Days 21–34, 82 — ubuntu-latest, templates", "Self-hosted scale sets if you stayed hosted"],
                ["Release / CD / gates", "Days 35–42, 91 — artifacts, envs, approvals", "Canary / ring depth you only read"],
                ["IaC + config", "Days 43–50, 93 — Bicep or Terraform", "The dialect you did not pick"],
                ["Secure / Key Vault / Policy", "Phase 7, Days 19, 83", "Microsoft Defender depth, Test Plans depth"],
                ["Feedback / Monitor", "Days 71–80 — Insights, alerts, analytics", "KQL you skipped; Application Insights sampling"],
            ],
            "widths": [48, 67, 67],
        },
        {
            "title": "Architecture B — tick practiced vs schedule a gap",
            "columns": ["Evidence", "Tick practiced", "Weekend list"],
            "rows": [
                ["You deployed a slot / env approval", "CD gates", "Canary math you never ran"],
                ["You ran plan/what-if", "IaC", "The dialect you did not pick"],
                ["You only read the doc", "Do not tick it", "That row on the outline"],
                ["You never opened Test Plans", "Do not tick it", "A short Learn module, not shame"],
                ["Tonight's urge to binge 6 hours", "Mapping only", "A weekend list with a few bullets"],
            ],
            "widths": [50, 50, 82],
        },
        {
            "title": "Architecture C — review pitfalls",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Fake credential", "Bio says AZ-400 before the exam", "Review is review"],
                ["Dump of dumps", "Random PDFs, no outline", "Official skills list first"],
                ["Tick unread rows", "A green checklist you cannot speak", "Labs beat flashcards; mark skimmed vs never"],
                ["Schedule exam in the post", "Pressure theater", "This handout does not book a Pearson slot"],
                ["Invent a score", "'I would get 85%'", "No score without an exam"],
            ],
            "widths": [40, 71, 71],
        },
    ],
    "one_liner": "AZ-400 rewards people who built things — your labs are the study guide you already wrote.",
    "lab_intro": "Personal study notes in azure-100-labs. Official Microsoft Learn outline only. No fake pass, no exam booking required today.",
    "lab": [
        "Open the official AZ-400 skills outline on Microsoft Learn (exams/az-400). Save the link in docs/az400-gaps-day96.md.",
        "Tick each objective: practiced in these 100 days / skimmed / never. Honesty is the lab.",
        "Write a weekend study list of the never/skimmed rows only — a few bullets, not the whole outline.",
        "For three practiced rows, write the lab artifact that proves it (pipeline file, Insights alert, infra plan).",
        "Do not write AZ-400 certified on a profile. Do not invent a score. Do not cram the whole outline tonight.",
        "Optional: add the outline PDF or a screenshot of the contents table — not a brain-dump site.",
    ],
    "code_title": "Gap file — outline first, binge never",
    "code": (
        "# docs/az400-gaps-day96.md\n"
        "# Outline: https://learn.microsoft.com/credentials/certifications/exams/az-400/\n"
        "# Practiced:\n"
        "#   - YAML CI / templates          → templates/build.yml, Day 82/90\n"
        "#   - Env promotion + approvals    → capstone pipeline, Day 91\n"
        "#   - Key Vault / no secrets in Git → Phase 7 + capstone README\n"
        "#   - Monitor + alert              → Day 80 forced fail\n"
        "# Gaps (weekend list, not tonight):\n"
        "#   - <paste 3–7 outline rows you never touched>\n"
        "# Review is review. No fake credential."
    ),
    "checklist": [
        "Official outline opened and linked",
        "Practiced vs skimmed vs never ticked honestly",
        "Weekend gap list written; no 6-hour hero binge claimed",
        "No unearned AZ-400 title, no invented score",
        "docs/az400-gaps-day96.md on the personal repo",
    ],
    "tomorrow": "Mock interview prep — say five answers out loud, including the failure path",
}

SPECS[97] = {
    "topic": "Mock Interview Prep",
    "subtitle": "Rehearse the happy path and the failure path — interviews are pipelines too",
    "phase": "10 - Portfolio & Public Launch",
    "tables": [
        {
            "title": "Architecture A — five questions as a career pipeline",
            "columns": ["Question", "Happy path (say this)", "Failure path (also say this)"],
            "rows": [
                ["Promote the same artifact across envs?", "One CI build; Environments download that artifact/digest", "If you rebuild in prod, go back to Day 39"],
                ["Secret landed in a PR?", "Rotate, treat the PR as an incident, rewrite history if needed", "'Delete the line and merge' leaves the secret in Git"],
                ["Pipeline red Friday 17:00?", "Who is affected, revert vs fix-forward with a clock", "YOLO to prod to paint the dashboard green"],
                ["Branching for this repo?", "Trunk + PRs + path filters (your ADR)", "A branching novel you cannot draw"],
                ["Rollback after a bad deploy?", "Redeploy last Build.BuildId / swap slot", "Hotfix on main with no last-good"],
            ],
            "widths": [50, 66, 66],
        },
        {
            "title": "Architecture B — how to answer 'I do not know'",
            "columns": ["Urge", "Do", "Do not"],
            "rows": [
                ["Blank on a tool", "'I would open X and verify Y'", "Invent a confident wrong"],
                ["DORA metrics", "Define the four; say you did not measure a team's numbers", "Invent a lead-time percentage"],
                ["Work story itching", "Use the public demo-shipboard", "Identify an employer or a client"],
                ["Rambling", "Stop; four bullets; say it again", "A 8-minute tour of your whole career"],
                ["Recording dread", "Record once; listen once", "Skip the recording and only type answers"],
            ],
            "widths": [36, 73, 73],
        },
        {
            "title": "Architecture C — interview failure modes you can rehearse",
            "columns": ["Pitfall", "What you hear yourself say", "Fix"],
            "rows": [
                ["Rebuild in prod", "'We compile again to be safe'", "Same artifact; say Build.BuildId"],
                ["Secret shrug", "'Just revert the file'", "Rotate + history"],
                ["Friday hero", "'I would patch live'", "Clock, blast radius, revert"],
                ["Fake DORA", "'Our MTTR is 4 minutes'", "Define metrics; no invented team numbers"],
                ["Typed only", "Perfect markdown, frozen voice", "Out loud is the lab"],
            ],
            "widths": [32, 75, 75],
        },
    ],
    "one_liner": "Interviews are pipelines for your career — rehearse the happy path and the failure path.",
    "lab_intro": "Personal time. Record on your own device. Use the public capstone as the example — no employer stories that identify a workplace.",
    "lab": [
        "Write the five questions in docs/mock-interview-day97.md with 4-bullet answers: artifact promotion, secret in a PR, Friday red pipeline, branching, rollback.",
        "Add DORA: name the four metrics in one sentence each. Do not invent numbers you never measured.",
        "Answer all five out loud. Record yourself once (phone voice memo is enough).",
        "Listen once. If you ramble, tighten the bullets and say the weak answer again.",
        "For any 'I do not know', write where you would look and what you would verify.",
        "Do not include workplace-identifying stories. The capstone is the exhibit.",
    ],
    "code_title": "Prompt card — say it, then listen once",
    "code": (
        "# Q1: How do you promote the same artifact across envs?\n"
        "# Q2: A secret appeared in a PR — what do you do?\n"
        "# Q3: Pipeline red on Friday 17:00 — what is the playbook?\n"
        "# Q4: What branching strategy does this repo use and why?\n"
        "# Q5: How do you roll back a bad deploy without a hero hotfix?\n"
        "# DORA: deployment frequency, lead time, CFR, MTTR — define, do not invent."
    ),
    "checklist": [
        "Five answers written as 4-bullet cards",
        "Recorded and listened once",
        "Happy path and failure path both spoken",
        "No invented DORA numbers, no employer-identifying story",
        "docs/mock-interview-day97.md on the personal repo",
    ],
    "tomorrow": "Professional profile setup — policy first, volume second",
}

SPECS[98] = {
    "topic": "Professional Profile Setup",
    "subtitle": "Profiles are loud — read the contract before you hit publish",
    "phase": "10 - Portfolio & Public Launch",
    "tables": [
        {
            "title": "Architecture A — two volume levels (portfolio vs paid profile)",
            "columns": ["Surface", "Volume", "Today's default"],
            "rows": [
                ["GitHub + case study (Days 94–95)", "Quiet proof", "Already public if you sanitized"],
                ["LinkedIn learning posts", "Classroom volume", "This series — educational, no hire-me CTA"],
                ["Paid-work marketplace profile", "Loud — implies you are for hire", "Draft offline; activate only if policy allows"],
                ["Personal site contact form", "Medium", "Optional; still not a sales page in this series"],
                ["Work laptop / work tenant", "Forbidden volume", "Personal equipment, personal time, personal Azure"],
            ],
            "widths": [56, 50, 76],
        },
        {
            "title": "Architecture B — policy before profile",
            "columns": ["Check", "If allowed", "If not allowed"],
            "rows": [
                ["Moonlighting / IP clause read", "Draft the profile in a local file", "Leave it as a local draft; GitHub still exists"],
                ["Equipment / time", "Personal PC, personal hours", "Do not build the profile on a work laptop"],
                ["What you sell (later)", "Skills you can demo from the capstone", "Anyone's customers, any employer account list"],
                ["Platforms (Toptal / Braintrust / Upwork, etc.)", "Create only after the clause is clear", "Browsing a marketing page is not a profile"],
                ["Portfolio links", "GitHub + case study are enough to wait", "A loud profile without proof"],
            ],
            "widths": [56, 63, 63],
        },
        {
            "title": "Architecture C — loud mistakes",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Publish then read policy", "A live paid profile and a contract problem", "Policy first; activate second"],
                ["Work tenant targeting", "You almost list employer customers", "Never. This series is not a prospecting list"],
                ["Work equipment", "Draft on a corporate laptop", "Personal device only"],
                ["Empty loud profile", "Marketplace live, README still 'TODO'", "Days 94–95 first"],
                ["This post as a hire-me ad", "CTA, calendar link, brand sell", "Educational reminder only"],
            ],
            "widths": [40, 71, 71],
        },
    ],
    "one_liner": "Profiles are loud — make sure your contract allows the volume before you hit publish.",
    "lab_intro": "Personal time and personal equipment. Read your own agreement. This handout is not a marketplace tour and not an invitation to hire anyone.",
    "lab": [
        "Read your employer moonlighting and IP policy (if you have an employer). If you are independent, write that fact in the notes. Do this before any paid profile.",
        "Create docs/profile-draft-day98.md offline: headline, three bullets tied to the public capstone, links to GitHub and the case study.",
        "Checklist in that file: policy reviewed, portfolio links ready, personal equipment only, no customer targeting.",
        "Do not activate a paid marketplace profile today unless the policy clearly allows it. A local draft is the lab.",
        "If policy says no, the draft stays a draft. GitHub and the case study remain the quiet proof.",
        "Do not use a work laptop, work tenant, or work time. Do not target any employer's customers.",
    ],
    "code_title": "Offline draft checklist — volume is a choice",
    "code": (
        "# docs/profile-draft-day98.md\n"
        "# [ ] Moonlighting / IP policy read (or N/A: independent)\n"
        "# [ ] Personal equipment / personal time\n"
        "# [ ] Portfolio links: GitHub capstone + Day 95 write-up\n"
        "# [ ] No customer targeting, no workplace leak\n"
        "# [ ] Paid profile NOT live unless policy allows\n"
        "# Headline draft: Azure DevOps CI/CD — public demo-shipboard walkthrough\n"
        "# Activate later. Loud is not the same as allowed."
    ),
    "checklist": [
        "Policy read (or independent noted) before any paid profile",
        "Offline draft exists with portfolio links",
        "No work laptop, no customer targeting",
        "Paid profile still off unless clearly allowed",
        "This post has no hire-me CTA",
    ],
    "tomorrow": "Outreach and pricing as a thinking exercise — boundaries, not a sales PDF",
}

SPECS[99] = {
    "topic": "Outreach Templates & Pricing",
    "subtitle": "Pricing is a boundary you write privately — this series stays a classroom",
    "phase": "10 - Portfolio & Public Launch",
    "tables": [
        {
            "title": "Architecture A — communication vs selling (this series is the former)",
            "columns": ["Move", "Educational use", "Out of scope here"],
            "rows": [
                ["Public walkthrough link", "Share demo-shipboard + the case study", "A product SKU, a 'health check' package, a brand offer"],
                ["DM template", "Offer to answer questions about a public article", "Cold 'hire me' + calendar spam"],
                ["Rate band", "Private note: what an hour of your time is worth to you", "A published price card on LinkedIn"],
                ["Who you write to", "People already asking about Azure Pipelines (rare, specific)", "Mass DMs on every hiring post"],
                ["Proof", "The repo a stranger can clone", "A rate without a public artifact"],
            ],
            "widths": [40, 78, 64],
        },
        {
            "title": "Architecture B — a thinking exercise for independent engineers",
            "columns": ["Question (private)", "Undercharging buys", "Overcharging without proof buys"],
            "rows": [
                ["What would I charge myself to redo this capstone?", "Stress and resentful yeses", "Silence — no one replies"],
                ["What evidence exists today?", "A low number with only a hello pipeline", "A high number with no README"],
                ["Hour vs outcome?", "Endless unpaid Slack", "A fixed fee you cannot scope"],
                ["Do I even want paid work?", "A rate you write and never use", "A profile that violates Day 98 policy"],
                ["Will I publish the number?", "No — the band stays in a private file", "A fake day rate to look senior"],
            ],
            "widths": [56, 63, 63],
        },
        {
            "title": "Architecture C — pitfalls that turn a classroom into a storefront",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Spam tax", "Fifty identical DMs", "Two templates, used rarely or never"],
                ["Hire-me on the lesson post", "Calendar link under a Day 99 PDF", "This series has no sales CTA"],
                ["Packaged 'assessment' sell", "A branded checkup offer on the handout", "Do not. Learning content only"],
                ["Invented market rate", "A number copied from a tweet", "Private band + your actual proof"],
                ["Prospecting a workplace", "DMs aimed at an employer's customers", "Never. Independent thinking exercise only"],
            ],
            "widths": [44, 69, 69],
        },
    ],
    "one_liner": "Pricing is a boundary — undercharging buys stress, overcharging without proof buys silence.",
    "lab_intro": "Educational thinking exercise for independent engineers. Personal notes only. No sales PDF, no packaged offer, no outreach blast from this lesson.",
    "lab": [
        "Write two DM templates in a private file (docs/outreach-draft-day99.md, keep the repo private or omit this file from the public GitHub copy).",
        "Template vibe: you published a public CI/CD walkthrough; here is the link; happy to answer questions. No 'hire me', no calendar, no packaged assessment.",
        "Write a private rate band as a thinking exercise: a floor that does not buy you stress, a ceiling you could defend with the capstone. Do not publish the numbers.",
        "Note whether Day 98 policy even allows paid work. If no, the templates stay unused — that is a complete lab.",
        "Do not drop the DMs on today's LinkedIn post. Do not mass-message hiring threads.",
        "Do not invent a day rate to look senior. Do not attach a service menu to this series.",
    ],
    "code_title": "Template vibe — help first; numbers stay private",
    "code": (
        "# Private draft only — do not paste rates on LinkedIn.\n"
        "# DM A: \"Saw you are hiring for Azure Pipelines. I published a public\n"
        "# CI/CD walkthrough here: <github-or-case-study>. Happy to answer questions.\"\n"
        "# DM B: \"Wrote up how I promote one artifact across two personal Azure envs:\n"
        "# <link>. If useful, the repo has the YAML.\"\n"
        "# Rate band: <floor>–<ceiling> in a file that is NOT in the public repo.\n"
        "# This series is a classroom. No service menu. No packaged checkup offer."
    ),
    "checklist": [
        "Two help-first DM templates written privately",
        "Private rate band written and not published",
        "No hire-me CTA, no packaged offer, no mass DM",
        "Policy from Day 98 still respected",
        "This handout stays educational",
    ],
    "tomorrow": "Launch day — pin the proof, destroy leftovers, write the next 100 days",
}

SPECS[100] = {
    "topic": "Launch Day + Next 100 Days",
    "subtitle": "The first public proof you can ship learning on purpose — then schedule the next slice",
    "phase": "10 - Portfolio & Public Launch",
    "tables": [
        {
            "title": "Architecture A — launch is a last-mile checklist, not a vibe",
            "columns": ["Piece", "Live today", "Still homework"],
            "rows": [
                ["Capstone README", "Stranger can follow How to run", "TODO badges and a missing diagram"],
                ["Pins", "Personal GitHub pins the sanitized demo", "test / new-folder still in the window"],
                ["Case study", "Pages or Dev.to link works", "Draft only in a local folder"],
                ["LinkedIn recap", "Day 100 document, personal account", "Workplace detail in the celebration"],
                ["Azure leftovers", "Destroyed or budget-alerted", "Forgotten AKS / ACR / App Service plans"],
                ["Next cycle", "docs/next-100.md with five goals", "Goals only in your head"],
            ],
            "widths": [36, 73, 73],
        },
        {
            "title": "Architecture B — five next-100 goals (pick, do not collect all)",
            "columns": ["Goal type", "Example (policy permitting)", "Not a goal"],
            "rows": [
                ["Certification study", "Weekend list from Day 96, then a real exam date later", "'AZ-400 certified' written today"],
                ["Depth", "AKS or GitOps on a personal cluster you will destroy", "A second 12-service rewrite"],
                ["Capstone hardening", "Add one brake: tracing, slot swap, or better tests", "Payments and ML"],
                ["Writing", "Four more public labs, same classroom rules", "A storefront, a packaged offer"],
                ["Paid work (optional)", "Only if Day 98 policy allows", "Targeting an employer's customers"],
            ],
            "widths": [40, 82, 60],
        },
        {
            "title": "Architecture C — finish-line pitfalls",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Half README", "Pinned repo, closed blinds", "Finish How to run, then pin"],
                ["Leftover bill", "Lab SKUs survive the parade", "az group list; delete or budget"],
                ["Employer leak in the recap", "Workplace story in Day 100", "Celebrate the public labs only"],
                ["Streak, not a practice", "No next-100 file", "Five goals in markdown"],
                ["Storefront turn", "Sales CTA on the victory post", "Classroom to the last sentence"],
            ],
            "widths": [44, 69, 69],
        },
    ],
    "one_liner": "Day 100 is not the finish line — it is the first public proof you can ship learning on purpose.",
    "lab_intro": "Personal GitHub, personal Azure, personal LinkedIn. Celebrate without leaking workplace detail. Destroy what still bills.",
    "lab": [
        "Pin sanitized repos on personal GitHub. Open the capstone as a stranger; fix How to run if it fails.",
        "Publish the Day 100 LinkedIn recap from your personal account. No employer names, no client stories, no sales CTA.",
        "Write five goals in docs/next-100.md (cert study, deeper AKS, tougher capstone slice, more public labs, optional paid work only if policy allows).",
        "az account show (personal sub) then az group list -o table. Delete leftover lab RGs or confirm a budget alert is on.",
        "Confirm Cost Management budget + Day 77 habit still hold. A launch that keeps billing is a trap you set for yourself.",
        "Tick the launch checklist in that file: portfolio live, README polished, recap live, resources destroyed or budgets set, next plan written.",
        "Then stop. Go outside. Finish lines are for races; this was a practice.",
    ],
    "code_title": "Day 100 checklist — proof, cleanup, next slice",
    "code": (
        "# docs/next-100.md\n"
        "# [ ] Portfolio live (pinned capstone + case study URL)\n"
        "# [ ] Capstone README polished (How to run works as a stranger)\n"
        "# [ ] LinkedIn Day 100 recap live (personal account, no workplace leak)\n"
        "# [ ] Leftover RGs destroyed or budgets set\n"
        "# [ ] Five next-100 goals written (policy permitting)\n"
        "az account show --query \"{name:name,id:id}\" -o table\n"
        "az group list -o table\n"
        "# Delete what you do not need. Then go outside."
    ),
    "checklist": [
        "Capstone pinned and README works as a stranger",
        "Day 100 recap posted with no employer leak and no sales CTA",
        "docs/next-100.md has five goals",
        "Personal subscription leftovers destroyed or budget-alerted",
        "You treated this as a practice, not a storefront",
    ],
    "tomorrow": "Keep going — the next 100 days are a file you already wrote, not a vibe",
}
