import pandas as pd
import glob
import fpdf
from pathlib import Path

filepaths = glob.glob('invoices/*.xlsx')

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    pdf = fpdf.FPDF(orientation='P',unit='mm',format='A4')
    pdf.add_page()
    pdf.set_font(family='Times',size=16,style='B')
    filename = Path(filepath).stem
    invoice_nr = filename.split('-')[0]
    pdf.cell(w=50,h=8,txt=f"Invoice nr. {invoice_nr}")
    pdf.output(f'PDFs/{filename}.pdf')

