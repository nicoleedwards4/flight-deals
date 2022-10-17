import requests


class DataManager:

    def __int__(self):
        self.header = {"Authorization": "Bearer kjsfiuy8y3rk;hsafluy"}
        self.endpoint = "https://api.sheety.co/78a262a8e64813691484e7fc96e63021/flightDeals/prices"

    def read_data(self):
        flight_data = requests.get(url=self.endpoint, headers=self.header)
        print(flight_data.text)

    def update_row(self, params):
        response = requests.put(url=self.endpoint, json=params, headers=self.header)
        print(response.text)
