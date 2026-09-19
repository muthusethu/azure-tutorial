# Day 97 - Mock Interview Prep

| | |
|---|---|
| **Date** | 25 Nov 2026 |
| **Phase** | 10 - Portfolio & Public Launch |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Common Azure DevOps scenario questions

## Hands-on lab (20-30 min)

1. Answer out loud 5 questions; record yourself once
2. Topics: branching, YAML, secrets, rollback, DORA

## Commands / code

```bash
# Q: How do you promote the same artifact across envs?
# Q: Secret in a PR - what do you do?
# Q: Pipeline red on Friday 5pm - what's your playbook?
```

## LinkedIn post (copy-paste)

```
Interviews are pipelines for your career — rehearse the happy path and the failure path.

Day 97 of #100DaysOfAzureDevOps. Mock interview prep.

Common Azure DevOps scenario questions. Answer out loud. Record yourself once. It will be embarrassing in the App Insights sense — useful. I have bombed questions I could have built in a lab because I only ever typed, never spoke. Interviews are not a typing test. They are a pipeline: input question, stages of reasoning, an artifact called an answer, and a failure path when you do not know.

Topics: branching, YAML, secrets, rollback, DORA. Happy path and failure path. "I would look it up" is allowed if I then say where and what I would verify.

Patterns I keep seeing

1. Promote the same artifact
• How do you promote across envs?
• If my spoken answer rebuilds in prod, I go back to Day 39

2. Secret in a PR
• Rotate, purge from history if needed, treat the PR as an incident
• "Delete the line and merge" is the wrong failure path

3. Pipeline red on Friday 5pm
• Do not YOLO to prod to make the dashboard green
• Playbook: what is broken, who is affected, revert vs fix-forward with a clock

4. DORA without theater
• I can define the four metrics
• I will not invent a team's numbers I never measured

What I am doing in today's lab

I am answering five questions out loud and recording once: artifact promotion, secret in a PR, Friday red pipeline, branching, rollback. I will listen once. If I ramble, I write a 4-bullet version and say it again. Rehearsal is the lab.

Happy path and failure path. A career pipeline with only the happy path fails the first real run.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-97-mock-interview-prep

Tomorrow: Professional profile setup — policy first, draft offline.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 97 — Mock Interview Prep` (max 58 chars)
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
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 32 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 32 of 33 (rewrite with your real experience)
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

**Professional profile setup**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
