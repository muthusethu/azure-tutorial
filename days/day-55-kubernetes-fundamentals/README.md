# Day 55 — Kubernetes Fundamentals

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 6 - Containers & Kubernetes |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Learn the airport (Pod, Deployment, Service, namespace) before you land a lemonade stand on AKS

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Object | Job | Where it lives |
| --- | --- | --- |
| Namespace | Tenancy lite. DNS and RBAC boundary | workloads for the app. kube-system for CoreDNS, kube-proxy, konnectivity — not Deployments of myapp |
| Pod | Smallest run unit. One or more containers, shared netns | Created by a controller. Naked Pods in prod are pets |
| Deployment | replicas + selector + pod template. Rolling updates | Workloads namespace. selector.matchLabels must equal template labels |
| Service | Stable virtual IP / DNS. Selects Pods by label, not by folklore IP | ClusterIP for in-cluster. containerPort must match the process |
| kube-system | Cluster plumbing. CoreDNS answers Service DNS | kubectl get pods -n kube-system is literacy. Do not kubectl apply your app there |

## Step-by-step lab

1. Write k8s/namespace.yaml (workloads), k8s/deployment.yaml, k8s/service.yaml for the sample app. Image from ACR with a pinned tag, not latest. replicas: 1. resources.requests set (cpu 50m, memory 64Mi).
2. Confirm labels: Deployment selector, pod template, Service selector are identical (app: myapp). Confirm containerPort matches the process.
3. If kind/minikube exists: kubectl apply -f k8s/ && kubectl -n workloads get deploy,po,svc,ep. kubectl -n kube-system get po — look, do not apply the app there.
4. If no local cluster: still write the YAML. Trace a request: Service ClusterIP → endpoints → Pod IP:containerPort. That tracing is the lab.
5. kubectl explain deployment.spec.template.spec.containers  (or read the YAML) until you can say why a naked Pod is the wrong object.
6. Write docs/k8s-day55.md: the three objects, why kube-system is off-limits for myapp, and that AKS is optional tomorrow with a destroy date.

## Done when

- [ ] Can map Service → endpoints → Pod without calling the Pod 'the Deployment'
- [ ] Manifests target namespace workloads, not kube-system
- [ ] Labels agree; port agrees; image tag is pinned
- [ ] Applied on kind/minikube OR traced on paper — AKS not created today

## LinkedIn

Post draft: [`../../daily-guides/day-55.md`](../../daily-guides/day-55.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-55-kubernetes-fundamentals
```

## Next

**Day 56** — AKS setup — optional gym membership with a cancel date
