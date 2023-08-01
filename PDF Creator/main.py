from fpdf import FPDF
import pandas as pd

# P-> Portrait, L-> Landscape
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pages = row["Pages"]
    for page in range(pages):
        pdf.add_page()

        pdf.set_font(family="Times", style="B", size=18)
        pdf.set_text_color(153, 0, 0)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="C", ln=1)
        pdf.line(10, 22, 200, 22)

        # Add lines in between
        for y in range(32, 262, 10):
            pdf.line(10, y, 200, y)

        # Footer
        pdf.ln(242)
        pdf.set_font(family="Times", style="I", size=12)
        pdf.line(10, 262, 200, 262)
        pdf.cell(w=170, h=12, txt="Footer", align="L")
        pdf.cell(w=20, h=12, txt=f"{page + 1}/{pages}", align="R", ln=1)


pdf.output("output.pdf")
