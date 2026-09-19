# -*- coding: utf-8 -*-
"""LinkedIn PDF handout specs for days 51–75 (#100DaysOfAzureDevOps)."""

from __future__ import annotations

SPECS: dict[int, dict] = {}

SPECS[51] = {
    "topic": "Docker Fundamentals",
    "subtitle": "Ship the process with its layers — not a prayer that prod looks like your laptop",
    "phase": "6 - Containers & Kubernetes",
    "tables": [
        {
            "title": "Architecture A — image, container, layer, tag (same Dockerfile, four products)",
            "columns": ["Object", "What it is", "What people confuse"],
            "rows": [
                ["Image", "Immutable filesystem layers + config, addressed by digest sha256:…", "The container that happens to be running on the laptop"],
                ["Container", "A running (or stopped) instance of an image. Writable layer on top", "docker commit of a mutated container as the new source of truth"],
                ["Layer", "Diff from one Dockerfile instruction. Cache key is that instruction + parents", "Cache as a miracle rather than COPY/RUN order"],
                ["Tag", "Mutable pointer (myapp:day51) that can move to a new digest", ":latest as a version. latest is a moving sign"],
                ["Digest", "Immutable content address. Pull by @sha256:… when you mean exactly this bits", "Optional decoration. Promotion identity lives here, not on latest"],
            ],
            "widths": [32, 78, 72],
        },
        {
            "title": "Architecture B — decide the Dockerfile like a cache design, not a blog paste",
            "columns": ["Constraint", "Default", "Change when"],
            "rows": [
                ["Base", "FROM node:20-alpine (pin major). Not node:latest", "You have a reason for distroless/debian — write it"],
                ["Dependency cache", "COPY package*.json → RUN npm ci --omit=dev → COPY .", "Never COPY . before install. README edits must not bust npm ci"],
                ["Runtime fat", "Single stage for a hello app", "Build needs a compiler the runtime image must not ship — then multi-stage"],
                ["Secrets", ".dockerignore excludes .env, .git, node_modules", "A secret in the image is in every layer forever"],
                ["Proof", "docker build + docker run on the personal PC", "ACR is tomorrow. Local process must start today"],
            ],
            "widths": [36, 76, 70],
        },
        {
            "title": "Architecture C — pitfalls that turn a 8s rebuild into a 5-minute customs check",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["COPY . before npm ci", "Every source typo rebuilds node_modules", "Reorder: manifests, install, then source"],
                ["FROM node:latest", "Tuesday image SKU change, different Node", "Pin 20-alpine; digest-pin if you are paranoid"],
                ["No .dockerignore", "Image contains .git, .env, local node_modules", "Add .dockerignore before the next build"],
                ["Mutate then commit", "Snowflake container nobody can rebuild", "Change the Dockerfile. Rebuild. Do not commit a running box"],
                ["Tag-only identity", "Which latest did we ship Friday?", "Record the digest. Treat tags as pointers"],
            ],
            "widths": [40, 71, 71],
        },
    ],
    "one_liner": "Containers are shipping containers for processes — same app, fewer 'works on my laptop' customs checks. Layer cache is a design, not a miracle.",
    "lab_intro": "Personal PC and personal Azure DevOps project azure-100-labs only. No employer Docker Desktop, no client app.",
    "lab": [
        "Install Docker Desktop on the personal PC (or confirm docker version already works). Do not use an employer-licensed install for this series.",
        "In the sample app repo, add a Dockerfile: FROM node:20-alpine, WORKDIR /app, COPY package*.json, RUN npm ci --omit=dev, COPY ., CMD. Add a .dockerignore that excludes .env, .git, node_modules.",
        "docker build -t myapp:day51 .  Note which steps show CACHED vs RUN. Touch README (or a source file) and rebuild. Touch package.json and rebuild. Write which layer busted.",
        "docker run --rm -p 3000:3000 myapp:day51  Hit localhost until the process answers. docker image ls and docker inspect myapp:day51 --format '{{.Id}} {{.RepoTags}}'.",
        "Write docs/docker-day51.md: image vs container in one sentence each, the cache observation, and the digest (or Image ID) you built. ACR is tomorrow — do not push yet.",
        "docker image prune is optional. Do not docker commit. If the app is not Node, same order: lockfile copy, install, then source.",
    ],
    "code_title": "Starter Dockerfile — cache order is the product",
    "code": "FROM node:20-alpine\nWORKDIR /app\nCOPY package*.json ./\nRUN npm ci --omit=dev\nCOPY . .\nEXPOSE 3000\nCMD [\"npm\", \"start\"]\n",
    "checklist": [
        "Can explain image vs container vs tag vs digest without saying the container is the image",
        "Dockerfile copies lockfile/manifests before source; .dockerignore exists",
        "Noted cache bust: source change vs package.json change",
        "docs/docker-day51.md on the personal repo; no employer screenshot",
    ],
    "tomorrow": "Azure Container Registry — private closet for images",
}

SPECS[52] = {
    "topic": "Azure Container Registry (ACR)",
    "subtitle": "App images belong in a private registry — Docker Hub is for bases you meant to be public",
    "phase": "6 - Containers & Kubernetes",
    "tables": [
        {
            "title": "Architecture A — ACR vs Docker Hub (same docker push, different closet)",
            "columns": ["Dimension", "ACR (azurecr.io)", "Docker Hub"],
            "rows": [
                ["Audience", "Private registry in your subscription. Default deny to the world", "Public-by-habit for tags unless the repo is paid-private"],
                ["Name", "Globally unique. myacr.azurecr.io/myapp:tag", "docker.io/library/… or your Hub namespace"],
                ["Auth", "az acr login / AcrPush+AcrPull RBAC / WIF. Admin user is a password in a drawer", "Hub credentials. Fine for public bases; wrong for app bits + .env accidents"],
                ["SKU", "Basic (lab), Standard, Premium (geo-replication, private link, retention)", "Hub plan limits. Not an Azure resource you can RBAC"],
                ["Tasks", "acr build / ACR Tasks can build in Azure. Optional literacy", "Hub automated builds are a different product. Not today's lab"],
            ],
            "widths": [28, 82, 72],
        },
        {
            "title": "Architecture B — decide where the bits live",
            "columns": ["Constraint", "Default", "Move when"],
            "rows": [
                ["Base images", "Pull pinned public bases (node:20-alpine)", "Air-gap / policy forbids public pulls — import into ACR"],
                ["App image myapp", "Push to ACR. Never Hub", "There is no valid lab exception"],
                ["Login", "az acr login -n <uniqueacr> (AAD)", "Pipeline tomorrow: service connection with AcrPush, not admin user"],
                ["SKU", "Basic for rg-day52", "Premium only for private link / geo-repl you can name"],
                ["Retention", "Delete tags you do not need today", "Untagged manifests pile up and still bill"],
            ],
            "widths": [32, 74, 76],
        },
        {
            "title": "Architecture C — pitfalls that leak an app into the thrift store",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Push to docker.io by habit", "docker push myapp:latest goes public-ish", "Retag to <acr>.azurecr.io/myapp:day52 first"],
                ["Admin user enabled for convenience", "Two passwords in Portal; they leak in screenshots", "admin-enabled false; AcrPush on an identity"],
                ["latest as the only tag", "Cannot say which bits ACI will pull tomorrow", "Tag day52 (and later Build.BuildId). latest is optional pointer"],
                ["Name collision", "az acr create fails; registry names are global", "Pick another unique name. Do not reuse a registry you do not own"],
                ["Leaving every tag", "Basic ACR still bills; untagged manifests linger", "az acr repository delete / untag what the lab does not need"],
            ],
            "widths": [42, 70, 70],
        },
    ],
    "one_liner": "ACR is a private closet for images — public Docker Hub is the thrift store. Put app bits in the closet; keep Hub for bases you intended to be public.",
    "lab_intro": "Personal Azure subscription only. Resource group rg-day52. Personal Azure DevOps project azure-100-labs.",
    "lab": [
        "az group create -n rg-day52 -l eastus. az acr create -g rg-day52 -n <uniqueacr> --sku Basic --admin-enabled false. If the name is taken, pick another — do not hijack a registry.",
        "az acr login -n <uniqueacr>. Confirm docker is talking to that login server, not docker.io.",
        "docker tag myapp:day51 <uniqueacr>.azurecr.io/myapp:day52 then docker push <uniqueacr>.azurecr.io/myapp:day52. Optional second tag :latest as a pointer only.",
        "Portal → Container registries → Repositories, or az acr repository show-tags -n <uniqueacr> --repository myapp -o table. Copy the digest, not only the tag.",
        "Do not enable admin user. Do not docker push the app image to Docker Hub. Delete extra tags you created as experiments.",
        "Write docs/acr-day52.md: registry name, tag, digest, and the one-line rule (Hub for bases, ACR for myapp). Leave the registry for Day 53 unless cost is tight — then note you will recreate.",
    ],
    "code_title": "Starter CLI — private tag, then push",
    "code": "az group create -n rg-day52 -l eastus\naz acr create -g rg-day52 -n <uniqueacr> --sku Basic --admin-enabled false\naz acr login -n <uniqueacr>\ndocker tag myapp:day51 <uniqueacr>.azurecr.io/myapp:day52\ndocker push <uniqueacr>.azurecr.io/myapp:day52\naz acr repository show-tags -n <uniqueacr> --repository myapp --detail -o table\n",
    "checklist": [
        "Basic ACR exists on the personal subscription; admin user is off",
        "myapp:day52 is in <acr>.azurecr.io, not on Docker Hub",
        "Can explain tag vs digest and why latest is not the promotion ID",
        "docs/acr-day52.md recorded the digest",
    ],
    "tomorrow": "Build and push the image from a pipeline — humans stop tagging on Fridays",
}

SPECS[53] = {
    "topic": "Build & Push Images in Pipelines",
    "subtitle": "The agent builds, ACR receives, a human does not copy-paste a tag from Slack",
    "phase": "6 - Containers & Kubernetes",
    "tables": [
        {
            "title": "Architecture A — laptop push vs pipeline publish (same image, different publisher)",
            "columns": ["Dimension", "docker push from PC", "Docker@2 buildAndPush"],
            "rows": [
                ["Who authenticates", "Your user via az acr login", "Service connection (AcrPush). Not the admin password in a variable"],
                ["Tag", "Whatever you typed. Friday :latest happens here", "$(Build.BuildId) plus optional latest pointer"],
                ["Dockerfile", "Whatever is on disk, dirty or not", "What Git has on that commit. Multi-stage if the build needs a compiler"],
                ["Scan", "Optional local Trivy if you remember", "Intro only today: a scan step can fail the job. Day 67 is the gate"],
                ["Audit", "No Build.BuildId, no commit SHA on the tag", "Repo + build number is the receipt"],
            ],
            "widths": [32, 72, 78],
        },
        {
            "title": "Architecture B — decide tags and stages with a constraint",
            "columns": ["Constraint", "Default", "Change when"],
            "rows": [
                ["Publisher", "Pipeline only for this proof", "Never laptop-push a tag you will run in ACI/AKS"],
                ["Tags", "$(Build.BuildId) required; latest optional pointer", "Promoting by latest is not a release process"],
                ["Dockerfile", "Single stage until compile tools appear", "Multi-stage: build in fat image, COPY --from=build into alpine/distroless"],
                ["Connection", "Docker Registry / ACR service connection, AcrPush on the RG or registry", "Admin user enabled 'so the pipeline works' — that is a finding"],
                ["Scan", "Know Trivy/Defender-for-DevOps exist; do not block the series on a marketplace tour", "Day 67: fail on secrets/critical CVEs with SARIF as the result format"],
            ],
            "widths": [28, 76, 78],
        },
        {
            "title": "Architecture C — pitfalls that publish the wrong bits on a Friday",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Laptop is still the publisher", "ACR shows a tag no build owns", "Disable personal push for this repo; Docker@2 is the only writer"],
                ["latest as identity", "ACI pulls 'latest' that moved two commits ago", "Substitute Build.BuildId into every run target"],
                ["Secret in a pipeline variable", "ACR admin password in Library", "Service connection with AcrPush. Admin stays off"],
                ["Build context includes .env", "Image layers contain the secret", ".dockerignore + never ARG for passwords"],
                ["Scan as wallpaper", "Green push, no CVE report", "A scan intro is fine; a green push is not a security attestation"],
            ],
            "widths": [40, 71, 71],
        },
    ],
    "one_liner": "If humans push images by hand, humans will push the wrong tag on a Friday. Let the pipeline own the closet key and tag with the build, not a mood.",
    "lab_intro": "Personal Azure DevOps org, project azure-100-labs. Microsoft-hosted ubuntu-latest. Personal ACR from Day 52.",
    "lab": [
        "Project Settings → Service connections → New → Docker Registry / Azure Container Registry. Use the personal ACR. Prefer identity over registry admin. Name it acr-connection.",
        "Confirm the identity has AcrPush on that registry (or RG). If the wizard created Owner on the subscription, that is a finding — tighten before you call the lab done.",
        "Add azure-pipelines.yml with pool vmImage ubuntu-latest and Docker@2 command buildAndPush, repository myapp, tags $(Build.BuildId) and optionally latest. Dockerfile path from the repo root.",
        "Run the pipeline. In ACR, confirm the Build.BuildId tag and digest. Do not docker push from the PC for this proof.",
        "Optional intro: a Trivy (or similar) step that prints CVEs but does not yet fail the whole CD path. Scanning as a gate is Day 67.",
        "Write docs/pipeline-push-day53.md: service connection name, build id tag, digest. If the job failed on auth, fix the identity — do not flip admin-enabled true.",
    ],
    "code_title": "Starter YAML — Docker@2 is the only publisher",
    "code": "trigger:\n  - main\npool:\n  vmImage: ubuntu-latest\nvariables:\n  imageRepository: myapp\n  tag: $(Build.BuildId)\nsteps:\n- task: Docker@2\n  displayName: Build and push to ACR\n  inputs:\n    command: buildAndPush\n    containerRegistry: acr-connection\n    repository: $(imageRepository)\n    Dockerfile: $(Build.SourcesDirectory)/Dockerfile\n    tags: |\n      $(tag)\n      latest\n",
    "checklist": [
        "Pipeline, not the laptop, produced the tag in ACR",
        "Tag includes Build.BuildId; latest is at most a pointer",
        "Service connection has AcrPush — admin user still off",
        "docs/pipeline-push-day53.md has the digest",
    ],
    "tomorrow": "Azure Container Instances — a URL without a cluster gym membership",
}

SPECS[54] = {
    "topic": "Azure Container Instances (ACI)",
    "subtitle": "Run one image, get a DNS label, delete the wrapper — no node pool required",
    "phase": "6 - Containers & Kubernetes",
    "tables": [
        {
            "title": "Architecture A — ACI vs AKS vs Container Apps (same image, three runtimes)",
            "columns": ["Dimension", "ACI", "AKS / Container Apps"],
            "rows": [
                ["What you operate", "A container group. No kubelet, no node pool", "AKS: control plane + nodes. Container Apps: scale rules, no cluster YAML"],
                ["Bill", "vCPU/memory/second while allocated. Easy to forget overnight", "AKS: nodes + control plane even at idle. CA: consumption or dedicated"],
                ["Pull from ACR", "AcrPull on a managed identity (--acr-identity). Not admin password in history", "kubelet / CA revision uses AcrPull or imagePullSecrets"],
                ["Network", "Public IP + --dns-name-label, or VNet-injected group", "Ingress / internal load balancer / CA ingress"],
                ["Fit", "Job, demo URL, sidecar-less hello", "AKS when you need kube API. CA when you want scale without kube YAML"],
            ],
            "widths": [32, 76, 74],
        },
        {
            "title": "Architecture B — decide fast-food vs gym membership",
            "columns": ["Constraint", "Default today", "Move off ACI when"],
            "rows": [
                ["Need a URL tonight", "az container create, unique dns-name-label, port the app listens on", "You need Deployments, HPA, or Helm — that is AKS, later"],
                ["Need scale to zero / HTTP scale", "ACI is not that product", "Azure Container Apps. Do not fake scale-to-zero with ACI restart policy"],
                ["Need kube API", "Stay on ACI for the hello", "Day 56 AKS — with a destroy date"],
                ["Identity to ACR", "User-assigned identity + AcrPull + --acr-identity", "Registry username/password. Lab last resort, not the pattern"],
                ["After the taste", "az container delete the same session", "Leaving ACI up 'to feel cloud-native' is a silent bill"],
            ],
            "widths": [38, 74, 70],
        },
        {
            "title": "Architecture C — pitfalls that surprise-bill or never start",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["dns-name-label taken", "Create fails on the name, not on the image", "Pick a unique label. Azure is not being rude"],
                ["Wrong port", "Group Running, browser hangs", "containerPort / --ports must match the process (3000 vs 80)"],
                ["Pull denied", "Waiting / CannotPull / unauthorized", "AcrPull on the identity; image tag exists; not Hub-by-accident"],
                ["Admin creds in CLI history", "Password in shell transcript", "--assign-identity + --acr-identity"],
                ["Forgot delete", "Next week's Cost Analysis mystery", "Delete is part of the lab. Restart policy Never for a one-shot"],
            ],
            "widths": [38, 72, 72],
        },
    ],
    "one_liner": "ACI is container fast-food — no cluster gym membership required. Taste the URL, throw away the wrapper. Fast-food left on the table still appears on the card.",
    "lab_intro": "Personal subscription. rg-day54 (or reuse rg-day52). Delete the container group before you close the laptop.",
    "lab": [
        "Create a user-assigned identity in the lab RG. Grant it AcrPull on the Day 52 registry. Do not enable ACR admin to 'just run ACI'.",
        "az container create with --image <acr>.azurecr.io/myapp:<Build.BuildId or day52>, --ports matching the process, --dns-name-label unique, --assign-identity and --acr-identity on that identity, --restart-policy Never, small CPU/memory.",
        "Wait until ProvisioningState Succeeded. Hit http://<label>.<region>.azurecontainer.io (or the IP). If it fails, az container logs — do not immediately jump to AKS.",
        "az container delete -g … -n hello-aci --yes. Confirm the group is gone. ACI left running is the lab failure even if the URL worked.",
        "Write docs/aci-day54.md: image tag used, whether identity pull worked, delete receipt. Optional: note when you would pick Container Apps instead (HTTP scale) vs AKS (kube API).",
        "Do not keep ACI overnight. Do not create AKS today to feel advanced.",
    ],
    "code_title": "Starter CLI — pull with AcrPull, then delete",
    "code": "az identity create -g rg-day54 -n id-aci-pull\nACR_ID=$(az acr show -n <uniqueacr> --query id -o tsv)\nPID=$(az identity show -g rg-day54 -n id-aci-pull --query principalId -o tsv)\naz role assignment create --assignee $PID --role AcrPull --scope $ACR_ID\nID=$(az identity show -g rg-day54 -n id-aci-pull --query id -o tsv)\naz container create -g rg-day54 -n hello-aci \\\n  --image <uniqueacr>.azurecr.io/myapp:day52 --os-type Linux --cpu 1 --memory 1 \\\n  --ports 3000 --dns-name-label <unique> --restart-policy Never \\\n  --assign-identity $ID --acr-identity $ID\naz container logs -g rg-day54 -n hello-aci\naz container delete -g rg-day54 -n hello-aci --yes\n",
    "checklist": [
        "One successful ACI run of the ACR image using AcrPull (not Hub)",
        "DNS/port actually answered, or logs explain why — then fixed",
        "Container group deleted in the same session",
        "docs/aci-day54.md notes identity vs admin-password temptation",
    ],
    "tomorrow": "Kubernetes fundamentals — airport vocabulary without buying the airport yet",
}

SPECS[55] = {
    "topic": "Kubernetes Fundamentals",
    "subtitle": "Learn the airport (Pod, Deployment, Service, namespace) before you land a lemonade stand on AKS",
    "phase": "6 - Containers & Kubernetes",
    "tables": [
        {
            "title": "Architecture A — request path (kube-system is not your app)",
            "columns": ["Object", "Job", "Where it lives"],
            "rows": [
                ["Namespace", "Tenancy lite. DNS and RBAC boundary", "workloads for the app. kube-system for CoreDNS, kube-proxy, konnectivity — not Deployments of myapp"],
                ["Pod", "Smallest run unit. One or more containers, shared netns", "Created by a controller. Naked Pods in prod are pets"],
                ["Deployment", "replicas + selector + pod template. Rolling updates", "Workloads namespace. selector.matchLabels must equal template labels"],
                ["Service", "Stable virtual IP / DNS. Selects Pods by label, not by folklore IP", "ClusterIP for in-cluster. containerPort must match the process"],
                ["kube-system", "Cluster plumbing. CoreDNS answers Service DNS", "kubectl get pods -n kube-system is literacy. Do not kubectl apply your app there"],
            ],
            "widths": [30, 78, 74],
        },
        {
            "title": "Architecture B — decide cluster today: kind vs reading YAML vs AKS",
            "columns": ["Constraint", "Default", "Move when"],
            "rows": [
                ["Need kubectl apply practice", "kind or minikube on the personal PC", "You cannot install a local cluster — still write YAML and trace Service → Pod"],
                ["Need Azure control plane", "Not today. AKS is Day 56 and optional", "You already accepted a destroy date this weekend"],
                ["Image tag", "Pin the ACR digest or Build.BuildId in the manifest", "image: …:latest is a mood, not a deploy"],
                ["Namespace", "workloads (create it). Not default-forever, not kube-system", "default is acceptable only as a 10-minute kind demo"],
                ["Service type", "ClusterIP + port-forward for kind", "LoadBalancer on kind is a sketch; AKS LoadBalancer is a bill"],
            ],
            "widths": [38, 72, 72],
        },
        {
            "title": "Architecture C — pitfalls that schedule nothing and look like Kubernetes is broken",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Label mismatch", "Deployment availableReplicas 0. Service endpoints empty", "template.metadata.labels == spec.selector.matchLabels == Service.selector"],
                ["App in kube-system", "Your crashLoop next to CoreDNS. RBAC horror later", "namespace: workloads. Leave kube-system to the cluster"],
                ["Port mismatch", "Endpoints exist, curl hangs", "containerPort and Service targetPort = listen port"],
                [":latest + imagePullPolicy", "Old bits keep running; you swear you deployed", "Pin tag/digest; set imagePullPolicy IfNotPresent vs Always on purpose"],
                ["No resources", "Fine on kind; HPA later stares at zero requests", "Set requests even on the hello Deployment — Day 59 will need them"],
            ],
            "widths": [38, 72, 72],
        },
    ],
    "one_liner": "Kubernetes is an airport for containers — powerful, expensive, and overkill for a lemonade stand. Learn Pod / Deployment / Service / namespace. Do not land on AKS until the stand needs runways.",
    "lab_intro": "Personal PC. Prefer kind or minikube. Do not create AKS today. Personal repo k8s/ manifests.",
    "lab": [
        "Write k8s/namespace.yaml (workloads), k8s/deployment.yaml, k8s/service.yaml for the sample app. Image from ACR with a pinned tag, not latest. replicas: 1. resources.requests set (cpu 50m, memory 64Mi).",
        "Confirm labels: Deployment selector, pod template, Service selector are identical (app: myapp). Confirm containerPort matches the process.",
        "If kind/minikube exists: kubectl apply -f k8s/ && kubectl -n workloads get deploy,po,svc,ep. kubectl -n kube-system get po — look, do not apply the app there.",
        "If no local cluster: still write the YAML. Trace a request: Service ClusterIP → endpoints → Pod IP:containerPort. That tracing is the lab.",
        "kubectl explain deployment.spec.template.spec.containers  (or read the YAML) until you can say why a naked Pod is the wrong object.",
        "Write docs/k8s-day55.md: the three objects, why kube-system is off-limits for myapp, and that AKS is optional tomorrow with a destroy date.",
    ],
    "code_title": "Starter manifests — workloads namespace, not kube-system",
    "code": "apiVersion: v1\nkind: Namespace\nmetadata: { name: workloads }\n---\napiVersion: apps/v1\nkind: Deployment\nmetadata: { name: myapp, namespace: workloads }\nspec:\n  replicas: 1\n  selector: { matchLabels: { app: myapp } }\n  template:\n    metadata: { labels: { app: myapp } }\n    spec:\n      containers:\n      - name: myapp\n        image: <acr>.azurecr.io/myapp:day53\n        ports: [{ containerPort: 3000 }]\n        resources:\n          requests: { cpu: 50m, memory: 64Mi }\n---\napiVersion: v1\nkind: Service\nmetadata: { name: myapp, namespace: workloads }\nspec:\n  selector: { app: myapp }\n  ports: [{ port: 80, targetPort: 3000 }]\n  type: ClusterIP\n",
    "checklist": [
        "Can map Service → endpoints → Pod without calling the Pod 'the Deployment'",
        "Manifests target namespace workloads, not kube-system",
        "Labels agree; port agrees; image tag is pinned",
        "Applied on kind/minikube OR traced on paper — AKS not created today",
    ],
    "tomorrow": "AKS setup — optional gym membership with a cancel date",
}

SPECS[56] = {
    "topic": "AKS Setup",
    "subtitle": "A one-node cluster is still a control plane plus a VM bill — create only with a destroy date",
    "phase": "6 - Containers & Kubernetes",
    "tables": [
        {
            "title": "Architecture A — control plane, node pools, kube-system vs your pool",
            "columns": ["Piece", "What Azure runs", "What you must not confuse"],
            "rows": [
                ["Control plane", "Managed API server, etcd, scheduler. You pay the AKS SKU relationship", "A VM you SSH to 'the master'. You do not"],
                ["System node pool", "First pool, mode=System. kube-system DaemonSets/pods (CoreDNS, CoreDNS-autoscaler, CSI)", "A place to schedule myapp 'because there is only one node'"],
                ["User node pool", "mode=User. Where Deployments for workloads should land (taints/labels in real designs)", "Optional on a 1-node lab — still know the mode exists"],
                ["Network plugin", "kubenet (pod CIDR + NAT) vs Azure CNI (pod VNet IPs) vs Azure CNI Overlay (recommended IP conservation)", "Rebuilding the cluster three times to 'compare' as a personality trait"],
                ["Identity", "kubelet uses managed identity (kubelet_identity) for ACR AcrPull", "imagePullSecrets with ACR admin as the default"],
            ],
            "widths": [32, 82, 68],
        },
        {
            "title": "Architecture B — create, skip, or Container Apps",
            "columns": ["Constraint", "Default", "Create AKS only when"],
            "rows": [
                ["Cost / attention", "Skip AKS. Use kind + ACI/Container Apps path", "You can name this weekend's az aks delete date before create returns"],
                ["Need kube API in Azure", "Smallest: --node-count 1, cheap VM size, Overlay CNI", "Production wants 3 system nodes. This is a lab, not that"],
                ["Network plugin", "Azure CNI Overlay for a modern default", "You can explain kubenet IP vs CNI subnet exhaustion in one sentence"],
                ["SSH keys", "--generate-ssh-keys is fine", "Do not copy those keys into the Git repo"],
                ["Skip is engineering", "Write why in docs — Container Apps / ACI", "Skipping is cheaper than a forgotten node in November"],
            ],
            "widths": [36, 72, 74],
        },
        {
            "title": "Architecture C — pitfalls that keep billing after the weekend demo",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["No destroy date", "'Lab cluster' still in Cost Analysis next quarter", "Calendar before create. az aks delete --yes --no-wait"],
                ["Apps in kube-system", "CrashLoop next to CoreDNS; later NetworkPolicy stories", "namespace workloads; system pool is plumbing"],
                ["Default NSG folklore", "Cannot pull ACR / cannot hit API", "Attach AcrPull to kubelet identity; az aks get-credentials --overwrite-existing"],
                ["Standard_D8 'because lab'", "Bill is the lesson, not kubectl", "Standard_B2s or the cheapest region SKU that AKS accepts"],
                ["Leave node-count 1 as architecture advice", "Resume-ready cluster that is not HA", "Lab only. Notes must say system pool min=3 in real life"],
            ],
            "widths": [42, 70, 70],
        },
    ],
    "one_liner": "AKS is a gym membership for orchestration — easy to start, painful if you forget to cancel. If you cannot name the destroy date, do not create the cluster.",
    "lab_intro": "Personal subscription. Optional cluster. If you create aks-lab, destroy is scheduled the same weekend. No employer cluster kubeconfig.",
    "lab": [
        "Read AKS node pools and kubenet vs Azure CNI vs Azure CNI Overlay at a survey level. Write one sentence each. Do not rebuild three clusters to feel thorough.",
        "Decide: create smallest AKS, or skip to Container Apps/ACI and write why. If you cannot put destroy on this weekend's calendar, you skip.",
        "If creating: az group create rg-day56; az aks create with --node-count 1, a small VM size, --network-plugin azure --network-plugin-mode overlay, --generate-ssh-keys. Then az aks nodepool list and note mode=System.",
        "az aks get-credentials -g rg-day56 -n aks-lab --overwrite-existing. kubectl get nodes. kubectl get pods -n kube-system. Do not apply myapp into kube-system.",
        "Grant the kubelet identity AcrPull on the lab ACR if you will deploy tomorrow (az aks show --query identityProfile.kubeletidentity.objectId).",
        "Write docs/aks-day56.md: created or skipped, destroy date or skip reason, system vs user pool, kube-system vs workloads. If created, put az aks delete in the doc as a copy-paste.",
    ],
    "code_title": "Starter CLI — smallest cluster, Overlay CNI, delete is documented",
    "code": "# Cost warning: AKS is not a daily-delete toy. Calendar destroy first.\naz aks create -g rg-day56 -n aks-lab \\\n  --node-count 1 --node-vm-size Standard_B2s \\\n  --network-plugin azure --network-plugin-mode overlay \\\n  --generate-ssh-keys --enable-managed-identity\naz aks nodepool list -g rg-day56 --cluster-name aks-lab -o table\naz aks get-credentials -g rg-day56 -n aks-lab --overwrite-existing\nkubectl get nodes -o wide\nkubectl get pods -n kube-system\n# Destroy (same weekend):\n# az aks delete -g rg-day56 -n aks-lab --yes --no-wait\n",
    "checklist": [
        "Either a one-node lab cluster with a written destroy date, or a written skip to ACI/Container Apps",
        "Can explain system node pool vs user pool and why myapp is not kube-system",
        "Can explain Overlay vs kubenet vs CNI in one sentence each",
        "docs/aks-day56.md exists; no SSH keys in Git",
    ],
    "tomorrow": "Deploy to AKS from a pipeline (or the same manifests against kind)",
}

SPECS[57] = {
    "topic": "Deploying to AKS via Pipelines",
    "subtitle": "CD to Kubernetes without Git is sticky-note kubectl wearing a hoodie",
    "phase": "6 - Containers & Kubernetes",
    "tables": [
        {
            "title": "Architecture A — laptop kubectl vs KubernetesManifest@1 (same YAML, different source of truth)",
            "columns": ["Dimension", "kubectl apply from PC", "Pipeline deploy"],
            "rows": [
                ["Source", "Whatever is on disk, maybe uncommitted", "k8s/*.yml (or baked Helm) on the commit being built"],
                ["Identity", "Your user kubeconfig. Easy to be cluster-admin", "Azure RM / Kubernetes service connection. Scope it; Day 63/69 will be rude"],
                ["Image", "Easy to leave :latest", "KubernetesManifest@1 containers: input substitutes Build.BuildId"],
                ["Namespace", "You remember -n, or you don't", "inputs.namespace: workloads — never kube-system"],
                ["No AKS", "kind apply is still Git if the files are committed", "Same YAML, local kubeconfig job or skip Azure target honestly"],
            ],
            "widths": [28, 74, 80],
        },
        {
            "title": "Architecture B — decide GitOps later vs push-from-pipeline today",
            "columns": ["Constraint", "Default today", "Change when"],
            "rows": [
                ["Process", "Push CD: pipeline applies manifests from Git", "Flux/Argo (pull GitOps) is a later day — do not fake it with a blog title"],
                ["Cluster missing", "Apply the same files to kind; keep them in Git", "Creating AKS today without a destroy date — still no"],
                ["Tag move", "Substitute image to <acr>/myapp:$(Build.BuildId)", "Manifest frozen on latest is not a deploy of this build"],
                ["RBAC", "Connection can deploy to namespace workloads", "cluster-admin service connection as a lab convenience is a finding"],
                ["Helm", "Manifests today; Helm upgrade is Day 58", "Do not copy three environment folders of YAML this afternoon"],
            ],
            "widths": [32, 76, 74],
        },
        {
            "title": "Architecture C — pitfalls that apply Friday's cluster with Thursday's Git",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Sticky-note apply", "Three people, three tags, one cluster", "Pipeline is the only apply to that cluster"],
                ["Wrong namespace", "Pods in default; Service in workloads; empty endpoints", "namespace: workloads on every object and on the task"],
                ["Image not substituted", "Old digest still running", "containers: input or a bake step; kubectl set image is not the process"],
                ["kube-system deploy", "Task namespace left default/system", "Fail the review. Plumbing namespace is not an app target"],
                ["cluster-admin forever", "Service connection can delete the cluster", "Namespace-scoped Role later; today at least not Owner on the subscription"],
            ],
            "widths": [38, 72, 72],
        },
    ],
    "one_liner": "If Git does not know the cluster state you intended, you do not have CD. You have a memory. Hoodies are not a release strategy.",
    "lab_intro": "Personal Azure DevOps project azure-100-labs. Target AKS if it exists with a destroy date, otherwise kind. Manifests in Git.",
    "lab": [
        "Commit k8s/*.yml from Day 55 (namespace workloads). Confirm no image: …:latest as the only tag — use a placeholder the task will replace, or the Build.BuildId you already pushed.",
        "If AKS exists: Project Settings → Service connections → Azure Resource Manager (or Kubernetes) to the personal cluster. Note the role. Not cluster-admin if you can avoid it.",
        "Add a pipeline job after Docker@2 (or a second pipeline) with KubernetesManifest@1 action: deploy, namespace workloads, manifests k8s/*.yml, containers: <acr>.azurecr.io/myapp:$(Build.BuildId).",
        "Run it. kubectl -n workloads get deploy,po,svc and kubectl -n workloads describe po | find the image. The running tag must be this Build.BuildId.",
        "If no AKS: kubectl apply -f k8s/ against kind from the same files, and still keep a YAML pipeline that would deploy — identity is the only missing piece. Do not treat laptop kubectl as the production process.",
        "Write docs/aks-deploy-day57.md: connection name, namespace, image tag that actually ran. Helm is tomorrow for values; do not fork the YAML per mood.",
    ],
    "code_title": "Starter YAML — KubernetesManifest@1 substitutes the image",
    "code": "- task: KubernetesManifest@1\n  displayName: Deploy to workloads (not kube-system)\n  inputs:\n    action: deploy\n    connectionType: Azure Resource Manager\n    azureSubscriptionConnection: aks-connection\n    azureResourceGroup: rg-day56\n    kubernetesCluster: aks-lab\n    namespace: workloads\n    manifests: k8s/*.yml\n    containers: |\n      <uniqueacr>.azurecr.io/myapp:$(Build.BuildId)\n",
    "checklist": [
        "Manifests in Git are the source; namespace is workloads",
        "Running image tag equals this build (or kind apply of the same files)",
        "Did not kubectl apply from a dirty laptop as the CD story",
        "Service connection noted; not treated as cluster-admin folklore",
    ],
    "tomorrow": "Helm charts — values.yaml instead of YAML-mountain copy-paste",
}

SPECS[58] = {
    "topic": "Helm Charts Basics",
    "subtitle": "A release is a named install of a chart — values.yaml is where environments stop being copy-paste crimes",
    "phase": "6 - Containers & Kubernetes",
    "tables": [
        {
            "title": "Architecture A — chart vs release vs revision (three different nouns)",
            "columns": ["Noun", "What it is", "Command that proves it"],
            "rows": [
                ["Chart", "Package: Chart.yaml + templates/ + values.yaml. Not running", "helm create charts/myapp ; helm template"],
                ["Release", "Named instance of a chart in a namespace (myapp in workloads)", "helm list -n workloads"],
                ["Revision", "Each upgrade increments. Rollback is a revision, not a vibe", "helm history myapp -n workloads"],
                ["values.yaml", "Default knobs: image.repository, image.tag, replicaCount", "helm upgrade --install … --set image.tag=…"],
                ["templates/", "Go templates → Kubernetes YAML. Render before you trust it", "helm template myapp charts/myapp --set image.tag=demo"],
            ],
            "widths": [28, 80, 74],
        },
        {
            "title": "Architecture B — one chart, many values files (not charts-dev vs charts-prod)",
            "columns": ["Constraint", "Default", "Change when"],
            "rows": [
                ["Env differences", "values-dev.yaml / values-lab.yaml overlays", "Copying the whole chart per environment — that is the crime"],
                ["Image tag", "--set image.tag=$(Build.BuildId) from CI", "Hardcoded latest in deployment.yaml template"],
                ["Install vs upgrade", "helm upgrade --install (one thought)", "helm install that fails the second time because the release exists"],
                ["No cluster", "helm template and read the Deployment it produced", "Skipping render because 'the chart looks fine'"],
                ["Uninstall", "helm uninstall myapp -n workloads once in the lab", "Abandoned releases as unnamed pets"],
            ],
            "widths": [32, 74, 76],
        },
        {
            "title": "Architecture C — pitfalls that ship the sample nginx and call it myapp",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Sample chart untreated", "Default nginx image, probes for a different app", "helm create is a tour. Delete what is not yours"],
                ["Tag in the template", "CI --set ignored because template does not use .Values.image.tag", "templates/deployment.yaml must reference Values"],
                ["Release vs chart mix-up", "helm list empty; charts/ folder full", "list shows releases. Package is not an install"],
                ["kube-system release", "helm upgrade --install -n kube-system", " -n workloads --create-namespace"],
                ["Three chart forks", "prod missed a securityContext for six months", "One chart; values files; reviews on values-prod.yaml"],
            ],
            "widths": [36, 74, 72],
        },
    ],
    "one_liner": "Helm is templating for YAML mountains — values.yaml is where environments stop being copy-paste crimes. A chart is a package; a release is what is running.",
    "lab_intro": "Personal repo charts/myapp. Cluster = AKS (if alive) or kind. Render is mandatory even with no cluster.",
    "lab": [
        "helm create charts/myapp. Open Chart.yaml, values.yaml, templates/deployment.yaml. Note image.repository / image.tag. Strip sample nginx assumptions you will not run.",
        "Point values at <acr>.azurecr.io/myapp. Do not hardcode latest in the template — it must be .Values.image.tag.",
        "helm template myapp charts/myapp --set image.tag=day58 --namespace workloads | less  — confirm Deployment image and namespace. This step counts if you have no cluster.",
        "If a cluster exists: helm upgrade --install myapp charts/myapp -n workloads --create-namespace --set image.tag=<Build.BuildId> --wait. helm list / helm history.",
        "Upgrade the tag once more. Confirm revision incremented. Then helm uninstall myapp -n workloads once so you know the opposite of install.",
        "Write docs/helm-day58.md: chart vs release vs revision in one line each, and the rendered image line. Optional pipeline: HelmDeploy@1 or a script step with the same upgrade --install.",
    ],
    "code_title": "Starter commands — render, then upgrade --install",
    "code": "helm create charts/myapp\nhelm template myapp charts/myapp \\\n  --namespace workloads \\\n  --set image.repository=<uniqueacr>.azurecr.io/myapp \\\n  --set image.tag=$(Build.BuildId)\nhelm upgrade --install myapp charts/myapp \\\n  --namespace workloads --create-namespace \\\n  --set image.repository=<uniqueacr>.azurecr.io/myapp \\\n  --set image.tag=$(Build.BuildId) --wait\nhelm list -n workloads\nhelm history myapp -n workloads\nhelm uninstall myapp -n workloads\n",
    "checklist": [
        "Can distinguish chart, release, and revision out loud",
        "image.tag comes from values/--set, not a hardcoded latest in the template",
        "helm template ran; install/upgrade/uninstall once if a cluster exists",
        "Release namespace is workloads, not kube-system",
    ],
    "tomorrow": "AKS scaling, monitoring, networking — HPA needs requests, not superstition",
}

SPECS[59] = {
    "topic": "AKS Scaling, Monitoring & Networking",
    "subtitle": "HPA scales pods; cluster autoscaler scales nodes; neither works without a metric",
    "phase": "6 - Containers & Kubernetes",
    "tables": [
        {
            "title": "Architecture A — four levers that are not the same YAML object",
            "columns": ["Lever", "What it changes", "Requires"],
            "rows": [
                ["Fixed replicas", "Deployment.spec.replicas", "Honesty that load is flat. Fine for a lemonade stand"],
                ["HPA", "Pod replica count from a metric (CPU 70%, 1–5)", "resources.requests.cpu on the container. metrics-server in kube-system"],
                ["Cluster autoscaler", "Node count when pods are Pending for capacity", "Autoscaler add-on + a node pool that can scale. Not a substitute for HPA"],
                ["Ingress", "HTTP entry (ingress controller + Ingress object)", "A controller (nginx/AGIC/etc). Not a Service type folklore"],
                ["NetworkPolicy", "Who may speak to whom in the CNI", "A plugin that enforces (Azure Network Policy / Calico). Default-allow if none"],
            ],
            "widths": [36, 72, 74],
        },
        {
            "title": "Architecture B — pick HPA vs more replicas vs more nodes",
            "columns": ["Symptom", "Wrong lever", "Right lever"],
            "rows": [
                ["App CPU high, nodes fine", "Add nodes 'because AKS'", "HPA (or fixed replicas) after requests exist"],
                ["Pods Pending: Insufficient cpu", "HPA maxReplicas++ on a packed node", "Cluster autoscaler / larger node / fewer requests"],
                ["Feels slow, no metrics", "HPA at 70% with requests: 0", "Set requests; look at Azure Monitor Container Insights or kubectl top"],
                ["Need HTTP routing", "LoadBalancer per Service as architecture", "Ingress survey; skip a CNI PhD if time-boxed"],
                ["Lemonade stand", "Copy a 12-object 'prod network' tutorial", "Fixed 1 replica. Write why HPA is jewelry today"],
            ],
            "widths": [40, 70, 72],
        },
        {
            "title": "Architecture C — pitfalls that encode superstition in YAML",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["HPA without requests", "CPU utilization 0% or unknown; no scale", "resources.requests.cpu on the Deployment"],
                ["HPA vs CA confusion", "Pending pods; HPA already at max", "Name the bottleneck: pod vs node"],
                ["Ingress without controller", "Ingress object exists; Address empty", "Install/identify a controller first — or skip and write it"],
                ["NetworkPolicy on default-deny by paste", "Broke kube-system DNS / lost the app", "Do not apply a random deny-all to kube-system. Survey only if time-boxed"],
                ["Forgotten cluster", "Day 56 gym membership still billing", "Re-check destroy date. Monitoring does not pay the VM"],
            ],
            "widths": [40, 71, 71],
        },
    ],
    "one_liner": "Autoscaling without metrics is superstition with YAML. If you cannot name the signal, do not autoscale. HPA is pods; cluster autoscaler is nodes.",
    "lab_intro": "Survey day. Personal notes over a CNI lab. If aks-lab still exists, the weekend destroy date is part of today's work.",
    "lab": [
        "Read HorizontalPodAutoscaler v2 and cluster autoscaler docs enough to write: HPA changes replicas; CA changes nodes; both need a signal.",
        "Open your Deployment: confirm resources.requests.cpu exists (Day 55). If not, add 50m. Write why HPA is undefined without it.",
        "Write docs/scale-day59.md with a table: when fixed replicas vs HPA vs CA. Include one sentence on Ingress vs LoadBalancer and one on NetworkPolicy default-allow.",
        "Optional: apply the HPA sketch to kind/AKS and kubectl get hpa. Do not load-test a paid cluster just to see a replica flicker.",
        "Skip deep CNI / AGIC labs if the clock says so — write what you skipped. Do not paste a default-deny NetworkPolicy into kube-system.",
        "If AKS from Day 56 exists, confirm the destroy date is still on the calendar (or delete now). Container Insights is literacy, not a requirement to leave the cluster up.",
    ],
    "code_title": "Starter HPA — CPU 70% between 1 and 5, requests required",
    "code": "apiVersion: autoscaling/v2\nkind: HorizontalPodAutoscaler\nmetadata:\n  name: myapp\n  namespace: workloads\nspec:\n  scaleTargetRef:\n    apiVersion: apps/v1\n    kind: Deployment\n    name: myapp\n  minReplicas: 1\n  maxReplicas: 5\n  metrics:\n  - type: Resource\n    resource:\n      name: cpu\n      target:\n        type: Utilization\n        averageUtilization: 70\n# Cluster autoscaler is a node-pool / add-on setting, not this object.\n",
    "checklist": [
        "Can separate HPA (pods) from cluster autoscaler (nodes) without mixing YAML objects",
        "Wrote when fixed replicas beat HPA for this app",
        "Know HPA needs resource requests and a metrics signal",
        "AKS destroy date re-checked or skip path still honest",
    ],
    "tomorrow": "Phase 6 mini project — one image in ACR, one automated run path",
}

SPECS[60] = {
    "topic": "Mini Project + Recap (Phase 6)",
    "subtitle": "Package once, run on one path you can pay for and tear down — slogans do not get invoices",
    "phase": "6 - Containers & Kubernetes",
    "tables": [
        {
            "title": "Architecture A — Phase 6 map (one artifact, one path)",
            "columns": ["Stage", "Object", "Done looks like"],
            "rows": [
                ["Pack", "Dockerfile + layer cache + digest", "Image builds locally and in CI"],
                ["Store", "ACR repository, tag = Build.BuildId", "Not Hub; not latest-as-identity"],
                ["Publish", "Docker@2 on ubuntu-latest", "Laptop is not the publisher"],
                ["Run (pick one)", "ACI or Container Apps or AKS+Helm/manifests", "Pipeline applied it; Git knows the tag"],
                ["Stop", "Delete ACI group / CA app / AKS", "Cost Analysis does not include a forgotten gym"],
            ],
            "widths": [28, 72, 82],
        },
        {
            "title": "Architecture B — pick one runtime, not a buffet",
            "columns": ["Constraint", "Pick", "Do not"],
            "rows": [
                ["Need a URL, no kube API", "ACI or Container Apps", "Stand up AKS 'so the recap looks senior'"],
                ["Need kube + Helm", "AKS with destroy date + helm upgrade --install", "Three half-paths (ACI + CA + AKS) all 'almost'"],
                ["Cost already bites", "kind + ACR proof + skip Azure runtime", "Leave node-count 1 because tomorrow-you might need it"],
                ["Tag", "Build.BuildId everywhere", "Promote by latest in the recap diagram"],
                ["Namespace", "workloads", "Anything in kube-system in the architecture one-liner"],
            ],
            "widths": [36, 74, 72],
        },
        {
            "title": "Architecture C — leftovers that still bill after a proud recap post",
            "columns": ["Leftover", "What you see", "Fix"],
            "rows": [
                ["ACI group", "dns-name-label still resolves, meter runs", "az container delete"],
                ["aks-lab", "System pool VM in Cost Analysis", "az aks delete — the date from Day 56"],
                ["Public IP / NSG orphans", "RG not empty after cluster delete", "az group delete rg-day56 if it was lab-only"],
                ["ACR junk tags", "Untagged manifests", "Delete what the mini project does not need"],
                ["Kubeconfig clutter", "kubectl still points at a dead cluster", "kubectl config delete-context"],
            ],
            "widths": [36, 72, 74],
        },
    ],
    "one_liner": "Phase 6 recap: package once, run anywhere — but 'anywhere' still has a bill. Done = image in ACR + one successful automated deploy path.",
    "lab_intro": "Personal subscription and azure-100-labs. One path only. Recap one-liner goes in docs/phase6-recap.md.",
    "lab": [
        "Confirm the pipeline still builds and pushes myapp:$(Build.BuildId) to ACR. Copy the digest into the recap doc.",
        "Choose one run path: ACI, Container Apps, or AKS (manifests or Helm). Automate it from the pipeline or a documented CLI that uses the build tag. Not three paths.",
        "Prove the running bits equal that digest/tag. If you skipped Azure runtime, prove kind ran the same tag and say so — skipping AKS is an architecture decision.",
        "Tear down the run path: delete ACI/CA/AKS leftovers from Days 54–59. Empty RGs or document why ACR stays for Phase 7.",
        "Write docs/phase6-recap.md: architecture one-liner, the path you picked, destroy receipts, kube-system vs workloads in one sentence.",
        "LinkedIn recap from the personal account. No employer cluster diagrams. No buffet of half-finished runtimes.",
    ],
    "code_title": "Definition of done — one publisher, one tag, one path",
    "code": "# Mini project receipt (fill real names)\n# ACR:  <uniqueacr>.azurecr.io/myapp:<Build.BuildId>  digest sha256:…\n# Path: aci | container-apps | aks-helm | kind-only\n# Apply: pipeline Docker@2 + (KubernetesManifest@1 | helm upgrade --install | az container create)\n# Stop:  az container delete | az aks delete | az containerapp delete\n# Rule:  workloads namespace, never kube-system; latest is not the promotion ID\n",
    "checklist": [
        "Image in ACR tagged with a build id, digest recorded",
        "Exactly one automated deploy path proved",
        "Paid runtimes from this phase deleted or dated",
        "docs/phase6-recap.md has the architecture one-liner",
    ],
    "tomorrow": "Entra ID fundamentals — the bouncer list every other control assumes",
}

SPECS[61] = {
    "topic": "Azure AD (Entra ID) Fundamentals",
    "subtitle": "If the bouncer list is wrong, RBAC and Key Vault are cosplay",
    "phase": "7 - Security, Compliance & Governance",
    "tables": [
        {
            "title": "Architecture A — tenant, user, app registration, service principal (four different objects)",
            "columns": ["Object", "What it is", "Not the same as"],
            "rows": [
                ["Tenant / directory", "The Entra boundary. Personal vs work — labs stay personal", "A subscription. A sub lives in a tenant; they are not synonyms"],
                ["User / group", "Human identities. Groups are how assignments should scale", "An app registration. Apps are not users with a funny name"],
                ["App registration", "Application object. Client ID (appId). Lives in the home tenant", "An Azure DevOps service connection (Day 63). That is an ADO badge that may use this app"],
                ["Service principal", "The instance of that app in a tenant (enterprise app). What RBAC is assigned to", "The client secret. Secret is a credential on the app, not the SP itself"],
                ["Client ID vs secret", "ID is public-ish. Secret is a password. Cert/WIF later", "Pasting a secret into YAML 'just for the lab'"],
            ],
            "widths": [34, 78, 70],
        },
        {
            "title": "Architecture B — what to register today vs what to wait for",
            "columns": ["Need", "Default today", "Wait"],
            "rows": [
                ["An app identity to look at", "Portal: Entra ID → App registrations → New → day61-lab. Note appId", "Client secret. Key Vault is Day 64; pipeline fetch is Day 65"],
                ["Redirect URI", "Skip for this lab (no user-login app)", "Pretending every registration needs localhost redirect"],
                ["Which tenant", "Personal tenant only", "Work tenant 'because that's where Azure is' — that is how labs leak"],
                ["Who is Owner on the app", "You. Not a random group from an employer directory", "Subscription Owner on the app — that is Day 62's flamethrower"],
                ["Federation", "Know WIF exists (Day 63)", "az ad app credential reset this afternoon"],
            ],
            "widths": [32, 78, 72],
        },
        {
            "title": "Architecture C — pitfalls that look like RBAC bugs and are actually the wrong directory",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Wrong tenant", "App not listed; CLI talks to work directory", "az account show / portal directory switch. Labs = personal"],
                ["Secret in a screenshot", "Client secret on LinkedIn or in git", "Do not create a secret today. Note the appId only"],
                ["Calling the app a user", "Trying to 'login as the registration'", "Users sign in; apps get tokens. Different objects"],
                ["App vs service connection mash-up", "One Portal blade expected to be the pipeline", "Registration is Entra. Connection is Azure DevOps. Day 63 wires them"],
                ["Work tenant screenshot", "Employer directory in the handout photo", "Personal tenant. Crop nothing from work"],
            ],
            "widths": [40, 71, 71],
        },
    ],
    "one_liner": "Entra ID is the bouncer list for Azure — if identity is wrong, every other control is cosplay. App registration is not a service connection, and a client ID is not a secret.",
    "lab_intro": "Personal Entra tenant only. Do not open an employer directory. Project azure-100-labs is later this week for connections.",
    "lab": [
        "Portal → Microsoft Entra ID (personal directory). Note tenant ID. az account show --query tenantId. If it is a work tenant, stop and switch.",
        "Entra ID → App registrations → New registration → name day61-lab. Supported account types: this org only. Redirect URI: skip. Register.",
        "Copy Application (client) ID and Directory (tenant) ID into docs/entra-day61.md. Not into azure-pipelines.yml.",
        "Open Certificates & secrets. Do not create a client secret today. Read that secrets would live here, and that Day 63 prefers federated credentials instead.",
        "Enterprise applications: find day61-lab — that object is the service principal. One sentence in the doc: registration vs SP vs (later) service connection.",
        "No LinkedIn screenshot of secrets, tenant gossip, or work users. Optional CLI: az ad app create --display-name day61-lab --query appId -o tsv.",
    ],
    "code_title": "Starter CLI — register, note appId, no secret",
    "code": "# Personal tenant only. Confirm first:\naz account show --query \"{sub:id, tenant:tenantId, user:user.name}\" -o json\nAPP_ID=$(az ad app create --display-name day61-lab --query appId -o tsv)\naz ad sp create --id $APP_ID --query id -o tsv\necho \"Client ID (appId)=$APP_ID\"\n# Do NOT: az ad app credential reset  — secret waits; WIF is Day 63\n",
    "checklist": [
        "day61-lab exists in the personal tenant; tenant ID and appId recorded",
        "Can explain tenant vs user vs app registration vs service principal",
        "No client secret created; none in Git",
        "Knows a service connection is an Azure DevOps object (Day 63), not this blade",
    ],
    "tomorrow": "RBAC deep dive — Owner is a flamethrower; scope is the verb",
}

SPECS[62] = {
    "topic": "RBAC Deep Dive",
    "subtitle": "Role + assignee + scope — Owner at subscription is blast radius, not speed",
    "phase": "7 - Security, Compliance & Governance",
    "tables": [
        {
            "title": "Architecture A — built-in roles at RG scope (same assignee, different blast)",
            "columns": ["Role", "Can", "Cannot"],
            "rows": [
                ["Reader", "List/read resources in scope", "PUT/PATCH/DELETE; cannot grant roles"],
                ["Contributor", "Create/change/delete resources in scope", "Grant roles (not Owner). Cannot always do data-plane secrets without extra roles"],
                ["Owner", "Contributor plus assign roles. The flamethrower", "Escape the tenant. Still not 'God' over another directory"],
                ["User Access Administrator", "Assign roles only", "A substitute for Contributor. Different job"],
                ["Custom role", "Actions[] you list. Last mile when built-ins are too wide/narrow", "A lab toy for a Reader test"],
            ],
            "widths": [42, 72, 68],
        },
        {
            "title": "Architecture B — decide scope before you pick a friendly role name",
            "columns": ["Constraint", "Default", "Reject"],
            "rows": [
                ["Lab pipeline / human", "Contributor or Reader on one RG", "Owner on the subscription 'so we are not blocked'"],
                ["Look but not touch", "Reader on rg-day62", "Contributor because the Portal was easier"],
                ["Grant roles", "Owner or User Access Admin at the smallest scope that works", "Subscription Owner for a hello assignment"],
                ["Custom role", "Skip today", "Inventing Microsoft.Authorization/roleDefinitions for fun"],
                ["Data plane", "Key Vault data-plane roles are extra (Day 64 Secrets User)", "Assuming Contributor reads KV secrets — it does not under RBAC vaults"],
            ],
            "widths": [32, 76, 74],
        },
        {
            "title": "Architecture C — pitfalls that turn 'just Owner' into a delete that went wide",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Subscription Owner for a pipeline", "SPN can grant itself more and delete the sub's RGs", "RG-scoped Contributor; no role-assignment permission"],
                ["Wrong assignee", "Assignment on a user you are not; or on the app object vs SP", "Assign to the service principal object ID / UPN you intend"],
                ["Scope typo", "Role assigned, Portal still denies", "scope must be the RG/resource ID, not a display name"],
                ["Classic admins folklore", "Co-admin from ASM era still lurking", "Literacy: prefer Azure RBAC. Do not add classic admins"],
                ["Leaving the test assignment", "Reader leftover you forget", "az role assignment delete when the proof is done (or keep Reader on a dedicated lab RG)"],
            ],
            "widths": [42, 70, 70],
        },
    ],
    "one_liner": "Owner is a flamethrower; prefer Reader/Contributor scoped to the resource group, not the subscription. Scope is the verb people skip.",
    "lab_intro": "Personal subscription. rg-day62. Assign to your user UPN, not an employer group. Azure CLI on the personal machine.",
    "lab": [
        "az group create -n rg-day62 -l eastus. Write the resource ID: /subscriptions/<sub>/resourceGroups/rg-day62.",
        "az role assignment create --assignee <your-upn> --role Reader --scope that RG ID. az role assignment list --scope … -o table.",
        "Compare in notes: Reader vs Contributor vs Owner in one paragraph you could say out loud. Do not assign yourself Owner on the subscription to 'feel the difference'.",
        "Optional proof: with only Reader, a write should fail (or reason about it if you also have higher roles inherited from the subscription — then say so honestly).",
        "Note: Contributor does not grant Key Vault Secrets User on an RBAC vault. That surprise is Day 64.",
        "Remove the extra assignment if it is noise, or keep Reader on rg-day62 as the muscle memory. Write docs/rbac-day62.md. No work-tenant screenshots.",
    ],
    "code_title": "Starter CLI — Reader on one RG, not Owner on the sub",
    "code": "az group create -n rg-day62 -l eastus\nSUB=$(az account show --query id -o tsv)\nSCOPE=/subscriptions/$SUB/resourceGroups/rg-day62\naz role assignment create --assignee <your-upn> --role Reader --scope $SCOPE\naz role assignment list --scope $SCOPE -o table\n# Contributor = change resources, not grant roles\n# Owner = includes Microsoft.Authorization/roleAssignments/write  (flamethrower)\n",
    "checklist": [
        "Can recite role + assignee + scope as the triple",
        "Reader assignment on a lab RG exists or existed with a CLI receipt",
        "Will not recommend subscription Owner for a pipeline",
        "Knows Contributor ≠ Key Vault secret read on RBAC vaults",
    ],
    "tomorrow": "Service connections and service principals — robot badges, not master keys",
}

SPECS[63] = {
    "topic": "Service Connections & Service Principals",
    "subtitle": "The Entra app is the identity; the Azure DevOps service connection is the badge that uses it",
    "phase": "7 - Security, Compliance & Governance",
    "tables": [
        {
            "title": "Architecture A — three objects people mash into one name",
            "columns": ["Object", "Where it lives", "Job"],
            "rows": [
                ["App registration", "Entra (Day 61). Client ID", "Application identity. May hold federated credentials or a secret"],
                ["Service principal", "Entra enterprise app in the tenant", "What Azure RBAC is assigned to (Contributor on one RG)"],
                ["Service connection", "Azure DevOps Project Settings", "How a pipeline job gets a token to call Azure. Not an Entra blade"],
                ["Client secret auth", "Password on the app. Stored by ADO", "Long-lived. Expires at 2am. Postcard with a delayed explosion"],
                ["Workload identity federation", "Federated credential on the app: issuer vstoken.dev.azure.com, subject sc://org/project/name", "ADO presents a token; Entra trusts it. No secret in a drawer"],
            ],
            "widths": [40, 62, 80],
        },
        {
            "title": "Architecture B — WIF first, then least privilege",
            "columns": ["Constraint", "Default", "Reject"],
            "rows": [
                ["Auth mode", "Azure RM service connection + Workload identity federation", "Automatic wizard that creates subscription Owner + client secret"],
                ["Scope", "Contributor on rg-day63 (or the lab RG that pipeline deploys)", "Owner on the subscription so ARM never fails"],
                ["Automatic vs manual", "Automatic is fine if you immediately inspect the SP roles", "Never looking at what the wizard granted"],
                ["One connection", "lab-sc for lab RG. Prod later gets a different connection (Day 69)", "A single connection named azure that can see every RG"],
                ["Day 61 app", "You may reuse day61-lab and add a federated credential", "Creating a secret on day61-lab because the UI offered it"],
            ],
            "widths": [32, 80, 70],
        },
        {
            "title": "Architecture C — pitfalls that mint master keys named 'Azure Resource Manager'",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Owner SPN", "Role assignments on the subscription for the new app", "Delete Owner; assign Contributor (or less) on one RG"],
                ["Secret-based connection", "Expiry date; password rotation theatre", "Recreate as WIF. Federated credentials, not client secrets"],
                ["Confusing connection with registration", "Cannot find the connection in Entra", "ADO project settings. Entra has the app/SP only"],
                ["Subject mismatch", "WIF token rejected (AADSTS / federated identity error)", "Subject sc://<org>/<project>/<connection> must match the federated credential"],
                ["User PAT in a script", "az login with a human, then hope", "Jobs use the service connection. Humans use their user"],
            ],
            "widths": [40, 71, 71],
        },
    ],
    "one_liner": "Service principals are robot employees — give them a badge scoped to one floor, not master keys. The service connection is the badge; the Entra app is the employee file.",
    "lab_intro": "Personal Azure DevOps org, project azure-100-labs. Personal tenant. Prefer workload identity federation.",
    "lab": [
        "Project Settings → Service connections → New → Azure Resource Manager. Choose Workload identity federation (automatic is OK). Name lab-sc. Subscription = personal.",
        "Open the connection → Manage Service Principal (or Entra). Note appId. This is the registration/SP. The connection object stays in ADO — two places, not one.",
        "In Azure: az role assignment list --assignee <appId>. If you see Owner at subscription, treat it as a finding. az role assignment create Contributor on rg-day63 and remove Owner if you can.",
        "If the UI created a client secret instead of WIF, delete that secret after switching to federated credential (Certificates & secrets → Federated credentials). Issuer https://vstoken.dev.azure.com/<org>.",
        "Queue a trivial pipeline job that uses azureSubscription: lab-sc (AzureCLI@2 az group list). Prove the robot works without your user password.",
        "Write docs/sc-day63.md: connection name, appId, roles, WIF vs secret. One connection per environment is the habit; today you have lab only.",
    ],
    "code_title": "Starter YAML — the connection name is the badge",
    "code": "pool:\n  vmImage: ubuntu-latest\nsteps:\n- task: AzureCLI@2\n  inputs:\n    azureSubscription: lab-sc   # ADO service connection, not the Entra client ID\n    scriptType: bash\n    scriptLocation: inlineScript\n    inlineScript: |\n      az account show --query name -o tsv\n      az group list --query \"[].name\" -o tsv\n# Federated credential subject (Entra, on the app):\n#   sc://<org>/<project>/lab-sc\n# Role (Azure): Contributor on /subscriptions/<sub>/resourceGroups/rg-day63\n",
    "checklist": [
        "Can separate app registration, service principal, and service connection in one breath",
        "lab-sc uses WIF (or you documented why not)",
        "Robot is not Owner on the subscription",
        "A pipeline job actually used the connection",
    ],
    "tomorrow": "Azure Key Vault — hotel safe, not a postcard in git",
}

SPECS[64] = {
    "topic": "Azure Key Vault",
    "subtitle": "Secrets, keys, certs — RBAC on the vault is the door; Contributor on the RG is not",
    "phase": "7 - Security, Compliance & Governance",
    "tables": [
        {
            "title": "Architecture A — three data types and two door locks",
            "columns": ["Thing", "What it holds", "Who reads it"],
            "rows": [
                ["Secret", "Connection strings, dummy DemoSecret", "Key Vault Secrets User (data plane). Not RG Contributor"],
                ["Key", "Cryptographic keys (encrypt/sign)", "Key Vault Crypto User / Officer — different role"],
                ["Certificate", "TLS material, often with a key + secret projection", "Cert roles; do not treat it as 'just a secret'"],
                ["Access policies (legacy)", "Vault-level policy entries per identity", "Do not mix with RBAC on the same vault as a hobby"],
                ["RBAC (modern)", "--enable-rbac-authorization true. Data-plane roles on vault or secret", "Control plane (vault resource) vs data plane (secret get) are different"],
            ],
            "widths": [40, 70, 72],
        },
        {
            "title": "Architecture B — decide dummy values, RBAC, and what not to screenshot",
            "columns": ["Constraint", "Default", "Reject"],
            "rows": [
                ["Authorization", "RBAC vault. Secrets Officer to set, Secrets User to read", "Access policies + RBAC both on, then debugging folklore"],
                ["Value", "DemoSecret = not-a-real-password", "A real password in a learning vault you will photograph"],
                ["Name", "Globally unique vault name", "Reusing a vault from a work sub"],
                ["Soft delete", "On by default. Literacy: recover deleted secrets", "Purge in the lab just to feel thorough"],
                ["Pipeline", "Do not paste DemoSecret into YAML today", "Day 65 fetches. Today the safe exists"],
            ],
            "widths": [32, 78, 72],
        },
        {
            "title": "Architecture C — pitfalls that leave the secret in git and the vault empty",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Contributor, still 403", "az keyvault secret show Forbidden", "Assign Key Vault Secrets User / Officer on the vault ID"],
                ["Secret in repo history", "git log -p still has the password after you 'deleted the line'", "Rotate. Treat history as leaked. Dummy values only today"],
                ["Portal screenshot of the value", "LinkedIn post is the incident", "Show the name blade, not the value"],
                ["Mixed permission model", "Assignments you cannot reason about", "RBAC only for this lab"],
                ["Public network + real secret", "Firewall later; dummy now", "Do not put production secrets in a wide-open lab vault"],
            ],
            "widths": [38, 72, 72],
        },
    ],
    "one_liner": "Key Vault is the hotel safe — secrets in repo chat history are postcards from an incident. If git ever saw it, rotate; do not delete the line and call it done.",
    "lab_intro": "Personal subscription rg-day64. Dummy value only. Personal UPN gets data-plane RBAC.",
    "lab": [
        "az group create -n rg-day64 -l eastus. az keyvault create -g rg-day64 -n <uniquekv> --enable-rbac-authorization true --sku standard.",
        "Assign yourself Key Vault Secrets Officer on the vault resource ID (need set). Optional: also Secrets User if you want the read-only role in notes.",
        "az keyvault secret set --vault-name <uniquekv> --name DemoSecret --value 'not-a-real-password'. az keyvault secret show --query name (not the value in any screenshot).",
        "Confirm RG Contributor alone is not the story: the data-plane role is why show works. Write that sentence.",
        "Do not enable access-policy mode. Do not put DemoSecret in the repo. Soft-delete literacy: note that delete is recoverable.",
        "Write docs/kv-day64.md: vault name, RBAC vs access policies, Secrets User vs Officer vs Contributor. Pipeline integration is tomorrow.",
    ],
    "code_title": "Starter CLI + Bicep property — RBAC vault, dummy secret",
    "code": "az keyvault create -g rg-day64 -n <uniquekv> --enable-rbac-authorization true --sku standard\nVAULT_ID=$(az keyvault show -n <uniquekv> --query id -o tsv)\naz role assignment create --assignee <your-upn> --role \"Key Vault Secrets Officer\" --scope $VAULT_ID\naz keyvault secret set --vault-name <uniquekv> --name DemoSecret --value \"not-a-real-password\"\naz keyvault secret show --vault-name <uniquekv> --name DemoSecret --query \"{n:name, id:id}\" -o json\n# Bicep: properties.enableRbacAuthorization: true\n#   Microsoft.KeyVault/vaults — control plane. Secret GET is data plane.\n",
    "checklist": [
        "RBAC vault exists; DemoSecret is a dummy",
        "Can explain why Contributor on the RG does not get secret GET",
        "No secret value in Git, chat, or LinkedIn",
        "docs/kv-day64.md records vault name and roles",
    ],
    "tomorrow": "Key Vault in pipelines — fetch at runtime, print length never the value",
}

SPECS[65] = {
    "topic": "Integrating Key Vault with Pipelines",
    "subtitle": "Three doors: AzureKeyVault@2, linked variable groups, App Service Key Vault references — pick on purpose",
    "phase": "7 - Security, Compliance & Governance",
    "tables": [
        {
            "title": "Architecture A — three ways a secret moves (pipeline is not the app)",
            "columns": ["Door", "Who fetches", "What the pipeline log should show"],
            "rows": [
                ["AzureKeyVault@2", "The job, via service connection with Secrets User on the vault", "*** and a length you print. Never the letters"],
                ["Variable group linked to KV", "Library group authorized to the pipeline; ADO maps secret names to $(DemoSecret)", "Same masking. Do not screenshot the Library value blade"],
                ["Key Vault reference", "App Service / Function app settings: @Microsoft.KeyVault(SecretUri=…)", "Pipeline need not see it. The app identity needs Secrets User"],
                ["Pipeline variable (plain)", "You pasted the secret into ADO", "A screenshot away from an incident. Not a door — a mailbox"],
                ["ARM/Bicep getSecret", "Deployment identity at deploy time", "Fine for resource wiring; still not a YAML literal"],
            ],
            "widths": [40, 72, 70],
        },
        {
            "title": "Architecture B — pick the door that matches the consumer",
            "columns": ["Consumer", "Default door", "Do not"],
            "rows": [
                ["A script step needs the value", "AzureKeyVault@2 SecretsFilter: DemoSecret, then env: VAL: $(DemoSecret)", "echo $(DemoSecret) or system.debug=true on that job"],
                ["Several jobs, same vault", "Linked variable group + 'Authorize' the pipeline", "Copy secret into a second non-linked group 'so it is easier'"],
                ["App runtime only", "Key Vault reference on the web app + app managed identity", "Download into the pipeline just to re-upload as an app setting"],
                ["Identity", "lab-sc (Day 63) with Key Vault Secrets User on the vault", "ACR admin-style passwords in Library"],
            ],
            "widths": [36, 82, 64],
        },
        {
            "title": "Architecture C — pitfalls that unmask a secret and still look green",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["echo the value", "Green job, secret in logs", "Print ${#VAL} only. Lab fails if letters appear"],
                ["system.debug true", "Masked variables expand in debug", "Keep debug off on secret jobs"],
                ["Concatenation tricks", "ADO masking misses a sliced string", "Do not get clever. Length is the proof"],
                ["Task vs group mash-up", "Two copies, different versions of DemoSecret", "One door for the lab; document which"],
                ["Connection lacks data-plane role", "AzureKeyVault@2 403", "Secrets User on the vault for the SP, not only Contributor on the RG"],
            ],
            "widths": [38, 72, 72],
        },
    ],
    "one_liner": "Pipelines that need secrets should fetch them — not store them in variable screenshots. Print the length. If the letters appear, the lab is red even when the job is green.",
    "lab_intro": "Personal azure-100-labs. lab-sc from Day 63. Vault from Day 64. Dummy DemoSecret only.",
    "lab": [
        "Grant the service connection's SP Key Vault Secrets User on the vault (data plane). Confirm lab-sc is the Azure RM connection, not the client ID pasted into YAML.",
        "Pipelines → Library → Variable group kv-lab. Link secrets from the Key Vault (DemoSecret). Authorize this pipeline. That is door 2 — you may use it instead of (or in addition to) the task, but pick one as the proof.",
        "Add AzureKeyVault@2 (door 1) with azureSubscription: lab-sc, KeyVaultName, SecretsFilter: DemoSecret, RunAsPreJob: true.",
        "Next step: bash that prints only ${#VAL} with env VAL: $(DemoSecret). Read the log. If DemoSecret's letters appear, you failed — fix masking before sleep.",
        "Write one sentence in docs/kv-pipeline-day65.md about Key Vault references (@Microsoft.KeyVault(SecretUri=…)) as door 3 for apps — pipeline may never see that value.",
        "No Library screenshots of the secret value. Dummy value stays dummy.",
    ],
    "code_title": "Starter YAML — fetch, then print length",
    "code": "pool:\n  vmImage: ubuntu-latest\nsteps:\n- task: AzureKeyVault@2\n  inputs:\n    azureSubscription: lab-sc\n    KeyVaultName: <uniquekv>\n    SecretsFilter: DemoSecret\n    RunAsPreJob: true\n- bash: |\n    echo \"DemoSecret length is ${#VAL}\"\n  displayName: Prove fetch without printing value\n  env:\n    VAL: $(DemoSecret)\n# Door 3 (app, not this job):\n# APPLICATIONINSIGHTS_CONNECTION_STRING=@Microsoft.KeyVault(SecretUri=https://<kv>.vault.azure.net/secrets/AppInsightsCs/)\n",
    "checklist": [
        "Pipeline fetched DemoSecret at runtime via task and/or linked group",
        "Log shows length or ***, never the dummy letters as a souvenir",
        "Can name all three doors: task, linked group, app Key Vault reference",
        "SP has Secrets User; RG Contributor was not the fix",
    ],
    "tomorrow": "Azure Policy — deny/audit so Finance is not your bouncer",
}

SPECS[66] = {
    "topic": "Azure Policy & Governance",
    "subtitle": "Definitions assign effects (Deny, Audit, …) at a scope — Blueprints are retired, initiatives are bundles",
    "phase": "7 - Security, Compliance & Governance",
    "tables": [
        {
            "title": "Architecture A — definition, initiative, assignment, effect",
            "columns": ["Object", "What it is", "Lab move"],
            "rows": [
                ["Definition", "JSON: if/then. Built-in 'Require a tag on resource groups'", "Use a built-in. Do not author custom JSON on day one"],
                ["Initiative (policy set)", "Bundle of definitions, one assignment", "Literacy. Assign one definition today"],
                ["Assignment", "Definition/initiative + scope (MG / sub / RG) + parameters + effect overlay sometimes", "Assign at lab RG or personal sub — not a work MG"],
                ["Compliance blade", "Compliant / non-compliant / not started", "Create a violating RG and watch the state — then delete it"],
                ["Blueprints", "Retired. Do not learn a dead product to sound enterprise", "Policy + landing-zone ideas are the current sentence"],
            ],
            "widths": [32, 82, 68],
        },
        {
            "title": "Architecture B — pick an effect like a culture choice, not a default checkbox",
            "columns": ["Effect", "What Azure does", "Use when"],
            "rows": [
                ["Audit", "Resource exists; marked non-compliant", "You need visibility first. Factories break if you Deny on day one"],
                ["Deny", "ARM PUT is blocked. Sin cannot land", "Lab tag requirement. Production after Audit noise is understood"],
                ["AuditIfNotExists", "Related resource missing (e.g. diagnostics) → non-compliant", "You are surveying a gap, not deploying it yet"],
                ["DeployIfNotExists", "Repair by deploying the missing related resource", "You accept the managed identity Policy needs to deploy"],
                ["Modify / Append / Disabled", "Mutate fields, or park the assignment", "Append a tag; Disabled = assignment exists but does nothing"],
            ],
            "widths": [36, 74, 72],
        },
        {
            "title": "Architecture C — pitfalls that never fire or block the wrong RG",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Wrong scope", "Compliance always green; you created the RG elsewhere", "Assignment scope must ancestor the resource"],
                ["Audit vs Deny confusion", "'Policy is on' but untagged RG still created", "Read the effect. Audit does not block"],
                ["Not-started forever", "Evaluation lag or wrong resource type", "Trigger a scan; confirm the definition applies to resource groups"],
                ["Custom JSON first", "Broken if/then, empty compliance", "Built-in require-tag-on-RGs, parameter tagName=env"],
                ["Work management group", "Employer policy in a personal series screenshot", "Personal sub/RG only. Delete the test RG after"],
            ],
            "widths": [36, 74, 72],
        },
    ],
    "one_liner": "Policy is the grown-up saying 'no untagged RGs' so Finance does not hunt you with spreadsheets. Audit sees sin; Deny stops it; the effect is a choice.",
    "lab_intro": "Personal subscription or rg-day66. Built-in policy only. Clean up the violating RG so compliance is not a junk drawer.",
    "lab": [
        "Portal → Policy → Definitions. Search Require a tag on resource groups. Open it and read the effect (typically Deny) and the parameter tagName.",
        "Policy → Assignments → Assign policy. Scope = personal sub or rg-day66. Parameter tagName=env. Note whether you leave Deny or set Audit for the experiment.",
        "Try az group create -n rg-day66-nopolicy -l eastus with no env tag. If Deny: create fails. If Audit: create succeeds and Compliance shows non-compliant.",
        "Create a compliant RG with --tags env=lab. Open Compliance blade. Screenshot states without any employer MG names.",
        "Delete the non-compliant/junk RG. Do not leave Policy nagging a leftover forever. Optional CLI: az policy assignment create with the built-in definition ID.",
        "Write docs/policy-day66.md: effect you used, what you observed, initiative vs definition in one line, Blueprints = retired.",
    ],
    "code_title": "Starter CLI — assign a built-in, then prove the effect",
    "code": "# Built-in: Require a tag on resource groups (effect: Deny)\n# Definition ID 96670d01-0a4d-4649-9c89-2d3efa4e1136\nSUB=$(az account show --query id -o tsv)\naz policy assignment create --name require-rg-tag-lab \\\n  --display-name \"Require env tag on RGs (lab)\" \\\n  --scope /subscriptions/$SUB \\\n  --policy 96670d01-0a4d-4649-9c89-2d3efa4e1136 \\\n  --params '{\"tagName\":{\"value\":\"env\"}}'\n# Prove Deny:\n# az group create -n rg-day66-nopolicy -l eastus          # should fail\naz group create -n rg-day66 -l eastus --tags env=lab     # should succeed\n",
    "checklist": [
        "Can name Deny vs Audit vs AuditIfNotExists vs DeployIfNotExists",
        "One built-in assignment visible on the compliance blade",
        "Proved the effect with a tagged vs untagged RG",
        "Junk RG deleted; Blueprints not in the notes as current",
    ],
    "tomorrow": "Compliance scanning in pipelines — SARIF as a format, not a product tour",
}

SPECS[67] = {
    "topic": "Compliance Scanning in Pipelines",
    "subtitle": "Secret scan, SCA, SAST — publish SARIF; fail on high; a ignored scan is décor",
    "phase": "7 - Security, Compliance & Governance",
    "tables": [
        {
            "title": "Architecture A — three scans and one result format",
            "columns": ["Scan", "When it runs", "What 'done' is"],
            "rows": [
                ["Secret scanning", "On the repo / PR (gitleaks, ADO secret scanning, GitHub push protection)", "Build fails if a key-shaped string lands. Day 64 is wasted otherwise"],
                ["SCA (dependencies)", "On restore (pip-audit, npm audit, NuGet)", "Lockfile + fail on high/critical. A lockfile without a scan is a list"],
                ["SAST", "On source (language analyzer if you have one)", "Findings next to the commit. If you have no task, document the gap"],
                ["SARIF", "Static Analysis Results Interchange Format — JSON the tools emit", "Publish the file (e.g. CodeAnalysisLogs). Humans and portals both ingest it"],
                ["Collector products", "Microsoft Defender for DevOps / Microsoft Security DevOps task can gather SARIF", "A concept: one publisher of results. Not a marketplace shopping lab"],
            ],
            "widths": [34, 78, 70],
        },
        {
            "title": "Architecture B — fail criteria before you install a brand",
            "columns": ["Finding", "Default gate", "Warn-only when"],
            "rows": [
                ["Secret in repo", "Fail. Always", "Never. Rotate if it already shipped"],
                ["Critical / high CVE in a dep you ship", "Fail if the tool can exit non-zero", "First run baseline — time-box, then tighten. Not forever"],
                ["Medium / noise", "Warn in the summary", "Silent continueOnError — that is how kitchens burn politely"],
                ["Tool missing", "Script + open-source scanner in Docker", "Skipping because the Microsoft task needs an extra install click"],
                ["Where results go", "Pipeline summary + SARIF artifact", "Line 4000 of a log nobody opens"],
            ],
            "widths": [40, 72, 70],
        },
        {
            "title": "Architecture C — pitfalls that make a green build look 'secure'",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Scan not in PR", "Main is clean; feature branches leak secrets", "Same job on pull request validation"],
                ["continueOnError: true", "Always green, SARIF ignored", "Remove it. Fail the job"],
                ["Product tour instead of a gate", "Three extensions, zero fail criteria", "One secret scan that can fail. Brands are optional collectors"],
                ["Dummy DemoSecret committed", "gitleaks may or may not fire on 'not-a-real-password'", "Do not commit it to test. Use a fake AWS AKIA pattern in a branch you will drop if you must test fail"],
                ["SARIF unpublished", "Tool ran, Azure DevOps shows nothing", "Write results.sarif; publish artifact. Ingestion is the point of the format"],
            ],
            "widths": [40, 71, 71],
        },
    ],
    "one_liner": "Shift-left security means finding the fire in the kitchen, not on the evening news. SARIF is the receipt format; the gate is a non-zero exit on secrets and critical CVEs.",
    "lab_intro": "Personal azure-100-labs. Microsoft-hosted ubuntu-latest. No employer scanners. No product-spam install-all.",
    "lab": [
        "Add a secret-scan step (gitleaks in Docker is enough). --exit-code 1. Publish a SARIF file as an artifact if the tool can emit it.",
        "Add a dependency scan on restore for whatever the sample app uses (npm audit --audit-level=high, pip-audit, etc.). Decide fail vs warn in a markdown file — not in your head.",
        "Optional: Microsoft Security DevOps / Defender for DevOps as a SARIF collector — only if it is already easy. The concept is 'tools → SARIF → pipeline'. Do not spend the lab on a marketplace tour.",
        "Run on a branch. If you need to prove fail, use a throwaway file with a clearly fake credential pattern and delete that commit. Do not commit Day 64's vault value.",
        "Confirm results are visible without opening raw logs (summary, artifact, or annotations). continueOnError must be off for the secret step.",
        "Write docs/scan-day67.md: tools used, fail criteria, SARIF yes/no. Tomorrow the Security stage wraps this.",
    ],
    "code_title": "Starter YAML — secret scan to SARIF, fail closed",
    "code": "pool:\n  vmImage: ubuntu-latest\nsteps:\n- bash: |\n    docker run --rm -v \"$(pwd):/repo\" ghcr.io/gitleaks/gitleaks:latest detect \\\n      --source=/repo --report-format sarif --report-path /repo/gitleaks.sarif --exit-code 1\n  displayName: Secret scan (fail on findings)\n- task: PublishBuildArtifacts@1\n  inputs:\n    PathtoPublish: gitleaks.sarif\n    ArtifactName: CodeAnalysisLogs\n  condition: always()\n- bash: npm audit --audit-level=high\n  displayName: SCA — fail on high (Node sample)\n# SARIF is a format. Defender for DevOps is one optional collector, not the homework.\n",
    "checklist": [
        "Secret scan can fail the job",
        "Knows SAST vs SCA vs secrets as three jobs, not one brand",
        "SARIF treated as the interchange format, not a product name",
        "Fail criteria written; continueOnError not used as a gate",
    ],
    "tomorrow": "DevSecOps shift-left — Security stage before Deploy, not a final boss",
}

SPECS[68] = {
    "topic": "DevSecOps - Shift-left Security",
    "subtitle": "Build → Security → Deploy, with dependsOn — a parallel 'security job' is a race, not a gate",
    "phase": "7 - Security, Compliance & Governance",
    "tables": [
        {
            "title": "Architecture A — stage order is a control plane",
            "columns": ["Stage", "Job", "Gate"],
            "rows": [
                ["Build", "Compile / Docker@2 push to ACR", "Must succeed before scans that need the image/artifact"],
                ["Security", "Day 67 scans + any image scan. Exit non-zero on written criteria", "dependsOn: Build. Deploy must not start on failure"],
                ["Deploy", "ACI/AKS/App Service", "dependsOn: Security. condition: succeeded()"],
                ["PR validation", "Same Security jobs on pull requests when you can", "Main-only scans are how badness waits for merge"],
                ["continueOnError", "A confession on the Security job", "If present, you have a dashboard of regret, not shift-left"],
            ],
            "widths": [32, 80, 70],
        },
        {
            "title": "Architecture B — write fail criteria so the release date cannot vote",
            "columns": ["Criterion", "Default", "Exception you will actually write"],
            "rows": [
                ["Secret detected", "Fail Security. Deploy stays still", "None"],
                ["Critical CVE in shipped image/deps", "Fail", "Time-boxed waiver in markdown with an expiry — not a silent skip"],
                ["High CVE", "Fail if the tool distinguishes", "Warn week one, fail week two — dated"],
                ["Scanner outage", "Fail closed (job fails) or rerun", "Fail open only with a named owner. Lab: fail closed"],
                ["Where it runs", "PR + main", "Main-only because PRs 'are slower' — that is the final-boss pattern"],
            ],
            "widths": [36, 68, 78],
        },
        {
            "title": "Architecture C — pitfalls that still ship while Security is 'running'",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Security // Deploy parallel", "Deploy green, scan red two minutes later", "dependsOn: Security on Deploy"],
                ["condition: always() on Deploy", "Deploy runs on failed scans", "condition: succeeded()"],
                ["Stage named Security, job empty", "Theatre", "Put the real scan steps in that stage"],
                ["continueOnError on the gate", "Badge is yellow, prod changed", "Delete the flag"],
                ["Weekly security meeting as the gate", "Release date always wins", "Non-zero exit next to the commit"],
            ],
            "widths": [40, 71, 71],
        },
    ],
    "one_liner": "Security as a final boss stage is how you ship late — put checks next to the commit. If Deploy still runs when Security is red, the dependsOn is theatre.",
    "lab_intro": "Personal azure-100-labs. Reuse Day 67 steps inside a Security stage. Prove Deploy does not start on a forced failure.",
    "lab": [
        "Reshape the pipeline into stages: Build, Security, Deploy. Security dependsOn Build. Deploy dependsOn Security with condition succeeded().",
        "Move secret scan / SCA into Security. Keep fail-closed on secrets.",
        "Write docs/security-gates-day68.md: fail criteria (secret=fail, critical=fail, high=…). Two sentences, not a novel.",
        "Force a failure once (exit 1 in a throwaway step, or a fake finding). Confirm Deploy is skipped. If Deploy still runs, fix dependsOn/condition before anything else.",
        "If PR pipelines exist, add the Security job there. Main-only is a note in the doc as a gap, not a boast.",
        "Do not add continueOnError to look green on LinkedIn. Restore the pipeline to a passing dummy after the forced-fail proof.",
    ],
    "code_title": "Starter YAML — stages with a real dependsOn",
    "code": "stages:\n- stage: Build\n  jobs:\n  - job: compile\n    pool: { vmImage: ubuntu-latest }\n    steps:\n    - script: echo build\n- stage: Security\n  dependsOn: Build\n  jobs:\n  - job: gates\n    pool: { vmImage: ubuntu-latest }\n    steps:\n    - script: echo \"secret scan + SCA live here\"\n    - script: exit 0   # flip to 1 to prove Deploy does not start\n      displayName: Forced-fail switch\n- stage: Deploy\n  dependsOn: Security\n  condition: succeeded()\n  jobs:\n  - job: push\n    pool: { vmImage: ubuntu-latest }\n    steps:\n    - script: echo deploy\n",
    "checklist": [
        "Three stages in that order with dependsOn",
        "Forced failure skipped Deploy",
        "Fail criteria written in markdown",
        "continueOnError not on the Security gate",
    ],
    "tomorrow": "Secure pipeline design — boring on purpose: approvals, locks, scoped connections",
}

SPECS[69] = {
    "topic": "Secure Pipeline Design",
    "subtitle": "Who can edit YAML can ship — branch policy, env approvals, one connection per environment",
    "phase": "7 - Security, Compliance & Governance",
    "tables": [
        {
            "title": "Architecture A — controls around the YAML, not only inside it",
            "columns": ["Control", "Where", "Failure if missing"],
            "rows": [
                ["Branch policy on main", "Repos → Branches → min reviewers + required build", "A Contributor pushes to main and skips Security"],
                ["Who can edit pipelines", "Project → Pipelines security / repo ACL", "Approvals are a speed bump around a hole — anyone rewrites Deploy"],
                ["Environment approval", "Pipelines → Environments → lab/prod → Approvals", "deployment: job goes to prod from a feature branch unattended"],
                ["Service connection scope", "lab-sc → rg-lab. prod-sc → rg-prod. Not one azure Owner", "Day 63 master key with a friendly name"],
                ["Agent threat model", "Hosted ubuntu-latest for these labs", "Self-hosted with org-wide creds is lateral movement as a hobby"],
            ],
            "widths": [40, 72, 70],
        },
        {
            "title": "Architecture B — decide prod drama vs lab boredom",
            "columns": ["Question", "Lab default", "Prod-shaped habit"],
            "rows": [
                ["Who approves", "You (email on the environment)", "A group, not a shared password"],
                ["Which branch deploys", "main only via environment + checks", "Feature branch with a prod connection — never"],
                ["Secrets in logs", "Day 65 length-only; debug off", "system.debug on a KV job is how incidents write themselves"],
                ["SPN leftover", "Remove Owner from lab-sc if still present", "An old Owner SPN from 'the wizard' is in-scope today"],
                ["Templates", "Optional; do not hide Owner in a template nobody reads", "Reviewed YAML still beats folklore"],
            ],
            "widths": [32, 70, 80],
        },
        {
            "title": "Architecture C — pitfalls that look like security and still ship from a fork",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Approval on the wrong environment", "Deploy job uses environment: none", "job type: deployment + environment: lab"],
                ["Open main", "Direct pushes, required check never runs", "Branch policy: require pull request"],
                ["Same SC for lab and 'prod'", "rg-prod deleted from a lab experiment", "Two connections, two RGs, two identities"],
                ["Secret echo still on", "Logs from Day 65 regress", "Re-read the length-only step"],
                ["Cannot answer who can ship", "Hope", "The audit is the lab. Write names/roles from the personal org"],
            ],
            "widths": [42, 68, 72],
        },
    ],
    "one_liner": "A secure pipeline is boring on purpose — drama belongs in fiction, not release logs. If you cannot answer who can ship, you do not have a secure pipeline.",
    "lab_intro": "Personal Azure DevOps org only. Audit azure-100-labs. Remove leftover Owner SPNs you created in this series.",
    "lab": [
        "Audit: Project Settings → Permissions / Pipelines. Who can edit pipeline YAML? Write the list (it may be only you). If Contributors can rewrite prod stages, note it as a finding.",
        "Repos → Branches → main: require a pull request (even if you are the only reviewer in a personal org). Required check = the pipeline with Security.",
        "Pipelines → Environments → create lab. Add an Approval (your user). Change Deploy to a deployment job with environment: lab.",
        "Inspect lab-sc (and any second connection). Remove subscription Owner if present. Confirm it cannot see a RG you did not intend. Separate names if you already have a prod-shaped RG.",
        "Re-check no secret echo / system.debug on Key Vault jobs. Tick a checklist file docs/secure-pipeline-day69.md: connections per env, no secret echo, main locked, approval on.",
        "Do not use an employer org for this audit. Boring is the outcome.",
    ],
    "code_title": "Starter YAML — deployment job hits an environment with approvals",
    "code": "stages:\n- stage: DeployLab\n  jobs:\n  - deployment: toLab\n    pool: { vmImage: ubuntu-latest }\n    environment: lab    # Approvals live on this environment\n    strategy:\n      runOnce:\n        deploy:\n          steps:\n          - checkout: self\n          - task: AzureCLI@2\n            inputs:\n              azureSubscription: lab-sc   # not prod-sc, not subscription Owner\n              scriptType: bash\n              scriptLocation: inlineScript\n              inlineScript: echo \"lab RG only\"\n# Checklist (also in docs):\n# - separate service connections per env\n# - no secret echo / system.debug off on KV jobs\n# - main locked with PR + required build\n# - prod/lab approval required\n",
    "checklist": [
        "Can name who can edit pipelines and who can approve lab",
        "main has a PR policy; Deploy uses environment: lab",
        "lab-sc is not subscription Owner",
        "docs/secure-pipeline-day69.md checklist ticked",
    ],
    "tomorrow": "Phase 7 mini project — secret not in YAML, policy visible, approvals on",
}

SPECS[70] = {
    "topic": "Mini Project + Recap (Phase 7)",
    "subtitle": "Speed without security is just a faster incident — identity, then RBAC, then the hotel safe",
    "phase": "7 - Security, Compliance & Governance",
    "tables": [
        {
            "title": "Architecture A — Phase 7 map (order is the product)",
            "columns": ["Layer", "Object", "Done looks like"],
            "rows": [
                ["Identity", "Entra tenant, day61-lab appId", "Personal directory; no secret in git"],
                ["RBAC", "Reader/Contributor at RG, not Owner at sub", "Scope sentence you can say out loud"],
                ["Robot badge", "lab-sc = WIF service connection + SP", "Not the same object as the app registration blade"],
                ["Safe", "Key Vault RBAC + DemoSecret dummy + pipeline fetch", "Length in logs, not letters"],
                ["Guardrails", "Policy Deny/Audit + Security stage + approvals", "Compliance blade + Deploy skipped on red scan"],
            ],
            "widths": [28, 78, 76],
        },
        {
            "title": "Architecture B — mini project scope (one pipeline, one policy, no theatre)",
            "columns": ["Piece", "Include", "Exclude"],
            "rows": [
                ["Pipeline", "AzureKeyVault@2 or linked group; Security before Deploy; environment approval", "A second CD platform to look busy"],
                ["Policy", "Require env tag on RGs, assignment visible", "Custom policy JSON and three initiatives"],
                ["Secret", "Dummy DemoSecret only", "Real passwords, work Key Vaults"],
                ["Identity leftovers", "Strip Owner from lab-sc", "Creating more SPNs 'for completeness'"],
                ["Evidence", "docs/phase7-recap.md + screenshots without values", "LinkedIn photo of a secret blade"],
            ],
            "widths": [28, 86, 68],
        },
        {
            "title": "Architecture C — recap failures that still look like a security week",
            "columns": ["Failure", "What you see", "Fix"],
            "rows": [
                ["Secret in YAML", "$(password): hunter2 still in git", "Fetch only; rotate if it was real (it should not be)"],
                ["Policy assigned nowhere", "Doc says Policy; Compliance is empty", "Show the assignment and a tagged RG"],
                ["Approvals off", "deployment job without environment", "environment: lab with your approval"],
                ["Owner SPN remains", "Wizard gift from Day 63", "Remove it as part of done"],
                ["Work tenant evidence", "Employer directory in the recap", "Delete the post draft; personal only"],
            ],
            "widths": [34, 74, 74],
        },
    ],
    "one_liner": "Phase 7 recap: speed without security is just a faster incident. Done = secret not in YAML, a policy you can see, approvals on, robot not Owner.",
    "lab_intro": "Personal subscription + azure-100-labs. Mini project is a demo, not a SIEM. Definition of done is written below.",
    "lab": [
        "Run one pipeline that fetches DemoSecret (length only) and has stages Build → Security → Deploy with environment: lab approval.",
        "Confirm Policy assignment from Day 66 still exists (or re-assign require tag). Compliance blade shows the lab scope.",
        "Confirm lab-sc is WIF, not Owner at subscription, and has Secrets User on the vault.",
        "Confirm main is PR-protected and no secret values live in YAML/Library screenshots.",
        "Write docs/phase7-recap.md: bouncer list → scoped badges → hotel safe → Policy effect → Security stage. Screenshot without secret values.",
        "Tear down junk RGs from the policy experiment if they remain. Keep the vault only if you still need it for Phase 8 — else delete dummy secrets first.",
    ],
    "code_title": "Definition of done — Phase 7",
    "code": "# Done when all are true:\n# 1. DemoSecret is not a YAML literal; job prints length only\n# 2. Policy assignment visible (tagName=env); effect named (Deny or Audit)\n# 3. Deploy is a deployment job with environment: lab approval\n# 4. lab-sc = WIF; Contributor (or less) on one RG; Secrets User on the vault\n# 5. main requires PR; Security dependsOn Build; Deploy dependsOn Security\n# 6. docs/phase7-recap.md exists; no secret values in it\n",
    "checklist": [
        "Secret not in YAML; policy visible; approvals on",
        "Can explain app registration vs service connection vs RBAC scope",
        "Owner SPN leftover removed or documented as absent",
        "Phase 7 recap doc on the personal repo",
    ],
    "tomorrow": "Azure Monitor fundamentals — the flashlight, not the fix",
}

SPECS[71] = {
    "topic": "Azure Monitor Fundamentals",
    "subtitle": "Metrics are the pulse, logs are the sentences, activity is who changed ARM — diagnostics are opt-in",
    "phase": "8 - Monitoring & Observability",
    "tables": [
        {
            "title": "Architecture A — four signal families (Monitor is the flashlight)",
            "columns": ["Signal", "What it answers", "Where it lives"],
            "rows": [
                ["Metrics", "CPU, availability, queue length — numbers on a time axis", "Platform metrics on the resource. Near-real-time, cheap-ish"],
                ["Logs", "The story in rows you query with KQL", "Log Analytics workspace, only after diagnostic settings (or agents) send them"],
                ["Activity log", "Control plane: who PUT/DELETE this RG / vault / AKS", "Subscription activity. Not the app's 500s"],
                ["Diagnostic settings", "The pipe: resource → workspace / storage / event hub", "Opt-in. Without them the workspace is an empty room"],
                ["Insights blades", "App Insights, Container Insights, VM Insights — packaged views", "Still Monitor. They do not patch the hole"],
            ],
            "widths": [36, 76, 70],
        },
        {
            "title": "Architecture B — turn on a light without buying a SIEM",
            "columns": ["Constraint", "Default today", "Skip / delay"],
            "rows": [
                ["One resource", "Key Vault AuditEvent or App Service HTTP logs → LAW", "Every resource in the sub 'for completeness'"],
                ["Retention", "Short (workspace default / 30 days class) for a lab", "730-day retention as a personality trait — that is a storage bill"],
                ["Cost already tight", "Map the four signals on paper; skip the workspace", "Leaving diagnostics on a chatty resource all month"],
                ["'It is down'", "Pick one signal you would actually look at", "A dashboard with no diagnostic settings behind it"],
                ["Alerts", "Tomorrow+ (Day 74). Today is the pipe", "Alert rules with no destination yet"],
            ],
            "widths": [32, 80, 70],
        },
        {
            "title": "Architecture C — pitfalls that start a war room with screenshots and feelings",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["No diagnostic setting", "Workspace queries return zero; people argue", "Enable logs to LAW on one lab resource"],
                ["Activity log as app log", "You know who deleted the webapp, not why it 500'd", "Need App Insights / resource logs for that"],
                ["Metrics without dimensions", "Average CPU looks fine, one instance is on fire", "Split by instance when the resource has more than one"],
                ["Infinite retention", "Cost Analysis surprise", "Set a finite cap; lab can be minimal"],
                ["Monitor as the fix", "Pretty chart of 500s, still 500s", "Flashlight ends the argument about reality. Patch is later"],
            ],
            "widths": [38, 72, 72],
        },
    ],
    "one_liner": "If you cannot see it, you cannot fix it — Monitor is the flashlight, not the fix. Turn on diagnostics before you argue about which wall is wet.",
    "lab_intro": "Personal subscription. One lab resource (Key Vault from Phase 7 or an App Service). Short retention. No employer workspace.",
    "lab": [
        "Portal → Monitor → Overview. Click through Metrics, Activity log, Logs. Write one sentence each: pulse vs diary vs sentences.",
        "Create or reuse a Log Analytics workspace in a lab RG (law-lab) if cost allows. If you skip, still complete the paper map and say why.",
        "On one resource (Key Vault or App Service) → Diagnostic settings → send Audit / HTTP logs + AllMetrics to law-lab. Category vs category group: pick what the blade offers.",
        "Generate a control-plane event (tag the resource). Activity log should show your user. That is not an app failure.",
        "Write docs/monitor-day71.md: which signal you would use to detect 'it is down', retention choice, resource id of the diagnostic setting.",
        "Do not onboard the whole subscription. Do not start a 90-day retention experiment. KQL is tomorrow.",
    ],
    "code_title": "Starter CLI — diagnostic setting to a workspace",
    "code": "az monitor log-analytics workspace create -g rg-day71 -n law-lab -l eastus\nLAW=$(az monitor log-analytics workspace show -g rg-day71 -n law-lab --query id -o tsv)\nKV=$(az keyvault show -n <uniquekv> --query id -o tsv)\naz monitor diagnostic-settings create --name kv-to-law --resource $KV --workspace $LAW \\\n  --logs '[{\"category\":\"AuditEvent\",\"enabled\":true}]' \\\n  --metrics '[{\"category\":\"AllMetrics\",\"enabled\":true}]'\n# Activity log is subscription-level (Monitor → Activity). It is not this pipe.\n",
    "checklist": [
        "Can separate metrics, logs, and activity log without mixing them",
        "One diagnostic setting exists — or a written cost skip plus the paper map",
        "Knows diagnostics are opt-in",
        "docs/monitor-day71.md names the 'it is down' signal",
    ],
    "tomorrow": "Log Analytics and KQL — ask a precise question, stop screenshotting 10,000 rows",
}

SPECS[72] = {
    "topic": "Log Analytics Workspace & KQL",
    "subtitle": "A workspace is a database for telemetry — TimeGenerated is part of every honest question",
    "phase": "8 - Monitoring & Observability",
    "tables": [
        {
            "title": "Architecture A — workspace, table, query (KQL is not Excel)",
            "columns": ["Piece", "What it is", "Lab table"],
            "rows": [
                ["Workspace", "The store. Retention and access live here", "law-lab from Day 71"],
                ["Table", "AzureActivity, Heartbeat, KV audit, App traces — schema differs", "AzureActivity is friendly even when Heartbeat is empty (no VMs)"],
                ["KQL", "where / summarize / join / top. SQL's cousin in the cloud", "Always filter TimeGenerated. Unbounded queries wait and pay"],
                ["Saved query", "Workspace notebook so tomorrow-you does not reinvent the where", "Save one query by name"],
                ["Empty result", "A result. New labs are quiet", "Do not fake a graph. Enable Day 71 diagnostics first"],
            ],
            "widths": [28, 86, 68],
        },
        {
            "title": "Architecture B — pick queries that match what you actually ingested",
            "columns": ["Question", "Default KQL", "Wrong table"],
            "rows": [
                ["Who changed ARM today?", "AzureActivity | where TimeGenerated > ago(1d) | summarize count() by OperationNameValue", "Heartbeat — that is agent/VM pulse"],
                ["Are agents alive?", "Heartbeat | summarize Last=max(TimeGenerated) by Computer", "AzureActivity — control plane is not a VM ping"],
                ["Top noisy operations", "top 10 by count_", "Export to Excel to 'just filter'"],
                ["App 500s", "App Insights requests/traces (Day 73) or AppService logs if diagnosed", "AzureActivity Put WebApps"],
            ],
            "widths": [36, 90, 56],
        },
        {
            "title": "Architecture C — pitfalls the cousin judges you for",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["No TimeGenerated filter", "Query spins; bill ticks", "where TimeGenerated > ago(1d) first"],
                ["Screenshot of 10k rows", "Nobody summarizes", "summarize + top 10"],
                ["Heartbeat on a VM-less sub", "Empty, assumed 'broken KQL'", "Use AzureActivity; empty Heartbeat is honest"],
                ["Query only in chat", "Lost tomorrow", "Save in the workspace"],
                ["Wrong workspace", "Tables you expected from Day 71 missing", "Picker in Logs blade = law-lab, not a work default"],
            ],
            "widths": [40, 71, 71],
        },
    ],
    "one_liner": "KQL is SQL's cousin who lives in the cloud and judges your where-clauses. Ask a precise question with TimeGenerated. Excel is not a Log Analytics strategy.",
    "lab_intro": "Personal law-lab. If the workspace is empty, send a diagnostic from Day 71 before inventing tables.",
    "lab": [
        "Portal → Log Analytics workspace law-lab → Logs. Confirm you are not in an employer workspace.",
        "Run query 1: AzureActivity | where TimeGenerated > ago(1d) | summarize count() by OperationNameValue | top 10 by count_.",
        "Run query 2: a where on a specific OperationNameValue you saw, or AzureActivity | take 10 if the lab is quiet — still a result.",
        "Run query 3: Heartbeat | take 5. If empty, write 'no VMs onboarded' — do not pretend. Optionally query the Key Vault audit table if Day 71 sent AuditEvent.",
        "Save one query with a name (e.g. lab-azureactivity-topops). Screenshot results without tenant gossip.",
        "Write docs/kql-day72.md: the three queries, which tables were empty, and why TimeGenerated is mandatory.",
    ],
    "code_title": "Starter KQL — time bound, summarize, top",
    "code": "AzureActivity\n| where TimeGenerated > ago(1d)\n| summarize count() by OperationNameValue\n| top 10 by count_\n\nAzureActivity\n| where TimeGenerated > ago(1d)\n| where OperationNameValue has \"Microsoft.Resources/subscriptions/resourcegroups\"\n| project TimeGenerated, Caller, OperationNameValue, ActivityStatusValue\n\nHeartbeat\n| where TimeGenerated > ago(1h)\n| summarize LastSeen=max(TimeGenerated) by Computer\n",
    "checklist": [
        "Three queries ran against the personal workspace",
        "One query saved",
        "Can explain why Heartbeat may be empty and AzureActivity still useful",
        "Every query used a TimeGenerated filter (or take with a reason)",
    ],
    "tomorrow": "Application Insights — a GoPro on the app, connection string not in git",
}

SPECS[73] = {
    "topic": "Application Insights Integration",
    "subtitle": "Instrumentation + connection string — dependencies tell you which friend is slow",
    "phase": "8 - Monitoring & Observability",
    "tables": [
        {
            "title": "Architecture A — SDK, connection string, workspace-based resource",
            "columns": ["Piece", "Job", "Secret handling"],
            "rows": [
                ["App Insights resource", "Workspace-based component (classic is legacy)", "Create in rg-day73; tie to law-lab"],
                ["Connection string", "SDK send target (InstrumentationKey is old news)", "App setting or Key Vault reference. Never commit"],
                ["SDK / auto-instrumentation", "Requests, exceptions, dependencies, live metrics", "Runtime. A portal resource with no SDK is an empty GoPro"],
                ["Dependencies", "HTTP/SQL/Redis map of who you wait on", "A slow app with clean CPU is often a slow friend"],
                ["Live metrics", "Incident stream", "Not the only alert; wallpaper is Day 74's problem"],
            ],
            "widths": [40, 72, 70],
        },
        {
            "title": "Architecture B — instrument, demo data, or honest empty",
            "columns": ["Constraint", "Default", "Honesty rule"],
            "rows": [
                ["Sample app you own", "Add SDK or Azure auto-instrumentation; set connection string via app settings / KV", "Do not paste the connection string into Git 'temporarily'"],
                ["No app today", "Create the resource; walk Failures / Performance with demo or zero data", "Label demo data as demo. Empty is not 'we are reliable'"],
                ["Key Vault", "Store connection string as a secret; app uses @Microsoft.KeyVault(SecretUri=…)", "Pipeline need not print it (Day 65 door 3)"],
                ["Traffic", "Hit the app; fail on purpose once if you can", "Admiring an empty Failures blade"],
            ],
            "widths": [32, 86, 64],
        },
        {
            "title": "Architecture C — pitfalls that record nothing useful",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Connection string in source", "Git history is a camera with a postcard", "Rotate; move to app settings / KV"],
                ["Resource without SDK", "Charts exist, all zero, assumed healthy", "Instrument or say 'dark'"],
                ["Sampling you did not know", "Missing a specific request", "Check sampling percentage before claiming 'never happened'"],
                ["Live metrics as the pager", "Someone must stare", "Day 74 alerts. Live metrics are for the incident"],
                ["Work app connection", "Employer telemetry in a personal lab", "Personal resource only"],
            ],
            "widths": [38, 72, 72],
        },
    ],
    "one_liner": "App Insights is a GoPro on your app — embarrassing, invaluable. No camera, no coaching. The connection string is a secret, not a README trophy.",
    "lab_intro": "Personal rg-day73. Workspace-based Application Insights. Connection string never committed.",
    "lab": [
        "az monitor app-insights component create (or Portal) in rg-day73, linked to law-lab. Copy the connection string into the vault or a local password manager — not the repo.",
        "Connect the sample app (SDK, Application Insights agent, or App Service auto-instrumentation). If you cannot, still create the resource and walk the blades with data honestly labeled.",
        "Generate traffic. Open Failures and Performance. Click a dependency if one exists. Note one request duration.",
        "Confirm git grep does not find InstrumentationKey or APPLICATIONINSIGHTS_CONNECTION_STRING values.",
        "Optional: add the connection string as a Key Vault reference on an App Service you already have. App identity needs Secrets User.",
        "Write docs/appi-day73.md: resource name, whether SDK or demo, that empty Failures means dark not reliable.",
    ],
    "code_title": "Starter CLI + app setting — connection string stays out of Git",
    "code": "az monitor app-insights component create \\\n  -g rg-day73 -l eastus -a appi-lab \\\n  --workspace $(az monitor log-analytics workspace show -g rg-day71 -n law-lab --query id -o tsv)\n# Store the connection string in Key Vault, then:\n# az webapp config appsettings set -g rg-day73 -n <app> --settings \\\n#   APPLICATIONINSIGHTS_CONNECTION_STRING=@Microsoft.KeyVault(SecretUri=https://<kv>.vault.azure.net/secrets/AppInsightsCs/)\n# KQL (once traffic exists):\n# requests | where timestamp > ago(1h) | summarize count(), avg(duration) by resultCode\n",
    "checklist": [
        "App Insights resource exists and is workspace-based",
        "Connection string not in the repo",
        "Generated traffic or honestly labeled empty/demo",
        "Can explain dependencies vs live metrics vs failures map",
    ],
    "tomorrow": "Alerts and action groups — screams need an inbox",
}

SPECS[74] = {
    "topic": "Alerts & Action Groups",
    "subtitle": "The rule is the condition; the action group is the destination — a rule with nobody to email is performance art",
    "phase": "8 - Monitoring & Observability",
    "tables": [
        {
            "title": "Architecture A — rule, condition, action group, severity",
            "columns": ["Piece", "What it is", "Lab choice"],
            "rows": [
                ["Action group", "Destination list: email, SMS, webhook, ITSM, ARM", "Email yourself (personal). Proof of delivery today"],
                ["Metric alert", "Platform metric threshold (CPU, availability)", "Something you can provoke on a tiny SKU or availability test"],
                ["Log alert", "KQL that returns rows → fire", "AzureActivity or App Insights requests failed > N"],
                ["Severity", "Sev 0–4 language", "Sev 3 for lab. If everything is Sev 0, nothing is"],
                ["Fired vs resolved", "State. Noise trains mute", "One clean fire beats ten flaps. Delete with the resource"],
            ],
            "widths": [32, 78, 72],
        },
        {
            "title": "Architecture B — action group first, then a condition you can force",
            "columns": ["Constraint", "Default", "Avoid"],
            "rows": [
                ["Destination", "Action group ag-lab-email → personal inbox", "Disabled mailbox / team DL you do not own"],
                ["Condition", "Availability ping on a URL you control, or a metric you can lift", "5xx on an app with zero traffic — never graduates from theory"],
                ["Window", "1–5 min evaluation for a lab", "24h window so you never see it fire today"],
                ["Smart detection only", "Fine as a bonus, not the only pager", "Assuming App Insights emails you without an action group"],
                ["After the lab", "Delete the alert with the resource", "Orphan rules firing for a year"],
            ],
            "widths": [32, 80, 70],
        },
        {
            "title": "Architecture C — pitfalls that scream into the void",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["Rule, no action group", "Monitor shows Fired; inbox silent", "Attach ag-lab-email. Then check spam"],
                ["Action group, no rule", "Theatre", "Create one alert that uses it"],
                ["Cannot provoke", "You never received the email; assumed it works", "Force CPU / stop the app / fail a test. Receipt required"],
                ["Sev 0 for disk 70%", "Mute culture", "Sev 3 lab; reserve 0 for wake-me"],
                ["Work SMS / PagerDuty", "Employer on-call in a personal series", "Personal email only"],
            ],
            "widths": [36, 74, 72],
        },
    ],
    "one_liner": "Alerts without action groups are screams into the void — polite, useless. Scream at an inbox that exists. An alert you have never received is a rumor about the future.",
    "lab_intro": "Personal subscription. Action group emails your personal address. One alert you can fire. Delete it when you delete the resource.",
    "lab": [
        "Monitor → Alerts → Action groups → Create ag-lab-email, short name labag, email receiver = your personal address.",
        "Create one alert rule: either a metric you can provoke, a standard availability test on a URL you control, or a log alert on a KQL you can satisfy. Severity 3. Attach ag-lab-email.",
        "Fire it (stop the app, exceed CPU on a tiny VM, or generate the log rows). Wait the evaluation window.",
        "Confirm the email arrived. If not: spam, action group receiver confirmed, alert Fired state in Portal. The lab is not done until delivery or a written blocker.",
        "Note the difference between Fired and a dashboard glance. Live metrics (Day 73) are not this.",
        "Write docs/alerts-day74.md: rule name, condition, action group, whether mail arrived. Plan to delete the rule with the resource so it does not flap for a year.",
    ],
    "code_title": "Starter CLI — action group, then a metric alert",
    "code": "az monitor action-group create -g rg-day74 -n ag-lab-email --short-name labag \\\n  --email-receiver name=me email=<personal@email>\n# Example metric alert (swap --scopes for a VM or App Service you can provoke):\naz monitor metrics alert create -g rg-day74 -n lab-cpu-or-availability \\\n  --scopes <resource-id> \\\n  --condition \"avg Percentage CPU > 80\" \\\n  --window-size 5m --evaluation-frequency 1m \\\n  --action ag-lab-email --severity 3\n# Availability tests: Portal → App Insights → Availability → add test → that action group.\n",
    "checklist": [
        "Action group emails the personal inbox",
        "One alert rule attached to that group",
        "Tried to receive the email (or documented the blocker)",
        "Severity chosen on purpose; delete plan written",
    ],
    "tomorrow": "Dashboards and workbooks — three tiles, not a 30-minute novel",
}

SPECS[75] = {
    "topic": "Dashboards & Workbooks",
    "subtitle": "A dashboard is a storyboard: up, erroring, spending — if it needs a TED talk it is a novel",
    "phase": "8 - Monitoring & Observability",
    "tables": [
        {
            "title": "Architecture A — dashboard vs workbook vs a pasted screenshot",
            "columns": ["Surface", "What it is", "Share / identity"],
            "rows": [
                ["Azure dashboard", "Pinned tiles from real blades (App Insights, Cost, metrics)", "Share with yourself only in this lab. Public = leak risk"],
                ["Workbook", "Narrative + parameters + queries. A runbook in portal form", "Literacy today. Do not add chapters because the storyboard is already long"],
                ["App Insights view", "Failures / availability as source of pins", "Pin the live chart, not a PNG of last Tuesday"],
                ["Cost Management tile", "Are we spending by accident?", "Lab sparkline keeps the habit honest"],
                ["ADO dashboard", "Pipeline widgets — different product (Day 76 energy)", "Do not mix it into the Azure storyboard unless labeled"],
            ],
            "widths": [36, 78, 68],
        },
        {
            "title": "Architecture B — three tiles, three questions",
            "columns": ["Question", "Pin this", "Do not pin"],
            "rows": [
                ["Are we up?", "Availability test result or App Insights availability", "A VM CPU chart as a proxy for 'the website works'"],
                ["Are we erroring?", "Failed requests / exceptions", "A green empty Failures blade labeled 'healthy' when the SDK is dark"],
                ["Are we spending by accident?", "Cost by RG or the lab RG sparkline", "A fictional savings percentage"],
                ["Need a guided investigation?", "Workbook with a time parameter", "Twelve more dashboard tiles instead of a workbook step"],
            ],
            "widths": [40, 74, 68],
        },
        {
            "title": "Architecture C — pitfalls that turn a glance into a novel",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [
                ["30-min explanation required", "Stakeholders glaze over", "Cut to three tiles. Workbook for the tour"],
                ["Screenshot-as-tile", "Stale PNG, looks official", "Pin from the blade so it queries"],
                ["Shared too widely", "Lab telemetry + maybe a secret in a query", "Myself only. Review pins for secret names"],
                ["No data, fake green", "Empty = healthy folklore", "Tile subtitle 'no data yet' or fix Day 73 traffic"],
                ["Every metric you know", "Novel", "If you cannot name the question, delete the tile"],
            ],
            "widths": [40, 71, 71],
        },
    ],
    "one_liner": "A dashboard is a storyboard — if it needs a 30-minute explanation, it is a novel, not a dashboard. Three tiles: up, erroring, spending. Share with yourself only.",
    "lab_intro": "Personal Azure Portal. Dashboard visible to you only. Pin live charts from App Insights and Cost Management when you have them.",
    "lab": [
        "Portal → Dashboard → New. Name it azure-100-lab. Privacy: private / share with yourself only.",
        "Pin tile 1 — availability (App Insights availability test or a metric that means 'up'). If you have no test, pin what you do have and label the gap.",
        "Pin tile 2 — failures / failed requests. If empty because the app is dark, write 'no data yet' in the tile title rather than inventing healthy green.",
        "Pin tile 3 — cost (Cost Management, lab RG). Even a small sparkline counts.",
        "Open Workbooks in Monitor or App Insights. Peek at a template (parameters, steps). Do not paste a 12-step novel onto the dashboard. One sentence in the doc: workbook = guided ops, dashboard = glance.",
        "Write docs/dashboard-day75.md: the three questions, share scope, and that Day 76 is pipeline analytics in Azure DevOps — a different storyboard.",
    ],
    "code_title": "Starter KQL for a workbook tile — requests by hour",
    "code": "requests\n| where timestamp > ago(24h)\n| summarize requests=count(), failed=countif(success == false) by bin(timestamp, 1h)\n| render timechart\n// Dashboard: Portal → Dashboard → New → pin Availability, Failures, Cost.\n// Share: myself only. Workbooks = parameters + narrative; cut tiles before adding chapters.\n",
    "checklist": [
        "Dashboard with three tiles mapped to up / erroring / spending",
        "Shared with yourself only",
        "Empty data labeled honestly",
        "Knows workbook vs dashboard in one sentence",
    ],
    "tomorrow": "Pipeline monitoring and analytics — a red pipeline ignored for a week is a culture problem",
}


def _validate() -> None:
    expected = set(range(51, 76))
    if set(SPECS) != expected:
        missing = sorted(expected - set(SPECS))
        extra = sorted(set(SPECS) - expected)
        raise SystemExit(f"SPECS keys mismatch: missing={missing} extra={extra}")
    for day, spec in SPECS.items():
        for key in ("topic", "subtitle", "phase", "tables", "one_liner", "lab_intro", "lab", "code", "checklist", "tomorrow"):
            if key not in spec:
                raise SystemExit(f"Day {day} missing {key}")
        if not (2 <= len(spec["tables"]) <= 3):
            raise SystemExit(f"Day {day} needs 2–3 tables, has {len(spec['tables'])}")
        if not (5 <= len(spec["lab"]) <= 7):
            raise SystemExit(f"Day {day} lab steps {len(spec['lab'])} not in 5–7")
        for table in spec["tables"]:
            total = sum(table["widths"])
            if total != 182:
                raise SystemExit(f"Day {day} {table['title']!r} widths sum {total}, want 182")
            cols = len(table["columns"])
            for i, row in enumerate(table["rows"]):
                if len(row) != cols:
                    raise SystemExit(f"Day {day} {table['title']!r} row {i} len {len(row)} != {cols}")


_validate()
