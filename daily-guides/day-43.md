# Day 43 - ARM Parameters & Outputs

| | |
|---|---|
| **Date** | 02 Oct 2026 |
| **Phase** | 5 - Infrastructure as Code |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Parameter files, variables, nested templates

## Hands-on lab (20-30 min)

1. Add parameters file; output storage endpoint
2. Skim only if you chose Terraform as primary

## Commands / code

```bash
az deployment group create -g rg-day43 -f main.json -p @main.parameters.json
```

## LinkedIn post (copy-paste)

```
Parameters are the dials; hardcoding names is how labs become landfills.

Day 43 of #100DaysOfAzureDevOps. ARM parameters and outputs.

A template with names baked in is a souvenir from one resource group. The second environment copies the file, forgets a string, and you have stprodprod in East US because someone concatenated in a panic. Parameters are the dials. Outputs are how the next stack finds the endpoint without spelunking the Portal.

If Terraform is my primary, I still skim this. Nested templates exist; I am not building a matryoshka today. Parameter file plus an output for the storage endpoint is the lab.

Patterns I keep seeing

1. Parameter files are environment knobs
• main.parameters.json (or per-env files) instead of edited copies of main.json
• az deployment group create ... -p @main.parameters.json

2. Hardcoded names collide
• Storage account names are globally unique
• A landfill of failed deployments is often a name that already existed

3. Outputs are the handshake
• Emit the blob endpoint or resource ID
• The next pipeline step should not grep the Portal

4. Nested templates are power tools
• Literacy: they exist
• Today: one file, parameters, outputs — enough

What I am doing in today's lab

I am adding a parameters file, outputting the storage endpoint, deploying with -p @main.parameters.json, and if Terraform is my primary I am keeping this to a skim plus one successful parameterized deploy. Then I delete what I created.

Dials belong in parameter files. Names that cannot change belong in uniqueString, not in my pride.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-43-arm-parameters-outputs

Tomorrow: Bicep fundamentals — same control plane, less JSON horror.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 43 — ARM Parameters & Outputs` (max 58 chars)
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
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 14 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 14 of 33 (rewrite with your real experience)
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

**Bicep fundamentals**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
