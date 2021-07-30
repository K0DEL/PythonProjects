import smtplib
import requests

my_email = "codeschooldxd@gmail.com"
password = "ILoveRias"

sheety_user_endpoint = ("https://api.sheety.co/1b098fe54df9e50132"
                        "b7149d50b3466e/flightDeals/users")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details. # noqa: E501
    def __init__(self):
        self.sender_mails = []

    def get_mails(self):
        response = requests.get(url=sheety_user_endpoint)
        print(response.status_code)
        if response.status_code == 402:
            self.sender_mails = [
                {'firstname': 'Pintu', 'lastname': 'Kumar',
                 'email': 'classwaliid@gmail.com', 'id': 2},
                {'firstname': 'Ashutosh', 'lastname': 'Yadav',
                 'email': 'ashutoshyadav7891@gmai.com', 'id': 3},
            ]
        else:
            self.sender_mails = response.json()['users']

    def send_mails(self, message):
        self.get_mails()
        for mails in self.sender_mails:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=mails['email'],
                    msg=f"Subject:New Flight Deal\n\n{message}".encode('utf-8')
                )
