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
CD to Kubernetes without Git is sticky-note ops wearing a hoodie.

Day 57 of #100DaysOfAzureDevOps. Deploying to AKS via pipelines.

kubectl apply from a laptop is fine until three people do it with three versions of the manifest. Sticky notes. A hoodie. Azure DevOps can apply KubernetesManifest@1 from the repo: namespace, manifests: k8s/*.yml, a service connection that is not cluster-admin forever if I can help it.

If I have no AKS, I practice kubectl against local kind/minikube with the same pipeline shape, or I run the task against the local kubeconfig story and still keep YAML in Git. GitOps (Flux/Argo) is a later day. Push-from-pipeline is today's honest CD.

Patterns I keep seeing

1. Manifests live in the repo
• k8s/*.yml is the source
• A change that only exists on a workstation is not a release

2. The task is the apply
• KubernetesManifest@1 action: deploy
• Service connection / kubeconfig is identity — least privilege later in the security phase

3. Image tag must move
• If the YAML is stuck on :latest, I did not deploy a build — I deployed a mood
• Substitute Build.BuildId in the manifest or via Helm tomorrow

4. No cluster? Local still counts
• kind/minikube apply
• The anti-pattern is still sticky-note kubectl to "the" cluster

What I am doing in today's lab

If I have AKS, the pipeline applies manifests. If I do not, I apply the same files locally and keep them in Git. Either way I will not treat a manual kubectl as the production process. Hoodies are not a release strategy.

If Git does not know the cluster state you intended, you do not have CD. You have a memory.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-57-deploying-to-aks-via-pipelines

Tomorrow: Helm charts — values.yaml so environments stop being copy-paste crimes.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 57 — Deploying to AKS via Pipelines` (max 58 chars)
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

**Helm basics**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
