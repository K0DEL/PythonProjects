import requests
from flight_data import FlightData
# import json

kiwi_search_endpoint = "https://tequila-api.kiwi.com/v2/search"

kiwi_location_endpoint = "https://tequila-api.kiwi.com/locations/query"

KIWI_API_KEY = "Vq3IS8MkD3HD3aHyJzXSyLCQrhYFKvB5"

kiwi_header = {
    "apikey": KIWI_API_KEY,
}


class FlightSearch:

    def search_flight(self, name):
        # print("get destination codes triggered")

        kiwi_params = {
            "location_types": "city",
            "term": name
        }
        response = requests.get(url=kiwi_location_endpoint, params=kiwi_params,
                                headers=kiwi_header)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code,
                      from_time, to_time):
        kiwi_params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 3,
            "curr": "GBP"
        }
        # print(kiwi_params)
        response = requests.get(url=kiwi_search_endpoint,
                                headers=kiwi_header, params=kiwi_params)
        # with open("data.json", "w") as file:
        #     json.dump(response.json(), file, indent=4)

        try:
            data = response.json()["data"][0]
            x = int(len(data["route"])/2 - 1)
            # print(x, type(x))
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][x]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
            stop_overs=x,
            via_city=data["route"][0]["cityTo"],
        )
        return flight_data
