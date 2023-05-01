# Import the dependencies.

import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import pandas as pd
import datetime as dt 


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
#reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

#Default route
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"//api/v1.0/tobs<br/>"
        f"Enter query start date in this format /api/v1.0/2016-8-17 for this route: /api/v1.0/<start><br/>"
        f"Enter query start and end date in this format /api/v1.0/2010-5-5/2016-8-17 for this route: /api/v1.0/<start>/<end><br/>"
    )

#Returns last 12 months of precip data by date based on the 1 year ago date of 2016-08-23
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Query last 12 precip
    sel = [Measurement.date, 
       Measurement.prcp]    
    results = session.query(*sel).\
    filter(Measurement.date >= '2016-08-23').\
    order_by(Measurement.date).all()

    session.close()

    # Convert list of tuples into normal list
    precip_year = list(np.ravel(results))
    
    return jsonify(precip_year)

#Returns a distinct list of all weather stations.
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of stations"""
    # Query all stations
    results = session.query(Measurement.station).group_by(Measurement.station).\
    order_by(func.count(Measurement.station).desc()).all()

    session.close()

        # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))
    
    return jsonify(all_stations)

#Returns temp for the most active weather station for one year back from 2017-8-23 by date.
@app.route("/api/v1.0/tobs")
def temps():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Query last 12 temp
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date >= query_date).\
    order_by(Measurement.date).all()

    session.close()

    # Convert list of tuples into normal list
    temp_year = list(np.ravel(results))
    
    return jsonify(temp_year)
    
    
@app.route("/api/v1.0/<start>")
def tempsbydate(start):
    
#Returns min, max, and avg since last date entered by user.
    """Fetch the Min, avg, and max for the date
       the path variable supplied by the user in yyyy-d-m format, or a 404 if not."""
    # Create our session (link) from Python to the DB

    session = Session(engine)

    result = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= start).all()
    
    results = list(np.ravel(result))
    session.close()
    return jsonify(results)

#Returns min, max, and avg between start and end dates entered by user.
@app.route("/api/v1.0/<start>/<end>")
def tempsbydaterange(start, end):
    
    """Fetch the Min, avg, and max for the date range
       the path variable supplied by the user, or a 404 if not."""
    # Create our session (link) from Python to the DB

    session = Session(engine)

    result = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
                           filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    
    results = list(np.ravel(result))
    session.close()
    return jsonify(results)

if __name__ == '__main__':
   app.run(debug=True)

