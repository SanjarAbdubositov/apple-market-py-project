from tkinter import *
import subprocess
import os


def open_homepage_file():
    subprocess.run(["python", "homepage.py"])
    os._exit(0)

window = Tk()
window.title("Register")
window.geometry("400x400")
#
title = Label(text="Register", font="blue")
title.place(x=145, y=25, width=120, height=40)

text = Label(text="O'zingiz haqingizda ma'lumotlarni to'ldiring")
text.place(x=65, y=65, width=300, height=40)
#
first_name = Entry(relief="solid")
first_name.place(x=25, y=115, width=140, height=30)
first_name.insert(0, "First name")
#
second_name = Entry(relief="solid")
second_name.place(x=175, y=115, width=200, height=30)
second_name.insert(0, "Second name")
#
gmail = Entry(relief="solid")
gmail.place(x=25, y=165, width=350, height=30)
gmail.insert(0, "@gmail.com")
#
password = Entry(relief="solid")
password.place(x=25, y=215, width=140, height=30)
password.insert(0, "Password")
#
confirm_password = Entry(relief="solid")
confirm_password.place(x=235, y=215, width=140, height=30)
confirm_password.insert(0, "Confirm Password")
#
davom_etish = Button(text="Davom etish", font=("Arial", 14), bg="yellow", fg="magenta", command=open_homepage_file)
davom_etish.place(x=25, y=265, width=350, height=50)

window = mainloop()