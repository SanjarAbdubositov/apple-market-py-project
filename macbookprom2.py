from tkinter import *
from PIL import Image, ImageTk
import subprocess

def open_homepage_file():
    subprocess.run(["python", "homepage.py"])

window = Tk()
window.title("iPhone 16 | Apple savdo")
window.geometry("700x400")

welcome = Label(window, text="Macbook Pro M1", font=("Arial", 16, "bold"))
welcome.place(x=300, y=30, width=315, height=60)

image_path = "img/macbookprom2.png"
image = Image.open(image_path)
image = image.resize((270, 308)) 
photo = ImageTk.PhotoImage(image)

image_label = Label(window, image=photo, bg="#f0f0f0")
image_label.place(x=20, y=70, width=275, height=310)

info = Label(window, text="""Chiqarilgan sana: 2022-yil
Protsessor: Apple M2
Operativ xotira: 8GB-24GB
Batareya quvvati: ~20 soatgacha""", font=("Arial", 13, "normal"))
info.place(x=300, y=90, width=315, height=200)
price = Label(window, text="Narxi: 950$", font=("Arial", 14, "bold"))
price.place(x=300, y=250, width=315, height=60)

window.mainloop()