import pandas
import glob
from fpdf import FPDF

filepaths = glob.glob("invoices/*xlsx")


for i in filepaths:
    df = pandas.read_excel(i, sheet_name="Sheet 1")
    print(df)
