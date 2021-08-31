import json

get_website = "google"

with open("data.json", mode="r") as file:
    data = json.load(file)
    if get_website in data.keys():
        username = data[get_website]["username"]
        password = data[get_website]["password"]
        print(username, password)
    else:
        print("빼액")

