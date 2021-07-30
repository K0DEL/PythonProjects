from bs4 import BeautifulSoup
import requests

# with open("./website.html", encoding="utf-8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)

response = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(response.text, "html.parser")
anchor_tag = soup.find_all(name="a", class_="storylink")
anchor_texts = [tag.getText() for tag in anchor_tag]
anchor_links = [tag.get("href") for tag in anchor_tag]
span_tag = soup.find_all(name="span", class_="score")
anchor_upvotes = [int(tag.getText().split()[0]) for tag in span_tag]
# print(anchor_tag.get("href"))
# upvotes = soup.find(name="span", class_="score").getText()
# print(anchor_texts)
# print(anchor_links)
# print(anchor_upvotes)
print(max(anchor_upvotes))
