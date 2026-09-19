# Day 2 — Azure Portal, CLI & PowerShell Basics

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 1 - Azure & DevOps Foundations |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Portal is the map; CLI is GPS; PowerShell is the object knife

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Hop | What it is | Proof in the lab |
| --- | --- | --- |
| You | Intent: create RG, list, delete | Decide rg-day02-lab / centralindia |
| Portal | portal.azure.com ARM JSON via the blade | Create RG once with clicks to feel the cost |
| Azure CLI | az → REST to management.azure.com | az group create --name rg-day02-lab |
| Azure PowerShell | Az module cmdlets, PS objects | New-AzResourceGroup when you need objects |
| ARM | Auth, RBAC, policy, lock, provider routing | Same 201/202 whether click or CLI |
| Resource provider | Microsoft.Resources/resourceGroups | az group show -n rg-day02-lab -o jsonc |

## Step-by-step lab

1. Install Azure CLI from https://aka.ms/installazurecliwindows (or brew/apt on your OS). Run az version.
2. Terminal: az login → pick the personal subscription. az account set --subscription "<personal-id>".
3. az group create --name rg-day02-lab --location centralindia. Confirm with az group show --name rg-day02-lab -o jsonc.
4. portal.azure.com → Resource groups → Create the same shape once (name rg-day02-portal-compare) to count the clicks.
5. az group list --output table. Compare properties: location, provisioningState, tags.
6. az group delete --name rg-day02-portal-compare --yes --no-wait. Keep or delete rg-day02-lab before Day 3.
7. Optional: pwsh → Connect-AzAccount → Get-AzResourceGroup -Name rg-day02-lab. Same ARM object, different client.

## Done when

- [ ] Can explain Portal vs CLI vs PowerShell in one line each
- [ ] az login targets the personal subscription (az account show)
- [ ] Created rg-day02-lab via CLI and inspected JSON
- [ ] Deleted the compare RG (or documented why it remains)

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-02-portal-cli-powershell
```

## Next

**Day 3** — Azure Resource Manager (ARM) basics
