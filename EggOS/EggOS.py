
from ast import Delete
from cProfile import label
from concurrent.futures import thread
from email.mime import image
from multiprocessing.connection import wait
from sqlite3 import Time
from struct import pack
import threading
from operator import truediv
from tkinter import *
import tkinter as tk
from time import perf_counter, sleep, time
from tkinter import ttk
from PIL import Image, ImageTk
#"EggOS\EggOS Assets\gaggleofchickens.png"

# declare the window stuff
window = Tk()
window.title("EggOS")
window.maxsize(width=800, height=600)
window.minsize(width=800, height=600)
window.configure(width=800, height=600)
window.resizable(0,0)
window.iconphoto(True, tk.PhotoImage(file="EggOS\EggOS Assets\Egg Favicon.png"))
window.eval('tk::PlaceWindow . center')

EggOStext = tk.Label(window, text="EggOS", fg="yellow")
EggOStext.config(font=("Calibri Bold",100))
EggOStext.place(x= (400 - (EggOStext.winfo_reqwidth()/2)),y=275)

tempimg = Image.open("EggOS\EggOS Assets\gaggleofchickens.png")
tempimg = tempimg.resize((200,150), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(tempimg)

ChickenGroup = tk.Label(window, image=img)
ChickenGroup.place(x=300,y=150)

StartButton = tk.Button(window,text="Press to Begin", command=animateStart)

def animateStart():
    if (x < 800):
        ChickenGroup.after(30, animateStart, )









# !DO NOT REMOVE!
# this places stuff on screen
window.mainloop() 





