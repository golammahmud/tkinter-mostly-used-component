from tkinter import *

def harry(event):
    print(f"You clicked on the button at {event.x}, {event.y}")
def pr(event):
    pass
root = Tk()
root.title("Events in Tkinter")
root.geometry("644x334")

widget = Button(root, text='Click me please')
widget.pack()

widget.bind('<B1-Motion>', pr)
widget.bind('<Button-1>', harry)
widget.bind('<Double-1>', quit)
root.mainloop()