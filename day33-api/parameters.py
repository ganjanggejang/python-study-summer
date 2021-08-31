import requests
from datetime import datetime

# api 매개변수에 들어갈 인자가 딕셔너리 형태여야 함.
location_info = {
    "lat": 51.507351,
    "lng": -0.127758,
    "formatted": 0
}


response = requests.get("https://api.sunrise-sunset.org/json", params=location_info)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]


print(data)

time_now = datetime.now()
print(time_now)






