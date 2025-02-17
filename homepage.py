from tkinter import *
from PIL import Image, ImageTk
import subprocess
import os

def open_exit_file():
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
# macbookprom1
def open_macbookprom1_file():
    subprocess.run(["python", "macbookprom1.py"])
# macbookprom2
def open_macbookprom2_file():
    subprocess.run(["python", "macbookprom2.py"])
# macbookprom3
def open_macbookprom3_file():
    subprocess.run(["python", "macbookprom3.py"])
# macbookprom4
def open_macbookprom4_file():
    subprocess.run(["python", "macbookprom4.py"])

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

iphone16_button = Button(text="Batafsil", font=('Arial', 12), command=open_iphone16_file)
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

iphone16plus_button = Button(text="Batafsil", font=('Arial', 12), command=open_iphone16plus_file)
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

iphone16pro_button = Button(text="Batafsil", font=('Arial', 12), command=open_iphone16pro_file)
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

iphone16promax_button = Button(text="Batafsil", font=('Arial', 12), command=open_iphone16promax_file)
iphone16promax_button.place(x=567, y=294, width=135, height=40)
#
# macbook pro m1
image_path = "img/macbookprom1.png"
macbookprom1 = Image.open(image_path)
macbookprom1 = macbookprom1.resize((150, 150))
photo_macbookprom1 = ImageTk.PhotoImage(macbookprom1)

macbookprom1_label1 = Label(window, image=photo_macbookprom1, bg="#f0f0f0")
macbookprom1_label1.place(x=20, y=400, width=150, height=175)

macbookprom1_label2 = Label(text="Macbook Pro M1", font=('Arial', 12), bg="white")
macbookprom1_label2.place(x=20, y=564, width=150, height=40)

macbookprom1_button = Button(text="Batafsil", font=('Arial', 12), command=open_macbookprom1_file)
macbookprom1_button.place(x=20, y=604, width=150, height=40)

#
# macbook pro m2
image_path = "img/macbookprom2.png"
macbookprom2 = Image.open(image_path)
macbookprom2 = macbookprom1.resize((150, 150))
photo_macbookprom2 = ImageTk.PhotoImage(macbookprom2)

macbookprom2_label1 = Label(window, image=photo_macbookprom2, bg="#f0f0f0")
macbookprom2_label1.place(x=200, y=400, width=150, height=175)

macbookprom2_label2 = Label(text="Macbook Pro M2", font=('Arial', 12), bg="white")
macbookprom2_label2.place(x=200, y=564, width=150, height=40)

macbookprom2_button = Button(text="Batafsil", font=('Arial', 12), command=open_macbookprom2_file)
macbookprom2_button.place(x=200, y=604, width=150, height=40)


#
# macbook pro m3
image_path = "img/macbookprom3.png"
macbookprom3 = Image.open(image_path)
macbookprom3 = macbookprom3.resize((150, 150))
photo_macbookprom3 = ImageTk.PhotoImage(macbookprom3)

macbookprom3_label1 = Label(window, image=photo_macbookprom3, bg="#f0f0f0")
macbookprom3_label1.place(x=380, y=400, width=150, height=175)

macbookprom3_label2 = Label(text="Macbook Pro M3", font=('Arial', 12), bg="white")
macbookprom3_label2.place(x=380, y=564, width=150, height=40)

macbookprom3_button = Button(text="Batafsil", font=('Arial', 12), command=open_macbookprom3_file)
macbookprom3_button.place(x=380, y=604, width=150, height=40)

#
# macbook pro m4
image_path = "img/macbookprom4.png"
macbookprom4 = Image.open(image_path)
macbookprom4 = macbookprom1.resize((150, 150))
photo_macbookprom4 = ImageTk.PhotoImage(macbookprom4)

macbookprom4_label1 = Label(window, image=photo_macbookprom4, bg="#f0f0f0")
macbookprom4_label1.place(x=560, y=400, width=150, height=175)

macbookprom4_label2 = Label(text="Macbook Pro M4", font=('Arial', 12), bg="white")
macbookprom4_label2.place(x=560, y=564, width=150, height=40)

macbookprom4_button = Button(text="Batafsil", font=('Arial', 12), command=open_macbookprom4_file)
macbookprom4_button.place(x=560, y=604, width=150, height=40)
#
exit_button = Button(text="Chiqish", font=("Arial", 14), command=open_exit_file)
exit_button.place(x=630, y=30, width=70, height=40)

window.mainloop()