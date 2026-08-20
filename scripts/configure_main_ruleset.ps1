# Configure main-branch protection for azure-tutorial
#
# Desired policy:
# - Repo owner (@muthusethu / muthusethu2@gmail.com) can push directly to main (bypass)
# - Everyone else must open a PR
# - PRs need approval from @muthusethu (via Code Owners)
#
# Prerequisites:
#   1. Install GitHub CLI
#   2. Run: gh auth login
#      Sign in as the account that owns the email muthusethu2@gmail.com
#   3. From repo root: powershell -File scripts/configure_main_ruleset.ps1

$ErrorActionPreference = "Stop"
$gh = "$env:ProgramFiles\GitHub CLI\gh.exe"
if (-not (Test-Path $gh)) { $gh = "gh" }

$owner = "muthusethu"
$repo = "azure-tutorial"

Write-Host "Auth check..."
& $gh auth status
$userJson = & $gh api user | ConvertFrom-Json
Write-Host "Authenticated as: $($userJson.login) (id=$($userJson.id))"

if ($userJson.login -ne $owner) {
  Write-Warning "You are logged in as '$($userJson.login)', not '$owner'."
  Write-Warning "Bypass will still be granted to @$owner (repo owner). Continue only if intentional."
}

# List existing rulesets
$existing = & $gh api "repos/$owner/$repo/rulesets" | ConvertFrom-Json
$targetName = "Protect main - PR required"
$existingMatch = @($existing | Where-Object { $_.name -eq $targetName }) | Select-Object -First 1

# Repository role IDs for bypass (optional extras):
# 5 = Admin role on the repository (owner typically has this)
# Prefer explicit User bypass for the owner account.
$bodyObj = @{
  name        = $targetName
  target      = "branch"
  enforcement = "active"
  bypass_actors = @(
    @{
      actor_id    = [int]$userJson.id   # will replace with owner id below
      actor_type  = "User"
      bypass_mode = "always"            # allow direct pushes to main
    }
  )
  conditions = @{
    ref_name = @{
      include = @("refs/heads/main")
      exclude = @()
    }
  }
  rules = @(
    @{
      type = "pull_request"
      parameters = @{
        required_approving_review_count   = 1
        dismiss_stale_reviews_on_push     = $true
        require_code_owner_review         = $true
        require_last_push_approval        = $false
        required_review_thread_resolution = $false
      }
    }
    @{ type = "deletion" }
    @{
      type = "non_fast_forward"
    }
  )
}

# Resolve owner user id (muthusethu), not whatever machine account is logged in
$ownerJson = & $gh api "users/$owner" | ConvertFrom-Json
$bodyObj.bypass_actors[0].actor_id = [int]$ownerJson.id
Write-Host "Bypass actor: @$($ownerJson.login) id=$($ownerJson.id) (email on account should be muthusethu2@gmail.com)"

$tmp = Join-Path $env:TEMP "azure-tutorial-ruleset.json"
$bodyObj | ConvertTo-Json -Depth 8 | Set-Content -Path $tmp -Encoding utf8
Write-Host "Ruleset payload written to $tmp"

if ($existingMatch) {
  Write-Host "Updating existing ruleset id=$($existingMatch.id)..."
  & $gh api -X PUT "repos/$owner/$repo/rulesets/$($existingMatch.id)" --input $tmp
} else {
  Write-Host "Creating new ruleset..."
  & $gh api -X POST "repos/$owner/$repo/rulesets" --input $tmp
}

Write-Host ""
Write-Host "Done. Verify in UI:"
Write-Host "https://github.com/$owner/$repo/settings/rules"
Write-Host "Also ensure .github/CODEOWNERS contains: * @$owner"
