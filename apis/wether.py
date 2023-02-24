import requests
import datetime as dt

parameters = {
    "lat": 29.838020,
    "lng": 77.628036,
    'formatted': 0
}


response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
iss_latitude = float(data['iss_position']['latitude '])
iss_longitude = float(data['iss_position']['longitude '])
sunset_time = data['results']['sunset'].split('T')[1].split(":")[0]
sunrise_time = data['results']['sunrise'].split('T')[1].split(":")[0]
print(sunset_time)
print(sunrise_time)
now_time = dt.datetime.now()
print(now_time.hour)
