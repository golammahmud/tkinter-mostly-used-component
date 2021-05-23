# Python program to demonstrate 
# scale widget 

from tkinter import *
from tkinter.ttk import *

root = Tk() 
root.geometry("400x300") 

v1 = DoubleVar() 

def show1(): 
	
	sel = "Horizontal Scale Value = " + str(v1.get()) 
	l1.config(text = sel, font =("Courier", 14)) 


s1 = Scale( root, variable = v1, 
		from_ = 1, to = 100, 
		orient = HORIZONTAL,) 

l3 = Label(root, text = "Horizontal Scaler") 

b1 = Button(root, text ="Display Horizontal", 
			command = show1, 
			)

l1 = Label(root) 


s1.pack(anchor = CENTER) 
l3.pack() 
b1.pack(anchor = CENTER) 
l1.pack() 

root.mainloop() 
# root – root window.
# bg – background colour
# fg – foreground colour
# bd – border
# orient – orientation(vertical or horizontal)
# from_ – starting value
# to – ending value
# troughcolor – set colour for trough.
# state – decides if the widget will be responsive or unresponsive.
# sliderlength – decides the length of the slider.
# label – to display label in the widget.
# highlightbackground – the colour of the focus when widget is not focused.
# cursor – The cursor on the widget ehich could be arrow, circle, dot etc.
# Methods

# set(value) – set the value for scale.
# get() – get the value of scale.