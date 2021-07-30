import requests

SHEETY_TOKEN = "vjdfshgvreyfvbvf43567t298463cbvfg82476f49483chdc"

sheety_endpoint = (
    "https://api.sheety.co/1b098fe54df9e50132b7149d50b3466e/"
    "flightDeals/prices")

sheety_header = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}


class DataManager:

    def __init__(self):
        self.city_data = []
        self.get_city_data()

    def get_city_data(self):
        response = requests.get(url=sheety_endpoint)
        print(response.status_code)
        if response.status_code == 402:
            self.city_data = [
                {'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54,
                 'id': 2},
                {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42,
                 'id': 3},
                {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485,
                 'id': 4},
                {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551,
                 'id': 5},
                {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95,
                 'id': 6},
                {'city': 'Kuala Lumpur', 'iataCode': 'KUL',
                    'lowestPrice': 414, 'id': 7},
                {'city': 'New York', 'iataCode': 'NYC',
                    'lowestPrice': 240, 'id': 8},
                {'city': 'San Francisco', 'iataCode': 'SFO',
                    'lowestPrice': 260, 'id': 9},
                {'city': 'Cape Town', 'iataCode': 'CPT',
                    'lowestPrice': 378, 'id': 10},
                {'city': 'Doha', 'iataCode': 'DOH', 'lowestPrice': 1000,
                 'id': 11}
            ]
        else:
            self.city_data = response.json()['prices']

    def update_city_data(self):
        for data in self.city_data:
            new_data = {
                "price": {
                    "iataCode": data['iataCode'],
                }
            }
            response = requests.put(
                url=f"{sheety_endpoint}/{data['id']}", json=new_data)
            print(response.status_code)
