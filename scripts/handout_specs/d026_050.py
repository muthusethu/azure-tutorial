# -*- coding: utf-8 -*-
"""LinkedIn PDF handout specs for Days 26–50 (#100DaysOfAzureDevOps)."""

SPECS = {
    26: {
        "topic": "CI Pipeline for a Python App",
        "subtitle": "Pin the interpreter, then make ruff and pytest run on the agent — not on your laptop",
        "phase": "3 - Continuous Integration",
        "tables": [
            {
                "title": "Architecture A — Python CI is a contract with the hosted agent",
                "columns": ["Piece", "YAML / file", "What it proves"],
                "rows": [
                    ["Interpreter", "UsePythonVersion@0  versionSpec: '3.11'", "Not leftover python3 on ubuntu-latest"],
                    ["Lockfile", "requirements.txt (pytest, ruff pinned)", "Next clone does not hunt a wiki"],
                    ["Lint", "ruff check src/sample-python", "Style + a class of bugs; own exit code"],
                    ["Tests", "pytest -q --junitxml=$(Build.StagingDirectory)/junit.xml", "Behavior. Do not merge with lint"],
                    ["Receipt", "PublishTestResults@2 on that junit.xml", "The run has evidence, not only a green job"],
                ],
                "widths": [32, 80, 70],
            },
            {
                "title": "Architecture B — decide what fails the job",
                "columns": ["Signal", "Fail the job when", "Lab exception (temporary)"],
                "rows": [
                    ["Interpreter missing", "UsePythonVersion@0 cannot resolve 3.11", "Never. Pin or the pipeline is folklore"],
                    ["Import / dep", "pip install exits non-zero", "Never. A missing wheel is a real break"],
                    ["ruff", "ruff check finds F/E rules you adopted", "|| true once so the first YAML exists"],
                    ["pytest", "any test fails or collects 0 tests you expected", "Never. Zero tests is not a safety net"],
                ],
                "widths": [42, 70, 70],
            },
            {
                "title": "Architecture C — pitfalls that go green for the wrong reason",
                "columns": ["Pitfall", "What you see", "Fix"],
                "rows": [
                    ["Agent Python", "Works locally, ImportError on ubuntu-latest", "UsePythonVersion@0; echo $(python --version)"],
                    ["No requirements.txt", "pip install pytest ruff typed from memory", "Commit the pins; Cache@2 on pip cache later"],
                    ["|| true forever", "ruff red in the log, job still green", "Remove the swallow before main is protected"],
                    ["pytest not collected", "pytest -q  collected 0 items  → still 0", "Put tests under tests/ or test_*.py; fail if empty"],
                ],
                "widths": [40, 71, 71],
            },
        ],
        "one_liner": "pytest is the friend who tells you the truth before your users do — but only if CI actually runs it.",
        "lab_intro": "Personal Azure DevOps org only. Project azure-100-labs. Hosted pool: vmImage ubuntu-latest.",
        "lab": [
            "In the lab repo create src/sample-python/app.py (a tiny function) and tests/test_app.py with one pytest that asserts it.",
            "Add src/sample-python/requirements.txt with pytest==8.* and ruff pinned. Commit on a feature branch — do not put secrets in the file.",
            "Pipelines → New pipeline → Azure Repos Git → azure-100-labs. Point at pipelines/python-ci.yml (starter below).",
            "Run once. Open the job log: confirm UsePythonVersion printed 3.11, ruff ran, pytest collected ≥1 item.",
            "If ruff is noisy, keep || true for this lab only and write that debt in docs/python-ci-day26.md. Do not leave it unexplained.",
            "Optional: add PublishTestResults@2. Confirm the Tests tab on the run shows the case. Screenshot no secrets.",
        ],
        "code_title": "Starter YAML — pin 3.11, lint, pytest",
        "code": """# pipelines/python-ci.yml
trigger:
  branches:
    include: [ main ]
  paths:
    include: [ src/sample-python/**, pipelines/python-ci.yml ]
pool:
  vmImage: ubuntu-latest
steps:
- task: UsePythonVersion@0
  inputs:
    versionSpec: '3.11'
    addToPath: true
- script: |
    python -m pip install --upgrade pip
    pip install -r src/sample-python/requirements.txt
    ruff check src/sample-python || true
    pytest -q src/sample-python tests -q
  displayName: pip, ruff, pytest
""",
        "checklist": [
            "UsePythonVersion@0 pinned 3.11 in the log — not 'whatever the image had'",
            "At least one pytest collected and passed on the agent",
            "requirements.txt is committed; no passwords in YAML",
            "Posted the LinkedIn document (personal account, no employer)",
        ],
        "tomorrow": "CI for Java/Maven — JavaToolInstaller@0, the Maven lifecycle train, and mvn -B test.",
    },
    27: {
        "topic": "CI Pipeline for a Java/Maven App",
        "subtitle": "The Maven train is compile → test → package. Jumping off at compile dumps untested jars on the tracks",
        "phase": "3 - Continuous Integration",
        "tables": [
            {
                "title": "Architecture A — Maven lifecycle on a hosted job",
                "columns": ["Phase", "What Maven does", "CI command"],
                "rows": [
                    ["validate / compile", "POM + javac against JDK on PATH", "mvn -B -f src/sample-java/pom.xml compile"],
                    ["test", "Surefire unit tests (fail the build)", "mvn -B -f src/sample-java/pom.xml test"],
                    ["package", "jar/war after tests (default)", "mvn -B -f ... package  (not -DskipTests)"],
                    ["JDK pin", "JavaToolInstaller@0 versionSpec: '17' PreInstalled", "Do not trust 'the agent had Java'"],
                    ["Cache", "Cache@2 on $(HOME)/.m2/repository", "Key includes pom.xml hash or you re-download the internet"],
                ],
                "widths": [36, 78, 68],
            },
            {
                "title": "Architecture B — when to skip a deep Java app",
                "columns": ["Constraint", "Do this", "Do not do this"],
                "rows": [
                    ["Java is your stack", "mvn archetype + green test on main", "Skip tests to 'save minutes'"],
                    ["Java is not your stack", "Read the YAML + lifecycle; write 8 lines of notes", "Skip the day. Interviews still ask about the train"],
                    ["Build too slow", "Cache@2 + -B; shrink the module", "-DskipTests as a lifestyle"],
                    ["Need a jar for later CD", "mvn -B package then PublishPipelineArtifact@1", "Compile-only job labeled 'CI'"],
                ],
                "widths": [42, 70, 70],
            },
            {
                "title": "Architecture C — pitfalls that ship shaded optimism",
                "columns": ["Pitfall", "What you see", "Fix"],
                "rows": [
                    ["Wrong JDK", "illegal start / preview errors; works on laptop 21", "JavaToolInstaller@0 17; echo $JAVA_HOME"],
                    ["cwd folklore", "Unable to find pom.xml at /home/vsts/work/1/s", "Always -f src/sample-java/pom.xml"],
                    ["Interactive Maven", "Job hangs on a prompt nobody will answer", "mvn -B (batch mode) in every CI script"],
                    ["-DskipTests", "Green in 40s; NPE in the first request", "test or verify. Fire exit, not a habit"],
                ],
                "widths": [40, 71, 71],
            },
        ],
        "one_liner": "Maven phases are a train: compile → test → package — jumping off early dumps jars on the tracks.",
        "lab_intro": "Personal Azure DevOps org only. Project azure-100-labs. Hosted ubuntu-latest. Deep Java app is optional; the lifecycle is not.",
        "lab": [
            "Option A: from a clean folder run mvn -B archetype:generate (quickstart) into src/sample-java and commit the pom + one unit test.",
            "Option B (time-box): copy a public tiny pom + test into src/sample-java. Do not import an employer repo.",
            "Add pipelines/maven-ci.yml with JavaToolInstaller@0 (17, x64, PreInstalled) and mvn -B -f src/sample-java/pom.xml test.",
            "Pipelines → run the YAML. In the log find JAVA_HOME / Java version and the Surefire summary.",
            "If you skip a full app, write docs/maven-lifecycle-day27.md: validate, compile, test, package, verify — one sentence each.",
            "Do not add -DskipTests. If the job is slow, add Cache@2 on ~/.m2 keyed by pom.xml, not a skip.",
        ],
        "code_title": "Starter YAML — JDK 17 + mvn -B test",
        "code": """# pipelines/maven-ci.yml
trigger:
  paths:
    include: [ src/sample-java/** ]
pool:
  vmImage: ubuntu-latest
steps:
- task: JavaToolInstaller@0
  inputs:
    versionSpec: '17'
    jdkArchitectureOption: x64
    jdkSourceOption: PreInstalled
- task: Cache@2
  inputs:
    key: 'maven | "$(Agent.OS)" | src/sample-java/pom.xml'
    path: $(HOME)/.m2/repository
- script: mvn -B -f src/sample-java/pom.xml test
  displayName: Maven test (no -DskipTests)
""",
        "checklist": [
            "Can list compile → test → package without calling it 'just build'",
            "YAML pins JDK 17; mvn uses -B and -f",
            "No -DskipTests on the lab pipeline",
            "Notes or a green Surefire run exist on the personal repo",
        ],
        "tomorrow": "Multi-stage YAML — dependsOn, succeeded(), and a matrix so 'works on my version' becomes two jobs.",
    },
    28: {
        "topic": "Multi-stage YAML Pipelines",
        "subtitle": "Stages remember order. Matrix clones the job. A deploy stub that ignores Test is theater",
        "phase": "3 - Continuous Integration",
        "tables": [
            {
                "title": "Architecture A — YAML objects and what they actually mean",
                "columns": ["Object", "Owns", "Typical keys"],
                "rows": [
                    ["stage", "A gate in the workflow", "dependsOn, condition, jobs, variables"],
                    ["job", "One agent lease", "pool, strategy.matrix, steps, dependsOn (other jobs)"],
                    ["deployment", "CD job + environment history", "environment, strategy.runOnce.deploy (Day 31+)"],
                    ["matrix", "N clones of the same job", "strategy.matrix: py311 / py312 → $(python.version)"],
                    ["condition", "Whether the stage/job runs", "succeeded() default after dependsOn; always() is explicit"],
                ],
                "widths": [34, 58, 90],
            },
            {
                "title": "Architecture B — dependsOn vs hope",
                "columns": ["Intent", "YAML", "If you omit it"],
                "rows": [
                    ["Test after Build", "stage Test  dependsOn: Build", "Stages can race; Test may start on a red Build"],
                    ["Stub only if green", "condition: succeeded()", "A failed test still 'deploys' an echo"],
                    ["Fan-out versions", "strategy.matrix on the job (not the stage)", "You tested one runtime and marketed three"],
                    ["Fan-in after matrix", "dependsOn: Build  condition: succeeded()", "Publish runs while one matrix leg is still red"],
                ],
                "widths": [42, 72, 68],
            },
            {
                "title": "Architecture C — pitfalls that look parallel and lie",
                "columns": ["Pitfall", "What you see", "Fix"],
                "rows": [
                    ["Matrix on a stage", "Schema error or one job anyway", "strategy lives on job"],
                    ["No parallelism SKU", "Matrix jobs queue one-by-one", "Expected on free Microsoft-hosted; still correct YAML"],
                    ["condition: succeededOrFailed()", "Publish runs after Test exploded", "Use that only when you mean cleanup"],
                    ["dependsOn: []", "Stage starts with CI, skips the chain", "Empty dependsOn is 'run now', not 'I forgot'"],
                ],
                "widths": [48, 67, 67],
            },
        ],
        "one_liner": "Matrix builds clone you across versions so 'works on my Node' becomes 'works on these Nodes' — and succeeded() keeps the stub honest.",
        "lab_intro": "Personal Azure DevOps org only. Project azure-100-labs. Reuse Day 26 Python or Day 25 Node — do not rebuild a third app.",
        "lab": [
            "Open pipelines/python-ci.yml (or node). Split it into stages Build and Test. Test must set dependsOn: Build.",
            "On the Build (or Test) job add strategy.matrix for two versions (3.11/3.12 or Node 18.x/20.x). NodeTool@0 / UsePythonVersion@0 reads $(version).",
            "Add stage Publish with dependsOn: Test and condition: succeeded() and a single script: echo stub — not a real deploy.",
            "Run on main or a PR. Confirm the run graph shows two matrix legs, then Publish.",
            "Break a test on purpose (assert 1 == 0), push, watch Publish stay skipped. If it still runs, the condition is theater — fix it.",
            "Revert the broken test. Write one paragraph in docs/multistage-day28.md: dependsOn vs condition vs matrix.",
        ],
        "code_title": "Starter YAML — matrix + dependsOn + succeeded()",
        "code": """# pipelines/multistage.yml
trigger:
  - main
stages:
- stage: Build
  jobs:
  - job: BuildJob
    pool: { vmImage: ubuntu-latest }
    strategy:
      matrix:
        py311: { version: '3.11' }
        py312: { version: '3.12' }
    steps:
    - task: UsePythonVersion@0
      inputs: { versionSpec: $(version) }
    - script: python --version
      displayName: Prove matrix version
- stage: Test
  dependsOn: Build
  condition: succeeded()
  jobs:
  - job: TestJob
    pool: { vmImage: ubuntu-latest }
    steps:
    - script: echo Tests would run here
- stage: Publish
  dependsOn: Test
  condition: succeeded()
  jobs:
  - job: Stub
    pool: { vmImage: ubuntu-latest }
    steps:
    - script: echo Stub only — no deploy bits
""",
        "checklist": [
            "Can point at dependsOn and condition: succeeded() in your YAML",
            "Matrix ran two versions (or you noted hosted parallelism queued them)",
            "A failed Test skipped Publish once",
            "docs/multistage-day28.md exists on the personal repo",
        ],
        "tomorrow": "Variables, groups, and secrets — runtime $( ), compile-time ${{ }}, and why secrets in YAML are postcards.",
    },
    29: {
        "topic": "Pipeline Variables, Groups & Secrets",
        "subtitle": "$( ) is runtime. ${{ }} is compile-time. A secret in YAML is a postcard",
        "phase": "3 - Continuous Integration",
        "tables": [
            {
                "title": "Architecture A — where a value lives and when it expands",
                "columns": ["Store", "Expansion", "Safe for secrets?"],
                "rows": [
                    ["YAML variables: key: value", "$(key) at runtime; ${{ variables.key }} at compile", "No. Repo is readable"],
                    ["UI pipeline variable", "$(name) runtime; secret ones mask as ***", "Only if marked secret; still not Key Vault"],
                    ["Library variable group", "variables: - group: lab-common", "Non-secrets yes; secrets if issecret + mask"],
                    ["Group linked to Key Vault", "Preview today; deep dive Day 64–65", "Yes — vault is source, group is pointer"],
                    ["Compile vs runtime", "${{ }} baked when the run is queued", "Do not ${{ }} a secret into a condition string"],
                ],
                "widths": [44, 78, 60],
            },
            {
                "title": "Architecture B — pick the drawer, not a blog title",
                "columns": ["Need", "Use", "Skip"],
                "rows": [
                    ["App name, region, SKU label", "Group lab-common → $(appName)", "Hardcoded per-pipeline copies"],
                    ["Dummy lab secret", "Group secret labDummy  value: not-a-password", "Real password, PAT, or connection string"],
                    ["Same value on 4 pipelines", "One group, many YAML references", "Four UI variables you will drift"],
                    ["Production secret later", "Key Vault + RBAC (Phase 7)", "Putting it in azure-pipelines.yml 'just for now'"],
                ],
                "widths": [48, 72, 62],
            },
            {
                "title": "Architecture C — pitfalls that print the postcard",
                "columns": ["Pitfall", "What you see", "Fix"],
                "rows": [
                    ["echo $(labDummy)", "Clear text if not marked secret", "Mark secret; debug length only, never letters"],
                    ["Group not linked", "$(appName) empty or literal $(appName)", "variables: - group: lab-common on the pipeline"],
                    ["Auth on the group", "Job fails: variable group could not be accessed", "Pipeline must be authorized to the Library group"],
                    ["Secret in compile-time", "Value appears in expanded YAML of the run", "Keep secrets runtime-only; never ${{ }} them"],
                ],
                "widths": [42, 70, 70],
            },
        ],
        "one_liner": "Secrets in YAML are postcards — variable groups and Key Vault are envelopes. If you need to debug, print the length, not the letters.",
        "lab_intro": "Personal Azure DevOps org only. Project azure-100-labs. Dummy values only — never a real password, PAT, or work secret.",
        "lab": [
            "Pipelines → Library → Variable groups → New → name lab-common. Add appName=azure-100-labs (not secret).",
            "Add labDummy as a secret. Value: not-a-real-password (literally). Do not reuse anything from work.",
            "In YAML set variables: - group: lab-common. First run will ask to authorize the group — allow it for this project only.",
            "Step: echo App name is $(appName). Confirm it expands. Do not echo $(labDummy).",
            "Optional: echo Dummy length is ${#LAB} after mapping — or skip and just confirm the secret shows as *** if you print it by accident, then remove that line.",
            "Write docs/variables-day29.md: compile-time ${{ }} vs runtime $( ) in two sentences. No values in the doc.",
        ],
        "code_title": "Starter YAML — group reference, no secret echo",
        "code": """# pipelines/vars-day29.yml
trigger: none
variables:
- group: lab-common
pool:
  vmImage: ubuntu-latest
steps:
- script: echo "App name is $(appName)"
  displayName: Non-secret from group
- script: echo "Dummy is set but will not be printed"
  displayName: Secret stays in the envelope
""",
        "checklist": [
            "Group lab-common exists; pipeline authorized to it",
            "$(appName) expanded in the log",
            "No real secret, PAT, or connection string in YAML or screenshots",
            "Can explain ${{ }} vs $( ) without saying 'variables are variables'",
        ],
        "tomorrow": "Phase 3 mini project — one green CI on your primary stack, artifact in hand, secrets still out of the file.",
    },
    30: {
        "topic": "Mini Project + Recap (Phase 3)",
        "subtitle": "Same spine in every language: install, build, test, publish a drop — secrets stay in the group",
        "phase": "3 - Continuous Integration",
        "tables": [
            {
                "title": "Architecture A — Phase 3 map (Days 21–29)",
                "columns": ["Day", "Object you should still be able to draw", "Keep"],
                "rows": [
                    ["21–22", "pool: vmImage vs named self-hosted pool", "Hosted ubuntu-latest until a private-network constraint"],
                    ["23 + 28", "trigger/pr → stages → jobs → steps; dependsOn; matrix", "Sketch from memory or you copied"],
                    ["24–27", ".NET / Node / Python / Maven CI tasks", "One primary stack green; others may stay stubs"],
                    ["29", "Library group + secret mask", "No passwords in azure-pipelines.yml"],
                    ["Handoff", "PublishPipelineArtifact@1 name: drop", "CD (Phase 4) must download this, not rebuild"],
                ],
                "widths": [28, 92, 62],
            },
            {
                "title": "Architecture B — pick depth, not four half-pipelines",
                "columns": ["Choice", "Definition of done today", "Trap"],
                "rows": [
                    [".NET primary", "restore/build/test/publish + drop on main", "Keeping Node/Python red 'for later'"],
                    ["Node primary", "NodeTool + npm ci + test + drop", "Skipping lockfile so CI ≠ laptop"],
                    ["Python primary", "3.11 + pytest collected ≥1 + drop (even a wheel/zip)", "Lint || true with no note"],
                    ["Java primary", "JDK 17 + mvn -B test/package + drop", "-DskipTests to force a screenshot"],
                ],
                "widths": [36, 82, 64],
            },
            {
                "title": "Architecture C — recap failures that fake a phase close",
                "columns": ["Pitfall", "What you see", "Fix"],
                "rows": [
                    ["No artifact", "Green job, nothing to promote Monday", "PublishPipelineArtifact@1 before you write the recap"],
                    ["Secret in shot", "Library value visible in a LinkedIn PNG", "Retake. Mask or crop. Rotate the dummy if leaked"],
                    ["Copied YAML only", "Cannot list trigger → stage → job → step", "Draw it once in docs/phase3-recap.md"],
                    ["Four languages, zero green", "A graveyard of samples", "One green main. Stubs are honest; red mains are not"],
                ],
                "widths": [40, 71, 71],
            },
        ],
        "one_liner": "Phase 3 recap: CI is a seatbelt you wear before the crash, not after — and the buckle is a drop you can promote.",
        "lab_intro": "Personal Azure DevOps org only. Project azure-100-labs. Pick one primary stack. Personal time, personal repo.",
        "lab": [
            "Choose primary stack (.NET Day 24, Node 25, Python 26, or Maven 27). Delete or ignore the other pipelines if they distract — do not keep red mains.",
            "Ensure that pipeline publishes an artifact named drop (PublishPipelineArtifact@1 or PublishBuildArtifacts@1). Run on main until green.",
            "Open the run → Artifacts and confirm drop exists. That object is the Phase 4 input.",
            "Write docs/phase3-recap.md: (1) YAML anatomy in one line, (2) one war story from this week (cache miss, skipped test, almost-echoed secret).",
            "Screenshot the green run with no variable values. Save it locally — do not commit secrets or org URLs you would not post.",
            "Pipelines folder is the source of truth. If Classic UI still holds a leftover, leave it unused.",
        ],
        "code_title": "Artifact handoff — publish drop (adapt path to your stack)",
        "code": """# append to your primary CI job
- task: PublishPipelineArtifact@1
  inputs:
    targetPath: $(Build.ArtifactStagingDirectory)
    artifact: drop
    publishLocation: pipeline
# Phase 4 will: download: current  artifact: drop
# Do not dotnet/npm/mvn publish again in a release job.
""",
        "checklist": [
            "One green CI on main for the primary stack",
            "Artifact drop is visible on that run",
            "docs/phase3-recap.md has anatomy + one war story",
            "No secrets in YAML or screenshots",
        ],
        "tomorrow": "Release pipelines overview — Classic is literacy; YAML CD is a deployment job + environment: dev.",
    },
    31: {
        "topic": "Release Pipelines Overview",
        "subtitle": "Classic is the old mall. YAML CD is a deployment job, an environment, and runOnce.deploy",
        "phase": "4 - Continuous Delivery",
        "tables": [
            {
                "title": "Architecture A — CD objects (same run, different job type)",
                "columns": ["Object", "YAML", "Why it exists"],
                "rows": [
                    ["Classic Release", "UI designer, not in the repo", "Brownfield literacy. Not the lab default"],
                    ["stage", "stage: DeployDev", "A gate. Can dependOn CI / previous env"],
                    ["deployment job", "deployment: Deploy  (not job:)", "Environment checks attach here"],
                    ["environment", "environment: dev", "Azure DevOps record: history, checks, resources"],
                    ["strategy", "runOnce.deploy.steps", "Smallest CD. rolling/canary come later as ideas"],
                    ["bits", "download: current  artifact: drop", "Consume Phase 3. Rebuilding here invents ghosts"],
                ],
                "widths": [36, 72, 74],
            },
            {
                "title": "Architecture B — Classic vs YAML for this series",
                "columns": ["Question", "YAML CD", "Classic Release"],
                "rows": [
                    ["Where is the workflow?", "In git. Reviews as a diff", "In the service. Reviews as screenshots"],
                    ["Approvals later (Day 38)", "Checks on the Environment", "Pre-deployment conditions on a stage"],
                    ["Multi-env (Day 39)", "dependsOn chain + same drop", "Stage-to-stage; still can rebuild if you let it"],
                    ["Lab default", "Use this", "Open once so you can recognize it; do not live there"],
                ],
                "widths": [46, 68, 68],
            },
            {
                "title": "Architecture C — pitfalls that impersonate CI",
                "columns": ["Pitfall", "What you see", "Fix"],
                "rows": [
                    ["job: instead of deployment:", "environment: ignored or no check history", "Use deployment: + strategy.runOnce"],
                    ["Rebuild in Deploy", "dotnet publish in the release job", "download: current artifact: drop"],
                    ["No Environment object", "YAML names prod; UI has empty list", "Pipelines → Environments → New → dev"],
                    ["Classic + YAML twins", "Two sources of truth, one of them stale", "Pick YAML. Leave Classic unused"],
                ],
                "widths": [44, 69, 69],
            },
        ],
        "one_liner": "Classic releases are the old mall; YAML CD is the street you actually live on — a deployment job aimed at environment: dev.",
        "lab_intro": "Personal Azure DevOps org only. Project azure-100-labs. No Azure spend required today — echo is a legal first proof.",
        "lab": [
            "Pipelines → Environments → New environment → name: dev → create with no resources. This is an Azure DevOps object, not a folder on disk.",
            "Add pipelines/cd-dev.yml (starter below): stage DeployDev, deployment job, environment: dev, download drop if CI published it, else echo.",
            "If drop is missing, run the Phase 3 CI once so current has an artifact — or keep echo-only and note the gap.",
            "Run the pipeline. Open Environments → dev → deployments and confirm this run is listed.",
            "Pipelines → Releases (Classic). Open it once. Write one line: why labs stay on YAML. Do not create a Classic release.",
            "docs/cd-yaml-day31.md: deployment vs job, environment, download: current.",
        ],
        "code_title": "Starter YAML — deployment job on environment dev",
        "code": """# pipelines/cd-dev.yml
trigger: none
resources:
  pipelines:
  - pipeline: ci
    source: azure-100-labs  # name of your CI pipeline
    trigger: true
stages:
- stage: DeployDev
  jobs:
  - deployment: Deploy
    environment: dev
    pool: { vmImage: ubuntu-latest }
    strategy:
      runOnce:
        deploy:
          steps:
          - download: ci
            artifact: drop
          - script: echo "Deploying $(Pipeline.Workspace)/ci/drop to dev"
            displayName: Proof — no rebuild
""",
        "checklist": [
            "Environment dev exists under Pipelines → Environments",
            "A deployment job (not a regular job) targeted it",
            "YAML does not rebuild the app in Deploy",
            "Classic was viewed, not adopted",
        ],
        "tomorrow": "Deploy to Azure App Service — F1 plan, AzureWebApp@1, the zip you already published.",
    },
    32: {
        "topic": "Deploying to Azure App Service",
        "subtitle": "PaaS comfort food: Microsoft.Web/serverfarms + sites, zip deploy, then delete the kitchen if it costs",
        "phase": "4 - Continuous Delivery",
        "tables": [
            {
                "title": "Architecture A — App Service pieces the task actually hits",
                "columns": ["Resource", "Type / SKU", "Pipeline hook"],
                "rows": [
                    ["Plan", "Microsoft.Web/serverfarms  sku F1 (Free)", "Always-on off; unloads. Fine for hello"],
                    ["Web app", "Microsoft.Web/sites  kind app", "appName in AzureWebApp@1"],
                    ["Bits", "zip / folder from artifact drop", "package: $(Pipeline.Workspace)/**/*.zip"],
                    ["Identity", "ARM service connection (azureSubscription)", "Robot badge. Not Owner on the subscription"],
                    ["Runtime", "linuxFxVersion or windows stack", "Must match what CI published (dotnet/node/python)"],
                ],
                "widths": [30, 78, 74],
            },
            {
                "title": "Architecture B — App Service vs what you will do tomorrow",
                "columns": ["Need", "App Service (today)", "Functions (Day 33)"],
                "rows": [
                    ["Shape of work", "HTTP site that stays a site", "Event: HTTP, timer, queue — scale to zero"],
                    ["Host", "Plan + site; you pick F1/B1/S1", "Consumption Y1 vs Premium EP1 vs dedicated plan"],
                    ["CD task", "AzureWebApp@1 / @2", "AzureFunctionApp@2  appType: functionApp"],
                    ["Slots later", "Standard S1+ (F1 has none)", "Premium/Dedicated; not the F1 story"],
                ],
                "widths": [36, 73, 73],
            },
            {
                "title": "Architecture C — pitfalls that succeed and deploy nothing useful",
                "columns": ["Pitfall", "What you see", "Fix"],
                "rows": [
                    ["Glob miss", "AzureWebApp@1 green; default page still there", "Match the zip CI published; list $(Pipeline.Workspace)"],
                    ["Wrong stack", "You do not have permission / module not found", "linuxFxVersion matches runtime; do not mix win/linux zips"],
                    ["Owner SPN", "It works, and the robot can delete the sub", "Scope the service connection to rg-day32-lab"],
                    ["Orphan plan", "RG gone, plan leftover billing", "Delete the RG (plan lives in the RG). Tonight if cost-sensitive"],
                ],
                "widths": [36, 73, 73],
            },
        ],
        "one_liner": "App Service is PaaS comfort food — less drama than VMs, still enough knobs to burn dinner if the zip glob is wrong.",
        "lab_intro": "Personal Azure subscription + personal Azure DevOps org. Project azure-100-labs. Resource group rg-day32-lab. Delete tonight if you do not need it for slots later this week.",
        "lab": [
            "az login on the personal account. az group create -n rg-day32-lab -l centralindia (or your nearest region).",
            "Create a Free F1 Linux plan + webapp with a globally unique name (starter CLI). Do not use a work subscription.",
            "Project Settings → Service connections → Azure Resource Manager → scoped to rg-day32-lab (or the subscription if you must). Name it azure-100-sc.",
            "Wire AzureWebApp@1 to azure-100-sc, appName, and the drop zip from CI. Run once. Hit https://<app>.azurewebsites.net.",
            "If the site is still the default page, the glob missed. List files on the agent; fix package; rerun. Do not rebuild in the deploy job.",
            "Cost-sensitive: az group delete -n rg-day32-lab --yes --no-wait. Slots (Day 34) need Standard — recreate then, not on F1.",
        ],
        "code_title": "CLI + AzureWebApp@1 — F1 hello, zip from drop",
        "code": """# personal Cloud Shell / local CLI
az group create -n rg-day32-lab -l centralindia
az appservice plan create -g rg-day32-lab -n plan-day32 --sku F1 --is-linux
az webapp create -g rg-day32-lab -p plan-day32 -n app-day32-<unique> --runtime "NODE:20-lts"

# pipelines/deploy-appservice.yml (deploy job steps)
- task: AzureWebApp@1
  inputs:
    azureSubscription: azure-100-sc
    appName: app-day32-<unique>
    package: $(Pipeline.Workspace)/ci/drop/**/*.zip
""",
        "checklist": [
            "Personal RG + F1 webapp deployed from the pipeline zip",
            "Service connection is not a story about subscription Owner",
            "No rebuild in the deploy job",
            "RG deleted or a written reason to keep it until Day 34",
        ],
        "tomorrow": "Deploy to Azure Functions — Consumption vs Premium, AzureFunctionApp@2, still a zip from CI.",
    },
    33: {
        "topic": "Deploying to Azure Functions",
        "subtitle": "Event-shaped work, a plan that can sleep, and a different CD task — still not a Visual Studio publish as source of truth",
        "phase": "4 - Continuous Delivery",
        "tables": [
            {
                "title": "Architecture A — Function App vs App Service (same control plane, different product)",
                "columns": ["Dimension", "Function App", "App Service web app"],
                "rows": [
                    ["Resource", "Microsoft.Web/sites  kind functionapp", "kind app (Day 32)"],
                    ["Unit of work", "Trigger: httptrigger, timerTrigger, queue", "HTTP site / always a web process"],
                    ["Plan", "Consumption (Y1), Flex, Premium EP1, or dedicated", "F1/B1/S1… you picked a SKU"],
                    ["Scale to zero", "Consumption yes (cold start)", "F1 unloads; paid SKUs stay warmer"],
                    ["CD task", "AzureFunctionApp@2  appType: functionApp", "AzureWebApp@1"],
                    ["Package", "Zip of function bits from CI drop", "Zip of the web app from the same drop idea"],
                ],
                "widths": [32, 78, 72],
            },
            {
                "title": "Architecture B — pick the plan for the sleep pattern",
                "columns": ["Plan", "Use when", "Bill / ops note"],
                "rows": [
                    ["Consumption Y1", "Lab HTTP or timer, scale to zero", "Pay per execution; cold start; quota can block create"],
                    ["Premium EP1", "VNet, pre-warmed, slots", "Always a bill. Not a nap"],
                    ["Dedicated plan", "You already pay for a serverfarms SKU", "Functions as another site on that plan"],
                    ["Skip create", "Quota / cost tight today", "Read-only: blades + YAML literacy. Honest lab"],
                ],
                "widths": [40, 70, 72],
            },
            {
                "title": "Architecture C — pitfalls that bill for the nap",
                "columns": ["Pitfall", "What you see", "Fix"],
                "rows": [
                    ["Timer left on", "Cost Management surprise; still firing", "Disable the function or delete the app after proof"],
                    ["VS publish + pipeline", "Portal shows an older zip than CI", "Pipeline is source of truth; stop the right-click publish"],
                    ["Wrong task", "AzureWebApp@1 on a functionapp", "AzureFunctionApp@2; appType functionApp"],
                    ["Storage missing", "Function app create fails (needs a storage account)", "Create st<unique> in the same RG; Functions requires it"],
                ],
                "widths": [40, 71, 71],
            },
        ],
        "one_liner": "Functions are micro-managers that only wake up when work arrives — and still send you a bill for a timer you forgot.",
        "lab_intro": "Personal subscription + personal Azure DevOps org. RG rg-day33-lab. Consumption default. Read-only is valid if quota is tight.",
        "lab": [
            "az group create -n rg-day33-lab -l centralindia. Create a storage account (Functions requires one) + a Consumption Function App, or stop at the portal error and write the quota note.",
            "If you create: use a tiny HTTP sample (func init / existing hello). Package a zip in CI — do not treat Visual Studio publish as the source of truth.",
            "Add AzureFunctionApp@2 with azureSubscription: azure-100-sc, appType: functionApp, appName, package glob on the zip.",
            "Trigger the HTTP function once (browser or curl). Confirm 200/output. If timer sample: fire once, then disable it.",
            "Project Settings → confirm the service connection scope. Do not leave a subscription-Owner robot from Day 32 unused on this RG.",
            "az functionapp delete or az group delete -n rg-day33-lab --yes --no-wait after the proof. Naps still meter.",
        ],
        "code_title": "CLI + AzureFunctionApp@2 — Consumption HTTP sample",
        "code": """az group create -n rg-day33-lab -l centralindia
az storage account create -g rg-day33-lab -n stfn<unique> --sku Standard_LRS
az functionapp create -g rg-day33-lab -n func-day33-<unique> \\
  --consumption-plan-location centralindia --runtime python --functions-version 4 \\
  --storage-account stfn<unique>

# deploy job
- task: AzureFunctionApp@2
  inputs:
    azureSubscription: azure-100-sc
    appType: functionApp
    appName: func-day33-<unique>
    package: $(Pipeline.Workspace)/ci/drop/**/*.zip
""",
        "checklist": [
            "Can explain Consumption vs Premium without saying 'serverless is free'",
            "CD uses AzureFunctionApp@2 on a CI zip (or a written quota skip)",
            "Timer/HTTP not left running overnight",
            "RG deleted or budget-watched",
        ],
        "tomorrow": "Deployment slots — staging as a dressing room, warm-up, swap. F1 will refuse; that is data.",
    },
    34: {
        "topic": "Deployment Slots & Swap Strategies",
        "subtitle": "Staging is a dressing room. Swap is a VIP flip. F1 has no room — Standard S1+ does",
        "phase": "4 - Continuous Delivery",
        "tables": [
            {
                "title": "Architecture A — slots on Microsoft.Web/sites (App Service)",
                "columns": ["Piece", "What it is", "YAML / portal"],
                "rows": [
                    ["Production slot", "The default site hostname", "appName only; slot not set"],
                    ["Staging slot", "Microsoft.Web/sites/slots  name staging", "Portal: Deployment slots → Add  or deployToSlotOrASE"],
                    ["Swap", "VIP / hostname flip; instances stay warm if you warmed them", "az webapp deployment slot swap"],
                    ["Slot setting", "Sticky app setting (slotSetting: true)", "Does not ride the swap — connection strings, flags"],
                    ["Warm-up", "applicationInitialization / hit staging URL", "Swap of a cold process is a scheduled brownout"],
                ],
                "widths": [36, 78, 68],
            },
            {
                "title": "Architecture B — SKU gate (do not fake the lab)",
                "columns": ["SKU", "Slots?", "What to do today"],
                "rows": [
                    ["F1 / D1 / Shared", "No", "Write the warm-up path + SKU note. Do not claim swap"],
                    ["B1 Basic", "No slots on Basic", "Same — document, or bump to S1 for a short lab"],
                    ["S1 Standard / P*", "Yes (staging + more on higher)", "Create staging, deploy, smoke, swap, swap back"],
                    ["Functions Consumption", "Not the App Service slot story", "Premium/Dedicated Functions if you need slots"],
                ],
                "widths": [44, 48, 90],
            },
            {
                "title": "Architecture C — pitfalls that swap the wrong outfit",
                "columns": ["Pitfall", "What you see", "Fix"],
                "rows": [
                    ["No sticky settings", "Staging DB URL becomes production's", "Mark secrets/flags as slot settings before swap"],
                    ["Skip warm-up", "First users after swap hit cold start / 503", "Hit staging until ready; then swap"],
                    ["Auto-swap on", "Every staging deploy flips prod", "Off until smoke is a real check, not a glance"],
                    ["Deploy to production slot", "You never used the dressing room", "AzureWebApp@1 deployToSlotOrASE: true  slot: staging"],
                ],
                "widths": [42, 70, 70],
            },
        ],
        "one_liner": "Slots are dressing rooms for production — try the outfit on, warm it, then walk the runway. Swap back if it rips.",
        "lab_intro": "Personal subscription + personal org. Slots need Standard S1+ (not F1). If you will not spend, the document still ships.",
        "lab": [
            "Portal → your web app → Deployment slots. If Add is disabled, you are on F1/Basic. Record the SKU. Do not lie that you swapped.",
            "If you bump: az appservice plan update --sku S1 (short window). Create slot staging. Remember S1 costs — delete same night.",
            "Deploy the same drop to staging (deployToSlotOrASE + resourceName: staging). Do not rebuild.",
            "Smoke the staging URL (default hostname -<slot>.azurewebsites.net). Hit it until the app is actually up.",
            "az webapp deployment slot swap -g <rg> -n <app> --slot staging --target-slot production. Confirm production URL. Swap back once (rollback practice).",
            "Write docs/slots-warmup-day34.md: warm-up path, sticky settings, auto-swap = off. Include 'SKU blocked slots' if it did.",
        ],
        "code_title": "Deploy to staging + swap (S1+ only)",
        "code": """- task: AzureWebApp@1
  inputs:
    azureSubscription: azure-100-sc
    appName: app-day32-<unique>
    deployToSlotOrASE: true
    resourceGroupName: rg-day32-lab
    slotName: staging
    package: $(Pipeline.Workspace)/ci/drop/**/*.zip

# after smoke on https://app-day32-<unique>-staging.azurewebsites.net
az webapp deployment slot swap -g rg-day32-lab -n app-day32-<unique> \\
  --slot staging --target-slot production
""",
        "checklist": [
            "Know F1 has no slots; S1+ does",
            "Warm-up path written even if SKU blocked the lab",
            "If you swapped: you also swapped back once",
            "S1 plan not left running overnight without a reason",
        ],
        "tomorrow": "Blue-green — two worlds, one traffic pointer. On App Service that map is prod slot + staging.",
    },
    35: {
        "topic": "Blue-Green Deployments",
        "subtitle": "Two complete worlds, one pointer. Rollback is a light switch — only if you kept the previous artifact",
        "phase": "4 - Continuous Delivery",
        "tables": [
            {
                "title": "Architecture A — blue-green mapped onto App Service slots",
                "columns": ["Idea", "App Service lab map", "Not this"],
                "rows": [
                    ["Blue (live)", "Production slot + production hostname", "A single in-place zip overwrite"],
                    ["Green (candidate)", "staging slot, smoked, still idle to users", "A branch named green with no second host"],
                    ["Cutover", "Swap (VIP flip) — 100% in one move", "A 5% traffic ramp (that is canary, Day 36)"],
                    ["Rollback", "Swap back; same two worlds", "Rebuild last week's commit from a laptop"],
                    ["AKS later", "Two Deployments + Service/Ingress flip", "Not today's cluster bill"],
                ],
                "widths": [34, 80, 68],
            },
            {
                "title": "Architecture B — when blue-green is the right switch",
                "columns": ["Constraint", "Prefer blue-green", "Prefer something else"],
                "rows": [
                    ["Need instant rollback", "Yes — flip the pointer", "Rolling (Day 37) rolls back in batches"],
                    ["Cannot pay for two worlds", "Slots on one plan (lab-sized)", "In-place deploy + accept downtime"],
                    ["Need a small slice of users first", "No — that is canary", "Day 36 traffic % or a feature flag"],
                    ["N and N-1 cannot coexist", "Green is isolated; cutover is atomic", "Do not roll; do not mix versions on one fleet"],
                ],
                "widths": [48, 67, 67],
            },
            {
                "title": "Architecture C — pitfalls that turn rollback into archaeology",
                "columns": ["Pitfall", "What you see", "Fix"],
                "rows": [
                    ["No previous drop", "Swap back lands old slot with new bits already", "Keep artifact drop N-1 for a written window (lab: 7 days)"],
                    ["Vanity health", "200 on / that never touches a dependency", "Smoke as a user: a path that hits data if you have data"],
                    ["Called it blue-green", "One slot, one deploy, a blog title", "If there is no idle world, there is no switch"],
                    ["Schema change first", "Green needs a column blue cannot read", "Expand/contract the data before the flip"],
                ],
                "widths": [40, 71, 71],
            },
        ],
        "one_liner": "Blue-green means two worlds; only one takes traffic — rollback is a light switch, not an archaeology dig.",
        "lab_intro": "Personal Azure / Azure DevOps only. If slots are unavailable, the rollback document still ships. No employer diagrams.",
        "lab": [
            "Draw blue = production slot, green = staging, pointer = swap. One box each in docs/rollback.md (or a comment sketch).",
            "Write docs/rollback.md with three numbered steps: (1) swap back staging/production, (2) verify a real URL, (3) keep previous pipeline artifact 7 days.",
            "If S1+ slots exist from Day 34: deploy N to green, smoke, swap (blue↔green), then swap back using only the doc.",
            "Record the artifact run ID you would keep as N-1. CD must download that drop — not rebuild.",
            "Add a sentence on schema: if green needs a breaking column, the switch is unsafe until expand/contract.",
            "Do not stand up AKS for this metaphor. Slots are the lab-sized two worlds.",
        ],
        "code_title": "rollback.md — the switch, not a scavenger hunt",
        "code": """# docs/rollback.md
# Blue = production slot. Green = staging. Pointer = swap.
# 1. az webapp deployment slot swap -g <rg> -n <app> --slot staging --target-slot production
#    (swap back is the same command after another swap, or swap again)
# 2. curl -fI https://<app>.azurewebsites.net/  (use a path that hits a dependency if you have one)
# 3. Keep Pipeline artifact 'drop' from run <BuildId> for 7 days — do not rebuild that commit.
""",
        "checklist": [
            "Can distinguish blue-green (100% flip) from canary (ramp)",
            "docs/rollback.md has swap, verify, keep artifact",
            "Did not call a single-slot deploy blue-green",
            "No AKS spend today",
        ],
        "tomorrow": "Canary releases — a small slice of real traffic, a watch, and an abort that is faster than a debate.",
    },
    36: {
        "topic": "Canary Releases",
        "subtitle": "A percentage is not a canary. A watch plus a named abort is. Averages hide a dying bird",
        "phase": "4 - Continuous Delivery",
        "tables": [
            {
                "title": "Architecture A — three ways to expose a small risk",
                "columns": ["Mechanism", "What moves", "Azure lab knob"],
                "rows": [
                    ["Slot traffic %", "Fraction of requests to staging slot", "App Service Testing in production (Standard+)"],
                    ["Feature flag", "Code path on/off per user/cohort", "App Configuration / your own flag — no fleet split"],
                    ["Revision weight", "Later: Container Apps / API Management", "Not required today"],
                    ["Abort", "0% / flag off / swap back", "Must be named before the ramp starts"],
                    ["Watch", "5xx, latency, a business heartbeat on the canary only", "Do not watch the blended average"],
                ],
                "widths": [36, 74, 72],
            },
            {
                "title": "Architecture B — ramp vs blue-green vs flag",
                "columns": ["Goal", "Choose", "Skip"],
                "rows": [
                    ["Prove on 5% of real users", "Canary traffic split + isolated metrics", "Blue-green 100% flip"],
                    ["Hide a path with no split", "Feature flag", "Calling a flag a canary without traffic"],
                    ["Instant all-or-nothing rollback", "Blue-green swap (Day 35)", "A 40-minute ramp you cannot stop"],
                    ["No Standard SKU", "Paper plan + abort metric — still the lab", "Claiming Testing-in-prod on F1"],
                ],
                "widths": [48, 72, 62],
            },
            {
                "title": "Architecture C — pitfalls that lunch through the watch",
                "columns": ["Pitfall", "What you see", "Fix"],
                "rows": [
                    ["Blended dashboard", "Error rate 'fine' while 5% is on fire", "Filter by slot / revision / flag"],
                    ["No abort signal", "Team debates in chat at 12%", "Write: 5xx > N for 15 min → 0%"],
                    ["5% then lunch", "Unattended experiment on customers", "15 min watch is a calendar block, not a vibe"],
                    ["Flag + split, no diagram", "Nobody knows who saw what", "Pick one mechanism for the paper plan"],
                ],
                "widths": [40, 71, 71],
            },
        ],
        "one_liner": "Canaries in coal mines and canaries in prod share a job: die early so the rest of us don't — write the abort before the ramp.",
        "lab_intro": "Personal Azure only. Paper plan is mandatory. Testing-in-production is optional and SKU-gated.",
        "lab": [
            "Write docs/canary-plan-day36.md for your webapp: 5% → watch 15 min → 25% → watch → 100% or abort.",
            "Name the abort metric in that file (example: 5xx rate on the canary slot, or a failed heartbeat). If you cannot name it, you do not have a canary.",
            "Portal → Web app → Deployment slots → Testing in production (if present). Note whether routing % exists on your SKU.",
            "If routing exists: send 5% to staging for a few minutes, then 0%. Do not leave a split overnight.",
            "Add one sentence: flag vs traffic split — which one this lab would use and why (not both).",
            "State that blended averages are forbidden as the watch. Isolated canary metrics only.",
        ],
        "code_title": "Canary checklist (paper is the product; CLI is optional)",
        "code": """# docs/canary-plan-day36.md
# Ramp: 5% (15 min) → 25% (15 min) → 100% or abort
# Abort: canary-slot 5xx > 2% for 5 min → set routing to 0% (or swap back)
# Watch: slot-filtered metrics, not the app-wide average
# Mechanism this lab: traffic % on staging  |  feature flag  (pick one)
#
# Optional (Standard+): Portal → Testing in production → route % to staging
# az webapp traffic-routing set -g <rg> -n <app> --distribution staging=5
""",
        "checklist": [
            "Abort metric is written, not 'we will see'",
            "Ramp times are on the page",
            "Know Testing-in-prod is SKU-gated",
            "Did not leave a traffic split running",
        ],
        "tomorrow": "Rolling deployments — change tires while moving; N and N-1 must coexist or you scheduled a partial outage.",
    },
    37: {
        "topic": "Rolling Deployments",
        "subtitle": "Batches replace instances while traffic still flows. Rollback is another movie — not a light switch",
        "phase": "4 - Continuous Delivery",
        "tables": [
            {
                "title": "Architecture A — where rolling actually lives (concepts; no AKS bill)",
                "columns": ["Platform", "Knob", "Mixed versions?"],
                "rows": [
                    ["VMSS", "upgradePolicy mode: Rolling; maxBatchInstancePercent; pauseTimeBetweenBatches", "Yes, during the wave"],
                    ["AKS Deployment", "strategy.rollingUpdate maxUnavailable / maxSurge", "Yes, until the ReplicaSet drains"],
                    ["App Service", "Instance replacement / restart — not the same as VMSS rolling", "Usually a new zip on the fleet, not a designed N/N-1 wave"],
                    ["Slots / blue-green", "Not rolling — idle world + flip", "No mix on the live pointer"],
                    ["Canary", "Not rolling — % of traffic, maybe one slot", "Old + new by request share"],
                ],
                "widths": [36, 92, 54],
            },
            {
                "title": "Architecture B — pick with downtime, complexity, rollback",
                "columns": ["Strategy", "Downtime / mix", "Rollback"],
                "rows": [
                    ["Rolling", "Low downtime; N and N-1 live together", "Slower — roll forward to old bits in batches"],
                    ["Blue-green", "Near-zero cutover; no mix on the pointer", "Fast swap if you paid for two worlds"],
                    ["Canary", "Near-zero; small mix by design", "Stop the ramp / 0% / flag off"],
                    ["In-place", "Possible blip; one world", "Redeploy previous artifact (you kept it)"],
                ],
                "widths": [36, 78, 68],
            },
            {
                "title": "Architecture C — pitfalls that make 'zero downtime' half-broken",
                "columns": ["Pitfall", "What you see", "Fix"],
                "rows": [
                    ["Breaking API in the wave", "20 minutes of mixed clients/servers", "N-1 compatibility or do not roll"],
                    ["Breaking schema first", "Old instances write, new ones migrate", "Expand/contract. Rolling is not a migration tool"],
                    ["maxUnavailable: 100%", "You invented an outage with extra YAML", "Small batches; wait for healthy"],
                    ["Called App Service zip a rolling deploy", "One restart, a blog title", "Use the comparison table; stay honest"],
                ],
                "widths": [48, 67, 67],
            },
        ],
        "one_liner": "Rolling deploys change the tires while the car is moving — thrilling, and occasionally stupid if N and N-1 cannot share the road.",
        "lab_intro": "Personal repo only. No AKS, no VMSS spend required. The product today is a comparison you could defend in a design review.",
        "lab": [
            "Create docs/deploy-strategies-day37.md with a table: Strategy | Downtime | Complexity | Rollback | Mixed versions? for Rolling, Blue-green, Canary, In-place.",
            "Fill every cell with something specific (swap, maxUnavailable, 5% ramp) — not 'low' / 'high' alone.",
            "Write one scenario where rolling is wrong (breaking API or breaking schema) and which strategy you would pick instead.",
            "Skim Learn: VMSS rolling upgrade OR Kubernetes rolling updates. Note one knob name in the doc (maxBatchInstancePercent or maxUnavailable).",
            "Do not create AKS or a scale set for this lab. Cost is not a badge.",
            "Cross-link docs/rollback.md (Day 35) and docs/canary-plan-day36.md so the three docs agree.",
        ],
        "code_title": "Comparison table (markdown you actually keep)",
        "code": """# docs/deploy-strategies-day37.md
# Strategy    | Downtime      | Mix N/N-1 | Rollback
# Rolling     | Low           | Yes       | Batches of the old bits (slow)
# Blue-green  | Near-zero     | No*       | Swap / flip pointer
# Canary      | Near-zero     | By %      | Stop ramp / 0%
# In-place    | Possible blip | Brief     | Redeploy kept artifact
# *live pointer is one color; green is idle
# Kubernetes sketch (do not apply today):
# spec.strategy.rollingUpdate: { maxUnavailable: 25%, maxSurge: 25% }
""",
        "checklist": [
            "Table exists with rollback + mixed-version columns",
            "Can explain why breaking changes forbid rolling",
            "No AKS/VMSS created for a metaphor",
            "Docs agree with Days 35–36",
        ],
        "tomorrow": "Approval gates and environments — checks live on the Environment, not in Slack.",
    },
    38: {
        "topic": "Approval Gates & Environments",
        "subtitle": "Checks hang on the Environment. A deployment job is the hook. Slack thumbs-up is not an audit trail",
        "phase": "4 - Continuous Delivery",
        "tables": [
            {
                "title": "Architecture A — Environment + check + deployment job",
                "columns": ["Object", "Where you create it", "What it does"],
                "rows": [
                    ["Environment", "Pipelines → Environments → prod", "History, checks, optional resource links"],
                    ["Check: Approvals", "Environment → ⋮ → Approvals and checks", "Pre-deploy: named users/groups must Approve"],
                    ["Other checks", "Business hours, REST, invoke Azure Function, exclusive lock", "Literacy. Lab = Approvals"],
                    ["deployment job", "deployment: ProdDeploy  environment: prod", "The only job type checks reliably attach to"],
                    ["YAML approver list", "Does not live in YAML", "UI on the Environment. Review the object, not a comment"],
                ],
                "widths": [36, 78, 68],
            },
            {
                "title": "Architecture B — where to put the speed bump",
                "columns": ["Environment", "Check?", "Why"],
                "rows": [
                    ["dev", "Usually none in a personal lab", "Feedback speed. Still a real Environment object"],
                    ["staging", "Optional", "If staging is a shared proof, bump once"],
                    ["prod", "Approvals: you (personal account)", "The 3am self-own brake"],
                    ["Chat approval only", "Never as the only gate", "No run record; no Reject path"],
                ],
                "widths": [40, 62, 80],
            },
            {
                "title": "Architecture C — pitfalls that Approve in your head",
                "columns": ["Pitfall", "What you see", "Fix"],
                "rows": [
                    ["job: with environment:", "Check never fires; job just runs", "Change to deployment: + runOnce.deploy"],
                    ["Wrong environment name", "prod in YAML, Production in UI", "Exact string match"],
                    ["Only ever Approve", "First Reject feels like an outage", "Practice Reject once; job must stop"],
                    ["Gate instead of tests", "Human stares at a 200MB zip", "Approvals catch process; tests catch product"],
                ],
                "widths": [42, 70, 70],
            },
        ],
        "one_liner": "Approvals are speed bumps before prod — annoying until the day they stop a 3am self-own. Reject is a path you must practice.",
        "lab_intro": "Personal Azure DevOps org only. Project azure-100-labs. You are the only approver. Invite nobody from work.",
        "lab": [
            "Pipelines → Environments → New → name: prod (create empty). Open Approvals and checks → + → Approvals → add your personal account → Create.",
            "Point a deployment job at environment: prod (extend Day 31 YAML or a tiny echo pipeline). Regular job: will not do.",
            "Run the pipeline. Confirm it waits on Approval. Click Approve. Confirm deploy steps run.",
            "Run again. Click Reject. Confirm the job fails/stops and does not execute the deploy script.",
            "If Reject still deploys, the check is on a different Environment than the job. Fix the name; rerun.",
            "Save both run URLs in docs/approvals-day38.md. That is the audit trail Slack never was.",
        ],
        "code_title": "deployment job hooked to environment prod (check is in the UI)",
        "code": """# Pipelines → Environments → prod → Approvals and checks → Approvals
# Approvers: <your personal account>   Timeout: 1 hour is enough for a lab
stages:
- stage: Prod
  jobs:
  - deployment: ProdDeploy
    environment: prod
    pool: { vmImage: ubuntu-latest}
    strategy:
      runOnce:
        deploy:
          steps:
          - script: echo "Only runs after Approve. Reject must skip this."
            displayName: Gated echo
""",
        "checklist": [
            "Environment prod has an Approvals check with your personal account",
            "A deployment job waited; Approve ran the echo",
            "Reject stopped the deploy script",
            "Both run URLs recorded; no work accounts invited",
        ],
        "tomorrow": "Multi-environment pipeline — Dev → Staging → Prod, same drop, approvals on the last stage.",
    },
    39: {
        "topic": "Multi-environment Pipeline",
        "subtitle": "Promote the artifact, not the vibes. dependsOn is the chain. Prod does not get a second compile",
        "phase": "4 - Continuous Delivery",
        "tables": [
            {
                "title": "Architecture A — one run, one drop, three environments",
                "columns": ["Stage", "Job type", "Consumes"],
                "rows": [
                    ["CI (or reuse resources.pipelines)", "job: Build + PublishPipelineArtifact@1", "Source. Produces artifact drop"],
                    ["Dev", "deployment:  environment: dev", "download: current  artifact: drop"],
                    ["Staging", "deployment:  dependsOn: Dev", "The same drop. Different app settings"],
                    ["Prod", "deployment:  environment: prod  dependsOn: Staging", "The same drop. Approvals check from Day 38"],
                    ["Config", "App settings / variable groups per env", "Not a new zip. Bits stay identical"],
                ],
                "widths": [48, 70, 64],
            },
            {
                "title": "Architecture B — promotion rules",
                "columns": ["Rule", "YAML / practice", "Violation"],
                "rows": [
                    ["Build once", "Publish in CI only", "dotnet publish / npm run build in Prod"],
                    ["Chain", "Staging dependsOn: Dev; Prod dependsOn: Staging", "dependsOn: [] on Prod because 'we are late'"],
                    ["Brake on pain", "Checks on prod Environment", "Approvals on Dev that teach people to click through"],
                    ["Budget", "Prod may echo if no App Service today", "Rebuilding 'just to have a real prod'"],
                ],
                "widths": [32, 78, 72],
            },
            {
                "title": "Architecture C — pitfalls that invent 'works in staging' ghosts",
                "columns": ["Pitfall", "What you see", "Fix"],
                "rows": [
                    ["Rebuild per env", "Staging Monday; Prod Tuesday; different transitive dep", "download the drop. Never restore again"],
                    ["download: none", "Deploy job compiles from checkout", "download: current (same run) or download: ci"],
                    ["Config baked in zip", "Staging connection string shipped to Prod", "Slot settings / env vars; bits stay dumb"],
                    ["Skipped Staging", "Prod waited on Dev only", "dependsOn: Staging even when Staging is echo"],
                ],
                "widths": [40, 71, 71],
            },
        ],
        "one_liner": "Promote the artifact, not the vibes — rebuilds between envs invent 'works in staging' ghosts.",
        "lab_intro": "Personal Azure DevOps org only. Project azure-100-labs. Environments dev and prod already exist. Add staging. Personal Azure optional.",
        "lab": [
            "Pipelines → Environments → New → staging (empty). Keep prod's Approvals check from Day 38.",
            "Write pipelines/multi-env.yml: stages Dev → Staging → Prod with dependsOn chain. Each is a deployment job.",
            "CI publishes drop. Each env stage downloads it (download: current artifact: drop). No compile/publish in those stages.",
            "Dev and Staging can echo if you are not spending. Prod must wait on the environment: prod approval.",
            "Run once. Graph should show Dev, then Staging, then waiting on Approve — not three independent builds.",
            "If any stage runs npm/dotnet/mvn, delete those steps. Config differences belong in variable groups, not a second artifact.",
        ],
        "code_title": "Starter YAML — three stages, one drop, approval on prod",
        "code": """# pipelines/multi-env.yml
trigger: none
stages:
- stage: CI
  jobs:
  - job: Build
    pool: { vmImage: ubuntu-latest }
    steps:
    - script: echo "CI bits" > $(Build.ArtifactStagingDirectory)/app.txt
    - task: PublishPipelineArtifact@1
      inputs: { targetPath: $(Build.ArtifactStagingDirectory), artifact: drop }
- stage: Dev
  dependsOn: CI
  jobs:
  - deployment: DeployDev
    environment: dev
    strategy:
      runOnce:
        deploy:
          steps:
          - download: current
            artifact: drop
          - script: echo "Dev gets $(Pipeline.Workspace)/drop — no rebuild"
- stage: Staging
  dependsOn: Dev
  jobs:
  - deployment: DeployStaging
    environment: staging
    strategy:
      runOnce:
        deploy:
          steps:
          - download: current
            artifact: drop
          - script: echo "Staging gets the same drop"
- stage: Prod
  dependsOn: Staging
  jobs:
  - deployment: DeployProd
    environment: prod
    strategy:
      runOnce:
        deploy:
          steps:
          - download: current
            artifact: drop
          - script: echo "Prod waits on Environment checks, then same drop"
""",
        "checklist": [
            "dependsOn chain is Dev → Staging → Prod",
            "Every env stage downloads drop; none rebuild",
            "Prod waited on the Approvals check",
            "Can explain why a second compile is a second dice roll",
        ],
        "tomorrow": "Phase 4 mini project — green path with visible brakes, same artifact, recap without heroics.",
    },
    40: {
        "topic": "Mini Project + Recap (Phase 4)",
        "subtitle": "Shipping is a pipeline with brakes: artifact, environments, a traffic strategy, a rollback that is not a scavenger hunt",
        "phase": "4 - Continuous Delivery",
        "tables": [
            {
                "title": "Architecture A — Phase 4 map (Days 31–39)",
                "columns": ["Day", "Object", "Keep"],
                "rows": [
                    ["31", "deployment job + environment", "YAML CD, not Classic as source of truth"],
                    ["32–33", "AzureWebApp@1 vs AzureFunctionApp@2", "Web site vs event + plan that can sleep"],
                    ["34–35", "Slots / swap = dressing room / blue-green pointer", "F1 has no slots; rollback.md exists anyway"],
                    ["36–37", "Canary ramp vs rolling batches", "Abort metric; N/N-1 compatibility"],
                    ["38–39", "Environment checks + promote drop", "Reject works; Prod does not rebuild"],
                ],
                "widths": [28, 78, 76],
            },
            {
                "title": "Architecture B — definition of done for the mini project",
                "columns": ["Bar", "Pass", "Fail"],
                "rows": [
                    ["Path", "One run Dev → Staging → Prod (prod may echo)", "Three unrelated pipelines"],
                    ["Brake", "Visible Approval wait + a Reject run saved", "YOLO button on prod"],
                    ["Bits", "Same drop ID in every deploy log", "dotnet/npm/mvn in a deploy stage"],
                    ["Rollback", "docs/rollback.md still true", "Rollback = 'we will figure it out'"],
                ],
                "widths": [28, 82, 72],
            },
            {
                "title": "Architecture C — recap failures",
                "columns": ["Pitfall", "What you see", "Fix"],
                "rows": [
                    ["Classic leftover", "A Release still firing on the same app", "Disable it. YAML is the street"],
                    ["Prod rebuilt", "Ghost from Day 39 still in the run", "Not a recap until download: current"],
                    ["S1 left on", "Cost Management is the recap", "Delete RG or scale to F1 / destroy"],
                    ["No screenshot of the wait", "You remember the gate; the post cannot show it", "Capture the Approval banner, no secrets"],
                ],
                "widths": [40, 71, 71],
            },
        ],
        "one_liner": "Phase 4 recap: shipping is a pipeline with brakes, not a YOLO button — and the bits you promote are the bits you tested.",
        "lab_intro": "Personal Azure DevOps org + personal subscription leftovers only. Project azure-100-labs.",
        "lab": [
            "Run pipelines/multi-env.yml (or equivalent) end to end. Approve prod. Save the run URL.",
            "Confirm each deploy stage lists the same drop / BuildId. If not, fix YAML before writing the recap.",
            "Keep docs/rollback.md, canary-plan, and deploy-strategies. Add docs/phase4-recap.md: artifact, env, strategy, brake.",
            "Delete leftover rg-day32-lab / rg-day33-lab / S1 plans unless you have a written reason. Echo prod is a valid budget choice.",
            "Screenshot the Approval wait (no variable values). That boring picture is the definition of done.",
            "Personal learning recap only. No employer story, no client names.",
        ],
        "code_title": "Recap receipt — same drop through the chain",
        "code": """# Definition of done (put in docs/phase4-recap.md)
# - Pipeline run <id>: CI published drop
# - Dev downloaded drop (no compile)
# - Staging downloaded drop (no compile)
# - Prod waited on Environment prod Approvals, then downloaded drop
# - Reject run <id> exists from Day 38
# - az group list | leftover lab RGs scheduled for delete
""",
        "checklist": [
            "One run with visible approval and logs saved",
            "Same artifact promoted — no rebuild in CD",
            "docs/phase4-recap.md written",
            "Cost leftovers deleted or listed",
        ],
        "tomorrow": "IaC concepts — declarative vs imperative, idempotency, drift, and picking Bicep or Terraform (one).",
    },
    41: {
        "topic": "IaC Concepts",
        "subtitle": "If it is not in code, it is a rumor. Declarative desired state, idempotent apply, drift is the Portal's revenge",
        "phase": "5 - Infrastructure as Code",
        "tables": [
            {
                "title": "Architecture A — three ways to change Azure, only two are IaC",
                "columns": ["Style", "What you write", "Engine"],
                "rows": [
                    ["Imperative script", "az group create; az storage account create …", "You. Second run often duplicates or errors"],
                    ["Declarative ARM/Bicep", "resources: desired JSON/Bicep", "ARM control plane. Deployment history in Azure"],
                    ["Declarative Terraform", "resource \"azurerm_*\"", "Plan/apply + state file mapping address → Azure ID"],
                    ["Click-ops", "Portal clicks", "A rumor. No PR, no diff, no rollback of intent"],
                    ["Idempotency test", "Apply twice", "Same world. If you get two of everything, it was a script"],
                ],
                "widths": [40, 72, 70],
            },
            {
                "title": "Architecture B — pick one primary tool for Phase 5",
                "columns": ["Pick", "When it fits a personal lab", "Cost of picking both as primary"],
                "rows": [
                    ["Bicep", "Azure-native, no state file, what-if, modules", "You will still read ARM errors — that is a feature"],
                    ["Terraform", "State, locking, modules, travels off Azure later", "You now operate terraform.tfstate like production data"],
                    ["ARM JSON only", "Literacy (Days 42–43), not the mini project default", "Eye strain without Bicep's compiler"],
                    ["Both as 'primary'", "Never for this phase", "Two half-labs. Pick one; skim the other"],
                ],
                "widths": [36, 78, 68],
            },
            {
                "title": "Architecture C — drift and other rumors",
                "columns": ["Pitfall", "What you see", "Fix"],
                "rows": [
                    ["Portal snowflake", "Firewall rule that exists only in prod", "what-if / terraform plan before the next apply"],
                    ["Script of creates", "Second apply: name already taken", "Declarative resource with a unique name function"],
                    ["No decision record", "Day 50 you cannot say why you picked the tool", "docs/iac-why.md today"],
                    ["Treating drift as 'ops'", "File green, Azure fork", "Either import/correct the file or the click was an incident"],
                ],
                "widths": [40, 71, 71],
            },
        ],
        "one_liner": "If it is not in code, it is a rumor — IaC turns 'someone clicked prod' into a diff.",
        "lab_intro": "Personal repo azure-100-labs. No employer landing-zone stories. You will still touch the non-primary tool for literacy.",
        "lab": [
            "Write docs/iac-why.md: one drift you have actually seen (SKU bump, extra firewall rule, lock only in prod) — keep it generic, no client names.",
            "Decision record in the same file: Tool: Bicep | Terraform. Reason: one paragraph. Not 'both'.",
            "Add a two-line glossary: declarative = desired state; idempotent = apply twice, one world.",
            "List the complementary tool as literacy only (ARM JSON if Bicep; Bicep sample if Terraform).",
            "Do not deploy anything yet. Day 42 is broccoli (ARM). Day 44/46 is the primary track.",
            "Commit the ADR on a personal branch. Invite nobody.",
        ],
        "code_title": "Decision record stub",
        "code": """# docs/iac-why.md
# Drift I have seen: ________________________________
# Primary tool for Phase 5:  Bicep  |  Terraform
# Reason: __________________________________________
# Literacy (not primary): ARM JSON always; the other DSL skimmed
# Idempotency test I will use: apply twice to rg-dayNN-lab, expect 0 extra resources
""",
        "checklist": [
            "Primary tool chosen with a reason, not a personality",
            "Drift example written without employer/client names",
            "Can define declarative vs imperative in one sentence each",
            "No Azure spend today",
        ],
        "tomorrow": "ARM templates basics — $schema, apiVersion, az deployment group create. Literacy, not a love affair.",
    },
    42: {
        "topic": "ARM Templates Basics",
        "subtitle": "Every Portal click is still an ARM call. JSON is broccoli: nutritious, rarely anyone's favorite",
        "phase": "5 - Infrastructure as Code",
        "tables": [
            {
                "title": "Architecture A — template anatomy (load-bearing boredom)",
                "columns": ["Key", "Role", "Lab value"],
                "rows": [
                    ["$schema", "JSON schema for validation", "2019-04-01/deploymentTemplate.json#"],
                    ["contentVersion", "Your version, not apiVersion", "10.0.0.1"],
                    ["parameters / variables", "Dials and locals (deep dive Day 43)", "Can be empty today"],
                    ["resources[]", "type + apiVersion + name + properties", "Microsoft.Storage/storageAccounts@2023-01-01"],
                    ["outputs", "Handshake to the next stack", "Optional today; required tomorrow"],
                    ["mode", "Incremental (default) vs Complete", "Complete can delete extras. Do not use Complete on a busy RG"],
                ],
                "widths": [36, 72, 74],
            },
            {
                "title": "Architecture B — how this relates to Bicep and Terraform",
                "columns": ["Tool", "Talks to", "You still need ARM literacy because"],
                "rows": [
                    ["ARM JSON", "ARM deployments API directly", "Error text and export-template dumps are JSON"],
                    ["Bicep", "Compiles to ARM, then the same API", "Failed deploy details show ARM resource IDs / apiVersion"],
                    ["Terraform azurerm", "ARM via the provider", "The resource type names are the ARM types in snake_case"],
                    ["Portal export", "A start that includes defaults you did not choose", "Read it; do not worship it"],
                ],
                "widths": [32, 64, 86],
            },
            {
                "title": "Architecture C — pitfalls that deploy 2016 into 2026",
                "columns": ["Pitfall", "What you see", "Fix"],
                "rows": [
                    ["Stale apiVersion", "Property not allowed / missing SKU fields", "Pin a current apiVersion from Learn, not a 2016 gist"],
                    ["Hardcoded storage name", "AlreadyExists globally", "uniqueString(resourceGroup().id) concat"],
                    ["Complete mode on shared RG", "Unrelated resources deleted", "Incremental. Separate rg-day42-lab"],
                    ["Leaving the account", "LRS storage still meters", "az group delete after the proof"],
                ],
                "widths": [44, 69, 69],
            },
        ],
        "one_liner": "ARM JSON is the broccoli of Azure — nutritious, rarely anyone's favorite. Eat a forkful so Bicep and Terraform errors make sense.",
        "lab_intro": "Personal subscription. RG rg-day42-lab. Delete tonight. This is literacy even if Terraform is your primary.",
        "lab": [
            "az group create -n rg-day42-lab -l centralindia on the personal subscription.",
            "Save infra/storage.json (starter). Confirm type Microsoft.Storage/storageAccounts and a real apiVersion.",
            "az deployment group create -g rg-day42-lab -n stor -f infra/storage.json. Wait for Succeeded.",
            "az storage account list -g rg-day42-lab -o table. Note the unique name ARM computed.",
            "Open the deployment in Portal → RG → Deployments → stor. That history is ARM's receipt (no Terraform state here).",
            "az group delete -n rg-day42-lab --yes --no-wait. Broccoli does not need to live in Cost Management.",
        ],
        "code_title": "Tiny storage ARM template + deploy",
        "code": """# infra/storage.json — save as JSON, then:
# az deployment group create -g rg-day42-lab -n stor -f infra/storage.json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "10.0.0.1",
  "resources": [
    {
      "type": "Microsoft.Storage/storageAccounts",
      "apiVersion": "2023-01-01",
      "name": "[concat('st', uniqueString(resourceGroup().id))]",
      "location": "[resourceGroup().location]",
      "sku": { "name": "Standard_LRS" },
      "kind": "StorageV2",
      "properties": { "allowBlobPublicAccess": false }
    }
  ]
}
""",
        "checklist": [
            "Can name $schema, contentVersion, resources, apiVersion",
            "One successful az deployment group create",
            "Know Incremental vs Complete well enough to fear Complete",
            "rg-day42-lab deleted",
        ],
        "tomorrow": "ARM parameters and outputs — dials in a .parameters.json, handshake via outputs, not hardcoded landfill names.",
    },
    43: {
        "topic": "ARM Parameters & Outputs",
        "subtitle": "Parameters are the dials. Outputs are the handshake. Hardcoded names are how labs become landfills",
        "phase": "5 - Infrastructure as Code",
        "tables": [
            {
                "title": "Architecture A — parameters, variables, outputs",
                "columns": ["Piece", "Lives in", "Consumed by"],
                "rows": [
                    ["parameters", "template + @main.parameters.json", "az deployment group create -p @file.json"],
                    ["variables", "template only (computed)", "Not overridden at deploy time"],
                    ["outputs", "template outputs: { endpoint: { value: ... } }", "Next script / pipeline; query via az deployment group show"],
                    ["uniqueString()", "expression in name", "Global uniqueness for storage/key vault"],
                    ["nested templates", "literacy — extra deployment resource", "Skip matryoshka today"],
                ],
                "widths": [36, 78, 68],
            },
            {
                "title": "Architecture B — what to parameterize",
                "columns": ["Value", "Parameter?", "Why"],
                "rows": [
                    ["location / sku name", "Yes", "Second env must not fork the template"],
                    ["secret / key", "securestring param or Key Vault ref", "Never default a real secret in JSON"],
                    ["apiVersion", "No", "That is the resource contract, not an env dial"],
                    ["storage account name", "Prefix param + uniqueString", "Fully hardcoded names collide globally"],
                ],
                "widths": [44, 64, 74],
            },
            {
                "title": "Architecture C — pitfalls",
                "columns": ["Pitfall", "What you see", "Fix"],
                "rows": [
                    ["Edited copies of main.json", "stprodprod in the wrong region", "One template, per-env parameter files"],
                    ["Forgot @ on -p", "CLI treats a path as a literal string", "-p @main.parameters.json"],
                    ["No outputs", "Next step greps the Portal", "output the blob endpoint / resourceId"],
                    ["securestring in logs", "Parameter value visible in a screenshot", "securestring; do not echo; dummy values only"],
                ],
                "widths": [42, 70, 70],
            },
        ],
        "one_liner": "Parameters are the dials; hardcoding names is how labs become landfills. Outputs are how the next stack finds the endpoint.",
        "lab_intro": "Personal subscription. RG rg-day43-lab. If Terraform is primary, still do one parameterized deploy — then delete.",
        "lab": [
            "Extend yesterday's template with parameters location and skuName, plus an output storageEndpoint.",
            "Create infra/main.parameters.json with location=centralindia (or yours) and skuName=Standard_LRS.",
            "az group create -n rg-day43-lab -l <location>. Deploy: az deployment group create -g rg-day43-lab -f infra/main.json -p @infra/main.parameters.json.",
            "az deployment group show -g rg-day43-lab -n <name> --query properties.outputs -o jsonc. Confirm the endpoint without opening Portal blades as the source of truth.",
            "If Terraform is primary: write three lines in docs/arm-params-day43.md and still complete one deploy.",
            "az group delete -n rg-day43-lab --yes --no-wait.",
        ],
        "code_title": "Parameterized deploy + output query",
        "code": """# infra/main.parameters.json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",
  "contentVersion": "10.0.0.1",
  "parameters": {
    "location": { "value": "centralindia" },
    "skuName": { "value": "Standard_LRS" }
  }
}

az deployment group create -g rg-day43-lab -n stor43 \\
  -f infra/main.json -p @infra/main.parameters.json
az deployment group show -g rg-day43-lab -n stor43 \\
  --query properties.outputs.storageEndpoint.value -o tsv
""",
        "checklist": [
            "Used -p @parameters.json (the @ matters)",
            "Output printed from CLI, not from memory",
            "No real secrets in parameter files",
            "RG deleted",
        ],
        "tomorrow": "Bicep fundamentals — same control plane, resource declarations, uniqueString, less brace sport.",
    },
    44: {
        "topic": "Bicep Fundamentals",
        "subtitle": "Bicep is ARM with the JSON horror filed down — same types, same apiVersions, a compiler you install",
        "phase": "5 - Infrastructure as Code",
        "tables": [
            {
                "title": "Architecture A — a Bicep file is an ARM deployment waiting to compile",
                "columns": ["Bicep", "Becomes", "Notes"],
                "rows": [
                    ["param location string = resourceGroup().location", "ARM parameters", "Default from the RG; still overridable"],
                    ["resource stg 'Microsoft.Storage/storageAccounts@2023-01-01'", "resources[] with that apiVersion", "Type string is the ARM type"],
                    ["sku: { name: 'Standard_LRS' }", "properties/sku in JSON", "Blocks instead of quote nests"],
                    ["name: 'st${uniqueString(resourceGroup().id)}'", "concat + uniqueString", "Stops the landfill of colliding names"],
                    ["az bicep build -f main.bicep", "main.json ARM", "You can read the broccoli it emitted"],
                ],
                "widths": [72, 50, 60],
            },
            {
                "title": "Architecture B — if this is not your primary track",
                "columns": ["Track", "Today's bar", "Skip"],
                "rows": [
                    ["Bicep primary", "az bicep install; deploy storage; delete RG", "Falling in love with JSON again"],
                    ["Terraform primary", "30 min: install, type the resource block, build to JSON", "Pretending Azure teams will never send .bicep"],
                    ["Both", "Not a track", "Pick Day 41's ADR"],
                ],
                "widths": [40, 82, 60],
            },
            {
                "title": "Architecture C — pitfalls",
                "columns": ["Pitfall", "What you see", "Fix"],
                "rows": [
                    ["No compiler", "az deployment ... .bicep fails oddly", "az bicep install; az bicep version"],
                    ["Hardcoded stmyname123", "AlreadyExists", "uniqueString(resourceGroup().id)"],
                    ["location copied in six places", "Second region = fork", "param location"],
                    ["Deploy to a leftover RG", "Complete-mode fear / name clashes", "Fresh rg-day44-lab, Incremental"],
                ],
                "widths": [44, 69, 69],
            },
        ],
        "one_liner": "Bicep is ARM with the JSON horror filed down — same control plane, less eye strain. ARM did not go away.",
        "lab_intro": "Personal subscription. RG rg-day44-lab. Bicep track deploys; Terraform track still types the block once.",
        "lab": [
            "az bicep install && az bicep version. Confirm the CLI can compile.",
            "Write infra/main.bicep from the starter. az bicep build -f infra/main.bicep and glance at the JSON once.",
            "az group create -n rg-day44-lab -l centralindia. az deployment group create -g rg-day44-lab -f infra/main.bicep.",
            "If Terraform is primary: stop after build + reading the resource symbol; optional deploy still recommended, then destroy.",
            "Confirm the storage account exists (az resource list -g rg-day44-lab -o table).",
            "az group delete -n rg-day44-lab --yes --no-wait.",
        ],
        "code_title": "main.bicep — storage with uniqueString",
        "code": """// infra/main.bicep
param location string = resourceGroup().location
param skuName string = 'Standard_LRS'

resource stg 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: 'st${uniqueString(resourceGroup().id)}'
  location: location
  sku: { name: skuName }
  kind: 'StorageV2'
  properties: { allowBlobPublicAccess: false }
}

output storageName string = stg.name
output blobEndpoint string = stg.properties.primaryEndpoints.blob

# az bicep install
# az deployment group create -g rg-day44-lab -f infra/main.bicep
""",
        "checklist": [
            "az bicep version works",
            "Resource type string includes apiVersion",
            "Name uses uniqueString, not pride",
            "RG deleted after proof",
        ],
        "tomorrow": "Bicep modules and what-if — split storage out, read Create/Modify/Delete before the audience arrives.",
    },
    45: {
        "topic": "Bicep Modules & Deployment",
        "subtitle": "Modules are boundaries. what-if is the dress rehearsal. A Delete you did not expect is an incident that has not happened yet",
        "phase": "5 - Infrastructure as Code",
        "tables": [
            {
                "title": "Architecture A — composition vs a 2,000-line main.bicep",
                "columns": ["Object", "File", "Call site"],
                "rows": [
                    ["Module", "infra/modules/storage.bicep", "params: prefix, sku, location"],
                    ["App", "infra/main.bicep", "module stg 'modules/storage.bicep' = { name: 'storage', params: { ... } }"],
                    ["what-if", "CLI against main.bicep", "az deployment group what-if — Create/Ignore/Modify/Delete"],
                    ["Deployment stacks", "Literacy: track + prune", "Not required for the lab apply"],
                    ["ARM still underneath", "Compiled JSON per module", "Errors still speak resource IDs"],
                ],
                "widths": [36, 62, 84],
            },
            {
                "title": "Architecture B — when to stop at what-if",
                "columns": ["what-if result", "Action", "Why"],
                "rows": [
                    ["Create (expected storage)", "Deploy", "Matches the file"],
                    ["Modify SKU", "Read twice, then deploy if you meant it", "SKU change can recreate"],
                    ["Delete you did not type", "Stop", "Wrong RG, Complete-mode surprise, or name change = replace"],
                    ["NoChange / Ignore", "Good", "Idempotency passing the adult test"],
                ],
                "widths": [48, 62, 72],
            },
            {
                "title": "Architecture C — pitfalls",
                "columns": ["Pitfall", "What you see", "Fix"],
                "rows": [
                    ["Name change in module", "Delete+Create of the storage account", "Treat name as identity; what-if before apply"],
                    ["Skipped what-if", "'Only a SKU change' recreates a disk", "Make what-if a required step, including in CI later"],
                    ["Module path typo", "Build fails / empty deploy", "Relative path from main.bicep"],
                    ["what-if unread in CI", "Log has a Delete, human did not look", "Eyes on Modify/Delete. Automation without eyes is a faster rumor"],
                ],
                "widths": [40, 71, 71],
            },
        ],
        "one_liner": "what-if is a dress rehearsal — read the diff before the audience (prod) arrives.",
        "lab_intro": "Personal subscription. RG rg-day45-lab. Terraform-primary: still run one what-if so the verb exists in your hands.",
        "lab": [
            "Split storage into infra/modules/storage.bicep. main.bicep only calls the module.",
            "az group create -n rg-day45-lab -l centralindia.",
            "az deployment group what-if -g rg-day45-lab -f infra/main.bicep. Read every Delete/Modify line out loud.",
            "If what-if matches intent: az deployment group create -g rg-day45-lab -f infra/main.bicep. Run what-if again — expect NoChange.",
            "If a Delete appears that you did not expect: stop. Do not 'just apply'.",
            "az group delete -n rg-day45-lab --yes --no-wait.",
        ],
        "code_title": "Module call + what-if (required manners)",
        "code": """// infra/main.bicep
param location string = resourceGroup().location
module stg 'modules/storage.bicep' = {
  name: 'storage'
  params: {
    location: location
    skuName: 'Standard_LRS'
  }
}

az deployment group what-if -g rg-day45-lab -f infra/main.bicep
# Read Create / Modify / Delete. Then, only if boring:
az deployment group create -g rg-day45-lab -f infra/main.bicep
""",
        "checklist": [
            "Storage lives in a module, not an inlined blob forever",
            "what-if run before create",
            "Second what-if is idle (idempotent) or you stopped on surprise Delete",
            "RG deleted",
        ],
        "tomorrow": "Terraform basics — init, plan, apply, destroy. State is memory; lose it and you argue with ghosts.",
    },
    46: {
        "topic": "Terraform Basics",
        "subtitle": "init / plan / apply / destroy. State is the mapping from resource addresses to Azure IDs — not a cache",
        "phase": "5 - Infrastructure as Code",
        "tables": [
            {
                "title": "Architecture A — four verbs and the file that remembers",
                "columns": ["Verb", "What it does", "Touches Azure?"],
                "rows": [
                    ["terraform init", "Download providers; later: configure backend", "No (unless backend init migrates state)"],
                    ["terraform plan", "Diff: desired config vs state vs reality (refresh)", "Read. Does not mutate (except refresh)"],
                    ["terraform apply", "Execute the plan; write terraform.tfstate", "Yes"],
                    ["terraform destroy", "Plan a teardown; remove from state as it deletes", "Yes. Adult ending for a lab"],
                    ["terraform.tfstate", "Address (azurerm_resource_group.lab) → ARM resource ID", "Lose it = ghosts: create already-exists, destroy skips live RGs"],
                ],
                "widths": [36, 86, 60],
            },
            {
                "title": "Architecture B — local state is a lab, not a team",
                "columns": ["Setup", "OK when", "Move off it when"],
                "rows": [
                    ["Local tfstate", "Today: one RG, one human, destroy tonight", "Two laptops / two applies (Day 48 remote + lock)"],
                    ["Bicep primary", "Still run the four verbs once so state is not a rumor", "Skipping Terraform entirely after Day 41 ADR"],
                    ["-auto-approve", "destroy on a disposable RG", "apply to anything you would miss"],
                    ["Partial apply", "Never as a habit", "You now have state that does not match the file"],
                ],
                "widths": [32, 78, 72],
            },
            {
                "title": "Architecture C — pitfalls that schedule amnesia",
                "columns": ["Pitfall", "What you see", "Fix"],
                "rows": [
                    ["Deleted tfstate to 'clean up'", "Next apply wants to create the RG that still exists", "Never delete state to tidy. destroy, or backend migrate"],
                    ["apply without plan", "Mental diff missed a replace", "Always read plan. Surprise = no apply"],
                    ["Skipped destroy", "Empty RG becomes a subscription hobby", "terraform destroy -auto-approve tonight"],
                    ["Committed tfstate with secrets", "Attributes in git history", "gitignore terraform.tfstate*; remote backend later"],
                ],
                "widths": [48, 67, 67],
            },
        ],
        "one_liner": "Terraform state is the memory of your infra — lose it and you are arguing with ghosts.",
        "lab_intro": "Personal PC + personal subscription. Local state on purpose. Always destroy at end of night. Do not commit tfstate.",
        "lab": [
            "Install Terraform (terraform -version). Confirm it is on PATH.",
            "New folder infra/tf-day46/. gitignore terraform.tfstate and .terraform/. Write a resource group only (starter).",
            "terraform init then terraform plan. Read the plan. Then terraform apply (type yes or -auto-approve on this disposable RG).",
            "az group show -n rg-day46-tf. Confirm reality matches state (terraform state list).",
            "Do not delete terraform.tfstate in Explorer. That is how ghosts start.",
            "terraform destroy -auto-approve. Confirm the RG is gone. If destroy fails, do not shrug — fix it tonight.",
        ],
        "code_title": "Local-state lab — RG only, then destroy",
        "code": """# infra/tf-day46/main.tf
terraform {
  required_version = ">= 1.6.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.100"
    }
  }
}
provider "azurerm" { features {} }
resource "azurerm_resource_group" "lab" {
  name     = "rg-day46-tf"
  location = "Central India"
}

# az login   # personal subscription
# terraform init
# terraform plan
# terraform apply
# terraform destroy -auto-approve
""",
        "checklist": [
            "init → plan → apply → destroy all ran",
            "tfstate is gitignored, not deleted as cleanup",
            "RG gone at the end of the night",
            "Can explain state as ID mapping, not a cache",
        ],
        "tomorrow": "Terraform with Azure (azurerm) — features {}, CLI auth, RG + storage. No subscription-Owner robot.",
    },
    47: {
        "topic": "Terraform with Azure (azurerm)",
        "subtitle": "azurerm is Terraform's Azure dialect. features {} is required. Auth today is az login, not a master-key SPN",
        "phase": "5 - Infrastructure as Code",
        "tables": [
            {
                "title": "Architecture A — provider, auth, resource graph",
                "columns": ["Piece", "HCL / CLI", "Maps to"],
                "rows": [
                    ["Provider", "required_providers hashicorp/azurerm  + features {}", "ARM APIs. Empty features {} is still required"],
                    ["Auth (lab)", "az login; az account set --subscription", "Azure CLI token. Terraform uses that context"],
                    ["RG", "azurerm_resource_group.lab", "Microsoft.Resources/resourceGroups"],
                    ["Storage", "azurerm_storage_account.lab  account_replication_type LRS", "Microsoft.Storage/storageAccounts"],
                    ["Graph", "storage.resource_group_name = azurerm_resource_group.lab.name", "Wrong ref → plan creates a second RG"],
                ],
                "widths": [28, 92, 62],
            },
            {
                "title": "Architecture B — identity for apply",
                "columns": ["Identity", "Lab?", "Later"],
                "rows": [
                    ["Your user via az login", "Yes — personal sub, short life", "Not how prod pipelines apply"],
                    ["SPN with Owner on subscription", "No", "Flamethrower. Scope to an RG, prefer WIF (Phase 7)"],
                    ["Service connection in ADO", "Day 49", "Same least-privilege rule"],
                    ["Pin provider version", "Yes (~> 3.x in required_providers)", "Floating latest is a surprise engine"],
                ],
                "widths": [52, 58, 72],
            },
            {
                "title": "Architecture C — pitfalls in the dialect",
                "columns": ["Pitfall", "What you see", "Fix"],
                "rows": [
                    ["Missing features {}", "Provider configuration invalid", "provider \"azurerm\" { features {} }"],
                    ["Wrong subscription", "Resources in a work tenant", "az account show before apply; personal only"],
                    ["Globally unique name", "StorageAccountAlreadyExists", "unique suffix; do not reuse a blog's stname"],
                    ["Plan shows extra RG", "reference used a string, not the resource", "Use .name / .id from the RG resource"],
                ],
                "widths": [40, 71, 71],
            },
        ],
        "one_liner": "azurerm is Terraform's Azure dialect — same ideas as ARM/Bicep, different accent. Do not give the dialect a master key to practice grammar.",
        "lab_intro": "Personal az login. Personal subscription. Destroy before you sleep. No work SPN.",
        "lab": [
            "az login and az account show. Confirm the personal subscription ID. az account set if it pointed at the wrong one.",
            "Extend Day 46: add azurerm_storage_account in rg-day47-tf (new RG name). Pin provider ~> 3.100.",
            "terraform plan. Confirm one RG + one storage. If you see two RGs, fix the reference.",
            "terraform apply. az storage account show -g rg-day47-tf -n <name>.",
            "No subscription-Owner service principal. Your user is enough for a lab.",
            "terraform destroy -auto-approve. Confirm both resources gone.",
        ],
        "code_title": "azurerm — RG + storage, CLI auth",
        "code": """provider "azurerm" {
  features {}
}
resource "azurerm_resource_group" "lab" {
  name     = "rg-day47-tf"
  location = "Central India"
}
resource "azurerm_storage_account" "lab" {
  name                     = "stday47xxxxx" # 3-24 lowercase; change xxxxx so it is globally unique
  resource_group_name      = azurerm_resource_group.lab.name
  location                 = azurerm_resource_group.lab.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  min_tls_version          = "TLS1_2"
}

# az login
# terraform init && terraform plan && terraform apply
# terraform destroy -auto-approve
""",
        "checklist": [
            "az account show was the personal subscription",
            "Plan showed one RG + one storage via resource references",
            "features {} present; provider version pinned",
            "destroy completed",
        ],
        "tomorrow": "Terraform modules and remote state — backend azurerm, blob lease locking, destroy order.",
    },
    48: {
        "topic": "Terraform Modules & Remote State",
        "subtitle": "Remote state in Azure Storage with a blob lease lock. Two applies at once is a tug-of-war with reality",
        "phase": "5 - Infrastructure as Code",
        "tables": [
            {
                "title": "Architecture A — backend azurerm + a module boundary",
                "columns": ["Piece", "Config", "Why"],
                "rows": [
                    ["State RG + account", "rg-tfstate / st<unique> / container tfstate", "Holds the memory. Note it costs (cheap LRS)"],
                    ["backend \"azurerm\"", "resource_group_name, storage_account_name, container_name, key", "key = lab.tfstate (path in the container)"],
                    ["Lock", "Blob lease while apply/plan (depending on version)", "Second apply waits or errors — do not force-unlock"],
                    ["Module", "modules/storage with inputs", "Reuse without three nearly identical main.tf files"],
                    ["Migrate", "Add backend; terraform init — migrate state? yes", "Do not copy tfstate like a raccoon"],
                ],
                "widths": [36, 86, 60],
            },
            {
                "title": "Architecture B — destroy order (this is the lab)",
                "columns": ["Order", "Do", "Never"],
                "rows": [
                    ["1", "destroy workload (the module stack)", "Delete the storage account from Portal first"],
                    ["2", "Confirm Azure empty for that stack", "Leave resources with remote state still pointing at them"],
                    ["3", "Only then delete rg-tfstate if you are done with Phase 5", "Destroy state while resources exist = amnesia on purpose"],
                    ["Lock stuck", "Wait / find the other apply", "terraform force-unlock because you are impatient"],
                ],
                "widths": [24, 82, 76],
            },
            {
                "title": "Architecture C — pitfalls",
                "columns": ["Pitfall", "What you see", "Fix"],
                "rows": [
                    ["Two local states", "Duplicate RGs; neither destroy is complete", "One backend, one key, locking on"],
                    ["State account in the workload RG", "You cannot destroy the RG without destroying memory", "Separate rg-tfstate from rg-day48-lab"],
                    ["force-unlock", "Two applies interleaved; duplicate names", "Treat unlock as an incident, not a shortcut"],
                    ["Module copy-paste", "Three storage blocks drifting", "module \"st\" { source = \"./modules/storage\" }"],
                ],
                "widths": [44, 69, 69],
            },
        ],
        "one_liner": "Remote state with locking stops two applies from playing tug-of-war with production. Destroy the workload before you destroy the memory.",
        "lab_intro": "Personal subscription. Separate rg-tfstate from the workload RG. Note storage cost. No force-unlock.",
        "lab": [
            "Create rg-tfstate + a Standard_LRS storage account + blob container tfstate (CLI). This account is the backend, not the app.",
            "Add terraform { backend \"azurerm\" { ... key = \"lab.tfstate\" } }. terraform init and accept state migration from local.",
            "Extract storage (or RG+storage) into modules/storage. Call it from main. terraform plan/apply through the backend once.",
            "In Azure Storage, confirm the blob lab.tfstate exists. Do not download it to email.",
            "terraform destroy the workload. Leave rg-tfstate until you are sure. If you also delete state storage, do it last.",
            "If a lock exists, wait. Do not force-unlock. Write that rule in docs/tf-state-day48.md.",
        ],
        "code_title": "backend azurerm (partial config; fill unique names)",
        "code": """terraform {
  backend "azurerm" {
    resource_group_name  = "rg-tfstate"
    storage_account_name = "sttfstate<unique>"
    container_name       = "tfstate"
    key                  = "lab.tfstate"
  }
}

# az group create -n rg-tfstate -l centralindia
# az storage account create -g rg-tfstate -n sttfstate<unique> --sku Standard_LRS
# az storage container create --account-name sttfstate<unique> -n tfstate
# terraform init   # migrate local state when prompted
# terraform plan && terraform apply
# terraform destroy   # workload first; state account last
""",
        "checklist": [
            "State lives in Azure Storage, not only on the laptop",
            "Workload RG ≠ state RG",
            "Did not force-unlock",
            "Workload destroyed; state account not deleted first",
        ],
        "tomorrow": "IaC in pipelines — plan on a clean agent, publish the plan, apply only with a brake.",
    },
    49: {
        "topic": "IaC in Pipelines",
        "subtitle": "Plan in CI on a clean agent. Apply the plan you reviewed — not a second plan nobody saw",
        "phase": "5 - Infrastructure as Code",
        "tables": [
            {
                "title": "Architecture A — plan artifact, then a gated apply",
                "columns": ["Stage", "Command", "Output"],
                "rows": [
                    ["CI Plan", "terraform plan -out=tfplan  (or az deployment group what-if)", "Reviewed diff + binary/json plan file"],
                    ["Publish", "PublishPipelineArtifact@1  artifact: tfplan", "The exact plan Apply must consume"],
                    ["Apply", "terraform apply tfplan   after approval / apply=true", "Mutates Azure. Same plan, not a fresh one"],
                    ["Bicep track", "what-if in Plan; deployment create in Apply", "Same brake. No 'it worked on my laptop'"],
                    ["Identity", "azure-100-sc scoped to the lab RG", "Not Owner on the subscription"],
                ],
                "widths": [28, 92, 62],
            },
            {
                "title": "Architecture B — brakes (pick at least one)",
                "columns": ["Brake", "YAML / UI", "Use"],
                "rows": [
                    ["Environment approval", "deployment job  environment: prod (Day 38)", "Human click before apply"],
                    ["Variable gate", "condition: and(succeeded(), eq(variables['apply'], 'true'))", "Manual run with apply=true"],
                    ["-auto-approve on apply", "Only after the gate, on the saved plan", "Never on a fresh unreviewed plan to prod"],
                    ["Laptop apply", "Homework", "Not how grown-ups change shared env"],
                ],
                "widths": [40, 86, 56],
            },
            {
                "title": "Architecture C — pitfalls that re-plan in the dark",
                "columns": ["Pitfall", "What you see", "Fix"],
                "rows": [
                    ["apply without -out", "Second plan at apply time; drift snuck in", "apply the tfplan file from the artifact"],
                    ["Plan on laptop, apply in CI", "Different env vars / different plugin versions", "Both on the same agent image + versions"],
                    ["Owner SPN", "Pipeline can delete the subscription", "Scope the service connection to rg-day49-lab"],
                    ["Auto-approve prod", "YOLO with extra YAML", "Approval or apply=true. Not hope"],
                ],
                "widths": [40, 71, 71],
            },
        ],
        "one_liner": "IaC without a pipeline is homework; IaC in a pipeline is how grown-ups change prod — apply the plan you reviewed.",
        "lab_intro": "Personal Azure DevOps org + personal subscription. Hosted ubuntu-latest. Brake required. Destroy after.",
        "lab": [
            "Pipeline stage Plan: terraform init -input=false, terraform plan -out=tfplan (Bicep: what-if). Publish tfplan (or the what-if log).",
            "Stage Apply dependsOn Plan, condition succeeded(), and either environment: prod approval or eq(variables['apply'], 'true').",
            "Apply step: terraform apply -input=false tfplan (download the artifact first). Do not run a new plan there.",
            "Queue once with apply=false / no approval path — confirm Apply skipped. Queue again with the brake released.",
            "If the apply changes something the published plan did not show, stop. Versions or backend drifted.",
            "Destroy via pipeline or local after the screenshot. Do not leave rg-day49-lab.",
        ],
        "code_title": "Plan artifact + gated apply (Terraform track)",
        "code": """# pipelines/iac.yml  (hosted ubuntu-latest)
stages:
- stage: Plan
  jobs:
  - job: PlanJob
    steps:
    - script: |
        terraform init -input=false
        terraform plan -out=tfplan
      workingDirectory: infra/tf
    - publish: infra/tf/tfplan
      artifact: tfplan
- stage: Apply
  dependsOn: Plan
  condition: and(succeeded(), eq(variables['apply'], 'true'))
  jobs:
  - deployment: ApplyJob
    environment: prod
    strategy:
      runOnce:
        deploy:
          steps:
          - download: current
            artifact: tfplan
          - script: terraform apply -input=false $(Pipeline.Workspace)/tfplan/tfplan
            workingDirectory: infra/tf
""",
        "checklist": [
            "Plan ran on the agent, not only on the laptop",
            "Apply consumed the published plan file",
            "A skipped Apply run exists (brake worked)",
            "Service connection is not subscription Owner",
        ],
        "tomorrow": "Phase 5 mini project — one RG + storage or webapp skeleton from the chosen IaC in a pipeline, then destroy.",
    },
    50: {
        "topic": "Mini Project + Recap (Phase 5)",
        "subtitle": "Click-ops is a hobby. IaC is how you sleep: one tool, plan then apply from a pipeline, destroy when the demo ends",
        "phase": "5 - Infrastructure as Code",
        "tables": [
            {
                "title": "Architecture A — Phase 5 map (Days 41–49)",
                "columns": ["Day", "Object", "Keep"],
                "rows": [
                    ["41", "Declarative vs imperative; drift; one primary tool", "ADR in docs/iac-why.md"],
                    ["42–43", "ARM JSON literacy: apiVersion, -p @params, outputs", "Broccoli you can read when deploys fail"],
                    ["44–45", "Bicep resources, modules, what-if", "Dress rehearsal before apply"],
                    ["46–48", "Terraform verbs, azurerm, backend + lock + modules", "State is memory; separate rg-tfstate"],
                    ["49–50", "Plan artifact + gated apply in YAML", "No laptop-as-prod; destroy after screenshot"],
                ],
                "widths": [28, 86, 68],
            },
            {
                "title": "Architecture B — mini project bar (not a landing zone)",
                "columns": ["In", "Out", "Done when"],
                "rows": [
                    ["One RG + storage or a webapp skeleton", "Hub-spoke, firewall, AKS", "plan+apply from pipeline once"],
                    ["Chosen tool from Day 41", "Rewriting the other tool 'just in case'", "Recap says why Bicep or why Terraform"],
                    ["Brake on apply", "Auto-approve because it is a lab RG you forgot is live", "Approval or apply=true demonstrated"],
                    ["Destroy after screenshot", "Leaving st* accounts 'for Day 51'", "az group list clean or budget-watched leftovers listed"],
                ],
                "widths": [52, 64, 66],
            },
            {
                "title": "Architecture C — recap failures",
                "columns": ["Pitfall", "What you see", "Fix"],
                "rows": [
                    ["Both as primary", "Two half folders, no green pipeline", "Pick one. Literacy notes for the other"],
                    ["Portal still source of truth", "File and Azure disagree; you 'fixed' in Portal", "Change the file, plan, apply"],
                    ["State leftover", "rg-tfstate + blobs after you destroyed workload", "Decide: keep for Phase 6 or delete last"],
                    ["Day 42 RGs still billing", "Cost recap writes itself", "az group delete the orphans"],
                ],
                "widths": [36, 73, 73],
            },
        ],
        "one_liner": "Phase 5 recap: click-ops is a hobby; IaC is how you sleep — environments that must survive a weekend live in a file.",
        "lab_intro": "Personal subscription + personal Azure DevOps org. Project azure-100-labs. Screenshot without secrets. Destroy after.",
        "lab": [
            "Provision one RG plus one storage account or a webapp skeleton using the Day 41 primary tool, from the Day 49 pipeline (brake on).",
            "Save a screenshot of the green plan+apply run (no secrets, no work tenant). Note the deployment name or tf apply ID in docs/phase5-recap.md.",
            "Write why you picked Bicep or Terraform in that recap. 'Both' is not a reason.",
            "Destroy once via the same tool (pipeline apply of destroy or terraform destroy / az group delete). Confirm Portal is empty for that RG.",
            "az group list -o table. Delete leftover rg-day42-lab … rg-day49-lab if any. rg-tfstate last, only if you are done with it.",
            "Tomorrow is Docker — do not keep storage accounts as souvenirs.",
        ],
        "code_title": "Definition of done",
        "code": """# docs/phase5-recap.md
# Primary: Bicep | Terraform
# Why: ____
# Pipeline run: plan stage URL ____  apply stage URL ____
# Resources: 1 RG + (storage | webapp skeleton)
# Destroy: command/run ____   az group list clean: yes/no
# Leftovers to kill: ____
""",
        "checklist": [
            "plan+apply from pipeline once on personal Azure",
            "Destroy once; leftovers listed or gone",
            "Written reason for Bicep or Terraform (one)",
            "Recap stays personal: no employer or client names",
        ],
        "tomorrow": "Docker fundamentals — images, containers, layer cache. Same app, fewer 'works on my laptop' customs checks.",
    },
}