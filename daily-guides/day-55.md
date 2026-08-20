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
Day 55 of #100DaysOfAzureDevOps

Kubernetes is an airport for containers - powerful, expensive, and overkill for a lemonade stand

Today's topic: **Kubernetes Fundamentals**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: AKS setup.

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

**AKS setup**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
