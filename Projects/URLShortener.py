import pyperclip
# if you don't have pyperclip imported, you can do so by using the command - pip install pyperclip
import pyshorteners
# if you don't have pyshortener imported, you can do so by using the command - pip install pyshortener
from tkinter import*
# importing tkinter

root=Tk()
root.geometry("400x200")
root.title("URL Shortener")
root.configure(bg="#49A")
url=StringVar()
url_address=StringVar()

def urlshortner():
    urladdress=url.get()
    url_short=pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short=url_address.get()
    pyperclip.copy(url_short)
Label(root,text="My URL Shortener", font="poppins").pack(pady=10)
Entry(root, textvariable=url).pack(pady=5)
Button(root, text="Generate Short URl", command=urlshortner).pack(pady=7)
Entry(root, textvariable=url_address).pack(pady=5)
Button(root, text="Copy URL", command=copyurl).pack(pady=5)

root.mainloop()

