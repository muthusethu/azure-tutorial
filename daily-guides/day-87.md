# Day 87 - Azure Landing Zones

| | |
|---|---|
| **Date** | 15 Nov 2026 |
| **Phase** | 9 - Advanced & Enterprise |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Enterprise-scale, hub-spoke - concepts

## Hands-on lab (20-30 min)

1. Read CAF landing zone overview
2. Sketch hub-spoke on paper for a fake company

## Commands / code

```bash
# Hub: shared networking/firewall
# Spokes: workloads
# Management groups + policy
```

## LinkedIn post (copy-paste)

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

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 87 — Azure Landing Zones` (max 58 chars)
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

**GitOps with Flux/Argo**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
