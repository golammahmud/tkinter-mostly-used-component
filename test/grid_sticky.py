from tkinter import *
root = Tk()
root.geometry("400x300")



btn_columnspan = Button(root, text="I have a columnspan of 9")
btn_columnspan.grid(columnspan=9,ipadx=40,padx=30,ipady=20,pady=35)




btn_sticky = Button(root, text="I'm stuck to north-east")
btn_sticky.grid(sticky=E)

root.mainloop()