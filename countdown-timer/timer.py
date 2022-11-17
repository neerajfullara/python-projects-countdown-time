from tkinter import *
import time # For clock

root = Tk()
root.title('CountDown Timer')
root.iconbitmap('C:/Users/neera/Desktop/python-projects/countdown-timer/resources/logo.ico')
root.geometry("500x300")

# Added the clock Functionality
def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    C_label.config(text=hour +":" + minute + ":" + second)
    C_label.after(1000,clock)

def  update():
    C_label.config(text="")

# Styling of Clock
C_label = Label(root, text="", font=("Georgia", 40),fg="black")
C_label.pack(pady=30)

clock()

root.mainloop()