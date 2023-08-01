import pandas as pd
import glob
import fpdf
from pathlib import Path

filepaths = glob.glob('invoices/*.xlsx')

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    pdf = fpdf.FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    # Get the name of the file
    filename = Path(filepath).stem
    invoice_nr,date = filename.split('-')

    # Puts the title of the invoice
    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=0, h=8, txt=f"Invoice nr. {invoice_nr}",ln=1)

    # Create the date
    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=0, h=8, txt=f"Date: {date}")

    




    pdf.output(f'PDFs/{filename}.pdf')
