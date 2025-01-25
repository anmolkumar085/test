from tkinter import *
import os
from PIL import ImageTk, Image
from gif import ImageLabel
win = Tk()

win.title("GameSera")
win.geometry("1200x1000")
win.configure(background='white')
img = ImageTk.PhotoImage(Image.open("img/atari-breakout-game.webp"))
img2 = ImageTk.PhotoImage(Image.open("img/ezgif.com-gif-maker (2).jpg"))
img3 = ImageTk.PhotoImage(Image.open("img/snake-pass-key-art-no-logo (1).jpg"))
img4 = ImageTk.PhotoImage(Image.open("img/depositphotos_199943868-stock-photo-wooden-tic-tac-toe-game (1).jpg"))
img5 = ImageTk.PhotoImage(Image.open("img/Boolean-image.jpg"))
img6 = ImageTk.PhotoImage(Image.open("img/table (1).jpg"))

def atari():
    os.system('Atari.py')
def floppy():
    os.system('angry.py')
def snake():
    os.system('snake.py')
def tic():
    os.system('tic.py')
def true():
    os.system('true.py')
def ping():
    os.system('pong.py')



label = ImageLabel(win)
label.grid(row=0, column=0, columnspan=3)
label.load("img/ezgif.com-gif-maker (4).gif")

label = Label(image = img, height=200,width=200)
label.grid(padx=20,pady=20,row=1,column=0)
Button(win, text="Atari",height=3,width=16,command=atari).grid(padx=130,pady=1,row=2,column=0)

label = Label(image = img2, height=200,width=300)
label.grid(padx=20,pady=20,row=1,column=1)
Button(win, text="Flappy bird",height=3,width=16,command=floppy).grid(padx=130,pady=1,row=2,column=1)

label = Label(image = img3, height=200,width=300)
label.grid(padx=20,pady=20,row=1,column=2)
Button(win, text="Snake",height=3,width=16,command=snake).grid(padx=130,pady=1,row=2,column=2)

label = Label(image = img4, height=200,width=300)
label.grid(padx=20,pady=20,row=3,column=0)
Button(win, text="Button-1",height=3,width=16,command=tic).grid(padx=130,pady=1,row=4,column=0)

label = Label(image = img5, height=200,width=300)
label.grid(padx=20,pady=20,row=3,column=1)
Button(win, text="Button-1",height=3,width=16,command=true).grid(padx=130,pady=1,row=4,column=1)

label = Label(image = img6, height=200,width=290)
label.grid(padx=20,pady=20,row=3,column=2)
Button(win, text="Button-1",height=3,width=16,command=ping).grid(padx=130,pady=1,row=4,column=2)

win.mainloop()
