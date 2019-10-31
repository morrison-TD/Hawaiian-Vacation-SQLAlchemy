# 1. import Flask
import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
# Create our session (link) from Python to the DB
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station= Base.classes.station

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

 #3. Define static routes
@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation>"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/start"
        f"/api/v1.0/end"
    )
"""Return a precipitation data"""
@app.route("/api/v1.0/precipitation")
def precipitation():
    session=Session(engine)
    precp=session.query(Measurement.date, Measurement.prcp)
    rain_num=[]
    for date, prcp in precp:
        precp_dict={}
        precp_dict["date"]= date
        precp_dict["prcp"]=prcp
        rain_num.append(precp_dict)
    return jsonify(rain_num)

"""Return a list of stations"""
@app.route("/api/v1.0/stations")
def stations():
    session=Session(engine)
    station_list=session.query(Station.station)
    weather_station=[]
    for station in station_list:
            station_dict={}
            station_dict["station"]=station
            weather_station.append(station_dict)
    return jsonify(weather_station)

"""Return tobs"""
@app.route("/api/v1.0/tobs")
def tobs():
    session=Session(engine)
    tobs_l=session.query(Measurement.tobs, Measurement.date)
    tobs_ct=[]
    for tobs, date in tobs_l:
            tobs_dict={}
            tobs_dict["date"]=date
            tobs_dict["tobs"]= tobs
            tobs_ct.append(tobs_dict)
    return jsonify(date, tobs )

"""Return date"""
@app.route("/api/v1.0/start")
def start_date():
    session=Session(engine)
    start_date=session.query(dt.date='2017-8-23')
    start=[]
    for date in start_date:
        start_d={}
        start_d["date"]=date
        start.append(start_d)
    return jsonify(date)
if __name__ == "__main__":
    app.run(debug=True)
