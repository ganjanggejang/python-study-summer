from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1 #25
SHORT_BREAK_MIN = 1 #5
LONG_BREAK_MIN = 1 #20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1

    if reps % 2 != 0:  # 홀수번째에선 work
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    else:  # 짝수번째에선 break
        title_label.config(text="Break", fg=RED)
        if reps % 8 == 0:  # 8의 배수번째에선 long break
            count_down(long_break_sec)
        else:
            count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):  # count는 초단위
    count_min = count // 60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(reps//2):
            marks += "✔"

        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
# 프로그램 창
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# 배경
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)  # image 인자에 "파일이름" 아니고 PhotoImage 클래스로 만든 객체를 집어넣어야함
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# 제목
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# 시작 버튼
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

# 리셋 버튼
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

# 체크 표시
check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
