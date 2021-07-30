import requests
import time
from datetime import datetime

MY_LAT = 27.458424  # Your latitude
MY_LONG = 77.688399  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


def check_position():
    if abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <= 5:
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()


# print(sunrise)
# print(time_now.hour)
# print(sunset)


def check_night():
    if(time_now.hour in range(sunset, sunrise)):
        return True
    else:
        return False


# If the ISS is close to my current position
while check_position():
    if check_night():
        print("YES")
    time.sleep(60)

# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
