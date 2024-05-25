import customtkinter as ctk
from tkinter import *

ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")  

calc = ctk.CTk()
calc.geometry("350x500")
calc.title("CALCULATOR")

input_box = ctk.CTkEntry(calc, font=("Consolas", 15), width=300, height=45)
input_box.place(x=24, y=35)

def answer():
    ans = str(input_box.get())
    try:
        evaluate = eval(ans)
        input_box.delete(0, END)
        input_box.insert(END, evaluate)
    except TypeError:
        input_box.delete(0, END)
        input_box.insert(END, "Error")

def input_num(num):
    dv = str(input_box.get())
    num = dv + str(num)
    input_box.delete(0, END)
    input_box.insert(END, num)

def clear_display():
    input_box.delete(0, END)

def backspace():
    bs = input_box.get()
    input_box.delete(0, END)
    input_box.insert(0, bs[0:-1])

# Define button dimensions
button_width = 70
button_height = 50

# FIRST ROW
ctk.CTkButton(calc, text="%", font=("Consolas", 15), command=lambda: input_num("%"), width=button_width, height=button_height).place(x=20, y=110)
ctk.CTkButton(calc, text="CE", font=("Consolas", 14), command=clear_display, width=button_width, height=button_height).place(x=100, y=110)
ctk.CTkButton(calc, text="C", font=("Consolas", 14), command=clear_display, width=button_width, height=button_height).place(x=180, y=110)
ctk.CTkButton(calc, text="⌫", font=("Consolas", 12), command=backspace, width=button_width, height=button_height).place(x=260, y=110)

# SECOND ROW
ctk.CTkButton(calc, text="(", font=("Consolas", 15), command=lambda: input_num("("), width=button_width, height=button_height).place(x=20, y=170)
ctk.CTkButton(calc, text="𝑥²", font=("Consolas", 15), command=lambda: input_num("**2"), width=button_width, height=button_height).place(x=100, y=170)
ctk.CTkButton(calc, text=")", font=("Consolas", 15), command=lambda: input_num(")"), width=button_width, height=button_height).place(x=180, y=170)
ctk.CTkButton(calc, text="÷", font=("Consolas", 18), command=lambda: input_num("/"), width=button_width, height=button_height).place(x=260, y=170)

# THIRD ROW
ctk.CTkButton(calc, text="7", font=("Consolas", 15), command=lambda: input_num(7), width=button_width, height=button_height).place(x=20, y=230)
ctk.CTkButton(calc, text="8", font=("Consolas", 15), command=lambda: input_num(8), width=button_width, height=button_height).place(x=100, y=230)
ctk.CTkButton(calc, text="9", font=("Consolas", 15), command=lambda: input_num(9), width=button_width, height=button_height).place(x=180, y=230)
ctk.CTkButton(calc, text="×", font=("Consolas", 15), command=lambda: input_num("*"), width=button_width, height=button_height).place(x=260, y=230)

# FOURTH ROW
ctk.CTkButton(calc, text="4", font=("Consolas", 15), command=lambda: input_num(4), width=button_width, height=button_height).place(x=20, y=290)
ctk.CTkButton(calc, text="5", font=("Consolas", 15), command=lambda: input_num(5), width=button_width, height=button_height).place(x=100, y=290)
ctk.CTkButton(calc, text="6", font=("Consolas", 15), command=lambda: input_num(6), width=button_width, height=button_height).place(x=180, y=290)
ctk.CTkButton(calc, text="-", font=("Consolas", 15), command=lambda: input_num("-"), width=button_width, height=button_height).place(x=260, y=290)

# FIFTH ROW
ctk.CTkButton(calc, text="1", font=("Consolas", 15), command=lambda: input_num(1), width=button_width, height=button_height).place(x=20, y=350)
ctk.CTkButton(calc, text="2", font=("Consolas", 15), command=lambda: input_num(2), width=button_width, height=button_height).place(x=100, y=350)
ctk.CTkButton(calc, text="3", font=("Consolas", 15), command=lambda: input_num(3), width=button_width, height=button_height).place(x=180, y=350)
ctk.CTkButton(calc, text="+", font=("Consolas", 15), command=lambda: input_num("+"), width=button_width, height=button_height).place(x=260, y=350)

# SIXTH ROW
ctk.CTkButton(calc, text="+/-", font=("Consolas", 15), command=lambda: input_num("-"), width=button_width, height=button_height).place(x=20, y=410)
ctk.CTkButton(calc, text="0", font=("Consolas", 15), command=lambda: input_num(0), width=button_width, height=button_height).place(x=100, y=410)
ctk.CTkButton(calc, text=".", font=("Consolas", 15), command=lambda: input_num("."), width=button_width, height=button_height).place(x=180, y=410)
ctk.CTkButton(calc, text="=", font=("Consolas", 15), fg_color="#19a8b2", command=answer, width=button_width, height=button_height).place(x=260, y=410)

calc.mainloop()
