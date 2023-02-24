import smtplib
import datetime
import random


now = datetime.datetime.now()
day_of_week = now.weekday()
print(day_of_week)
my_email = "vickesharma8@gmail.com"
my_password = "Mahadevg@1998"

if day_of_week == 1:
    with open("quotes.txt") as quotes:
        all_quotes = quotes.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="vikaskapila15@gmail.com",
                            msg=f"Subject:Monday Motivation \n\n {quote}")
        connection.close()



