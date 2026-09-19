# #100DaysOfAzureDevOps — detailed LinkedIn posts (Days 22–100)

These replace the short six-line templates in the daily guides and in the LinkedIn track file. Publish from the **personal** profile at **07:00 IST**. Document post: upload the PDF, paste the **Document title** from [`100-days-document-titles.md`](./100-days-document-titles.md), then paste the text. No selling, no Health Check, no company CTA.

First line of each post is the stand-alone hook. Hashtags stay exactly as written.

---

## Day 22 — Sat 19 Sep 2026 — Microsoft-hosted vs Self-hosted Agents

**Document title:** `Day 22 — Hosted vs Self-hosted Agents`

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

## Day 23 — Sun 20 Sep 2026 — YAML Pipeline Basics

**Document title:** `Day 23 — YAML Pipeline Basics`

```
YAML pipelines are Lego instructions written by someone who enjoys whitespace arguments.

Day 23 of #100DaysOfAzureDevOps. YAML pipeline basics.

Classic editor pipelines taught a generation to click. YAML taught the next one to argue about indentation. After ten years around release trains, I still prefer the argument. A pipeline you cannot diff in a pull request is a pipeline that will drift the moment two people edit it in the UI on the same afternoon.

Today is literacy, not poetry. Triggers, stages, jobs, steps. A PR trigger so main does not become a dumping ground. Logs read end-to-end so "the build failed" becomes a specific step, not a vibe.

What I keep seeing

1. Schema is a map, not decoration
• trigger and pr decide when the robot wakes up
• stages group jobs; jobs grab an agent; steps are the actual work
• If you cannot point to which layer failed, you will debug the wrong layer

2. dependsOn is a promise
• Test that does not depend on Build will race it and lie
• A missing dependsOn looks like speed until it ships an unbuilt artifact

3. PR triggers are manners
• include: main on pull requests catches the break before merge
• Skipping PR CI is how "it worked on my branch" becomes tomorrow's incident

4. Logs are the product of the pipeline
• displayName is how humans find the step at 1am
• Reading the run once, fully, is cheaper than guessing for a week

What I am doing in today's lab

I am expanding the hello pipeline into stages Build then Test (Test can still be echo), adding a PR trigger on main, and reading the pipeline run logs end-to-end instead of celebrating the green checkbox.

If you cannot explain the YAML out loud, you do not own the pipeline yet. Whitespace is annoying. Undiffable clicks are worse.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-23-yaml-pipeline-basics

Tomorrow: CI pipeline for a .NET app — restore, build, test, publish, artifact.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 24 — Mon 21 Sep 2026 — CI Pipeline for a .NET App

**Document title:** `Day 24 — CI Pipeline for a .NET App`

```
.NET CI is the same ritual every time: restore, build, test, publish — skip one and production finds it for you.

Day 24 of #100DaysOfAzureDevOps. CI pipeline for a .NET app.

I have lost count of how many "the API is down" threads ended with a missing restore, a Debug build in a Release slot, or tests that were commented out because they were slow. The ritual is boring on purpose. restore, build, test, publish. Then an artifact that the next environment can actually deploy.

UseDotNet@2 pins the SDK so the agent image does not surprise you. Path filters keep the pipeline from rebuilding the universe when someone edits a README. None of this is clever. All of it is how .NET teams stop being the person who compiled from their laptop into production.

Patterns from a decade of delivery

1. Pin the SDK
• UseDotNet@2 with 8.x (or whatever the repo actually builds)
• "It compiled on the agent last month" is not a version strategy

2. Restore is not optional theater
• dotnet restore, then build -c Release --no-restore
• Skipping restore to "save time" is how you get a random package graph

3. Test before you publish, even if today the test is thin
• dotnet test on the same configuration you ship
• || true in a lab is honesty; in production it is a lie you scheduled

4. Publish an artifact, do not rebuild later
• PublishBuildArtifacts (or PublishPipelineArtifact) from bin/Release
• The CD stage should consume drop, not invoke dotnet build again

What I am doing in today's lab

I am creating a minimal Web API under /src/SampleApi (dotnet new webapi), adding a pipeline that restores, builds, tests, and publishes, and storing the drop as a pipeline artifact. Path trigger stays on src/SampleApi/** so the rest of the repo can be noisy.

Skip a step of the ritual and you are not being agile. You are postponing the finding to a user.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-24-ci-pipeline-for-a-net-app

Tomorrow: CI for Node.js — npm ci, Cache@2, and stopping the paint-dry restore.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 25 — Tue 22 Sep 2026 — CI Pipeline for a Node.js App

**Document title:** `Day 25 — CI Pipeline for a Node.js App`

```
Node CI without caching is watching paint dry while paying Microsoft for the privilege.

Day 25 of #100DaysOfAzureDevOps. CI pipeline for a Node.js app.

npm install on a cold agent is a small tax that becomes a lifestyle. I have sat through pipelines that spent four minutes downloading the same packages the team downloaded an hour earlier. Cache@2 is not a micro-optimization for a conference talk. It is how you stop paying hosted-agent minutes to re-download left-pad's entire family tree.

The other habit: npm install in CI when the lockfile exists. npm ci is the one that respects the lock. If CI uses npm install, you do not have a lockfile. You have a suggestion.

What usually goes wrong

1. npm ci, not npm install, when package-lock.json exists
• ci fails if the lock is stale — that is a feature
• install will quietly mutate the graph and still go green

2. Cache the right key
• Cache@2 key: npm | Agent.OS | package-lock.json
• Cache node_modules (or the npm cache) — not the entire repo
• Wrong key = cache never hits and you still wait

3. Pin Node like you pin .NET
• NodeTool@0 with 20.x (or the engines field you actually mean)
• ubuntu-latest Node floating is how "works on my 18" becomes "fails on 22"

4. A tiny app is enough
• Today's sample-node can have a test script that prints ok
• The point is the pipeline shape, not a fake product

What I am doing in today's lab

I am adding a tiny Node app under /src/sample-node, wiring NodeTool@0, Cache@2 keyed off package-lock.json, then npm ci and npm test. If the cache hits, the log should show it. If it misses, I want to know why, not shrug.

Pay for compute that does work. Do not pay for compute that re-downloads the internet.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-25-ci-pipeline-for-a-node-js-app

Tomorrow: CI for Python — pip, ruff, pytest on a tiny sample.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 26 — Wed 23 Sep 2026 — CI Pipeline for a Python App

**Document title:** `Day 26 — CI Pipeline for a Python App`

```
pytest is the friend who tells you the truth before your users do.

Day 26 of #100DaysOfAzureDevOps. CI pipeline for a Python app.

Python CI looks optional until an import fails in production because the agent had a different implicit package. I have watched teams "just run the script" on a developer laptop, push, and discover that pytest was never in the pipeline because "we will add tests later." Later is a calendar that does not exist.

Today is a small sample: UsePythonVersion@0 at 3.11, pip, ruff, pytest. Lint that is allowed to warn in a lab is still lint you can see. Tests that do not run in CI are documentation of intent, not a safety net.

Patterns I keep seeing

1. Pin the interpreter
• UsePythonVersion@0 with 3.11 (or the version in .python-version)
• The agent image's leftover Python is not your runtime

2. Install tools in the job, not in folklore
• pip install pytest ruff in the pipeline so the next person is not hunting a wiki
• requirements.txt (even a short one) beats "it was on my machine"

3. Lint and test are different signals
• ruff check . catches style and a class of bugs early
• pytest -q tells you behavior; do not conflate them into one exit code you ignore

4. A failing lint in lab can be || true once — not forever
• I am allowing ruff to warn today so the first pipeline exists
• Leaving || true in a real main branch is how quality becomes optional

What I am doing in today's lab

I am adding /src/sample-python with at least one pytest, then a pipeline that upgrades pip, installs pytest and ruff, runs ruff check, and runs pytest -q. Green means the interpreter, the tools, and the tests agreed in CI — not that I ran a file locally.

Users will test your Python if you will not. pytest is cheaper.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-26-ci-pipeline-for-a-python-app

Tomorrow: CI for Java/Maven — lifecycle, tests, and not jumping off the train early.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 27 — Thu 24 Sep 2026 — CI Pipeline for a Java/Maven App

**Document title:** `Day 27 — CI Pipeline for a Java App`

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

## Day 28 — Fri 25 Sep 2026 — Multi-stage YAML Pipelines

**Document title:** `Day 28 — Multi-stage YAML Pipelines`

```
Matrix builds are cloning yourself across versions so "works on my Node" becomes "works on these Nodes."

Day 28 of #100DaysOfAzureDevOps. Multi-stage YAML pipelines.

A single-stage pipeline is a to-do list. Multi-stage is a workflow with memory: Build, then Test, then a deploy stub that should not run if Test failed. Matrix is the move that stops the most expensive sentence in engineering: it works on my version.

I have seen production Node 18 fail a library that staging ran on 20 because nobody asked CI to clone the job. strategy.matrix is not showing off. It is renting two of you for the price of YAML.

Patterns from real delivery

1. Stages need dependsOn and conditions
• Test depends on Build
• A deploy stub with condition: succeeded() so a red test does not "deploy" an echo to nowhere

2. Matrix is a version conversation in code
• node18: 18.x and node20: 20.x (or two Python versions)
• NodeTool@0 reads $(version) from the matrix — one job definition, two realities

3. Parallel is a gift with a bill
• Matrix jobs run in parallel if you have parallelism
• That is faster feedback and more hosted minutes — know which you are buying

4. A deploy stage can be a stub today
• echo is legal if the condition is real
• Wiring fake success on a failed build is how YAML lies in production later

What I am doing in today's lab

I am adding a matrix for Node 18/20 (or two Python versions) and a deploy-stage stub that only runs on succeeded(). Then I will fail a test on purpose once to watch the stub stay still. If it still runs, the condition is theater.

Clone the job across the versions you claim to support. Otherwise you support a laptop.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-28-multi-stage-yaml-pipelines

Tomorrow: Pipeline variables, groups, and secrets — envelopes, not postcards.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 29 — Sat 26 Sep 2026 — Pipeline Variables, Groups & Secrets

**Document title:** `Day 29 — Variables, Groups & Secrets`

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

## Day 30 — Sun 27 Sep 2026 — Mini Project + Recap (Phase 3)

**Document title:** `Day 30 — Phase 3 Mini Project & Recap`

```
Phase 3 recap: CI is a seatbelt you wear before the crash, not after.

Day 30 of #100DaysOfAzureDevOps. Mini project and recap for Phase 3 — Continuous Integration.

Nine days of agents, YAML, .NET, Node, Python, Maven, matrix, and secrets. The point was not to become four ecosystems in a week. The point was to feel the same spine in every language: restore or install, build, test, publish an artifact, keep secrets out of the file.

I have been in delivery long enough to know the crash is not theoretical. A merge on Friday, a missing test, a hosted agent that drifted. CI is the seatbelt. Putting it on after the incident is a blog post, not a practice.

What Phase 3 actually taught me to keep

1. YAML anatomy I can draw from memory
• trigger / pr → stages → jobs → pool → steps
• If I cannot sketch it, I copied it

2. One primary stack, stubs for the rest
• Pick .NET or Node or Python as the real green build
• The other languages can stay samples; depth beats a graveyard of half pipelines

3. Artifacts are the handoff
• CI produces a drop; CD should not rebuild
• A screenshot of a green run is allowed; a screenshot of a secret is not

4. Secrets stay in groups
• No passwords in azure-pipelines.yml
• That rule survives every phase after this

What I am doing in today's lab

I am picking my primary stack, getting a green build on main, saving a screenshot with no secrets, and writing a short recap: YAML anatomy plus one war story from this week (a cache miss, a skipped test, a secret that almost got echoed). Pipelines live under /pipelines.

Wear the seatbelt on the first commit you care about. Phase 3 is that commit, repeated until it is boring.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-30-mini-project-recap-phase-3

Tomorrow: Release pipelines overview — Classic vs YAML CD, and an environment named dev.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 31 — Mon 28 Sep 2026 — Release Pipelines Overview

**Document title:** `Day 31 — Release Pipelines Overview`

```
Classic releases are the old mall; YAML CD is the street you actually live on now.

Day 31 of #100DaysOfAzureDevOps. Release pipelines overview.

Classic Release pipelines still work. They also hide the workflow in a UI that does not review well and does not travel with the repo. After a decade of delivery, I can still click a Classic stage in my sleep. I do not want my labs, or a future team's source of truth, to live in that mall.

YAML CD is a deployment job, an environment, and a strategy. runOnce. deploy. The environment named dev is not a folder on a laptop. It is an Azure DevOps object you can hang approvals and checks on later this phase.

Patterns I keep seeing

1. Prefer YAML CD for new work
• The pipeline file lives next to the app
• Classic is literacy for brownfield, not the default for a 100-day lab

2. Environments are first-class
• Pipelines → Environments → create dev
• A deployment job targets environment: dev so history is not a buried log

3. strategy.runOnce.deploy is the smallest CD
• steps under deploy run on the agent against that environment
• echo Deploying to dev is a legal first proof — the wiring matters more than the bits today

4. CD consumes CI, it does not impersonate it
• Download the artifact from Day 24–30
• Rebuilding in the release job is how staging and production diverge

What I am doing in today's lab

I am leaving Classic alone for these labs, creating environment dev in Pipelines → Environments, and adding a DeployDev stage with a deployment job that echoes a deploy. Tomorrow the echo becomes App Service. Today the environment object has to exist.

Live on the street that diffs. Visit the mall only when a legacy release still pays the rent.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-31-release-pipelines-overview

Tomorrow: Deploy to Azure App Service — zip deploy from the pipeline.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 32 — Tue 29 Sep 2026 — Deploying to Azure App Service

**Document title:** `Day 32 — Deploying to Azure App Service`

```
App Service is PaaS comfort food — less drama than VMs, still enough knobs to burn dinner.

Day 32 of #100DaysOfAzureDevOps. Deploying to Azure App Service.

I have spent years around VMs that needed patching, agents, and a load balancer that someone named after a pet. App Service removes a pile of that drama. It does not remove configuration, SKU choice, or the zip that is not the zip you thought you published.

Today is a Free/F1 plan, a webapp in a personal resource group, AzureWebApp@1, and a service connection that must not be over-privileged later. Cost-sensitive means the RG dies tonight. Comfort food still goes stale if you leave it on the counter.

What usually happens

1. Zip deploy is a contract
• package: $(Pipeline.Workspace)/drop/**/*.zip must match what CI published
• Wrong glob = a successful task that deployed nothing useful

2. Service connection is identity
• azureSubscription in AzureWebApp@1 is the robot's badge
• If that badge is Owner on the subscription, the lab is teaching the wrong lesson

3. SKU is a budget decision
• F1/free for a hello app
• Slots and some networking need a higher plan — do not discover that after the deploy is "done"

4. Delete is a skill
• Personal RG, personal subscription, delete tonight if cost-sensitive
• Orphan App Service plans are quiet invoices

What I am doing in today's lab

I am creating a free/F1 App Service plan and webapp in a personal RG, deploying a hello app from the pipeline with AzureWebApp@1, confirming the URL responds, and deleting the RG tonight if I do not need it for slots later this week.

PaaS is comfort. The knobs are still hot. Deploy the zip you published, then clean up the kitchen.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-32-deploying-to-azure-app-service

Tomorrow: Deploy to Azure Functions — Consumption vs Premium, timer or HTTP sample.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 33 — Wed 30 Sep 2026 — Deploying to Azure Functions

**Document title:** `Day 33 — Deploying to Azure Functions`

```
Functions are micro-managers that only wake up when work arrives — and still send you a bill for the nap.

Day 33 of #100DaysOfAzureDevOps. Deploying to Azure Functions.

Consumption plans feel like free until a timer fires more than you thought, or a runaway retry turns "serverless" into a line item. I have seen teams love Functions for the right reason (event-shaped work) and the wrong reason ("we do not want to think about hosts"). You still think about hosts. You just think about them as plans: Consumption vs Premium vs dedicated.

If quota is tight, a read-only lab is honest. Deploying a timer or HTTP sample on Consumption is the default. AzureFunctionApp@2 is the CD task. The package is still a zip you built in CI.

Patterns I keep seeing

1. Pick the plan for the sleep pattern
• Consumption: scale to zero, cold starts, pay per execution
• Premium: pre-warmed, VNet, a bill that does not nap as hard

2. HTTP and timer are different operational stories
• HTTP is a public or gateway-shaped surface
• Timer is a cron you will forget is running until Cost Management reminds you

3. CD is still a package
• AzureFunctionApp@2, appType functionApp, package glob on the zip
• Do not "publish from Visual Studio" as the source of truth if the pipeline exists

4. Quota and cost are lab design
• Create on Consumption or read the blade if the subscription cannot
• Delete the Function App when the proof is done

What I am doing in today's lab

I am creating a Function App on Consumption (or reading the experience if quota is tight), deploying a timer or HTTP sample from the pipeline, triggering it once, and checking that I know how to stop or delete it so the nap does not keep billing.

Serverless sleeps. Billing does not always. Know which plan you bought.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-33-deploying-to-azure-functions

Tomorrow: Deployment slots and swap — staging as a dressing room.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 34 — Thu 1 Oct 2026 — Deployment Slots & Swap Strategies

**Document title:** `Day 34 — Deployment Slots & Swap`

```
Slots are dressing rooms for production — try the outfit on before walking the runway.

Day 34 of #100DaysOfAzureDevOps. Deployment slots and swap strategies.

Swapping a slot is the closest App Service gets to a rehearsal. Warm the staging slot, hit a smoke URL, swap. If the outfit rips, swap back. I have watched teams treat swap as a fancy copy-paste and skip warm-up, then blame "Azure" for a cold-start outage they scheduled.

Not every SKU has slots. That is not a trivia question. It is why yesterday's F1 plan may refuse today's lab. Document the warm-up path anyway. Auto-swap is a power tool; I am not turning it on until smoke is real.

What I keep seeing

1. Staging is not production with a nickname
• Slot settings can stick (connection strings, flags) so the swap does not carry the wrong config
• If config is identical by accident, you have not learned slots — you have copied them

2. Warm-up is the point
• Hit the staging URL until the app is actually ready
• Swap of a cold process is a self-inflicted brownout

3. Swap is two-way
• staging → production after smoke
• production → staging is the rollback, not a conference-call archaeology dig

4. Auto-swap needs a grown-up smoke
• If smoke is "I looked at the log," do not auto-swap
• Document the warm-up path even if the SKU blocks the slot today

What I am doing in today's lab

If the SKU allows it, I am adding a staging slot, deploying to it, smoking it, and swapping. If it does not, I am writing the warm-up path and the SKU note so I do not pretend the lab passed. Portal: Web App → Deployment slots → Add slot staging.

Walk the runway only after the dressing room mirror. Swap is a rehearsal tool, not a personality.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-34-deployment-slots-swap-strategies

Tomorrow: Blue-green deployments — two worlds, one traffic, a written rollback.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 35 — Fri 2 Oct 2026 — Blue-Green Deployments

**Document title:** `Day 35 — Blue-Green Deployments`

```
Blue-green means two worlds; only one takes traffic — rollback is a light switch, not an archaeology dig.

Day 35 of #100DaysOfAzureDevOps. Blue-green deployments.

The idea is older than App Service slots: two complete environments, one VIP or hostname taking traffic. Blue is live. Green is the candidate. Flip. If green is sick, flip back. I have been in change windows where "rollback" meant rebuild the previous bits from a laptop because nobody kept the last known good. That is archaeology. Blue-green is a light switch if you paid for the second world and kept the previous artifact.

On App Service, slots are the cheap map: blue = production slot, green = staging. AKS comes later. Today I write rollback steps I would actually follow.

Patterns I keep seeing after a decade in delivery

1. Two worlds, one traffic pointer
• Do not call a single-slot deploy "blue-green" because it sounds senior
• If there is no idle world, there is no switch — there is a hope

2. Rollback is a written procedure
• Swap back staging/production
• Verify a health endpoint, not a feeling
• Keep the previous artifact for a defined window (I am writing 7 days for the lab)

3. Health has to mean ready, not process-up
• A 200 from / that does not touch a dependency is a vanity light
• The switch is only safe if green was smoked as a user would

4. Cost is the reason teams fake it
• A second environment is real money
• Slots on a capable SKU are the lab-sized version of the pattern

What I am doing in today's lab

I am mapping blue-green onto slots (blue=prod, green=staging) and writing /docs/rollback.md with three steps: swap back, verify health, keep the previous artifact for 7 days. If I cannot swap today because of SKU, the document still has to exist. A rollback that lives only in my head is not a rollback.

Keep two worlds or admit you have one. Archaeology is not a rollback strategy.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-35-blue-green-deployments

Tomorrow: Canary releases — 5% / 25% / 100% or abort.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 36 — Sat 3 Oct 2026 — Canary Releases

**Document title:** `Day 36 — Canary Releases`

```
Canaries in coal mines and canaries in prod share a job: die early so the rest of us don't.

Day 36 of #100DaysOfAzureDevOps. Canary releases.

Canary is not a percentage because percentages are fashionable. It is a small slice of real traffic, watched hard, with an abort that is faster than a debate. I have seen "canary" mean "we deployed to one server and went to lunch." That is not a canary. That is an unattended experiment on customers.

App Service testing-in-production / traffic routing is the optional Azure knob. Feature flags are another. Today's mandatory work is a paper plan: 5% → watch errors 15 minutes → 25% → watch → 100% or abort. If I cannot name the abort signal, I do not have a canary. I have a vibe.

What I keep seeing

1. Ramp is a schedule with watches, not a slider
• 5% traffic, watch errors for 15 minutes
• 25%, watch again
• 100% only if the watches were boring

2. Abort is a first-class step
• Name the metric: 5xx rate, latency, a business heartbeat
• If abort is "we will see," the canary cannot die early — users will

3. Flags versus traffic splits
• A feature flag can hide a path without splitting the fleet
• Traffic split can send 5% of users to a new slot or revision
• Pick one for the lab plan; mixing both without a diagram is how you gaslight yourself

4. Health during the watch
• Look at the canary's errors, not the average of old+new
• Averages hide a dying bird

What I am doing in today's lab

I am designing a canary plan on paper for the webapp, and optionally looking at App Service testing in production / traffic routing if the SKU allows. The checklist is 5% → 15 min → 25% → 100% or abort. If I skip Azure knobs today, the paper still has to name the abort.

If the canary cannot die, it cannot save anyone. Write the abort before the ramp.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-36-canary-releases

Tomorrow: Rolling deployments — changing tires while the car is moving.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 37 — Sun 4 Oct 2026 — Rolling Deployments

**Document title:** `Day 37 — Rolling Deployments`

```
Rolling deploys change the tires while the car is moving — thrilling, and occasionally stupid.

Day 37 of #100DaysOfAzureDevOps. Rolling deployments.

VMSS and Kubernetes rolling updates replace instances in batches. The car never fully stops. That is the appeal. It is also how you run two versions of the API at once and discover they disagree about a database column. I have lived through rolling deploys that were "zero downtime" and still half-broken for twenty minutes because mixed versions were not in the design.

No AKS yet. Today is a comparison table in docs: rolling vs blue-green vs canary. Downtime, complexity, rollback speed. Pick with eyes open, not with a blog title.

Patterns I keep seeing

1. Rolling: low downtime, slower rollback
• Batches go healthy before the next batch
• Rollback means rolling forward to old bits — also in batches
• Mixed versions are a feature until a breaking change arrives

2. Blue-green: near-zero cutover, fast switch
• You paid for two worlds
• Rollback is the switch, not a second rolling movie

3. Canary: near-zero, higher operational complexity
• Stop the ramp if the bird dies
• Needs metrics that isolate the new slice

4. Compatibility is the hidden requirement
• Rolling demands N and N-1 can coexist
• If they cannot, rolling is how you schedule a partial outage

What I am doing in today's lab

I am writing a markdown table: Strategy | Downtime | Complexity | Rollback — Rolling, Blue-green, Canary. No AKS cluster today. The table has to be specific enough that I could defend a choice in a design review without hand-waving.

Thrilling is not a strategy. If N and N-1 cannot coexist, do not roll. Switch or flag.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-37-rolling-deployments

Tomorrow: Approval gates and environments — I am the approver on prod.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 38 — Mon 5 Oct 2026 — Approval Gates & Environments

**Document title:** `Day 38 — Approval Gates & Environments`

```
Approvals are speed bumps before prod — annoying until the day they stop a 3am self-own.

Day 38 of #100DaysOfAzureDevOps. Approval gates and environments.

Nobody likes waiting on a checkbox. Everybody likes the checkbox after they almost deployed a debug flag to production because they reused the wrong variable group. I have been the person who hated gates and the person who was grateful a human had to click. After ten years, I will take the bump.

Azure DevOps environments can carry checks: pre-deployment approvals, post-deployment, business hours, whatever you configure. Today's lab is not a governance novel. It is environment prod, me as approver, one run where I Approve, one where I Reject, and a log that shows both.

What I keep seeing

1. Approvals belong on environments, not in chat
• Pipelines → Environments → prod → Checks → Approvals
• A Slack thumbs-up is not an audit trail

2. The approver should not be "whoever is awake"
• For the lab, the approver is my personal account
• In a real team, name a group, not a hero

3. Reject is a path you must practice
• If you only ever click Approve, you will freeze the first time you should not
• The pipeline should stop. That is success.

4. Gates are not a substitute for tests
• A human cannot eyeball a 200MB zip
• Approvals catch process mistakes; tests catch product mistakes

What I am doing in today's lab

I am adding an approval check on a prod environment with myself as approver, running the pipeline, practicing Approve once and Reject once, and keeping the run URLs. If Reject still deploys, the check is not attached to the job I think it is.

Annoying is the point. 3am you does not want a YOLO button.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-38-approval-gates-environments

Tomorrow: Multi-environment pipeline — Dev → Staging → Prod, same artifact.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 39 — Tue 6 Oct 2026 — Multi-environment Pipeline

**Document title:** `Day 39 — Multi-environment Pipeline`

```
Promote the artifact, not the vibes — rebuilds between envs invent "works in staging" ghosts.

Day 39 of #100DaysOfAzureDevOps. Multi-environment pipeline.

Dev → QA → Staging → Prod is a sentence every deck contains. The failure mode I have seen for a decade is rebuilding the app in each stage "because the pipeline is simpler that way." Staging compiled on Monday. Production compiled on Tuesday from the same commit and pulled a different transitive dependency. Ghosts.

Three stages in YAML. Approvals on the last. The same drop from CI. Dev can be a real App Service. Prod can be echo if budget is tight. The promotion rule does not change.

Patterns I keep seeing

1. Build once, deploy many
• CI publishes drop; each env stage downloads it
• dotnet publish in Prod is a second dice roll

2. dependsOn is the promotion chain
• Staging depends on Dev
• Prod depends on Staging
• Skipping Staging because "we are late" is how you become later

3. Approvals only on the environments that hurt
• Dev can be automatic in a lab
• Prod gets the environment check from Day 38

4. Config is not the artifact
• Connection strings and flags differ by env
• The bits should not. If they must, you are not promoting an artifact — you are assembling one

What I am doing in today's lab

I am writing YAML with three stages — Dev, Staging, Prod — approvals on the last, and the same artifact promoted. Prod can echo if I am not spending. The run should show Dev then Staging then a waiting approval, not three independent rebuilds.

If staging worked, deploy that zip. Vibes are not a promotion strategy.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-39-multi-environment-pipeline

Tomorrow: Phase 4 mini project — CI/CD with visible approvals.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 40 — Wed 7 Oct 2026 — Mini Project + Recap (Phase 4)

**Document title:** `Day 40 — Phase 4 Mini Project & Recap`

```
Phase 4 recap: shipping is a pipeline with brakes, not a YOLO button.

Day 40 of #100DaysOfAzureDevOps. Mini project and recap for Phase 4 — Continuous Delivery.

This phase was App Service, Functions, slots, blue-green, canary, rolling, approvals, and multi-env promotion. The spine is the same: an artifact from CI, an environment object, a strategy for how traffic meets bits, and a brake someone can actually pull.

I have watched "just deploy it" work until it did not. YOLO is a button. Delivery is a path with stages, checks, and a rollback that is not a scavenger hunt. Today's definition of done is one pipeline run with visible approvals and logs saved.

What I am keeping from Phase 4

1. CD is YAML, environments, and a strategy
• Classic mall is literacy; the street we live on is multi-stage YAML
• environment: dev/prod is how history shows up

2. Traffic strategies are choices with costs
• Slots/swap ≈ dressing room
• Blue-green ≈ light switch if you paid for two worlds
• Canary ≈ die early
• Rolling ≈ mixed versions on purpose

3. Brakes are approvals plus rollback docs
• Reject must work
• rollback.md must exist even if prod is an echo

4. Same artifact through the chain
• The recap is not complete if Prod rebuilt
• Ghosts from Day 39 still count as a miss

What I am doing in today's lab

I am running a green path Dev → Staging → Prod (prod may be echo if there is no budget), capturing approvals in the run, saving logs, and writing a recap without heroics. Success is a boring screenshot of a pipeline that waited for me.

Ship with brakes. A YOLO button is not courage. It is unpaid incident duty.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-40-mini-project-recap-phase-4

Tomorrow: IaC concepts — declarative vs imperative, drift, pick Bicep or Terraform.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 41 — Thu 8 Oct 2026 — IaC Concepts

**Document title:** `Day 41 — Infrastructure as Code Concepts`

```
If it is not in code, it is a rumor — IaC turns "someone clicked prod" into a diff.

Day 41 of #100DaysOfAzureDevOps. IaC concepts.

Click-ops is how every environment I have inherited started: a portal session, a naming convention that lasted three resources, and a story about "the storage account that was always there." If it is not in code, it is a rumor. Infrastructure as Code is how the rumor becomes a pull request.

Declarative vs imperative. Idempotency. Drift. Today I write why IaC, pick a primary tool for Phase 5 — Bicep or Terraform, one, not both as a personality — and I write down drift I have actually seen: a firewall rule someone "just added," a SKU bump, a lock that existed only in production.

Patterns I keep seeing

1. Declarative says what; imperative says how
• Bicep/ARM/Terraform: desired state, the engine converges
• A shell script of az commands is a recipe that forgets deletions

2. Idempotency is the adult test
• Apply twice, same world
• If the second apply creates a second of everything, you have a script, not IaC

3. Drift is the portal's revenge
• Someone clicked, the file did not change, production is now a fork
• What-if / plan exist to see the fork before you overwrite a human's surprise

4. One primary tool for this phase
• Bicep if I want Azure-native and ARM literacy
• Terraform if I want state, modules, and a tool that travels
• Both as "I will learn everything" is how I learn neither

What I am doing in today's lab

I am writing docs/iac-why.md with examples of drift I have seen, and a decision record: Tool: Terraform | Bicep, Reason: ______. I will still touch the other tool for literacy. The primary is the one that will provision the mini project.

Rumors do not rollback. Diffs do. Put the environment in a file.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-41-iac-concepts

Tomorrow: ARM templates basics — deploy a tiny Storage Account, then delete the RG.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 42 — Fri 9 Oct 2026 — ARM Templates Basics

**Document title:** `Day 42 — ARM Templates Basics`

```
ARM JSON is the broccoli of Azure — nutritious, rarely anyone's favorite.

Day 42 of #100DaysOfAzureDevOps. ARM templates basics.

Every Portal click still becomes an ARM call. Bicep compiles to ARM. Terraform talks to the same control plane. If I refuse to read JSON templates, I will one day debug a failed deployment by staring at an error that only makes sense if I know schema, resources, and apiVersions.

This is literacy, not my main tool. Deploy a tiny Storage Account template. Delete the resource group. Feel the broccoli. Then decide I do not have to eat a bucket of it every day.

What I keep seeing

1. Template structure is boring and load-bearing
• $schema, contentVersion, parameters, variables, resources, outputs
• Skip resources and you have a comment file

2. apiVersion is a contract
• Wrong version, surprise properties
• Copy-paste from an old blog is how you deploy 2016 into 2026

3. CLI is the honest deploy
• az deployment group create -g rg-day42 -n stor -f infra/storage.json
• Portal "export template" is a start; it is also a nest of defaults you did not choose

4. Delete is part of the lab
• Empty or leftover storage still bills
• rg-day42 should not survive the night without a reason

What I am doing in today's lab

I am deploying a tiny Storage Account ARM template with az deployment group create, confirming the resource exists, then deleting the RG. I am not falling in love with JSON. I am making sure I can read the broccoli.

Nutritious, not favorite. Still eat a forkful so Bicep and Terraform errors make sense.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-42-arm-templates-basics

Tomorrow: ARM parameters and outputs — dials instead of hardcoded names.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 43 — Sat 10 Oct 2026 — ARM Parameters & Outputs

**Document title:** `Day 43 — ARM Parameters & Outputs`

```
Parameters are the dials; hardcoding names is how labs become landfills.

Day 43 of #100DaysOfAzureDevOps. ARM parameters and outputs.

A template with names baked in is a souvenir from one resource group. The second environment copies the file, forgets a string, and you have stprodprod in East US because someone concatenated in a panic. Parameters are the dials. Outputs are how the next stack finds the endpoint without spelunking the Portal.

If Terraform is my primary, I still skim this. Nested templates exist; I am not building a matryoshka today. Parameter file plus an output for the storage endpoint is the lab.

Patterns I keep seeing

1. Parameter files are environment knobs
• main.parameters.json (or per-env files) instead of edited copies of main.json
• az deployment group create ... -p @main.parameters.json

2. Hardcoded names collide
• Storage account names are globally unique
• A landfill of failed deployments is often a name that already existed

3. Outputs are the handshake
• Emit the blob endpoint or resource ID
• The next pipeline step should not grep the Portal

4. Nested templates are power tools
• Literacy: they exist
• Today: one file, parameters, outputs — enough

What I am doing in today's lab

I am adding a parameters file, outputting the storage endpoint, deploying with -p @main.parameters.json, and if Terraform is my primary I am keeping this to a skim plus one successful parameterized deploy. Then I delete what I created.

Dials belong in parameter files. Names that cannot change belong in uniqueString, not in my pride.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-43-arm-parameters-outputs

Tomorrow: Bicep fundamentals — same control plane, less JSON horror.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 44 — Sun 11 Oct 2026 — Bicep Fundamentals

**Document title:** `Day 44 — Bicep Fundamentals`

```
Bicep is ARM with the JSON horror filed down — same control plane, less eye strain.

Day 44 of #100DaysOfAzureDevOps. Bicep fundamentals.

Bicep is not a different Azure. It is ARM with a language that does not make you count braces for sport. resource declarations, params, uniqueString for names that must be globally unique. After years of JSON templates, the first Bicep file feels like someone turned the lights on.

If I chose Terraform as primary, I still read a Bicep sample for thirty minutes. Azure-native teams will send me .bicep files. Illiteracy is not a brand.

What I keep seeing

1. Same resource types, calmer syntax
• Microsoft.Storage/storageAccounts@2023-01-01
• sku and kind in a block instead of a nest of quotes

2. uniqueString is how you stop name collisions
• name: 'st${uniqueString(resourceGroup().id)}'
• Hardcoded stmyname123 is a landfill ticket from Day 43

3. location should be a param
• param location string = resourceGroup().location
• A second region should not require a fork of the file

4. Install the compiler
• az bicep install
• Then deploy storage if this is my track; otherwise read the sample and still type the resource block once

What I am doing in today's lab

If Bicep is my track: az bicep install and deploy a storage account from main.bicep. If Terraform is my track: thirty minutes on the sample, still write the resource block so my hands know it. Either way I delete the RG when the proof is done.

Same control plane. Less eye strain. File down the horror, do not pretend ARM went away.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-44-bicep-fundamentals

Tomorrow: Bicep modules and what-if — dress rehearsal before prod.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 45 — Mon 12 Oct 2026 — Bicep Modules & Deployment

**Document title:** `Day 45 — Bicep Modules & Deployment`

```
what-if is a dress rehearsal — read the diff before the audience (prod) arrives.

Day 45 of #100DaysOfAzureDevOps. Bicep modules and deployment.

A module is how Bicep stops being a 2,000-line main.bicep that nobody dares touch. Split storage into a module. Call it from main. what-if is the rehearsal: az deployment group what-if shows Create/Ignore/Modify/Delete before you let the audience in.

I have seen production applies where nobody ran plan or what-if because "it is only a SKU change." The diff included a recreate. Dress rehearsal exists for that sentence.

Patterns I keep seeing

1. Modules are boundaries
• Storage module takes name prefix / SKU as params
• Main composes modules; it does not inline every resource forever

2. what-if is mandatory manners
• az deployment group what-if -g rg-day45 -f main.bicep
• Read Modify and Delete like they are incidents that have not happened yet

3. Deployment stacks are the grown-up cleanup story
• Literacy: stacks can track and prune
• Lab: one what-if, one module split, one real deploy if this is my track

4. A diff you did not read still applies
• CI can print what-if
• Humans still have to look. Automation without eyes is a faster rumor

What I am doing in today's lab

I am running az deployment group what-if against main.bicep, splitting storage into a module, and only then deploying. If the what-if shows a Delete I did not expect, I stop. The audience is not invited to surprises.

Read the diff. Prod is a terrible place to learn you recreated a disk.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-45-bicep-modules-deployment

Tomorrow: Terraform basics — init, plan, apply, destroy, and state as memory.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 46 — Tue 13 Oct 2026 — Terraform Basics

**Document title:** `Day 46 — Terraform Basics`

```
Terraform state is the memory of your infra — lose it and you are arguing with ghosts.

Day 46 of #100DaysOfAzureDevOps. Terraform basics.

init, plan, apply, destroy. The verbs are simple. The state file is the plot. Terraform's memory of what it created lives in state. Lose it, and the next apply will try to create things that already exist, or will refuse to destroy things you can still see in the Portal. I have watched grown teams argue with ghosts for a day because someone deleted terraform.tfstate to "clean up."

Today is local state on purpose: a resource group only, then destroy at the end of the night. Remote state is Day 48. Skipping destroy is how a lab becomes a subscription.

What I keep seeing

1. The four verbs are a ritual
• terraform init — providers
• plan — the diff
• apply — change the world
• destroy — the adult ending

2. State is not a cache
• It is the mapping from resource addresses to Azure IDs
• Delete it and Terraform amnesia begins

3. Plan is the dress rehearsal (again)
• Never apply a mental diff
• If plan surprises you, you do not apply until it does not

4. Destroy tonight
• Local state lab: RG only
• Always destroy at end of night — leftover RGs are how Cost Management becomes a personality test

What I am doing in today's lab

I am installing Terraform, running init/plan/apply on a resource group with local state, confirming the RG in Azure, then terraform destroy -auto-approve. If destroy fails, I do not shrug and leave it. Ghosts start as leftovers.

Protect state like production data. Memory loss in Terraform is not a vibe. It is an outage you scheduled.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-46-terraform-basics

Tomorrow: Terraform with Azure (azurerm) — CLI auth, RG + storage.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 47 — Wed 14 Oct 2026 — Terraform with Azure (azurerm)

**Document title:** `Day 47 — Terraform with Azure`

```
azurerm is Terraform's Azure dialect — same ideas, different accent.

Day 47 of #100DaysOfAzureDevOps. Terraform with Azure (azurerm).

The azurerm provider is how Terraform speaks ARM without you writing ARM. provider "azurerm" { features {} }. Auth today is Azure CLI: az login on a personal account, personal subscription. I have seen service principals with Owner at subscription scope used "just for Terraform." That is not a dialect. That is a master key in a language file.

Lab shape: resource group plus storage. Central India or the region I actually use. Names that can collide will. Destroy still exists.

Patterns I keep seeing

1. Provider block is the accent
• features {} is required even when empty
• Pin provider versions in real work; floating latest is a surprise engine

2. Auth via CLI for labs
• az login, then Terraform uses that context
• Tomorrow's professional version is a scoped identity, not my user forever

3. Resources map 1:1 with Azure types
• azurerm_resource_group, then a storage account in that group
• If the plan creates a second RG, my reference is wrong — I read the plan

4. Region is a variable waiting to happen
• location = "Central India" is fine in a lab
• Hardcoding it in six modules is how you migrate with a prayer

What I am doing in today's lab

I am authenticating with az login, writing a tiny azurerm config that creates rg-day47-tf and a storage account, applying, verifying in Portal or CLI, then destroying. No subscription-Owner robot. Personal user, personal sub, short life.

Same ideas as ARM/Bicep. Different accent. Do not give the dialect a master key to practice grammar.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-47-terraform-with-azure-azurerm

Tomorrow: Terraform modules and remote state — locking so two applies cannot tug-of-war.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 48 — Thu 15 Oct 2026 — Terraform Modules & Remote State

**Document title:** `Day 48 — Terraform Modules & State`

```
Remote state with locking stops two applies from playing tug-of-war with production.

Day 48 of #100DaysOfAzureDevOps. Terraform modules and remote state.

Local state on a laptop is a lab. Two people applying with two local states is a fork of reality. Remote state in Azure Storage, with locking, is how grown-ups share memory. I have seen two applies in the same hour create duplicate resources and a third that could not destroy either. Tug-of-war.

Modules are the other half: reuse without copy-paste. Backend azurerm: resource group, storage account, container, key. Note the cost of the state account. Destroy carefully — destroying the state account before the workload is how you orphan the world.

What I keep seeing

1. Backend is the shared brain
• backend "azurerm" with rg, account, container, key = lab.tfstate
• Migrate with terraform init when you add the backend — do not copy files like a raccoon

2. Locking is the point
• Blob lease lock stops concurrent applies
• If someone force-unlocks because they are impatient, they just volunteered to be the incident

3. Modules beat copy-paste
• A storage module with inputs beats three nearly identical main.tf files
• Module versioning is later; today is the split

4. Destroy order matters
• Workload first, state account last, and only if I am done with the lab
• Deleting state storage while resources exist is amnesia on purpose

What I am doing in today's lab

I am creating storage for state (noting it costs), configuring the azurerm backend, migrating state, applying through the backend once, then destroying the workload carefully. I am not force-unlocking anything. If a lock exists, I wait or I investigate.

Share memory. Lock the door. Two applies at once is not speed. It is a race with prod as the prize.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-48-terraform-modules-remote-state

Tomorrow: IaC in pipelines — plan in CI, apply behind an approval.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 49 — Fri 16 Oct 2026 — IaC in Pipelines

**Document title:** `Day 49 — IaC in Pipelines`

```
IaC without a pipeline is homework; IaC in a pipeline is how grown-ups change prod.

Day 49 of #100DaysOfAzureDevOps. IaC in pipelines.

A plan on a laptop is a school assignment. A plan in CI, published as an artifact, applied only when an approval says so, is how you stop "it worked on my Terraform." I have watched production apply from a developer workstation because the pipeline "wasn't ready." The workstation had a different variable file. Of course it did.

Pipeline: terraform plan -out=tfplan (or bicep what-if). Publish the plan. Apply with a condition — eq(variables['apply'], 'true') or an environment approval. Not both auto-approve and hope.

Patterns I keep seeing

1. Plan in CI on a clean agent
• The agent checks out the same commit a human reviewed
• Laptop plans pick up leftover env vars like lint

2. Apply is gated
• condition: and(succeeded(), eq(variables['apply'], 'true'))
• Or a prod environment approval from Day 38
• Auto-approve in a lab destroy is fine; auto-approve prod is a personality disorder

3. The plan file is the artifact
• Apply the plan you reviewed, not a fresh plan nobody saw
• A second plan at apply time is how surprises sneak in

4. Identity of the pipeline is scoped
• The service connection should not be Owner on the subscription
• IaC robots with flamethrowers write very complete incidents

What I am doing in today's lab

I am adding a pipeline that runs terraform plan -out=tfplan (or Bicep what-if), publishes the plan, and applies only when apply=true or an approval lands. I will run it once without apply, once with. If the second run changes something the first plan did not show, I stop and read.

Homework stays on the laptop. Production changes wait in a pipeline with a brake.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-49-iac-in-pipelines

Tomorrow: Phase 5 mini project — one plan+apply from a pipeline, then destroy.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 50 — Sat 17 Oct 2026 — Mini Project + Recap (Phase 5)

**Document title:** `Day 50 — Phase 5 Mini Project & Recap`

```
Phase 5 recap: click-ops is a hobby; IaC is how you sleep.

Day 50 of #100DaysOfAzureDevOps. Mini project and recap for Phase 5 — Infrastructure as Code.

ARM for literacy, Bicep for Azure-native calm, Terraform for state and modules, then the same files in a pipeline. The mini project is not a landing zone. It is one resource group plus one storage account or a webapp skeleton, provisioned by the tool I picked on Day 41, from a pipeline, then destroyed after a screenshot.

I sleep better when the Portal is a view, not a source of truth. Click-ops is fun until the person who clicked is on leave.

What I am keeping from Phase 5

1. One primary tool, one honest reason
• The recap says why Bicep or why Terraform
• "Both" is not a reason. It is indecision with extra files

2. Plan/what-if before apply
• A diff I did not read still executes
• Pipeline + approval is the grown-up version of that rule

3. State and names are operational
• Remote state with locking, or Bicep without that class of ghost
• unique names, parameter files, destroy when the demo ends

4. Definition of done is boring
• plan+apply from pipeline once; destroy once
• A screenshot without secrets; RG gone or budget-watched

What I am doing in today's lab

I am provisioning one RG plus storage or a webapp skeleton via the chosen IaC in a pipeline, screenshotting the green run, destroying after, and writing why I picked Bicep or Terraform. If I still have leftover day-42 RGs, those die too. Sleep is a cost-control strategy.

Hobbies can live in the Portal. Environments that must survive a weekend live in code.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-50-mini-project-recap-phase-5

Tomorrow: Docker fundamentals — images, layers, a hello Dockerfile.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 51 — Sun 18 Oct 2026 — Docker Fundamentals

**Document title:** `Day 51 — Docker Fundamentals`

```
Containers are shipping containers for processes — same app, fewer "works on my laptop" customs checks.

Day 51 of #100DaysOfAzureDevOps. Docker fundamentals.

The laptop had Node 20, a global package, and a .env that was never committed. Production had Node 18 and no global package. Customs seized the app at the border. A Dockerfile is how you ship the process with its language, its OS slice, and its start command — not a prayer that the destination looks like your desk.

Images, containers, layers, cache. COPY package*.json before COPY . so npm ci can cache. I have seen Dockerfiles that copy the universe first and then wait five minutes on every README change. Layer cache is a design, not a miracle.

Patterns I keep seeing

1. Image vs container
• Image is the immutable snapshot
• Container is a running instance of that snapshot
• Mutating a running container and calling it "the image" is how drift gets a hoodie

2. Dockerfile order is cache order
• FROM node:20-alpine, WORKDIR, COPY package*.json, RUN npm ci --omit=dev, COPY ., CMD
• Copy source before install and every code change busts the dependency layer

3. Pin the base
• node:20-alpine is a choice
• FROM node:latest is a surprise waiting for a Tuesday

4. Local proof before registries
• Docker Desktop on the personal PC
• Build and run the hello app until localhost behaves

What I am doing in today's lab

I am installing Docker Desktop on my personal PC, writing a hello Dockerfile for the sample app, building it, running it, and noting the cache behavior when I change a line of source versus a line in package.json. ACR is tomorrow. Today the process has to ship locally.

Pack the process. Stop negotiating with the destination's personality.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-51-docker-fundamentals

Tomorrow: Azure Container Registry — private closet for images.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 52 — Mon 19 Oct 2026 — Azure Container Registry (ACR)

**Document title:** `Day 52 — Azure Container Registry (ACR)`

```
ACR is a private closet for images — public Docker Hub is the thrift store.

Day 52 of #100DaysOfAzureDevOps. Azure Container Registry.

Public Hub is fine for base images you trust and for toys. Pushing an app image that contains your bits (and sometimes your accidentally copied .env) to a public registry is how a thrift store becomes a data leak. ACR is a private closet: tags, maybe ACR Tasks later, Basic SKU for the lab.

docker tag, docker push, az acr login. Unique registry names because they are globally unique, like storage. Delete images you do not need. Basic ACR still bills. Closets overflow.

What I keep seeing

1. Private by default for app images
• az acr create ... --sku Basic
• Hub for bases; ACR for myapp:day52

2. Tags are pointers, not comments
• myapp:day52 and later Build.BuildId
• :latest is a moving sign. Do not promote latest as if it were immutable

3. Login is identity
• az acr login -n <uniqueacr>
• Admin user enabled "for convenience" is a password in a drawer

4. Garbage collection is a habit
• Delete images you do not need
• Untagged manifests pile up like unread mail

What I am doing in today's lab

I am creating a Basic ACR in rg-day52, logging in, tagging myapp:latest as <uniqueacr>.azurecr.io/myapp:day52, pushing, confirming the repository in Portal, and deleting extra tags. If the name collides, I pick another unique name — I do not reuse a registry I do not own.

Put app images in a closet. The thrift store is for bases you intended to be public.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-52-azure-container-registry-acr

Tomorrow: Build and push images in pipelines — humans will push the wrong Friday tag.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 53 — Tue 20 Oct 2026 — Build & Push Images in Pipelines

**Document title:** `Day 53 — Build & Push Images in CI`

```
If humans push images by hand, humans will push the wrong tag on a Friday.

Day 53 of #100DaysOfAzureDevOps. Build and push images in pipelines.

Friday, 5:40pm, someone typed :latest when they meant the git SHA. I have been in that sentence. Docker@2 buildAndPush with tags $(Build.BuildId) and, if I must, latest as a convenience pointer — not as the promotion identity. Service connection to ACR. Multi-stage Dockerfile if the build needs a compiler the runtime does not.

Scanning is an intro today, not a platform. The pipeline is the point: the agent builds, the registry receives, a human does not copy-paste a tag from Slack.

Patterns I keep seeing

1. The pipeline is the only publisher
• Docker@2, containerRegistry: acr-connection, command: buildAndPush
• Laptop docker push in prod is how Friday tags happen

2. Tag with the build, not with a mood
• $(Build.BuildId) is boring and unique enough for a lab
• latest as a second tag is optional; promoting by latest is not

3. Multi-stage builds keep runtime thin
• Build in a fat image, copy the output into a slim one
• Shipping gcc into production is a hobby

4. Scan is a preview, not a vibe
• Know that image scanning exists
• A green push is not a CVE report. Later phases will be rude about that

What I am doing in today's lab

I am adding a pipeline that builds the Dockerfile, pushes to ACR with Build.BuildId (and latest if I want the pointer), using a service connection. I will not docker push from my PC for this proof. If the connection cannot push, I fix the identity, I do not enable admin and paste a password into a variable.

Humans are bad at Friday tags. Robots are consistent. Let the pipeline own the closet key.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-53-build-push-images-in-pipelines

Tomorrow: Azure Container Instances — container fast-food, delete after the test.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 54 — Wed 21 Oct 2026 — Azure Container Instances (ACI)

**Document title:** `Day 54 — Azure Container Instances`

```
ACI is container fast-food — no cluster gym membership required.

Day 54 of #100DaysOfAzureDevOps. Azure Container Instances.

AKS is a gym membership: easy to start, painful if you forget to cancel, overkill for a hello container. ACI is fast-food: run the image, get a DNS label, taste it, throw away the wrapper. I have seen teams skip ACI because it is not "real Kubernetes" and then spend a week on a cluster for a demo that needed a URL.

az container create with the ACR image, registry credentials, a unique dns-name-label, port 80. Then delete. ACI can surprise-bill if you leave it. Fast-food left on the table still appears on the card.

What I keep seeing

1. ACI is for run-and-done
• No node pools, no control plane you babysit
• Restart policy and CPU/memory still exist — it is not magic

2. Pulling from ACR needs identity
• registry-login-server, username/password or a better identity later
• A public image is easier and teaches the wrong privacy lesson for app bits

3. DNS labels collide
• --dns-name-label <unique>
• If create fails on the name, it is not Azure being rude. The name is taken

4. Delete after test
• ACI left running is a small silent bill
• The lab is the create and the delete

What I am doing in today's lab

I am running the image in ACI once with az container create, hitting the URL, then deleting the container (and RG if that was the point). I am not keeping ACI up overnight to feel cloud-native. Gym membership is optional and later.

Need a URL for a container tonight? Fast-food. Need orchestration? Then pay for the gym on purpose.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-54-azure-container-instances-aci

Tomorrow: Kubernetes fundamentals — Pods, Deployments, Services, and a lemonade-stand warning.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 55 — Thu 22 Oct 2026 — Kubernetes Fundamentals

**Document title:** `Day 55 — Kubernetes Fundamentals`

```
Kubernetes is an airport for containers — powerful, expensive, and overkill for a lemonade stand.

Day 55 of #100DaysOfAzureDevOps. Kubernetes fundamentals.

Pods, Deployments, Services, namespaces. The vocabulary is the ticket. The airport is real: scheduling, networking, identity, and a bill if you choose AKS too early. I have watched lemonade-stand apps land on a cluster because a résumé wanted the word Kubernetes. The app needed a container and a URL. It got an airport.

Prefer concepts plus kind or minikube if AKS cost is high. Write a Deployment+Service YAML. Apply locally. If there is no cluster, reading the YAML and tracing a request through Service → Pod is still the lab. AKS is tomorrow and optional.

Patterns I keep seeing

1. Pod is a wrapper, Deployment is the adult
• You rarely create naked Pods in production
• replicas, selector, template.labels must agree or the Deployment stares at an empty room

2. Service is how traffic finds Pods
• Labels, not IP folklore
• containerPort in the spec must match what the process listens on

3. Namespaces are tenancy lite
• default is fine for a lab
• Everything in default forever is how lemonade stands become lost luggage

4. Local cluster is a valid airport simulator
• kind/minikube for apply
• Read-only if I cannot run a cluster — still write the YAML

What I am doing in today's lab

I am writing a Deployment+Service YAML for the app (image from ACR, port 80), applying on local kind/minikube if I have it, or tracing the YAML on paper if I do not. I am not creating AKS today just to feel advanced.

Learn the airport. Do not land a lemonade stand there until the stand needs runways.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-55-kubernetes-fundamentals

Tomorrow: AKS setup — smallest cluster or skip; destroy the same weekend if I create it.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 56 — Fri 23 Oct 2026 — AKS Setup

**Document title:** `Day 56 — AKS Setup`

```
AKS is a gym membership for orchestration — easy to start, painful if you forget to cancel.

Day 56 of #100DaysOfAzureDevOps. AKS setup.

az aks create with one node is still a control plane, a node VM, and a billing relationship. I have seen "just a lab cluster" survive a quarter because destroy was nobody's job. Cost warning is not flavor text. AKS is not a daily-delete toy.

Optional: smallest AKS, or skip to Azure Container Apps as a path. If I create it, I schedule destroy the same weekend. kubenet vs CNI is a survey, not a thesis. Node pools exist. One node is enough to feel kubectl against Azure.

What I keep seeing

1. Create is the easy button
• az aks create -g rg-day56 -n aks-lab --node-count 1 --generate-ssh-keys
• The hard button is remembering it exists on day 59

2. Network plugin is a fork in the road
• kubenet vs Azure CNI: IP usage, network policy, complexity
• Survey today; do not rebuild the cluster three times to feel thorough

3. Skip is a valid engineering choice
• Container Apps / ACI if cost bites
• Skipping AKS is cheaper than a forgotten node

4. Destroy is scheduled, not hoped
• Calendar: this weekend
• If I cannot name the destroy date, I should not create the cluster

What I am doing in today's lab

I am either creating the smallest AKS and putting destroy on the calendar the same weekend, or skipping to a Container Apps mental path and writing why. I am not leaving a one-node cluster "for later phases" without a date. Later phases can recreate.

Gym memberships you forget still bill. Orchestrate on purpose, cancel on a date.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-56-aks-setup

Tomorrow: Deploy to AKS via pipelines — manifests, not sticky-note kubectl.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 57 — Sat 24 Oct 2026 — Deploying to AKS via Pipelines

**Document title:** `Day 57 — Deploying to AKS via Pipelines`

```
CD to Kubernetes without Git is sticky-note ops wearing a hoodie.

Day 57 of #100DaysOfAzureDevOps. Deploying to AKS via pipelines.

kubectl apply from a laptop is fine until three people do it with three versions of the manifest. Sticky notes. A hoodie. Azure DevOps can apply KubernetesManifest@1 from the repo: namespace, manifests: k8s/*.yml, a service connection that is not cluster-admin forever if I can help it.

If I have no AKS, I practice kubectl against local kind/minikube with the same pipeline shape, or I run the task against the local kubeconfig story and still keep YAML in Git. GitOps (Flux/Argo) is a later day. Push-from-pipeline is today's honest CD.

Patterns I keep seeing

1. Manifests live in the repo
• k8s/*.yml is the source
• A change that only exists on a workstation is not a release

2. The task is the apply
• KubernetesManifest@1 action: deploy
• Service connection / kubeconfig is identity — least privilege later in the security phase

3. Image tag must move
• If the YAML is stuck on :latest, I did not deploy a build — I deployed a mood
• Substitute Build.BuildId in the manifest or via Helm tomorrow

4. No cluster? Local still counts
• kind/minikube apply
• The anti-pattern is still sticky-note kubectl to "the" cluster

What I am doing in today's lab

If I have AKS, the pipeline applies manifests. If I do not, I apply the same files locally and keep them in Git. Either way I will not treat a manual kubectl as the production process. Hoodies are not a release strategy.

If Git does not know the cluster state you intended, you do not have CD. You have a memory.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-57-deploying-to-aks-via-pipelines

Tomorrow: Helm charts — values.yaml so environments stop being copy-paste crimes.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 58 — Sun 25 Oct 2026 — Helm Charts Basics

**Document title:** `Day 58 — Helm Charts Basics`

```
Helm is templating for YAML mountains — values.yaml is where environments stop being copy-paste crimes.

Day 58 of #100DaysOfAzureDevOps. Helm charts basics.

Three folders of nearly identical Kubernetes YAML is a crime scene. Helm's chart is a mountain with a trail: Chart.yaml, templates/, values.yaml. helm create myapp. Then values for image tag, replica count, environment. upgrade --install so install and upgrade are one thought.

I have watched teams fork a chart per environment and then forget to copy a security context. values.yaml is where env differences belong. Template drift is how prod missed a probe for six months.

What I keep seeing

1. create, then delete most of the sample
• helm create charts/myapp
• The sample chart is a tour, not a product

2. image.tag is a value
• helm upgrade --install myapp charts/myapp --set image.tag=$(Build.BuildId)
• Hardcoded latest in the template is the Friday tag again

3. One chart, many values files
• values-dev.yaml vs values-prod.yaml
• Not charts-dev vs charts-prod copies

4. uninstall is a lab skill
• Install, upgrade a tag, uninstall once
• Helm releases left behind are unnamed pets

What I am doing in today's lab

I am running helm create, packaging values for the image tag, install/upgrade once with --set image.tag, then uninstall. If I have no cluster, I still helm template and read the rendered YAML so I can see the Deployment the chart actually produced. Rendering is the point of the mountain. A chart I never render is just another folder of hopes.

Stop copying YAML mountains. Put the difference in values. That is the whole trick.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-58-helm-charts-basics

Tomorrow: AKS scaling, monitoring, networking — HPA vs fixed replicas.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 59 — Mon 26 Oct 2026 — AKS Scaling, Monitoring & Networking

**Document title:** `Day 59 — AKS Scale, Monitor, Network`

```
Autoscaling without metrics is superstition with YAML.

Day 59 of #100DaysOfAzureDevOps. AKS scaling, monitoring, and networking.

HPA, cluster autoscaler, ingress, network policies. A survey, not a CNI PhD. I have seen replica counts raised because "it felt slow" and HPA added because a tutorial had it, with CPU requests left at zero so the autoscaler stared at nonsense. Superstition. YAML.

HorizontalPodAutoscaler sketch: scale on CPU 70% between 1 and 5 replicas. That sentence requires requests to be set. Cluster autoscaler is nodes, not pods. Ingress is how HTTP enters. Network policy is who may speak. Time-box the deep CNI labs.

Patterns I keep seeing

1. HPA needs a signal
• CPU 70%, min 1, max 5 is a sketch
• Without resource requests, CPU utilization is a ghost story

2. HPA vs fixed replicas is a product choice
• Fixed is fine for a lemonade stand
• HPA is for load that actually moves
• I am writing when I would use which — not adding HPA as jewelry

3. Cluster autoscaler is a different lever
• Pods pending for lack of nodes vs pods needing more replicas on existing nodes
• Confusing them is how you scale the wrong thing

4. Ingress and network policy are the city gates
• Survey: ingress controller, TLS later
• Skip deep CNI if the clock says so — write what I skipped

What I am doing in today's lab

I am reading HPA docs, writing when I would use HPA vs a fixed replica count, and skipping a deep CNI lab if I am time-boxed. If the cluster still exists from Day 56, I am also checking whether destroy is still on the weekend calendar.

If you cannot name the metric, do not autoscale. YAML will happily encode the superstition.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-59-aks-scaling-monitoring-networking

Tomorrow: Phase 6 mini project — image in ACR plus one automated deploy path.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 60 — Tue 27 Oct 2026 — Mini Project + Recap (Phase 6)

**Document title:** `Day 60 — Phase 6 Mini Project & Recap`

```
Phase 6 recap: package once, run anywhere — but "anywhere" still has a bill.

Day 60 of #100DaysOfAzureDevOps. Mini project and recap for Phase 6 — containers and Kubernetes.

Dockerfile, ACR, pipeline build/push, ACI as fast-food, Kubernetes vocabulary, optional AKS, Helm, a glance at HPA. The mini project is one path: containerize the app, put the image in ACR, deploy via CI/CD. Prefer Container Apps or ACI if AKS cost bites. Architecture one-liner in the recap.

"Run anywhere" is a slogan. Anywhere with a registry pull, a CPU, and an invoice is the adult version.

What I am keeping from Phase 6

1. Image in ACR is the artifact now
• Not only a zip. A tagged image from the pipeline
• latest is not the promotion ID

2. One deploy path, automated
• ACI or Container Apps or AKS — one
• Three half-paths is not a recap. It is a buffet

3. Helm or manifests in Git
• No sticky-note kubectl as the process
• values.yaml for env differences

4. Cost is part of the architecture one-liner
• If AKS exists, destroy date is in the recap
• If I skipped AKS, that is an architecture decision, not a failure

What I am doing in today's lab

I am finishing image-in-ACR plus one successful automated deploy path, writing a one-line architecture, and killing ACI/AKS leftovers. Done = image in ACR + one successful deploy path automated. The bill should not include a forgotten gym.

Package once. Run on a path you can pay for and tear down. Slogans do not get invoices.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-60-mini-project-recap-phase-6

Tomorrow: Entra ID fundamentals — tenants, app registrations, identity as the bouncer list.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 61 — Wed 28 Oct 2026 — Azure AD (Entra ID) Fundamentals

**Document title:** `Day 61 — Entra ID Fundamentals`

```
Entra ID is the bouncer list for Azure — if identity is wrong, every other control is cosplay.

Day 61 of #100DaysOfAzureDevOps. Azure AD (Entra ID) fundamentals.

Tenants, users, groups, app registrations. Everything else in Azure assumes this list is right. I have watched beautiful RBAC and Key Vault designs collapse because the app registration was in the wrong tenant or the secret was taped to a wiki. If the bouncer list is wrong, the velvet rope is theater.

Personal tenant. Register an app day61-lab. Note the client ID. I am not putting a client secret in YAML. Tomorrow is Key Vault for secrets, or a certificate later. Redirect URI optional for this lab.

Patterns I keep seeing

1. Tenant is the building
• Work tenant vs personal tenant — labs stay personal
• A registration in the wrong directory is a bug that looks like RBAC

2. App registration is not a user
• It is an identity for an application
• Client ID is public-ish; client secret is not

3. Groups beat one-off assignments at scale
• Literacy: assign to groups
• Lab: I am one user, still do not make the app Owner of the subscription

4. Secrets have a next step
• Do not create a secret I will paste into a pipeline today
• Note the ID; Key Vault is the envelope later this week

What I am doing in today's lab

In the personal tenant I am registering app day61-lab, noting the client ID, and not creating a long-lived secret in a text file. Portal: Entra ID → App registrations → New registration. Redirect URI optional. Screenshot without secrets.

Fix the bouncer list first. Every other Azure control is cosplay if identity is a rumor.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-61-azure-ad-entra-id-fundamentals

Tomorrow: RBAC deep dive — Reader on a lab RG, Owner as a flamethrower.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 62 — Thu 29 Oct 2026 — RBAC Deep Dive

**Document title:** `Day 62 — Azure RBAC Deep Dive`

```
Owner is a flamethrower; prefer Reader/Contributor scoped to the RG, not the subscription.

Day 62 of #100DaysOfAzureDevOps. RBAC deep dive.

Built-in roles, custom roles, scope. Scope is the part people skip. Contributor on a resource group is a job. Owner on a subscription is a flamethrower with a smile. I have spent ten years watching "just give them Owner so they are not blocked" become the reason a delete went wider than the incident.

Today I assign myself Reader on a lab RG via CLI and I compare Contributor vs Owner in my notes. Mentally. I do not need to assign Owner to feel the difference. I have seen it.

What I keep seeing

1. Scope is the verb
• Role + assignee + scope
• az role assignment create --role Reader --scope .../resourceGroups/rg-day62

2. Built-ins cover most honesty
• Reader: look
• Contributor: change resources, not grant roles
• Owner: including the ability to grant — the flamethrower

3. Custom roles are a last mile
• Literacy: they exist when built-ins are too wide or too narrow
• Lab: do not invent a custom role for a Reader test

4. Subscription-wide is rarely a lab need
• RG scope is the muscle memory I want
• Subscription Owner for a pipeline is a future incident

What I am doing in today's lab

I am assigning my user Reader on rg-day62 via Azure CLI, verifying I cannot create in that assignment's intent, and writing Contributor vs Owner in one paragraph I could say out loud. Then I remove the assignment if it is leftover noise. Flamethrowers stay on the wall.

Scope the badge to the floor. Owner at the building level is not speed. It is blast radius.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-62-rbac-deep-dive

Tomorrow: Service connections and service principals — robot employees, scoped badges.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 63 — Fri 30 Oct 2026 — Service Connections & Service Principals

**Document title:** `Day 63 — Service Connections & SPs`

```
Service principals are robot employees — give them a badge scoped to one floor, not master keys.

Day 63 of #100DaysOfAzureDevOps. Service connections and service principals.

Azure DevOps needs an identity to talk to Azure. That robot used to be a secret-based service principal that someone rotated never. Workload identity federation (WIF) is how the robot proves itself without a password in a drawer. I have rotated expired SPN secrets at the worst possible hour. I would like fewer of those hours.

Project Settings → Service connections → Azure Resource Manager. Automatic is fine. Prefer WIF over long-lived secrets when the UI offers it. Least privilege: the connection should not be Owner.

Patterns I keep seeing

1. The connection is the badge
• Pipelines never get my user password
• A service connection with Contributor on one RG is a floor badge

2. WIF over client secrets
• Federation: Azure DevOps presents a token, Entra trusts it
• Long-lived secrets are postcards with a delayed explosion

3. Automatic vs manual
• Automatic is fast and often wider than you think — I will look at what it created
• Manual if I need a tighter SPN I created myself

4. One connection per environment later
• A single prod-or-everything connection is a master key with a friendly name
• Day 69 will be rude about that. Today I start the habit

What I am doing in today's lab

I am creating an Azure RM service connection (automatic is OK), preferring workload identity federation when possible, and checking the role it received. If it is Owner on the subscription, I treat that as a finding, not a convenience.

Robots need badges, not master keys. If it can deploy, it should not also be able to re-own the subscription.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-63-service-connections-service-principals

Tomorrow: Azure Key Vault — hotel safe, not repo chat history.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 64 — Sat 31 Oct 2026 — Azure Key Vault

**Document title:** `Day 64 — Azure Key Vault`

```
Key Vault is the hotel safe — secrets in repo chat history are postcards from an incident.

Day 64 of #100DaysOfAzureDevOps. Azure Key Vault.

Secrets, keys, certificates. Access policies vs RBAC. The hotel safe is not glamorous. It is why a connection string does not live in azure-pipelines.yml, a wiki, or a screenshot in a team chat. I have searched git history for a secret that was "removed" and still sat in an old commit. Postcards. They travel.

Create a vault with RBAC authorization. Secret DemoSecret with value not-a-real-password. Grant myself Key Vault Secrets User. unique vault names. This is still a lab value, not a real password.

What I keep seeing

1. RBAC on the vault is the modern door
• az keyvault create ... --enable-rbac-authorization true
• Access policies still exist; I am not mixing both as a hobby

2. Secrets User is enough to read secrets
• I do not need vault Owner to fetch DemoSecret
• Owner on the vault is another flamethrower

3. Dummy values only
• DemoSecret = not-a-real-password
• A real password in a learning vault that I will screenshot is a contradiction

4. Soft delete exists for a reason
• Literacy: deleted secrets can be recovered
• Purge protection is a real-world conversation; I note it, I do not skip the dummy secret

What I am doing in today's lab

I am creating a Key Vault, setting DemoSecret to a dummy value, granting my user Secrets User via RBAC, and proving I can read it in Portal or CLI. I am not pasting the value into the LinkedIn screenshot, the repo, or a chat.

Hotel safe. Not a postcard. If git ever saw it, rotate — do not "delete the line" and call it done.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-64-azure-key-vault

Tomorrow: Key Vault in pipelines — print length, never the value.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 65 — Sun 1 Nov 2026 — Integrating Key Vault with Pipelines

**Document title:** `Day 65 — Key Vault in Pipelines`

```
Pipelines that need secrets should fetch them — not store them in variable screenshots.

Day 65 of #100DaysOfAzureDevOps. Integrating Key Vault with pipelines.

AzureKeyVault@2 pulls secrets at runtime. Variable groups can link to a vault. The log should show asterisks. The step that prints length, never the value, is how I prove the fetch without mailing the postcard. I have seen "debug: true" turn a masked secret into a lesson for the whole company.

Link a variable group to Key Vault, or use the task with SecretsFilter: DemoSecret. Echo the length. If the value appears, I failed the lab even if the pipeline is green.

Patterns I keep seeing

1. Fetch at runtime
• AzureKeyVault@2 with the service connection and vault name
• Do not copy the secret into a pipeline variable "so it is easier"

2. Linked variable groups are a second door
• Group linked to Key Vault for DemoSecret
• Same rule: no screenshots of the value blade

3. Print length, not letters
• A lab-safe proof
• echo of the secret is how you practice incidents

4. Masking is not magic if you concatenate
• Some log tricks leak
• Do not get clever. Length is enough

What I am doing in today's lab

I am linking a variable group to Key Vault (or using AzureKeyVault@2), running a step that prints the length of DemoSecret, and reading the log for leaks. Green plus a visible secret is a red lab. I fix that before I sleep.

Fetch. Mask. Never souvenir the value. The pipeline is not a scrapbook.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-65-integrating-key-vault-with-pipelines

Tomorrow: Azure Policy — require a tag so Finance does not hunt with spreadsheets.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 66 — Mon 2 Nov 2026 — Azure Policy & Governance

**Document title:** `Day 66 — Azure Policy & Governance`

```
Policy is the grown-up saying "no untagged RGs" so Finance does not hunt you with spreadsheets.

Day 66 of #100DaysOfAzureDevOps. Azure Policy and governance.

Policy definitions, initiatives, compliance. Blueprints are retired; I am not learning a dead product to sound enterprise. Policy plus landing-zone ideas are the current sentence. A built-in like "require a tag on resource groups" assigned to the lab subscription or RG is enough to see the compliance blade light up.

I have watched untagged resource groups become a quarterly forensic exercise. Policy is how you stop playing detective with Cost Management exports.

What I keep seeing

1. Built-ins before custom JSON
• Require a tag on resource groups
• Assign, then create an RG without the tag and watch deny or audit

2. Audit vs deny is a culture choice
• Audit: you see sin
• Deny: sin cannot land
• Labs can deny. Production often starts with audit so you do not break a factory

3. Initiatives are bundles
• Literacy: many policies as one assignment
• Lab: one policy, one assignment, one compliance look

4. Scope again
• Assignment at MG / subscription / RG
• A policy at the wrong scope is a rumor that never fires

What I am doing in today's lab

I am assigning a built-in "require a tag on resource groups" to the lab subscription or a lab RG, opening the compliance blade, and creating a test RG that should fail or show non-compliant. Then I clean up so Policy does not nag a junk RG forever.

Let Policy be the grown-up. Spreadsheets are a slow bouncer.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-66-azure-policy-governance

Tomorrow: Compliance scanning in pipelines — SAST, deps, secrets.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 67 — Tue 3 Nov 2026 — Compliance Scanning in Pipelines

**Document title:** `Day 67 — Compliance Scanning in CI`

```
Shift-left security means finding the fire in the kitchen, not on the evening news.

Day 67 of #100DaysOfAzureDevOps. Compliance scanning in pipelines.

SAST, dependency scanning, secret scanning. The kitchen is the pull request. The evening news is a leaked key in a public gist. I have seen both. Adding a scan that publishes a summary and fails on high if the tool allows it is the lab. Perfect coverage is not. A scan you ignore is décor.

Mindset: dependency scan on restore, secret scan on the repo, results as a pipeline summary. GitHub push protection on a mirror if that is what I have. Azure DevOps tasks vary; the habit does not.

Patterns I keep seeing

1. Secrets first — they are already a fire
• Scan the repo; fail if a key-shaped string lands
• Yesterday's Key Vault work is wasted if today's commit contains DemoSecret's cousin

2. Dependencies are the supply chain
• Restore/install is when you learn you pulled a CVE
• A lockfile without a scan is a list, not a control

3. SAST is the slow cousin that still matters
• If I have a task, I run it
• If I do not, I document the gap instead of pretending

4. Publish results where humans look
• Pipeline summary, not a log line 4,000 down
• Fail on high if the tool can; warnings-only is how kitchens burn politely

What I am doing in today's lab

I am adding a secret scan task or enabling push protection on a personal mirror, failing the build on high vulnerabilities if the tool allows, and capturing a summary. If the marketplace task is too spicy (Day 83 energy), I still run an open-source scanner in a script. The fire drill is the point.

Find it in the kitchen. Evening news is for people who skipped the PR.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-67-compliance-scanning-in-pipelines

Tomorrow: DevSecOps shift-left — Security stage before Deploy.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 68 — Wed 4 Nov 2026 — DevSecOps - Shift-left Security

**Document title:** `Day 68 — DevSecOps Shift-left Security`

```
Security as a final boss stage is how you ship late — put checks next to the commit.

Day 68 of #100DaysOfAzureDevOps. DevSecOps — shift-left security.

A stage named Security that runs after everyone wanted to go home is a boss fight. People skip it, mark it optional, or "temporarily" continueOnError. Shift-left means Build, then Security, then Deploy — and Security exits non-zero on critical CVEs so Deploy never starts.

I have been on trains where security was a weekly meeting. The meeting always lost to the release date. A pipeline stage with fail criteria in a doc is ruder and kinder.

What I keep seeing

1. Order is a control
• stages: Build, Security, Deploy
• Security that runs in parallel with Deploy is a race, not a gate

2. Fail criteria are written
• Critical CVE = fail
• Secret detected = fail
• Medium = warn in the lab if I must, not silent

3. continueOnError is a confession
• If Security has it, I do not have shift-left
• I have a dashboard of regret

4. Left means next to the commit
• PR validation includes the security job when I can
• Main-only scans are how badness waits for merge

What I am doing in today's lab

I am adding a pipeline stage Security before Deploy, documenting fail criteria in a short markdown file, and running once with a forced failure (or a dummy critical) to watch Deploy stay still. If Deploy still runs, the dependsOn/condition is theater.

Do not save security for the final boss. Put it next to the commit so the release date cannot vote it off the island.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-68-devsecops-shift-left-security

Tomorrow: Secure pipeline design — least privilege, locked main, no secret echo.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 69 — Thu 5 Nov 2026 — Secure Pipeline Design

**Document title:** `Day 69 — Secure Pipeline Design`

```
A secure pipeline is boring on purpose — drama belongs in Netflix, not release logs.

Day 69 of #100DaysOfAzureDevOps. Secure pipeline design.

Least privilege agents, approvals, protected branches. The audit is personal: who can edit pipelines? who can approve prod? Is there a broad Owner SPN leftover from a lab? I have reviewed pipelines that could push to production from a feature branch with a PAT that never expired. That is a series. It should not be my series.

Checklist: separate service connections per env, no secret echo, main locked, prod approval required. Boring. Correct.

Patterns I keep seeing

1. Who can edit YAML is who can ship
• If Contributors can rewrite the prod stage, approvals are a speed bump around a hole
• Branch policies on main: PR, required checks

2. Separate connections per environment
• Dev connection cannot touch prod RG
• One connection to rule them all is Day 63's master key again

3. Agents are part of the threat model
• Hosted is isolated-enough for these labs
• Self-hosted with org-wide access is a lateral-movement hobby

4. No secret echo, still
• system.debug on a secret job is how Netflix writes itself
• I re-check Day 65 habits

What I am doing in today's lab

I am auditing who can edit pipelines and who can approve prod, removing any over-permissioned Owner SPN from the lab if I created one, locking main if it is not locked, and ticking the checklist in a file. If I cannot answer "who can ship," I do not have a secure pipeline. I have hope.

Bore the attacker. Bore your future self. Keep the drama in fiction.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-69-secure-pipeline-design

Tomorrow: Phase 7 mini project — secret not in YAML, policy visible, approvals on.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 70 — Fri 6 Nov 2026 — Mini Project + Recap (Phase 7)

**Document title:** `Day 70 — Phase 7 Mini Project & Recap`

```
Phase 7 recap: speed without security is just a faster incident.

Day 70 of #100DaysOfAzureDevOps. Mini project and recap for Phase 7 — security, compliance, and governance.

Entra, RBAC, service connections, Key Vault, pipeline fetch, Policy, scanning, shift-left, boring pipeline design. The mini project is one demo pipeline that fetches a secret, a tag policy that is actually assigned, and approvals on. Secret not in YAML.

I can ship faster by skipping all of it. I have seen that speed. It arrives at an incident with better velocity metrics.

What I am keeping from Phase 7

1. Identity, then RBAC, then secrets
• Bouncer list, scoped badges, hotel safe
• Skipping to Key Vault with Owner SPNs is cosplay

2. Policy is the tag adult
• Visible on the compliance blade
• Not a PDF of good intentions

3. Security stage before Deploy
• Fail criteria written
• No continueOnError confession

4. Definition of done
• Secret not in YAML; policy visible; approvals on
• Screenshot without secret values

What I am doing in today's lab

I am wiring one demo pipeline that fetches DemoSecret, confirming the RG tag policy is on, keeping prod approval, and writing the recap. If any secret printed this week, I rotate the dummy and fix the step. Speed is allowed. Unauthenticated speed is not a flex. The screenshot still shows asterisks, not letters. Policy blade still shows the assignment.

Faster incidents are still incidents. Phase 7 is the brakes that let Phase 4 go fast without lying. Wear them before you enjoy the velocity.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-70-mini-project-recap-phase-7

Tomorrow: Azure Monitor fundamentals — flashlight, not the fix.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 71 — Sat 7 Nov 2026 — Azure Monitor Fundamentals

**Document title:** `Day 71 — Azure Monitor Fundamentals`

```
If you cannot see it, you cannot fix it — Monitor is the flashlight, not the fix.

Day 71 of #100DaysOfAzureDevOps. Azure Monitor fundamentals.

Metrics, logs, activity log, diagnostic settings. A flashlight does not patch the hole. It tells you which wall is wet. I have been in war rooms where nobody had diagnostics enabled, so we argued from Portal screenshots and feelings. The fix was later. The seeing should have been first.

Enable diagnostics on a lab resource to Log Analytics — or note the cost and skip long retention. Activity log is the control-plane diary. Metrics are the pulse. Logs are the sentences. I am not building a SIEM today. I am turning on a light.

Patterns I keep seeing after a decade in delivery

1. Metrics vs logs vs activity
• Metrics: CPU, length of a queue, availability
• Logs: the story in rows
• Activity: who changed what in ARM

2. Diagnostics are opt-in more often than people think
• App Service / Key Vault / NSG — pick one lab resource
• Without diagnostic settings, the workspace is an empty room

3. Retention is a bill
• Lab: short retention or skip if cost is tight
• Infinite logs is not maturity. It is a storage hobby

4. Monitor is not the product fix
• A pretty chart of 500s is still 500s
• The flashlight's job is to end the argument about reality

What I am doing in today's lab

I am opening Monitor → Overview, enabling diagnostic settings on one lab resource (App Service or Key Vault) to a workspace if cost allows, and writing which signal I would use to detect "it is down." If I skip the workspace, I still map metrics vs logs vs activity on paper.

Turn on the light before you argue. Monitor does not heal. It stops the guessing.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-71-azure-monitor-fundamentals

Tomorrow: Log Analytics and KQL — AzureActivity, top operations, a saved query.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 72 — Sun 8 Nov 2026 — Log Analytics Workspace & KQL

**Document title:** `Day 72 — Log Analytics & KQL`

```
KQL is SQL's cousin who lives in the cloud and judges your where-clauses.

Day 72 of #100DaysOfAzureDevOps. Log Analytics workspace and KQL.

A workspace is a database for telemetry. KQL is how you ask it questions without exporting to Excel to "just filter." I have watched people screenshot 10,000 rows. The cousin is judging. summarize, where TimeGenerated, top 10. Save a query so tomorrow-you is not reinventing the where-clause.

Three queries: AzureActivity is a friendly start even when Heartbeat is empty. ago(1d), count by OperationNameValue. If the workspace is new and quiet, that is data too — I note it instead of faking a graph.

What I keep seeing

1. Time is always part of the question
• where TimeGenerated > ago(1d)
• Unbounded queries are how you wait and pay

2. summarize is the adult SELECT
• count() by OperationNameValue
• top 10 by count_ — a ranking, not a dump

3. Save the query
• A useful KQL that lives only in a chat will die
• Workspace saved queries are the notebook

4. Empty is a result
• No Heartbeat if I never onboarded VMs
• AzureActivity on a quiet lab sub may be thin — I run it anyway and say what I see

What I am doing in today's lab

I am running three KQL queries (AzureActivity sample plus two variations), saving one, and screenshotting results without tenant gossip. If the workspace has no logs, I enable a diagnostic from Day 71 first rather than inventing a table.

Ask the cousin a precise question. Excel is not a Log Analytics strategy.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-72-log-analytics-workspace-kql

Tomorrow: Application Insights — GoPro on the app, connection string not in git.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 73 — Mon 9 Nov 2026 — Application Insights Integration

**Document title:** `Day 73 — Application Insights`

```
App Insights is a GoPro on your app — embarrassing, invaluable.

Day 73 of #100DaysOfAzureDevOps. Application Insights integration.

Instrumentation, dependencies, live metrics. A GoPro will record you dropping the ball. That is the point. I have shipped apps whose only telemetry was IIS logs and a prayer. Failures map, dependency arrows, a request that took 8 seconds because it waited on a DNS mistake — you see it when the SDK is in the app and the connection string is not in git.

Create Application Insights. Connect to the sample app or use a portal demo. Generate traffic. Look at failures. Connection string via Key Vault or app settings. Never commit it.

Patterns I keep seeing

1. Connection string is a secret
• App settings or Key Vault
• A connection string in source is a postcard with a camera attached

2. Dependencies tell the truth
• HTTP, SQL, Redis — the map of who you wait on
• A slow app with a clean CPU is often a slow friend

3. Live metrics are for the incident, not the wallpaper
• Use them when you are in it
• Do not require a human to stare at live metrics as the only alert

4. Generate traffic or you will admire an empty GoPro
• Hit the sample, fail on purpose once if I can
• Empty failures blade is not "we are reliable." It is "we are dark"

What I am doing in today's lab

I am creating Application Insights, pointing the sample (or portal demo) at it, generating traffic, opening the failures map, and confirming the connection string is not in the repo. If I cannot instrument the app today, I still create the resource and walk the blades with demo data honestly labeled as demo.

Embarrassing video is how you stop dropping the ball. No camera, no coaching.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-73-application-insights-integration

Tomorrow: Alerts and action groups — screams need a destination.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 74 — Tue 10 Nov 2026 — Alerts & Action Groups

**Document title:** `Day 74 — Alerts & Action Groups`

```
Alerts without action groups are screams into the void — polite, useless.

Day 74 of #100DaysOfAzureDevOps. Alerts and action groups.

A metric alert that emails nobody is performance art. Action groups are the destination: email to myself for the lab. I have inherited alert rules that fired for a year into a disabled mailbox. Polite screams.

Create an action group. Create an alert on CPU, availability test, or a log query I can force. Then fire it once if I can. An alert you have never received is a rumor about the future.

What I keep seeing

1. Action group first
• Email yourself (personal)
• SMS/webhook later — today is proof of delivery

2. Alert on something I can provoke
• Availability test on a URL I control, or CPU on a tiny SKU
• A 5xx alert on an app with no traffic will never graduate from theory

3. Severity is a language
• Sev 0 for "wake me"
• If everything is Sev 0, nothing is

4. Noise trains people to mute
• One alert that fires cleanly beats ten that flap
• I will delete the lab alert when I delete the resource

What I am doing in today's lab

I am creating an action group that emails my personal address, creating one alert rule, and trying to receive it. Monitor → Alerts → Create alert rule. If the email never arrives, the lab is not done. I check spam, then the action group.

Scream at an inbox that exists. The void does not page.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-74-alerts-action-groups

Tomorrow: Dashboards and workbooks — three tiles, not a novel.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 75 — Wed 11 Nov 2026 — Dashboards & Workbooks

**Document title:** `Day 75 — Dashboards & Workbooks`

```
A dashboard is a storyboard — if it needs a 30-min explanation, it is a novel, not a dashboard.

Day 75 of #100DaysOfAzureDevOps. Dashboards and workbooks.

Stakeholders will not read your KQL. They will glance at a storyboard. Three tiles: availability, failures, cost. If I need a guided tour, I built a novel. I have presented both. The novel loses the room.

Portal dashboard, pin charts from App Insights and Cost Management if I can. Share with myself only. Workbooks are the version with narrative and parameters; I can peek. Today is three tiles that tell a true short story.

Patterns I keep seeing

1. Three tiles, three questions
• Are we up?
• Are we erroring?
• Are we spending by accident?

2. Pin from the real blades
• App Insights charts, not a screenshot pasted as art
• Cost: even a lab sparkline keeps the habit honest

3. Share scope is identity again
• Myself only
• A public dashboard of a lab is still a data leak if I pin the wrong thing

4. Workbooks later for guided ops
• Literacy: parameters, steps, a runbook in portal form
• If the storyboard is already a novel, I cut tiles — I do not add chapters

What I am doing in today's lab

I am creating a dashboard, pinning availability, failures, and cost, and not sharing it beyond myself. If I do not have App Insights data, I pin what I do have and label a tile "no data yet" rather than inventing a healthy green.

Storyboard. Glanceable. If it needs a TED talk, it is not a dashboard.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-75-dashboards-workbooks

Tomorrow: Pipeline monitoring — a red build ignored for a week is culture, not YAML.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 76 — Thu 12 Nov 2026 — Pipeline Monitoring & Analytics

**Document title:** `Day 76 — Pipeline Monitoring`

```
A red pipeline ignored for a week is a culture problem wearing a YAML costume.

Day 76 of #100DaysOfAzureDevOps. Pipeline monitoring and analytics.

Build analytics, release analytics, flaky tests. Azure DevOps will show failure rate if I look. I have been on teams where main was red from Monday to Thursday because "it is always like that." That is not YAML. That is a culture that trained itself to ignore the fire alarm.

Open Pipelines analytics/insights. Note this week's failure rate. If I have few runs, I still look at the last ten and write which failed and why. Flakes get names or they get ignored forever.

What I keep seeing

1. Failure rate is a DORA cousin
• A number I can say out loud
• Zero runs is not 100% success. It is darkness

2. Flakes are incidents on installment
• Re-run until green is how you teach the team to ignore red
• Name the flake or delete the test. Do not live with a coin flip

3. Duration is a cost
• Hosted minutes, feedback delay
• A 40-minute CI that used to be 8 is a product problem

4. Insights are only useful if someone owns red
• Today: I own my lab pipelines
• If I leave a red run "for later," I am practicing the culture I am complaining about

What I am doing in today's lab

I am opening Azure DevOps → Pipelines → Analytics/Insights, noting failure rate this week (or last N runs), and fixing or documenting any red I am ignoring. Costume off. If it is red, it is mine.

Red is a signal. A week of mute is a culture. YAML is just the fabric.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-76-pipeline-monitoring-analytics

Tomorrow: Cost management — delete orphan RGs, tighten the budget alert.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 77 — Fri 13 Nov 2026 — Cost Management & Optimization

**Document title:** `Day 77 — Cost Management`

```
The best Azure skill is deleting things — empty RGs are silent subscriptions eating money.

Day 77 of #100DaysOfAzureDevOps. Cost management and optimization.

Budgets, alerts, right-sizing. I have seen more "mystery bills" from leftover labs than from a single large VM that someone at least knew existed. Empty resource groups with a forgotten Public IP, a Basic ACR, an AKS I swore I would kill. Silent eating.

Cost Analysis on the lab subscription. Tighten the budget alert from Day 1 energy. az group list, delete unused. Right-sizing is a sentence I will not fake with invented percentages. I will say what I actually deleted.

Patterns I keep seeing

1. Budgets are promises to future-you
• Alert before the invoice is a personality
• A budget you never look at is a sticker

2. Orphans hide in lists
• az group list -o table
• az group delete -n <old-rg> --yes --no-wait
• Names like rg-day42 that survived Day 50

3. Right-size after you see the graph
• Cost Analysis, filter by RG
• I will not invent a savings number I did not measure

4. Delete is a deploy skill
• Destroy from Terraform/Bicep when that is how it was born
• Portal delete when it was click-ops. Either way, gone

What I am doing in today's lab

I am opening Cost Analysis, tightening a budget alert, listing resource groups, and deleting unused lab RGs. I will mention what I deleted, not a fictional savings percentage. If AKS from Day 56 is still alive, today is its due date if the weekend already passed.

Deletion is cost optimization you can prove. Empty RGs are not free. They are quiet.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-77-cost-management-optimization

Tomorrow: Azure Advisor and Well-Architected — five pillars, one recommendation I actually judge.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 78 — Sat 14 Nov 2026 — Azure Advisor & Well-Architected Framework

**Document title:** `Day 78 — Advisor & Well-Architected`

```
Well-Architected is a report card — Advisor is the teacher who already knows you skipped networking homework.

Day 78 of #100DaysOfAzureDevOps. Azure Advisor and the Well-Architected Framework.

Five pillars: Reliability, Security, Cost, Operational Excellence, Performance Efficiency. Advisor will already have opinions about the leftover public IP and the VM with no backup. I am not pretending I scored 100. I am opening Advisor, picking one recommendation, and writing why I accept or dismiss it.

Dismiss without a note is how homework stays skipped. Accept without a change is a bookmark. One recommendation, one decision.

What I keep seeing

1. Pillars are a checklist for arguments
• A design that is cheap and down fails Reliability
• A design that is locked down and unpayable fails Cost
• Name the pillar you are trading

2. Advisor is noisy and still useful
• Open it on the personal subscription
• One rec: accept with a change, or dismiss with a sentence

3. Dismiss is allowed if honest
• "Lab resource, will delete today" is a reason
• "Not now" is not a reason

4. Do not fake a score
• I am not posting a Well-Architected assessment I did not run
• The lesson is the five pillars and one real Advisor row

What I am doing in today's lab

I am opening Advisor, choosing one recommendation, accepting it with a fix or dismissing it with a written why, and listing the five pillars in my notes. Teacher already knows about the networking homework. I might as well read the note.

Report cards work when you respond. Advisor is not a screensaver.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-78-azure-advisor-well-architected-framework

Tomorrow: Incident management — runbook for webapp down, blameless postmortem template.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 79 — Sun 15 Nov 2026 — Incident Management Basics

**Document title:** `Day 79 — Incident Management Basics`

```
Postmortems without blame create learning; postmortems with blame create silence.

Day 79 of #100DaysOfAzureDevOps. Incident management basics.

On-call concepts, runbooks, postmortems. I have sat in both kinds of review. The blameless one produced a checklist. The blame one produced quieter Slack and the same outage later. Silence is not reliability.

Write a one-page runbook for "webapp down" in /docs/runbook-webapp-down.md: Symptom → Checks → Mitigate → Communicate → Postmortem link. A template for a blameless write-up. I do not need a real outage to practice the shape. I need the page to exist before 2am.

Patterns I keep seeing

1. Runbooks are for 2am brains
• Short steps, named checks, a health URL
• A novel runbook will not be read in an incident

2. Mitigate is not root cause
• Swap back, scale, disable a flag — stop the bleeding
• Root cause waits until users can log in

3. Communicate is a step, not a side effect
• Who gets a message, what the status is
• Silence while you debug is how rumors fill the gap

4. Blameless is a writing rule
• What happened, what we believed, what we change
• Not who is stupid. That sentence trains people to hide the next incident

What I am doing in today's lab

I am writing the webapp-down runbook and a blameless postmortem template. Symptom → Checks → Mitigate → Communicate → Postmortem. If I have a real lab failure this week, I fill the template once. If not, the empty template still has headings I would not want to invent under stress.

Learn in the write-up. Silence in the write-up is how the outage books a sequel.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-79-incident-management-basics

Tomorrow: Phase 8 mini project — App Insights + one alert + one dashboard.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 80 — Mon 16 Nov 2026 — Mini Project + Recap (Phase 8)

**Document title:** `Day 80 — Phase 8 Mini Project & Recap`

```
Phase 8 recap: deploy is not done — observable is done.

Day 80 of #100DaysOfAzureDevOps. Mini project and recap for Phase 8 — monitoring and observability.

Monitor, KQL, App Insights, alerts that email someone, a three-tile dashboard, pipeline analytics, cost cleanup, Advisor, a runbook. The mini project is observability on a deployed app: App Insights + one alert + one dashboard. Definition of done: I can detect a forced failure within five minutes.

I have signed off deploys that were "done" because the pipeline was green. Users were already in the flashlight's dark zone. Observable is done.

What I am keeping from Phase 8

1. Flashlight, camera, scream, storyboard
• Monitor / App Insights / action group / dashboard
• Missing one is a blind corner

2. Five minutes is the test
• Force a failure I control
• If I cannot see it, the stack is décor

3. Cost and noise are part of ops
• Delete leftover RGs
• Mute is not a strategy; tune is

4. Incidents have paper
• Runbook + blameless template
• Even a lab deserves that habit

What I am doing in today's lab

I am wiring App Insights, one alert, one dashboard, forcing a failure I can reverse, and confirming I notice within five minutes. Recap without fake MTTR numbers. If I cannot force a failure, I say so and still finish the three pieces. Done means I can detect a forced failure, not that the dashboard is pretty.

Green pipeline is a conveyor belt. Observable is the product. Phase 8 is the difference between shipped and seen.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-80-mini-project-recap-phase-8

Tomorrow: Multi-repo vs monorepo — pick the drama I can afford.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 81 — Tue 17 Nov 2026 — Multi-repo & Monorepo Strategies

**Document title:** `Day 81 — Multi-repo & Monorepo`

```
Repo strategy is politics with folders — pick the drama you can afford.

Day 81 of #100DaysOfAzureDevOps. Multi-repo and monorepo strategies.

A monorepo is atomic PRs and shared pipelines. Multi-repo is clear ownership and a harder time changing a cross-cutting concern. I have lived in both. Both have politics. Folders are just how the politics render.

This lab stays a monorepo for samples — that is an ADR, not a religion. I will list when I would split repos for a real product: different lifecycles, different access, a library consumed by many. I will not list fake clients.

Patterns I keep seeing

1. Monorepo strengths
• One PR can change API and pipeline together
• Templates live next to consumers

2. Multi-repo strengths
• Permissions and release cadence can differ
• A noisy app does not rebuild a quiet library by accident — if you designed it that way

3. The cost is coordination
• Monorepo: CI graph and PATH discipline
• Multi-repo: versioning and "which commit is prod" meetings

4. Write the ADR
• this lab stays monorepo for samples
• Split when ownership or lifecycle actually splits — not when a blog post is trending

What I am doing in today's lab

I am writing an ADR that this 100-day repo stays monorepo, plus a short list of when I would split: different lifecycles, different access, a library consumed by many. No company names. Drama I can afford: one repo, many /src samples, pipelines that path-filter so a Node change does not rebuild .NET.

Pick the folder politics on purpose. Defaulting to ten repos is not enterprise. It is scatter.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-81-multi-repo-monorepo-strategies

Tomorrow: Pipeline templates — extract templates/build.yml and reuse it.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 82 — Wed 18 Nov 2026 — Pipeline Templates & Reusable YAML

**Document title:** `Day 82 — Pipeline Templates & YAML`

```
Copy-paste YAML is how organizations invent 14 slightly different ways to be broken.

Day 82 of #100DaysOfAzureDevOps. Pipeline templates and reusable YAML.

templates, extends, parameters. I have counted fourteen "standard" build pipelines that all forgot the same cache key. Copy-paste is a bug-spreading strategy. A template with projectPath is one place to fix the ritual.

Extract templates/build.yml. Reuse it from the main pipeline. parameters.projectPath. The first template can echo. The point is the call site, not a novel of abstractions on day one.

What I keep seeing

1. parameters are the contract
• projectPath: string
• A template with secret defaults nobody sees is a trap

2. Reuse from main
• steps: - template: templates/build.yml
• Two consumers tomorrow in the Phase 9 recap; one caller today is the seed

3. extends is the bigger hammer
• Literacy: a pipeline can extend a template that owns stages
• Lab: a step template is enough to feel the win

4. Fix once
• When Node 20 becomes Node 22, I want one file to change
• Fourteen files is how one team stays on 18 until an incident

What I am doing in today's lab

I am extracting templates/build.yml with a projectPath parameter and calling it from the main pipeline. echo Building the parameter is legal for the first cut. If I still have duplicated restore/build steps after this, I did not extract. I rearranged. The call site should look boring: one template line, one path.

One broken template is cheaper than fourteen unique snowflakes. Reuse is a reliability feature.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-82-pipeline-templates-reusable-yaml

Tomorrow: Marketplace extensions — spices, not a handful in the stew.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 83 — Thu 19 Nov 2026 — Azure DevOps Extensions & Marketplace

**Document title:** `Day 83 — Azure DevOps Extensions`

```
Marketplace extensions are spices — a pinch helps; a handful ruins the stew and the security review.

Day 83 of #100DaysOfAzureDevOps. Azure DevOps extensions and Marketplace.

Third-party tasks can save a week. They can also inject a publisher you did not vet, permissions you did not read, and a last-updated date from a previous geopolitical era. I have removed extensions after a review asked "who is this publisher?" and nobody had a sentence.

Browse Marketplace. Install one reputable extension or document why I install zero. Prefer Microsoft-maintained tasks for labs. Check publisher, permissions, last update.

Patterns I keep seeing

1. Publisher is part of the supply chain
• Microsoft-maintained first
• Unknown publisher + wide org permissions = spice dump

2. Last update is a smell
• Years of silence is not "stable." It may be abandoned
• I will not install abandonware to feel productive

3. Permissions on install
• Read the scopes
• An extension that can touch all pipelines is not a linter, it is a tenant guest

4. Zero is a valid install count
• Document why
• A clean org is a posture

What I am doing in today's lab

I am browsing Marketplace and either installing one extension I can defend (publisher, permissions, last update) or writing why the lab stays on built-in tasks. Prefer Microsoft-maintained for these labs. I will not sprinkle five tools on a hello pipeline just to feel enterprise. Zero installs with a written reason still counts as finishing the lab.

A pinch. Not a handful. The security review can taste every spice you added.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-83-azure-devops-extensions-marketplace

Tomorrow: Jenkins to Azure Pipelines — migrate pipelines, not nostalgia.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 84 — Fri 20 Nov 2026 — Migrating Jenkins to Azure Pipelines

**Document title:** `Day 84 — Jenkins to Azure Pipelines`

```
Jenkins migrations succeed when you migrate pipelines, not nostalgia.

Day 84 of #100DaysOfAzureDevOps. Migrating Jenkins to Azure Pipelines.

Jenkinsfile has a shape: agent, stages, post, credentials. Azure YAML has a mapping, not a religion. I have seen migrations that rebuilt the Jenkins UI in Azure DevOps because someone missed the blue ball. Nostalgia. The work is mapping stages to jobs, credentials to variable groups or Key Vault, agents to pools.

Today is paper: translate a sample Jenkinsfile. I am not standing up Jenkins. I am proving I can leave it without lying about feature parity.

What I keep seeing

1. agent → pool
• Jenkins label vs vmImage or a self-hosted pool
• "We need the same snowflake agent" might be true; it might be nostalgia

2. stages → stages/jobs
• post { always } becomes a job condition or a later stage
• Do not require identical names. Require identical guarantees

3. credentials → envelopes
• Jenkins credential store is not a reason to put secrets in YAML
• Variable group / Key Vault from Phase 7

4. Plugins are the trap
• Every Jenkins plugin is a negotiation
• If the plugin was the product, write that down — do not hide it in "the YAML is not ready"

What I am doing in today's lab

I am translating a sample Jenkinsfile (agent, stages, post) into Azure YAML on paper: stage→job, credentials→group/Key Vault, agents→pools. If I do not have an old Jenkinsfile, I write a tiny one first so the mapping is real, not abstract.

Migrate the guarantees. Leave the blue ball to memory. Nostalgia does not compile.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-84-migrating-jenkins-to-azure-pipelines

Tomorrow: Hybrid and multi-cloud CI/CD — insurance and complexity, survey only.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 85 — Sat 21 Nov 2026 — Hybrid & Multi-cloud CI/CD

**Document title:** `Day 85 — Hybrid & Multi-cloud CI/CD`

```
Multi-cloud is insurance and complexity — buy it for a reason, not a slide.

Day 85 of #100DaysOfAzureDevOps. Hybrid and multi-cloud CI/CD.

Azure Pipelines can deploy to other clouds. That sentence is true and expensive. Identity, secrets, network, three consoles, three bills. I have sat through slides titled "multi-cloud strategy" that were really "we might need AWS someday." Insurance. Complexity. Buy it when a constraint is real.

Survey only. Write risks: secrets, identity, network. Do not actually deploy to AWS unless a personal account is ready and I want that bill. Prefer one cloud deep in these 100 days. Pattern: build once in Azure DevOps, deploy with cloud-specific tasks if you must.

Patterns I keep seeing

1. Build once still applies
• The artifact or image is the passport
• Rebuilding per cloud is the ghost from Day 39 with extra stamps

2. Identity does not unify itself
• Entra vs IAM vs another IdP
• A secret copied into two clouds is two postcards

3. Network is the boring blocker
• Hybrid: self-hosted agents, VPN, private endpoints
• A hosted agent cannot see your on-prem by wishing

4. Slides are not constraints
• A reason: data residency, an existing estate, a product on two clouds
• Not a reason: the architecture diagram looks worldly

What I am doing in today's lab

I am writing a one-pager of risks (secrets, identity, network) and the rule for this series: one cloud deep. I am not opening AWS "just to try" unless I already have a personal account and a destroy plan. Survey, not a second gym membership.

Insurance is priced. If you cannot name the risk you are buying, it is a slide.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-85-hybrid-multi-cloud-ci-cd

Tomorrow: Disaster recovery and backup — RPO, RTO, restore or it is fiction.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 86 — Sun 22 Nov 2026 — Disaster Recovery & Backup

**Document title:** `Day 86 — Disaster Recovery & Backup`

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

## Day 87 — Mon 23 Nov 2026 — Azure Landing Zones

**Document title:** `Day 87 — Azure Landing Zones`

```
Landing zones are city planning for Azure — skip them and you get shantytowns of resource groups.

Day 87 of #100DaysOfAzureDevOps. Azure Landing Zones.

Enterprise-scale, hub-spoke, management groups, policy. Cloud Adoption Framework landing zone overview. I am not deploying a fake enterprise today. I am sketching a hub and spokes on paper for a fictional company — clearly fictional, no logos, no customers.

Hub: shared networking and firewall. Spokes: workloads. Policy at management groups so the shantytown cannot sprawl. I have inherited subscriptions that were a city without zoning. You can live there. You cannot grow there cleanly.

Patterns I keep seeing

1. Management groups are the map
• Platform vs landing zones vs sandboxes
• Policy at the right MG beats 200 identical assignments

2. Hub-spoke is a network story
• Hub: connectivity, DNS, firewall
• Spokes: apps that peer, not a mesh of accidents

3. Identity and governance ride along
• Entra, RBAC, Policy from Phase 7
• A landing zone without those is a VNet with optimism

4. Sketch, do not simulate a corporation
• Paper diagram, CAF overview
• No invented savings, no invented employees

What I am doing in today's lab

I am reading the CAF landing zone overview and sketching hub-spoke for a fake company on paper (or a private markdown). Hub, spokes, management groups, policy. Clearly fictional — no logos, no customers. I am not deploying a full enterprise-scale because that is how labs become shantytowns with extra steps.

Zone the city before the RGs squat. Planning is cheaper than archaeology.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-87-azure-landing-zones

Tomorrow: GitOps with Flux/Argo CD — the cluster is not a kubectl petting zoo.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 88 — Tue 24 Nov 2026 — GitOps with Flux/Argo CD

**Document title:** `Day 88 — GitOps with Flux / Argo CD`

```
GitOps means the cluster stops being a petting zoo for kubectl.

Day 88 of #100DaysOfAzureDevOps. GitOps with Flux or Argo CD.

Git as the desired state. A controller reconciles the cluster. A PR changes prod. No cowboy kubectl. I have been the cowboy. It is fun until three cowboys ride at once. GitOps is how the zoo gets a lock on the gate.

Read GitOps principles. Optional local Flux quickstart. Compare to Azure Pipelines push (Day 57). Push CD applies from a job. GitOps pulls from Git. Both can be mature. Mixing cowboy kubectl with either is the petting zoo.

What I keep seeing

1. Desired state is Git, not a memory
• If it is not in the repo, the cluster will drift back or fight you
• Hotfix via kubectl is a debt with interest

2. Controllers close the loop
• Flux/Argo reconcile
• A pipeline that only pushes still needs something to notice drift

3. PRs are the change window
• Review, then merge, then the cluster follows
• Prod access for humans can shrink

4. Optional quickstart, mandatory comparison
• Local Flux if I have time and a cluster
• Written comparison to Azure Pipelines push if I do not

What I am doing in today's lab

I am reading GitOps principles, optionally running a local Flux quickstart, and writing push-vs-pull in a short note. I will not kubectl into a reconciled cluster to "just fix it" as a habit, even in a lab. The zoo stays closed.

If the cluster is a petting zoo, Git is not the source of truth. The last cowboy is.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-88-gitops-with-flux-argo-cd

Tomorrow: Scaling DevOps for large teams — five platform capabilities for a 50-dev org.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 89 — Wed 25 Nov 2026 — Scaling DevOps for Large Teams

**Document title:** `Day 89 — Scaling DevOps for Teams`

```
Platform engineering is DevOps that productized the paved road.

Day 89 of #100DaysOfAzureDevOps. Scaling DevOps for large teams.

Governance, self-service, internal developer portals. A 50-dev org cannot all be YAML artisans. Someone paves a road: app pipeline template, RG + budget bootstrap, golden-path docs. I have seen platform teams that only said no, and platform teams that shipped a catalog. The second one scales. The first one gets shadow IT.

List five platform capabilities I would offer. Map them to Azure DevOps + templates. No fake org chart. No sales. Just the catalog I would want if I were the 50th developer.

Patterns I keep seeing

1. Self-service beats ticket theater
• A template to scaffold a pipeline
• A ticket to "please make a pipeline" does not scale to 50

2. Guardrails in the path, not in a PDF
• Policy, approvals, Key Vault from earlier phases
• A wiki named Golden Path that nobody's pipeline uses is art

3. Five capabilities is enough to think
• app pipeline template
• RG + budget bootstrap
• golden path docs
• plus two I actually care about: secret fetch, env promotion

4. Platform is a product
• Version the templates
• Talk to users. A paved road nobody walks is a mural

What I am doing in today's lab

I am listing five platform capabilities for a hypothetical 50-dev org and mapping them to Azure DevOps plus the templates folder from Day 82. Hypothetical means hypothetical. I am not inventing a customer. I am inventing a catalog I would want.

Pave the road. Productize it. Saying no at scale is not a platform. It is a queue.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-89-scaling-devops-for-large-teams

Tomorrow: Phase 9 mini project — one template, two consumers, two green runs.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 90 — Thu 26 Nov 2026 — Mini Project + Recap (Phase 9)

**Document title:** `Day 90 — Phase 9 Mini Project & Recap`

```
Phase 9 recap: enterprise is reuse plus guardrails, not more YAML copy-paste.

Day 90 of #100DaysOfAzureDevOps. Mini project and recap for Phase 9 — advanced and enterprise patterns.

Repo strategy, templates, marketplace restraint, Jenkins mapping, multi-cloud caution, DR that restores, landing zones on paper, GitOps vs push, a paved-road catalog. The mini project is the enterprise artifact: templates/ used by two sample pipelines, one green run each.

Enterprise is not a font on a slide. It is one fix that repairs two consumers, plus a gate that still bites.

What I am keeping from Phase 9

1. One template, two consumers
• If both are green, reuse is real
• If I duplicated to go green, I failed the recap with extra files

2. Guardrails from Phase 7 still apply
• Secrets, approvals, Policy
• A template that echoes secrets is a faster incident

3. Paper architecture counts
• Landing zone sketch, GitOps comparison, DR targets
• I do not need a fake enterprise subscription to have thought

4. Definition of done
• one template, two consumers, one green run each
• ADR for monorepo still true unless I changed it on purpose

What I am doing in today's lab

I am publishing templates/ consumed by two sample pipelines, running both to green, and writing the recap. Reuse plus guardrails. If a third pipeline still has pasted YAML, I extract or I admit it is leftover homework. Two green consumers is the definition of done — not a third unique snowflake.

Enterprise is not more YAML. It is less YAML, better gates, and a road people actually walk.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-90-mini-project-recap-phase-9

Tomorrow: Capstone 1 — thin vertical slice, not a fake ecommerce platform.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 91 — Fri 27 Nov 2026 — Capstone Project 1 - E2E App CI/CD

**Document title:** `Day 91 — Capstone 1: E2E App CI/CD`

```
Capstones fail from ambition — ship a thin vertical slice you can demo in 5 minutes.

Day 91 of #100DaysOfAzureDevOps. Capstone project 1 — end-to-end app CI/CD.

Reuse the earlier app. Harden CI/CD. Do not start a giant ecommerce from zero. I have watched capstones die under payments, recommendation ML, and twelve microservices that never took a single request. Ambition. The slice is one service, tests, pipeline, environment promotion, a README diagram.

Work in capstone/. MVP: one app, CI, CD to App Service or Container Apps. In: tests, pipeline, env promotion. Out: payments, ML, a fleet. A 5-minute demo is a design constraint, not a lack of seriousness.

Patterns I keep seeing after a decade in delivery

1. Reuse beats rewrite
• The sample from CI/CD phases is the product
• A new repo named shop-clone is how Day 100 arrives with nothing to pin

2. Vertical slice means a user-shaped path
• Build → test → artifact → deploy → URL
• Horizontal "all the YAML in the world" is not a demo. It is a junk drawer

3. README diagram is part of the build
• If I cannot draw it, I cannot demo it in five minutes
• Boxes: repo, pipeline, env, app

4. Scope control is a written list
• In / Out in capstone/README
• When I want to add a microservice, I read the Out list out loud

What I am doing in today's lab

I am defining the MVP in capstone/: one app, CI, CD to App Service or Container Apps, README diagram. I am not scaffolding payments. If the old pipeline is dusty, I harden it here — that is the work. Thin slice, demo-able.

Five minutes. One path. Ambition can wait for a product that has users.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-91-capstone-project-1-e2e-app-ci-cd

Tomorrow: Capstone 2 — same app in a container tuxedo.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 92 — Sat 28 Nov 2026 — Capstone Project 2 - Containers Path

**Document title:** `Day 92 — Capstone 2: Containers Path`

```
Day 92 is the same app in a container tuxedo — not a new Netflix clone.

Day 92 of #100DaysOfAzureDevOps. Capstone project 2 — containers path.

Containerize the capstone. ACR plus deploy. AKS optional. Same app as Day 91. A tuxedo is a costume change, not a new actor. I have seen people throw away a working zip deploy to start "real microservices" in week two of a capstone. They shipped neither.

Dockerfile, pipeline build/push, deploy via the path I already trust (Container Apps, App Service containers, or k8s YAML). Add /Dockerfile and k8s or containerapp yaml in the same repo.

What I keep seeing

1. Same repo, new packaging
• The code did not become a platform overnight
• The image is the artifact now — Build.BuildId tag, not latest-as-truth

2. AKS is still optional
• If cost bites, Container Apps or App Service
• A tuxedo that requires a forgotten cluster is a gym membership in silk

3. Pipeline must push
• No laptop docker push as the capstone story
• Day 53's Friday tag still applies in a nicer folder

4. README gains a box
• Registry + runtime
• The 5-minute demo still has to work

What I am doing in today's lab

I am adding a Dockerfile, a pipeline that builds and pushes to ACR, and a deploy of the same app. AKS only if I will destroy it. Netflix clones are out of scope with extra neon. Tuxedo on. Same actor.

Package the slice. Do not replace the slice with a streaming empire.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-92-capstone-project-2-containers-path

Tomorrow: Capstone 3 — Bicep or Terraform for two environments, destroy non-prod.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 93 — Sun 29 Nov 2026 — Capstone Project 3 - IaC Multi-env

**Document title:** `Day 93 — Capstone 3: IaC Multi-env`

```
Infra as code for your demo is the difference between a toy and a portfolio piece.

Day 93 of #100DaysOfAzureDevOps. Capstone project 3 — IaC multi-environment.

Terraform or Bicep for dev and staging. Wire to a pipeline. The demo that only exists because I clicked in Portal is a toy I cannot reproduce. The demo whose environments come from infra/ plus pipelines/infra.yml with plan/apply approvals is something I can talk about without waving my hands.

Two environments for the same capstone. Destroy non-prod when done. I will not keep two App Service plans as souvenirs.

Patterns I keep seeing

1. Same tool as Phase 5
• Do not switch Bicep to Terraform this week for spice
• Depth on one dialect beats a bilingual toy

2. Two envs, one module/template
• Parameters or tfvars, not a copied folder named infra-prod-final-FINAL
• Promotion of the app artifact is still Day 39's rule

3. Plan in CI, apply gated
• pipelines/infra.yml
• Approval on apply — even for my own lab prod-that-is-not-prod

4. Destroy is in the README
• Non-prod teardown steps
• A portfolio piece that bills forever is a trap I set for myself

What I am doing in today's lab

I am adding infra/ for the capstone, two environments, a pipeline with plan and gated apply, then destroying non-prod when the screenshot exists. Toy vs portfolio is whether a stranger could recreate the env from the repo without me on a screenshare.

If the environment is a rumor, the demo is a toy. Put it in code so the portfolio piece can be rebuilt.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-93-capstone-project-3-iac-multi-env

Tomorrow: GitHub portfolio — README that a stranger can run.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 94 — Mon 30 Nov 2026 — GitHub Portfolio Setup

**Document title:** `Day 94 — GitHub Portfolio Setup`

```
GitHub is your shop window — pinned repos with vague names are closed blinds.

Day 94 of #100DaysOfAzureDevOps. GitHub portfolio setup.

Clean READMEs, diagrams, pinned repos. I have opened GitHub profiles that pinned "test," "new-folder," and a fork with no description. Closed blinds. The capstone goes to personal GitHub sanitized: no secrets, no internal names, no employer content.

README sections: Problem, Architecture, Pipelines, Security, Cost notes, License. How to run. Screenshots that do not show secrets or someone else's data.

What I keep seeing

1. Sanitize on the way out
• No Key Vault values, no service connection names that leak a tenant
• Personal repo, personal time

2. README is the demo when I am not in the room
• Problem in one paragraph
• Architecture diagram
• How to run — if I cannot follow my own steps, the blinds are still closed

3. Pin with intent
• Pin the capstone, not a graveyard
• Vague repo names get a rename or a description that works without the name

4. Cost notes are honesty
• What SKUs I used, what I destroyed
• No invented savings. "F1 / Basic / deleted after" is a cost note

What I am doing in today's lab

I am pushing a sanitized capstone to personal GitHub and writing the README with Problem, Architecture, Pipelines, Security, Cost notes, License. I will click through how to run once as if I were a stranger. If I get stuck, the README is wrong.

Open the blinds. A pinned repo should explain itself without me on a call.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-94-github-portfolio-setup

Tomorrow: Personal site or blog — YAML translated into a story.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 95 — Tue 1 Dec 2026 — Personal Site / Blog for Case Studies

**Document title:** `Day 95 — Site / Blog for Case Studies`

```
A case study translates YAML into a story a non-terminal human can trust.

Day 95 of #100DaysOfAzureDevOps. Personal site or blog for case studies.

Publish a write-up of the capstone. GitHub Pages or a Dev.to article linking the repo. No employer content. YAML is evidence. The story is why the pipeline has brakes, why the image is tagged with a build id, why the secret is in Key Vault. A hiring manager or a future collaborator may not read azure-pipelines.yml first. They will read a title.

Title shape: How I built a small Azure DevOps CI/CD demo in public. Not a certification flex I did not earn. Not a client case I do not have.

Patterns I keep seeing

1. Story then evidence
• Problem, approach, what I would do differently
• Link the repo; do not paste 400 lines of YAML into the article

2. Public does not mean employer
• Personal labs only
• No internal diagrams, no "at my company we..." that identifies a workplace

3. One post is enough
• GitHub Pages or Dev.to
• Two platforms with half a draft is not a case study

4. Trust is specifics without theater
• I will describe labs I actually ran
• I will not invent traffic numbers or customers

What I am doing in today's lab

I am publishing one write-up that links the repo, with a title about the public CI/CD demo, and zero employer material. If the site is not live today, the draft still has to be complete enough to paste tomorrow. YAML stays in Git. The story stays in prose.

Translate the repo into a story. Humans trust a path they can follow, not a gist of tasks.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-95-personal-site-blog-for-case-studies

Tomorrow: AZ-400 skills outline — map labs to objectives, gap list, no cram night.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 96 — Wed 2 Dec 2026 — AZ-400 Certification Review

**Document title:** `Day 96 — AZ-400 Certification Review`

```
AZ-400 rewards people who built things — your labs are the study guide you already wrote.

Day 96 of #100DaysOfAzureDevOps. AZ-400 certification review.

Map 100 days to exam objectives. Gap-fill. I am not claiming a pass I do not have. I am downloading the skills outline, ticking what I practiced, and making a weekend study list for the gaps. Cramming the whole outline tonight is how people memorize portal clicks they never did.

The labs are the guide: YAML, environments, Key Vault, IaC, containers, Monitor. The outline will still contain items I skipped on purpose (Test Plans depth, a service I never opened). Those become the list. Not shame. A list.

What I keep seeing

1. Outline first, not a dump of dumps
• Official AZ-400 skills list
• Tick practiced vs skimmed vs never

2. Labs beat flashcards for this exam family
• If I deployed a slot, I can talk about slots
• If I only read about canaries, I mark it as a gap

3. Schedule gap study, not a hero night
• A weekend list with a few bullets
• Tonight is mapping, not a 6-hour binge I will not finish

4. No fake credential
• I will not write "AZ-400 certified" on anything until that is true
• Review is review

What I am doing in today's lab

I am downloading the skills outline, ticking what these 100 days actually touched, and writing a gap list for later. Link: Microsoft Learn AZ-400 exam page. I am not scheduling an exam in this post. I am not inventing a score.

You already wrote a study guide in YAML and markdown. The outline just tells you which chapters are missing.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-96-az-400-certification-review

Tomorrow: Mock interview — five questions out loud, happy path and failure path.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 97 — Thu 3 Dec 2026 — Mock Interview Prep

**Document title:** `Day 97 — Mock Interview Prep`

```
Interviews are pipelines for your career — rehearse the happy path and the failure path.

Day 97 of #100DaysOfAzureDevOps. Mock interview prep.

Common Azure DevOps scenario questions. Answer out loud. Record yourself once. It will be embarrassing in the App Insights sense — useful. I have bombed questions I could have built in a lab because I only ever typed, never spoke. Interviews are not a typing test. They are a pipeline: input question, stages of reasoning, an artifact called an answer, and a failure path when you do not know.

Topics: branching, YAML, secrets, rollback, DORA. Happy path and failure path. "I would look it up" is allowed if I then say where and what I would verify.

Patterns I keep seeing

1. Promote the same artifact
• How do you promote across envs?
• If my spoken answer rebuilds in prod, I go back to Day 39

2. Secret in a PR
• Rotate, purge from history if needed, treat the PR as an incident
• "Delete the line and merge" is the wrong failure path

3. Pipeline red on Friday 5pm
• Do not YOLO to prod to make the dashboard green
• Playbook: what is broken, who is affected, revert vs fix-forward with a clock

4. DORA without theater
• I can define the four metrics
• I will not invent a team's numbers I never measured

What I am doing in today's lab

I am answering five questions out loud and recording once: artifact promotion, secret in a PR, Friday red pipeline, branching, rollback. I will listen once. If I ramble, I write a 4-bullet version and say it again. Rehearsal is the lab.

Happy path and failure path. A career pipeline with only the happy path fails the first real run.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-97-mock-interview-prep

Tomorrow: Professional profile setup — policy first, draft offline.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 98 — Fri 4 Dec 2026 — Professional Profile Setup

**Document title:** `Day 98 — Professional Profile Setup`

```
Profiles are loud — make sure your contract allows the volume before you hit publish.

Day 98 of #100DaysOfAzureDevOps. Professional profile setup.

Marketplace profiles (the kind that imply paid work) are loud. Employment agreements are often quieter until they are not. I am reading moonlighting and IP policy before creating any paid profile. Draft offline. Activate only if allowed. Personal equipment, personal time, personal Azure — the same rules this whole series already used.

This post is not an invitation to hire me and not a tour of platforms. It is a reminder that a public portfolio and a paid-work profile are different volume levels. Policy first.

What I keep seeing

1. Policy before profile
• Read the actual agreement
• A draft in a local file is not a violation; a live paid profile might be

2. Portfolio links are the quiet version
• GitHub and the case study from Days 94–95
• They do not require a marketplace account

3. Personal equipment only
• The rule has not changed since Day 1
• Work laptop, work tenant, work time — still no

4. No targeting of anyone's customers
• Learning in public is not a prospecting list
• This series stays educational

What I am doing in today's lab

I am reading employer moonlighting policy before creating any paid profiles, drafting copy offline, and activating only if allowed. Checklist in notes: policy reviewed, portfolio links ready, personal equipment only. If policy says no, the draft stays a draft and GitHub still exists.

Volume is a choice. Contract first. Publish second. Loud is not the same as allowed.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-98-professional-profile-setup

Tomorrow: Outreach templates and pricing — solve a pain, keep rates private, still no sell on this series.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 99 — Sat 5 Dec 2026 — Outreach Templates & Pricing

**Document title:** `Day 99 — Outreach Templates & Pricing`

```
Pricing is a boundary — undercharging buys stress, overcharging without proof buys silence.

Day 99 of #100DaysOfAzureDevOps. Outreach templates and pricing.

I am writing two DM templates that offer a public walkthrough, not a "hire me" pitch, and I am noting a rate band privately. This LinkedIn series still does not sell. Templates without spammy CTAs. Pricing ranges are references in a private note, not a number I will invent here for theater.

The vibe of a decent DM: you published something useful, here is the link, happy to answer questions. The vibe of a bad DM is a cold résumé with a calendar link. I have received both. Only one gets a reply from me.

Patterns I keep seeing

1. Help first, ask never in this series
• This post has no website CTA
• The templates live in a private file, not as comments on strangers' jobs

2. Proof is the public repo
• Walkthrough link from Days 94–95
• Without proof, a high rate is silence; without a boundary, a low rate is stress

3. Rates stay private today
• A band in a note I do not publish
• I will not post a fake day rate to look senior

4. Spam is a reputation tax
• Mass DM is how you teach people to mute you
• Two templates, used rarely, beats fifty copies

What I am doing in today's lab

I am writing two DMs focused on solving a DevOps pain and pointing at the public CI/CD walkthrough, plus a private rate-band note. I am not dropping those DMs on this post. Tomorrow is launch day. Today is boundaries.

A boundary is a kindness to future-you. Spam is a tax. This series stays a classroom.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-99-outreach-templates-pricing

Tomorrow: Launch day — portfolio, recap, destroy leftovers, write the next 100.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

## Day 100 — Sun 6 Dec 2026 — Launch Day + Next 100 Days

**Document title:** `Day 100 — Launch Day + Next 100 Days`

```
Day 100 is not the finish line — it is the first public proof you can ship learning on purpose.

Day 100 of #100DaysOfAzureDevOps. Launch day and the next 100 days.

Pin GitHub repos. Post this recap. Write five goals for the next 100 days — a cert study plan, deeper AKS, a tougher capstone — policy permitting, still no employer leak. Celebrate without leaking workplace detail. Destroy leftover resources. Set budgets. Put the next cycle in /docs/next-100.md.

I have finished projects that never got a last mile: the README half-written, the RG still billing, the goals in my head. Launch is the last mile. Proof is public. The next 100 is a file, not a vibe.

What I am keeping from 100 days

1. A classroom, not a storefront
• No sales in this series, no fake customers
• The proof is labs, posts, and a repo a stranger can read

2. Delivery habits that survived the cute hooks
• Build once, promote the artifact
• Secrets in the safe, approvals on prod
• Plan before apply, observe after deploy, delete what you do not need

3. Capstone is a slice
• If it demos in five minutes, it launched
• If it is still a Netflix clone in my head, I cut it today and pin what exists

4. Next 100 is five goals, written
• docs/next-100.md
• Budgets on, leftovers destroyed
• Learning in public continues or it was a streak, not a practice

What I am doing in today's lab

I am pinning sanitized repos, publishing this recap, writing five goals, destroying leftover Azure, confirming budget alerts, and leaving a next-100 plan in markdown. Checklist: portfolio live, capstone README polished, this post live, resources destroyed or budgets set, next plan written. Then I go outside.

Ship the learning. Then schedule the next slice. Finish lines are for races. This was a practice.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-100-launch-day-next-100-days

Tomorrow: Keep going — the first public proof I can ship learning on purpose.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```
