import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Disappearing Text Writing App")
window.config(width=500, height=500, background="#222831", pady=100)

time = 0
times_up = False

text = Text(window, {"bg": "#222831", "bd": 150, "fg": "#00ADB5", "height": 2, "font": ("Courier New", 30),
                     "insertbackground": "#FF2E63", "wrap": "word", "highlightthickness": 0})
text.focus()
text.mark_set("insert", "%d.%d" % (1.0, 0.0))
text.pack()



def countdown():
    global times_up
    if times_up:
        global time
        time += 1
        if time >= 5:
            text.delete("1.0", END)
            times_up = False

        window.after(1000, countdown)



def text_check(event=None):
    global times_up
    global  time
    if times_up:
        time = 0
    else:
        times_up = True
        countdown()


text.bind("<Key>", text_check)
window.mainloop()
