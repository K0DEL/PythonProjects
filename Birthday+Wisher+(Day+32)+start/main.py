import smtplib
import datetime as dt
import random

my_email = "codeschooldxd@gmail.com"
password = "ILoveRias"
sender_email = "classwaliid@gmail.com"
message = ""


def get_quote():
    global message
    with open("quotes.txt") as file:
        quotes = file.readlines()
        message = f"Subject:Today's Motivation\n\n{random.choice(quotes)}"


def send_mail():
    get_quote()
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=sender_email,
            msg=message
        )


today = dt.datetime.now().weekday()
if today == 1:
    send_mail()
