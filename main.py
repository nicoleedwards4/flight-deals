#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from datetime import datetime, timedelta

post_endpoint = "https://api.sheety.co/78a262a8e64813691484e7fc96e63021/flightDeals/prices"

flight_endpoint = "https://api.tequila.kiwi.com/v2/search"

flight_API = "PJ9RUdtOSMnp-9WrJwLimDG5iY2Vi-YP"

tomorrow_date = datetime.now() + timedelta(days=1)
tomorrow_date = tomorrow_date.strftime("%m/%d/%Y")

six_month_date = datetime.now() + timedelta(months=6)
six_month_date = six_month_date.strftime("%m/%d/%Y")

flight_params = {
    "apikey": flight_API,
    "fly_from": ,
    "fly_to": ,
    "date_from": tomorrow_date,
    "date_to": six_month_date,
}

twilio_sid = "AC687a5e19a09a890258ee201b09c3dae2"
twilio_token = "097be1f9f3b59fe73e859e4d0c5e73ec"

