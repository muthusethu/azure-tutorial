# Day 39 - Multi-environment Pipeline

| | |
|---|---|
| **Date** | 28 Sep 2026 |
| **Phase** | 4 - Continuous Delivery |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Dev -> QA -> Staging -> Prod with gates

## Hands-on lab (20-30 min)

1. YAML with 3 stages; approvals on last
2. Promote same artifact, do not rebuild

## Commands / code

```bash
stages:
- stage: Dev
  jobs: [ ... deploy ... ]
- stage: Staging
  dependsOn: Dev
  jobs: [ ... ]
- stage: Prod
  dependsOn: Staging
  jobs:
  - deployment: ProdDeploy
    environment: prod
```

## LinkedIn post (copy-paste)

```
Promote the artifact, not the vibes — rebuilds between envs invent "works in staging" ghosts.

Day 39 of #100DaysOfAzureDevOps. Multi-environment pipeline.

Dev → QA → Staging → Prod is a sentence every deck contains. The failure mode I have seen for a decade is rebuilding the app in each stage "because the pipeline is simpler that way." Staging compiled on Monday. Production compiled on Tuesday from the same commit and pulled a different transitive dependency. Ghosts.

Three stages in YAML. Approvals on the last. The same drop from CI. Dev can be a real App Service. Prod can be echo if budget is tight. The promotion rule does not change.

Patterns I keep seeing

1. Build once, deploy many
• CI publishes drop; each env stage downloads it
• dotnet publish in Prod is a second dice roll

2. dependsOn is the promotion chain
• Staging depends on Dev
• Prod depends on Staging
• Skipping Staging because "we are late" is how you become later

3. Approvals only on the environments that hurt
• Dev can be automatic in a lab
• Prod gets the environment check from Day 38

4. Config is not the artifact
• Connection strings and flags differ by env
• The bits should not. If they must, you are not promoting an artifact — you are assembling one

What I am doing in today's lab

I am writing YAML with three stages — Dev, Staging, Prod — approvals on the last, and the same artifact promoted. Prod can echo if I am not spending. The run should show Dev then Staging then a waiting approval, not three independent rebuilds.

If staging worked, deploy that zip. Vibes are not a promotion strategy.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-39-multi-environment-pipeline

Tomorrow: Phase 4 mini project — CI/CD with visible approvals.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 39 — Multi-environment Pipeline` (max 58 chars)
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

**Phase 4 mini project**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
