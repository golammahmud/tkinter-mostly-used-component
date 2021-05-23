from  tkinter import  *
root =Tk()
root.geometry("600x500")
w1=PanedWindow(root)
w1.pack(fill=BOTH,expand=1)

leftwin=Entry(w1,relief=SUNKEN,)
w1.add(leftwin)

# second paned window

w2 = PanedWindow(w1, orient=VERTICAL)  
w1.add(w2)  
  
e1 = Entry(w2)
e2 = Entry(w2)
  
w2.add(e1)  
w2.add(e2)  

btn=Button (w2,text='Addition',)
btn.pack()
w2.add(btn)


w3=PanedWindow(w1,orient=HORIZONTAL)
w1.add(w3)

root.mainloop()
