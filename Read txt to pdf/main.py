import glob
import fpdf
from pathlib import Path

filepaths = glob.glob('TextFiles/*.txt')

for filepath in filepaths:
    with open(filepath, 'r') as f:
        text = f.read()

    pdf = fpdf.FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font(family='Times', size=20, style='B')
    filename = Path(filepath).stem
    pdf.cell(w=0, h=20, txt=filename.title(), ln=1)
    pdf.set_font(family='Times', size=15)
    pdf.multi_cell(w=0, h=10, txt=text)
    pdf.output(f"PDFFiles/{filename}.pdf")
