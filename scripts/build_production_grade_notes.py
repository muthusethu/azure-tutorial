#!/usr/bin/env python3
"""Build standalone production-grade LinkedIn posts from legacy combined draft file."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "publish" / "production-field-notes.md"
OUT = ROOT / "publish" / "production-grade" / "notes.md"

CALENDAR = [
    (1, 4, "24 Aug 2026", "The sticker said DevOps. DORA said otherwise."),
    (2, 7, "27 Aug 2026", "The board that lied for two sprints"),
    (3, 10, "30 Aug 2026", "Foundations we skipped until production billed us"),
    (4, 13, "02 Sep 2026", "Default branch with no protection"),
    (5, 16, "05 Sep 2026", "The hook everyone bypassed with --no-verify"),
    (6, 19, "08 Sep 2026", "A PAT in a screenshot and a weekend of rotation"),
    (7, 22, "11 Sep 2026", "Disk full at 2:14am on the only self-hosted agent"),
    (8, 25, "14 Sep 2026", "npm install vs the lockfile — two different trees"),
    (9, 28, "17 Sep 2026", "CI green on main. CD deployed hotfix/temp."),
    (10, 31, "20 Sep 2026", "Click-ops release at midnight because YAML was not ready"),
    (11, 34, "23 Sep 2026", "Slot swap with the wrong sticky settings"),
    (12, 37, "26 Sep 2026", "Half the farm on the old binary"),
    (13, 40, "29 Sep 2026", "Approval gates that only proved someone was awake"),
    (14, 43, "02 Oct 2026", "Prod parameter file pointed at the test Key Vault"),
    (15, 46, "05 Oct 2026", "State in git, apply from a laptop, one lock"),
    (16, 49, "08 Oct 2026", "Portal just this once vs the next pipeline run"),
    (17, 52, "11 Oct 2026", "Tag latest and a rollback that was not yesterday"),
    (18, 55, "14 Oct 2026", "CrashLoopBackOff and the ritual restart"),
    (19, 58, "17 Oct 2026", "values-prod.yaml with a connection string in git history"),
    (20, 61, "20 Oct 2026", "Guest account with Owner for the vendor, temporary"),
    (21, 64, "23 Oct 2026", "Pipeline variables that were secrets for two years"),
    (22, 67, "26 Oct 2026", "continueOnError on the only gate that mattered"),
    (23, 70, "29 Oct 2026", "Service principal with Contributor on the subscription"),
    (24, 73, "01 Nov 2026", "Sampling hid the outage; the dashboard said 200 OK"),
    (25, 76, "04 Nov 2026", "A 41-minute pipeline nobody had timed on purpose"),
    (26, 79, "07 Nov 2026", "A war room with twelve people and no incident commander"),
    (27, 82, "10 Nov 2026", "Thirty YAML files, one bug, thirty copy-paste fixes"),
    (28, 85, "13 Nov 2026", "Agent online, Azure unreachable, firewall unchanged"),
    (29, 88, "16 Nov 2026", "kubectl apply then GitOps politely undeployed you"),
    (30, 91, "19 Nov 2026", "The simple pipeline that took checkout down"),
    (31, 94, "22 Nov 2026", "Ten years of work vs a green contribution graph"),
    (32, 97, "25 Nov 2026", "The question they ask vs the outage they should ask about"),
    (33, 100, "28 Nov 2026", "What 10 years taught me that 100 days made say out loud"),
]

HASHTAGS = "#ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic"


def clean_story(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Tomorrow:"):
            continue
        if stripped.startswith("(every 3 days"):
            continue
        if stripped.startswith("(Document attached"):
            continue
        if stripped == HASHTAGS or stripped.startswith("#100DaysOfAzureDevOps"):
            continue
        lines.append(line.rstrip())
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def extract_story(block: str, note_num: int) -> str:
    marker = f"Production field note {note_num} of 33"
    if marker in block:
        return clean_story(block.split(marker, 1)[1].lstrip("\n"))
    if note_num == 1 and marker.replace("field ", "") in block:
        return clean_story(block.split(marker.replace("field ", ""), 1)[1].lstrip("\n"))
    # Fallback: strip daily-series opener through first blank run
    lines = block.splitlines()
    out: list[str] = []
    skip_daily = True
    for line in lines:
        if skip_daily:
            if line.strip().startswith("---"):
                skip_daily = False
            continue
        out.append(line)
    return clean_story("\n".join(out))


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"Missing source: {SRC}")

    raw = SRC.read_text(encoding="utf-8")
    sections = re.split(r"\n## Note \d+ — ", raw)[1:]

    OUT.parent.mkdir(parents=True, exist_ok=True)

    header = f"""# Production Grade Azure — LinkedIn posts

**Separate track** from [#100DaysOfAzureDevOps](../README.md). Do **not** merge into the daily lesson post.

| | |
|---|---|
| **Cadence** | Every 3rd series day: Day 4, 7, 10, … 100 (**33 posts**) |
| **Same calendar** | Runs in parallel until the 100-day plan ends |
| **Posts per field day** | **Two** LinkedIn updates: (1) daily lesson, (2) this production note |
| **Voice** | ~10 years production — issue, what broke, fix, best practice |
| **Hashtags** | `{HASHTAGS}` |

**Before you post:** rewrite with your real incident (anonymized). No employer, client, or internal URLs.

**Reminder:** run `python scripts/production_reminder.py` each morning.

Schedule + checkboxes: [REMINDERS.md](./REMINDERS.md)

---

"""

    parts = [header]

    for (note_num, series_day, post_date, title), section in zip(CALENDAR, sections, strict=True):
        m = re.search(r"```\n(.*?)```", section, re.DOTALL)
        if not m:
            raise SystemExit(f"No code block in note {note_num}")
        story = extract_story(m.group(1), note_num)
        linked = title.lower().replace(" ", "-").replace("'", "")
        parts.append(
            f"## Note {note_num} — Day {series_day} ({post_date})\n\n"
            f"**Title:** {title}\n\n"
            f"```\n"
            f"Production note {note_num} of 33 — #ProductionGradeAzure\n\n"
            f"{title}\n\n"
            f"{story}\n\n"
            f"Best practice: name the guardrail you would add so this class of failure cannot repeat quietly.\n\n"
            f"{HASHTAGS}\n"
            f"```\n\n"
            f"---\n\n"
        )

    OUT.write_text("".join(parts), encoding="utf-8")
    print(f"Wrote {OUT} ({len(CALENDAR)} notes)")


if __name__ == "__main__":
    main()
