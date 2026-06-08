from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.set_font(
    "Arial",
    size=16
)

pdf.cell(
    200,
    10,
    txt="Weekly Feedback Report",
    ln=True
)

pdf.set_font(
    "Arial",
    size=12
)

pdf.multi_cell(
    0,
    10,
    "Top complaints include crashes, login issues and payment problems."
)

pdf.output(
    "weekly_report.pdf"
)

print("PDF Generated")