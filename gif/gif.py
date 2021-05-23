from tkinter import *
from PIL import Image,ImageTk

root=Tk(className='Display Gif')
root.geometry("500x400")


info=Image.open('gif/1.gif')
frame=info.n_frames

print(frame)



root.mainloop()