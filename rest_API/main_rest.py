import pandas
from flask import Flask, render_template

app = Flask(__name__)

df = pandas.read_csv("dictionary.csv")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def about(word):
    definition = df.loc[df["word"] == word]["definition"].squeeze()
    return {"definition": definition,
            "word": word,
            }


if __name__ == "__main__":
    app.run(debug=True)
