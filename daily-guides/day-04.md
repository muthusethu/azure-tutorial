# Day 4 — DevOps Principles & Culture

| | |
|---|---|
| **Date** | 24 Aug 2026 |
| **Phase** | 1 — Azure & DevOps Foundations |
| **Time box** | 60–90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Understand CALMS and DORA well enough to explain them without a slide deck. Publish **Day 4 lesson only** on LinkedIn (production track is a **separate second post** today — see reminder below). No Azure spend today.

## Learn (20–30 min)

- CALMS: Culture, Automation, Lean, Measurement, Sharing
- DevOps lifecycle vs Agile (complement, not replace)
- DORA metrics: deployment frequency, lead time for changes, change failure rate, time to restore
- Article: [Using the four keys to measure DevOps performance](https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance)

## Hands-on lab (20–30 min)

1. Score your last team (or this 100-day project) 1–5 on each CALMS letter. Be honest.
2. Pick **one** DORA metric you could measure on a personal lab later (even “deploys per week to a throwaway App Service”).
3. Write three sentences: what “good” would look like for that metric in six months.

## Commands / code

```bash
# Optional personal scorecard (fill honestly 1-5)
# Culture: _
# Automation: _
# Lean: _
# Measurement: _
# Sharing: _
#
# DORA metric I will try to measure: _
```

## LinkedIn post (copy-paste)

**Important:** After pasting into LinkedIn, press Enter between sections so line breaks stay visible.

This is **post 1 of 2 today**. Do not paste the production story here — that is a separate update ([Note 1](../publish/production-grade/notes.md)).

```
Day 4 of #100DaysOfAzureDevOps

Yesterday: ARM — the head office behind every Azure click.

Today: the word everyone puts on their laptop sticker.

DevOps.

DevOps is not a job title.
It is whether your team can change software without a fire drill.

CALMS is the checklist people skip:

• Culture — blame the process, not the person on the keyboard
• Automation — if you do it twice, script it
• Lean — smaller batches, less WIP, less “big bang Friday”
• Measurement — numbers beat vibes
• Sharing — runbooks and postmortems beat tribal knowledge

If any one letter is fake, the rest is theatre.

DORA is how you catch the theatre — four questions:

• How often do you ship? (deployment frequency)
• How long from commit to production? (lead time)
• How often does a release hurt users? (change failure rate)
• How fast do you recover? (time to restore)

You can own Azure Pipelines, run stand-ups, freeze every Friday —
and still score low on DORA.

Tools do not raise DORA. Habits do.

Lab today: scored myself honestly on CALMS (1–5 each letter)
and picked one DORA metric I can actually measure on a personal project —
not vibes. A number.

One-liner:

CALMS = what good feels like.
DORA = how you prove it.
A sticker = optional.

Tomorrow: Azure DevOps Services —
Boards, Repos, Pipelines, Test Plans, Artifacts — five hubs, one roof.

(Document attached: Day 4 CALMS + DORA handout PDF)

Lab notes + PDF also here:
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-04-devops-principles

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### Attach with the post (PDF handout)

Attach this document on LinkedIn (document / PDF upload):

- [`../days/day-04-devops-principles/handout.pdf`](../days/day-04-devops-principles/handout.pdf)

**How to post on LinkedIn:** Start a post → **document** icon → upload `handout.pdf` → paste the text above → title e.g. `Day 4 — DevOps Principles (CALMS + DORA)`.

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no hiring CTAs.
- After posting: leave 5–10 real comments on other Azure/DevOps posts.

## Reminder — 2nd LinkedIn post (production track)

**Today you publish TWO separate LinkedIn posts.** The daily lesson above is post 1 only.

| | Post 1 — #100DaysOfAzureDevOps | Post 2 — #ProductionGradeAzure |
|---|-------------------------------|----------------------------------|
| **When** | ~10:00 IST | ~17:00–19:00 IST (after some engagement on post 1) |
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 1 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 1 of 33 (rewrite with your real experience)
- [ ] Record URLs in [`publish/production-grade/LINKS.md`](../publish/production-grade/LINKS.md)

Run: `python scripts/production_reminder.py`


## Done checklist

- [ ] Learned CALMS + DORA
- [ ] Filled the 1–5 scorecard
- [ ] Published LinkedIn post 1 — daily lesson (line breaks kept)
- [ ] Published LinkedIn post 2 — production note (separate post)
- [ ] Engaged with 5–10 community comments

## Tomorrow

**Azure DevOps Services overview**

---

*Personal learning guide — views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
