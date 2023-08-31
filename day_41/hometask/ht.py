import pandas
from day_41.hometask.pdf_code import Converter

df = pandas.read_csv("articles.csv", dtype={"id": str})


# availability = df.loc[df["id"] == "100", "name"].squeeze()
# print(availability)

class ProductList:
    def __init__(self, product_id):
        self.product_id = product_id

    def available(self):
        availability = df.loc[df["id"] == self.product_id, "id"].squeeze()

        if df["id"].isin([availability]).any():
            return True
        else:
            return False

    def checker(self):
        value = self.product_id
        index = df[df['id'] == value].index
        row = df.loc[index[0]]
        return row["id"], row["name"], row["price"]


choose_user = input("Choose an article to by: ")

product_user = ProductList(choose_user)

if product_user.available():
    id_p, name_p, price_p = product_user.checker()
    gen_pdf = Converter(id_product=id_p, name_product=name_p, price_product=price_p)
    gen_pdf.add_pdf_file()
else:
    print("Wrong ID")
