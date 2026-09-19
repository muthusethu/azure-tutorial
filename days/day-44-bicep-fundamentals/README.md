# Day 44 — Bicep Fundamentals

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 5 - Infrastructure as Code |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Bicep is ARM with the JSON horror filed down — same types, same apiVersions, a compiler you install

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Bicep | Becomes | Notes |
| --- | --- | --- |
| param location string = resourceGroup().location | ARM parameters | Default from the RG; still overridable |
| resource stg 'Microsoft.Storage/storageAccounts@2023-01-01' | resources[] with that apiVersion | Type string is the ARM type |
| sku: { name: 'Standard_LRS' } | properties/sku in JSON | Blocks instead of quote nests |
| name: 'st${uniqueString(resourceGroup().id)}' | concat + uniqueString | Stops the landfill of colliding names |
| az bicep build -f main.bicep | main.json ARM | You can read the broccoli it emitted |

## Step-by-step lab

1. az bicep install && az bicep version. Confirm the CLI can compile.
2. Write infra/main.bicep from the starter. az bicep build -f infra/main.bicep and glance at the JSON once.
3. az group create -n rg-day44-lab -l centralindia. az deployment group create -g rg-day44-lab -f infra/main.bicep.
4. If Terraform is primary: stop after build + reading the resource symbol; optional deploy still recommended, then destroy.
5. Confirm the storage account exists (az resource list -g rg-day44-lab -o table).
6. az group delete -n rg-day44-lab --yes --no-wait.

## Done when

- [ ] az bicep version works
- [ ] Resource type string includes apiVersion
- [ ] Name uses uniqueString, not pride
- [ ] RG deleted after proof

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-44-bicep-fundamentals
```

## Next

**Day 45** — Bicep modules and what-if — split storage out, read Create/Modify/Delete before the audience arrives.
