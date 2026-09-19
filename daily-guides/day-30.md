# Day 30 - Mini Project + Recap (Phase 3)

| | |
|---|---|
| **Date** | 19 Sep 2026 |
| **Phase** | 3 - Continuous Integration |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- CI for multi-language sample OR one solid language + stub others

## Hands-on lab (20-30 min)

1. Pick your primary stack; green build on main
2. Recap post: YAML anatomy + one war story from today

## Commands / code

```bash
# Keep pipelines/ under repo; badge optional later
# Goal: one green CI run you can screenshot (no secrets in screenshot)
```

## LinkedIn post (copy-paste)

```
Phase 3 recap: CI is a seatbelt you wear before the crash, not after.

Day 30 of #100DaysOfAzureDevOps. Mini project and recap for Phase 3 — Continuous Integration.

Nine days of agents, YAML, .NET, Node, Python, Maven, matrix, and secrets. The point was not to become four ecosystems in a week. The point was to feel the same spine in every language: restore or install, build, test, publish an artifact, keep secrets out of the file.

I have been in delivery long enough to know the crash is not theoretical. A merge on Friday, a missing test, a hosted agent that drifted. CI is the seatbelt. Putting it on after the incident is a blog post, not a practice.

What Phase 3 actually taught me to keep

1. YAML anatomy I can draw from memory
• trigger / pr → stages → jobs → pool → steps
• If I cannot sketch it, I copied it

2. One primary stack, stubs for the rest
• Pick .NET or Node or Python as the real green build
• The other languages can stay samples; depth beats a graveyard of half pipelines

3. Artifacts are the handoff
• CI produces a drop; CD should not rebuild
• A screenshot of a green run is allowed; a screenshot of a secret is not

4. Secrets stay in groups
• No passwords in azure-pipelines.yml
• That rule survives every phase after this

What I am doing in today's lab

I am picking my primary stack, getting a green build on main, saving a screenshot with no secrets, and writing a short recap: YAML anatomy plus one war story from this week (a cache miss, a skipped test, a secret that almost got echoed). Pipelines live under /pipelines.

Wear the seatbelt on the first commit you care about. Phase 3 is that commit, repeated until it is boring.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-30-mini-project-recap-phase-3

Tomorrow: Release pipelines overview — Classic vs YAML CD, and an environment named dev.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 30 — Phase 3 Mini Project & Recap` (max 58 chars)
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

**Release pipelines overview**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
