# Day 34 — Deployment Slots & Swap Strategies

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | 4 - Continuous Delivery |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

Staging is a dressing room. Swap is a VIP flip. F1 has no room — Standard S1+ does

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

| Piece | What it is | YAML / portal |
| --- | --- | --- |
| Production slot | The default site hostname | appName only; slot not set |
| Staging slot | Microsoft.Web/sites/slots  name staging | Portal: Deployment slots → Add  or deployToSlotOrASE |
| Swap | VIP / hostname flip; instances stay warm if you warmed them | az webapp deployment slot swap |
| Slot setting | Sticky app setting (slotSetting: true) | Does not ride the swap — connection strings, flags |
| Warm-up | applicationInitialization / hit staging URL | Swap of a cold process is a scheduled brownout |

## Step-by-step lab

1. Portal → your web app → Deployment slots. If Add is disabled, you are on F1/Basic. Record the SKU. Do not lie that you swapped.
2. If you bump: az appservice plan update --sku S1 (short window). Create slot staging. Remember S1 costs — delete same night.
3. Deploy the same drop to staging (deployToSlotOrASE + resourceName: staging). Do not rebuild.
4. Smoke the staging URL (default hostname -<slot>.azurewebsites.net). Hit it until the app is actually up.
5. az webapp deployment slot swap -g <rg> -n <app> --slot staging --target-slot production. Confirm production URL. Swap back once (rollback practice).
6. Write docs/slots-warmup-day34.md: warm-up path, sticky settings, auto-swap = off. Include 'SKU blocked slots' if it did.

## Done when

- [ ] Know F1 has no slots; S1+ does
- [ ] Warm-up path written even if SKU blocked the lab
- [ ] If you swapped: you also swapped back once
- [ ] S1 plan not left running overnight without a reason

## LinkedIn

Post draft: [`../../daily-guides/day-34.md`](../../daily-guides/day-34.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/day-34-deployment-slots-swap-strategies
```

## Next

**Day 35** — Blue-green — two worlds, one traffic pointer. On App Service that map is prod slot + staging.
