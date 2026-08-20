# Day 27 - CI Pipeline for a Java/Maven App

| | |
|---|---|
| **Date** | 16 Sep 2026 |
| **Phase** | 3 - Continuous Integration |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Maven lifecycle, unit tests, packaging

## Hands-on lab (20-30 min)

1. Optional: skip deep Java if not your stack - read a sample Maven pipeline instead
2. Or `mvn -B test` on a tiny archetype project

## Commands / code

```bash
steps:
- task: JavaToolInstaller@0
  inputs:
    versionSpec: 17
    jdkArchitectureOption: x64
    jdkSourceOption: PreInstalled
- script: mvn -B -f src/sample-java/pom.xml test
  displayName: Maven test
```

## LinkedIn post (copy-paste)

```
Day 27 of #100DaysOfAzureDevOps

Maven phases are a train: compile -> test -> package - jumping off early dumps jars on the tracks

Today's topic: **CI Pipeline for a Java/Maven App**.

I am learning in public for 100 days - mistakes included, sales pitches not included.

Tomorrow: Multi-stage YAML.

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

**Multi-stage YAML**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
