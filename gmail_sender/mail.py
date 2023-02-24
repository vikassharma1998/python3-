import smtplib
import datetime as dt

now = dt.datetime.now()
# year = now.year
# month = now.month
day_of_week = now.weekday()
print(day_of_week)

# date_of_birth = dt.datetime(year=2022, month=1, day=25, hour=11, minute=11)
# print(date_of_birth)

my_email = "vickesharma8@gmail.com"
my_password = "Mahadevg@1998"
if day_of_week == 1:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="vikaskapila15@gmail.com",
            msg="subject:Hello sir  \n\n have a nice day")
        connection.close()




