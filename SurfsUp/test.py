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

session = Session(engine)
test = session.query(Measurement.tobs).first()
print(test)

#################################################
# Flask Setup
#################################################
#app = Flask(__name__)


#################################################
# Flask Routes
#################################################

    # Query all passengers
  #  results = session.query(Passenger.name, Passenger.age, Passenger.sex).all()

   # session.close()


#if __name__ == '__main__':
#    app.run(debug=True)





