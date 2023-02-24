import datetime as dt
import random
import smtplib
import pandas

data = pandas.read_csv("birthdays.csv")
now = dt.datetime.now()
today_tuple = (now.month, now.day)
my_user = "vickesharma8@gmail.com"
my_password = "Mahadevg@1998"
birth_day_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birth_day_dict:
    birth_day_person = birth_day_dict[today_tuple]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
        content = file.read()
        msg = content.replace("[NAME]", birth_day_person['name'])
        print(msg)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_user, password=my_password)
        connection.sendmail(from_addr=my_user,
                            to_addrs=birth_day_person['email'],
                            msg=f"Subject:Happy Birthday \n\n {msg}")
        connection.close()
