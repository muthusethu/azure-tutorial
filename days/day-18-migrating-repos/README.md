# Day 18 — Migrating Repos to Azure Repos

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 2 - Azure Repos & Git Mastery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Moving apartments — bring the furniture (history), leave the broken IKEA (secrets)

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Path | What is preserved | Lab choice |
| --- | --- | --- |
| ADO Import (Repos → Import) | Git history from a public URL you can reach | Small public GitHub sample |
| git clone --bare + push --mirror | All refs: branches, tags | When Import UI cannot see the source |
| git remote add + push --all --tags | Named branches you pick | When you do not want every junk ref |
| TFVC import | Changesets → Git (lossy-ish) | Mention only — stay on Git |
| ZIP upload | One tree, no history | Not a migration |
| LFS objects | Pointers unless LFS migrated | Skip LFS for this lab sample |

## Step-by-step lab

1. Repos → New repository → Name imported-sample → do NOT add a README (empty, ready for import).
2. Option A: imported-sample → Import → paste a SMALL public GitHub URL you own or a well-known tiny sample. Import.
3. Option B (if Import fails): git clone --bare https://github.com/<user>/<small-repo>.git then git push --mirror https://dev.azure.com/<org>/azure-100-labs/_git/imported-sample
4. Clone imported-sample locally. git log --oneline -10. Confirm old commits (dates/messages) survived.
5. Repos → Branches: set default to main if the source used main; if only master exists, leave it or rename.
6. Search the tree for .env, id_rsa, nuget.config with keys. If found, document in notes — do not push fixes to a work repo.
7. Write docs/migration-day18.md in azure-100-labs (the main repo): which option you used and that git log still shows history.

## Done when

- [ ] imported-sample exists in the personal project
- [ ] git log shows commits from before the import
- [ ] Did not import employer / private work history
- [ ] Documented Import UI vs --mirror in the main lab repo

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-18-migrating-repos
```

## Next

**Day 19** — Repo security
