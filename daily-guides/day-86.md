# Day 86 - Disaster Recovery & Backup

| | |
|---|---|
| **Date** | 14 Nov 2026 |
| **Phase** | 9 - Advanced & Enterprise |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Backup policies, geo-redundancy, drills

## Hands-on lab (20-30 min)

1. Enable soft delete on Key Vault if not on
2. Document RPO/RTO targets for your lab app (even if fictional)

## Commands / code

```bash
# RPO: how much data loss OK?
# RTO: how fast back online?
# Drill: restore once or it is fiction
```

## LinkedIn post (copy-paste)

```
Backups you never restore are fan fiction.

Day 86 of #100DaysOfAzureDevOps. Disaster recovery and backup.

Backup policies, geo-redundancy, drills. RPO: how much data loss is OK? RTO: how fast back online? I have read beautiful backup policies that had never been restored. Fan fiction. The first restore in anger is how you learn the password was wrong and the vault was in the same region as the fire.

Enable soft delete on Key Vault if it is not on. Document RPO/RTO for the lab app even if the numbers are fictional targets — labeled as targets, not as achievements. A drill: restore once or it is fiction.

What I keep seeing

1. RPO and RTO are product sentences
• Write them for the lab app
• "Zero / instant" is usually a wish, not a design

2. Soft delete is a cheap drill ingredient
• Key Vault soft delete on
• I can delete a dummy secret and recover it — a restore with training wheels

3. Geo is not a checkbox religion
• GRS/GZRS cost money and complexity
• Same-region backup is not DR. It is a nicer disk failure story

4. Drills write the real RTO
• Time the restore once
• A number I did not measure will not be posted as a fact

What I am doing in today's lab

I am turning on Key Vault soft delete if needed, writing RPO/RTO targets for the lab app (clearly as targets), and doing one tiny restore drill (secret recovery or a documented "I restored X"). If I cannot restore today, I write that the DR plan is still fiction.

Restore or it is a story. Fan fiction does not bring the app back.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-86-disaster-recovery-backup

Tomorrow: Azure Landing Zones — city planning, hub-spoke on paper.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 86 — Disaster Recovery & Backup` (max 58 chars)
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

**Azure Landing Zones**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
