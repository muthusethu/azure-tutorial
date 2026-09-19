# Day 27 — CI Pipeline for a Java/Maven App

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 3 - Continuous Integration |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

The Maven train is compile → test → package. Jumping off at compile dumps untested jars on the tracks

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Phase | What Maven does | CI command |
| --- | --- | --- |
| validate / compile | POM + javac against JDK on PATH | mvn -B -f src/sample-java/pom.xml compile |
| test | Surefire unit tests (fail the build) | mvn -B -f src/sample-java/pom.xml test |
| package | jar/war after tests (default) | mvn -B -f ... package  (not -DskipTests) |
| JDK pin | JavaToolInstaller@0 versionSpec: '17' PreInstalled | Do not trust 'the agent had Java' |
| Cache | Cache@2 on $(HOME)/.m2/repository | Key includes pom.xml hash or you re-download the internet |

## Step-by-step lab

1. Option A: from a clean folder run mvn -B archetype:generate (quickstart) into src/sample-java and commit the pom + one unit test.
2. Option B (time-box): copy a public tiny pom + test into src/sample-java. Do not import an employer repo.
3. Add pipelines/maven-ci.yml with JavaToolInstaller@0 (17, x64, PreInstalled) and mvn -B -f src/sample-java/pom.xml test.
4. Pipelines → run the YAML. In the log find JAVA_HOME / Java version and the Surefire summary.
5. If you skip a full app, write docs/maven-lifecycle-day27.md: validate, compile, test, package, verify — one sentence each.
6. Do not add -DskipTests. If the job is slow, add Cache@2 on ~/.m2 keyed by pom.xml, not a skip.

## Done when

- [ ] Can list compile → test → package without calling it 'just build'
- [ ] YAML pins JDK 17; mvn uses -B and -f
- [ ] No -DskipTests on the lab pipeline
- [ ] Notes or a green Surefire run exist on the personal repo

## LinkedIn

Post draft: [`../../daily-guides/day-27.md`](../../daily-guides/day-27.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-27-ci-pipeline-for-a-java-maven-app
```

## Next

**Day 28** — Multi-stage YAML — dependsOn, succeeded(), and a matrix so 'works on my version' becomes two jobs.
