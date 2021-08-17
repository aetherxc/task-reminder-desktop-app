import tkinter
from tkinter import messagebox
from time import time, sleep

# hide main window
root = tkinter.Tk()
root.withdraw()

# message box display
while True:
    sleep(60 - time() % 60)
    messagebox.showinfo("Stuff you gotta do"," w3schools \n dl labs from zhen \n cv and nlp labs \n youtube vids \n brilliant courses")