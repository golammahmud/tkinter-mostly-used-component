from tkinter import *
import time
root = Tk(className="status bar")
root.geometry("500x500")

def update():
    statusbar.set('bussy')
    time.sleep(2)
    statusbar.set('ready now')



statusbar=StringVar()
statusbar.set('ready')
sbar=Label(root,textvariable=statusbar,relief=SUNKEN,anchor='w')
sbar.pack(side=BOTTOM,fill=X)

btn=Button(root,text='update',command=update).pack()



root.mainloop()