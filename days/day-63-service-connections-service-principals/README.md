# Day 63 — Service Connections & Service Principals

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 7 - Security, Compliance & Governance |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

The Entra app is the identity; the Azure DevOps service connection is the badge that uses it

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Object | Where it lives | Job |
| --- | --- | --- |
| App registration | Entra (Day 61). Client ID | Application identity. May hold federated credentials or a secret |
| Service principal | Entra enterprise app in the tenant | What Azure RBAC is assigned to (Contributor on one RG) |
| Service connection | Azure DevOps Project Settings | How a pipeline job gets a token to call Azure. Not an Entra blade |
| Client secret auth | Password on the app. Stored by ADO | Long-lived. Expires at 2am. Postcard with a delayed explosion |
| Workload identity federation | Federated credential on the app: issuer vstoken.dev.azure.com, subject sc://org/project/name | ADO presents a token; Entra trusts it. No secret in a drawer |

## Step-by-step lab

1. Project Settings → Service connections → New → Azure Resource Manager. Choose Workload identity federation (automatic is OK). Name lab-sc. Subscription = personal.
2. Open the connection → Manage Service Principal (or Entra). Note appId. This is the registration/SP. The connection object stays in ADO — two places, not one.
3. In Azure: az role assignment list --assignee <appId>. If you see Owner at subscription, treat it as a finding. az role assignment create Contributor on rg-day63 and remove Owner if you can.
4. If the UI created a client secret instead of WIF, delete that secret after switching to federated credential (Certificates & secrets → Federated credentials). Issuer https://vstoken.dev.azure.com/<org>.
5. Queue a trivial pipeline job that uses azureSubscription: lab-sc (AzureCLI@2 az group list). Prove the robot works without your user password.
6. Write docs/sc-day63.md: connection name, appId, roles, WIF vs secret. One connection per environment is the habit; today you have lab only.

## Done when

- [ ] Can separate app registration, service principal, and service connection in one breath
- [ ] lab-sc uses WIF (or you documented why not)
- [ ] Robot is not Owner on the subscription
- [ ] A pipeline job actually used the connection

## LinkedIn

Post draft: [`../../daily-guides/day-63.md`](../../daily-guides/day-63.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-63-service-connections-service-principals
```

## Next

**Day 64** — Azure Key Vault — hotel safe, not a postcard in git
