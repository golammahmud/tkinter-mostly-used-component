from tkinter import *
from PIL import Image,ImageTk
canvas_width=600
canvas_height=400
root=Tk(className='tkinter canvas')
root.geometry(f"{canvas_width}x{canvas_height}")
can_widget=Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()


image=Image.open('laptop.jpeg')
filename = ImageTk.PhotoImage(image =image,)
image = can_widget.create_image(250, 150, anchor=W, image=filename,)


root.mainloop()