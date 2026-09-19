# Day 54 - Azure Container Instances (ACI)

| | |
|---|---|
| **Date** | 13 Oct 2026 |
| **Phase** | 6 - Containers & Kubernetes |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Serverless containers, quick deploys

## Hands-on lab (20-30 min)

1. Run your image in ACI once
2. Delete after test - ACI can surprise-bill

## Commands / code

```bash
az container create -g rg-day54 -n hello-aci \
  --image <acr>.azurecr.io/myapp:latest --registry-login-server <acr>.azurecr.io \
  --registry-username <user> --registry-password <pass> --dns-name-label <unique> --ports 80
```

## LinkedIn post (copy-paste)

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

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 54 — Azure Container Instances` (max 58 chars)
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

**Kubernetes fundamentals**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
