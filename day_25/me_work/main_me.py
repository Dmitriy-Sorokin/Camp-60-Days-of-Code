import pandas
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("files/*txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")


for filename in filepaths:
    pdf.add_page()
    print(filename)
    correct_name = filename.split(".")[0].replace("files\\", "").capitalize()
    # print(correct_name)
    with open(filename, "r") as file:
        text_in_file = file.read()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=correct_name, ln=True)

    pdf.set_font(family="Times", size=14)
    pdf.multi_cell(w=190, h=8, txt=text_in_file)

pdf.output("me_pdf/one.pdf")
