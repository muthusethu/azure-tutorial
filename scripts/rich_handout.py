# -*- coding: utf-8 -*-
"""Render 2–3 page architecture handouts from SPECS dicts."""
from __future__ import annotations

import sys
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    HRFlowable,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from generate_handout_pdfs import (  # noqa: E402
    DAYS,
    LIGHT,
    LINE,
    NAVY,
    OUT,
    PUBLISH_MAP,
    SERIES_TAGS,
    TEAL,
    bullets,
    code_html,
    curriculum,
    folder_slug,
    header_bar,
    numbered,
    section_box,
    styles,
)

ROOT = Path(__file__).resolve().parents[1]


def _cell(text: str) -> str:
    # Always escape. Specs often contain YAML like <sub> or <image> which
    # reportlab would parse as HTML tags.
    return escape(text or "").replace("\n", "<br/>")


def build_from_spec(path: Path, day: int, spec: dict) -> None:
    s = styles()
    topic = spec["topic"]
    subtitle = spec.get("subtitle") or f"Architecture, decision table, and a lab you can finish today"
    phase = spec.get("phase") or ""
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=14 * mm,
        rightMargin=14 * mm,
        topMargin=10 * mm,
        bottomMargin=10 * mm,
        title=f"Day {day} — {topic} | 100DaysOfAzureDevOps",
        author="Personal learning series",
    )
    story = []
    cover_title = ParagraphStyle(
        f"cover_title_{day}",
        parent=s["cover_title"],
        fontSize=15,
        leading=19,
        spaceAfter=4,
    )
    story.append(header_bar(day, topic))
    story.append(Spacer(1, 8))
    story.append(Paragraph("100 Days of Azure DevOps", s["cover_sub"]))
    story.append(Paragraph(_cell(f"Day {day} Handout — {subtitle}"), cover_title))
    story.append(Paragraph(
        _cell(f"{phase} · Personal lab only · Educational content · Not a sales pitch"),
        s["cover_sub"],
    ))
    story.append(Spacer(1, 2))
    story.append(HRFlowable(width="100%", thickness=1, color=TEAL, spaceAfter=6))

    for table in spec.get("tables") or []:
        headers = table["columns"]
        rows = [_cell(c) for c in headers]
        data = [rows]
        for row in table["rows"]:
            data.append([_cell(c) for c in row])
        widths = [w * mm for w in table.get("widths") or [180 / len(headers)] * len(headers)]
        story.append(section_box(table["title"], data, col_widths=widths))
        story.append(Spacer(1, 3))

    one = spec.get("one_liner") or ""
    if one:
        story.append(Paragraph("One-liner to remember", s["h1"]))
        box = Table([[Paragraph(
            f"<b>{_cell(one)}</b>",
            ParagraphStyle(
                f"ol{day}",
                fontName="Helvetica",
                fontSize=9,
                leading=12,
                textColor=NAVY,
                alignment=TA_CENTER,
            ),
        )]], colWidths=[182 * mm])
        box.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FEF3C7")),
            ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#D97706")),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ("LEFTPADDING", (0, 0), (-1, -1), 6),
            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ]))
        story.append(box)

    lab = spec.get("lab") or []
    if lab:
        story.append(Paragraph("Step-by-step lab (personal Azure / Azure DevOps only)", s["h1"]))
        intro = spec.get("lab_intro")
        if intro:
            story.append(Paragraph(_cell(intro), s["body"]))
        story.append(numbered([_cell(x) for x in lab]))

    code = (spec.get("code") or "").strip()
    if code:
        story.append(Paragraph(spec.get("code_title") or "Starter snippet", s["h1"]))
        cmd = Table(
            [[Paragraph(code_html(code), s["body"])]],
            colWidths=[182 * mm],
        )
        cmd.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), LIGHT),
            ("BOX", (0, 0), (-1, -1), 0.6, LINE),
            ("LEFTPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ]))
        story.append(cmd)

    checks = spec.get("checklist") or [
        "Finished the lab on a personal subscription / org",
        "Posted the LinkedIn lesson (personal account, no employer)",
        "Deleted spare lab resources if they cost money",
    ]
    story.append(Paragraph("Done checklist", s["h1"]))
    story.append(bullets([_cell(x) for x in checks]))

    nxt = spec.get("tomorrow") or ""
    if day < 100:
        story.append(Paragraph(f"Tomorrow — Day {day + 1}", s["h2"]))
    else:
        story.append(Paragraph("After Day 100", s["h2"]))
    if nxt:
        story.append(Paragraph(_cell(nxt), s["body"]))

    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=0.6, color=LINE, spaceAfter=4))
    story.append(Paragraph(
        "Personal learning handout · Views are my own · Not affiliated with any employer · Not legal advice",
        s["footer"],
    ))
    story.append(Paragraph(SERIES_TAGS, s["footer"]))
    path.parent.mkdir(parents=True, exist_ok=True)
    doc.build(story)


def write_readme(folder: Path, day: int, spec: dict, slug: str) -> None:
    topic = spec["topic"]
    nxt = spec.get("tomorrow") or ""
    tables = spec.get("tables") or []
    arch_lines = []
    if tables:
        t0 = tables[0]
        cols = t0["columns"]
        arch_lines.append("| " + " | ".join(cols) + " |")
        arch_lines.append("| " + " | ".join("---" for _ in cols) + " |")
        for row in t0["rows"][:6]:
            clean = [c.replace("<br/>", " ").replace("&nbsp;", " ") for c in row]
            arch_lines.append("| " + " | ".join(clean) + " |")
    lab = "\n".join(f"{i}. {x}" for i, x in enumerate(spec.get("lab") or [], 1))
    text = f"""# Day {day} — {topic}

| | |
|---|---|
| **Series** | [#100DaysOfAzureDevOps](https://github.com/muthusethu/azure-tutorial) |
| **Phase** | {spec.get("phase", "")} |
| **Time box** | 60–90 minutes |
| **Handout** | [handout.pdf](./handout.pdf) |

## Goal

{spec.get("subtitle") or topic}

## Architecture (summary)

Open **[handout.pdf](./handout.pdf)** for the full tables.

{chr(10).join(arch_lines)}

## Step-by-step lab

{lab}

## Done when

{chr(10).join(f"- [ ] {c}" for c in (spec.get("checklist") or [])[:5])}

## LinkedIn

Post draft: [`../../daily-guides/day-{day:02d}.md`](../../daily-guides/day-{day:02d}.md)  
Attach **[handout.pdf](./handout.pdf)**.

```
https://github.com/muthusethu/azure-tutorial/tree/main/days/{slug}
```

## Next

**Day {day + 1}** — {nxt}
"""
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "README.md").write_text(text, encoding="utf-8")


def load_all_specs() -> dict[int, dict]:
    from handout_specs import load_specs

    return load_specs()


def main(days=None) -> None:
    specs = load_all_specs()
    missing = [d for d in range(1, 101) if d not in specs]
    if missing:
        raise SystemExit(f"Missing specs for days: {missing}")
    guide = curriculum()
    for day, spec in guide.items():
        if day not in PUBLISH_MAP:
            PUBLISH_MAP[day] = DAYS / folder_slug(day, spec["topic"]) / "handout.pdf"

    if days is None:
        days = list(range(1, 101))

    OUT.mkdir(parents=True, exist_ok=True)
    DAYS.mkdir(parents=True, exist_ok=True)
    for d in days:
        spec = specs[d]
        spec.setdefault("topic", guide[d]["topic"])
        spec.setdefault("phase", guide[d]["phase"])
        spec.setdefault("tomorrow", guide[d]["tomorrow"])
        scratch = OUT / f"day-{d:02d}-handout.pdf"
        try:
            build_from_spec(scratch, d, spec)
        except Exception as exc:
            raise SystemExit(f"Day {d} failed: {exc}") from exc
        pub = PUBLISH_MAP[d]
        pub.parent.mkdir(parents=True, exist_ok=True)
        pub.write_bytes(scratch.read_bytes())
        write_readme(pub.parent, d, spec, pub.parent.name)
        print("Wrote", pub)

    from generate_handout_pdfs import rewrite_days_index

    rewrite_days_index(guide)
    print("done", len(days), "pdfs")


if __name__ == "__main__":
    args = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else None
    main(args or None)
