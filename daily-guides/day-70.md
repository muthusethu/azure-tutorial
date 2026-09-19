# Day 70 - Mini Project + Recap (Phase 7)

| | |
|---|---|
| **Date** | 29 Oct 2026 |
| **Phase** | 7 - Security, Compliance & Governance |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Secure pipeline with Key Vault + a policy

## Hands-on lab (20-30 min)

1. One demo pipeline fetching a secret; RG tag policy on
2. Recap

## Commands / code

```bash
# Done = secret not in YAML; policy visible; approvals on
```

## LinkedIn post (copy-paste)

```
Phase 7 recap: speed without security is just a faster incident.

Day 70 of #100DaysOfAzureDevOps. Mini project and recap for Phase 7 — security, compliance, and governance.

Entra, RBAC, service connections, Key Vault, pipeline fetch, Policy, scanning, shift-left, boring pipeline design. The mini project is one demo pipeline that fetches a secret, a tag policy that is actually assigned, and approvals on. Secret not in YAML.

I can ship faster by skipping all of it. I have seen that speed. It arrives at an incident with better velocity metrics.

What I am keeping from Phase 7

1. Identity, then RBAC, then secrets
• Bouncer list, scoped badges, hotel safe
• Skipping to Key Vault with Owner SPNs is cosplay

2. Policy is the tag adult
• Visible on the compliance blade
• Not a PDF of good intentions

3. Security stage before Deploy
• Fail criteria written
• No continueOnError confession

4. Definition of done
• Secret not in YAML; policy visible; approvals on
• Screenshot without secret values

What I am doing in today's lab

I am wiring one demo pipeline that fetches DemoSecret, confirming the RG tag policy is on, keeping prod approval, and writing the recap. If any secret printed this week, I rotate the dummy and fix the step. Speed is allowed. Unauthenticated speed is not a flex. The screenshot still shows asterisks, not letters. Policy blade still shows the assignment.

Faster incidents are still incidents. Phase 7 is the brakes that let Phase 4 go fast without lying. Wear them before you enjoy the velocity.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-70-mini-project-recap-phase-7

Tomorrow: Azure Monitor fundamentals — flashlight, not the fix.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 70 — Phase 7 Mini Project & Recap` (max 58 chars)
3. Paste the text above (press **Enter** between sections so line breaks stay)

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5-10 real comments on other Azure/DevOps posts.

## Reminder — 2nd LinkedIn post (production track)

**Today you publish TWO separate LinkedIn posts.** The daily lesson above is post 1 only.

| | Post 1 — #100DaysOfAzureDevOps | Post 2 — #ProductionGradeAzure |
|---|-------------------------------|----------------------------------|
| **When** | ~10:00 IST | ~17:00–19:00 IST (after some engagement on post 1) |
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 23 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 23 of 33 (rewrite with your real experience)
- [ ] Record URLs in [`publish/production-grade/LINKS.md`](../publish/production-grade/LINKS.md)

Run: `python scripts/production_reminder.py`

## Done checklist

- [ ] Learned the topic (docs or short video)
- [ ] Completed the lab steps
- [ ] Ran / saved the commands or code
- [ ] Published LinkedIn post
- [ ] Engaged with 5-10 community comments
- [ ] Deleted spare Azure resources if any (cost control)

## Tomorrow

**Azure Monitor fundamentals**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
