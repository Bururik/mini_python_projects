import sys
from tkinter import *

App=Tk()

def helloCallBack():
    messagebox.showinfo( "Hello Python", "I will destroy everyone")
    
b = Button(App, text = "kill", command = helloCallBack)

b.pack()

App.geometry("600x400")

App.mainloop()
