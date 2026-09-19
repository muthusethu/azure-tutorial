# Day 22 - Microsoft-hosted vs Self-hosted Agents

| | |
|---|---|
| **Date** | 11 Sep 2026 |
| **Phase** | 3 - Continuous Integration |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- When to self-host
- Scale sets, capabilities, trade-offs

## Hands-on lab (20-30 min)

1. Compare hosted vs self-hosted in docs
2. List agent pools in org settings
3. Decide: hosted for all 100-day labs unless you need private network

## Commands / code

```bash
# Prefer for labs:
pool:
  vmImage: ubuntu-latest
# Self-hosted later when you need VPN / licensed software
```

## LinkedIn post (copy-paste)

```
Hosted agents are Uber; self-hosted is owning the car — insurance and parking included.

Day 22 of #100DaysOfAzureDevOps. Microsoft-hosted vs self-hosted agents.

After about a decade in infrastructure and delivery, the agent question still arrives in week one of any pipeline design. Not because people romanticize VMs. Because a licensed compiler, a private network hop, or a policy that says binaries cannot leave the building shows up and suddenly ubuntu-latest feels naive.

I have watched teams default to self-hosted for "control" and then spend nights patching agents, chasing disk filled with leftover workspaces, and explaining why the pool is offline. I have also watched teams stay on Microsoft-hosted until a job needed a VPN that hosted agents will never have. Both choices are valid. Pretending they cost the same is not.

Patterns I keep seeing after a decade in delivery

1. Hosted should stay the default until a constraint appears
• ubuntu-latest, windows-latest, macOS images with SDKs already on them
• Microsoft patches the VM; you pay in minutes, not in patch Tuesday
• Fine for public SaaS builds and for every remaining lab in this 100-day series unless the job needs a private network

2. Self-hosted is a product you now operate
• Scale sets, capabilities, agent version drift, antivirus, certificates
• You own the 2am "agent is offline" ticket
• Worth it for on-prem artifact feeds, licensed ISV tools, or VNet-only endpoints

3. Capabilities versus folklore pool names
• A job that demands a capability nobody registered will queue forever
• Pool sprawl is how "the Java agent" becomes tribal knowledge instead of YAML

4. Parallelism is two bills, not one
• Hosted: Microsoft-hosted minutes and parallel-job SKUs
• Self-hosted: you still need a parallel job in Azure DevOps; the VM bill is extra

What I am doing in today's lab

I am comparing hosted vs self-hosted in the docs, listing agent pools under org settings, and writing the rule I will actually follow: Microsoft-hosted ubuntu-latest for all remaining 100-day labs unless I hit a private-network requirement. The YAML stays pool: vmImage: ubuntu-latest.

Pick hosted until a concrete constraint forces you off it. Owning the car is not a personality trait.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-22-microsoft-hosted-vs-self-hosted-agents

Tomorrow: YAML pipeline basics — triggers, stages, jobs, steps, and a PR trigger I can actually read in the logs.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 22 — Hosted vs Self-hosted Agents` (max 58 chars)
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
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note 7 |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note 7 of 33 (rewrite with your real experience)
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

**YAML pipeline basics**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
