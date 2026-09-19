# Day 94 — GitHub Portfolio Setup

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 10 - Portfolio & Public Launch |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Pinned repos with vague names are closed blinds

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Pane | What goes on personal GitHub | What never ships |
| --- | --- | --- |
| Repo | Sanitized capstone + selected 100-day samples | Work tenant URLs, internal project names |
| README | Problem, Architecture, Pipelines, Security, Cost, License | Empty README or 'test' / 'new-folder' |
| Diagram | The four/six boxes from Days 91–93 | Employer network diagrams |
| How to run | Commands you clicked through as a stranger | Steps that require a secret you did not document as a placeholder |
| Pins | Capstone first; one or two supporting repos | Graveyard forks and untitled gists |
| License | MIT or another license you mean | Default leftover with no LICENSE |

## Step-by-step lab

1. Create or update a personal GitHub repo for the capstone. If history might contain secrets, start a clean public repo and copy sanitized files.
2. Write README sections: Problem | Architecture | Pipelines | Security | Cost notes | License | How to run.
3. Grep the tree for passwords, PATs, tenant IDs, and work hostnames. Remove them. Rotate anything that already leaked.
4. Add screenshots that show /health and a green pipeline with no email, no coworker, no work board.
5. Click through How to run once as if you were a stranger. If you get stuck, the README is wrong — fix it.
6. Pin the capstone on your personal GitHub profile. Unpin vague test repos or give them descriptions.
7. Cost note: SKUs used and what you already destroyed. No invented savings.

## Done when

- [ ] Sanitized capstone is on personal GitHub
- [ ] README has Problem, Architecture, Pipelines, Security, Cost, License, How to run
- [ ] You followed How to run once as a stranger
- [ ] No secrets, no employer screenshots
- [ ] Capstone is pinned; vague repos are unpinned or described

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-94-github-portfolio-setup
```

## Next

**Day 95** — Personal site or blog — translate the YAML into a story a non-terminal human can trust
