from tkinter import *
from PIL import Image, ImageTk
import os

def exit():
    os._exit(0)

window = Tk()
window.title("Macbook Pro M3 | Apple savdo")
window.geometry("700x400")

welcome = Label(window, text="Macbook Pro M3", font=("Arial", 16, "bold"))
welcome.place(x=300, y=30, width=315, height=60)

image_path = "img/macbookprom3.png"
image = Image.open(image_path)
image = image.resize((270, 270)) 
photo = ImageTk.PhotoImage(image)

image_label = Label(window, image=photo, bg="#f0f0f0")
image_label.place(x=20, y=70, width=275, height=310)

info = Label(window, text="""Chiqarilgan sana: 2023-yil
Protsessor: Apple M3
Operativ xotira: 8GB-36GB
Batareya quvvati: ~22 soatgacha""", font=("Arial", 13, "normal"))
info.place(x=300, y=90, width=315, height=200)
price = Label(window, text="Narxi: 1300$", font=("Arial", 14, "bold"))
price.place(x=300, y=250, width=315, height=60)

exit_button = Button(text="Chiqish", font=("Arial", 14), command=exit)
exit_button.place(x=600, y=30, width=70, height=40)
window.mainloop()