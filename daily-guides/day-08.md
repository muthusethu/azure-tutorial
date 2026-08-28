# Day 8 — Azure Test Plans Basics

| | |
|---|---|
| **Date** | 28 Aug 2026 |
| **Phase** | 1 — Azure & DevOps Foundations |
| **Time box** | 60–90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Understand the structure of Azure Test Plans (Plans, Suites, Cases, Runs) and how manual/exploratory testing connects to Azure Boards work items. Publish Day 8 on LinkedIn with the PDF handout.

## Learn (20–30 min)

- Test Plans vs Test Suites vs Test Cases
- Suite types: Static, Requirement-based (linked to User Story), Query-based
- Manual & exploratory testing vs automated testing in CI pipelines
- End-to-end traceability: User Story → Test Case → Execution Run → Bug
- Docs: [Azure Test Plans overview](https://learn.microsoft.com/azure/devops/test/overview)

## Hands-on lab (20–30 min)

1. In `azure-100-labs`, open **Test Plans** (enable trial or basic access if prompted)
2. Create Test Plan: `Phase 1 Smoke Tests`
3. Add a Static Test Suite: `Portal & CLI Baseline`
4. Add 2 Test Cases with step-by-step actions and expected results:
   - `TC01: Verify Azure login and personal subscription directory`
   - `TC02: Verify resource group creation via Azure CLI`
5. Click **Run for web application** → execute steps → mark one **Passed**
6. Link one test case to a User Story in Boards to see traceability

## Commands / code

```bash
# Example Test Case steps to enter in the Test Case editor:

# Test Case 1: TC01 - Verify Azure login
# Step 1: Open terminal / Cloud Shell -> Action: Run 'az account show -o table'
#         Expected: Correct personal subscription ID and Tenant ID displayed
# Step 2: Open portal.azure.com -> Action: Check top right directory
#         Expected: Personal directory selected, no corporate tenant

# Test Case 2: TC02 - Verify CLI RG creation
# Step 1: Run 'az group create -n rg-testplan-lab -l centralindia'
#         Expected: ProvisioningState is 'Succeeded'
# Step 2: Run 'az group delete -n rg-testplan-lab --yes --no-wait'
#         Expected: Command returns without error
```

## LinkedIn post (copy-paste)

**Important:** After pasting into LinkedIn, press Enter between sections so line breaks stay visible.

```
Day 8 of #100DaysOfAzureDevOps

“We clicked around and it worked” is not a test strategy.
It is an anecdote.

Yesterday we organized our work on Azure Boards.
Today: how do you prove a feature actually works before users find the bugs?

Azure Test Plans.

In CI/CD, automated unit and integration tests run fast.
But manual testing, UAT, and exploratory verification often end up in messy Excel sheets or forgotten chat messages.

Azure Test Plans brings structure:

• Test Plan — the milestone or release goal (e.g. “Phase 1 Smoke”)
• Test Suite — logical group of test cases (Static, Requirement-based, Query-based)
• Test Case — explicit steps + expected results (reproducible by anyone)
• Test Runner — step-through UI to record Pass / Fail / Blocked and log bugs with attachments

The killer feature: Traceability.
When a test fails, the bug links directly to the Test Case, which links back to the User Story on Azure Boards.

No more “who tested what on which build?”

Lab today in azure-100-labs:
Created a Test Plan, added test cases with step-by-step actions, executed them in the web runner, and linked them to a User Story.

One-liner:
Automated tests verify what you expected.
Test Plans track what humans must prove.
Traceability connects both to the board.

Tomorrow: Azure Artifacts — package feeds and dependency management.

(Document attached: Day 8 Azure Test Plans handout PDF)

Lab notes + PDF also here:
https://bit.ly/4zHsGD3

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### Attach with the post (PDF handout)

Attach this document on LinkedIn (document / PDF upload):

- [`../days/day-08-azure-test-plans/handout.pdf`](../days/day-08-azure-test-plans/handout.pdf)

### How to post

1. LinkedIn → **document** → upload `days/day-08-azure-test-plans/handout.pdf`
2. Paste the text above (press **Enter** between sections so line breaks stay visible)
3. **Document title:** `Day 8 — Azure Test Plans Basics` (max 58 chars on LinkedIn)

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5–10 real comments on other Azure/DevOps posts.

## Done checklist

- [ ] Learned Test Plans vs Suites vs Cases vs Runs
- [ ] Created `Phase 1 Smoke Tests` plan in `azure-100-labs`
- [ ] Added 2 test cases with actions and expected results
- [ ] Executed a test run in the web runner
- [ ] Published LinkedIn post with PDF handout
- [ ] Engaged with 5–10 community comments

## Tomorrow

**Azure Artifacts**

---

*Personal learning guide — views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
