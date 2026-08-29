# Day 9 — Azure Artifacts

| | |
|---|---|
| **Date** | 29 Aug 2026 |
| **Phase** | 1 — Azure & DevOps Foundations |
| **Time box** | 60–90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Create a project-scoped Azure Artifacts feed with upstream sources enabled, understand feed views (@local, @prerelease, @release), and connect client tooling (npm / NuGet). Publish Day 9 on LinkedIn with the PDF handout.

## Learn (20–30 min)

- What Azure Artifacts solves: private package feeds vs shared folders or public registries
- Supported package ecosystems: NuGet, npm, Maven, Python (pip/twine), Universal Packages
- Upstream sources: caching public dependencies locally for build reliability and security
- Feed views (@local, @prerelease, @release) for promotion quality gates
- Docs: [Azure Artifacts overview](https://learn.microsoft.com/azure/devops/artifacts/start-using-azure-artifacts)

## Hands-on lab (20–30 min)

1. In `azure-100-labs`, navigate to **Artifacts**
2. Click **Create Feed**:
   - Name: `day09-packages`
   - Visibility: **Members of <your-org>** or **Project: azure-100-labs** (project-scoped recommended)
   - Upstream sources: check **Include packages from common public sources** (nuget.org, npmjs)
3. Inspect **Feed Settings**:
   - View default upstream sources (nuget.org, npmjs.org)
   - Check default **Views**: `@local`, `@prerelease`, `@release`
4. Click **Connect to feed** → choose **npm** or **NuGet** → review `.npmrc` / `nuget.config` snippet
5. Save feed URL in your notes for Phase 3 CI/CD pipelines

## Commands / code

```bash
# Example .npmrc configuration for Azure Artifacts:
# registry=https://pkgs.dev.azure.com/<your-org>/azure-100-labs/_packaging/day09-packages/npm/registry/
# always-auth=true

# Example nuget.config configuration:
# <?xml version="1.0" encoding="utf-8"?>
# <configuration>
#   <packageSources>
#     <clear />
#     <add key="day09-packages" value="https://pkgs.dev.azure.com/<your-org>/azure-100-labs/_packaging/day09-packages/nuget/v3/index.json" />
#   </packageSources>
# </configuration>

# Authenticate via CLI tools:
# npx vsts-npm-auth -config .npmrc
```

## LinkedIn post (copy-paste)

**Important:** After pasting into LinkedIn, press Enter between sections so line breaks stay visible.

```
Day 9 of #100DaysOfAzureDevOps

Copying DLLs over Slack is not dependency management.
It is a ticking time bomb.

Yesterday we tackled Azure Test Plans.
Today: how do you share internal libraries and protect your builds from registry outages?

Azure Artifacts.

In modern software delivery, your code is 10% your own logic and 90% dependencies.
If npmjs or nuget.org has a blip or unpublishes a package, your entire pipeline halts.

Azure Artifacts solves three critical problems:

1. Private Package Feeds
Host internal NuGet, npm, Maven, Python, and Universal packages securely inside your Azure DevOps org with fine-grained access.

2. Upstream Sources & Caching
When your build requests a public package, Azure Artifacts fetches and saves a cached copy in your feed. If the public registry goes down, your builds keep succeeding.

3. Feed Views (@local, @prerelease, @release)
Promote packages across quality gates without rebuilding binaries or changing package version numbers.

Lab today in azure-100-labs:
Created a project-scoped feed 'day09-packages', enabled upstream sources for public registries, configured feed views, and generated client connection profiles.

One-liner:
Pipelines cook the software; Artifacts is the pantry.
Without a managed feed, you re-buy public flour on every build.

Tomorrow: Day 10 — Phase 1 Capstone Mini Project & Recap!

(Document attached: Day 9 Azure Artifacts handout PDF)

Lab notes + PDF also here:
https://bit.ly/4xDxqIc

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### Attach with the post (PDF handout)

Attach this document on LinkedIn (document / PDF upload):

- [`../days/day-09-azure-artifacts/handout.pdf`](../days/day-09-azure-artifacts/handout.pdf)

### How to post

1. LinkedIn → **document** → upload `days/day-09-azure-artifacts/handout.pdf`
2. Paste the text above (press **Enter** between sections so line breaks stay visible)
3. **Document title:** `Day 9 — Azure Artifacts Basics` (max 58 chars on LinkedIn)

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5–10 real comments on other Azure/DevOps posts.

## Done checklist

- [ ] Learned private feeds, upstream sources, and feed views
- [ ] Created `day09-packages` feed in `azure-100-labs`
- [ ] Enabled upstream sources (nuget.org, npmjs)
- [ ] Inspected `.npmrc` / `nuget.config` connection setup
- [ ] Published LinkedIn post with PDF handout
- [ ] Engaged with 5–10 community comments

## Tomorrow

**Day 10 — Phase 1 Mini Project & Recap**

---

*Personal learning guide — views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
