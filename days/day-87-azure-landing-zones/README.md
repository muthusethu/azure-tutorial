# Day 87 — Azure Landing Zones

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 9 - Advanced & Enterprise |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

City planning for Azure — skip it and resource groups squat

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Piece | Job | What you draw today |
| --- | --- | --- |
| Management groups | Policy and RBAC inheritance | Root → Platform → Landing zones → Sandboxes |
| Platform sub | Identity, connectivity, management | Hub VNet, firewall/DNS box, log sink |
| Landing zone sub | Workloads | One spoke VNet per app family |
| Hub-spoke | Shared network path, not a mesh of accidents | Peering lines hub↔spoke only |
| Azure Policy | Guardrails at the MG, not 200 copies | One assignment note: e.g. allowed locations |
| Identity | Entra + RBAC from Phase 7 | No landing zone is 'just a VNet' |

## Step-by-step lab

1. Read the Cloud Adoption Framework landing zone overview on Microsoft Learn (enterprise-scale / management groups / hub-spoke).
2. Sketch in docs/landing-zone-day87.md: management groups (Platform, Landing zones, Sandboxes), one hub, two spokes.
3. Label hub: connectivity, DNS, firewall. Label spokes: workloads. Label sandboxes: personal labs like azure-100.
4. Write one policy you would assign at Sandboxes (e.g. allowed locations = your lab region; deny public IP on non-lab).
5. Write one sentence: this is FICTION. You are not deploying ALZ Terraform/Bicep into the personal subscription today.
6. Optional: az account management-group list -o table on the personal tenant. Empty is a valid receipt.

## Done when

- [ ] CAF overview read
- [ ] Hub-spoke + MG sketch exists and is labeled FICTION
- [ ] One sandbox policy named
- [ ] Did not deploy enterprise-scale into the personal sub
- [ ] No logos, no employer org chart

## LinkedIn

Post draft: [`../../daily-guides/day-87.md`](../../daily-guides/day-87.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-87-azure-landing-zones
```

## Next

**Day 88** — GitOps with Flux or Argo CD — Git as desired state, not a kubectl petting zoo
