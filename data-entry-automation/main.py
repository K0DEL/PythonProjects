from selenium import webdriver
import requests
from bs4 import BeautifulSoup
# from selenium.webdriver.common.keys import Keys
firefox_driver_path = "C:/Users/Keshav/Documents/CP/webdriver/geckodriver"


GOOGLE_DOCS_LINK = "https://forms.gle/pmafMcBPT15Rn49d9"
ZELLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"  # noqa E501

headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0)"
    " Gecko/20100101 Firefox/90.0"
}

response = requests.get(ZELLOW_URL, headers=headers)

# with open("data.txt", "w") as file:
#     file.write(str(response.text.encode('utf-8')))

# print(response.text)
soup = BeautifulSoup(response.text, "lxml")

prices_tags = soup.find_all(name="div", class_="list-card-price")
prices = [tag.text[:6] for tag in prices_tags]
link_tags = soup.select("li .list-card-top a")

links = []
for tag in link_tags:
    if tag.get("href").find("https://www.zillow.com") == -1:
        links.append("https://www.zillow.com"+tag.get("href"))
    else:
        links.append(tag.get("href"))

addresses_tags = soup.find_all(name="address", class_="list-card-addr")
addresses = [tag.text for tag in addresses_tags]

length = len(prices)
# print(prices)
# print(links)
# print(addresses)

driver = webdriver.Firefox(executable_path=firefox_driver_path)

for i in range(0, length):
    driver.get(GOOGLE_DOCS_LINK)

    price_bar = driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div'
        '/div[2]/div/div[1]/div/div[1]/input')
    price_bar.click()
    price_bar.send_keys(prices[i])

    link_bar = driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/'
        'div[2]/div/div[1]/div/div[1]/input')
    link_bar.click()
    link_bar.send_keys(links[i])

    address_bar = driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/'
        'div[2]/div/div[1]/div/div[1]/input')
    address_bar.click()
    address_bar.send_keys(addresses[i])

    driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span/span'
    ).click()
