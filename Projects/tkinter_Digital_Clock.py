import time
from tkinter import*

root = Tk()
root.geometry('450x100')
root.title('DIGITAL CLOCK')

def clocktime(time1 = ''):
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text = time2)

    clock.after(1000,clocktime)
clock = Label(root, font='verdana 55 bold', background='black', foreground='green')
clock.pack(fill='both', expand=1)
clocktime()
root.mainloop()
