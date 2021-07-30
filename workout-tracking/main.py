import requests
from datetime import datetime

APP_ID = "ce0ecf55"
API_KEY = "25fc0fd0af35fbad31515bb0c5ea6b1a"

SHEETY_TOKEN = "nc34978cbfvhrgcf6743bnpiex3jf834ncf4738t2gfr3"

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = ("https://api.sheety.co/1b098fe54df9e50132b7149d50b3466e/"
                   "myWorkouts/workouts")

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

query = input("Enter Your Exercise: ")

nutritionix_params = {
    "query": query,
    "gender": "male",
    "weight_kg": 60,
    "height_cm": 175,
    "age": 20
}

response = requests.post(url=nutritionix_endpoint,
                         json=nutritionix_params,
                         headers=nutritionix_headers)
excerises = response.json()['exercises']


sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}",
    "Content-Type": "application/json"
}

now = datetime.now()
time = now.strftime("%X")
today = now.strftime("%d/%m/%Y")

for exercise in excerises:

    sheety_params = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
        }
    }

    response = requests.post(
        url=sheety_endpoint, json=sheety_params, headers=sheety_headers)
    print(response.text)
