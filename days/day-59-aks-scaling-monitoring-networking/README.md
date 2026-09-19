# Day 59 — AKS Scaling, Monitoring & Networking

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 6 - Containers & Kubernetes |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

HPA scales pods; cluster autoscaler scales nodes; neither works without a metric

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Lever | What it changes | Requires |
| --- | --- | --- |
| Fixed replicas | Deployment.spec.replicas | Honesty that load is flat. Fine for a lemonade stand |
| HPA | Pod replica count from a metric (CPU 70%, 1–5) | resources.requests.cpu on the container. metrics-server in kube-system |
| Cluster autoscaler | Node count when pods are Pending for capacity | Autoscaler add-on + a node pool that can scale. Not a substitute for HPA |
| Ingress | HTTP entry (ingress controller + Ingress object) | A controller (nginx/AGIC/etc). Not a Service type folklore |
| NetworkPolicy | Who may speak to whom in the CNI | A plugin that enforces (Azure Network Policy / Calico). Default-allow if none |

## Step-by-step lab

1. Read HorizontalPodAutoscaler v2 and cluster autoscaler docs enough to write: HPA changes replicas; CA changes nodes; both need a signal.
2. Open your Deployment: confirm resources.requests.cpu exists (Day 55). If not, add 50m. Write why HPA is undefined without it.
3. Write docs/scale-day59.md with a table: when fixed replicas vs HPA vs CA. Include one sentence on Ingress vs LoadBalancer and one on NetworkPolicy default-allow.
4. Optional: apply the HPA sketch to kind/AKS and kubectl get hpa. Do not load-test a paid cluster just to see a replica flicker.
5. Skip deep CNI / AGIC labs if the clock says so — write what you skipped. Do not paste a default-deny NetworkPolicy into kube-system.
6. If AKS from Day 56 exists, confirm the destroy date is still on the calendar (or delete now). Container Insights is literacy, not a requirement to leave the cluster up.

## Done when

- [ ] Can separate HPA (pods) from cluster autoscaler (nodes) without mixing YAML objects
- [ ] Wrote when fixed replicas beat HPA for this app
- [ ] Know HPA needs resource requests and a metrics signal
- [ ] AKS destroy date re-checked or skip path still honest

## LinkedIn

Post draft: [`../../daily-guides/day-59.md`](../../daily-guides/day-59.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-59-aks-scaling-monitoring-networking
```

## Next

**Day 60** — Phase 6 mini project — one image in ACR, one automated run path
