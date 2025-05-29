import smtplib
import datetime as dt
import random

my_email = "dahalsugam24@gmail.com"
password = "kfvt chnn nnyv gefm"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        print(quote)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject = Motivation\n\n{quote}")






















# import smtplib
#
# my_email = "dahalsugam24@gmail.com"
# password = "kfvt chnn nnyv gefm"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="sugam.d24@gmail.com", msg="Subject:Hello\n\nHey!!! What's up?")

#
# import datetime as dt
# now = dt.datetime.now()
# day_of_week = now.weekday()
# print(day_of_week)

