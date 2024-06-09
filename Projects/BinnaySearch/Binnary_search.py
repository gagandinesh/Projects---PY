# install Tkinter

from tkinter import *
import tkinter as tk

# Define Binnary search


def binnary_search():
    l = E.get().split(" ")
    for i in range(0, len(1)):
        l[i] == int(l[i])

    num = N.get()
    first = 0
    last = len(l) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if l[mid] == num:
            found = True
        else:
            if num < l[mid]:
                last = mid - 1
            else:
                first = mid + 1
        if found == True:
            Label(window, text="Number found  in the Given List", font=("Arial")).place(
                x=280, y=180
            )

        else:
            Label(
                window, text="Number not found in the Above List", font=("Calibri")
            ).place(x=240, y=210)


# Create Window
window = Tk()
window.geometry("700x350")
window.title("Binnary search")
head = Label(window, text="Lets Do Binnary Search", font=("Arial")).pack()

# Entry box
Entry(window, textvariable=E).pack()
Entry(window, textvariable=N).place(x=280, y=120)

# Create a Button
Button(window, text="Search", command=binnary_search, font=("Airal"))

N = tk.IntVar()
window.mainloop()
