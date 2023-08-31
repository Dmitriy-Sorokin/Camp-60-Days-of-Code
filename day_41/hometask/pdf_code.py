from fpdf import FPDF


class Converter:
    def __init__(self, id_product, name_product, price_product):
        self.id_product = id_product
        self.name_product = name_product
        self.price_product = price_product

    def add_pdf_file(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{self.id_product}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.name_product}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.price_product}", ln=1)

        pdf.output("receipt.pdf")
