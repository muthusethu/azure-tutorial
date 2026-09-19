# Day 17 — Fork Workflows & Repo Permissions

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 2 - Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Permissions are seatbelts — annoying until someone force-pushes main into the sun

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Identity | Typical Git rights | Lab setting |
| --- | --- | --- |
| Project Collection Admin | Bypass almost everything | You only |
| Project Administrators | Repo create/delete, security | You |
| Contributors | Contribute (push to non-protected), PR | Default if a friend joins |
| Readers | Clone / pull | No push |
| <Repo> Bypass policies | Push to main ignoring PR | Deny for Contributors |
| Force push (rewrite) | git push --force on that ref | Deny on main for everyone but you-as-breakglass |

## Step-by-step lab

1. Project settings → Repositories → select azure-100-labs → Security.
2. Select Contributors. Find Force push. Set Deny (or confirm inherited Deny) for this repo / refs/heads/main if scoped.
3. Find Bypass policies when pushing / Bypass policies when completing pull requests. Deny for Contributors.
4. Confirm your user (as Project Admin) still can administer. Do not add a work AAD group.
5. Write docs/repo-permissions-day17.md: Contributors may contribute via PR; cannot force-push main; cannot bypass policies.
6. Optional: GitHub → new private repo → add remote github and push notes only. Never mirror a work repository.
7. Commit the markdown on feature/day17-permissions and open a PR. Do not screenshot employer orgs.

## Done when

- [ ] Can explain fork workflow vs in-repo feature branches
- [ ] Contributors cannot force-push main (Deny)
- [ ] Bypass policies denied for Contributors
- [ ] docs/repo-permissions-day17.md committed on the personal repo

## LinkedIn

Post draft: [`../../daily-guides/day-17.md`](../../daily-guides/day-17.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-17-fork-permissions
```

## Next

**Day 18** — Migrating repos to Azure Repos
