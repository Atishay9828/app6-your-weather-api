from flask import Flask, render_template as rt
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("data_small/stations.txt" ,skiprows= 17 )
stations = stations[["STAID" , "STANAME                                 "]]
@app.route("/")
def home():
    return rt("home.html" , data= stations.to_html())
@app.route("/api/v1/<station>/<date>")
def station_date(station,date):
    filename= "data_small\TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename,skiprows= 20, parse_dates= ["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {
        "temperature" : temperature ,
        "date" : date ,
        "station" : station 
    }
@app.route("/api/v1/<station>")
def station(station):
    filename= "data_small\TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename,skiprows= 20, parse_dates= ["    DATE"])
    return df.to_dict(orient= "records")

@app.route("/api/v1/year/<station>/<year>")
def yearly(station,year):
    filename= "data_small\TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename,skiprows= 20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df['    DATE'].str.startswith(str(year))]

    return result.to_dict(orient= "records")

app.run(debug=True)
