# Day 58 — Helm Charts Basics

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 6 - Containers & Kubernetes |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

A release is a named install of a chart — values.yaml is where environments stop being copy-paste crimes

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Noun | What it is | Command that proves it |
| --- | --- | --- |
| Chart | Package: Chart.yaml + templates/ + values.yaml. Not running | helm create charts/myapp ; helm template |
| Release | Named instance of a chart in a namespace (myapp in workloads) | helm list -n workloads |
| Revision | Each upgrade increments. Rollback is a revision, not a vibe | helm history myapp -n workloads |
| values.yaml | Default knobs: image.repository, image.tag, replicaCount | helm upgrade --install … --set image.tag=… |
| templates/ | Go templates → Kubernetes YAML. Render before you trust it | helm template myapp charts/myapp --set image.tag=demo |

## Step-by-step lab

1. helm create charts/myapp. Open Chart.yaml, values.yaml, templates/deployment.yaml. Note image.repository / image.tag. Strip sample nginx assumptions you will not run.
2. Point values at <acr>.azurecr.io/myapp. Do not hardcode latest in the template — it must be .Values.image.tag.
3. helm template myapp charts/myapp --set image.tag=day58 --namespace workloads | less  — confirm Deployment image and namespace. This step counts if you have no cluster.
4. If a cluster exists: helm upgrade --install myapp charts/myapp -n workloads --create-namespace --set image.tag=<Build.BuildId> --wait. helm list / helm history.
5. Upgrade the tag once more. Confirm revision incremented. Then helm uninstall myapp -n workloads once so you know the opposite of install.
6. Write docs/helm-day58.md: chart vs release vs revision in one line each, and the rendered image line. Optional pipeline: HelmDeploy@1 or a script step with the same upgrade --install.

## Done when

- [ ] Can distinguish chart, release, and revision out loud
- [ ] image.tag comes from values/--set, not a hardcoded latest in the template
- [ ] helm template ran; install/upgrade/uninstall once if a cluster exists
- [ ] Release namespace is workloads, not kube-system

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-58-helm-charts-basics
```

## Next

**Day 59** — AKS scaling, monitoring, networking — HPA needs requests, not superstition
