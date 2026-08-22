# Day 2 — Azure Portal, CLI & PowerShell Basics

| | |
|---|---|
| **Date** | 22 Aug 2026 |
| **Phase** | 1 — Azure & DevOps Foundations |
| **Time box** | 60–90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Know when to use Portal vs CLI vs PowerShell. Install Azure CLI, create a resource group from the command line, and publish Day 2 on LinkedIn with the PDF handout.

## Learn (20–30 min)

- When to use Portal vs CLI vs PowerShell
- Install Azure CLI; sign-in with `az login`
- Resource groups, subscriptions, naming conventions (`rg-`, `app-`, `pip-`)
- Docs: [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

## Hands-on lab (20–30 min)

1. Install Azure CLI on your **personal** PC ([Windows installer](https://aka.ms/installazurecliwindows)).
2. Run `az login` and select your **personal** subscription.
3. Create RG `rg-day02-lab` via CLI.
4. Create a second empty RG once via Portal — compare clicks vs one command.
5. List RGs, then delete lab RGs (`--no-wait` is fine).

## Commands / code

```bash
# Install: https://aka.ms/installazurecliwindows
az login
az account set --subscription "<your-subscription-name-or-id>"
az group create --name rg-day02-lab --location centralindia
az group show --name rg-day02-lab --output jsonc
az group list --output table
az group delete --name rg-day02-lab --yes --no-wait
```

## LinkedIn post (copy-paste)

**Important:** After pasting into LinkedIn, press Enter between sections so it does not become one giant paragraph (Day 1 lesson).

```
Day 2 of #100DaysOfAzureDevOps

Three ways to talk to Azure.
Same cloud. Very different vibes.

1) Azure Portal
The tourist map.
Click. Search. Click again.
Perfect when you are learning…
dangerous when you are doing the same click 40 times on a Friday.

2) Azure CLI (az)
GPS with coordinates.
One command. Repeatable. Scriptable.
If you can type it, you can put it in a pipeline later.

3) PowerShell
The Swiss-army knife.
Great in Windows-heavy shops, automation,
and “I need objects — not just text.”

My rule of thumb:

• Exploring something new? Portal.
• Doing it twice? CLI.
• Building a habit / pipeline? CLI or PowerShell —
  never “remember the clicks.”

Today I installed Azure CLI, ran az login,
and created a resource group without walking through 12 blades.

Naming tip that saves future-you:
rg-day02-lab beats “New Resource Group (1)” every single time.

Tomorrow: Azure Resource Manager —
the control plane behind every click and every az command.

(Document attached: Day 2 — Portal vs CLI vs PowerShell)

Lab notes + PDF:
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-02-portal-cli-powershell

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### Attach with the post (PDF handout)

- [`../days/day-02-portal-cli-powershell/handout.pdf`](../days/day-02-portal-cli-powershell/handout.pdf)

LinkedIn → **document** icon → upload PDF → title: `Day 2 — Portal vs CLI vs PowerShell (Architecture + Lab)` → paste post → publish ~10am IST.

### Posting tips

- Personal account only; no employer name; no hiring CTAs.
- Reply to Day 1 comments if any are still open.
- Leave 5–10 real comments on other Azure/DevOps posts.

## Done checklist

- [ ] Azure CLI installed + `az login` works (personal sub)
- [ ] Created and deleted (or cleaned) `rg-day02-lab`
- [ ] LinkedIn Day 2 published **with PDF attached** + line breaks intact
- [ ] Engaged with 5–10 community comments

## Tomorrow

**Day 3 — Azure Resource Manager (ARM) basics** → [`day-03.md`](./day-03.md)

---

*Personal learning guide — views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
