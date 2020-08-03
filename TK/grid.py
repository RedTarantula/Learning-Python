from tkinter import *
import os

root = Tk()

# myLabel = Label(root,text = "Hello World!")
# myLabel.pack()

myLabel = Label(root,text = "HHHHHH")
myLabel.grid(row = 0, column = 0)

myLabel = Label(root,text = "WWWWWW")
myLabel.grid(row = 0, column = 1)

Label(root,text = "FFFFFFFF").grid(row = 1, column = 1)
Label(root,text = "WOOOOOOO").grid(row = 1, column = 0)

root.mainloop()