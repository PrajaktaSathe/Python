from tkinter import Tk, StringVar, Label, Entry, Button

import pyperclip
import pyshorteners


def url_shortener():
    url_address = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(url_address)
    url_address.set(url_short)


def copy_url():
    url_short = url_address.get()
    pyperclip.copy(url_short)


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x200")
    root.title("URL Shortener")
    root.configure(bg="#49A")

    url = StringVar()
    url_address = StringVar()

    Label(root, text="My URL Shortener", font="poppins").pack(pady=10)
    Entry(root, textvariable=url).pack(pady=5)
    Button(root, text="Generate Short URl", command=url_shortener).pack(pady=7)
    Entry(root, textvariable=url_address).pack(pady=5)
    Button(root, text="Copy URL", command=copy_url).pack(pady=5)

    root.mainloop()
