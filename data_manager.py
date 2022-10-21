from pprint import pprint
import requests
import os
import creds

sheety_endpoint = creds.SHEETY_ENDPOINT
SHEETY_BEARER = creds.SHEETY_BEARER
sheety_header = {"Authorization": {SHEETY_BEARER}}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def read_data(self):
        flight_data = requests.get(url=sheety_endpoint, headers=sheety_header)
        data = flight_data.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{sheety_endpoint}/{city['id']}", json=new_data, headers=sheety_header)
            print(response.text)


