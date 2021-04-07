import pandas
import smtplib
import datetime as dt
import random

my_email = "shruthi41098@gmail.com"
password = "Shruthigmail123"

now = dt.datetime.now()
today_tuple = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthdays_name = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        contents = letter.read()
        birthday_message = contents.replace("[NAME]", birthdays_name["name"])

    with (smtplib.SMTP("smtp.gmail.com")) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthdays_name["email"],
            msg=f"Subject:Happy Birthday!\n\n{birthday_message}"
        )




