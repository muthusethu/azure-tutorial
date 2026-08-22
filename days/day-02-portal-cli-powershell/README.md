# Day 02 — Azure Portal, CLI & PowerShell

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Know **when** to use Portal vs CLI vs PowerShell. Create a resource group from the CLI on a personal subscription.

## High-level architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the decision diagram. Short version:

| Tool | Metaphor | Best for |
|------|----------|----------|
| **Portal** | Tourist map | First-time exploration, visual checks |
| **Azure CLI (`az`)** | GPS coordinates | Repeatable scripts, pipelines later |
| **PowerShell** | Swiss-army knife | Windows automation, object pipelines |

**Rule of thumb:** explore once in Portal → second time use CLI → forever after, script it.

## Learn

- [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)
- Naming: `rg-day02-lab` beats `New Resource Group (1)`

## Step-by-step lab

1. Install Azure CLI on a **personal** PC.
2. `az login` → select personal subscription.
3. Create `rg-day02-lab` in Central India (or nearest).
4. Optionally recreate once via Portal to feel the click cost.
5. Delete when done.

```bash
az login
az group create --name rg-day02-lab --location centralindia
az group list --output table
az group delete --name rg-day02-lab --yes --no-wait
```

## Done when

- [ ] You can explain Portal vs CLI vs PowerShell in one sentence each  
- [ ] `az login` works on your machine  
- [ ] You created an RG without relying only on Portal  

## LinkedIn

Post draft: [`../../daily-guides/day-02.md`](../../daily-guides/day-02.md)  
Attach **[handout.pdf](./handout.pdf)** as a LinkedIn document.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-02-portal-cli-powershell
```

Hashtags: `#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic`

## Next

**Day 03** — Azure Resource Manager (ARM) basics.
