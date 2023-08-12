import pandas
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def about(word):
    if word == "pillow":
        description = word.upper()
    elif word == "sun":
        description = word.upper()
    return {"description": description,
            "word": word,
            }


if __name__ == "__main__":
    app.run(debug=True)
