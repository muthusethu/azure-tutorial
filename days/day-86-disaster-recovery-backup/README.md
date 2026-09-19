# Day 86 — Disaster Recovery & Backup

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 9 - Advanced & Enterprise |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

A backup you never restore is fan fiction

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Term | Meaning | Lab-sized control |
| --- | --- | --- |
| RPO | How much data loss is acceptable | Write a target (e.g. 24h lab notes) — label it TARGET |
| RTO | How fast you must be back | Write a target (e.g. 4h) — measure a drill, do not invent |
| Soft delete | Recover a deleted secret/blob | Key Vault enableSoftDelete + secret recover |
| Local HA | Disk / zone / slot swap | Not DR. Same-region nicer failure |
| Geo | GRS/GZRS / paired region | Costs money; skip buy for a hello lab unless you drill it |
| Drill | Restore once on purpose | Recover a dummy secret or restore a backup |

## Step-by-step lab

1. Write RPO and RTO targets for the fictional lab app in docs/dr-day86.md. Label them TARGET. 'Zero / instant' is a wish — rewrite it.
2. az keyvault list -o table on the personal sub. Pick one lab vault (or record that you have none and stop before buying geo).
3. az keyvault show -n <vault> --query "{soft:properties.enableSoftDelete,purge:properties.enablePurgeProtection}". Soft delete should be true on modern vaults.
4. Drill: set a dummy secret drill-day86=temp, delete it, then az keyvault secret recover. Write the elapsed time.
5. State in the markdown whether this is backup (same region) or DR (paired region / second stamp). Do not call LRS a DR plan.
6. If you cannot restore today, write 'DR plan is still fiction' — that sentence is the lesson.

## Done when

- [ ] RPO/RTO written as TARGETs, not achievements
- [ ] One restore drill completed, or an explicit 'still fiction' sentence
- [ ] Soft-delete flag recorded
- [ ] Did not call same-region backup a DR story
- [ ] docs/dr-day86.md on the personal repo

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-86-disaster-recovery-backup
```

## Next

**Day 87** — Azure Landing Zones — city planning on paper for a clearly fictional company
