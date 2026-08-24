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


# Registry for future days (extend over time)
HANDOUTS = {
    1: build_day01,
    2: build_day02,
    3: build_day03,
    4: build_day04,
}


def main(days=None):
    OUT.mkdir(parents=True, exist_ok=True)
    days = days or sorted(HANDOUTS.keys())
    publish_map = {
        1: DAYS / "day-01-cloud-fundamentals" / "handout.pdf",
        2: DAYS / "day-02-portal-cli-powershell" / "handout.pdf",
        3: DAYS / "day-03-arm-basics" / "handout.pdf",
        4: DAYS / "day-04-devops-principles" / "handout.pdf",
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
