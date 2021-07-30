import datetime as dt
import pandas
import smtplib
import random
##################### Extra Hard Starting Project ###################### noqa E501

my_email = "codeschooldxd@gmail.com"
password = "ILoveRias"

recipients = []


def pick_template():
    file_no = random.randint(1, 3)
    with open(f"./letter_templates/letter_{file_no}.txt") as file:
        content = file.read()
    return content.replace('Angela', 'Rider OP')


def send_mail():
    for recipient in recipients:
        content = pick_template().replace('[NAME]', recipient["Name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=recipient["Email"],
                msg=f"Subject:Happy Birthday\n\n{content}"
            )


# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
data = pandas.read_csv("birthdays.csv")
for (index, rows) in data.iterrows():
    if(rows.day == today.day and rows.month == today.month):
        recipient = {
            "Name": rows['name'],
            "Email": rows['email']
        }
        recipients.append(recipient)


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv # noqa E501


# 4. Send the letter generated in step 3 to that person's email address.
send_mail()
