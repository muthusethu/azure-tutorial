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
Maven phases are a train: compile → test → package — jumping off early dumps jars on the tracks.

Day 27 of #100DaysOfAzureDevOps. CI pipeline for a Java/Maven app.

I am not a full-time Java engineer. I have still been in rooms where someone skipped tests with -DskipTests because "the build was taking too long" and a null-pointer boarded production in a shaded jar. Maven's lifecycle is a train for a reason. compile, test, package. Jumping off at compile because the platform "only needs a jar" is how you ship untested bytecode with confidence.

If Java is not my stack this month, the honest lab is to read a sample Maven pipeline and still understand JavaToolInstaller@0, the pom.xml, and mvn -B test. Skipping the topic because I prefer C# is how gaps survive into interviews.

What I keep seeing

1. Install the JDK you mean
• JavaToolInstaller@0, versionSpec 17, PreInstalled on hosted agents
• "The agent had Java" is not a contract

2. Batch mode in CI
• mvn -B so Maven does not wait for a human in a log nobody is watching
• Point -f at the pom so the job does not depend on cwd folklore

3. Do not skip tests to go green
• mvn -B test (or verify) on the tiny archetype project
• -DskipTests is a fire exit, not a lifestyle

4. Package is a later car on the same train
• CI that only compiles is a syntax check
• Packaging without tests is a zip file with optimism

What I am doing in today's lab

I am either running mvn -B -f src/sample-java/pom.xml test on a tiny archetype project, or — if I am time-boxed — reading a sample Maven pipeline end-to-end and writing what each task is for. Optional skip of a deep Java app. Not optional skip of the lifecycle idea.

The train is compile, test, package. Get off early and someone else walks the tracks.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-27-ci-pipeline-for-a-java-maven-app

Tomorrow: Multi-stage YAML — dependsOn, matrix, conditions.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 27 — CI Pipeline for a Java App` (max 58 chars)
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

**Multi-stage YAML**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
