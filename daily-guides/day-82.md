# Day 82 - Pipeline Templates & Reusable YAML

| | |
|---|---|
| **Date** | 10 Nov 2026 |
| **Phase** | 9 - Advanced & Enterprise |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- templates, extends, parameters

## Hands-on lab (20-30 min)

1. Extract a `templates/build.yml` and reuse from main pipeline

## Commands / code

```bash
# templates/build.yml
parameters:
- name: projectPath
  type: string
steps:
- script: echo Building ${{ parameters.projectPath }}
```

## LinkedIn post (copy-paste)

```
Copy-paste YAML is how organizations invent 14 slightly different ways to be broken.

Day 82 of #100DaysOfAzureDevOps. Pipeline templates and reusable YAML.

templates, extends, parameters. I have counted fourteen "standard" build pipelines that all forgot the same cache key. Copy-paste is a bug-spreading strategy. A template with projectPath is one place to fix the ritual.

Extract templates/build.yml. Reuse it from the main pipeline. parameters.projectPath. The first template can echo. The point is the call site, not a novel of abstractions on day one.

What I keep seeing

1. parameters are the contract
• projectPath: string
• A template with secret defaults nobody sees is a trap

2. Reuse from main
• steps: - template: templates/build.yml
• Two consumers tomorrow in the Phase 9 recap; one caller today is the seed

3. extends is the bigger hammer
• Literacy: a pipeline can extend a template that owns stages
• Lab: a step template is enough to feel the win

4. Fix once
• When Node 20 becomes Node 22, I want one file to change
• Fourteen files is how one team stays on 18 until an incident

What I am doing in today's lab

I am extracting templates/build.yml with a projectPath parameter and calling it from the main pipeline. echo Building the parameter is legal for the first cut. If I still have duplicated restore/build steps after this, I did not extract. I rearranged. The call site should look boring: one template line, one path.

One broken template is cheaper than fourteen unique snowflakes. Reuse is a reliability feature.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-82-pipeline-templates-reusable-yaml

Tomorrow: Marketplace extensions — spices, not a handful in the stew.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 82 — Pipeline Templates & YAML` (max 58 chars)
3. Paste the text above (press **Enter** between sections so line breaks stay)

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5-10 real comments on other Azure/DevOps posts.

## Reminder — 2nd LinkedIn post (production track)

**Today you publish TWO separate LinkedIn posts.** The daily lesson above is post 1 only.

| | Post 1 — #100DaysOfAzureDevOps | Post 2 — #ProductionGradeAzure |
|---|-------------------------------|----------------------------------|
| **When** | ~10:00 IST | ~17:00–19:00 IST (after some engagement on post 1) |
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 27 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 27 of 33 (rewrite with your real experience)
- [ ] Record URLs in [`publish/production-grade/LINKS.md`](../publish/production-grade/LINKS.md)

Run: `python scripts/production_reminder.py`

## Done checklist

- [ ] Learned the topic (docs or short video)
- [ ] Completed the lab steps
- [ ] Ran / saved the commands or code
- [ ] Published LinkedIn post
- [ ] Engaged with 5-10 community comments
- [ ] Deleted spare Azure resources if any (cost control)

## Tomorrow

**Extensions & marketplace**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
