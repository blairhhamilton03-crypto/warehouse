from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import random

# File name
pdf_path = "period_symptom_tracking_template_super_cute.pdf"

# Styles
styles = getSampleStyleSheet()
title_style = styles["Title"]
title_style.textColor = colors.darkmagenta

# Table columns
columns = [
    "Date",
    "Cycle Day",
    "Pain Location",
    "Pain Intensity (0-10)",
    "Pain Type",
    "Duration",
    "Associated Symptoms",
    "Possible Triggers",
    "Relief Methods Tried",
    "Impact on Daily Life"
]

# Cute affirmations
affirmations = [
    "✨ You’re stronger than you think! ✨",
    "🌸 Rest, hydrate, and be kind to yourself 🌸",
    "💖 Every cycle is a reminder of your resilience 💖",
    "🌙 Slow down, breathe, and trust your body 🌙",
    "☀️ Brighter days are always ahead ☀️",
    "🌷 Take it one step at a time 🌷"
]

# Create document
doc = SimpleDocTemplate(pdf_path, pagesize=A4)
elements = []

# Number of pages (~1 month of tracking)
num_pages = 4

for page in range(num_pages):
    # Title
    elements.append(Paragraph("🌸✨ Period Symptom Tracking Template ✨🌸", title_style))
    elements.append(Spacer(1, 0.2 * inch))

    # Subheading
    elements.append(Paragraph("Track your cycle with love and care 💕", styles["Normal"]))
    elements.append(Spacer(1, 0.2 * inch))

    # Create table
    data = [columns] + [["" for _ in columns] for _ in range(12)]
    table = Table(data, repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightpink),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.darkmagenta),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 6),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.pink),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 0.3 * inch))

    # Random affirmation
    affirmation = random.choice(affirmations)
    elements.append(Paragraph(affirmation, styles["Italic"]))

    if page < num_pages - 1:
        elements.append(PageBreak())

# Build PDF
doc.build(elements)

print(f"PDF created: {pdf_path}")
