import time
import requests
from datetime import datetime as dt
import smtplib

MY_LAT = 27.7360
MY_LONG = 85.3601
MY_EMAIL = "dahalsugam24@gmail.com"
MY_PASSWORD = "123456"


def is_iss_overhead():
    response = requests.get(url="https://api.open-notify.org/iss-now.json", params=parameters)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = float(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = float(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:LOOK UP\n\nThe ISS is above the sky.")
