import smtplib

my_email = "codeschooldxd@gmail.com"
password = "ILoveRias"
sender_email = "classwaliid@gmail.com"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=sender_email,
        msg="Subject:Hello\n\nThis is the body of my email"
    )
