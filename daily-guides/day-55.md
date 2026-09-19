# Day 55 - Kubernetes Fundamentals

| | |
|---|---|
| **Date** | 14 Oct 2026 |
| **Phase** | 6 - Containers & Kubernetes |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Pods, Deployments, Services, namespaces
- Prefer concepts + kind/minikube if AKS cost is high

## Hands-on lab (20-30 min)

1. Write a Deployment+Service YAML for your app
2. Apply on local kind/minikube OR read-only if no cluster

## Commands / code

```bash
apiVersion: apps/v1
kind: Deployment
metadata: { name: myapp }
spec:
  replicas: 1
  selector: { matchLabels: { app: myapp } }
  template:
    metadata: { labels: { app: myapp } }
    spec:
      containers:
      - name: myapp
        image: <acr>.azurecr.io/myapp:latest
        ports: [{ containerPort: 80 }]
```

## LinkedIn post (copy-paste)

```
Kubernetes is an airport for containers — powerful, expensive, and overkill for a lemonade stand.

Day 55 of #100DaysOfAzureDevOps. Kubernetes fundamentals.

Pods, Deployments, Services, namespaces. The vocabulary is the ticket. The airport is real: scheduling, networking, identity, and a bill if you choose AKS too early. I have watched lemonade-stand apps land on a cluster because a résumé wanted the word Kubernetes. The app needed a container and a URL. It got an airport.

Prefer concepts plus kind or minikube if AKS cost is high. Write a Deployment+Service YAML. Apply locally. If there is no cluster, reading the YAML and tracing a request through Service → Pod is still the lab. AKS is tomorrow and optional.

Patterns I keep seeing

1. Pod is a wrapper, Deployment is the adult
• You rarely create naked Pods in production
• replicas, selector, template.labels must agree or the Deployment stares at an empty room

2. Service is how traffic finds Pods
• Labels, not IP folklore
• containerPort in the spec must match what the process listens on

3. Namespaces are tenancy lite
• default is fine for a lab
• Everything in default forever is how lemonade stands become lost luggage

4. Local cluster is a valid airport simulator
• kind/minikube for apply
• Read-only if I cannot run a cluster — still write the YAML

What I am doing in today's lab

I am writing a Deployment+Service YAML for the app (image from ACR, port 80), applying on local kind/minikube if I have it, or tracing the YAML on paper if I do not. I am not creating AKS today just to feel advanced.

Learn the airport. Do not land a lemonade stand there until the stand needs runways.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-55-kubernetes-fundamentals

Tomorrow: AKS setup — smallest cluster or skip; destroy the same weekend if I create it.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 55 — Kubernetes Fundamentals` (max 58 chars)
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
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 18 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 18 of 33 (rewrite with your real experience)
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

**AKS setup**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
