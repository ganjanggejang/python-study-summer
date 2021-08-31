import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)  # 시퀀스 객체가 data에 저장됨
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

# 이런 csv 파일에서 데이터를 추출하는 작업을 단순화해주는 라이브러리 : Pandas
