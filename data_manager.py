import requests

sheety_endpoint = "https://api.sheety.co/78a262a8e64813691484e7fc96e63021/flightDeals/prices"
sheety_header = {"Authorization": "Bearer kjsfiuy8y3rk;hsafluy"}

class DataManager:

    def __int__(self):
        self.destination_data = {}

    def read_data(self):
        flight_data = requests.get(url=sheety_endpoint, headers=sheety_header)
        self.destination_data = flight_data.json()["prices"]
        return self.destination_data

    def update_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iatacode"]
                }
            }
            response = requests.put(url=f"{sheety_endpoint}/{city['id']}", json=new_data, headers=sheety_header)
            print(response.text)


