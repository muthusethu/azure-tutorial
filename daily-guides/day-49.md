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
Day 49 of #100DaysOfAzureDevOps

IaC without a pipeline is homework; IaC in a pipeline is how grown-ups change prod

Today's topic: **IaC in Pipelines**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Phase 5 mini project.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no "DM me for freelance".
- After posting: leave 5-10 real comments on other Azure/DevOps posts.

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
