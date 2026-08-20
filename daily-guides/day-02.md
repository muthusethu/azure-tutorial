# Day 2 - Azure Portal, CLI & PowerShell Basics

| | |
|---|---|
| **Date** | 22 Aug 2026 |
| **Phase** | 1 - Azure & DevOps Foundations |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- When to use Portal vs CLI vs PowerShell
- Install Azure CLI; sign-in with `az login`
- Resource groups, subscriptions, naming conventions (rg-, app-, pip-)
- Docs: https://learn.microsoft.com/cli/azure/install-azure-cli

## Hands-on lab (20-30 min)

1. Install Azure CLI on your personal PC
2. Run `az login` and select personal subscription
3. Create RG `rg-day02-lab` via CLI
4. Create the same RG shape via Portal once (compare clicks vs commands)
5. List and delete the RG (or leave empty and delete tomorrow)

## Commands / code

```bash
# Install: https://aka.ms/installazurecliwindows
az login
az account set --subscription "<your-subscription-name-or-id>"
az group create --name rg-day02-lab --location centralindia
az group show --name rg-day02-lab --output jsonc
az group delete --name rg-day02-lab --yes --no-wait
```

## LinkedIn post (copy-paste)

```
Day 2 of #100DaysOfAzureDevOps

Three ways to talk to Azure. Same cloud. Very different vibes.

1) Azure Portal
The tourist map.
Click. Search. Click again.
Perfect when you are learning… dangerous when you are doing the same click 40 times on a Friday.

2) Azure CLI (az)
GPS with coordinates.
One command. Repeatable. Scriptable.
If you can type it, you can put it in a pipeline later.

3) PowerShell
The Swiss-army knife.
Great in Windows-heavy shops, automation, and “I need objects not just text.”

My rule of thumb:

- Exploring something new? Portal.
- Doing it twice? CLI.
- Building a habit / pipeline? CLI or PowerShell — never “remember the clicks.”

Today I installed Azure CLI, ran az login, and created a resource group without clicking through 12 blades.

Naming tip that saves future-you:
rg-day02-lab beats “New Resource Group (1)” every single time.

Tomorrow: Azure Resource Manager —
the control plane behind every click and every az command.

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

**Azure Resource Manager (ARM) basics**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
