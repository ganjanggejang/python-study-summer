import pandas

# --------------------- Data -------------------------- #
data = pandas.read_csv("./data/french_words.csv").to_dict()
french_words = []
english_words = []

for d in data["French"].values():
    french_words.append(d)

for d in data["English"].values():
    english_words.append(d)

words = {}
for n in range(len(english_words)):
    words[english_words[n]] = french_words[n]

print(words)
