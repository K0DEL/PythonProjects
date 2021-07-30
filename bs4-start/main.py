from bs4 import BeautifulSoup
import requests


response = requests.get(
    "https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")


with open("data.txt", "w") as file:
    file.write(response.text)


# I was unable to make since the website got stricter regarding web scrapping
# and i was unable to get the movie title.
# so i feel sad :(
