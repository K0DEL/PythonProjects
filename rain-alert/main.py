import requests

OW_API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall?"
apikey = "14084f6a421c88fc3ae1b166f6dc6656"

parameters = {
    "lat": 27.492413,
    "lon": 77.673676,
    "appid": apikey,
    "exclude": "current,minutely,daily",
}

response = requests.get(url=OW_API_ENDPOINT, params=parameters)

hourly_data = response.json()["hourly"]

for i in range(0, 12):
    code = int(hourly_data[i]["weather"][0]["id"])
    # print(code)
    if code < 700:
        print("Carry an Umbrella")
        break
