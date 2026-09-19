# Day 52 — Azure Container Registry (ACR)

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 6 - Containers & Kubernetes |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

App images belong in a private registry — Docker Hub is for bases you meant to be public

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Dimension | ACR (azurecr.io) | Docker Hub |
| --- | --- | --- |
| Audience | Private registry in your subscription. Default deny to the world | Public-by-habit for tags unless the repo is paid-private |
| Name | Globally unique. myacr.azurecr.io/myapp:tag | docker.io/library/… or your Hub namespace |
| Auth | az acr login / AcrPush+AcrPull RBAC / WIF. Admin user is a password in a drawer | Hub credentials. Fine for public bases; wrong for app bits + .env accidents |
| SKU | Basic (lab), Standard, Premium (geo-replication, private link, retention) | Hub plan limits. Not an Azure resource you can RBAC |
| Tasks | acr build / ACR Tasks can build in Azure. Optional literacy | Hub automated builds are a different product. Not today's lab |

## Step-by-step lab

1. az group create -n rg-day52 -l eastus. az acr create -g rg-day52 -n <uniqueacr> --sku Basic --admin-enabled false. If the name is taken, pick another — do not hijack a registry.
2. az acr login -n <uniqueacr>. Confirm docker is talking to that login server, not docker.io.
3. docker tag myapp:day51 <uniqueacr>.azurecr.io/myapp:day52 then docker push <uniqueacr>.azurecr.io/myapp:day52. Optional second tag :latest as a pointer only.
4. Portal → Container registries → Repositories, or az acr repository show-tags -n <uniqueacr> --repository myapp -o table. Copy the digest, not only the tag.
5. Do not enable admin user. Do not docker push the app image to Docker Hub. Delete extra tags you created as experiments.
6. Write docs/acr-day52.md: registry name, tag, digest, and the one-line rule (Hub for bases, ACR for myapp). Leave the registry for Day 53 unless cost is tight — then note you will recreate.

## Done when

- [ ] Basic ACR exists on the personal subscription; admin user is off
- [ ] myapp:day52 is in <acr>.azurecr.io, not on Docker Hub
- [ ] Can explain tag vs digest and why latest is not the promotion ID
- [ ] docs/acr-day52.md recorded the digest

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-52-azure-container-registry-acr
```

## Next

**Day 53** — Build and push the image from a pipeline — humans stop tagging on Fridays
