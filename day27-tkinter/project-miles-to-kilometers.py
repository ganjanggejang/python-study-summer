from tkinter import *


def button_clicked():
    new_text = int(miles_input.get())
    new_text *= 1.609
    km_text.config(text=new_text)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=50, pady=50)

# (1,0)
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# (2,0)
text0 = Label(text="Miles")
text0.grid(column=2, row=0)
text0.config(padx=10, pady=10)

# (0,1)
text1 = Label(text="is equal to")
text1.grid(column=0, row=1)
text1.config(padx=10, pady=10)

# (1,1)
km_text = Label(text=0)
km_text.grid(column=1, row=1)
km_text.config(padx=10, pady=10)

# (2,1)
text2 = Label(text="Km")
text2.grid(column=2, row=1)
text2.config(padx=10, pady=10)

# (2,2)
cal_button = Button(text="Calculate", command=button_clicked)
cal_button.grid(column=1, row=3)
cal_button.config(padx=10, pady=10)

window.mainloop()
