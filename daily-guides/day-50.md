# Day 50 - Mini Project + Recap (Phase 5)

| | |
|---|---|
| **Date** | 09 Oct 2026 |
| **Phase** | 5 - Infrastructure as Code |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Provision an environment via your chosen IaC in a pipeline

## Hands-on lab (20-30 min)

1. One RG + one storage or webapp skeleton
2. Destroy after screenshot
3. Recap: why you picked Bicep or Terraform

## Commands / code

```bash
# Definition of done: plan+apply from pipeline once; destroy once
```

## LinkedIn post (copy-paste)

```
Phase 5 recap: click-ops is a hobby; IaC is how you sleep.

Day 50 of #100DaysOfAzureDevOps. Mini project and recap for Phase 5 — Infrastructure as Code.

ARM for literacy, Bicep for Azure-native calm, Terraform for state and modules, then the same files in a pipeline. The mini project is not a landing zone. It is one resource group plus one storage account or a webapp skeleton, provisioned by the tool I picked on Day 41, from a pipeline, then destroyed after a screenshot.

I sleep better when the Portal is a view, not a source of truth. Click-ops is fun until the person who clicked is on leave.

What I am keeping from Phase 5

1. One primary tool, one honest reason
• The recap says why Bicep or why Terraform
• "Both" is not a reason. It is indecision with extra files

2. Plan/what-if before apply
• A diff I did not read still executes
• Pipeline + approval is the grown-up version of that rule

3. State and names are operational
• Remote state with locking, or Bicep without that class of ghost
• unique names, parameter files, destroy when the demo ends

4. Definition of done is boring
• plan+apply from pipeline once; destroy once
• A screenshot without secrets; RG gone or budget-watched

What I am doing in today's lab

I am provisioning one RG plus storage or a webapp skeleton via the chosen IaC in a pipeline, screenshotting the green run, destroying after, and writing why I picked Bicep or Terraform. If I still have leftover day-42 RGs, those die too. Sleep is a cost-control strategy.

Hobbies can live in the Portal. Environments that must survive a weekend live in code.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-50-mini-project-recap-phase-5

Tomorrow: Docker fundamentals — images, layers, a hello Dockerfile.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 50 — Phase 5 Mini Project & Recap` (max 58 chars)
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

**Docker fundamentals**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
