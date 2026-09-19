# Day 47 — Terraform with Azure (azurerm)

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 5 - Infrastructure as Code |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

azurerm is Terraform's Azure dialect. features {} is required. Auth today is az login, not a master-key SPN

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Piece | HCL / CLI | Maps to |
| --- | --- | --- |
| Provider | required_providers hashicorp/azurerm  + features {} | ARM APIs. Empty features {} is still required |
| Auth (lab) | az login; az account set --subscription | Azure CLI token. Terraform uses that context |
| RG | azurerm_resource_group.lab | Microsoft.Resources/resourceGroups |
| Storage | azurerm_storage_account.lab  account_replication_type LRS | Microsoft.Storage/storageAccounts |
| Graph | storage.resource_group_name = azurerm_resource_group.lab.name | Wrong ref → plan creates a second RG |

## Step-by-step lab

1. az login and az account show. Confirm the personal subscription ID. az account set if it pointed at the wrong one.
2. Extend Day 46: add azurerm_storage_account in rg-day47-tf (new RG name). Pin provider ~> 3.100.
3. terraform plan. Confirm one RG + one storage. If you see two RGs, fix the reference.
4. terraform apply. az storage account show -g rg-day47-tf -n <name>.
5. No subscription-Owner service principal. Your user is enough for a lab.
6. terraform destroy -auto-approve. Confirm both resources gone.

## Done when

- [ ] az account show was the personal subscription
- [ ] Plan showed one RG + one storage via resource references
- [ ] features {} present; provider version pinned
- [ ] destroy completed

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-47-terraform-with-azure-azurerm
```

## Next

**Day 48** — Terraform modules and remote state — backend azurerm, blob lease locking, destroy order.
