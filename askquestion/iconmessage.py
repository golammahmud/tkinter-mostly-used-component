# ICONS that We can use in Options 
 

# Error
# Info
# Warning
# Question
# We can change
# illustration of icon - Error
from tkinter import *
from tkinter import messagebox

main = Tk()

def check():
    messagebox.askquestion("Form", 
						"Is your name correct?", 
						icon ='error')

main.geometry("100x100")
B1 = Button(main, text = "check", command = check)
B1.pack()

main.mainloop()
