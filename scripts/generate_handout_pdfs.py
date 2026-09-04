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


def build_day02(path: Path):
    s = styles()
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm,
        title="Day 2 — Portal vs CLI vs PowerShell | 100DaysOfAzureDevOps",
        author="Personal learning series",
    )
    story = []

    story.append(header_bar(2, "Azure Portal, CLI & PowerShell Basics"))
    story.append(Spacer(1, 10))
    story.append(Paragraph("100 Days of Azure DevOps", s["cover_sub"]))
    story.append(Paragraph("Day 2 Handout — When to click vs when to script", s["cover_title"]))
    story.append(Paragraph(
        "Learning in public · Personal lab only · Educational content · Not a sales pitch",
        s["cover_sub"],
    ))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1, color=TEAL, spaceAfter=8))

    story.append(Paragraph("What you will understand today", s["h1"]))
    story.append(bullets([
        "<b>Portal</b> — best for exploration and visual confirmation",
        "<b>Azure CLI (az)</b> — best for repeatable, pipeline-friendly commands",
        "<b>PowerShell</b> — best when you need objects and Windows-centric automation",
        "<b>Naming</b> — rg-day02-lab beats New Resource Group (1)",
    ]))

    story.append(Paragraph("High-level architecture — choose your interface", s["h1"]))
    rows = [
        ["Job", "Portal", "Azure CLI", "PowerShell"],
        ["First time seeing a service", "Best", "OK", "OK"],
        ["Same task twice this week", "Avoid", "Best", "Best"],
        ["Put it in a pipeline later", "No", "Best", "Good"],
        ["Need structured objects", "Limited", "Text/JSON", "Best"],
        ["Windows estate / AD-heavy", "OK", "Good", "Best"],
    ]
    story.append(section_box("Decision table — pick the tool by the job", rows,
                             col_widths=[50 * mm, 40 * mm, 45 * mm, 45 * mm]))

    story.append(Spacer(1, 6))
    flow = [
        ["Step", "What happens"],
        ["1. You", "Decide the change (create RG, list resources, …)"],
        ["2. Portal / CLI / PowerShell", "Your interface — clicks or commands"],
        ["3. Azure Resource Manager", "Control plane that accepts the request (Day 3)"],
        ["4. Azure resource providers", "Actually create/update the resource"],
    ]
    story.append(section_box("Architecture — all three tools talk to the same plane", flow,
                             col_widths=[55 * mm, 125 * mm]))

    story.append(Paragraph("One-liner to remember", s["h1"]))
    one = Table([[Paragraph(
        "<b>Explore once in Portal &nbsp;·&nbsp; Second time use CLI &nbsp;·&nbsp; "
        "Forever after, script it</b>",
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
        "Use a <b>personal</b> Microsoft account and personal Azure subscription only.",
        s["body"],
    ))
    story.append(numbered([
        "Install Azure CLI: <b>https://aka.ms/installazurecliwindows</b>",
        "Run <b>az login</b> and select your personal subscription.",
        "Create resource group: <b>az group create --name rg-day02-lab --location centralindia</b>",
        "Optionally create one RG in the Portal to feel the click cost.",
        "List with <b>az group list --output table</b>, then delete lab RGs.",
    ]))

    story.append(Paragraph("Commands", s["h1"]))
    cmd = Table([[Paragraph(
        "<font face='Courier' size='8'>"
        "az login<br/>"
        "az account set --subscription \"&lt;name-or-id&gt;\"<br/>"
        "az group create --name rg-day02-lab --location centralindia<br/>"
        "az group show --name rg-day02-lab --output jsonc<br/>"
        "az group list --output table<br/>"
        "az group delete --name rg-day02-lab --yes --no-wait"
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
        "I can explain Portal vs CLI vs PowerShell in one line each",
        "az login works on my personal machine",
        "I created (and cleaned up) rg-day02-lab",
    ]))

    story.append(Paragraph("Tomorrow — Day 3", s["h2"]))
    story.append(Paragraph(
        "Azure Resource Manager (ARM) — the control plane behind every click and command.",
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


def build_day03(path: Path):
    s = styles()
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm,
        title="Day 3 — ARM Basics | 100DaysOfAzureDevOps",
        author="Personal learning series",
    )
    story = []

    story.append(header_bar(3, "Azure Resource Manager (ARM) Basics"))
    story.append(Spacer(1, 10))
    story.append(Paragraph("100 Days of Azure DevOps", s["cover_sub"]))
    story.append(Paragraph("Day 3 Handout — Control plane, tags & locks", s["cover_title"]))
    story.append(Paragraph(
        "Learning in public · Personal lab only · Educational content · Not a sales pitch",
        s["cover_sub"],
    ))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1, color=TEAL, spaceAfter=8))

    story.append(Paragraph("What you will understand today", s["h1"]))
    story.append(bullets([
        "<b>ARM</b> is the control plane behind Portal, CLI, and PowerShell",
        "<b>Hierarchy</b> — management group → subscription → resource group → resource",
        "<b>Tags</b> — sticky notes for cost and ownership",
        "<b>Locks</b> — duct tape so prod is harder to delete by accident",
    ]))

    story.append(Paragraph("High-level architecture", s["h1"]))
    flow = [
        ["Layer", "What it does"],
        ["You (Portal / CLI / PowerShell)", "Express the change you want"],
        ["Azure Resource Manager (ARM)", "Auth, validate, orchestrate the request"],
        ["Resource providers", "Create/update the real resource (Storage, Web, …)"],
        ["Resource", "The thing that exists and (often) costs money"],
    ]
    story.append(section_box("Architecture A — request path", flow,
                             col_widths=[70 * mm, 110 * mm]))

    story.append(Spacer(1, 6))
    hier = [
        ["Level", "Metaphor", "Why it matters"],
        ["Management group", "Company / folder of folders", "Policy at scale"],
        ["Subscription", "Billing boundary", "Where invoices land"],
        ["Resource group", "Project box", "Lifecycle + delete scope"],
        ["Resource", "The actual thing", "VM, storage, web app, …"],
    ]
    story.append(section_box("Architecture B — scope hierarchy", hier,
                             col_widths=[40 * mm, 55 * mm, 85 * mm]))

    story.append(Spacer(1, 6))
    tools = [
        ["Tool", "Job"],
        ["Tags", "Label owner / project / env for cost and cleanup"],
        ["CanNotDelete lock", "Block delete until lock is removed"],
        ["ReadOnly lock", "Block most changes (stricter)"],
    ]
    story.append(section_box("Architecture C — tags vs locks", tools,
                             col_widths=[50 * mm, 130 * mm]))

    story.append(Paragraph("One-liner to remember", s["h1"]))
    one = Table([[Paragraph(
        "<b>Portal/CLI = how you talk &nbsp;·&nbsp; ARM = who enforces rules &nbsp;·&nbsp; "
        "Tags = sticky notes &nbsp;·&nbsp; Locks = duct tape</b>",
        ParagraphStyle("ol", fontName="Helvetica", fontSize=9.5, leading=12,
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
        "Personal subscription only. Delete the lab RG when finished.",
        s["body"],
    ))
    story.append(numbered([
        "Create <b>rg-day03-lab</b> with tags Project=100Days, Owner=personal, Env=lab",
        "Add a <b>CanNotDelete</b> lock on the resource group",
        "Try <b>az group delete</b> — expect failure while locked",
        "Delete the lock, then delete the resource group",
    ]))

    story.append(Paragraph("Commands", s["h1"]))
    cmd = Table([[Paragraph(
        "<font face='Courier' size='7.5'>"
        "az group create -n rg-day03-lab -l centralindia "
        "--tags Project=100Days Owner=personal Env=lab<br/>"
        "az lock create --name cannot-delete --lock-type CanNotDelete "
        "--resource-group rg-day03-lab<br/>"
        "az lock delete --name cannot-delete --resource-group rg-day03-lab<br/>"
        "az group delete -n rg-day03-lab --yes --no-wait"
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
        "I can explain ARM in one sentence",
        "I applied tags and a CanNotDelete lock",
        "I cleaned up rg-day03-lab",
    ]))

    story.append(Paragraph("Tomorrow — Day 4", s["h2"]))
    story.append(Paragraph(
        "DevOps principles & culture — CALMS and DORA without the buzzword fog.",
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


def build_day04(path: Path):
    s = styles()
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm,
        title="Day 4 — DevOps Principles & Culture | 100DaysOfAzureDevOps",
        author="Personal learning series",
    )
    story = []

    story.append(header_bar(4, "DevOps Principles & Culture"))
    story.append(Spacer(1, 10))
    story.append(Paragraph("100 Days of Azure DevOps", s["cover_sub"]))
    story.append(Paragraph("Day 4 Handout — CALMS + DORA without the buzzword fog", s["cover_title"]))
    story.append(Paragraph(
        "Learning in public · Personal lab only · Educational content · Not a sales pitch",
        s["cover_sub"],
    ))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1, color=TEAL, spaceAfter=8))

    story.append(Paragraph("What you will understand today", s["h1"]))
    story.append(bullets([
        "<b>DevOps</b> is habits + outcomes — not a job title or a laptop sticker",
        "<b>CALMS</b> — Culture, Automation, Lean, Measurement, Sharing",
        "<b>DORA</b> — four metrics that expose theatre",
        "Agile and DevOps <b>complement</b> each other; they do not replace each other",
    ]))

    story.append(Paragraph("High-level architecture — CALMS", s["h1"]))
    calms = [
        ["Letter", "Means", "Red flag if missing"],
        ["Culture", "Blame process, not people", "Who deployed? is the first question"],
        ["Automation", "Script what you repeat", "Click-ops at midnight"],
        ["Lean", "Small batches, less WIP", "Big-bang Friday releases"],
        ["Measurement", "Numbers beat vibes", "Only metric is ticket count"],
        ["Sharing", "Runbooks + postmortems", "Only one person knows how"],
    ]
    story.append(section_box("Architecture A — CALMS scorecard", calms,
                             col_widths=[28 * mm, 55 * mm, 97 * mm]))

    story.append(Spacer(1, 6))
    dora = [
        ["DORA metric", "Question it answers", "Why it matters"],
        ["Deployment frequency", "How often do we ship?", "Smaller changes, faster feedback"],
        ["Lead time for changes", "Commit → production how long?", "Friction in the path to users"],
        ["Change failure rate", "How often do releases hurt?", "Quality of your delivery system"],
        ["Time to restore", "How fast do we recover?", "Resilience when (not if) it breaks"],
    ]
    story.append(section_box("Architecture B — DORA four keys", dora,
                             col_widths=[45 * mm, 60 * mm, 75 * mm]))

    story.append(Paragraph("One-liner to remember", s["h1"]))
    one = Table([[Paragraph(
        "<b>CALMS = what good feels like &nbsp;·&nbsp; DORA = how you prove it &nbsp;·&nbsp; "
        "Tools without habits = theatre</b>",
        ParagraphStyle("ol", fontName="Helvetica", fontSize=9.5, leading=12,
                       textColor=NAVY, alignment=TA_CENTER)
    )]], colWidths=[180 * mm])
    one.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FEF3C7")),
        ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#D97706")),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(one)

    story.append(Paragraph("Step-by-step lab (20–30 min) — no Azure spend", s["h1"]))
    story.append(Paragraph(
        "Concepts only today. Be honest. Nobody grades this but future-you.",
        s["body"],
    ))
    story.append(numbered([
        "Score yourself (or your last team) <b>1–5</b> on each CALMS letter",
        "Circle the weakest letter — that is your next habit to build",
        "Pick <b>one</b> DORA metric you can measure on a personal lab later "
        "(even deploys-per-week to a throwaway App Service)",
        "Write three sentences: what “good” looks like for that metric in six months",
    ]))

    story.append(Paragraph("Scorecard template", s["h1"]))
    cmd = Table([[Paragraph(
        "<font face='Courier' size='9'>"
        "Culture:     _ / 5<br/>"
        "Automation:  _ / 5<br/>"
        "Lean:        _ / 5<br/>"
        "Measurement: _ / 5<br/>"
        "Sharing:     _ / 5<br/><br/>"
        "DORA metric I will track: _______________________"
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
        "I can explain CALMS without reading a slide",
        "I can name the four DORA metrics",
        "I filled a 1–5 scorecard and picked one metric to track",
    ]))

    story.append(Paragraph("Tomorrow — Day 5", s["h2"]))
    story.append(Paragraph(
        "Azure DevOps Services overview — Boards, Repos, Pipelines, Test Plans, Artifacts.",
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


def build_day05(path: Path):
    s = styles()
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm,
        title="Day 5 — Azure DevOps Services Overview | 100DaysOfAzureDevOps",
        author="Personal learning series",
    )
    story = []

    story.append(header_bar(5, "Azure DevOps Services Overview"))
    story.append(Spacer(1, 10))
    story.append(Paragraph("100 Days of Azure DevOps", s["cover_sub"]))
    story.append(Paragraph("Day 5 Handout — Boards, Repos, Pipelines, Tests, Artifacts", s["cover_title"]))
    story.append(Paragraph(
        "Learning in public · Personal lab only · Educational content · Not a sales pitch",
        s["cover_sub"],
    ))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1, color=TEAL, spaceAfter=8))

    story.append(Paragraph("What you will understand today", s["h1"]))
    story.append(bullets([
        "<b>Boards</b> for planning and tracking work",
        "<b>Repos</b> for source control and PR reviews",
        "<b>Pipelines</b> for CI/CD automation",
        "<b>Test Plans</b> for manual and exploratory test cases",
        "<b>Artifacts</b> for package feeds and dependency sharing",
    ]))

    story.append(Paragraph("High-level architecture — service map", s["h1"]))
    flow = [
        ["Step", "Service", "Outcome"],
        ["1", "Boards", "Work item planned and prioritized"],
        ["2", "Repos", "Code committed and reviewed"],
        ["3", "Pipelines", "Build/test/deploy executed"],
        ["4", "Test Plans", "Manual or exploratory validation captured"],
        ["5", "Artifacts", "Packages published and versioned"],
    ]
    story.append(section_box("Architecture A — idea to delivery", flow,
                             col_widths=[18 * mm, 52 * mm, 110 * mm]))

    story.append(Spacer(1, 6))
    compare = [
        ["Service", "Best used for", "Signal of healthy usage"],
        ["Boards", "Backlog, sprint planning, traceability", "Stories map to commits and releases"],
        ["Repos", "Branch strategy and code reviews", "PR workflow with clear history"],
        ["Pipelines", "Repeatable CI/CD", "Same pipeline runs for every change"],
        ["Test Plans", "Structured manual testing", "Pass/fail tied to work items"],
        ["Artifacts", "Reusable package feeds", "Versioned dependencies, no ad-hoc binaries"],
    ]
    story.append(section_box("Architecture B — each hub's role", compare,
                             col_widths=[30 * mm, 70 * mm, 80 * mm]))

    story.append(Paragraph("One-liner to remember", s["h1"]))
    one = Table([[Paragraph(
        "<b>Boards plan &nbsp;·&nbsp; Repos store &nbsp;·&nbsp; Pipelines ship &nbsp;·&nbsp; "
        "Test Plans validate &nbsp;·&nbsp; Artifacts distribute</b>",
        ParagraphStyle("ol", fontName="Helvetica", fontSize=9.5, leading=12,
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
        "Create and explore one personal Azure DevOps project end-to-end. No production data.",
        s["body"],
    ))
    story.append(numbered([
        "Create personal org at <b>https://dev.azure.com</b>",
        "Create project <b>day05-overview</b> (Agile, private)",
        "Create one User Story in Boards",
        "Initialize repo with README in Repos",
        "Open New Pipeline wizard and select your repo (no run required)",
        "Open Test Plans and Artifacts hubs once to understand layout",
    ]))

    story.append(Paragraph("Quick reference", s["h1"]))
    cmd = Table([[Paragraph(
        "<font face='Courier' size='8'>"
        "Portal: https://dev.azure.com/&lt;your-org&gt;<br/>"
        "Project: https://dev.azure.com/&lt;your-org&gt;/day05-overview<br/>"
        "Hubs: Boards | Repos | Pipelines | Test Plans | Artifacts"
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
        "I can explain what each of the five hubs does",
        "I created a project and touched each service once",
        "I can describe the flow from work item to deployment",
    ]))

    story.append(Paragraph("Tomorrow — Day 6", s["h2"]))
    story.append(Paragraph(
        "Setting up an Azure DevOps organization with clean defaults and access boundaries.",
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


def build_day06(path: Path):
    s = styles()
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm,
        title="Day 6 — Azure DevOps Org Setup | 100DaysOfAzureDevOps",
        author="Personal learning series",
    )
    story = []

    story.append(header_bar(6, "Setting Up an Azure DevOps Organization"))
    story.append(Spacer(1, 10))
    story.append(Paragraph("100 Days of Azure DevOps", s["cover_sub"]))
    story.append(Paragraph("Day 6 Handout — Org, project, process & permissions", s["cover_title"]))
    story.append(Paragraph(
        "Learning in public · Personal lab only · Educational content · Not a sales pitch",
        s["cover_sub"],
    ))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1, color=TEAL, spaceAfter=8))

    story.append(Paragraph("What you will understand today", s["h1"]))
    story.append(bullets([
        "<b>Organization</b> — tenancy, users, collection-level settings",
        "<b>Project</b> — container for Boards, Repos, Pipelines, Test Plans, Artifacts",
        "<b>Process template</b> — Agile / Scrum / Basic / CMMI shapes work items",
        "<b>Permissions</b> — Collection Admin vs Project Admin vs Contributor",
        "<b>Personal-only rule</b> — no work accounts, no employer data",
    ]))

    story.append(Paragraph("High-level architecture", s["h1"]))
    hier = [
        ["Layer", "What it controls", "Lab choice"],
        ["Organization", "Who can sign in; org-wide settings", "Personal Microsoft account only"],
        ["Project", "Where hubs and repos live", "azure-100-labs (private)"],
        ["Process", "Work item types and states", "Agile for this series"],
        ["Permissions", "What each identity can change", "Minimal Collection Admins"],
    ]
    story.append(section_box("Architecture A — org stack", hier,
                             col_widths=[35 * mm, 70 * mm, 75 * mm]))

    story.append(Spacer(1, 6))
    roles = [
        ["Role", "Typical power", "Use carefully"],
        ["Project Collection Administrators", "Org-wide: users, policies, all projects", "Keep this list tiny"],
        ["Project Administrators", "One project: settings, repos, pipelines", "Fine for lab owners"],
        ["Contributors", "Create work items, push (with policies), run pipelines", "Default for team members"],
        ["Readers", "View only", "Useful for stakeholders later"],
    ]
    story.append(section_box("Architecture B — permission bands", roles,
                             col_widths=[55 * mm, 65 * mm, 60 * mm]))

    story.append(Paragraph("One-liner to remember", s["h1"]))
    one = Table([[Paragraph(
        "<b>Org = tenancy and access &nbsp;·&nbsp; Project = where work lives &nbsp;·&nbsp; "
        "Keep both personal and clean</b>",
        ParagraphStyle("ol", fontName="Helvetica", fontSize=9.5, leading=12,
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
        "Personal Microsoft account only. Do not invite work users.",
        s["body"],
    ))
    story.append(numbered([
        "Open <b>https://dev.azure.com/&lt;your-org&gt;</b> (create org if needed)",
        "Org settings → Overview: note name and owner",
        "Org settings → Users / Permissions: confirm personal-only access",
        "Create project <b>azure-100-labs</b> (Agile process, private)",
        "Set project description: Personal 100DaysOfAzureDevOps labs — views are my own",
        "Optional: configure Azure DevOps CLI defaults for org + project",
    ]))

    story.append(Paragraph("Commands (optional)", s["h1"]))
    cmd = Table([[Paragraph(
        "<font face='Courier' size='7.5'>"
        "az extension add --name azure-devops<br/>"
        "az devops configure --defaults "
        "organization=https://dev.azure.com/&lt;your-org&gt; project=azure-100-labs<br/>"
        "az devops project list -o table<br/>"
        "az devops project show --project azure-100-labs -o table"
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
        "I can explain organization vs project",
        "azure-100-labs exists and is private",
        "No work accounts were invited",
    ]))

    story.append(Paragraph("Tomorrow — Day 7", s["h2"]))
    story.append(Paragraph(
        "Azure Boards deep dive — Epics, Features, Stories, and honest WIP.",
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


def build_day07(path: Path):
    s = styles()
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm,
        title="Day 7 — Azure Boards Deep Dive | 100DaysOfAzureDevOps",
        author="Personal learning series",
    )
    story = []

    story.append(header_bar(7, "Azure Boards Deep Dive"))
    story.append(Spacer(1, 10))
    story.append(Paragraph("100 Days of Azure DevOps", s["cover_sub"]))
    story.append(Paragraph("Day 7 Handout — Hierarchy, backlog, board & queries", s["cover_title"]))
    story.append(Paragraph(
        "Learning in public · Personal lab only · Educational content · Not a sales pitch",
        s["cover_sub"],
    ))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1, color=TEAL, spaceAfter=8))

    story.append(Paragraph("What you will understand today", s["h1"]))
    story.append(bullets([
        "<b>Epic → Feature → Story → Task/Bug</b> — planning hierarchy",
        "<b>Backlog</b> — prioritized list of work",
        "<b>Board</b> — visual flow (To Do, Doing, Done)",
        "<b>Queries</b> — saved filters (e.g. open stories)",
        "<b>WIP</b> — limit work in Doing so flow stays honest",
    ]))

    story.append(Paragraph("High-level architecture", s["h1"]))
    hier = [
        ["Level", "Example (this series)", "Finish when"],
        ["Epic", "100 Days Learning", "Series complete"],
        ["Feature", "Phase 1 Foundations", "Phase recap done"],
        ["User Story", "Day 8 — Test Plans lab", "Lab + post done"],
        ["Task", "Create test plan, add 2 cases", "Checklist ticked"],
    ]
    story.append(section_box("Architecture A — work item hierarchy", hier,
                             col_widths=[28 * mm, 72 * mm, 80 * mm]))

    story.append(Spacer(1, 6))
    board = [
        ["Column", "Meaning", "Warning sign"],
        ["New / To Do", "Accepted, not started", "Huge backlog, no grooming"],
        ["Active / Doing", "In progress now", "20+ items — WIP explosion"],
        ["Resolved / Done", "Finished", "Done without demo or review"],
    ]
    story.append(section_box("Architecture B — board columns", board,
                             col_widths=[35 * mm, 70 * mm, 75 * mm]))

    story.append(Paragraph("One-liner to remember", s["h1"]))
    one = Table([[Paragraph(
        "<b>Backlog = might do &nbsp;·&nbsp; Board = doing now &nbsp;·&nbsp; "
        "Query = forgot to close</b>",
        ParagraphStyle("ol", fontName="Helvetica", fontSize=9.5, leading=12,
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
        "Project: <b>azure-100-labs</b> (from Day 6). Personal org only.",
        s["body"],
    ))
    story.append(numbered([
        "Boards → create Epic <b>100 Days Learning</b>",
        "Add Feature <b>Phase 1 Foundations</b> under the Epic",
        "Add 3 User Stories (e.g. Days 8–10 topics)",
        "Open Board → move one story To Do → Doing → Done",
        "Queries → new query: Type = User Story AND State <> Done",
    ]))

    story.append(Paragraph("Example story titles", s["h1"]))
    cmd = Table([[Paragraph(
        "<font face='Courier' size='8'>"
        "• Explore Azure Test Plans<br/>"
        "• Create Azure Artifacts feed<br/>"
        "• Stand up end-to-end mini project"
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
        "I can explain Epic → Feature → Story in one sentence each",
        "Hierarchy exists in azure-100-labs",
        "One story moved to Done on the board",
        "Open-stories query created",
    ]))

    story.append(Paragraph("Tomorrow — Day 8", s["h2"]))
    story.append(Paragraph(
        "Azure Test Plans basics — structured testing beyond “we clicked around.”",
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


def build_day08(path: Path):
    s = styles()
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm,
        title="Day 8 — Azure Test Plans Basics | 100DaysOfAzureDevOps",
        author="Personal learning series",
    )
    story = []

    story.append(header_bar(8, "Azure Test Plans Basics"))
    story.append(Spacer(1, 10))
    story.append(Paragraph("100 Days of Azure DevOps", s["cover_sub"]))
    story.append(Paragraph("Day 8 Handout — Test plans, suites, test cases & traceability", s["cover_title"]))
    story.append(Paragraph(
        "Learning in public · Personal lab only · Educational content · Not a sales pitch",
        s["cover_sub"],
    ))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1, color=TEAL, spaceAfter=8))

    hier = [
        ["Level", "What it represents", "Example / Usage"],
        ["Test Plan", "Top-level milestone, release, or sprint test container", "Phase 1 Smoke Tests"],
        ["Test Suite", "Logical grouping of test cases (Static, Requirement, Query)", "Portal & CLI Baseline"],
        ["Test Case", "Step-by-step action + expected outcome (reproducible)", "TC01: Verify Azure login"],
        ["Test Run", "Execution record capturing Pass, Fail, Blocked, and attachments", "Run via Web Test Runner"],
    ]
    story.append(section_box("Architecture A — test plans hierarchy", hier,
                             col_widths=[32 * mm, 78 * mm, 70 * mm]))

    story.append(Spacer(1, 6))
    comp = [
        ["Testing track", "Where it runs", "Best suited for"],
        ["Automated CI Tests", "Build pipeline (az pipelines / runners)", "Unit tests, linting, regression, fast feedback"],
        ["Manual & Exploratory", "Azure Test Plans + Web Test Runner", "UAT, UI flows, exploratory edge cases, acceptance"],
        ["Traceability loop", "User Story ↔ Test Case ↔ Run ↔ Bug", "Full visibility from backlog requirement to defect"],
    ]
    story.append(section_box("Architecture B — automated CI vs test plans traceability", comp,
                             col_widths=[40 * mm, 70 * mm, 70 * mm]))

    story.append(Paragraph("One-liner to remember", s["h1"]))
    one = Table([[Paragraph(
        "<b>Automated tests verify what you expected &nbsp;·&nbsp; "
        "Test Plans track what humans must prove &nbsp;·&nbsp; "
        "Traceability links both to the board</b>",
        ParagraphStyle("ol", fontName="Helvetica", fontSize=9.5, leading=12,
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
        "In <b>azure-100-labs</b> (enable Test Plans basic/trial access if prompted):",
        s["body"],
    ))
    story.append(numbered([
        "Open <b>Test Plans</b> → create Test Plan <b>Phase 1 Smoke Tests</b>",
        "Add a Static Suite named <b>Portal & CLI Baseline</b>",
        "Add Test Case: <b>TC01 — Verify Azure login & personal directory</b>",
        "Add Test Case: <b>TC02 — Verify resource group creation via CLI</b>",
        "Define step-by-step <i>Action</i> and <i>Expected result</i> for each test case",
        "Click <b>Run for web application</b>, step through, and mark results (Pass / Blocked)",
        "Link a test case to a User Story on Azure Boards to verify the traceability chain",
    ]))

    story.append(Paragraph("Test case steps example", s["h1"]))
    cmd = Table([[Paragraph(
        "<font face='Courier' size='7.5'>"
        "TC01 Step 1: Run 'az account show -o table' &nbsp;→ Expected: Shows personal sub/tenant ID<br/>"
        "TC01 Step 2: Open portal.azure.com &nbsp;→ Expected: Correct personal directory shown<br/>"
        "TC02 Step 1: Run 'az group create -n rg-lab-smoke -l centralindia' &nbsp;→ Expected: Succeeded<br/>"
        "TC02 Step 2: Run 'az group delete -n rg-lab-smoke --yes --no-wait' &nbsp;→ Expected: Exit 0"
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
        "I can explain Test Plan vs Suite vs Case vs Run",
        "Test Plan and 2 Test Cases created in azure-100-labs",
        "Executed a test run in the Web Runner",
        "Test case linked to a User Story on Boards",
    ]))

    story.append(Paragraph("Tomorrow — Day 9", s["h2"]))
    story.append(Paragraph(
        "Azure Artifacts — package management feeds, upstream sources, and dependency hygiene.",
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


def build_day09(path: Path):
    s = styles()
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm,
        title="Day 9 — Azure Artifacts | 100DaysOfAzureDevOps",
        author="Personal learning series",
    )
    story = []

    story.append(header_bar(9, "Azure Artifacts"))
    story.append(Spacer(1, 10))
    story.append(Paragraph("100 Days of Azure DevOps", s["cover_sub"]))
    story.append(Paragraph("Day 9 Handout — Feeds, upstream caching & package promotion", s["cover_title"]))
    story.append(Paragraph(
        "Learning in public · Personal lab only · Educational content · Not a sales pitch",
        s["cover_sub"],
    ))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1, color=TEAL, spaceAfter=8))

    hier = [
        ["Artifacts Component", "What it provides", "Typical use case"],
        ["Feed", "Organizational or project-scoped package registry", "Internal shared libraries & utilities"],
        ["Upstream Sources", "Proxy + cache for public registries (nuget, npm)", "Build resilience when public registries fail"],
        ["Feed Views", "Promotion channels (@local, @prerelease, @release)", "Release gating without re-tagging versions"],
        ["Retention Policy", "Auto-clean rules for older package versions", "Storage cost control and decluttering"],
    ]
    story.append(section_box("Architecture A — artifacts building blocks", hier,
                             col_widths=[40 * mm, 70 * mm, 70 * mm]))

    story.append(Spacer(1, 6))
    comp = [
        ["Package Ecosystem", "Config File", "Auth / Publish Tool"],
        ["npm / Node.js", ".npmrc (registry + always-auth)", "vsts-npm-auth / npm publish"],
        ["NuGet / .NET", "nuget.config (packageSources)", "dotnet nuget push / Azure DevOps task"],
        ["Python (pip/twine)", "pip.ini / .pypirc", "twine upload --repository-url"],
        ["Universal Packages", "Pipeline Task / az artifacts", "az artifacts universal publish"],
    ]
    story.append(section_box("Architecture B — supported ecosystems & client setup", comp,
                             col_widths=[40 * mm, 70 * mm, 70 * mm]))

    story.append(Paragraph("One-liner to remember", s["h1"]))
    one = Table([[Paragraph(
        "<b>Pipelines cook the software &nbsp;·&nbsp; "
        "Artifacts is the pantry &nbsp;·&nbsp; "
        "Upstream caching ensures you never starve when public repos blip</b>",
        ParagraphStyle("ol", fontName="Helvetica", fontSize=9.5, leading=12,
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
        "In <b>azure-100-labs</b> (Azure Artifacts is included for up to 2GB free storage):",
        s["body"],
    ))
    story.append(numbered([
        "Navigate to <b>Artifacts</b> hub in your project",
        "Click <b>Create Feed</b> → Name: <b>day09-packages</b>",
        "Set visibility to <b>Project: azure-100-labs</b> (project-scoped)",
        "Check <b>Include packages from common public sources</b> (nuget.org, npmjs)",
        "Open <b>Feed settings</b> → inspect default views: <b>@local</b>, <b>@prerelease</b>, <b>@release</b>",
        "Click <b>Connect to feed</b> → select npm / NuGet → review the auth config snippet",
        "Save the feed URL in your notes — you will consume it in Phase 3 CI/CD pipelines",
    ]))

    story.append(Paragraph("Client config snippet example", s["h1"]))
    cmd = Table([[Paragraph(
        "<font face='Courier' size='7.5'>"
        "# .npmrc<br/>"
        "registry=https://pkgs.dev.azure.com/&lt;your-org&gt;/azure-100-labs/_packaging/day09-packages/npm/registry/<br/>"
        "always-auth=true<br/>"
        "# Auth CLI helper: npx vsts-npm-auth -config .npmrc"
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
        "I can explain Feeds vs Upstream Sources vs Views",
        "Feed day09-packages created in azure-100-labs",
        "Upstream sources enabled for public packages",
        "Client config snippet (.npmrc / nuget.config) saved",
    ]))

    story.append(Paragraph("Tomorrow — Day 10", s["h2"]))
    story.append(Paragraph(
        "Phase 1 Capstone Mini Project & Recap — tying Boards, Repos, Test Plans, and Artifacts together.",
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


def build_day10(path: Path):
    s = styles()
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm,
        title="Day 10 — Phase 1 Capstone & Architecture Recap | 100DaysOfAzureDevOps",
        author="Personal learning series",
    )
    story = []

    story.append(header_bar(10, "Phase 1 Capstone & Recap"))
    story.append(Spacer(1, 10))
    story.append(Paragraph("100 Days of Azure DevOps", s["cover_sub"]))
    story.append(Paragraph("Day 10 Handout — Azure & DevOps Foundations Capstone", s["cover_title"]))
    story.append(Paragraph(
        "Learning in public · Personal lab only · Educational content · Not a sales pitch",
        s["cover_sub"],
    ))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1, color=TEAL, spaceAfter=8))

    matrix = [
        ["Phase 1 Track", "Days & Key Concepts", "Core Deliverable / Proof"],
        ["Azure Foundations", "Days 1–3: Cloud models, CLI/PWSH, ARM & Locks", "Resource hierarchy, Tags & Budget alerts"],
        ["DevOps Culture", "Day 4: CALMS principles, DORA metrics", "Flow & Deployment Frequency mindset"],
        ["Azure DevOps Hubs", "Days 5–9: Boards, Repos, Test Plans, Artifacts", "Project azure-100-labs, WIP limits, Feeds"],
        ["Phase 1 Capstone", "Day 10: End-to-end integration & Dashboards", "Phase 1 Command Center overview live"],
    ]
    story.append(section_box("Architecture A — Phase 1 foundations master matrix", matrix,
                             col_widths=[38 * mm, 74 * mm, 68 * mm]))

    story.append(Spacer(1, 6))
    hubs = [
        ["Azure DevOps Hub", "Role in azure-100-labs", "Phase 2 & 3 Evolution"],
        ["Boards", "Epics, Features, User Stories with WIP limits", "Work item linking to branches & PRs"],
        ["Repos", "Git repository initialized with README.md", "Branch policies, PR gates, merge strategies"],
        ["Test Plans", "Phase 1 Smoke Tests plan with manual test cases", "Automated test integration via CI pipelines"],
        ["Artifacts", "day09-packages feed with upstream sources", "Publishing & consuming build packages"],
        ["Dashboards", "Phase 1 Command Center with query charts", "Pipeline health, DORA & sprint telemetry"],
    ]
    story.append(section_box("Architecture B — end-to-end hub integration", hubs,
                             col_widths=[32 * mm, 78 * mm, 70 * mm]))

    story.append(Paragraph("One-liner to remember", s["h1"]))
    one = Table([[Paragraph(
        "<b>Foundations are not the boring part of DevOps &nbsp;·&nbsp; "
        "They are the guardrails that keep future CI/CD pipelines from automating chaos</b>",
        ParagraphStyle("ol", fontName="Helvetica", fontSize=9.5, leading=12,
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
        "In <b>azure-100-labs</b> (verify all Phase 1 foundations before Phase 2):",
        s["body"],
    ))
    story.append(numbered([
        "Verify <b>Boards</b>: confirm Epic, Feature, and User Stories exist with WIP limits",
        "Verify <b>Repos</b>: clone locally, commit README.md, and push to main",
        "Verify <b>Test Plans</b>: confirm Smoke Test plan is linked to a User Story",
        "Verify <b>Artifacts</b>: confirm day09-packages feed has upstream sources active",
        "Navigate to <b>Overview → Dashboards</b> → create <b>Phase 1 Command Center</b>",
        "Add widgets: Query Tile (Open stories), Work item chart, and Project Markdown",
        "Run Azure CLI cost audit: confirm zero orphan lab resource groups remain active",
    ]))

    story.append(Paragraph("Bootstrap & governance commands", s["h1"]))
    cmd = Table([[Paragraph(
        "<font face='Courier' size='7.5'>"
        "git clone https://dev.azure.com/&lt;org&gt;/azure-100-labs/_git/azure-100-labs<br/>"
        "git commit -m 'docs: bootstrap Phase 1 lab repo' && git push origin main<br/>"
        "az group list --query \"[?starts_with(name, 'rg-lab-')].name\" -o table"
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
        "Completed Phase 1 (Days 1–10) foundations",
        "All 5 hubs active & verified in azure-100-labs",
        "Phase 1 Command Center dashboard created",
        "Azure subscription clean of unwanted lab resources",
    ]))

    story.append(Paragraph("Tomorrow — Day 11 (Phase 2 Begins)", s["h2"]))
    story.append(Paragraph(
        "Git Foundations for DevOps Engineers — commits, branches, internals, and clean hygiene.",
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


def build_day11(path: Path):
    s = styles()
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm,
        title="Day 11 — Git Fundamentals for DevOps Engineers | 100DaysOfAzureDevOps",
        author="Personal learning series",
    )
    story = []

    story.append(header_bar(11, "Git Fundamentals for DevOps"))
    story.append(Spacer(1, 10))
    story.append(Paragraph("100 Days of Azure DevOps", s["cover_sub"]))
    story.append(Paragraph("Day 11 Handout — 4 Git areas, object models & commit DAG", s["cover_title"]))
    story.append(Paragraph(
        "Learning in public · Personal lab only · Educational content · Not a sales pitch",
        s["cover_sub"],
    ))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1, color=TEAL, spaceAfter=8))

    areas = [
        ["Area", "Location / State", "Purpose in DevOps Workflow"],
        ["Working Tree", "Filesystem directory", "Unstaged edits, live code changes"],
        ["Staging Area (Index)", ".git/index", "Curated snapshot boundary for atomic commits"],
        ["Local Repo", ".git/objects (DAG)", "Committed, immutable history points with SHA-1s"],
        ["Remote Repo", "Azure Repos", "Shared upstream collaboration hub triggering CI runs"],
    ]
    story.append(section_box("Architecture A — the 4 areas of git", areas,
                             col_widths=[38 * mm, 62 * mm, 80 * mm]))

    story.append(Spacer(1, 6))
    objects = [
        ["Git Primitive", "Internal Structure", "Why it matters in CI/CD"],
        ["Blob", "Compressed file contents hashed by SHA", "Deduplication across commits & branches"],
        ["Tree", "List of SHA pointers to blobs and subtrees", "Captures exact directory structure snapshots"],
        ["Commit", "Root tree SHA + Author + Committer + Parent SHA", "Creates immutable, traceable history graph"],
        ["Branch / Ref", "41-byte text pointer in .git/refs/heads/", "Cheap, instant isolation for feature branches"],
    ]
    story.append(section_box("Architecture B — git object model & graph (DAG)", objects,
                             col_widths=[32 * mm, 78 * mm, 70 * mm]))

    story.append(Paragraph("One-liner to remember", s["h1"]))
    one = Table([[Paragraph(
        "<b>Git doesn't store file diffs — it stores snapshot DAGs &nbsp;·&nbsp; "
        "Treat your commit history like production code, not a scratchpad</b>",
        ParagraphStyle("ol", fontName="Helvetica", fontSize=9.5, leading=12,
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
        "In your local clone of <b>azure-100-labs</b>:",
        s["body"],
    ))
    story.append(numbered([
        "Verify status and branch: <b>git status</b> and <b>git branch</b>",
        "Create & switch to feature branch: <b>git switch -c feature/day11-git-notes</b>",
        "Create notes file: <b>notes/day-11-git-model.md</b> with 4-areas summary",
        "Stage file explicitly: <b>git add notes/day-11-git-model.md</b>",
        "Commit with clear intent: <b>git commit -m 'docs: add Day 11 git mental model'</b>",
        "Inspect commit graph: <b>git log --oneline --graph --decorate -n 5</b>",
        "Push to remote with upstream tracking: <b>git push -u origin feature/day11-git-notes</b>",
    ]))

    story.append(Paragraph("Core Git CLI commands", s["h1"]))
    cmd = Table([[Paragraph(
        "<font face='Courier' size='7.5'>"
        "git switch -c feature/day11-git-notes<br/>"
        "git add notes/day-11-git-model.md<br/>"
        "git commit -m 'docs: add Day 11 git notes'<br/>"
        "git push -u origin feature/day11-git-notes<br/>"
        "git log --oneline --graph --decorate -n 5"
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
        "I can explain the 4 Git areas and Blob/Tree/Commit objects",
        "Created and switched branches using git switch",
        "Created an atomic commit and inspected the graph",
        "Pushed feature branch to Azure Repos with -u tracking",
    ]))

    story.append(Paragraph("Tomorrow — Day 12", s["h2"]))
    story.append(Paragraph(
        "Branching Strategies for CI/CD — Trunk-based development vs GitFlow & Release branches.",
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


def build_day12(path: Path):
    s = styles()
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm,
        title="Day 12 — Branching Strategies for CI/CD | 100DaysOfAzureDevOps",
        author="Personal learning series",
    )
    story = []

    story.append(header_bar(12, "Branching Strategies for CI/CD"))
    story.append(Spacer(1, 10))
    story.append(Paragraph("100 Days of Azure DevOps", s["cover_sub"]))
    story.append(Paragraph("Day 12 Handout — GitFlow vs GitHub Flow vs Trunk-Based", s["cover_title"]))
    story.append(Paragraph(
        "Learning in public · Personal lab only · Educational content · Not a sales pitch",
        s["cover_sub"],
    ))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1, color=TEAL, spaceAfter=8))

    models = [
        ["Model", "Branch Structure", "Best For", "Main Risk"],
        ["GitFlow", "main + develop + feature/release/hotfix", "Scheduled releases, multi-version prod", "Late integration, merge debt"],
        ["GitHub Flow", "main + short feature/*", "Continuous delivery, one prod line", "main must stay deployable"],
        ["Trunk-Based", "main (+ branches &lt; 1 day)", "High velocity, mature CI/CD", "Needs feature flags + discipline"],
    ]
    story.append(section_box("Architecture A — branching model comparison", models,
                             col_widths=[28 * mm, 52 * mm, 52 * mm, 48 * mm]))

    story.append(Spacer(1, 6))
    rules = [
        ["Decision Factor", "GitFlow Signal", "Trunk-Based Signal"],
        ["Release cadence", "Fixed schedule (monthly/quarterly)", "Deploy multiple times per day"],
        ["Prod versions", "2+ versions supported simultaneously", "Single production line"],
        ["Team size", "Large, role-separated (dev/QA/release)", "Small, full-stack ownership"],
        ["CI maturity", "Can tolerate longer integration windows", "Requires fast, reliable automated tests"],
    ]
    story.append(section_box("Architecture B — how to choose a model", rules,
                             col_widths=[45 * mm, 67 * mm, 68 * mm]))

    story.append(Paragraph("One-liner to remember", s["h1"]))
    one = Table([[Paragraph(
        "<b>Branching strategy is a delivery decision &nbsp;·&nbsp; "
        "Pick complexity that matches how often you actually ship</b>",
        ParagraphStyle("ol", fontName="Helvetica", fontSize=9.5, leading=12,
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
        "In your local clone of <b>azure-100-labs</b>:",
        s["body"],
    ))
    story.append(numbered([
        "Create branch: <b>git switch -c feature/day12-branching-adr</b>",
        "Create ADR: <b>docs/branching-strategy.md</b>",
        "Document decision: <b>GitHub Flow</b> — protected main, feature/* &lt; 2 days",
        "Specify: PR required, squash merge, no develop/release branches",
        "Commit: <b>git commit -m 'docs: add branching strategy ADR'</b>",
        "Push: <b>git push -u origin feature/day12-branching-adr</b>",
        "Open Pull Request in Azure Repos",
    ]))

    story.append(Paragraph("ADR skeleton", s["h1"]))
    cmd = Table([[Paragraph(
        "<font face='Courier' size='7.5'>"
        "# Branching Strategy — azure-100-labs<br/>"
        "# Decision: GitHub Flow (trunk-based lite)<br/>"
        "# - main: protected, always deployable<br/>"
        "# - feature/*: short-lived (&lt; 2 days)<br/>"
        "# - PR required; squash merge<br/>"
        "# - No develop, release/, or hotfix/ branches"
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
        "I can compare GitFlow, GitHub Flow, and Trunk-Based",
        "ADR docs/branching-strategy.md created in azure-100-labs",
        "Feature branch pushed with ADR commit",
        "PR opened (or ready to open) in Azure Repos",
    ]))

    story.append(Paragraph("Tomorrow — Day 13", s["h2"]))
    story.append(Paragraph(
        "Azure Repos setup — remotes, permissions, and repository hygiene.",
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


def build_day13(path: Path):
    s = styles()
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm,
        title="Day 13 — Azure Repos Setup & Hygiene | 100DaysOfAzureDevOps",
        author="Personal learning series",
    )
    story = []

    story.append(header_bar(13, "Azure Repos Setup & Hygiene"))
    story.append(Spacer(1, 10))
    story.append(Paragraph("100 Days of Azure DevOps", s["cover_sub"]))
    story.append(Paragraph("Day 13 Handout — Layout, gitignore, remotes & permissions", s["cover_title"]))
    story.append(Paragraph(
        "Learning in public · Personal lab only · Educational content · Not a sales pitch",
        s["cover_sub"],
    ))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1, color=TEAL, spaceAfter=8))

    layout = [
        ["Folder", "Purpose", "Phase"],
        ["/src", "Application source code", "Phase 2+"],
        ["/docs", "ADRs, architecture notes, runbooks", "Phase 2 (today)"],
        ["/pipelines", "CI/CD YAML pipeline definitions", "Phase 3"],
        ["/infra", "IaC templates (ARM, Bicep, Terraform)", "Phase 4+"],
        ["/notes", "Daily learning notes from series", "Ongoing"],
    ]
    story.append(section_box("Architecture A — standard repo folder layout", layout,
                             col_widths=[28 * mm, 92 * mm, 60 * mm]))

    story.append(Spacer(1, 6))
    hygiene = [
        ["Hygiene Item", "What to configure", "Why it matters"],
        ["Default branch", "main (single deployable line)", "Clear PR target and pipeline trigger"],
        [".gitignore", "node_modules, .env, dist/, IDE folders", "Secrets and artifacts stay out of history"],
        ["Remote URL", "HTTPS or SSH — verify git remote -v", "Consistent clone/push across machines"],
        ["Permissions", "Readers / Contributors / Admins", "Least privilege; branch policies on Day 19"],
        ["Feature branches", "Push feature/* not direct to main", "Prepares for PR workflow (Day 14)"],
    ]
    story.append(section_box("Architecture B — repo hygiene checklist", hygiene,
                             col_widths=[38 * mm, 72 * mm, 70 * mm]))

    story.append(Paragraph("One-liner to remember", s["h1"]))
    one = Table([[Paragraph(
        "<b>Repo structure is infrastructure &nbsp;·&nbsp; "
        "Set it up like you mean to maintain it</b>",
        ParagraphStyle("ol", fontName="Helvetica", fontSize=9.5, leading=12,
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
        "In <b>azure-100-labs</b> (Azure Repos):",
        s["body"],
    ))
    story.append(numbered([
        "Verify default branch = <b>main</b> in Project settings → Repositories",
        "Create branch: <b>git switch -c feature/day13-repo-setup</b>",
        "Create folders: <b>src/</b>, <b>docs/</b>, <b>pipelines/</b>, <b>infra/</b>",
        "Add <b>.gitignore</b> (node_modules, .env, dist/, IDE files)",
        "Add <b>docs/repo-structure.md</b> describing each folder",
        "Commit: <b>git commit -m 'chore: standardize repo layout and gitignore'</b>",
        "Push: <b>git push -u origin feature/day13-repo-setup</b>",
        "Review repo permissions: Contributors vs Readers",
    ]))

    story.append(Paragraph(".gitignore essentials", s["h1"]))
    cmd = Table([[Paragraph(
        "<font face='Courier' size='7.5'>"
        "node_modules/<br/>"
        "dist/ build/<br/>"
        ".env .env.*<br/>"
        "*.log .DS_Store<br/>"
        ".vscode/ __pycache__/"
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
        "Default branch verified as main",
        "Standard folder layout committed",
        ".gitignore blocks secrets and build artifacts",
        "Feature branch pushed; remote verified",
    ]))

    story.append(Paragraph("Tomorrow — Day 14", s["h2"]))
    story.append(Paragraph(
        "Pull requests & code review — the human gate before merge.",
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


def build_day14(path: Path):
    s = styles()
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm,
        title="Day 14 — Pull Requests & Code Review | 100DaysOfAzureDevOps",
        author="Personal learning series",
    )
    story = []

    story.append(header_bar(14, "Pull Requests & Code Review"))
    story.append(Spacer(1, 10))
    story.append(Paragraph("100 Days of Azure DevOps", s["cover_sub"]))
    story.append(Paragraph("Day 14 Handout — PR templates, work items & review etiquette", s["cover_title"]))
    story.append(Paragraph(
        "Learning in public · Personal lab only · Educational content · Not a sales pitch",
        s["cover_sub"],
    ))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1, color=TEAL, spaceAfter=8))

    anatomy = [
        ["PR Element", "What it captures", "Good practice"],
        ["Title", "One-line change summary", "Avoid 'fix' / 'update' — say what changed"],
        ["Description", "What / Why / How verified", "Use a template so fields are never blank"],
        ["Work item link", "Boards ↔ Repos traceability", "Link User Story or Task (AB#123)"],
        ["Files review", "Diff of every changed file", "Self-review before assigning reviewers"],
        ["Reviewers", "Human gate before merge", "Ask for risk & clarity feedback, not rubber stamps"],
    ]
    story.append(section_box("Architecture A — pull request anatomy", anatomy,
                             col_widths=[35 * mm, 65 * mm, 80 * mm]))

    story.append(Spacer(1, 6))
    etiquette = [
        ["Role", "Do this", "Avoid this"],
        ["Author", "Fill template; self-review Files tab", "Empty description; surprise reviewers"],
        ["Reviewer", "Ask about edge cases and risk", "Personal comments; nitpick without context"],
        ["Team", "Approve when merge-ready", "Approve out of politeness"],
        ["Process", "Link work items; keep PRs small", "Mega-PRs that take a day to read"],
    ]
    story.append(section_box("Architecture B — review etiquette that scales", etiquette,
                             col_widths=[32 * mm, 74 * mm, 74 * mm]))

    story.append(Paragraph("One-liner to remember", s["h1"]))
    one = Table([[Paragraph(
        "<b>A PR is a contract between the author and the team &nbsp;·&nbsp; "
        "If the contract is empty, do not expect a safe merge</b>",
        ParagraphStyle("ol", fontName="Helvetica", fontSize=9.5, leading=12,
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
        "In your local clone of <b>azure-100-labs</b>:",
        s["body"],
    ))
    story.append(numbered([
        "Create branch: <b>git switch -c feature/day14-pr-template</b>",
        "Create folder: <b>.azuredevops/</b>",
        "Add <b>pull_request_template.md</b> with What / Why / Test plan / Risk",
        "Commit: <b>git commit -m 'chore: add pull request template'</b>",
        "Push: <b>git push -u origin feature/day14-pr-template</b>",
        "Open PR in Azure Repos: feature → main; fill template; link a work item",
        "Self-review the Files tab before inviting reviewers",
    ]))

    story.append(Paragraph("PR template skeleton", s["h1"]))
    cmd = Table([[Paragraph(
        "<font face='Courier' size='7.5'>"
        "## What<br/>"
        "-<br/>"
        "## Why<br/>"
        "-<br/>"
        "## Test plan<br/>"
        "- [ ] Local build / sanity check<br/>"
        "- [ ] Linked work item<br/>"
        "- [ ] No secrets in the diff<br/>"
        "## Risk<br/>"
        "- Low / Med / High"
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
        "PR template committed under .azuredevops/",
        "PR opened with filled description",
        "Work item linked from Boards",
        "Self-review completed on Files tab",
    ]))

    story.append(Paragraph("Tomorrow — Day 15", s["h2"]))
    story.append(Paragraph(
        "Advanced Git — rebase, squash, and history hygiene for clean CI/CD.",
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


def build_day15(path: Path):
    s = styles()
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm,
        title="Day 15 — Advanced Git: Rebase & Squash | 100DaysOfAzureDevOps",
        author="Personal learning series",
    )
    story = []

    story.append(header_bar(15, "Advanced Git: Rebase & Squash"))
    story.append(Spacer(1, 10))
    story.append(Paragraph("100 Days of Azure DevOps", s["cover_sub"]))
    story.append(Paragraph("Day 15 Handout — Merge, rebase, squash & history hygiene", s["cover_title"]))
    story.append(Paragraph(
        "Learning in public · Personal lab only · Educational content · Not a sales pitch",
        s["cover_sub"],
    ))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1, color=TEAL, spaceAfter=8))

    ops = [
        ["Operation", "Effect on history", "Best used for"],
        ["Merge", "Keeps topology + merge commit", "Preserve exact integration story"],
        ["Rebase", "Rewrites SHAs; linear history", "Update feature branch onto latest main"],
        ["Squash", "Many commits → one commit", "Ship one coherent change via PR"],
        ["Cherry-pick", "Copies a single commit SHA", "Hotfix onto another branch line"],
    ]
    story.append(section_box("Architecture A — history operations compared", ops,
                             col_widths=[32 * mm, 70 * mm, 78 * mm]))

    story.append(Spacer(1, 6))
    safety = [
        ["Rule", "Do this", "Never do this"],
        ["Shared branches", "Merge into main via PR", "Rebase / rewrite published main"],
        ["Feature branches", "Rebase onto origin/main before PR", "Leave stale base with surprise conflicts"],
        ["Force push", "git push --force-with-lease", "Blind git push --force"],
        ["Conflicts", "Resolve + test, then continue", "Abort and force-merge without reading"],
        ["PR to main", "Squash or atomic commits", "Dump 30 WIP commits onto main"],
    ]
    story.append(section_box("Architecture B — history hygiene for CI/CD", safety,
                             col_widths=[38 * mm, 72 * mm, 70 * mm]))

    story.append(Paragraph("One-liner to remember", s["h1"]))
    one = Table([[Paragraph(
        "<b>Rebase rewrites history &nbsp;·&nbsp; Merge preserves the plot &nbsp;·&nbsp; "
        "Choose based on whether teammates already depend on that timeline</b>",
        ParagraphStyle("ol", fontName="Helvetica", fontSize=9.5, leading=12,
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
        "In your local clone of <b>azure-100-labs</b>:",
        s["body"],
    ))
    story.append(numbered([
        "Create branch: <b>git switch -c feature/day15-rebase-lab</b>",
        "Make 2–3 small commits (notes / docs)",
        "Fetch and rebase: <b>git fetch origin && git rebase origin/main</b>",
        "If conflicts: fix → <b>git add</b> → <b>git rebase --continue</b>",
        "Push safely: <b>git push --force-with-lease</b>",
        "Open PR; prefer squash merge for WIP cleanup",
        "Document choice in <b>docs/merge-strategy.md</b>",
    ]))

    story.append(Paragraph("Core commands", s["h1"]))
    cmd = Table([[Paragraph(
        "<font face='Courier' size='7.5'>"
        "git fetch origin<br/>"
        "git rebase origin/main<br/>"
        "git rebase --abort   # if needed<br/>"
        "git push --force-with-lease<br/>"
        "git cherry-pick &lt;sha&gt;"
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
        "I can explain merge vs rebase vs squash",
        "Feature branch rebased onto origin/main",
        "Used --force-with-lease (not blind --force)",
        "Merge strategy notes documented",
    ]))

    story.append(Paragraph("Tomorrow — Day 16", s["h2"]))
    story.append(Paragraph(
        "Git hooks & pre-commit — local gates before the server gates.",
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
    2: build_day02,
    3: build_day03,
    4: build_day04,
    5: build_day05,
    6: build_day06,
    7: build_day07,
    8: build_day08,
    9: build_day09,
    10: build_day10,
    11: build_day11,
    12: build_day12,
    13: build_day13,
    14: build_day14,
    15: build_day15,
}


def main(days=None):
    OUT.mkdir(parents=True, exist_ok=True)
    days = days or sorted(HANDOUTS.keys())
    publish_map = {
        1: DAYS / "day-01-cloud-fundamentals" / "handout.pdf",
        2: DAYS / "day-02-portal-cli-powershell" / "handout.pdf",
        3: DAYS / "day-03-arm-basics" / "handout.pdf",
        4: DAYS / "day-04-devops-principles" / "handout.pdf",
        5: DAYS / "day-05-azure-devops-services" / "handout.pdf",
        6: DAYS / "day-06-azure-devops-org" / "handout.pdf",
        7: DAYS / "day-07-azure-boards" / "handout.pdf",
        8: DAYS / "day-08-azure-test-plans" / "handout.pdf",
        9: DAYS / "day-09-azure-artifacts" / "handout.pdf",
        10: DAYS / "day-10-phase-1-recap" / "handout.pdf",
        11: DAYS / "day-11-git-fundamentals" / "handout.pdf",
        12: DAYS / "day-12-branching-strategies" / "handout.pdf",
        13: DAYS / "day-13-azure-repos-setup" / "handout.pdf",
        14: DAYS / "day-14-pull-requests" / "handout.pdf",
        15: DAYS / "day-15-advanced-git" / "handout.pdf",
    }
    for d in days:
        fn = HANDOUTS[d]
        out = OUT / f"day-{d:02d}-handout.pdf"
        fn(out)
        pub = publish_map.get(d)
        if pub is not None:
            pub.parent.mkdir(parents=True, exist_ok=True)
            pub.write_bytes(out.read_bytes())
            print("Also wrote", pub)


if __name__ == "__main__":
    main()
