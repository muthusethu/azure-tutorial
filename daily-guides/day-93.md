# Day 93 - Capstone Project 3 - IaC Multi-env

| | |
|---|---|
| **Date** | 21 Nov 2026 |
| **Phase** | 10 - Portfolio & Public Launch |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Terraform/Bicep for dev+staging
- Wire to pipeline

## Hands-on lab (20-30 min)

1. Infra for the same capstone; two environments
2. Destroy non-prod when done

## Commands / code

```bash
# infra/ + pipelines/infra.yml with plan/apply approvals
```

## LinkedIn post (copy-paste)

```
Infra as code for your demo is the difference between a toy and a portfolio piece.

Day 93 of #100DaysOfAzureDevOps. Capstone project 3 — IaC multi-environment.

Terraform or Bicep for dev and staging. Wire to a pipeline. The demo that only exists because I clicked in Portal is a toy I cannot reproduce. The demo whose environments come from infra/ plus pipelines/infra.yml with plan/apply approvals is something I can talk about without waving my hands.

Two environments for the same capstone. Destroy non-prod when done. I will not keep two App Service plans as souvenirs.

Patterns I keep seeing

1. Same tool as Phase 5
• Do not switch Bicep to Terraform this week for spice
• Depth on one dialect beats a bilingual toy

2. Two envs, one module/template
• Parameters or tfvars, not a copied folder named infra-prod-final-FINAL
• Promotion of the app artifact is still Day 39's rule

3. Plan in CI, apply gated
• pipelines/infra.yml
• Approval on apply — even for my own lab prod-that-is-not-prod

4. Destroy is in the README
• Non-prod teardown steps
• A portfolio piece that bills forever is a trap I set for myself

What I am doing in today's lab

I am adding infra/ for the capstone, two environments, a pipeline with plan and gated apply, then destroying non-prod when the screenshot exists. Toy vs portfolio is whether a stranger could recreate the env from the repo without me on a screenshare.

If the environment is a rumor, the demo is a toy. Put it in code so the portfolio piece can be rebuilt.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-93-capstone-project-3-iac-multi-env

Tomorrow: GitHub portfolio — README that a stranger can run.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 93 — Capstone 3: IaC Multi-env` (max 58 chars)
3. Paste the text above (press **Enter** between sections so line breaks stay)

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

**GitHub portfolio setup**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
