# Day 45 - Bicep Modules & Deployment

| | |
|---|---|
| **Date** | 04 Oct 2026 |
| **Phase** | 5 - Infrastructure as Code |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Modules, what-if, deployment stacks

## Hands-on lab (20-30 min)

1. Run `az deployment group what-if`
2. Split storage into a module

## Commands / code

```bash
az deployment group what-if -g rg-day45 -f main.bicep
```

## LinkedIn post (copy-paste)

```
what-if is a dress rehearsal — read the diff before the audience (prod) arrives.

Day 45 of #100DaysOfAzureDevOps. Bicep modules and deployment.

A module is how Bicep stops being a 2,000-line main.bicep that nobody dares touch. Split storage into a module. Call it from main. what-if is the rehearsal: az deployment group what-if shows Create/Ignore/Modify/Delete before you let the audience in.

I have seen production applies where nobody ran plan or what-if because "it is only a SKU change." The diff included a recreate. Dress rehearsal exists for that sentence.

Patterns I keep seeing

1. Modules are boundaries
• Storage module takes name prefix / SKU as params
• Main composes modules; it does not inline every resource forever

2. what-if is mandatory manners
• az deployment group what-if -g rg-day45 -f main.bicep
• Read Modify and Delete like they are incidents that have not happened yet

3. Deployment stacks are the grown-up cleanup story
• Literacy: stacks can track and prune
• Lab: one what-if, one module split, one real deploy if this is my track

4. A diff you did not read still applies
• CI can print what-if
• Humans still have to look. Automation without eyes is a faster rumor

What I am doing in today's lab

I am running az deployment group what-if against main.bicep, splitting storage into a module, and only then deploying. If the what-if shows a Delete I did not expect, I stop. The audience is not invited to surprises.

Read the diff. Prod is a terrible place to learn you recreated a disk.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-45-bicep-modules-deployment

Tomorrow: Terraform basics — init, plan, apply, destroy, and state as memory.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 45 — Bicep Modules & Deployment` (max 58 chars)
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

**Terraform basics**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
