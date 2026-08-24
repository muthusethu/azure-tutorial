# Cross-platform publishing

Canonical source (always link back here):

https://github.com/muthusethu/azure-tutorial

**LinkedIn** remains the daily home base. **GitHub** is the canonical lab + PDF source. Other platforms amplify the same lesson — do **not** invent a second series voice.

**Separate track:** [#ProductionGradeAzure](./production-grade/) — every 3rd series day (4, 7, 10, … 100), publish a **second LinkedIn post** (production issues / fixes). Do **not** merge into the daily lesson. Morning reminder: `python scripts/production_reminder.py`.

## Platform status

| Platform | Status | Notes |
|----------|--------|--------|
| LinkedIn | **Active** | Daily post + PDF |
| GitHub | **Active** | `days/day-NN-*/` |
| X (Twitter) | **Paused** | `@ItsCloudhub_Tec` permanently read-only (appeal submitted / pending). Do **not** create a new X account to continue the series. Do not plan daily X threads until reinstated. |
| Threads | Optional later | Can reuse old X drafts if desired; not required |
| Dev.to / Hashnode | Optional 2–3× week | Set canonical URL → GitHub day folder |
| Medium / Reddit / IG / YouTube | Optional | Lower priority while LinkedIn streak runs |

## Rules (every platform)

- Educational only — no hiring CTAs, no “follow for tips” spam
- Personal learning series — views are your own
- Link GitHub day folder (or article canonical URL) when the platform allows links
- Same hashtag set **only on LinkedIn**: `#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic`
- Reddit: **zero hashtags**, zero “follow me”
- If X returns: post slowly, avoid link-heavy first tweets, no burst threads on day one

## Suggested cadence (do not burn out)

| When | Platforms |
|------|-----------|
| Daily ~10am | **LinkedIn** post 1 — #100DaysOfAzureDevOps (+ PDF document) |
| Every 3rd series day ~5–7pm | **LinkedIn** post 2 — [#ProductionGradeAzure](./production-grade/notes.md) (separate update) |
| Same week (optional) | **Dev.to** *or* **Hashnode** |
| 1× per week (optional) | **Medium** week recap |
| Only when standalone-useful | **Reddit** (r/AZURE, r/devops) — pure content |
| Paused | **X** |
| Optional later | Threads, Instagram, YouTube, Facebook groups |

## Folder layout

```text
publish/
  README.md
  day-01/ … day-NN/
    02-x-threads.md     ← kept for archive / if X is reinstated; not required daily
    LINKS.md
    …
```

## After you publish

Paste URLs into that day’s `LINKS.md` (LinkedIn + GitHub at minimum).
