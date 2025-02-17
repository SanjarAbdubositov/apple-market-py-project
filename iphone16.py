from tkinter import *
from PIL import Image, ImageTk
import os

def exit():
    os._exit(0)

window = Tk()
window.title("iPhone 16 | Apple savdo")
window.geometry("700x400")

welcome = Label(window, text="iPhone 16", font=("Arial", 16, "bold"))
welcome.place(x=300, y=30, width=315, height=60)

image_path = "img/iphone16.png"
image = Image.open(image_path)
image = image.resize((270, 308)) 
photo = ImageTk.PhotoImage(image)

image_label = Label(window, image=photo, bg="#f0f0f0")
image_label.place(x=20, y=70, width=275, height=310)
#info
info = Label(window, text="""Rang: Yashil
Protsessor: A18 Bionic
Ekran: 6.1 inch
Kamera: 48mp
AI: Apple Intelligence""", font=("Arial", 13, "normal"))
info.place(x=300, y=90, width=315, height=200)
price = Label(window, text="Narxi: 799$", font=("Arial", 14, "bold"))
price.place(x=300, y=250, width=315, height=60)

exit_button = Button(text="Chiqish", font=("Arial", 14), command=exit)
exit_button.place(x=600, y=30, width=70, height=40)
window.mainloop()