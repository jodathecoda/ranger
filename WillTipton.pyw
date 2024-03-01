import os
from tkinter import *
from PIL import ImageTk,Image
import random

global cwd
cwd = os.getcwd()

root = Tk()
root.iconbitmap("mush_small.ico")
root.title('Ranger')

SB_7  = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\7_SB.png"))
BB_7  = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\7_BB.png"))
SB_10 = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\10_SB.png"))
BB_10 = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\10_BB.png"))
SB_15 = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\15_SB.png"))
BB_15 = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\15_BB.png"))
SB_20 = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\20_SB.png"))
BB_20 = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\20_BB.png"))


# A Radiobutton to toggle between images
bigblinds = IntVar()

def call():
    canvas.delete(ALL)
    #heads up
    if bigblinds.get() == 1:
        canvas.create_image((2, 2), image=SB_7, anchor=NW)
    elif bigblinds.get() == 2:
        canvas.create_image((2, 2), image=BB_7, anchor=NW)
    elif bigblinds.get() == 3:
        canvas.create_image((2, 2), image=SB_10, anchor=NW)
    elif bigblinds.get() == 4:
        canvas.create_image((2, 2), image=BB_10, anchor=NW)
    elif bigblinds.get() == 5:
        canvas.create_image((2, 2), image=SB_15, anchor=NW)
    elif bigblinds.get() == 6:
        canvas.create_image((2, 2), image=BB_15, anchor=NW)
    elif bigblinds.get() == 7:
        canvas.create_image((2, 2), image=SB_20, anchor=NW)
    elif bigblinds.get() == 8:
        canvas.create_image((2, 2), image=BB_20, anchor=NW)
    else:
        pass

def randomizer():
    rnd = random.randint(1,100)
    R9['text'] = str(rnd)[0:5] + "%"

#Description
R1=Radiobutton(root, text="7 SB", variable=bigblinds, value=1, command=call)
R1.grid(row=0, column=0, sticky=N+E)
R2=Radiobutton(root, text="7 BB", variable=bigblinds, value=2, command=call)
R2.grid(row=1, column=0, sticky=N+E)
R3=Radiobutton(root, text="10 SB", variable=bigblinds, value=3, command=call)
R3.grid(row=2, column=0, sticky=N+E)
R4=Radiobutton(root, text="10 BB", variable=bigblinds, value=4, command=call)
R4.grid(row=3, column=0, sticky=N+E)
R5=Radiobutton(root, text="15 SB", variable=bigblinds, value=5, command=call)
R5.grid(row=4, column=0, sticky=N+E)
R6=Radiobutton(root, text="15 BB", variable=bigblinds, value=6, command=call)
R6.grid(row=5, column=0, sticky=N+E)
R7=Radiobutton(root, text="20 SB", variable=bigblinds, value=7, command=call)
R7.grid(row=6, column=0, sticky=N+E)
R8=Radiobutton(root, text="20 BB", variable=bigblinds, value=8, command=call)
R8.grid(row=7, column=0, sticky=N+E)



R9=Button(root, text="% RANDOMIZER %", command = lambda: randomizer())
#R7.grid(row=6, column=0, rowspan=6,columnspan=2,sticky=N+E)
R9.grid(row=8, column=0, columnspan=2, sticky=N+E+W+S)


# A canvas for mouse events and image drawing
canvas = Canvas(root, height=450, width=450,)
canvas.grid(column=1, row=0, rowspan=6, sticky=W)
#canvas.create_image((2, 2), image=pushfold_img, anchor=NW)
canvas.create_image((0, 1), image=SB_20, anchor=NW)

# Configure columns 0 and 1 to expand when the window is resized
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Enter event loop
root.mainloop()