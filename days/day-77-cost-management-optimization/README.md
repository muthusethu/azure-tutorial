# Day 77 — Cost Management & Optimization

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 8 - Monitoring & Observability |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

The best Azure skill is deleting things you can name

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Control | Azure object | What it actually does |
| --- | --- | --- |
| Cost Analysis | Microsoft.CostManagement / Portal Cost Analysis | Filter by resource group, meter, tag |
| Budget + alert | Microsoft.Consumption/budgets | Email/Action Group before the invoice, not after |
| Advisor cost recs | Microsoft.Advisor recommendations (Cost) | Idle SKUs, reserved-instance noise; still a list, not a bill |
| Resource graph | az group list / az resource list | Orphans: Public IP, Basic ACR, forgotten AKS |
| IaC destroy | terraform destroy / az deployment ... --mode Complete | Delete the way you created, or Portal if it was click-ops |

## Step-by-step lab

1. az account show -o table. Confirm the personal subscription name and ID. Stop if it is not yours.
2. Portal → Cost Management + Billing → Cost Analysis. Filter last 30 days by resource group. Write the top three meters in docs/cost-day77.md (no invented %).
3. Cost Management → Budgets. Tighten the lab budget alert (amount or filter). Note the new threshold in the markdown.
4. az group list -o table. Mark every RG that is not part of this week's lab.
5. Delete unused groups: az group delete -n <old-rg> --yes --no-wait. If born from Terraform/Bicep, destroy from that tool first.
6. If AKS, a Basic ACR, or a leftover Public IP is still listed, delete it today. Then re-run az group list.

## Done when

- [ ] az account show is the personal subscription
- [ ] Wrote top Cost Analysis meters without a fake savings percentage
- [ ] Budget alert tightened
- [ ] At least one unused RG deleted, or wrote 'none leftover' with the group list
- [ ] docs/cost-day77.md on the personal repo

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-77-cost-management-optimization
```

## Next

**Day 78** — Azure Advisor and the Well-Architected pillars — one recommendation, one written decision
