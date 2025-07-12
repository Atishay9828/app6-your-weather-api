from flask import Flask, render_template as rt
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return rt("home.html")
@app.route("/api/v1/<station>/<date>")
def about(station,date):
    filename= "data_small\TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename,skiprows= 20, parse_dates= ["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {
        "temperature" : temperature ,
        "date" : date ,
        "station" : station 
    }

app.run(debug=True)
