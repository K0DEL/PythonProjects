import pandas

values = {}
data = pandas.read_csv("squirrel.csv")
colors = data["Primary Fur Color"].unique().tolist()

for color in colors[1:]:
    count = data[data["Primary Fur Color"] == color].count()
    # print(count["Primary Fur Color"])
    values[color] = count["Primary Fur Color"]

print(values)
