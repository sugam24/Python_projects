import smtplib
import datetime as dt
import pandas

MY_EMAIL = "dahalsugam24@gmail.com"
MY_PASSWORD = "123456"

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict()

birthdays_dict = {data_row.month: data_row.day for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = "letter.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person.name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person.email,
                            msg=f"Subject:HAPPY BIRTHDAY!\n\n{contents}")



