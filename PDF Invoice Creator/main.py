import pandas as pd
import glob
import fpdf
from pathlib import Path

filepaths = glob.glob('invoices/*.xlsx')

for filepath in filepaths:

    pdf = fpdf.FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    # Get the name of the file
    filename = Path(filepath).stem
    invoice_nr, date = filename.split('-')

    # Puts the title of the invoice
    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=0, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1)

    # Create the date
    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=0, h=8, txt=f"Date: {date}", ln=3)
    pdf.cell(w=0, h=12, ln=2)

    # Add the column names
    df = pd.read_excel(filepath, sheet_name='Sheet 1')

    cols = df.columns
    cols_names = [item.replace("_", ' ').title() for item in cols]
    for col in range(len(cols_names)):
        pdf.set_font(family='Times', size=12, style='B')
        pdf.cell(w=38, h=12, txt=cols_names[col], align='C', border=1)
    pdf.cell(w=0, h=12, ln=1)

    # Add rows
    for index, row in df.iterrows():
        for col in range(len(cols)):
            name_col = cols[col]
            pdf.set_font(family='Times', size=8)
            pdf.cell(w=38, h=9, txt=str(row[name_col]), align='L', border=1)
        pdf.cell(w=0, h=9, ln=1)
    pdf.cell(w=0, h=0, ln=1)

    # Total
    total_invoice = df['total_price'].sum()
    pdf.set_font(family='Times', size=8, style='B')
    pdf.cell(w=114, h=9)
    pdf.cell(w=38, h=9, txt='Total Sum', align='L', border=1)
    pdf.cell(w=38, h=9, txt=f"$ {total_invoice}", align='L', border=1,ln=1)

    pdf.cell(w=0, h=9, ln=3)

    # Total sentence
    pdf.set_font(family='Times', size=14, style='B')
    pdf.cell(w=0, h=9, txt=f"Total of the price is $ {total_invoice}", align="L", ln=1)

    # Logo
    pdf.set_font(family='Times', size=20, style='B')
    pdf.cell(w=30, h=9, txt="Python", align='L')
    pdf.image('pythonhow.png',w=10)


    pdf.output(f'PDFs/{filename}.pdf')
