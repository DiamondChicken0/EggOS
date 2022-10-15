from tkinter import *
import tkinter as tk

# declare the reg stuff
loadingScreenWait = 3000

# declare the window stuff
window = Tk()
window.title("EggOS")
window.maxsize(width=1920, height= 1080)
window.configure(width=1280, height=720)
window.configure(bg='lightgray')
window.iconphoto(True, tk.PhotoImage(file="Egg Favicon.png"))
window.eval('tk::PlaceWindow . center')


window.mainloop()


