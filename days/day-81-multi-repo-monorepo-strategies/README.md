# Day 81 — Multi-repo & Monorepo Strategies

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 9 - Advanced & Enterprise |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Repo strategy is politics with folders — pick the drama you can afford

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Dimension | Monorepo | Multi-repo |
| --- | --- | --- |
| Atomic change | One PR can move API + pipeline + infra together | Cross-repo PRs and version pins |
| Ownership | PATH / CODEOWNERS / folder reviews | Repo permissions and separate service connections |
| CI graph | Path filters or you rebuild the world | Per-repo pipeline; 'which commit is prod' meetings |
| Templates | templates/ sits next to consumers | Template repo + refs; version lag |
| This 100-day lab | Default: one repo, many /src samples | Split only for a written lifecycle/access reason |

## Step-by-step lab

1. Read your current repo layout (folders, pipelines). You are documenting reality, not a dream org chart.
2. Write docs/adr-repo-strategy.md: Decision = this lab stays a monorepo for samples. Status = accepted.
3. Add a short 'we would split when' list: different lifecycle, different access, a library consumed as a versioned package. No company names.
4. If you have two sample apps, add a path filter on one pipeline so a change under src/a does not build src/b.
5. Note the coordination cost you chose: monorepo CI graph vs multi-repo version meetings.
6. Commit the ADR. Drama you can afford: one repo, path filters, templates next to consumers.

## Done when

- [ ] ADR says the 100-day repo stays monorepo, with split criteria that are constraints not logos
- [ ] Path filter exists or you wrote why a single sample does not need one
- [ ] No employer repo diagram
- [ ] docs/adr-repo-strategy.md committed
- [ ] Posted the LinkedIn document

## LinkedIn

Post draft: [`../../daily-guides/day-81.md`](../../daily-guides/day-81.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-81-multi-repo-monorepo-strategies
```

## Next

**Day 82** — Pipeline templates — extract templates/build.yml so you stop inventing a 15th way to be broken
