##import library
from tkinter import *
import time
from playsound import playsound

#######################timer countdown##########

##########fun to start countdown
paused = False
running = False
def validate(P):
    global paused
    if len(P) == 0 and not paused:
        # empty Entry is ok
        return True
    elif len(P) == 1 and P.isdigit() and not paused:
        # Entry with 1 digit is ok
        return True
    elif len(P) == 2 and P.isdigit() and not paused:
        # Entry with 1 digit is ok
        return True
    else:
        # Anything else, reject it
        return False

## display window 
root = Tk()
root.geometry('550x400')
root.resizable(0,0)
root.config(bg ='CadetBlue3')
root.title('CountDown Timer')
root.iconbitmap('Add-your-path/python-projects-countdown-time/countdown-timer/resources/logo.ico')
Label(root, text = 'Countdown Timer' , font = 'arial 30 bold',  bg ='CadetBlue3').pack()
vcmd = (root.register(validate), '%P')

#storing seconds
sec = StringVar()
Entry(root, textvariable = sec, width = 2, font = 'arial 15',bg='AntiqueWhite2', validate="key").place(x=358, y=110)
sec.set('00')

#storing minutes
mins= StringVar()
Entry(root, textvariable = mins, width = 2, font = 'arial 15',bg='AntiqueWhite2',validate="key").place(x=329, y=110)
mins.set('00')

# storing hours
hrs= StringVar()
Entry(root, textvariable = hrs, width = 2, font = 'arial 15',bg='AntiqueWhite2', validate="key").place(x=300, y=110)
hrs.set('00')

def countdown():
    global paused
    global done
    global running
    running = True
    paused = False
    hours=int(hrs.get())
    minutes=int(mins.get())
    secs=int(sec.get())
    if (secs==0 and minutes==0 and hours==0):
        return
    done = False
    times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
    while times > -1 and not done and not paused:
        minute,second = (times // 60 , times % 60)
        
        hour = 0
        if minute > 60:
            hour , minute = (minute // 60 , minute % 60)
            
        time.sleep(1)
        sec.set(second)
        mins.set(minute)
        hrs.set(hour)
        root.update()

        if(times == 0):
            playsound("countdown-timer/resources/alarm.mp3")
            done = True
            sec.set('00')
            mins.set('00')
            hrs.set('00')
            running = False
        times -= 1

# For Reset Button
def reset():
    global done
    global running
    running = False
    done=True
    hrs.set('00')
    mins.set('00')
    sec.set('00')

def update(hour,minute,second):
    # actions to perform
    sec.set(second)
    mins.set(minute)
    hrs.set(hour)
    root.after(10, update) #iterative

# For Pause Button
def pause():
    global paused
    global running
    if not paused and running:
        paused=True
        root.update()

# For Resume Button
def resume():
    global paused
    global running
    if paused and running:
        paused = False
        countdown()

# Label for the Timer
Label(root, font ='arial 22 bold', text = 'Set Timer -',   bg ='CadetBlue3').place(x = 135 ,y = 100)

# Buttons
# START
Button(root, text='START', bd ='5', command = countdown, bg = 'CadetBlue4', font = 'arial 25 bold').place(x=100, y=170)
# RESET
button_reset = Button(root, text='RESET', bd ='5', command = reset, bg = 'CadetBlue4', font = 'arial 25 bold').place(x=300, y=170)
# PAUSE
button_pause = Button(root, text='PAUSE', bd ='5', command = pause, bg = 'CadetBlue4', font = 'arial 25 bold').place(x=100, y=270)
# RESUME
button_pause = Button(root, text='RESUME', bd ='5', command = resume, bg = 'CadetBlue4', font = 'arial 24 bold').place(x=290, y=270)

root.mainloop()
