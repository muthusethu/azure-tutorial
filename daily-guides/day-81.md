# Day 81 - Multi-repo & Monorepo Strategies

| | |
|---|---|
| **Date** | 09 Nov 2026 |
| **Phase** | 9 - Advanced & Enterprise |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Trade-offs; pipeline design

## Hands-on lab (20-30 min)

1. Write ADR: this lab stays monorepo for samples
2. List when you would split repos for a client

## Commands / code

```bash
# Monorepo: shared pipelines, atomic PRs
# Multi-repo: clear ownership, harder cross-cutting changes
```

## LinkedIn post (copy-paste)

```
Repo strategy is politics with folders — pick the drama you can afford.

Day 81 of #100DaysOfAzureDevOps. Multi-repo and monorepo strategies.

A monorepo is atomic PRs and shared pipelines. Multi-repo is clear ownership and a harder time changing a cross-cutting concern. I have lived in both. Both have politics. Folders are just how the politics render.

This lab stays a monorepo for samples — that is an ADR, not a religion. I will list when I would split repos for a real product: different lifecycles, different access, a library consumed by many. I will not list fake clients.

Patterns I keep seeing

1. Monorepo strengths
• One PR can change API and pipeline together
• Templates live next to consumers

2. Multi-repo strengths
• Permissions and release cadence can differ
• A noisy app does not rebuild a quiet library by accident — if you designed it that way

3. The cost is coordination
• Monorepo: CI graph and PATH discipline
• Multi-repo: versioning and "which commit is prod" meetings

4. Write the ADR
• this lab stays monorepo for samples
• Split when ownership or lifecycle actually splits — not when a blog post is trending

What I am doing in today's lab

I am writing an ADR that this 100-day repo stays monorepo, plus a short list of when I would split: different lifecycles, different access, a library consumed by many. No company names. Drama I can afford: one repo, many /src samples, pipelines that path-filter so a Node change does not rebuild .NET.

Pick the folder politics on purpose. Defaulting to ten repos is not enterprise. It is scatter.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-81-multi-repo-monorepo-strategies

Tomorrow: Pipeline templates — extract templates/build.yml and reuse it.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 81 — Multi-repo & Monorepo` (max 58 chars)
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

**Pipeline templates**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
