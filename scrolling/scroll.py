# from tkinter import *
# from tkinter.ttk import *

# root=Tk(className="Tkinter Scrolling")
# root.geometry("500x400")

# w=Label(root,text="Tkinter Scrooling",font='cosmica 20 bold italic').pack()

# scrollbar=Scrollbar(root,orient=VERTICAL,)
# scrollbar.pack(side=RIGHT,fill=Y)


# mylist=Listbox(root,yscrollcommand=scrollbar.set,width=70,bg='gray',)


# for line in range(1,20):
#     mylist.insert(END,"Tkinter scrolling Number:"+str(line))
    
# mylist.pack(side=LEFT,fill=BOTH)
# scrollbar.config(command=mylist.yview)

# root.mainloop()
from tkinter import *

root = Tk()
scrollbar = Scrollbar(root,cursor='spider',activebackground='blue')
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

mainloop()