# Day 54 — Azure Container Instances (ACI)

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 6 - Containers & Kubernetes |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Run one image, get a DNS label, delete the wrapper — no node pool required

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Dimension | ACI | AKS / Container Apps |
| --- | --- | --- |
| What you operate | A container group. No kubelet, no node pool | AKS: control plane + nodes. Container Apps: scale rules, no cluster YAML |
| Bill | vCPU/memory/second while allocated. Easy to forget overnight | AKS: nodes + control plane even at idle. CA: consumption or dedicated |
| Pull from ACR | AcrPull on a managed identity (--acr-identity). Not admin password in history | kubelet / CA revision uses AcrPull or imagePullSecrets |
| Network | Public IP + --dns-name-label, or VNet-injected group | Ingress / internal load balancer / CA ingress |
| Fit | Job, demo URL, sidecar-less hello | AKS when you need kube API. CA when you want scale without kube YAML |

## Step-by-step lab

1. Create a user-assigned identity in the lab RG. Grant it AcrPull on the Day 52 registry. Do not enable ACR admin to 'just run ACI'.
2. az container create with --image <acr>.azurecr.io/myapp:<Build.BuildId or day52>, --ports matching the process, --dns-name-label unique, --assign-identity and --acr-identity on that identity, --restart-policy Never, small CPU/memory.
3. Wait until ProvisioningState Succeeded. Hit http://<label>.<region>.azurecontainer.io (or the IP). If it fails, az container logs — do not immediately jump to AKS.
4. az container delete -g … -n hello-aci --yes. Confirm the group is gone. ACI left running is the lab failure even if the URL worked.
5. Write docs/aci-day54.md: image tag used, whether identity pull worked, delete receipt. Optional: note when you would pick Container Apps instead (HTTP scale) vs AKS (kube API).
6. Do not keep ACI overnight. Do not create AKS today to feel advanced.

## Done when

- [ ] One successful ACI run of the ACR image using AcrPull (not Hub)
- [ ] DNS/port actually answered, or logs explain why — then fixed
- [ ] Container group deleted in the same session
- [ ] docs/aci-day54.md notes identity vs admin-password temptation

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-54-azure-container-instances-aci
```

## Next

**Day 55** — Kubernetes fundamentals — airport vocabulary without buying the airport yet
