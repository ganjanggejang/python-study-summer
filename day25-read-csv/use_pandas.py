# Pandas : 파이썬 데이터 분석 라이브러리
import pandas

data = pandas.read_csv("weather_data.csv")  # data는 pandas 객체. pandas의 각종 메서드를 사용할 수 있다.
# print(data)
# print(data["temp"])  # temp 열의 데이터를 가져옴

# data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
# print(len(temp_list))

# print(data["temp"])

sum = 0
for d in data["temp"]:
    sum += d

# print(sum / len(temp_list))
# print(data["temp"].mean())
# print(data["temp"].max())

# Get Data in Columns(열)
# print(data["condition"])
# print(data.condition)

# Get Data in Row(행)
# print(data[data.day == "Monday"])  # day 값이 Monday인 행의 값을 가져옴
# print(data[data.temp == data.temp.max()])  # temp 값이 최대인 행의 값을 가져옴

# monday = data[data.day == "Monday"]
# print(monday.condition)

# fahrenheit = []
# for d in data["temp"]:
#     f = d * 9/5 + 32
#     fahrenheit.append(f)

# print(fahrenheit)

# dictionary --> DataFrame --> csv 파일
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")  # 새로운 csv 파일 생성
