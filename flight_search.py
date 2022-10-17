import requests
from flight_data import FlightData

flight_endpoint = "https://api.tequila.kiwi.com/v2/search"
flight_api = "Yhnj8M3tmUNPH61OCXEXhOyjksUN-tU5"


class FlightSearch:

    def get_code(self, city):
        # to get the IATA city code:
        iata_endpoint = "https://api.tequila.kiwi.com/locations/query"
        iata_parameters = {
            "term": city,
            "location_types": "city",
        }
        headers = {"apikey": flight_api}
        iata_search = requests.get(url=iata_endpoint, params=iata_parameters, headers=headers)
        results = iata_search.json()["locations"]
        code = results[0]["code"]
        return code

    def run_search(self, orig_city_code, dest_city_code, from_date, to_date):
        flight_params = {
            "fly_from": orig_city_code,
            "fly_to": dest_city_code,
            "date_from": from_date.strftime("%d/%m/%Y"),
            "date_to": to_date.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }
        headers = {"apikey": flight_api}
        search = requests.get(url=flight_endpoint, params=flight_params, headers=headers)
        try:
            data = search.json()["data"][0]
        except IndexError:
            print(f"No flights found for {dest_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            dest_city=data["route"][0]["cityTo"],
            dest_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.dest_city}: ${flight_data.price}")
        return flight_data


