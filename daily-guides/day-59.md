# Day 59 - AKS Scaling, Monitoring & Networking

| | |
|---|---|
| **Date** | 18 Oct 2026 |
| **Phase** | 6 - Containers & Kubernetes |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- HPA, cluster autoscaler, ingress, network policies - survey

## Hands-on lab (20-30 min)

1. Read HPA docs; write when you would use HPA vs more replicas fixed
2. Skip deep CNI labs if time-boxed

## Commands / code

```bash
# HorizontalPodAutoscaler sketch
# scale on cpu 70% between 1 and 5 replicas
```

## LinkedIn post (copy-paste)

```
Autoscaling without metrics is superstition with YAML.

Day 59 of #100DaysOfAzureDevOps. AKS scaling, monitoring, and networking.

HPA, cluster autoscaler, ingress, network policies. A survey, not a CNI PhD. I have seen replica counts raised because "it felt slow" and HPA added because a tutorial had it, with CPU requests left at zero so the autoscaler stared at nonsense. Superstition. YAML.

HorizontalPodAutoscaler sketch: scale on CPU 70% between 1 and 5 replicas. That sentence requires requests to be set. Cluster autoscaler is nodes, not pods. Ingress is how HTTP enters. Network policy is who may speak. Time-box the deep CNI labs.

Patterns I keep seeing

1. HPA needs a signal
• CPU 70%, min 1, max 5 is a sketch
• Without resource requests, CPU utilization is a ghost story

2. HPA vs fixed replicas is a product choice
• Fixed is fine for a lemonade stand
• HPA is for load that actually moves
• I am writing when I would use which — not adding HPA as jewelry

3. Cluster autoscaler is a different lever
• Pods pending for lack of nodes vs pods needing more replicas on existing nodes
• Confusing them is how you scale the wrong thing

4. Ingress and network policy are the city gates
• Survey: ingress controller, TLS later
• Skip deep CNI if the clock says so — write what I skipped

What I am doing in today's lab

I am reading HPA docs, writing when I would use HPA vs a fixed replica count, and skipping a deep CNI lab if I am time-boxed. If the cluster still exists from Day 56, I am also checking whether destroy is still on the weekend calendar.

If you cannot name the metric, do not autoscale. YAML will happily encode the superstition.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-59-aks-scaling-monitoring-networking

Tomorrow: Phase 6 mini project — image in ACR plus one automated deploy path.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 59 — AKS Scale, Monitor, Network` (max 58 chars)
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

**Phase 6 mini project**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
