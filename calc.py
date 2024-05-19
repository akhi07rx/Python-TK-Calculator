import tkinter as tk
from tkinter import *

calc = tk.Tk()
calc.geometry("350x500")
calc.title("CALCULATOR")

input_box = tk.Entry(calc, font=("Consolas", 15))
input_box.place(x=24, y=35, height=45, width=300)

def answer():
    ans = str(input_box.get())
    evaluate = eval(ans)
    input_box.delete(0, END)
    input_box.insert(END, evaluate)

def input_num(num):
    dv = str(input_box.get())
    num = dv + str(num)
    input_box.delete(0, END)
    input_box.insert(END, num)
    
def clear_display():
    input_box.delete(0,"end")
    
def backspace():
    bs = input_box.get()
    input_box.delete(0, END)
    input_box.insert(0, bs[0:-1])

# FIRST ROW
Button(text="%", font=("Consolas", 15), command=lambda: input_num("%")).place(x=20, y=110, height=50, width=70)
Button(text="CE", font=("Consolas", 14),command=clear_display).place(x=100, y=110, height=50, width=70)
Button(text="C", font=("Consolas", 14),command=clear_display).place(x=180, y=110, height=50, width=70)
Button(text="⌫", font=("Consolas", 12),command=backspace).place(x=260, y=110, height=50, width=70)

# SECOND ROW
Button(text="(", font=("Consolas", 15), command=lambda: input_num("(")).place(x=20, y=170, height=50, width=70)
Button(text="𝑥²", font=("Consolas", 15), command=lambda: input_num("𝑥²")).place(x=100, y=170, height=50, width=70)
Button(text=")", font=("Consolas", 15), command=lambda: input_num(")")).place(x=180, y=170, height=50, width=70)
Button(text="÷", font=("Consolas", 18),command=lambda: input_num("/")).place(x=260, y=170, height=50, width=70)

# THIRD ROW
Button(text="7", font=("Consolas", 15), command=lambda: input_num(7)).place(x=20, y=230, height=50, width=70)
Button(text="8", font=("Consolas", 15), command=lambda: input_num(8)).place(x=100, y=230, height=50, width=70)
Button(text="9", font=("Consolas", 15), command=lambda: input_num(9)).place(x=180, y=230, height=50, width=70)
Button(text="×", font=("Consolas", 15), command=lambda: input_num("*")).place(x=260, y=230, height=50, width=70)

# FOURTH ROW
Button(text="4", font=("Consolas", 15), command=lambda: input_num(4)).place(x=20, y=290, height=50, width=70)
Button(text="5", font=("Consolas", 15), command=lambda: input_num(5)).place(x=100, y=290, height=50, width=70)
Button(text="6", font=("Consolas", 15), command=lambda: input_num(6)).place(x=180, y=290, height=50, width=70)
Button(text="-", font=("Consolas", 15), command=lambda: input_num("-")).place(x=260, y=290, height=50, width=70)

# FIFTH ROW
Button(text="1", font=("Consolas", 15), command=lambda: input_num(1)).place(x=20, y=350, height=50, width=70)
Button(text="2", font=("Consolas", 15), command=lambda: input_num(2)).place(x=100, y=350, height=50, width=70)
Button(text="3", font=("Consolas", 15), command=lambda: input_num(3)).place(x=180, y=350, height=50, width=70)
Button(text="+", font=("Consolas", 15), command=lambda: input_num("+")).place(x=260, y=350, height=50, width=70)

# SIXTH ROW
Button(text="+/-", font=("Consolas", 15), command=lambda: input_num("+/-")).place(x=20, y=410, height=50, width=70)
Button(text="0", font=("Consolas", 15), command=lambda: input_num(0)).place(x=100, y=410, height=50, width=70)
Button(text=".", font=("Consolas", 15), command=lambda: input_num(".")).place(x=180, y=410, height=50, width=70)
Button(text="=", font=("Consolas", 15), bg="#19a8b2", command=answer).place(x=260, y=410, height=50, width=70)

calc.mainloop()

