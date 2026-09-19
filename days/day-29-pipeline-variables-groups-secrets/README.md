# Day 29 — Pipeline Variables, Groups & Secrets

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 3 - Continuous Integration |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

$( ) is runtime. ${{ }} is compile-time. A secret in YAML is a postcard

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Store | Expansion | Safe for secrets? |
| --- | --- | --- |
| YAML variables: key: value | $(key) at runtime; ${{ variables.key }} at compile | No. Repo is readable |
| UI pipeline variable | $(name) runtime; secret ones mask as *** | Only if marked secret; still not Key Vault |
| Library variable group | variables: - group: lab-common | Non-secrets yes; secrets if issecret + mask |
| Group linked to Key Vault | Preview today; deep dive Day 64–65 | Yes — vault is source, group is pointer |
| Compile vs runtime | ${{ }} baked when the run is queued | Do not ${{ }} a secret into a condition string |

## Step-by-step lab

1. Pipelines → Library → Variable groups → New → name lab-common. Add appName=azure-100-labs (not secret).
2. Add labDummy as a secret. Value: not-a-real-password (literally). Do not reuse anything from work.
3. In YAML set variables: - group: lab-common. First run will ask to authorize the group — allow it for this project only.
4. Step: echo App name is $(appName). Confirm it expands. Do not echo $(labDummy).
5. Optional: echo Dummy length is ${#LAB} after mapping — or skip and just confirm the secret shows as *** if you print it by accident, then remove that line.
6. Write docs/variables-day29.md: compile-time ${{ }} vs runtime $( ) in two sentences. No values in the doc.

## Done when

- [ ] Group lab-common exists; pipeline authorized to it
- [ ] $(appName) expanded in the log
- [ ] No real secret, PAT, or connection string in YAML or screenshots
- [ ] Can explain ${{ }} vs $( ) without saying 'variables are variables'

## LinkedIn

Post draft: [`../../daily-guides/day-29.md`](../../daily-guides/day-29.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-29-pipeline-variables-groups-secrets
```

## Next

**Day 30** — Phase 3 mini project — one green CI on your primary stack, artifact in hand, secrets still out of the file.
