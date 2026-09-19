# Day 57 — Deploying to AKS via Pipelines

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 6 - Containers & Kubernetes |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

CD to Kubernetes without Git is sticky-note kubectl wearing a hoodie

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Dimension | kubectl apply from PC | Pipeline deploy |
| --- | --- | --- |
| Source | Whatever is on disk, maybe uncommitted | k8s/*.yml (or baked Helm) on the commit being built |
| Identity | Your user kubeconfig. Easy to be cluster-admin | Azure RM / Kubernetes service connection. Scope it; Day 63/69 will be rude |
| Image | Easy to leave :latest | KubernetesManifest@1 containers: input substitutes Build.BuildId |
| Namespace | You remember -n, or you don't | inputs.namespace: workloads — never kube-system |
| No AKS | kind apply is still Git if the files are committed | Same YAML, local kubeconfig job or skip Azure target honestly |

## Step-by-step lab

1. Commit k8s/*.yml from Day 55 (namespace workloads). Confirm no image: …:latest as the only tag — use a placeholder the task will replace, or the Build.BuildId you already pushed.
2. If AKS exists: Project Settings → Service connections → Azure Resource Manager (or Kubernetes) to the personal cluster. Note the role. Not cluster-admin if you can avoid it.
3. Add a pipeline job after Docker@2 (or a second pipeline) with KubernetesManifest@1 action: deploy, namespace workloads, manifests k8s/*.yml, containers: <acr>.azurecr.io/myapp:$(Build.BuildId).
4. Run it. kubectl -n workloads get deploy,po,svc and kubectl -n workloads describe po | find the image. The running tag must be this Build.BuildId.
5. If no AKS: kubectl apply -f k8s/ against kind from the same files, and still keep a YAML pipeline that would deploy — identity is the only missing piece. Do not treat laptop kubectl as the production process.
6. Write docs/aks-deploy-day57.md: connection name, namespace, image tag that actually ran. Helm is tomorrow for values; do not fork the YAML per mood.

## Done when

- [ ] Manifests in Git are the source; namespace is workloads
- [ ] Running image tag equals this build (or kind apply of the same files)
- [ ] Did not kubectl apply from a dirty laptop as the CD story
- [ ] Service connection noted; not treated as cluster-admin folklore

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-57-deploying-to-aks-via-pipelines
```

## Next

**Day 58** — Helm charts — values.yaml instead of YAML-mountain copy-paste
