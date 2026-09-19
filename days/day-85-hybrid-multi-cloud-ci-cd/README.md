# Day 85 — Hybrid & Multi-cloud CI/CD

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 9 - Advanced & Enterprise |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Insurance is priced — buy it for a constraint, not a slide

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Layer | Azure-only (this series) | Hybrid / extra cloud |
| --- | --- | --- |
| Build | Azure Pipelines + ubuntu-latest | Still build once; artifact/image is the passport |
| Identity | Workload identity / service connection to Azure | Second cloud IAM + a second secret envelope |
| Secrets | Key Vault + variable group | Copied cloud keys = two postcards to lose |
| Network | Public Microsoft-hosted is enough for labs | Self-hosted pool / VPN / private endpoint for on-prem |
| Deploy task | AzureWebApp / AzureContainerApps / az | Cloud-specific task only if a real second target exists |

## Step-by-step lab

1. Write docs/multicloud-risks-day85.md with three sections: secrets, identity, network. Each section gets one real failure mode.
2. Write the series rule in that file: one cloud deep for Days 1–100 unless a named constraint appears.
3. Sketch 'build once in Azure DevOps → deploy with a cloud-specific task' as a four-box diagram. The artifact is the passport.
4. List why a Microsoft-hosted agent cannot see an on-prem feed (Day 22). Hybrid is often a network hop, not a second logo.
5. Do not create AWS/GCP resources 'to try' unless the personal account and destroy command are already ready. If you skip, write 'did not deploy'.
6. No employer multi-cloud diagram and no invented customer estate.

## Done when

- [ ] Risks one-pager covers secrets, identity, and network
- [ ] Series rule written: one cloud deep
- [ ] Did not open a second cloud 'for the slide' (or destroyed it the same night)
- [ ] No employer estate diagram
- [ ] Posted the LinkedIn document

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-85-hybrid-multi-cloud-ci-cd
```

## Next

**Day 86** — Disaster recovery and backup — RPO/RTO as sentences, and a restore that is not fan fiction
