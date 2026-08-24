# 100 Days of Azure DevOps

Personal learning-in-public series: **one Azure / DevOps topic per day**, with a short lab and a downloadable PDF handout (architecture + step-by-step).

**Parallel track:** [#ProductionGradeAzure](./publish/production-grade/) — production issues, fixes, and best practices every **3rd series day** (33 posts). **Two separate LinkedIn posts** on those days; the daily lesson plan is unchanged.

> Educational content only. Personal labs on a personal Azure subscription. Views are my own. Not affiliated with any employer. Not a course product and not a sales pitch.

**LinkedIn series:** `#100DaysOfAzureDevOps`  
**Hashtags (daily posts):** `#100DaysOfAzureDevOps` `#Azure` `#DevOps` `#CloudComputing` `#LearningInPublic`

**Production track (separate posts):** `#ProductionGradeAzure` — see [`publish/production-grade/`](./publish/production-grade/)

---

## What is in this repo?

| Path | Purpose |
|------|---------|
| [`days/`](./days) | One folder per day — guide + PDF handout (share these) |
| [`daily-guides/`](./daily-guides) | Full markdown guides (learn, lab, LinkedIn draft, checklist) |
| [`scripts/`](./scripts) | Helpers to generate guides / PDFs (optional for readers) |
| [`publish/production-grade/`](./publish/production-grade/) | Separate production track (every 3rd day, 2nd LinkedIn post) |
| [`docs/`](./docs) | Repo policy notes |

You do **not** need to clone this repo to follow along. Open the day folder, read the guide, download the PDF.

---

## Folder structure

```text
azure-tutorial/
├── README.md                          ← you are here
├── LICENSE
├── days/
│   ├── README.md                      ← day index
│   ├── day-01-cloud-fundamentals/
│   │   ├── README.md                  ← day overview + lab
│   │   └── handout.pdf                ← LinkedIn document / study PDF
│   ├── day-02-portal-cli-powershell/
│   │   ├── README.md
│   │   └── handout.pdf
│   └── ...
├── daily-guides/
│   ├── README.md
│   └── day-01.md ... day-100.md       ← full daily playbooks
├── docs/
└── scripts/                           ← generators (maintainers)
```
**Naming rule for each day folder**

```text
days/day-NN-short-slug/
  README.md      # what to learn + lab steps
  handout.pdf    # architecture + step-by-step (share on LinkedIn)
```

---

## How to follow (learners)

1. Open today’s folder under [`days/`](./days).
2. Read `README.md` (concepts + lab).
3. Download `handout.pdf` for the architecture diagram and checklist.
4. Use a **personal** Azure account / subscription for labs.
5. Optional: watch the LinkedIn post the same day for the short “story” version.

### Cost tip

Create a budget alert on day 1. Delete unused resource groups when a lab is done.

---

## Day index (published)

| Day | Topic | Folder | Handout |
|-----|--------|--------|---------|
| 01 | Cloud Computing & Azure Fundamentals | [day-01-cloud-fundamentals](./days/day-01-cloud-fundamentals) | [PDF](./days/day-01-cloud-fundamentals/handout.pdf) |
| 02 | Azure Portal, CLI & PowerShell | [day-02-portal-cli-powershell](./days/day-02-portal-cli-powershell) | [PDF](./days/day-02-portal-cli-powershell/handout.pdf) |
| 03 | Azure Resource Manager (ARM) Basics | [day-03-arm-basics](./days/day-03-arm-basics) | [PDF](./days/day-03-arm-basics/handout.pdf) |
| 04 | DevOps Principles & Culture | [day-04-devops-principles](./days/day-04-devops-principles) | [PDF](./days/day-04-devops-principles/handout.pdf) |

More days will appear here as the series continues (target: 100 days).

### Roadmap (high level)

1. **Days 1–10** — Azure & DevOps foundations  
2. **Days 11–20** — Git & Azure Repos  
3. **Days 21–40** — CI/CD with Azure Pipelines  
4. **Days 41–60** — IaC & containers  
5. **Days 61–80** — Security & observability  
6. **Days 81–100** — Advanced topics + public portfolio polish  

---

## LinkedIn + GitHub workflow (author)

For each day:

1. Write / update `daily-guides/day-NN.md` (post text + lab).
2. Generate or place `handout.pdf` in `days/day-NN-.../`.
3. Copy platform variants from `publish/day-NN/` (X, Dev.to, Reddit, etc.).
4. Push to this repo.
5. On LinkedIn: upload the PDF as a **document**, paste the post, use the standard hashtags.
6. Optional link in the post:

```text
Handout + lab notes: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-01-cloud-fundamentals
```

Cross-post guide: [`publish/README.md`](./publish/README.md)
---

## Disclaimer

- Labs are generic samples from public Microsoft docs and personal experiments.
- No employer systems, client data, or internal tooling.
- This repository is for learning and portfolio demonstration only.

## License

Content and sample labs: [MIT](./LICENSE).  
Microsoft product names are trademarks of their respective owners. Azure documentation links point to [Microsoft Learn](https://learn.microsoft.com/).
