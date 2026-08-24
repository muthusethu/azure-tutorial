#!/usr/bin/env python3
"""Print today's #100DaysOfAzureDevOps + #ProductionGradeAzure posting reminder."""

from __future__ import annotations

from datetime import date, timedelta

SERIES_START = date(2026, 8, 21)  # Day 1
FIELD_NOTE_DAYS = [4 + 3 * i for i in range(33)]  # 4, 7, 10, … 100
NOTE_DATES = {
    day: SERIES_START + timedelta(days=day - 1) for day in FIELD_NOTE_DAYS
}
NOTE_BY_DAY = {day: idx + 1 for idx, day in enumerate(FIELD_NOTE_DAYS)}


def series_day(for_date: date | None = None) -> int | None:
    d = for_date or date.today()
    n = (d - SERIES_START).days + 1
    if n < 1 or n > 100:
        return None
    return n


def next_field_day(after: int) -> int | None:
    for d in FIELD_NOTE_DAYS:
        if d > after:
            return d
    return None


def main() -> None:
    today = date.today()
    day = series_day(today)

    print("=" * 60)
    print("Azure posting reminder")
    print(f"Calendar date: {today.isoformat()}")
    print("=" * 60)

    if day is None:
        print("Outside the 100-day window (21 Aug – 28 Nov 2026).")
        return

    print(f"\n#100DaysOfAzureDevOps — Day {day}")
    print(f"  Guide: daily-guides/day-{day:02d}.md")
    print("  Post 1 (~10:00 IST): daily lesson (+ PDF when ready)")
    print("  Hashtags: #100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic")

    if day in FIELD_NOTE_DAYS:
        note = NOTE_BY_DAY[day]
        print(f"\n*** 2ND POST TODAY — Production track (separate post) ***")
        print(f"  #ProductionGradeAzure — note {note} of 33")
        print(f"  Copy: publish/production-grade/notes.md (Note {note})")
        print("  Post 2 (~17:00–19:00 IST): after lesson post + some engagement")
        print("  Hashtags: #ProductionGradeAzure #Azure #DevOps #CloudComputing #LearningInPublic")
        print("  Checklist: publish/production-grade/REMINDERS.md")
    else:
        nxt = next_field_day(day)
        if nxt:
            nd = NOTE_DATES[nxt]
            print(f"\nNext production post: Day {nxt} ({nd.strftime('%d %b %Y')}) — note {NOTE_BY_DAY[nxt]} of 33")

    print("\nFull schedule: publish/production-grade/REMINDERS.md")


if __name__ == "__main__":
    main()
