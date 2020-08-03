# TKinter GUI

from tkinter import * # already included
import os
os.system('clear')

root = Tk() # window
root.title("OWO")
root.geometry("400x600")


def hello():
	helloLabel = Label(root, text="NO U " + myTextbox.get())
	helloLabel.pack()


myLabel = Label(root, text="Enter your first name:")
myLabel.pack()

myTextbox = Entry(root, width=30)
myTextbox.pack()

myButton = Button(root,text="Get fucked, bitch", command=hello)
myButton.pack()

root.mainloop()