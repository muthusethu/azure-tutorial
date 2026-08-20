# Main branch policy (target)

## Goal

| Who | Can do |
|-----|--------|
| **Repo owner** (`muthusethu2@gmail.com` → GitHub user `@muthusethu`) | Push **directly** to `main` (bypass) |
| **Everyone else** | Must open a **Pull Request** to `main` |
| **PR merge** | Needs **approval from `@muthusethu`** (Code Owners) |

GitHub rules use **usernames**, not email addresses. Confirm in GitHub → Settings → Emails that `muthusethu2@gmail.com` belongs to `@muthusethu`.

## One-time setup (UI)

1. Open: https://github.com/muthusethu/azure-tutorial/settings/rules  
2. **New ruleset** → **New branch ruleset**  
3. Name: `Protect main - PR required`  
4. Enforcement: **Active**  
5. Target branches → **Include by pattern** → `main`  
6. **Bypass list**  
   - Add **`muthusethu`** (your owner account)  
   - Bypass mode: **Always** (allows direct push to `main`)  
   - Do **not** add other users  
7. Rules → enable **Restrict deletions**  
8. Rules → enable **Block force pushes**  
9. Rules → enable **Require a pull request before merging**  
   - Required approvals: **1**  
   - Enable **Require review from Code Owners**  
   - Enable **Dismiss stale pull request approvals when new commits are pushed**  
10. Save  

## Code Owners (required for “approved by owner”)

File: [`.github/CODEOWNERS`](../.github/CODEOWNERS)

```text
* @muthusethu
```

With “Require review from Code Owners”, other contributors’ PRs need your approval before merge.

## Automated setup (optional)

```powershell
gh auth login
# sign in as @muthusethu (muthusethu2@gmail.com)
powershell -File scripts/configure_main_ruleset.ps1
```

## How to verify

| Test | Expected |
|------|----------|
| Owner pushes to `main` | Allowed (may show “Bypassed rule violations”) |
| Another user pushes to `main` | **Rejected** — must use a PR |
| Another user opens PR | Merge blocked until `@muthusethu` approves |

## Notes

- Collaborators with **Admin** on the repo can often bypass unless you avoid granting Admin. Prefer **Write** for contributors.  
- Your laptop git email (`muthukumar.m@itscloudhub.com`) does not control bypass — the **logged-in GitHub account** that performs the push does.
