import pandas
from flask import Flask, render_template

app = Flask(__name__)

stations = pandas.read_csv("files/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]


@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = f"files/TG_STAID{str(station).zfill(6)}.txt"
    df = pandas.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    return {"station": station,
            "date": date,
            "temp": temperature}


@app.route("/api/v1/<station>")
def all_data(station):
    filename = f"files/TG_STAID{str(station).zfill(6)}.txt"
    df = pandas.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records")
    return result


@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    filename = f"files/TG_STAID{str(station).zfill(6)}.txt"
    df = pandas.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    print(result)
    return result

if __name__ == "__main__":
    app.run(debug=True)
