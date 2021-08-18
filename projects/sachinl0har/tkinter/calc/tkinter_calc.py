from tkinter import *

wind = Tk()
wind.geometry("270x430")
wind.title("Basic Calculator")

text = Entry(wind, font=("arial", 16))
text.pack(fill=X, padx=5, pady=5, ipady=5)


def add_to_text(n):
    text.insert(END, n)


def calculate():
    result = eval(text.get())
    text.delete(0, END)
    text.insert(0, result)


def button_clear():
    text.delete(0, END)


frame = Frame(wind)
frame.pack(side=TOP, anchor=NW)

rightFrame = Frame(frame)
rightFrame.pack(side=RIGHT)

frame1 = Frame(frame)
frame1.pack()


# FIXME: The following repeats a lot of code.

# btn 1 to 3
btn1 = Button(frame1, text="1", fg='black', bg='#696969', width=9, height=4, command=lambda: add_to_text("1"))
btn1.pack(side=LEFT)
btn2 = Button(frame1, text="2", fg='black', bg='#696969', width=9, height=4, command=lambda: add_to_text("2"))
btn2.pack(side=LEFT)
btn3 = Button(frame1, text="3", fg='black', bg='#696969', width=9, height=4, command=lambda: add_to_text("3"))
btn3.pack(side=LEFT)

frame2 = Frame(frame)
frame2.pack()

# btn 4 to 6
btn4 = Button(frame2, text="4", fg='black', bg='#696969', width=9, height=4, command=lambda: add_to_text("4"))
btn4.pack(side=LEFT)
btn5 = Button(frame2, text="5", fg='black', bg='#696969', width=9, height=4, command=lambda: add_to_text("5"))
btn5.pack(side=LEFT)
btn6 = Button(frame2, text="6", fg='black', bg='#696969', width=9, height=4, command=lambda: add_to_text("6"))
btn6.pack(side=LEFT)

frame3 = Frame(frame)
frame3.pack()

# btn 7 to 9
btn7 = Button(frame3, text="7", fg='black', bg='#696969', width=9, height=4, command=lambda: add_to_text("7"))
btn7.pack(side=LEFT)
btn8 = Button(frame3, text="8", fg='black', bg='#696969', width=9, height=4, command=lambda: add_to_text("8"))
btn8.pack(side=LEFT)
btn9 = Button(frame3, text="9", fg='black', bg='#696969', width=9, height=4, command=lambda: add_to_text("9"))
btn9.pack(side=LEFT)

frame4 = Frame(frame)
frame4.pack()

# btn . 0 =
btnpoint = Button(frame4, text=".", fg='black', bg='#696969', width=9, height=4, command=lambda: add_to_text("."))
btnpoint.pack(side=LEFT)
btnzero = Button(frame4, text="0", fg='black', bg='#696969', width=9, height=4, command=lambda: add_to_text("0"))
btnzero.pack(side=LEFT)
btneq = Button(frame4, text="=", fg='black', bg='#696969', width=9, height=4, command=lambda: calculate())
btneq.pack(side=LEFT)

# operators
btndiv = Button(rightFrame, text="/", fg='black', bg='#696969', width=6, height=4, command=lambda: add_to_text("/"))
btndiv.pack()
btnmul = Button(rightFrame, text="x", fg='black', bg='#696969', width=6, height=4, command=lambda: add_to_text("*"))
btnmul.pack()
btndif = Button(rightFrame, text="-", fg='black', bg='#696969', width=6, height=4, command=lambda: add_to_text("-"))
btndif.pack()
btnplus = Button(rightFrame, text="+", fg='black', bg='#696969', width=6, height=4, command=lambda: add_to_text("+"))
btnplus.pack()
btnplus = Button(rightFrame, text="%", fg='black', bg='#696969', width=6, height=4, command=lambda: add_to_text("%"))
btnplus.pack()

frame5 = Frame(frame)
frame5.pack()

btnclear = Button(frame5, text="C", fg='black', bg='#696969', width=30, height=4, command=lambda: button_clear())
btnclear.pack()

wind.mainloop()
