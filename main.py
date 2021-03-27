import smtplib
import datetime as dt
import random

# People's emails you want to send emails to
people = []

def send_quote_mail(quote,to):
    # Your email account username and password eg my_email = test@email.com password = 123
    my_email = ""
    password = ""
    # Your stmp service provider eg. "smtp.gmail.com" for gmail
    with smtplib.SMTP("",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to, msg=f"Subject:Monday Motivation\n\n{quote}")

with open("quotes.txt") as file:
    data = file.read()
    data = data.split("\n")

now = dt.datetime.now()

if now.weekday() == 0:
    picked_quote = random.choice(data)
    for to in people:
        send_quote_mail(picked_quote,to)