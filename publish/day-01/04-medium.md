# Medium — Day 1 (longer narrative)

**Title:** The Cloud Responsibility Question Nobody Asks Until 2am  
**Subtitle:** IaaS, PaaS, SaaS — and the city/building map that saves outages  
**Canonical link / “Originally published”:** https://github.com/muthusethu/azure-tutorial/tree/main/days/day-01-cloud-fundamentals  

---

Most people can recite “IaaS, PaaS, SaaS” in an interview.

Fewer can answer the only question that matters in production:

**When this breaks at 2am — who is responsible?**

That is the whole shared-responsibility model, dressed up in three letters.

## Start with a restaurant (it sticks)

Imagine your application is a restaurant.

**IaaS** is renting the entire kitchen. Azure Virtual Machines live here. You still patch the OS. You still design the network. You still own backups. You get maximum control — and maximum operational load. When the soup is cold, the pager usually points at you.

**PaaS** is a shared kitchen with a manager on payroll. App Service, Functions, Azure SQL. You bring the recipe (your code and data). Microsoft keeps the ovens running. You still own the dish that reaches the customer: identity, app bugs, cost surprises.

**SaaS** is takeout. Microsoft 365. GitHub. You configure. You consume. You do not build the kitchen — and you should not pretend you did.

The mistake is treating these as morality rankings (“real engineers use IaaS”). They are trade-offs. Pick the model that matches the blast radius you are willing to own.

## Then look at the map

Cloud diagrams forget geography until latency or compliance shows up angry.

A **region** is a city on the map. Central India is not East US. Different customers, different laws, different round-trips.

An **availability zone** is a different building in that same city — separate power and networking. Spreading a workload across zones is how you survive a building failure without failing over to another country.

If you remember nothing else from Day 1 of my public Azure DevOps series:

**Region = which city. Zone = which building. IaaS/PaaS/SaaS = who holds the spatula.**

## A small personal lab

I am documenting 100 days of Azure DevOps learning in public — personal subscription, personal time, educational posts only.

Day 1 lab is intentionally boring on purpose:

1. Confirm personal Azure access  
2. Set a budget alert  
3. Create `rg-day01-lab`  
4. Optionally run:

```bash
az account show --output table
az group create --name rg-day01-lab --location centralindia
```

PDF handout with architecture tables:  
https://github.com/muthusethu/azure-tutorial/blob/main/days/day-01-cloud-fundamentals/handout.pdf

## Tomorrow

Portal vs CLI vs PowerShell — three ways to talk to Azure, and why clicking alone will not save you when the task repeats.

If this framing helped, the series lives here:  
https://github.com/muthusethu/azure-tutorial

---

*Views are my own.*
