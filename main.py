#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from datetime import datetime, timedelta
from data_manager import DataManager
# read flight data

flight_matrix = DataManager.read_data()

for row in flight_matrix:
    city = flight_matrix["iataCode"]
    lowest = flight_matrix["lowestPrice"]



tomorrow_date = datetime.now() + timedelta(days=1)
tomorrow_date = tomorrow_date.strftime("%m/%d/%Y")

six_month_date = datetime.now() + timedelta(months=6)
six_month_date = six_month_date.strftime("%m/%d/%Y")



