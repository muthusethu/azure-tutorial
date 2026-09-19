# Day 60 — Mini Project + Recap (Phase 6)

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 6 - Containers & Kubernetes |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Package once, run on one path you can pay for and tear down — slogans do not get invoices

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Stage | Object | Done looks like |
| --- | --- | --- |
| Pack | Dockerfile + layer cache + digest | Image builds locally and in CI |
| Store | ACR repository, tag = Build.BuildId | Not Hub; not latest-as-identity |
| Publish | Docker@2 on ubuntu-latest | Laptop is not the publisher |
| Run (pick one) | ACI or Container Apps or AKS+Helm/manifests | Pipeline applied it; Git knows the tag |
| Stop | Delete ACI group / CA app / AKS | Cost Analysis does not include a forgotten gym |

## Step-by-step lab

1. Confirm the pipeline still builds and pushes myapp:$(Build.BuildId) to ACR. Copy the digest into the recap doc.
2. Choose one run path: ACI, Container Apps, or AKS (manifests or Helm). Automate it from the pipeline or a documented CLI that uses the build tag. Not three paths.
3. Prove the running bits equal that digest/tag. If you skipped Azure runtime, prove kind ran the same tag and say so — skipping AKS is an architecture decision.
4. Tear down the run path: delete ACI/CA/AKS leftovers from Days 54–59. Empty RGs or document why ACR stays for Phase 7.
5. Write docs/phase6-recap.md: architecture one-liner, the path you picked, destroy receipts, kube-system vs workloads in one sentence.
6. LinkedIn recap from the personal account. No employer cluster diagrams. No buffet of half-finished runtimes.

## Done when

- [ ] Image in ACR tagged with a build id, digest recorded
- [ ] Exactly one automated deploy path proved
- [ ] Paid runtimes from this phase deleted or dated
- [ ] docs/phase6-recap.md has the architecture one-liner

## LinkedIn

Post draft: [`../../daily-guides/day-60.md`](../../daily-guides/day-60.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-60-mini-project-recap-phase-6
```

## Next

**Day 61** — Entra ID fundamentals — the bouncer list every other control assumes
