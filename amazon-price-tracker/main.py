import requests
import smtplib
from bs4 import BeautifulSoup

my_email = "codeschooldxd@gmail.com"
password = "ILoveRias"

headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0)"
    " Gecko/20100101 Firefox/90.0"
}
url = ("https://www.amazon.com/15-BR075NR-15M-BP012DX-15M-BP011DX-15M-BQ021DX"
       "-17M-AE111DX/dp/B07CVJZPTT/ref=sr_1_1?dchild=1&keywords=hp%2Bkeyboard"
       "%2Bskin&qid=1625384060&sr=8-1&th=1")

response = requests.get(
    url=url,
    headers=headers
)

soup = BeautifulSoup(response.text, "lxml")
title_tag = soup.find(
    name="span", class_="a-size-large product-title-word-break")
title = title_tag.getText().strip()
price_tag = soup.find(name="span", class_="a-size-medium a-color-price")
price = float(price_tag.getText().strip()[1:])

if price <= 4.99:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="classwaliid@gmail.com",
            msg=f"Subject:New Product Deal on {title}\n\n The product you like"
            f"is available for ${price}\n{url} ".encode('utf-8')
        )
