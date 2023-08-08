import pandas
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*xlsx")


for i in filepaths:
    df = pandas.read_excel(i, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(i).stem
    invoice_nr = filename.split("-")[0]
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoices nr.{invoice_nr}")
    pdf.output(f"pdfs/{filename}.pdf")

