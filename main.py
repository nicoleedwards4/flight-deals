from datetime import datetime, timedelta
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.read_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_CODE = "SEA"

for row in flight_matrix:
    city = flight_matrix["city"]
    code = FlightSearch.get_code(city)
    data_manager
    lowest = flight_matrix["lowestPrice"]



tomorrow_date = datetime.now() + timedelta(days=1)
tomorrow_date = tomorrow_date.strftime("%m/%d/%Y")

six_month_date = datetime.now() + timedelta(months=6)
six_month_date = six_month_date.strftime("%m/%d/%Y")



