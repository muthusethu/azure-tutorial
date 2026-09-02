# Bitly short links (GitHub day folders)

Use these in LinkedIn posts instead of the long GitHub URL.

| Day | Bitly | Long URL |
|----:|-------|----------|
| 1 | https://bit.ly/4gQhXP9 | https://github.com/muthusethu/azure-tutorial/tree/main/days/day-01-cloud-fundamentals |
| 2 | https://bit.ly/3SqFgG2 | https://github.com/muthusethu/azure-tutorial/tree/main/days/day-02-portal-cli-powershell |
| 3 | https://bit.ly/45MtWHm | https://github.com/muthusethu/azure-tutorial/tree/main/days/day-03-arm-basics |
| 4 | https://bit.ly/45MtYyY | https://github.com/muthusethu/azure-tutorial/tree/main/days/day-04-devops-principles |
| 5 | https://bit.ly/4giLVv7 | https://github.com/muthusethu/azure-tutorial/tree/main/days/day-05-azure-devops-services |
| 6 | https://bit.ly/4ivofF7 | https://github.com/muthusethu/azure-tutorial/tree/main/days/day-06-azure-devops-org |
| 7 | https://bit.ly/45RGZXX | https://github.com/muthusethu/azure-tutorial/tree/main/days/day-07-azure-boards |
| 8 | https://bit.ly/4zHsGD3 | https://github.com/muthusethu/azure-tutorial/tree/main/days/day-08-azure-test-plans |
| 9 | https://bit.ly/4xDxqIc | https://github.com/muthusethu/azure-tutorial/tree/main/days/day-09-azure-artifacts |
| 10 | https://bit.ly/4gDGA05 | https://github.com/muthusethu/azure-tutorial/tree/main/days/day-10-phase-1-recap |
| 11 | https://bit.ly/45WLoJm | https://github.com/muthusethu/azure-tutorial/tree/main/days/day-11-git-fundamentals |
| 12 | https://bit.ly/46xX1GJ | https://github.com/muthusethu/azure-tutorial/tree/main/days/day-12-branching-strategies |
| 13 | https://bit.ly/4xyn8cz | https://github.com/muthusethu/azure-tutorial/tree/main/days/day-13-azure-repos-setup |

**Going forward:** after each new `days/day-NN-*/` folder is on `main`, run:

```bash
python scripts/bitly_shorten.py "https://github.com/muthusethu/azure-tutorial/tree/main/days/day-NN-slug" "Day NN title"
```

Paste the Bitly URL into that day’s LinkedIn post and `publish/day-NN/LINKS.md`.

Token: local `.env` only (`BITLY_ACCESS_TOKEN`). Copy from `.env.example`. Never commit `.env`.
