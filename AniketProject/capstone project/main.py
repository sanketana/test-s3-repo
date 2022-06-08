from tkinter import *
from tkinter import ttk 
import random
import tkinter
from PIL import Image,ImageTk
import colorgame
import rockpaperscissors
import tictactoe

win=Tk()


win.title('Game Launcher')
win.geometry('300x300')

def colorgamefunc():
	colorgame.colorprog()
	

def rpsfunc():
	rockpaperscissors.rpsprog()

def tttfunc():
	tictactoe.tttprog()

Label(win,text='Games').place(x=110,y=10)
Label(win,text=' Color Game').place(x=85,y=50)
Label(win,text=' Tic-Tac-Toe').place(x=85,y=75)
Label(win,text=' Rock Paper Scissors').place(x=85,y=100)
Label(win,text=' Quit').place(x=85,y=125)
Button(win,text='1',command=colorgamefunc).place(x=75,y=50)
Button(win,text='2',command=tttfunc).place(x=75,y=75)
Button(win,text='3',command=rpsfunc).place(x=75,y=100)
Button(win,text='4',command=exit).place(x=75,y=125)

win.mainloop()
