<!-- # sqlalchemy-challenge



Analyze and Explore the Climate Data

file: climate_starter.ipynb

Code performs the following tasks:

1. Creates a connection to the hawaii.sqlite database using SQLAlchemy create_engine().
2. Uses SQLAlchemy to reflect tables into classes.
3. Performs precipitation analysis by querying previous 12 months of data from the latest date in the database.
4. Loaded precipitation data into a Pandas DataFrame.
5. Plot the precipitation data.
6. Provided summary statistics for the precipitation data.
7. Performs station analysis by querying to calculate the total number of stations in the dataset.
8. Queries for the most active stations.
9. Filters by the station with the most observations.
10. Plots the results in a histogram.

Climate App Design

file: app.py

Code performs the following tasks:

1. Using Flask, creates the following routes: /, precipitation, stations, temperature, start, and start/end. Start returns the min, max, and 
avg temperature beginning on the start date input by the user. Start/end returns the min, max, and avg temperatures between the start and end
dates provided by the user.
2. All API data is returned as a valid JSON response. -->