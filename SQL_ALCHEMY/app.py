import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

last_twelve_months = '2016-08-23'

# Flask Setup

app = Flask(__name__)

#  Routes



@app.route("/")
def welcome():
    """List all available api routes."""
    return f"Available Routes:<br/>" f"/api/v1.0/precipitation<br/><br/>" f"/api/v1.0/stations<br/><br/>" f"/api/v1.0/tobs<br/><br/>" f"/api/v1.0/<start>/<end>" 


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all precipitation scores"""
    # Query all scores
    results = session.query(Measurement.date, func.avg(Measurement.prcp)).filter(Measurement.date >= last_twelve_months).group_by(Measurement.date).all()

    session.close()

    return jsonify(results)
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    st_results = results = session.query(Station.station, Station.name).all()

    session.close()

    return jsonify(st_results)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    t_results = session.query(Measurement.date, Measurement.station, Measurement.tobs).filter(Measurement.date >= last_twelve_months).all()

    session.close()

    return jsonify(t_results)

@app.route("/api/v1.0/<start>/<end>")
def startDateEndDate(start,end):
    session = Session(engine)

    start_end_temp_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    session.close()

    return jsonify(start_end_temp_results)

if __name__ == "__main__":
    app.run(debug=False)
