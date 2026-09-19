# Day 88 — GitOps with Flux/Argo CD

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 9 - Advanced & Enterprise |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

The cluster stops being a petting zoo for kubectl

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Dimension | Azure Pipelines push (Day 57) | Flux / Argo pull |
| --- | --- | --- |
| Source of truth | Pipeline run + what it last applied | Git commit the controller wants |
| Who talks to the API | Pipeline job (service connection / kubeconfig) | In-cluster controller reconciles |
| Change window | YAML stage + env approval | PR review, then merge; cluster follows |
| Drift | Unless you re-run, drift can hide | Reconcile loop notices and heals or fights you |
| Hotfix temptation | az / kubectl in a job or from a laptop | kubectl apply is debt; PR is the path |
| Lab default | Push is enough for App Service / Container Apps | GitOps when a cluster is the product |

## Step-by-step lab

1. Read the GitOps principles (desired state in Git, declarative, pulled, continuously reconciled). Write them in docs/gitops-day88.md.
2. Write a push-vs-pull table comparing Azure Pipelines apply (Day 57) to Flux/Argo reconcile.
3. Optional: Flux quickstart on local kind/minikube — not on a leftover paid AKS unless you will destroy it tonight.
4. Add a sample manifests/gitops/kustomization.yaml (or Flux GitRepository YAML) that points at this personal repo path. Do not apply to a work cluster.
5. Write the cowboy rule: no kubectl hotfix habit even in a lab. A PR changes desired state.
6. If you skip the cluster, the written comparison still finishes the lab. Say so in the markdown.

## Done when

- [ ] Push-vs-pull written in docs/gitops-day88.md
- [ ] Sample manifest or Flux YAML in the personal repo
- [ ] No work-cluster kubeconfig
- [ ] Any AKS started for this lab is destroyed, or you used local-only
- [ ] Posted the LinkedIn document

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-88-gitops-with-flux-argo-cd
```

## Next

**Day 89** — Scaling DevOps for teams — five paved-road capabilities, not a queue that only says no
