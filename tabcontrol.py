from tkinter import *

from tkinter import ttk

window = Tk()
window.geometry('550x500')
window.title("Welcome to LikeGeeks app")

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)

tab2 = ttk.Frame(tab_control)

tab_control.add(tab2, text='single page',padding=10,)

tab_control.add(tab1, text='multiple pages',padding=10 ,)




#labelframe start here

fr=Frame(tab1)
fr.pack()

labelframe1 = LabelFrame(fr, text="Positive Comments",  
                bd=10,width=30,height=10) 
labelframe1.pack()
l1=Label(labelframe1,text="Choose Your Playing Option",font='rumanian 20 bold bold')
l1.pack()

frame1=Frame(tab1)
frame1.pack(pady=10)

frame2 = Frame(tab1)
frame2.pack(pady=10)

var1=IntVar()
var1.set('')
var2=IntVar()
var2.set('')

#page entry section
l2=Label(frame1,text='Starting Page',font='lucida 10 bold').grid(row=0,column=6)
entry1=Entry(frame1,textvariable=var1,font='lucida 15 bold')
entry1.grid(row=1,column=6,padx=20)
# entry1.pack(side=LEFT)

l3=Label(frame1,text='Ending Page',font='lucida 10 bold').grid(row=0,column=8)
entry2=Entry(frame1,textvariable=var2,font='lucida 15 bold')
entry2.grid(row=1,column=8,padx=20)


btn1=Button(frame2,text='play',font='lucida 10 bold',padx=10,relief=RAISED,bd=5,).pack(side='left',padx=10)
btn2=Button(frame2,text='pause',font='lucida 10 bold',padx=10,relief=RAISED,bd=5).pack(side='right',padx=10)

#tab multiple pages
l1=Label(tab2,text="Choose Your Playing Option",font='rumanian 20 bold bold')
l1.pack()

frame1=Frame(tab2)
frame1.pack(pady=10)

frame2 = Frame(tab2)
frame2.pack(pady=10)

var1=IntVar()
var1.set('')

#page entry section
l2=Label(frame1,text='Starting Page',font='lucida 10 bold').grid(row=0,column=6)
entry1=Entry(frame1,textvariable=var1,font='lucida 15 bold')
entry1.grid(row=1,column=6,padx=20)

btn1=Button(frame2,text='play',font='lucida 10 bold',padx=10,relief=RAISED,bd=5,).pack(side='left',padx=10)
btn2=Button(frame2,text='pause',font='lucida 10 bold',padx=10,relief=RAISED,bd=5).pack(side='right',padx=10)





tab_control.pack(expand=1, fill='both')

window.mainloop()