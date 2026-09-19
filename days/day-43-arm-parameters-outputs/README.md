# Day 43 — ARM Parameters & Outputs

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 5 - Infrastructure as Code |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Parameters are the dials. Outputs are the handshake. Hardcoded names are how labs become landfills

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Piece | Lives in | Consumed by |
| --- | --- | --- |
| parameters | template + @main.parameters.json | az deployment group create -p @file.json |
| variables | template only (computed) | Not overridden at deploy time |
| outputs | template outputs: { endpoint: { value: ... } } | Next script / pipeline; query via az deployment group show |
| uniqueString() | expression in name | Global uniqueness for storage/key vault |
| nested templates | literacy — extra deployment resource | Skip matryoshka today |

## Step-by-step lab

1. Extend yesterday's template with parameters location and skuName, plus an output storageEndpoint.
2. Create infra/main.parameters.json with location=centralindia (or yours) and skuName=Standard_LRS.
3. az group create -n rg-day43-lab -l <location>. Deploy: az deployment group create -g rg-day43-lab -f infra/main.json -p @infra/main.parameters.json.
4. az deployment group show -g rg-day43-lab -n <name> --query properties.outputs -o jsonc. Confirm the endpoint without opening Portal blades as the source of truth.
5. If Terraform is primary: write three lines in docs/arm-params-day43.md and still complete one deploy.
6. az group delete -n rg-day43-lab --yes --no-wait.

## Done when

- [ ] Used -p @parameters.json (the @ matters)
- [ ] Output printed from CLI, not from memory
- [ ] No real secrets in parameter files
- [ ] RG deleted

## LinkedIn

Post draft: [`../../daily-guides/day-43.md`](../../daily-guides/day-43.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-43-arm-parameters-outputs
```

## Next

**Day 44** — Bicep fundamentals — same control plane, resource declarations, uniqueString, less brace sport.
