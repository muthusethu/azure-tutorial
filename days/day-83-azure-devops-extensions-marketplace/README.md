# Day 83 — Azure DevOps Extensions & Marketplace

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 9 - Advanced & Enterprise |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

A pinch helps; a handful ruins the stew and the security review

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Source | Trust default | Check before install |
| --- | --- | --- |
| Built-in tasks | Prefer for every 100-day lab | script, DotNetCoreCLI, PublishBuildArtifacts, Docker |
| Microsoft-published extension | OK if the task is not already built-in | Publisher = Microsoft, last update, scopes |
| Known OSS publisher | Maybe — treat as supply chain | Repo, last release, permissions on install |
| Unknown publisher | No for labs | Wide org scopes + years of silence |
| Custom private extension | Out of scope for this series | Do not sideload a .vsix you cannot explain |

## Step-by-step lab

1. Org settings → Extensions (or Marketplace from the personal org). List what is already installed. Screenshot nothing from a work org.
2. Browse Marketplace for one task you actually need (or confirm you need none). Record publisher, last update, and requested scopes.
3. If publisher/scopes/update are defensible, install that one extension in the personal org. Otherwise install zero.
4. Write docs/marketplace-day83.md: the one extension and why, or 'zero — built-in tasks cover the lab' plus the scopes you refused.
5. Open a pipeline YAML and confirm it does not reference a mystery task name you cannot map to a publisher.
6. Do not sprinkle Replace Tokens / Slack / extra scanners onto a hello pipeline just to look enterprise.

## Done when

- [ ] Either one defensible install or a written zero
- [ ] Publisher, last update, and scopes recorded
- [ ] docs/marketplace-day83.md exists
- [ ] No work-org Marketplace screenshot
- [ ] Posted the LinkedIn document

## LinkedIn

Post draft: [`../../daily-guides/day-83.md`](../../daily-guides/day-83.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-83-azure-devops-extensions-marketplace
```

## Next

**Day 84** — Jenkins to Azure Pipelines — migrate guarantees, not the blue ball
