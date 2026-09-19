# Day 38 - Approval Gates & Environments

| | |
|---|---|
| **Date** | 27 Sep 2026 |
| **Phase** | 4 - Continuous Delivery |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Pre/post approvals, checks, environment resources

## Hands-on lab (20-30 min)

1. Add approval check on `prod` environment (you as approver)
2. Run pipeline; practice Approve / Reject

## Commands / code

```bash
# Pipelines -> Environments -> prod -> Checks -> Approvals
# Approvers: you (personal account)
```

## LinkedIn post (copy-paste)

```
Approvals are speed bumps before prod — annoying until the day they stop a 3am self-own.

Day 38 of #100DaysOfAzureDevOps. Approval gates and environments.

Nobody likes waiting on a checkbox. Everybody likes the checkbox after they almost deployed a debug flag to production because they reused the wrong variable group. I have been the person who hated gates and the person who was grateful a human had to click. After ten years, I will take the bump.

Azure DevOps environments can carry checks: pre-deployment approvals, post-deployment, business hours, whatever you configure. Today's lab is not a governance novel. It is environment prod, me as approver, one run where I Approve, one where I Reject, and a log that shows both.

What I keep seeing

1. Approvals belong on environments, not in chat
• Pipelines → Environments → prod → Checks → Approvals
• A Slack thumbs-up is not an audit trail

2. The approver should not be "whoever is awake"
• For the lab, the approver is my personal account
• In a real team, name a group, not a hero

3. Reject is a path you must practice
• If you only ever click Approve, you will freeze the first time you should not
• The pipeline should stop. That is success.

4. Gates are not a substitute for tests
• A human cannot eyeball a 200MB zip
• Approvals catch process mistakes; tests catch product mistakes

What I am doing in today's lab

I am adding an approval check on a prod environment with myself as approver, running the pipeline, practicing Approve once and Reject once, and keeping the run URLs. If Reject still deploys, the check is not attached to the job I think it is.

Annoying is the point. 3am you does not want a YOLO button.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-38-approval-gates-environments

Tomorrow: Multi-environment pipeline — Dev → Staging → Prod, same artifact.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 38 — Approval Gates & Environments` (max 58 chars)
3. Paste the text above (press **Enter** between sections so line breaks stay)

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5-10 real comments on other Azure/DevOps posts.

## Done checklist

- [ ] Learned the topic (docs or short video)
- [ ] Completed the lab steps
- [ ] Ran / saved the commands or code
- [ ] Published LinkedIn post
- [ ] Engaged with 5-10 community comments
- [ ] Deleted spare Azure resources if any (cost control)

## Tomorrow

**Multi-environment pipeline**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
