# Day 90 - Mini Project + Recap (Phase 9)

| | |
|---|---|
| **Date** | 18 Nov 2026 |
| **Phase** | 9 - Advanced & Enterprise |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Reusable pipeline template as the 'enterprise' artifact

## Hands-on lab (20-30 min)

1. Publish `templates/` used by 2 sample pipelines
2. Recap

## Commands / code

```bash
# Done = one template, two consumers, one green run each
```

## LinkedIn post (copy-paste)

```
Phase 9 recap: enterprise is reuse plus guardrails, not more YAML copy-paste.

Day 90 of #100DaysOfAzureDevOps. Mini project and recap for Phase 9 — advanced and enterprise patterns.

Repo strategy, templates, marketplace restraint, Jenkins mapping, multi-cloud caution, DR that restores, landing zones on paper, GitOps vs push, a paved-road catalog. The mini project is the enterprise artifact: templates/ used by two sample pipelines, one green run each.

Enterprise is not a font on a slide. It is one fix that repairs two consumers, plus a gate that still bites.

What I am keeping from Phase 9

1. One template, two consumers
• If both are green, reuse is real
• If I duplicated to go green, I failed the recap with extra files

2. Guardrails from Phase 7 still apply
• Secrets, approvals, Policy
• A template that echoes secrets is a faster incident

3. Paper architecture counts
• Landing zone sketch, GitOps comparison, DR targets
• I do not need a fake enterprise subscription to have thought

4. Definition of done
• one template, two consumers, one green run each
• ADR for monorepo still true unless I changed it on purpose

What I am doing in today's lab

I am publishing templates/ consumed by two sample pipelines, running both to green, and writing the recap. Reuse plus guardrails. If a third pipeline still has pasted YAML, I extract or I admit it is leftover homework. Two green consumers is the definition of done — not a third unique snowflake.

Enterprise is not more YAML. It is less YAML, better gates, and a road people actually walk.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-90-mini-project-recap-phase-9

Tomorrow: Capstone 1 — thin vertical slice, not a fake ecommerce platform.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 90 — Phase 9 Mini Project & Recap` (max 58 chars)
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

**Capstone 1**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
