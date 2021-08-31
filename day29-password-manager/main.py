from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)  # password_list의 요소들을 합쳐줌
    input_password.insert(0, password)
    pyperclip.copy(password)  # 생성된 password를 클립보드에 자동으로 복사

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_data():
    get_website = input_website.get()
    get_username = input_username.get()
    get_password = input_password.get()

    new_data = {
        get_website: {
            "username": get_username,
            "password": get_password
        }
    }

    if get_website == "" or get_username == "" or get_password == "":
        messagebox.showwarning(title="오류", message="정보를 전부 입력하십시오")
    else:
        # askokcancel()은 input()이랑 비슷한 메서드
        is_ok = messagebox.askokcancel(title=f"{get_website} 계정 정보 저장하기", message=f"입력하신 정보가 맞습니까?: \nUsername: {get_username} \nPassword : {get_password}")
        if is_ok:
            # json 파일이 없는 초기 상태에 대비해 try-except-else-finally 구문 작성
            try:
                with open("data.json", mode="r") as file:
                    data = json.load(file)  # load() 메서드 --> json 읽기
                    data.update(new_data)  # update() 메서드 --> json 데이터 갱신
            except FileNotFoundError: # json 파일이 없는 초기 상태에서는 새로 data.json을 만듦
                with open("data.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)  # dump() 메서드 --> json 덧대어쓰기
            finally:
                input_website.delete(0, "end")
                input_username.delete(0, "end")
                input_password.delete(0, "end")

                input_website.focus()
                input_username.insert(0, "c111202@g.hongik.ac.kr")

# ----------------------------- FIND ID/PW ------------------------------- #

def find_password():
    get_website = input_website.get()

    with open("data.json", mode="r") as file:
        data = json.load(file)
        if get_website in data.keys():
            username = data[get_website]["username"]
            password = data[get_website]["password"]
            messagebox.showerror(title="이미 등록된 계정", message=f"검색하신 웹사이트에 대한 계정 정보가 이미 등록되어 있습니다.\n{get_website}의\nusername: {username}\npassword: {password}")
        else:
            messagebox.showinfo(title="암호를 저장하세요", message="아직 등록하지 않은 웹사이트입니다.")


# ---------------------------- UI SETUP ------------------------------- #

# 프로그램 창
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

# 배경
canvas = Canvas(width=200, height=200)
background_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=background_img)
canvas.grid(column=1, row=1)

# Website:
text_website = Label(text="Website:")
text_website.grid(column=0, row=2)
text_website.config(padx=5, pady=5)

input_website = Entry(width=35)
input_website.grid(column=1, row=2)
input_website.focus()  # 처음 실행할 때 커서가 여기에 가있음

# Search
button_search = Button(text="Search", command=find_password)
button_search.grid(column=2, row=2)
button_search.config(padx=5, pady=10)

# Email/Username:
text_username = Label(text="Username:")
text_username.grid(column=0, row=3)
text_username.config(padx=5, pady=5)

input_username = Entry(width=35)
input_username.grid(column=1, row=3)
input_username.insert(0, "c111202@g.hongik.ac.kr")  # 처음 실행할 때 미리 메일 써놓음

# Password:
text_password = Label(text="Password:")
text_password.grid(column=0, row=4)
text_password.config(padx=5, pady=5)

input_password = Entry(width=35)
input_password.grid(column=1, row=4)

# Generate Password
button_generate_password = Button(text="Generate", command=generate_password)
button_generate_password.grid(column=2, row=4)
button_generate_password.config(padx=5, pady=10)

# Add
button_add = Button(text="Add", width=35, command=add_data)
button_add.grid(column=1, row=5)
button_generate_password.config(padx=5, pady=5)

window.mainloop()
