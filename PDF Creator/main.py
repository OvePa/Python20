from fpdf import FPDF
import pandas as pd

# P-> Portrait, L-> Landscape
pdf = FPDF(orientation="P", unit="mm", format="A4")
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=18)
    pdf.set_text_color(153, 0, 0)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="C", ln=1)
    pdf.line(10, 22, 200, 22)


pdf.output("output.pdf")
