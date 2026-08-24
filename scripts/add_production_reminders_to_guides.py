#!/usr/bin/env python3
"""Add a 2nd-post reminder block to daily-guides on production-grade days."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUIDES = ROOT / "daily-guides"
FIELD_DAYS = [4 + 3 * i for i in range(33)]
NOTE_BY_DAY = {d: i + 1 for i, d in enumerate(FIELD_DAYS)}

MARKER = "## Reminder — 2nd LinkedIn post (production track)"
BLOCK_RE = re.compile(
    rf"{re.escape(MARKER)}.*?(?=\n## |\n---\n|\Z)",
    re.DOTALL,
)


def reminder_block(day: int) -> str:
    note = NOTE_BY_DAY[day]
    return f"""{MARKER}

**Today you publish TWO separate LinkedIn posts.** The daily lesson above is post 1 only.

| | Post 1 — #100DaysOfAzureDevOps | Post 2 — #ProductionGradeAzure |
|---|-------------------------------|----------------------------------|
| **When** | ~10:00 IST | ~17:00–19:00 IST (after some engagement on post 1) |
| **Copy** | This file — LinkedIn section | [`publish/production-grade/notes.md`](../publish/production-grade/notes.md) — Note {note} |
| **Attach** | Day PDF when ready | None (story post) |

- [ ] Post 1 — daily lesson (+ PDF)
- [ ] Post 2 — production note {note} of 33 (rewrite with your real experience)
- [ ] Record URLs in [`publish/production-grade/LINKS.md`](../publish/production-grade/LINKS.md)

Run: `python scripts/production_reminder.py`

"""


def main() -> None:
    for day in FIELD_DAYS:
        path = GUIDES / f"day-{day:02d}.md"
        if not path.exists():
            print(f"skip missing {path.name}")
            continue
        text = path.read_text(encoding="utf-8")
        block = reminder_block(day)

        if MARKER in text:
            text = BLOCK_RE.sub(block.rstrip() + "\n\n", text)
        elif "## Done checklist" in text:
            text = text.replace("## Done checklist", block + "## Done checklist", 1)
        elif "## Tomorrow" in text:
            text = text.replace("## Tomorrow", block + "## Tomorrow", 1)
        else:
            text = text.rstrip() + "\n\n" + block

        path.write_text(text, encoding="utf-8")
        print(f"updated {path.name}")


if __name__ == "__main__":
    main()
