from tkinter import *
from time import time
# from tkinter.ttk import Button
demos= Tk()
b = Button(demos, text = 'Welcome To My Domain')
b.pack(pady = 77,side = TOP)
pink = Button(demos, text = "pink",bg='pink')
pink.pack( side = TOP)
green = Button(demos, text = "green")
green.pack( side = BOTTOM )
violet = Button(demos, text = "violet")
violet.pack( side = LEFT )
yellow = Button(demos, text = "yellow")
yellow.pack( side = RIGHT)
print('The Tk Widget is running on the screen...')
startingtime = time()
pink.after(20000,pink.config(bg='red'))
# demos.after(20000, demos.destroy)
demos.mainloop()
endingtime = time()
print('The Tk Widget is closed after % d seconds' % (endingtime-startingtime))