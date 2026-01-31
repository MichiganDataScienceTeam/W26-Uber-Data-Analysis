import json
from timezonefinder import TimezoneFinder
import requests
import time
error_list = []
# Load the existing coordinates
with open('master_coords_with_tz.json', 'r') as f:
    coords = json.load(f)

# Update each entry with a timezone
for city, data in coords.items():
    lat = data['lat']
    lon = data['lon']
    timezone = data['timezone']
    url = f'https://archive-api.open-meteo.com/v1/archive?latitude={lat}&longitude={lon}&timezone={timezone}&start_date=2016-01-01&end_date=2016-12-31&temperature_unit=fahrenheit&hourly=apparent_temperature&hourly=is_day&hourly=rain&hourly=snowfall&hourly=showers&hourly=weather_code&hourly=wind_speed_10m&hourly=wind_gusts_10m'
    send_api = requests.get(url).json()
    if 'error' in send_api:
        error_list.append(city)
        continue
    print(city)
    with open(f"{city}.json", "w") as out:
        json.dump(send_api, out)
    time.sleep(10)

print(error_list)