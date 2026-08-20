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
Day 58 of #100DaysOfAzureDevOps

Helm is templating for YAML mountains - values.yaml is where environments stop being copy-paste crimes

Today's topic: **Helm Charts Basics**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: AKS scaling & networking.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

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

**AKS scaling & networking**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
