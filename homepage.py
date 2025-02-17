from tkinter import *
from PIL import Image, ImageTk
import subprocess
import os

def open_registerpage_file():
    os._exit(0)
# iphone16
def open_iphone16_file():
    subprocess.run(["python", "iphone16.py"])
# iphone16plus
def open_iphone16plus_file():
    subprocess.run(["python", "iphone16plus.py"])
# iphone16pro
def open_iphone16pro_file():
    subprocess.run(["python", "iphone16pro.py"])
# iphone16promax
def open_iphone16promax_file():
    subprocess.run(["python", "iphone16promax.py"])

window = Tk()
window.title("Bosh sahifa | Apple savdo")
window.geometry("725x725")

welcome = Label(window, text="Apple savdosiga xush kelibsiz!", font=("Arial", 16, "bold"))
welcome.place(x=30, y=30, width=315, height=60)

# iphone 16
image_path = "img/iphone16.png"
iphone16 = Image.open(image_path)
iphone16 = iphone16.resize((135, 154)) 
photo_iphone16 = ImageTk.PhotoImage(iphone16)

iphone16_label1 = Label(window, image=photo_iphone16, bg="#f0f0f0")
iphone16_label1.place(x=20, y=90, width=150, height=175)

iphone16_label2 = Label(text="iPhone 16", font=('Arial', 12), bg="white")
iphone16_label2.place(x=27, y=254, width=135, height=40)

iphone16_button = Button(text="Btafsil", font=('Arial', 12), command=open_iphone16_file)
iphone16_button.place(x=27, y=294, width=135, height=40)
#
# iphone 16 plus
image_path = "img/iphone16plus.png"
iphone16plus = Image.open(image_path)
iphone16plus = iphone16plus.resize((135, 154)) 
photo_iphone16plus1 = ImageTk.PhotoImage(iphone16plus)

iphone16plus_label1 = Label(window, image=photo_iphone16plus1, bg="#f0f0f0")
iphone16plus_label1.place(x=200, y=90, width=150, height=175)

iphone16plus_label2 = Label(text="iPhone 16 Plus", font=('Arial', 12), bg="white")
iphone16plus_label2.place(x=207, y=254, width=135, height=40)

iphone16plus_button = Button(text="Btafsil", font=('Arial', 12), command=open_iphone16plus_file)
iphone16plus_button.place(x=207, y=294, width=135, height=40)
#
# iphone 16 pro
image_path = "img/iphone16pro.png"
iphone16pro = Image.open(image_path)
iphone16pro = iphone16pro.resize((135, 154)) 
photo_iphone16pro1 = ImageTk.PhotoImage(iphone16pro)

iphone16pro_label1 = Label(window, image=photo_iphone16pro1, bg="#f0f0f0")
iphone16pro_label1.place(x=380, y=90, width=150, height=175)

iphone16pro_label2 = Label(text="iPhone 16 Pro", font=('Arial', 12), bg="white")
iphone16pro_label2.place(x=387, y=254, width=135, height=40)

iphone16pro_button = Button(text="Btafsil", font=('Arial', 12), command=open_iphone16pro_file)
iphone16pro_button.place(x=387, y=294, width=135, height=40)
#
# iphone 16 pro max
image_path = "img/iphone16promax.png"
iphone16promax = Image.open(image_path)
iphone16promax = iphone16promax.resize((135, 154)) 
photo_iphone16promax1 = ImageTk.PhotoImage(iphone16promax)

iphone16promax_label1 = Label(window, image=photo_iphone16promax1, bg="#f0f0f0")
iphone16promax_label1.place(x=560, y=90, width=150, height=175)

iphone16promax_label2 = Label(text="iPhone 16 Pro Max", font=('Arial', 12), bg="white")
iphone16promax_label2.place(x=567, y=254, width=135, height=40)

iphone16promax_button = Button(text="Btafsil", font=('Arial', 12), command=open_iphone16promax_file)
iphone16promax_button.place(x=567, y=294, width=135, height=40)
#
logout = Button(text="Chiqish", font=("Arial", 14), command=open_registerpage_file)
logout.place(x=630, y=30, width=70, height=40)
window.mainloop()