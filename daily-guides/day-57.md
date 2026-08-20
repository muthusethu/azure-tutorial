# Day 57 - Deploying to AKS via Pipelines

| | |
|---|---|
| **Date** | 16 Oct 2026 |
| **Phase** | 6 - Containers & Kubernetes |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- kubectl/Helm tasks, service connections

## Hands-on lab (20-30 min)

1. If no AKS: practice kubectl against local cluster
2. Pipeline applies manifests

## Commands / code

```bash
- task: KubernetesManifest@1
  inputs:
    action: deploy
    namespace: default
    manifests: k8s/*.yml
```

## LinkedIn post (copy-paste)

```
Day 57 of #100DaysOfAzureDevOps

CD to Kubernetes without Git is sticky-note ops wearing a hoodie

Today's topic: **Deploying to AKS via Pipelines**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Helm basics.

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

**Helm basics**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
