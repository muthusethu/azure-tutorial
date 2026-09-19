# Day 51 - Docker Fundamentals

| | |
|---|---|
| **Date** | 10 Oct 2026 |
| **Phase** | 6 - Containers & Kubernetes |
| **Time box** | 60-90 minutes |
| **Series** | #100DaysOfAzureDevOps |

## Goal

Finish today's topic with one small hands-on proof and one LinkedIn post. Prefer a working lab over perfect notes.

## Learn (20-30 min)

- Images, containers, Dockerfile, layer caching

## Hands-on lab (20-30 min)

1. Install Docker Desktop (personal PC)
2. Build/run a hello Dockerfile for your sample app

## Commands / code

```bash
# Dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY . .
CMD ["npm", "start"]
```

## LinkedIn post (copy-paste)

```
Containers are shipping containers for processes — same app, fewer "works on my laptop" customs checks.

Day 51 of #100DaysOfAzureDevOps. Docker fundamentals.

The laptop had Node 20, a global package, and a .env that was never committed. Production had Node 18 and no global package. Customs seized the app at the border. A Dockerfile is how you ship the process with its language, its OS slice, and its start command — not a prayer that the destination looks like your desk.

Images, containers, layers, cache. COPY package*.json before COPY . so npm ci can cache. I have seen Dockerfiles that copy the universe first and then wait five minutes on every README change. Layer cache is a design, not a miracle.

Patterns I keep seeing

1. Image vs container
• Image is the immutable snapshot
• Container is a running instance of that snapshot
• Mutating a running container and calling it "the image" is how drift gets a hoodie

2. Dockerfile order is cache order
• FROM node:20-alpine, WORKDIR, COPY package*.json, RUN npm ci --omit=dev, COPY ., CMD
• Copy source before install and every code change busts the dependency layer

3. Pin the base
• node:20-alpine is a choice
• FROM node:latest is a surprise waiting for a Tuesday

4. Local proof before registries
• Docker Desktop on the personal PC
• Build and run the hello app until localhost behaves

What I am doing in today's lab

I am installing Docker Desktop on my personal PC, writing a hello Dockerfile for the sample app, building it, running it, and noting the cache behavior when I change a line of source versus a line in package.json. ACR is tomorrow. Today the process has to ship locally.

Pack the process. Stop negotiating with the destination's personality.

Handout PDF is attached to this document post.

Lab notes + PDF: https://github.com/muthusethu/azure-tutorial/tree/main/days/day-51-docker-fundamentals

Tomorrow: Azure Container Registry — private closet for images.

#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic
```

### How to post

1. LinkedIn → **document** → upload today's `handout.pdf`
2. **Document title:** `Day 51 — Docker Fundamentals` (max 58 chars)
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

**Azure Container Registry**

---

*Personal learning guide - views are your own. Not legal advice. Keep labs on personal subscriptions and personal time.*
