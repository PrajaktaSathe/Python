import time
from tkinter import Tk, Label


def clock_time(clock):
    now = time.strftime('%H:%M:%S')
    clock.config(text=now)
    clock.after(1000, clock_time)


if __name__ == "__main__":
    root = Tk()
    root.geometry('450x100')
    root.title('DIGITAL CLOCK')

    clock = Label(root, font='verdana 55 bold', background='black', foreground='green')
    clock.pack(fill='both', expand=1)
    clock_time(clock)

    root.mainloop()
