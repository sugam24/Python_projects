import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "ca4d132635f42ab85e8ab531bdd54030"

weather_params = {
    "lat": 27.7360,
    "lon": 85.3601,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code)
