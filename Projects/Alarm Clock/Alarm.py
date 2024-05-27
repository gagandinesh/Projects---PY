# install playsound--> pip install playsound (if u get error while installing use pip install --upgrade setuptools wheel
# pip install playsound
# download any sound and place it in the same folder
# Run using python debugger


from playsound import playsound
import time

clear = "\033[2J"
clear_and_return = "\033[H "


def alarm(seconds):
    time_elapsed = 0
    print(clear)

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{clear_and_return}{minutes_left:02d}:{seconds_left:02d}")
    playsound("C:\Python(pract)\Projects\Alarm Clock\Alarm.mp3")


minutes = int(input("How many minutes do you want : "))
seconds = int(input("How many seconds to wait : "))
total_seconds = minutes * 60 + seconds

alarm(total_seconds)
