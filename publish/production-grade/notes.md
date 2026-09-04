# Production Grade Azure — LinkedIn posts

**Separate track** from [#100DaysOfAzureDevOps](../README.md). Do **not** merge into the daily lesson post.

| | |
|---|---|
| **Cadence** | Every **3–4 days** while the 100-day plan runs (flexible) |
| **Style model** | Title + hook + patterns + controls — like Note 1 |
| **Voice** | ~10 years DevOps engineer |
| **Rule** | Topic must **not** be that day’s 100-day lesson |

**Format:** engaging title → story → patterns → what you change → closing line → hashtags.  
No “note N of 33.” No series countdown in the body.

Schedule: [REMINDERS.md](./REMINDERS.md) · Track rules: [README.md](./README.md)

---

## Note 1 — 24 Aug 2026

**Title:** Green pipeline. Red production. Why “Succeeded” is not enough.  
**Topic:** Pipeline success is not production health  
**Status:** Posted — https://www.linkedin.com/feed/update/urn:li:activity:7497701160330633216/

```
Green pipeline. Red production. Why “Succeeded” is not enough.

The pipeline was green.
The release was “successful.”
Support tickets started within twelve minutes.

That gap — CI/CD success versus production health — is where a lot of real DevOps work lives.

What usually happened

The build compiled.
Unit tests passed.
The artifact was pushed.
The App Service / VM / container took the new bits.
The job status flipped to Succeeded.

None of those steps prove a user can complete a login, place an order, or hit the API that matters.

A green pipeline means your delivery system did what you asked.
It does not mean the product is healthy.

Patterns I keep seeing after a decade in delivery

1. Health endpoint that always returns 200
• /health only checks process up, not dependency up
• Database, cache, or downstream API can be down while the probe is green

2. Config that never ran in CI
• Connection strings, feature flags, and slot settings applied only at deploy time
• Test suite never exercised the production configuration path

3. Rebuild per environment
• Staging ran build A
• Production rebuilt from the same commit and got a different dependency tree
• You did not promote an artifact — you rolled dice twice

4. No post-deploy smoke
• Traffic switched immediately
• First real validation was a customer

5. Rollback exists only in a runbook
• Nobody timed it
• Nobody owns who clicks it
• At 2am the “plan” is tribal knowledge

What I put after every production deploy

A short, automated smoke path — not a full regression:

• Hit the real URL (or internal gateway), not only localhost on the agent
• Authenticate with a synthetic account if the product needs auth
• Exercise one write and one read on the critical path
• Verify one dependency (DB ping, queue depth, or cache)
• Fail the release job if any check fails — do not only log a warning

Then decide rollback or forward-fix with a clock, not a debate.

Engineering rules that reduce this class of incident

• Promote the same immutable artifact: build once, deploy many
• Separate “pipeline succeeded” from “service accepted traffic”
• Make /health (or readiness) fail when critical dependencies fail
• Keep smoke checks in the pipeline or release gate, not in chat
• Practice rollback in non-prod until the time is known

One sentence I use with teams

If your definition of done for a release stops at “job status = Succeeded,”
you are measuring the conveyor belt — not the product.

Green build. Red users. That is a signal that validation ended too early.

Personal views from production delivery work. No employer or client details.

#DevOps #Azure #CICD #SRE #CloudComputing #ProductionEngineering #Automation
```

---

## Note 2 — 28 Aug 2026

**Title:** Connection pooling & the autoscaling trap: Why compute scale-out can kill your database.  
**Topic:** Compute autoscaling vs database connection ceilings  
**Status:** Posted — https://lnkd.in/p/gNvctge5

```
Connection pooling & the autoscaling trap: Why compute scale-out can kill your database.

The traffic spike hit.
Autoscaling kicked in smoothly from 4 instances to 32.

Within three minutes, response latency jumped from 45ms to 18s, followed by 504 timeouts.

Compute CPU was sitting at 22%.
The database was in complete cardiac arrest.

What actually happened

Stateless compute is easy to scale. Stateful backends are not.

Every app replica spun up with default settings: Max Pool Size = 100.
• 4 instances = max 400 connections.
• 32 instances = potential 3,200 connections.
The DB max limit was 1,200.

As new pods initialized, they flooded the DB with TCP handshakes and connection allocations. The database spent 100% CPU managing connection overhead—leaving zero cycles to run queries.

Compute scaled out to solve load, and created a self-inflicted DoS against its own data layer.

Engineering controls that prevent this:

• Calculate pool size: Set Max Pool Size = (Max DB Connections * 0.70) / Max Replicas.
• Separate probes: Liveness checks process only; do not run DB queries on frequent health checks.
• Add a proxy layer: Use PgBouncer or Azure DB Proxy to keep static pools to the engine.
• Add circuit breakers: Fail fast with cached responses instead of launching retry storms.
• Gradual scaling: Scale out in controlled steps rather than 4x jumps.

One rule from 10 years in the seat:
Autoscaling compute without bounding downstream connection limits is not elasticity. It is an amplification attack against your database.

#DevOps #Azure #CloudArchitecture #SRE #Database #Kubernetes #ProductionEngineering
```

---

## Note 3 — 1 Sep 2026

**Title:** The Cold-Start Storm: Why fetching secrets from Key Vault on startup took down our cluster.  
**Topic:** Key Vault rate limits during AKS rolling deployments  
**Status:** Posted — https://lnkd.in/p/g3bFxVCY

```
The Cold-Start Storm: Why fetching secrets from Key Vault on startup took down our cluster.

We rolled a routine patch to an AKS cluster running 60 microservices.
Rolling restart started smoothly.

Two minutes in, half the new pods were stuck in `CrashLoopBackOff`.
The existing pods were dying as Kubernetes cycled them.
Within five minutes, the entire ingress was returning 503 Service Unavailable.

Application code had zero bugs.
The database was healthy.
Azure Key Vault had started aggressively HTTP 429 throttling every single container.

What actually happened

Every microservice was configured to connect directly to Azure Key Vault on startup to fetch DB connection strings, API keys, and certificates.

In steady-state production:
Pods start occasionally. Key Vault handles a few requests per second with ease.

During a rolling deployment:
150+ pods initialized within a 45-second window.
Each pod requested 12 secrets sequentially.
That generated nearly 2,000 API requests to Key Vault in under a minute.

Azure Key Vault has strict transaction limits per vault (e.g., 2,000 ops/10s across an entire subscription tier).
The vault hit its rate limit and returned `429 Too Many Requests`.
Apps lacked exponential backoff on startup, failed their initialization checks, and immediately terminated.
Kubernetes saw dead pods and immediately restarted them—multiplying the request storm tenfold.

Engineering controls that eliminate this failure mode:

• Never fetch raw secrets on boot in runtime code:
Use the Azure Key Vault Provider for Secrets Store CSI Driver. Secrets are mounted directly as in-memory volumes or synced to Kubernetes Secrets. Pods read local files with zero HTTP calls to Key Vault.

• Implement local in-memory caching:
If services must query Key Vault via SDK, cache secrets with a TTL (e.g., 1–4 hours). Never fetch secrets per incoming request or on every internal dependency health check.

• Exponential backoff + Jitter on bootstrap:
Configure Azure SDK retry policies with randomized jitter so 50 pods don't retry failed requests at the exact same millisecond.

• Separate Key Vaults per workload:
Never share a single Key Vault between critical customer-facing APIs and heavy batch workers. Fault domains must remain isolated.

One rule I keep repeating in production:
Cloud services have rate limits. If your deployment architecture creates a synchronized surge against a shared API gate, you have built a self-inflicted DoS into your release process.

#DevOps #Azure #Kubernetes #CloudArchitecture #SRE #SystemDesign #Security #ProductionEngineering
```

---

## Note 4 — 3 Sep 2026

**Title:** The pipeline variable that was a secret for two years  
**Topic:** Plaintext secrets in Azure DevOps variable groups and debug logs  
**Status:** Posted — https://lnkd.in/p/ghVRPyxN

```
The pipeline variable that was a secret for two years.

It started as a temporary workaround.
Connection string in a Library variable group.
Not marked as secret.
"Just for this sprint."

Two years later it was still there.
Anyone who could edit the pipeline — or open a failed job with system.debug=true — had seen it.
Some had left the company. The value had not rotated.

What actually happened

Azure DevOps variable groups are convenient.
They are not Key Vault.

When a variable is not typed as secret:
• It can appear in job logs
• It can appear in REST API responses for users with permission
• It survives every pipeline YAML review because "the secret is not in git"

Debug mode makes it worse.
`system.debug=true` expands environment dumps.
A failed agent job becomes a credential dump with a green "Download logs" button.

The incident was not a sophisticated breach.
It was a weekend of rotation:
database passwords, service principal secrets, and a git history search for anything that looked similar.

Engineering controls that close this class of failure

• If it can open a database or call an API as a privileged identity, it is a secret — not a variable.
• Mark secrets as secret in variable groups, or better: link the group to Azure Key Vault.
• Prefer Key Vault references / Key Vault tasks over pasted connection strings.
• Ban `system.debug=true` on production pipelines except under break-glass procedure.
• Rotate on a calendar, not on an incident.
• Audit who can edit Library groups and who can download pipeline logs.

One rule I keep repeating in production:
A secret that lives in a plain pipeline variable is not "temporary configuration."
It is a shared password with an audit trail you will regret reading.

#DevOps #Azure #AzureDevOps #CICD #Security #SRE #CloudComputing #ProductionEngineering
```

---

## Note 5 — Day 16 (05 Sep 2026)

**Title:** The hook everyone bypassed with --no-verify

```
Production note 5 of 33 — #ProductionGradeAzure

The hook everyone bypassed with --no-verify

We had a beautiful pre-commit hook for secrets and format.
The wiki said “always run it.”

Production taught me the flag: `--no-verify`.

One engineer was late. One YAML file had a tab in the wrong place.
The pipeline failed 40 minutes later on a hosted agent
with a message nobody read because Slack was already on fire.

Hooks that can be skipped will be skipped.
Put the real gate on the server: PR build, secret scan, policy.

Local hooks are courtesy. Branch policy is the lock.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 6 — Day 19 (08 Sep 2026)

**Title:** A PAT in a screenshot and a weekend of rotation

```
Production note 6 of 33 — #ProductionGradeAzure

A PAT in a screenshot and a weekend of rotation

A well-meaning screenshot in a ticket:
pipeline log + a redacted-looking connection string that was not redacted
on the next page.

Then a PAT in a gist “just for the vendor,” expiry set to never.

The weekend was not architecture. It was rotation:
tokens, service connections, and a search through git history.

After that I treat every PAT like a password,
every log like it will be copied, and “never expires” as a bug.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 7 — Day 22 (11 Sep 2026)

**Title:** Disk full at 2:14am on the only self-hosted agent

```
Production note 7 of 33 — #ProductionGradeAzure

Disk full at 2:14am on the only self-hosted agent

The pipeline was “red for no reason.”
The reason was 0 bytes free on the only self-hosted agent.

Docker images. npm caches. Nobody owned cleanup.
The agent had been “fine” for months — until it was the only path to prod.

Hosted agents fail too, but they fail as cattle.
Self-hosted agents fail as pets with names.

If you self-host: disk alerts, a second agent, and a documented
“what we install on this box.” Otherwise you are one full disk away
from a frozen release train.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 8 — Day 25 (14 Sep 2026)

**Title:** npm install vs the lockfile — two different trees

```
Production note 8 of 33 — #ProductionGradeAzure

npm install vs the lockfile — two different trees

Dev machines ran `npm install`.
The pipeline ran `npm install` too — on a different day, different registry cache.

`package-lock.json` was in git. Nobody treated it as the contract.
A transitive dependency shifted. Tests still passed.
Production took the new tree. A subtle crypto/auth library broke login.

The postmortem was one line I now repeat:
the pipeline must install the lockfile, not “whatever npm feels today.”

`npm ci`. Frozen lockfile. Same Node version as prod.
Boring. Ships.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 9 — Day 28 (17 Sep 2026)

**Title:** CI green on main. CD deployed hotfix/temp.

```
Production note 9 of 33 — #ProductionGradeAzure

CI green on main. CD deployed hotfix/temp.

CI ran on `main` and went green.
CD had a default branch override in the UI from a hotfix week.
It deployed `hotfix/temp` that still had a debug flag.

The YAML file on `main` was innocent.
The pipeline definition in Azure DevOps remembered a click.

I now distrust any setting that exists only in the portal.
If it can change what gets deployed, it belongs in YAML
or it belongs in a documented, locked variable group.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 10 — Day 31 (20 Sep 2026)

**Title:** Click-ops release at midnight because YAML was not ready

```
Production note 10 of 33 — #ProductionGradeAzure

Click-ops release at midnight because YAML was not ready

Midnight incident. The person who knew YAML was asleep.
Someone opened Classic Release, picked a build from a dropdown,
and hit Deploy because the UI felt safer.

They picked the build from the wrong branch.
The dropdown does not lecture you.

YAML in git is not fashion. It is an audit trail
you can `git blame` after the call.

If you still have Classic: treat every dropdown deploy as an incident drill.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 11 — Day 34 (23 Sep 2026)

**Title:** Slot swap with the wrong sticky settings

```
Production note 11 of 33 — #ProductionGradeAzure

Slot swap with the wrong sticky settings

We swapped staging to prod.
Staging had been tested against a staging database (slot setting).
A different app setting was not sticky. It came along for the ride.

Users hit prod with a mix: new code, old config, staging-ish data path.
The swap was “successful.” The product was not.

Before any swap I now print:
what is sticky, what is shared, what will be live in 10 seconds.
Then I smoke-test the slot as if it were already prod — because after swap, it is.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 12 — Day 37 (26 Sep 2026)

**Title:** Half the farm on the old binary

```
Production note 12 of 33 — #ProductionGradeAzure

Half the farm on the old binary

We rolled a breaking API change across a farm.
Load balancer kept sending users to mixed versions.
Session stickiness made it “work on my machine” for some people.

Half the instances had the new schema expectation.
Half did not. Errors looked random. They were not random.

Rolling requires expand/contract:
compatible versions overlapping, then remove the old.
Or you are A/B testing an incident.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 13 — Day 40 (29 Sep 2026)

**Title:** Approval gates that only proved someone was awake

```
Production note 13 of 33 — #ProductionGradeAzure

Approval gates that only proved someone was awake

I have seen approval gates that proved only this:
someone’s phone unlocked and they tapped Approve
because the release was late and the group chat was loud.

That is not a change advisory board.
That is a speed bump with a rubber stamp.

Useful gates ask something a human can actually know:
smoke test passed, change ticket exists, business hours, rollback owner named.

If your gate is “any of 20 people,” you do not have a gate.

Next phase: IaC — so production is not a unique snowflake.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 14 — Day 43 (02 Oct 2026)

**Title:** Prod parameter file pointed at the test Key Vault

```
Production note 14 of 33 — #ProductionGradeAzure

Prod parameter file pointed at the test Key Vault

A parameter file named `prod.parameters.json`
still had the test Key Vault resource ID.
Copy-paste. Reviewers looked at the template, not the file next to it.

Deploy succeeded. App came up. Secrets were the test secrets.
Nobody noticed until a test user appeared in a prod report.

I now review parameter files like production code.
Names lie. Values do not — unless you skip the diff.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 15 — Day 46 (05 Oct 2026)

**Title:** State in git, apply from a laptop, one lock

```
Production note 15 of 33 — #ProductionGradeAzure

State in git, apply from a laptop, one lock

State lived in git “so we would not lose it.”
Two laptops, two applies, one corrupted mental model.
Then a third person ran apply because the pipeline was red.

Remote state + lock exists because humans overlap.

The other failure mode: apply from a laptop against prod
because “the pipeline takes 20 minutes.”

If it is prod, it goes through the pipeline.
If it cannot, you do not have prod access — you have a hole.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 16 — Day 49 (08 Oct 2026)

**Title:** Portal just this once vs the next pipeline run

```
Production note 16 of 33 — #ProductionGradeAzure

Portal just this once vs the next pipeline run

A firewall rule was needed for a demo.
Portal. 10 minutes. Customers unblocked.

Next pipeline run: Terraform/ARM wanted the old rule set.
Apply “corrected” production back to the diagram.
Demo died in front of people.

Two valid worlds. One state file. No process for exceptions.

The rule I use now:
portal changes to prod are incidents, or they are PRs to the IaC
before the next pipeline runs. There is no third option that stays healthy.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 17 — Day 52 (11 Oct 2026)

**Title:** Tag latest and a rollback that was not yesterday

```
Production note 17 of 33 — #ProductionGradeAzure

Tag latest and a rollback that was not yesterday

Rollback plan: “redeploy latest.”
Latest had been overwritten by a CI run during the incident.
We rolled back to the broken build with confidence.

Immutable tags (git SHA, build ID) are not ceremony.
They are how rollback means a specific blob, not a moving nickname.

I want the pipeline to push `abc123` and prod to run `abc123`.
Latest can exist for humans. Production should not depend on it.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 18 — Day 55 (14 Oct 2026)

**Title:** CrashLoopBackOff and the ritual restart

```
Production note 18 of 33 — #ProductionGradeAzure

CrashLoopBackOff and the ritual restart

The ritual was: delete the pod.
It came back. Delete again. War room nodded. Metrics still bad.

The app was crashing on a bad config map.
Restarting faster does not fix a wrong value.

I have wasted more hours on “just bounce it”
than I have on reading the last 50 log lines.

Probes, logs, events, then change.
Restart is for buying minutes, not for root cause.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 19 — Day 58 (17 Oct 2026)

**Title:** values-prod.yaml with a connection string in git history

```
Production note 19 of 33 — #ProductionGradeAzure

values-prod.yaml with a connection string in git history

Someone put a production connection string in values
“so the chart would work.” It was gitignored locally.
It was not gitignored on the machine that committed.

History does not forget. Rotation does not un-push.

Helm values for secrets: Key Vault, sealed secrets, or a pipeline
that injects at deploy time. Not a YAML file with a hopeful `.gitignore`.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 20 — Day 61 (20 Oct 2026)

**Title:** Guest account with Owner for the vendor, temporary

```
Production note 20 of 33 — #ProductionGradeAzure

Guest account with Owner for the vendor, temporary

A vendor needed access for a week.
Guest user. Owner on the subscription. Calendar invite: “remove after go-live.”

Go-live was 14 months later. The guest was still Owner.
The vendor employee had left. The account had not.

Break-glass accounts that nobody tests are also a story.
Unused until the day everyone who knew the password is on leave.

PIM, expiry, least privilege, a tested emergency account.
Identity problems feel slow until they are the whole incident.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 21 — Day 64 (23 Oct 2026)

**Title:** Pipeline variables that were secrets for two years

```
Production note 21 of 33 — #ProductionGradeAzure

Pipeline variables that were secrets for two years

“Temporary” pipeline variables:
password in a library group, not secret-typed, logged once in a debug run.

Two years later it was still there.
Everyone who had ever been a contributor had seen it.

Key Vault + Key Vault task / variable group linked to KV
is not extra Azure spend for fun.
It is how you rotate without grepping YAML.

If it can open a database, it is not a variable. It is a secret.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 22 — Day 67 (26 Oct 2026)

**Title:** continueOnError on the only gate that mattered

```
Production note 22 of 33 — #ProductionGradeAzure

continueOnError on the only gate that mattered

Security added a tool. The YAML had `continueOnError: true`
because the first run found 400 issues and the release was Friday.

Those 400 issues became background noise.
The one CVE that later mattered was in the noise.

I would rather fail on a small, owned allowlist
than pass with a dashboard nobody opens.

If leadership wants the scan, they also want the red build.
Otherwise they wanted a slide.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 23 — Day 70 (29 Oct 2026)

**Title:** Service principal with Contributor on the subscription

```
Production note 23 of 33 — #ProductionGradeAzure

Service principal with Contributor on the subscription

A service principal used by CI had Contributor on the subscription
“so the pipeline would not fail.”

That SP’s client secret lived in a variable group.
Anyone who could edit the pipeline could be the subscription.

Least privilege for pipelines:
resource group scope, federated credentials where you can,
secrets that rotate, logs that do not print them.

A pipeline identity is a production identity.
Treat it like a person who never sleeps and never forgets a token.

Next phase: Monitor — because secure and silent is still down.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 24 — Day 73 (01 Nov 2026)

**Title:** Sampling hid the outage; the dashboard said 200 OK

```
Production note 24 of 33 — #ProductionGradeAzure

Sampling hid the outage; the dashboard said 200 OK

The board said availability 100%.
Users said checkout failed.

Sampling was aggressive. The exception type was rare enough
to almost never land in ingested telemetry.
We were monitoring the sample, not the product.

I now ask: what is sampled, what is a metric alert vs a log alert,
and can I find one real failed request by id?

If you cannot follow a single user action through the logs,
you have a poster, not observability.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 25 — Day 76 (04 Nov 2026)

**Title:** A 41-minute pipeline nobody had timed on purpose

```
Production note 25 of 33 — #ProductionGradeAzure

A 41-minute pipeline nobody had timed on purpose

Nobody had a goal for pipeline time.
It grew the way kitchens grow dirty: one extra install, one extra test project,
one extra “just in case” publish.

Engineers started deploying from branches with fewer checks
because waiting felt worse than risk.

We treated duration like an SLO:
cache, parallel jobs, fail fast, stop publishing the same artifacts twice.

Speed is a safety control. Slow pipelines create shadow CD.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 26 — Day 79 (07 Nov 2026)

**Title:** A war room with twelve people and no incident commander

```
Production note 26 of 33 — #ProductionGradeAzure

A war room with twelve people and no incident commander

Twelve people on a call. Everyone SSHing. Duplicate restarts.
The customer status page stayed “investigating” for 90 minutes
because nobody owned the sentence.

MTTR was bad. MTTD was worse — we noticed via Twitter-before-it-was-paused,
not via an alert.

What I want in the first five minutes:
one incident lead, one person on user comms, one shared doc with timestamps,
rollback as a first-class option.

Heroics do not scale. Roles do.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 27 — Day 82 (10 Nov 2026)

**Title:** Thirty YAML files, one bug, thirty copy-paste fixes

```
Production note 27 of 33 — #ProductionGradeAzure

Thirty YAML files, one bug, thirty copy-paste fixes

Thirty pipelines. Same “checkout, npm, test, publish” with small snowflakes.
A Node version bump needed thirty PRs.
Three pipelines were missed. Those three became the incident.

Reusable templates + a version you pin
hurt the first week (everyone argues about the interface).
They save the year.

If two pipelines share 80% of steps, they share a template
or they share a future outage.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 28 — Day 85 (13 Nov 2026)

**Title:** Agent online, Azure unreachable, firewall unchanged

```
Production note 28 of 33 — #ProductionGradeAzure

Agent online, Azure unreachable, firewall unchanged

Self-hosted agent showed Online.
Jobs queued. Error: cannot reach `*.visualstudio.com` / Azure endpoints.
Someone’s “security hardening” the night before.

From the agent’s view, DevOps was down.
From Azure DevOps’ view, the agent was rude.

Hybrid runbooks need: explicit egress, a named owner for the proxy,
and a test job that runs hourly so you do not discover this at release time.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 29 — Day 88 (16 Nov 2026)

**Title:** kubectl apply then GitOps politely undeployed you

```
Production note 29 of 33 — #ProductionGradeAzure

kubectl apply then GitOps politely undeployed you

Hotfix on the cluster. Users recovered. We felt smart.
Flux/Argo saw drift and kindly put the old manifest back.

Outage round two, now with confusion.

If GitOps is on, the hotfix is a git commit (or a documented freeze).
Live cluster edits are how you get a revert you did not request.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 30 — Day 91 (19 Nov 2026)

**Title:** The simple pipeline that took checkout down

```
Production note 30 of 33 — #ProductionGradeAzure

The simple pipeline that took checkout down

The pipeline was simple: build, test, deploy App Service.
The outage was simple too: a config transform that only ran in Release,
a test suite that never hit that path, a slot setting nobody listed.

“Simple” pipelines fail in the gaps between stages —
the thing you did not promote, the test you did not run as prod.

My capstone standard is not more YAML.
It is: the same artifact, the same config rules, a smoke test after deploy,
and a rollback that does not require the original author.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 31 — Day 94 (22 Nov 2026)

**Title:** Ten years of work vs a green contribution graph

```
Production note 31 of 33 — #ProductionGradeAzure

Ten years of work vs a green contribution graph

I have interviewed people with beautiful READMEs
and no story about a rollback.
I have worked with people whose git history looks messy
and who have restored a region without a speech.

This 100-day repo is a lab trail.
The field notes are the other portfolio: what I would do differently
when the user is real.

If you show work, show a postmortem you sanitized,
a pipeline you sped up, a permission you removed.
Green squares are optional.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 32 — Day 97 (25 Nov 2026)

**Title:** The question they ask vs the outage they should ask about

```
Production note 32 of 33 — #ProductionGradeAzure

The question they ask vs the outage they should ask about

They ask: “What is blue-green?”
Production asks: “What was sticky, who approved, how did you know swap worked,
and what was the rollback clock?”

They ask: “What is Key Vault?”
Production asks: “Who could read the secret, where did it log, when did it last rotate?”

Study AZ-400 language. Answer with a timeline:
detect, contain, fix, prevent.

That is 10 years compressed into four verbs.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

## Note 33 — Day 100 (28 Nov 2026)

**Title:** What 10 years taught me that 100 days made say out loud

```
Production note 33 of 33 — #ProductionGradeAzure

What 10 years taught me that 100 days made say out loud

If I have to leave one sentence from ~10 years on-call and on-pipeline:

Ship smaller. Measure restore time. Never let a pipeline identity
be more powerful than the humans who review it.
Put the real gates in git, not in memory.

Tools will change. Azure will rename things.
The outages stay rhymed: drift, secrets, sampling, approvals that were not,
and a tag called latest.

Thank you for reading along.
I will keep learning in public — mistakes included, sales pitches not included.

Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.

#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic
```

---

