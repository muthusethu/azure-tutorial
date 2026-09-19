# -*- coding: utf-8 -*-
"""Build the #100DaysOfAzureDevOps LinkedIn track playbook (Days 22–51)."""

from __future__ import annotations

import re
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUIDES = ROOT / "daily-guides"
OUT = ROOT / "publish" / "100-days-linkedin-track.md"

START = date(2026, 9, 19)
FIRST_DAY = 22
LAST_DAY = 51  # 19 Sep through 18 Oct inclusive


def extract_post(n: int) -> tuple[str, str]:
    text = (GUIDES / f"day-{n:02d}.md").read_text(encoding="utf-8")
    title = text.splitlines()[0].lstrip("# ").strip()
    marker = "## LinkedIn post (copy-paste)"
    i = text.find(marker)
    if i < 0:
        raise SystemExit(f"No LinkedIn section in day-{n:02d}.md")
    rest = text[i + len(marker) :]
    start = rest.find("```")
    end = rest.find("```", start + 3)
    post = rest[start + 3 : end].strip()
    return title, post


def main() -> None:
    rows = []
    sections = []
    for n in range(FIRST_DAY, LAST_DAY + 1):
        d = START + timedelta(days=n - FIRST_DAY)
        title, post = extract_post(n)
        topic = re.sub(r"^Day \d+\s*[-—]\s*", "", title)
        rows.append(
            f"| {d.strftime('%a %d %b')} | Day {n} | {topic} | [day-{n:02d}.md](../daily-guides/day-{n:02d}.md) |"
        )
        sections.append(
            f"## Day {n} — {d.strftime('%a %d %b %Y')} — {topic}\n\n"
            f"Guide: [`daily-guides/day-{n:02d}.md`](../daily-guides/day-{n:02d}.md)  \n"
            f"PDF: attach `days/day-{n:02d}-*/handout.pdf` if that folder exists. "
            f"If not, post text only and link the GitHub guide.\n\n"
            f"```\n{post}\n```\n"
        )

    header = f"""# Track A — #100DaysOfAzureDevOps LinkedIn

**Separate from** the ItsCloudHub client posts (Track B) and the company page (Track C).

| | Track A (this file) | Track B | Track C |
|---|---|---|---|
| Identity | Personal profile | Personal profile | ItsCloudHub company page |
| Series | `#100DaysOfAzureDevOps` | Consulting / problem-solving | Practice methodology |
| Cadence | **Every day**, including weekends | Mon–Fri only | Mon / Wed / Fri |
| Time (IST) | **07:00** | **19:15** | **19:40** |
| Format | Lesson + optional PDF | Problem → diagnose → takeaway | We / the practice |
| Sell | **Never.** No Health Check. No website CTA. | Rare, natural ItsCloudHub mention | Soft offer from week 3 |
| Copy | This file | `ItsCloudHub_LinkedIn_30_Day_Playbook.md` | Same playbook, C1–C12 |

Last published lesson: **Day 21** (10 Sep). Days 22–30 were not posted. This track **resumes at Day 22 on Saturday 19 Sep 2026**. It does not jump to Day 31 to match the old calendar. Dates inside `daily-guides/day-XX.md` are stale; **use the dates below**.

Window: **19 Sep → 18 Oct 2026** = Days **22–51** (30 posts). Then continue Day 52 on 19 Oct.

Production-grade extras (`#ProductionGradeAzure`) stay paused in this window. Track B already fills that voice.

IBM: personal account, personal time, personal Azure. No employer, no clients, no IBM laptop.

---

## How to post (every morning)

1. 07:00 IST — copy today’s block. Personal profile only.
2. Hashtags stay exactly: `#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic`
3. Attach the day PDF when the `days/day-NN-*` folder exists. Through Day 21 those exist. From Day 22, post text if the PDF is not ready yet.
4. Do **not** tag ItsCloudHub. Do **not** post this series on the company page.
5. Tick the tracker: [`100-days-linkedin-tracker.csv`](./100-days-linkedin-tracker.csv)
6. Lab + comments can wait until evening. The LinkedIn lesson goes out at 07:00 even if the lab is unfinished — then finish the lab the same day.

Weekday after that: Track B at 19:15 (and Track C at 19:40 if Mon/Wed/Fri). Do not swap the two posts. Morning = student series. Evening = engineer who can help a company.

---

## Calendar (shifted)

| Date | Day | Topic | Guide |
|---|---|---|---|
"""

    footer = """
---

## After 18 Oct

**19 Oct = Day 52** (Azure Container Registry). Keep daily posting. Rebuild `days/day-NN-*/` folders and PDFs when you can; do not block the morning post on a missing PDF.

Full original topic list: [`../daily-guides/README.md`](../daily-guides/README.md).

---

# Copy-paste posts

"""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(header + "\n".join(rows) + "\n" + footer + "\n".join(sections), encoding="utf-8")
    print(f"Wrote {OUT} ({LAST_DAY - FIRST_DAY + 1} days)")


if __name__ == "__main__":
    main()
