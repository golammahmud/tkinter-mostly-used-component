from tkinter import *
from tkinter import messagebox

tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('PythonExamples.org - Tkinter Example')

def showMsg():  
    Label_1 = Label(text = "DONE")
    Label_1.pack()
    button.configure(state=DISABLED)

button = Button(tkWindow,
	text = 'Submit',
	command = showMsg)  
button.pack()  
  
tkWindow.mainloop()