# Day 56 — AKS Setup

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 6 - Containers & Kubernetes |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

A one-node cluster is still a control plane plus a VM bill — create only with a destroy date

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Piece | What Azure runs | What you must not confuse |
| --- | --- | --- |
| Control plane | Managed API server, etcd, scheduler. You pay the AKS SKU relationship | A VM you SSH to 'the master'. You do not |
| System node pool | First pool, mode=System. kube-system DaemonSets/pods (CoreDNS, CoreDNS-autoscaler, CSI) | A place to schedule myapp 'because there is only one node' |
| User node pool | mode=User. Where Deployments for workloads should land (taints/labels in real designs) | Optional on a 1-node lab — still know the mode exists |
| Network plugin | kubenet (pod CIDR + NAT) vs Azure CNI (pod VNet IPs) vs Azure CNI Overlay (recommended IP conservation) | Rebuilding the cluster three times to 'compare' as a personality trait |
| Identity | kubelet uses managed identity (kubelet_identity) for ACR AcrPull | imagePullSecrets with ACR admin as the default |

## Step-by-step lab

1. Read AKS node pools and kubenet vs Azure CNI vs Azure CNI Overlay at a survey level. Write one sentence each. Do not rebuild three clusters to feel thorough.
2. Decide: create smallest AKS, or skip to Container Apps/ACI and write why. If you cannot put destroy on this weekend's calendar, you skip.
3. If creating: az group create rg-day56; az aks create with --node-count 1, a small VM size, --network-plugin azure --network-plugin-mode overlay, --generate-ssh-keys. Then az aks nodepool list and note mode=System.
4. az aks get-credentials -g rg-day56 -n aks-lab --overwrite-existing. kubectl get nodes. kubectl get pods -n kube-system. Do not apply myapp into kube-system.
5. Grant the kubelet identity AcrPull on the lab ACR if you will deploy tomorrow (az aks show --query identityProfile.kubeletidentity.objectId).
6. Write docs/aks-day56.md: created or skipped, destroy date or skip reason, system vs user pool, kube-system vs workloads. If created, put az aks delete in the doc as a copy-paste.

## Done when

- [ ] Either a one-node lab cluster with a written destroy date, or a written skip to ACI/Container Apps
- [ ] Can explain system node pool vs user pool and why myapp is not kube-system
- [ ] Can explain Overlay vs kubenet vs CNI in one sentence each
- [ ] docs/aks-day56.md exists; no SSH keys in Git

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-56-aks-setup
```

## Next

**Day 57** — Deploy to AKS from a pipeline (or the same manifests against kind)
