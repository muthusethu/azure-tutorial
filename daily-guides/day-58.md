# Day 58 - Helm Charts Basics

| | |
|---|---|
| **Date** | 17 Oct 2026 |
| **Phase** | 6 - Containers & Kubernetes |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Chart structure, values.yaml, releases

## Hands-on lab (20-30 min)

1. `helm create myapp` and package values for image tag
2. Install/upgrade/uninstall once

## Commands / code

```bash
helm create charts/myapp
helm upgrade --install myapp charts/myapp --set image.tag=$(Build.BuildId)
```

## LinkedIn post (copy-paste)

```
Helm is templating for YAML mountains — values.yaml is where environments stop being copy-paste crimes.

Day 58 of #100DaysOfAzureDevOps. Helm charts basics.

Three folders of nearly identical Kubernetes YAML is a crime scene. Helm's chart is a mountain with a trail: Chart.yaml, templates/, values.yaml. helm create myapp. Then values for image tag, replica count, environment. upgrade --install so install and upgrade are one thought.

I have watched teams fork a chart per environment and then forget to copy a security context. values.yaml is where env differences belong. Template drift is how prod missed a probe for six months.

What I keep seeing

1. create, then delete most of the sample
• helm create charts/myapp
• The sample chart is a tour, not a product

2. image.tag is a value
• helm upgrade --install myapp charts/myapp --set image.tag=$(Build.BuildId)
• Hardcoded latest in the template is the Friday tag again

3. One chart, many values files
• values-dev.yaml vs values-prod.yaml
• Not charts-dev vs charts-prod copies

4. uninstall is a lab skill
• Install, upgrade a tag, uninstall once
• Helm releases left behind are unnamed pets

What I am doing in today's lab

I am running helm create, packaging values for the image tag, install/upgrade once with --set image.tag, then uninstall. If I have no cluster, I still helm template and read the rendered YAML so I can see the Deployment the chart actually produced. Rendering is the point of the mountain. A chart I never render is just another folder of hopes.

Stop copying YAML mountains. Put the difference in values. That is the whole trick.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-58-helm-charts-basics

Tomorrow: AKS scaling, monitoring, networking — HPA vs fixed replicas.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 58 — Helm Charts Basics` (max 58 chars)
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
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 19 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 19 of 33 (rewrite with your real experience)
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

**AKS scaling & networking**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
