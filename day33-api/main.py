import requests


response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)  # HTTP status code를 출력함. 해당 웹사이트의 상태(접근 가능 여부, 사용자 또는 서버의 문제를 나타내줌)
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
print(data)
print(longitude, latitude)
