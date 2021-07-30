import requests
from datetime import datetime

USERNAME = "darkdeveloper"
TOKEN = "hbfdsu654tgjfhbg7458b"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

GRAPH_ID = "graph1"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(
#     url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime(year=2021, month=6, day=24).strftime("%Y%m%d")
pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{today}"


pixel_config = {
    "quantity": "4",
}

response = requests.delete(
    url=pixel_endpoint, headers=headers)
print(response.text)
