# Day 61 — Azure AD (Entra ID) Fundamentals

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 7 - Security, Compliance & Governance |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

If the bouncer list is wrong, RBAC and Key Vault are cosplay

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Object | What it is | Not the same as |
| --- | --- | --- |
| Tenant / directory | The Entra boundary. Personal vs work — labs stay personal | A subscription. A sub lives in a tenant; they are not synonyms |
| User / group | Human identities. Groups are how assignments should scale | An app registration. Apps are not users with a funny name |
| App registration | Application object. Client ID (appId). Lives in the home tenant | An Azure DevOps service connection (Day 63). That is an ADO badge that may use this app |
| Service principal | The instance of that app in a tenant (enterprise app). What RBAC is assigned to | The client secret. Secret is a credential on the app, not the SP itself |
| Client ID vs secret | ID is public-ish. Secret is a password. Cert/WIF later | Pasting a secret into YAML 'just for the lab' |

## Step-by-step lab

1. Portal → Microsoft Entra ID (personal directory). Note tenant ID. az account show --query tenantId. If it is a work tenant, stop and switch.
2. Entra ID → App registrations → New registration → name day61-lab. Supported account types: this org only. Redirect URI: skip. Register.
3. Copy Application (client) ID and Directory (tenant) ID into docs/entra-day61.md. Not into azure-pipelines.yml.
4. Open Certificates & secrets. Do not create a client secret today. Read that secrets would live here, and that Day 63 prefers federated credentials instead.
5. Enterprise applications: find day61-lab — that object is the service principal. One sentence in the doc: registration vs SP vs (later) service connection.
6. No LinkedIn screenshot of secrets, tenant gossip, or work users. Optional CLI: az ad app create --display-name day61-lab --query appId -o tsv.

## Done when

- [ ] day61-lab exists in the personal tenant; tenant ID and appId recorded
- [ ] Can explain tenant vs user vs app registration vs service principal
- [ ] No client secret created; none in Git
- [ ] Knows a service connection is an Azure DevOps object (Day 63), not this blade

## LinkedIn

Post draft: [`../../daily-guides/day-61.md`](../../daily-guides/day-61.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-61-azure-ad-entra-id-fundamentals
```

## Next

**Day 62** — RBAC deep dive — Owner is a flamethrower; scope is the verb
