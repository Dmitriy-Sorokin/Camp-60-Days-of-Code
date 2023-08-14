from fpdf import FPDF
import pandas

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pandas.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()

    # set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(254, 0, 0)
    pdf.cell(w=0, h=10, txt=str(row["Topic"]), ln=True)
    pdf.line(10, 21, 200, 21)

    # set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=str(row["Topic"]), ln=True)

    for i in range(row["Pages"]):
        pdf.add_page()
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=str(row["Topic"]), ln=True)

pdf.output("out.pdf")
