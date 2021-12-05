import requests
import os
from twilio.rest import Client

account_sid = "ACb36156c0ba00be6be8c1c020a57a5189"
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

parameters = {
    "lat": 11.42,
    "lon": 59.49,
    "exclude": "current,minutely,daily",
    "appid": os.environ.get("OWM_API_KEY")
}


request = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
request.raise_for_status()
weather_data = request.json()
# weather_id_test = weather_data["hourly"][0]["weather"][0]["id"]
hour_slice = weather_data["hourly"][:12]

will_rain = False

# test for loop: I want the ID for each hour in the next 12 hours.
for hour in hour_slice:
    condition = hour["weather"][0]["id"]
    # print(condition)
    if int(condition) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from_='+17404869840',
        to='+17176768920',
    )
    print(message.status)
# weather_ids = [(hour["weather"][0]["id"]) for hour in hour_slice]
# for wid in weather_ids:
#     if wid < 700:
#         print("Bring an umbrella!")
# print(weather_ids)
