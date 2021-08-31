from tkinter import *
from tkinter import messagebox
import pandas
import random
import time
BACKGROUND_COLOR = "#B1DDC6"
random_french_word = ""
my_wrong_words = []  # 사용자가 틀린 단어 수집하는 리스트
# --------------------- Data -------------------------- #
data = pandas.read_csv("./data/french_words.csv").to_dict()
french_words = []
korean_words = []

for d in data["French"].values():
    french_words.append(d)

for d in data["Korean"].values():
    korean_words.append(d)

words = {}  # 프랑스어단어가 키, 한국어단어가 값인 딕셔너리
for n in range(len(korean_words)):
    words[french_words[n]] = korean_words[n]

# -------------------function-----------------#

def click_right_button():
    quiz_start()

def click_wrong_button():
    quiz_start()

def quiz_start():
    global random_french_word
    canvas.itemconfig(text_language, text="French")
    canvas.itemconfig(card, image=card_front_img)
    random_french_word = random.choice(french_words)
    canvas.itemconfig(text_word, text=f"{random_french_word}")  # canvas text config 하는법 기억하기
    window.after(4000, show_answer)  # 4000밀리초 후에 show_answer 함수를 실행

def show_answer():
    # 정답 공개
    global random_french_word
    canvas.itemconfig(text_language, text="Korean")
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(text_word, text=f"{words[random_french_word]}")

def click_info_button():
    messagebox.showinfo(title="프랑스어 연습 게임", message="체크 버튼을 누르면 게임이 시작됩니다.\n프랑스어 단어가 화면에 4초간 표시된 후 정답이 공개됩니다.\n맞췄다면 체크 버튼을, 틀렸다면 엑스 버튼을 누르세요")


# ----------------------- UI ------------------------ #

# 프로그램 창
window = Tk()
window.title("Flash Card - Learning French")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# flash card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(highlightthickness=0)

card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card = canvas.create_image(400, 263, image=card_front_img)

text_language = canvas.create_text(400, 150, text="Title", font=("Product Sans", 20, "italic"))
text_word = canvas.create_text(400, 263, text="word", font=("Product Sans", 40, "bold"))

# wrong button
wrong_img = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=wrong_img, command=click_wrong_button)  # command 인자 추가해야함
button_wrong.grid(column=0, row=1)

# right button
right_img = PhotoImage(file="./images/right.png")
button_right = Button(image=right_img, command=click_right_button)  # command 인자 추가해야함
button_right.grid(column=1, row=1)

# introduction button
button_info = Button(text="Help", command=click_info_button)
button_info.grid(column=3, row=2)

window.mainloop()
