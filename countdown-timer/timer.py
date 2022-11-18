import tkinter
from tkinter import *
import  datetime
import winsound

class countDown(tkinter.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.widget_create()
        self.show_Widgets()
        self.seconds_Left=0
        self.time_On=False

    def show_Widgets(self):
        self.label.pack()
        self.entry.pack()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()
        self.pause.pack()
        self.resume.pack()

    def widget_create(self):
        self.label = tkinter.Label(self,text='Enter the time')
        self.entry = tkinter.Entry(self,justify="center")
        self.entry.focus_set()
        self.reset = tkinter.Button(self,text="Reset",command=self.reset_button)
        self.start = tkinter.Button(self,text="Start",command=self.start_button)
        self.stop = tkinter.Button(self,text="Stop",command=self.stop_button)
        self.pause = tkinter.Button(self,text="Pause",command=self.pause_button)
        self.resume = tkinter.Button(self,text="Resume",command=self.resume_button)

    def CountD(self):
        self.label["text"] = self.convert_seconds_left_time()

        if self.seconds_Left:
            self.seconds_Left -= 1
            self.time_On = self.after(1000,self.CountD)
        else:
            self.time_On = False
            winsound.PlaySound('C:/Users/neera/Desktop/python-projects/countdown-timer/resources/alarm.mp3', winsound.SND_FILENAME)

    def reset_button(self):
        self._second_left = 0
        self.stop_timer()
        self.time_On = FALSE
        self.label["text"] = "Enter the time in seconds."
        self.start.forget()
        self.stop.forget()
        self.reset.forget()
        self.pause.forget()
        self.reset.forget()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()
        self.pause.pack()
        self.reset.pack()

    def stop_button(self):
        self.seconds_Left = int(self.entry.get())
        self.stop_timer()

    def start_button(self):
        self.seconds_Left = int(self.entry.get())
        self.stop_timer()
        self.CountD()
        self.start.forget()
        self.stop.forget()
        self.pause.forget()
        self.reset.forget()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()
        self.pause.pack()
        self.reset.pack()

    def pause_button(self):
        self.seconds_Left = int(self.entry.get())
        self.pause_timer()

# Work on the Resume button part
    def resume_button(self):
        self.seconds_Left = int(self.entry.get())
        self.stop_timer()
        self.CountD()
        self.start.forget()
        self.stop.forget()
        self.pause.forget()
        self.reset.forget()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()
        self.pause.pack()
        self.reset.pack()

    def stop_timer(self):
        if self.time_On:
            self.after_cancel(self.time_On)
            self.time_On = False

    def pause_timer(self):
        if self.time_On:
            self.after_cancel(self.time_On)
            self.time_On = False

    def convert_seconds_left_time(self):
        return datetime.timedelta(seconds = self.seconds_Left)

# Main
if __name__ == "__main__":
    root = tkinter.Tk()
    root.title('CountDown Timer')
    root.iconbitmap('C:/Users/neera/Desktop/python-projects/countdown-timer/resources/logo.ico')
    root.geometry("500x300")
    root.resizable(False,False)

    countdown = countDown(root)
    countdown.pack()

    root.mainloop()