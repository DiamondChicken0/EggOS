
from multiprocessing.connection import wait
from operator import truediv
from tkinter import *
import tkinter as tk
from time import perf_counter, sleep
from tkinter import ttk

# declare the reg stuff
progressCheck = "false"


def progDone():
    print("done")

# declare the window stuff
window = Tk()
window.title("EggOS")
window.maxsize(width=800, height=600)
window.minsize(width=800, height=600)
window.configure(width=800, height=600)
window.resizable(0,0)
window.iconphoto(True, tk.PhotoImage(file="EggOS\EggOS Assets\Egg Favicon.png"))
window.eval('tk::PlaceWindow . center')



# visual elements
progressBar = ttk.Progressbar(window, orient= "horizontal", mode= "determinate", length=300)
progressBar.pack(pady=350)

timeStart = perf_counter
sleep(1000)
progressBar.start()
sleep(1000)

window.mainloop() 



# !DO NOT REMOVE!
# this places stuff on screen






