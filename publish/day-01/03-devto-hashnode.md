# Dev.to / Hashnode — Day 1 article

**Title:** Your App Is a Restaurant: IaaS vs PaaS vs SaaS (and Why Regions Matter)

**Tags (Dev.to):** `azure`, `devops`, `cloud`, `beginners`  
**Tags (Hashnode):** Azure, DevOps, Cloud Computing  

**Canonical URL (set in both platforms):**  
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-01-cloud-fundamentals  

---

Copy below the line into the editor:

---

I'm doing **100 days of Azure DevOps** in public. Day 1 is the foundation everyone thinks they know — until an outage asks who gets paged.

## Your app is a restaurant

### IaaS — rent the whole kitchen
You buy the stove, hire the chef, clean the grease trap, and still get yelled at when the soup is cold.

**Azure example:** Virtual Machines  
**You own:** OS, patching, runtime, app  
**Vendor owns:** hardware / hypervisor

Maximum control. Maximum "why is this on fire."

### PaaS — shared kitchen with a manager
You cook. They fix the oven and pay for electricity.

**Azure examples:** App Service, Azure Functions, Azure SQL  
**You own:** app + data + identity  
**Vendor owns:** OS and platform

### SaaS — order takeout
You tap "biryani" and complain about delivery time.

**Examples:** Microsoft 365, GitHub  
**You:** configure and consume  
**You don't:** build the kitchen

## The map people skip

| Concept | Meaning | Metaphor |
|--------|---------|----------|
| **Region** | Set of datacenters in a geography | City |
| **Availability Zone** | Separate datacenter in that region | Different building, same city |

If Building A floods, Building B can still serve lunch. That is zone redundancy — not "pray and redeploy."

## One-liner

> **Region = city · Zone = building · IaaS/PaaS/SaaS = who holds the spatula**

## Tiny lab (personal subscription only)

```bash
az account show --output table
az group create --name rg-day01-lab --location centralindia
az group list --output table
```

Also: create a **budget alert** on day one. Empty curiosity still generates bills later.

## Handout

Architecture diagrams + step-by-step checklist (PDF):  
https://github.com/muthusethu/azure-tutorial/blob/main/days/day-01-cloud-fundamentals/handout.pdf

Series repo:  
https://github.com/muthusethu/azure-tutorial

Tomorrow: Portal vs CLI vs PowerShell — when to click, when to script.

---

*Personal learning notes. Views are my own. Not affiliated with any employer.*
