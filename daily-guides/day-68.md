# Day 68 - DevSecOps - Shift-left Security

| | |
|---|---|
| **Date** | 27 Oct 2026 |
| **Phase** | 7 - Security, Compliance & Governance |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Embed gates early

## Hands-on lab (20-30 min)

1. Add a pipeline stage `Security` before `Deploy`
2. Document fail criteria

## Commands / code

```bash
stages: [Build, Security, Deploy]
# Security job exits non-zero on critical CVEs
```

## LinkedIn post (copy-paste)

```
Day 68 of #100DaysOfAzureDevOps

Security as a final boss stage is how you ship late - put checks next to the commit

Today's topic: **DevSecOps - Shift-left Security**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Secure pipeline design.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### Posting tips

- Publish from your **personal** account, outside work hours (morning IST works well).
- No employer name, no client details, no "DM me for freelance".
- After posting: leave 5-10 real comments on other Azure/DevOps posts.

## Done checklist

- [ ] Learned the topic (docs or short video)
- [ ] Completed the lab steps
- [ ] Ran / saved the commands or code
- [ ] Published LinkedIn post
- [ ] Engaged with 5-10 community comments
- [ ] Deleted spare Azure resources if any (cost control)

## Tomorrow

**Secure pipeline design**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
