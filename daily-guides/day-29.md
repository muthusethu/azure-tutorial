# Day 29 - Pipeline Variables, Groups & Secrets

| | |
|---|---|
| **Date** | 18 Sep 2026 |
| **Phase** | 3 - Continuous Integration |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Runtime vs compile-time vars
- Variable groups; Key Vault link preview

## Hands-on lab (20-30 min)

1. Create variable group `lab-common`
2. Store a dummy secret (not real passwords)
3. Reference $(myVar) in pipeline

## Commands / code

```bash
variables:
- group: lab-common
steps:
- script: echo "App name is $(appName)"
  displayName: Use variable
```

## LinkedIn post (copy-paste)

```
Secrets in YAML are postcards — variable groups and Key Vault are envelopes.

Day 29 of #100DaysOfAzureDevOps. Pipeline variables, groups, and secrets.

I have reviewed YAML where a connection string sat in plain text because "it is only a lab" and then the repo got forked. A postcard is readable by everyone on the route. An envelope is still just paper, but it is the difference between a mistake and a habit.

Runtime versus compile-time variables still trips people up. Some values are baked when the run is queued. Some expand at step time. If you debug with echo, you will one day echo a secret. Today's rule: dummy secrets only, never real passwords, and never print the value.

What I keep seeing

1. Variable groups are shared drawers
• lab-common holds appName and non-secret defaults
• Link the group in YAML with variables: - group: lab-common

2. Secrets are a different object
• Mark them secret in the group so logs mask them
• A dummy value is enough to practice the mask — do not use anything real

3. Key Vault is the preview of next month
• Variable groups can link to Key Vault later (Day 65)
• Today I am not putting production secrets anywhere; I am practicing the envelope

4. echo is a loaded gun
• echo "App name is $(appName)" is fine for a non-secret
• echo $(mySecret) is how incident timelines get a screenshot

What I am doing in today's lab

I am creating variable group lab-common, storing a dummy secret (not a real password), referencing $(myVar) / $(appName) in a pipeline step, and confirming the secret is masked in the log. If it prints in clear text, the setup is wrong — I fix that before I go to bed.

If it is secret, it is not in YAML. If you need to debug it, print the length, not the letters.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-29-pipeline-variables-groups-secrets

Tomorrow: Phase 3 mini project — one green CI run I can screenshot without secrets.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 29 — Variables, Groups & Secrets` (max 58 chars)
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

**Phase 3 mini project**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
