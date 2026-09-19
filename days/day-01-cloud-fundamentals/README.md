# Day 1 — Cloud Computing & Azure Fundamentals

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 1 - Azure & DevOps Foundations |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Who holds the spatula, which city, which building

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Layer | IaaS (VM) | PaaS (App Service) | SaaS |
| --- | --- | --- | --- |
| Azure type | Microsoft.Compute/virtualMachines | Microsoft.Web/sites, Microsoft.Web/sites/functions | Microsoft 365, GitHub, Azure DevOps |
| Application / data | You: app, disks, backups | You: app + App Settings / Connection Strings | Vendor: tenant data under their SLA |
| Runtime / middleware | You: IIS, nginx, .NET, Node, Java | Vendor: Kudu / platform stack you pick | Vendor |
| OS / patching | You: Windows/Linux Update, NSG, disks | Vendor patches the worker | Vendor |
| Network / identity | You: VNet, NIC, NSG, public IP | You: VNet integration, Private Endpoint, Entra ID | Vendor + your tenant admin |
| Failure blast | You reboot the VM; you own the 2am patch | Swap slot / scale out; platform recycles workers | Wait on vendor status + your admin settings |

## Step-by-step lab

1. portal.azure.com → sign in with the personal Microsoft account. Top-right directory picker: confirm it is NOT a work tenant.
2. Subscriptions → open the personal subscription → copy Name + Subscription ID into notes (never a work sub).
3. Cost Management + Billing → Budgets → Add → amount Rs 500 or $20 → alert email = you. Save.
4. Resource groups → Create → Name rg-day01-lab → Region Central India (or nearest) → Review + create.
5. Open Cloud Shell (Bash) → az account show --output table → confirm the same subscription ID.
6. Browse Create a resource → Storage account or App Service create blade. Read SKUs. Do NOT deploy.
7. Optional: az group list --output table. Keep rg-day01-lab for Day 2 or delete if you created nothing inside.

## Done when

- [ ] Can explain IaaS vs PaaS vs SaaS with one Azure resource type each
- [ ] Can explain Region vs Availability Zone without saying 'datacenter somewhere'
- [ ] Budget alert exists on the personal subscription
- [ ] rg-day01-lab exists in the chosen region (or you can recreate it)

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-01-cloud-fundamentals
```

## Next

**Day 2** — Azure Portal, CLI & PowerShell basics
