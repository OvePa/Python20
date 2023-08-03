from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)


def read_csv(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    df.columns = ["STAID", "SOUID", "DATE", "TG", "Q_TG"]
    return df


stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations.columns = ["STAID", "STANAME", "CN", "LAT", "LON", "HGHT"]
stations = stations[["STAID", "STANAME"]]


@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    df = read_csv(station)
    temperature = df.loc[df["DATE"] == date]["TG"].squeeze() / 10
    return {"station": station, "date": date, "temperature": temperature}


@app.route("/api/v1/<station>")
def all_data(station):
    df = read_csv(station)
    result = df.to_dict(orient="records")
    return result


@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    df = read_csv(station)
    df["DATE"] = df["DATE"].astype(str)

    result = df[df["DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result


if __name__ == "__main__":
    app.run(debug=True)
