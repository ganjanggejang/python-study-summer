from tkinter import *

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)  # my_label["text"] = new_text


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

#Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(row=0, column=0)

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

new_button = Button(text="New Button")
new_button.grid(row=0, column=2)
#Entry
user_input = Entry(width=10)
user_input.grid(row=1, column=0)
print(user_input.get())



window.mainloop()
