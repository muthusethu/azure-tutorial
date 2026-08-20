# Reddit — Day 1

**Subreddits (pick one first):** r/AZURE → then maybe r/devops  
**Avoid on Day 1:** r/ExperiencedDevs (save for deeper posts later)  

**Title options (no series branding in title):**
- IaaS vs PaaS vs SaaS explained with a restaurant metaphor (and where Regions/AZs fit)
- ELI5: Region vs Availability Zone in Azure

**Body rules:** no hashtags, no “follow my series,” no PDF hard-sell. Soft GitHub link at the end is OK if the post stands alone.

---

Imagine your app is a restaurant. That framing fixed IaaS/PaaS/SaaS for me more than any slide deck.

**IaaS** — you rent the whole kitchen. You still patch the OS, own the runtime, and get paged when the soup is cold. In Azure-land that's VMs. Max control, max operational load.

**PaaS** — shared kitchen with a manager. You cook; they keep the ovens alive. App Service / Functions / Azure SQL. You still own the dish (app, identity, data, cost).

**SaaS** — takeout. M365, GitHub. You configure and consume. You don't build the kitchen.

The part people skip is geography:

- **Region** = city (Central India ≠ East US — latency + residency)
- **Availability Zone** = different building in that city (own power/network). Building A floods, Building B can still serve lunch.

One-liner I keep:

`Region = city | Zone = building | IaaS/PaaS/SaaS = who holds the spatula`

Curious how others explain shared responsibility to juniors — metaphors that worked for you?

(Notes/diagrams I used while learning: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-01-cloud-fundamentals )
