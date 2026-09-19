# Day 49 - IaC in Pipelines

| | |
|---|---|
| **Date** | 08 Oct 2026 |
| **Phase** | 5 - Infrastructure as Code |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Plan in CI, apply with approval

## Hands-on lab (20-30 min)

1. Pipeline: terraform plan -> publish plan -> apply on approval

## Commands / code

```bash
- script: terraform plan -out=tfplan
- script: terraform apply -auto-approve tfplan
  condition: and(succeeded(), eq(variables['apply'], 'true'))
```

## LinkedIn post (copy-paste)

```
IaC without a pipeline is homework; IaC in a pipeline is how grown-ups change prod.

Day 49 of #100DaysOfAzureDevOps. IaC in pipelines.

A plan on a laptop is a school assignment. A plan in CI, published as an artifact, applied only when an approval says so, is how you stop "it worked on my Terraform." I have watched production apply from a developer workstation because the pipeline "wasn't ready." The workstation had a different variable file. Of course it did.

Pipeline: terraform plan -out=tfplan (or bicep what-if). Publish the plan. Apply with a condition — eq(variables['apply'], 'true') or an environment approval. Not both auto-approve and hope.

Patterns I keep seeing

1. Plan in CI on a clean agent
• The agent checks out the same commit a human reviewed
• Laptop plans pick up leftover env vars like lint

2. Apply is gated
• condition: and(succeeded(), eq(variables['apply'], 'true'))
• Or a prod environment approval from Day 38
• Auto-approve in a lab destroy is fine; auto-approve prod is a personality disorder

3. The plan file is the artifact
• Apply the plan you reviewed, not a fresh plan nobody saw
• A second plan at apply time is how surprises sneak in

4. Identity of the pipeline is scoped
• The service connection should not be Owner on the subscription
• IaC robots with flamethrowers write very complete incidents

What I am doing in today's lab

I am adding a pipeline that runs terraform plan -out=tfplan (or Bicep what-if), publishes the plan, and applies only when apply=true or an approval lands. I will run it once without apply, once with. If the second run changes something the first plan did not show, I stop and read.

Homework stays on the laptop. Production changes wait in a pipeline with a brake.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-49-iac-in-pipelines

Tomorrow: Phase 5 mini project — one plan+apply from a pipeline, then destroy.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 49 — IaC in Pipelines` (max 58 chars)
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
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 16 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 16 of 33 (rewrite with your real experience)
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

**Phase 5 mini project**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
