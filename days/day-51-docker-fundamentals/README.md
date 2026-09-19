# Day 51 — Docker Fundamentals

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 6 - Containers & Kubernetes |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Ship the process with its layers — not a prayer that prod looks like your laptop

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Object | What it is | What people confuse |
| --- | --- | --- |
| Image | Immutable filesystem layers + config, addressed by digest sha256:… | The container that happens to be running on the laptop |
| Container | A running (or stopped) instance of an image. Writable layer on top | docker commit of a mutated container as the new source of truth |
| Layer | Diff from one Dockerfile instruction. Cache key is that instruction + parents | Cache as a miracle rather than COPY/RUN order |
| Tag | Mutable pointer (myapp:day51) that can move to a new digest | :latest as a version. latest is a moving sign |
| Digest | Immutable content address. Pull by @sha256:… when you mean exactly this bits | Optional decoration. Promotion identity lives here, not on latest |

## Step-by-step lab

1. Install Docker Desktop on the personal PC (or confirm docker version already works). Do not use an employer-licensed install for this series.
2. In the sample app repo, add a Dockerfile: FROM node:20-alpine, WORKDIR /app, COPY package*.json, RUN npm ci --omit=dev, COPY ., CMD. Add a .dockerignore that excludes .env, .git, node_modules.
3. docker build -t myapp:day51 .  Note which steps show CACHED vs RUN. Touch README (or a source file) and rebuild. Touch package.json and rebuild. Write which layer busted.
4. docker run --rm -p 3000:3000 myapp:day51  Hit localhost until the process answers. docker image ls and docker inspect myapp:day51 --format '{{.Id}} {{.RepoTags}}'.
5. Write docs/docker-day51.md: image vs container in one sentence each, the cache observation, and the digest (or Image ID) you built. ACR is tomorrow — do not push yet.
6. docker image prune is optional. Do not docker commit. If the app is not Node, same order: lockfile copy, install, then source.

## Done when

- [ ] Can explain image vs container vs tag vs digest without saying the container is the image
- [ ] Dockerfile copies lockfile/manifests before source; .dockerignore exists
- [ ] Noted cache bust: source change vs package.json change
- [ ] docs/docker-day51.md on the personal repo; no employer screenshot

## LinkedIn

Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-51-docker-fundamentals
```

## Next

**Day 52** — Azure Container Registry — private closet for images
