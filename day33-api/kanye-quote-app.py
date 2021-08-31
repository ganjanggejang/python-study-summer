# 칸예 어록 api ㅋㅋ 를 이용한 앱
from tkinter import *
import requests


def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)


# 프로그램 창
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# 배경
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
canvas.grid(row=0, column=0)

quote_text = canvas.create_text(150, 207, text="Gang", width=250, font=("Arial", 30, "bold"), fill="white")

# 칸예 얼굴 버튼
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
