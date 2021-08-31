import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_Squirrel_Data.csv")

colors = []
for d in data["Primary Fur Color"]:
    colors.append(d)

gray = 0
cinnamon = 0
black = 0

for c in colors:
    if c == "Gray":
        gray += 1
    if c == "Cinnamon":
        cinnamon += 1
    if c == "Black":
        black += 1

squirrel_color_count = {
    "Colors": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}

new_data = pandas.DataFrame(squirrel_color_count)
new_data.to_csv("color_count_data.csv")
