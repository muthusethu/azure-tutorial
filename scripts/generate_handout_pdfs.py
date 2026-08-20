# -*- coding: utf-8 -*-
"""Generate LinkedIn-ready PDF handouts for each #100DaysOfAzureDevOps day."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
# Scratch output (gitignored). Published PDFs live under days/day-NN-*/handout.pdf
OUT = ROOT / "daily-guides" / "handouts"
DAYS = ROOT / "days"

# Brand-ish flat palette (no purple gradients)
NAVY = colors.HexColor("#0F2744")
TEAL = colors.HexColor("#0E7490")
SLATE = colors.HexColor("#334155")
LIGHT = colors.HexColor("#F1F5F9")
LINE = colors.HexColor("#CBD5E1")
WHITE = colors.white
ACCENT = colors.HexColor("#0369A1")

SERIES_TAGS = "#100DaysOfAzureDevOps #Azure #DevOps #CloudComputing #LearningInPublic"


def styles():
    base = getSampleStyleSheet()
    return {
        "cover_title": ParagraphStyle(
            "cover_title",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=22,
            leading=26,
            textColor=NAVY,
            alignment=TA_CENTER,
            spaceAfter=6,
        ),
        "cover_sub": ParagraphStyle(
            "cover_sub",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=11,
            leading=14,
            textColor=SLATE,
            alignment=TA_CENTER,
            spaceAfter=4,
        ),
        "h1": ParagraphStyle(
            "h1",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=18,
            textColor=NAVY,
            spaceBefore=10,
            spaceAfter=8,
        ),
        "h2": ParagraphStyle(
            "h2",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=11,
            leading=14,
            textColor=TEAL,
            spaceBefore=8,
            spaceAfter=4,
        ),
        "body": ParagraphStyle(
            "body",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=13,
            textColor=SLATE,
            spaceAfter=4,
        ),
        "small": ParagraphStyle(
            "small",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8,
            leading=11,
            textColor=colors.HexColor("#64748B"),
            alignment=TA_CENTER,
        ),
        "cell": ParagraphStyle(
            "cell",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8,
            leading=10,
            textColor=SLATE,
            alignment=TA_CENTER,
        ),
        "cell_bold": ParagraphStyle(
            "cell_bold",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=8.5,
            leading=10,
            textColor=NAVY,
            alignment=TA_CENTER,
        ),
        "bullet": ParagraphStyle(
            "bullet",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=12,
            textColor=SLATE,
        ),
        "footer": ParagraphStyle(
            "footer",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=7.5,
            leading=9,
            textColor=colors.HexColor("#64748B"),
            alignment=TA_CENTER,
        ),
    }


def header_bar(day: int, title: str):
    s = styles()
    data = [[
        Paragraph(f"<b>Day {day}</b> &nbsp;|&nbsp; {title}", ParagraphStyle(
            "hb", fontName="Helvetica", fontSize=9, textColor=WHITE, leading=12
        )),
        Paragraph("#100DaysOfAzureDevOps", ParagraphStyle(
            "hb2", fontName="Helvetica", fontSize=8, textColor=WHITE, leading=12, alignment=2
        )),
    ]]
    t = Table(data, colWidths=[120 * mm, 60 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, -1), WHITE),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    return t


def section_box(title: str, rows_of_cells: list[list[str]], col_widths=None):
    s = styles()
    header = [Paragraph(f"<b>{c}</b>", s["cell_bold"]) for c in rows_of_cells[0]]
    body = []
    for row in rows_of_cells[1:]:
        body.append([Paragraph(c, s["cell"]) for c in row])
    data = [header] + body
    if col_widths is None:
        w = 180 * mm / len(header)
        col_widths = [w] * len(header)
    t = Table(data, colWidths=col_widths, hAlign="CENTER")
    style_cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), LIGHT),
        ("BOX", (0, 0), (-1, -1), 0.6, LINE),
        ("INNERGRID", (0, 0), (-1, -1), 0.4, LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]
    # highlight first column
    style_cmds.append(("BACKGROUND", (0, 1), (0, -1), colors.HexColor("#E0F2FE")))
    t.setStyle(TableStyle(style_cmds))
    return KeepTogether([Paragraph(title, styles()["h2"]), t, Spacer(1, 4)])


def architecture_stack():
    """IaaS / PaaS / SaaS shared responsibility diagram as tables."""
    s = styles()
    # Who manages what
    rows = [
        ["Layer", "IaaS (VM)", "PaaS (App Service)", "SaaS (M365/GitHub)"],
        ["Application / data", "You", "You", "Vendor"],
        ["Runtime / middleware", "You", "Vendor", "Vendor"],
        ["OS / patching", "You", "Vendor", "Vendor"],
        ["Virtualization / hosts", "Vendor", "Vendor", "Vendor"],
        ["Physical datacenter", "Vendor", "Vendor", "Vendor"],
        ["Azure examples", "Virtual Machines", "App Service, Functions, Azure SQL", "Microsoft 365, GitHub"],
    ]
    return section_box("Architecture A — Shared responsibility (who holds the spatula?)", rows,
                       col_widths=[38 * mm, 42 * mm, 50 * mm, 50 * mm])


def architecture_geo():
    rows = [
        ["Concept", "What it is", "Restaurant metaphor", "Why it matters"],
        ["Geography", "Area with compliance boundary", "Country / market", "Data residency rules"],
        ["Region", "Set of datacenters in a place", "City", "Latency, DR pairing"],
        ["Availability Zone", "Separate datacenter in a region", "Different building, same city", "Survive building failure"],
        ["Resource Group", "Logical folder for resources", "One kitchen project folder", "Lifecycle + cost scope"],
    ]
    return section_box("Architecture B — Azure geography map", rows,
                       col_widths=[32 * mm, 48 * mm, 50 * mm, 50 * mm])


def region_az_visual():
    s = styles()
    # Simple visual using nested tables
    inner = Table(
        [[Paragraph("<b>Zone 1</b><br/>Datacenter A", s["cell"]),
          Paragraph("<b>Zone 2</b><br/>Datacenter B", s["cell"]),
          Paragraph("<b>Zone 3</b><br/>Datacenter C", s["cell"])]],
        colWidths=[50 * mm, 50 * mm, 50 * mm],
    )
    inner.setStyle(TableStyle([
        ("BOX", (0, 0), (0, 0), 1, TEAL),
        ("BOX", (1, 0), (1, 0), 1, TEAL),
        ("BOX", (2, 0), (2, 0), 1, TEAL),
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#ECFEFF")),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ]))
    outer = Table(
        [[Paragraph("<b>Azure Region</b> (example: Central India) — the city", s["cell_bold"])],
         [inner]],
        colWidths=[160 * mm],
    )
    outer.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 1.2, NAVY),
        ("BACKGROUND", (0, 0), (0, 0), LIGHT),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ]))
    return KeepTogether([
        Paragraph("Architecture C — Region contains Availability Zones", styles()["h2"]),
        outer,
        Paragraph(
            "Put critical apps across zones in the same region for higher availability. "
            "Use a paired region for disaster recovery across cities.",
            styles()["body"],
        ),
    ])


def bullets(items: list[str]):
    s = styles()
    return ListFlowable(
        [ListItem(Paragraph(i, s["bullet"]), leftIndent=8, bulletColor=TEAL) for i in items],
        bulletType="bullet",
        start="•",
        leftIndent=12,
        bulletFontSize=9,
    )


def numbered(items: list[str]):
    s = styles()
    return ListFlowable(
        [ListItem(Paragraph(i, s["bullet"]), leftIndent=8, bulletColor=NAVY) for i in items],
        bulletType="1",
        leftIndent=16,
        bulletFontSize=9,
    )


def build_day01(path: Path):
    s = styles()
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm,
        title="Day 1 — Azure Fundamentals | 100DaysOfAzureDevOps",
        author="Personal learning series",
    )
    story = []

    # Cover
    story.append(header_bar(1, "Cloud Computing & Azure Fundamentals"))
    story.append(Spacer(1, 10))
    story.append(Paragraph("100 Days of Azure DevOps", s["cover_sub"]))
    story.append(Paragraph("Day 1 Handout — Architecture + Step-by-step Lab", s["cover_title"]))
    story.append(Paragraph(
        "Learning in public · Personal lab only · Educational content · Not a sales pitch",
        s["cover_sub"],
    ))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1, color=TEAL, spaceAfter=8))

    story.append(Paragraph("What you will understand today", s["h1"]))
    story.append(bullets([
        "<b>IaaS vs PaaS vs SaaS</b> — who is responsible when something breaks",
        "<b>Region vs Availability Zone</b> — city vs building",
        "<b>Personal Azure setup</b> — subscription, budget alert, first resource group",
    ]))

    story.append(Paragraph("High-level architecture", s["h1"]))
    story.append(architecture_stack())
    story.append(Spacer(1, 6))
    story.append(architecture_geo())
    story.append(Spacer(1, 6))
    story.append(region_az_visual())

    story.append(Paragraph("One-liner to remember", s["h1"]))
    one = Table([[Paragraph(
        "<b>Region = which city &nbsp;·&nbsp; Zone = which building &nbsp;·&nbsp; "
        "IaaS/PaaS/SaaS = who holds the spatula</b>",
        ParagraphStyle("ol", fontName="Helvetica", fontSize=10, leading=13,
                       textColor=NAVY, alignment=TA_CENTER)
    )]], colWidths=[180 * mm])
    one.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FEF3C7")),
        ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#D97706")),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(one)

    story.append(Paragraph("Step-by-step lab (20–30 min)", s["h1"]))
    story.append(Paragraph(
        "Use a <b>personal</b> Microsoft account and personal Azure subscription. "
        "Do not use employer SSO, work tenants, or work data.",
        s["body"],
    ))
    story.append(numbered([
        "Sign in at <b>portal.azure.com</b> with your personal account.",
        "Open <b>Subscriptions</b> → note your subscription <b>name</b> and <b>ID</b>.",
        "Open <b>Cost Management + Billing</b> → Budgets → create a budget alert "
        "(example: Rs 500 or $20) with email to yourself.",
        "Create a Resource Group named <b>rg-day01-lab</b> in <b>Central India</b> "
        "(or your nearest region).",
        "Optional: open <b>Cloud Shell</b> and run the commands on the next section.",
        "Browse a free-tier create page (Storage / App Service) but <b>do not deploy</b> "
        "anything costly yet.",
        "Optional cleanup: delete <b>rg-day01-lab</b> if you created nothing inside it, "
        "or keep it for Day 2.",
    ]))

    story.append(Paragraph("Commands (optional)", s["h1"]))
    cmd = Table([[Paragraph(
        "<font face='Courier' size='8'>"
        "az account show --output table<br/>"
        "az group create --name rg-day01-lab --location centralindia<br/>"
        "az group list --output table"
        "</font>",
        s["body"],
    )]], colWidths=[180 * mm])
    cmd.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LIGHT),
        ("BOX", (0, 0), (-1, -1), 0.6, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(cmd)

    story.append(Paragraph("Done checklist", s["h1"]))
    story.append(bullets([
        "I can explain IaaS / PaaS / SaaS with one example each",
        "I can explain Region vs Availability Zone",
        "Budget alert exists on my personal subscription",
        "Resource group rg-day01-lab exists (or I know how to create it)",
    ]))

    story.append(Paragraph("Tomorrow — Day 2", s["h2"]))
    story.append(Paragraph(
        "Azure Portal vs CLI vs PowerShell — when to click, when to script.",
        s["body"],
    ))

    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=0.6, color=LINE, spaceAfter=6))
    story.append(Paragraph(
        "Personal learning handout for LinkedIn series · Views are my own · "
        "Not affiliated with any employer · Not legal advice",
        s["footer"],
    ))
    story.append(Paragraph(SERIES_TAGS, s["footer"]))

    doc.build(story)
    print("Wrote", path)


# Registry for future days (extend over time)
HANDOUTS = {
    1: build_day01,
}


def main(days=None):
    OUT.mkdir(parents=True, exist_ok=True)
    days = days or sorted(HANDOUTS.keys())
    for d in days:
        fn = HANDOUTS[d]
        out = OUT / f"day-{d:02d}-handout.pdf"
        fn(out)
        # Publish Day 1 into the public days/ folder when present
        if d == 1:
            pub = DAYS / "day-01-cloud-fundamentals" / "handout.pdf"
            if pub.parent.exists():
                pub.write_bytes(out.read_bytes())
                print("Also wrote", pub)


if __name__ == "__main__":
    main()
