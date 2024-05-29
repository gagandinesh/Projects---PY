# install tkinter module for GUI
# install time and date moudule ---  pip install datetime
# install Toast notification module-- pip install win10toast (helps in displaying notification on desktop)
## "LETS START CODIN"

# Time Module

from threading import Timer
import time
import tkinter as tk
from tkinter import *
from datetime import datetime

# Create a Window ""code""

Window = Tk()
Window.geometry("600x500")
Window.title("Count Timer")
head = Label(Window, text="Countdown Clock", font=("Calibri 15"))
head.pack(pady=20)

Label(Window, text="Enter Time in HH : MM : SS", font=("bold")).pack()
Entry(Window, textvariable= hour, width=30).pack()
Entry(Window, textvariable= minutes, width=30).pack()
Entry(Window, textvariable= seconds, width=30).pack()

# NOTE - pack() funtion makes sure tht ther is no need of X and Y asxis and decides automatically

# Create Ckeck Box

checkbutton(text="Check for music", onvalue=True, variable=check).pack()

checkbutton(Window, text="set Timer", command=countdown, bg="Pink").place(x=260, y=230)

# Show Current Time

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
Label(Window, text=current_time).pack()

# Function for countdown and Time


def countdown():
    t = count.get()
    while t:
        hour,mins, secs = divmod(t, 60)
        display = "{:02d}:{:02d}".format(mins, secs)
        time, sleep(1)
        t -= 1
        Label(Window, text=display).pack()

    Label(window, text="Time's up Fellas", font=("bold", 20)).place(x=250, y=290)


# Notification

toast = ToastNotifier()
toast.show_toast(
    "Notified", "Timer is signing off", duration=20, icon_path=None, threaded=True
)

# Beep Sound

if check.get() == True:
    winsound.Beep(440, 1000)

Window.update()
Window.mainloop()
