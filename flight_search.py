import requests


# class FlightSearch:
#
#     def __int__(self):
#         self.flight_endpoint = "https://api.tequila.kiwi.com/v2/search"
#         self.flight_API = "PJ9RUdtOSMnp-9WrJwLimDG5iY2Vi-YP"
#
#     def run_search(self, city, from_date, to_date):
#         flight_params = {
#                         "apikey": self.flight_API,
#                         "fly_from": "SEA",
#                         "fly_to": city,
#                         "date_from": from_date,
#                         "date_to": to_date,
#                         }
#         search = requests.get(url=self.flight_endpoint, json=flight_params)


flight_endpoint = "https://api.tequila.kiwi.com/v2/search"
flight_API = "PJ9RUdtOSMnp-9WrJwLimDG5iY2Vi-YP"


        flight_params = {
                        "apikey": self.flight_API,
                        "fly_from": "SEA",
                        "fly_to": city,
                        "date_from": from_date,
                        "date_to": to_date,
                        }
        search = requests.get(url=self.flight_endpoint, json=flight_params)

tomorrow_date = datetime.now() + timedelta(days=1)
tomorrow_date = tomorrow_date.strftime("%m/%d/%Y")

six_month_date = datetime.now() + timedelta(months=6)
six_month_date = six_month_date.strftime("%m/%d/%Y")