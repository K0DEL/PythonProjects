import requests
# import datetime

alpha_apikey = "02IFJTGK2BPT60OZ"
news_apikey = "950e6a9f8004474ca1b69ccee14edddc"
ALPHA_ENDPOINT = "https://www.alphavantage.co/query?"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything?"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day
# before yesterday then print("Get News").
alpha_params = {
    "apikey": alpha_apikey,
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
}

alpha_response = requests.get(url=ALPHA_ENDPOINT, params=alpha_params).json()[
    'Time Series (Daily)']


# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list
# comprehensions on Python dictionaries. e.g. [new_value for (key, value)
# in dictionary.items()]
# yesterday = str(datetime.datetime.today() -
#                 datetime.timedelta(days=1)).split(" ")[0]
# print(response[yesterday])
data_list = [value for (key, value) in alpha_response.items()]
yesterday_data = data_list[0]
yesterday_close_price = float(yesterday_data['4. close'])

# TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_close_price = float(day_before_yesterday_data['4. close'])

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20,
# but the positive difference is 20.
# Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = abs(yesterday_close_price - day_before_yesterday_close_price)

# TODO 4. - Work out the percentage difference in price between closing price
# yesterday and closing price the day before yesterday.
diff_percent = (difference / yesterday_close_price) * 100

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

# STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces
# for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles
# related to the COMPANY_NAME.
if diff_percent > 5:
    news_params = {
        "apiKey": news_apikey,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params).json()
    articles = news_response["articles"]


# TODO 7. - Use Python slice operator to create a list that contains the first
# 3 articles.
# Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
three_articles = articles[:3]
print(three_articles)

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to
# your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and
# description using list comprehension.
articles_list = [
    f"Headline: {article['title']}. \nBrief: {article['description']}"
    for article in three_articles]


# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds
and prominent investors are required to file by the SEC The 13F filings
show the funds' and investors' portfolio positions as of March 31st,
near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds
and prominent investors are required to file by the SEC The 13F filings
show the funds' and investors' portfolio positions as of March 31st,
near the height of the coronavirus market crash.
"""
