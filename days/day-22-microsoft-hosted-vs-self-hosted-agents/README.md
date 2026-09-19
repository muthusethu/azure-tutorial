# Day 22 — Microsoft-hosted vs Self-hosted Agents

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 3 - Continuous Integration |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Pick the agent like a capacity decision, not a personality trait

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Dimension | Microsoft-hosted | Self-hosted |
| --- | --- | --- |
| What it is | Microsoft-provided VM image for the job | A machine / scale set you operate |
| YAML | pool: vmImage: ubuntu-latest | pool: Default (named pool) |
| Images | ubuntu-latest, windows-latest, macOS SKUs with SDKs on the image | Whatever you installed. You own drift. |
| Patching / disk | Microsoft patches the VM. Workspace dies with the job | You patch OS, agents, AV, certs. Disk fills with leftover workspaces |
| Network | Public Microsoft IPs. No hop into your VNet unless you design for it | Can sit on a VNet / on-prem. Use when the job must reach private endpoints |
| Licensed tools | Public SDKs only. No ISV compiler that cannot leave the building | Install the licensed compiler, private NuGet, air-gapped feed |

## Step-by-step lab

1. Open Microsoft Learn: hosted vs self-hosted agents. Write three constraints that would force self-hosted (private network, licensed tool, policy). If you cannot name one, hosted stays the default.
2. Org settings → Agent pools. List every pool. Note Microsoft-hosted vs any Default / self-hosted pool. Screenshot nothing from an employer org.
3. Open yesterday's YAML (Day 21). Confirm pool: vmImage: ubuntu-latest. That is the rule for every remaining 100-day lab unless a private-network requirement appears.
4. In the last pipeline run, open the job log. Find the image name / hosted agent line. That receipt is how you prove hosted actually ran.
5. Write docs/agents-day22.md with: (1) the three constraints, (2) the pool list from this org, (3) the one-sentence rule you will follow for Days 23–100.
6. Do not install the agent on your laptop 'for practice'. That creates a 2am offline pool you now own.

## Done when

- [ ] Can explain hosted vs self-hosted without saying we wanted control
- [ ] Named at least one real constraint that would justify self-hosted — or wrote none yet
- [ ] YAML still uses vmImage: ubuntu-latest
- [ ] docs/agents-day22.md exists on the personal repo

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-22-microsoft-hosted-vs-self-hosted-agents
```

## Next

**Day 23** — YAML pipeline basics
