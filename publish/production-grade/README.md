# Production Grade Azure

**Separate LinkedIn track** — runs on the **same calendar** as [#100DaysOfAzureDevOps](../../README.md) but does **not** change the daily lesson posts.

## What this is

| | Daily lesson | This track |
|---|--------------|------------|
| **Series** | `#100DaysOfAzureDevOps` | `#ProductionGradeAzure` |
| **Cadence** | Every day (100 posts) | Every **3rd series day** (33 posts) |
| **Content** | Learn + lab + PDF handout | Production issue → what broke → fix → best practice |
| **Voice** | Learning in public | ~10 years in production (anonymized) |
| **LinkedIn** | **One post per day** | **Second post** on field-note days only |

**Field-note days:** 4, 7, 10, 13, … 100.

## Two posts on field-note days

| Post | When (IST) | Source |
|------|------------|--------|
| **1 — Daily lesson** | ~10:00 | `daily-guides/day-NN.md` (+ PDF in `days/` when ready) |
| **2 — Production note** | ~17:00–19:00 | [`notes.md`](./notes.md) |

Do **not** merge them into one post.

## Hashtags (production track only)

`#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic`

Do **not** use `#100DaysOfAzureDevOps` on production posts (keeps the tracks distinct).

## Before you post

- Rewrite every draft with **your** real incident (composite/anonymized is fine).
- No employer name, client name, internal URLs, or live secrets.
- After posting, paste URLs into [`LINKS.md`](./LINKS.md).

## Reminders

1. **Each morning:** `python scripts/production_reminder.py`
2. **Checklist calendar:** [`REMINDERS.md`](./REMINDERS.md)
3. **On field-note days:** yellow reminder block at the bottom of that day’s `daily-guides/day-NN.md`

## Files

| File | Purpose |
|------|---------|
| [`notes.md`](./notes.md) | Copy-paste LinkedIn text — notes 1–33 |
| [`REMINDERS.md`](./REMINDERS.md) | Dates + checkboxes |
| [`LINKS.md`](./LINKS.md) | Published LinkedIn URLs |
