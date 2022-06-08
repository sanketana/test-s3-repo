from tkinter import *
from tkinter import ttk 
import random
import tkinter
from PIL import Image,ImageTk
import color game


win=Tk()
wcol=Tk()
rps=Tk()

win.title('Game Launcher')
win.geometry('300x300')

wcol.title('Color Game')
wcol.geometry('400x400')

rps.title('Rock Paper Scissors')
rps.geometry('300x300')

colors=['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']
score=0
timeleft=30

userscore=compscore=0
uc=cc=''

wcol.withdraw()
rps.withdraw()

def newwin1():
	wcol.deiconify()

def newwin2():
	rps.deiconify()

def startGame(entry):
	if timeleft==30:
		countdown()
	nextColor()
def nextColor():
	global score
	global timeleft
	if timeleft>0:
		e.focus_set()
		if e.get().lower()==colors[1].lower():
			score+=1
		e.delete(0,tkinter.END)
		random.shuffle(colors)
		lc.config(fg=str(colors[1]),text=str(colors[0]))
		l4.config(text='Score: '+str(score))
def countdown():
	global timeleft
	if timeleft>0:
		timeleft-=1
		l3.config(text='Time: '+str(timeleft))
		l3.after(1000,countdown)
def choicetonumber(choice):
	rpss={'scissor':0,'paper':1,'rock':2}
	return rpss[choice]
def numbertochoice(number):
        rpss={'scissor':0,'paper':1,'rock':2}
        return rpss[number]
def rcc():
	return random.choice(['scissor','paper','rock'])
def result(hchoice,cchoice):
	global userscore
	global compscore
	user=choicetonumber(hchoice)
	comp=numbertochoice(cchoice)
	if user==comp:
		statusl.configure(text='Tie!')
	elif ((user-comp)%3==1):
		statusl.configure(text="Computer Wins!")
		compscore+=1
	else:
		statusl.configure(text='You Win!')
		userscore+=1
	userchoice.configure(text=f'Your Choice: ')
	compchoice.configure(text=f"Computer's Choice: ")
	userscorel.configure(text=f'Your Score: {userscore}')
	compscorel.configure(text=f"Computer's Score: {compscore}")
	if uc=='rock':
		userchoicepic.configure(image=rockphoto)
	elif uc=='paper':
		userchoicepic.configure(image=paperphoto)
	else:
		userchoicepic.configure(image=scissorphoto)
	if cc=='rock':
		compchoicepic.configure(image=rockphoto)
	elif cc=='paper':
		compchoicepic.configure(image=paperphoto)
	else:
		compchoicepic.configure(image=scissorphoto)

def rock():
	global uc 
	global cc 
	uc='rock'
	cc=rcc()
	result(uc,cc)
def paper():
	global uc 
	global cc 
	uc='paper'
	cc=rcc()
	result(uc,cc)
def scissor():
	global uc 
	global cc 
	uc='scissor'
	cc=rcc()
	result(uc,cc)

def resetbutton():
	userscore=compscore=0
	userscorel.configure(text=f"Your Score: {userscore}")
	compscorel.configure(text=f"Computer's Score: {compscore}")

rockimg=Image.open('rock.png')
rockimg.thumbnail((30,30),Image.ANTIALIAS)
rockphoto=ImageTk.PhotoImage(rockimg)
paperimg=Image.open('paper.png')
paperimg.thumbnail((30,30),Image.ANTIALIAS)
paperphoto=ImageTk.PhotoImage(paperimg)
scissorimg=Image.open('scissor.png')
scissorimg.thumbnail((30,30),Image.ANTIALIAS)
scissorphoto=ImageTk.PhotoImage(scissorimg)

Label(win,text='Games').place(x=110,y=10)
Label(win,text=' Color Game').place(x=85,y=50)
Label(win,text=' Tic-Tac-Toe').place(x=85,y=75)
Label(win,text=' Rock Paper Scissors').place(x=85,y=100)
Label(win,text=' Quit').place(x=85,y=125)
Button(win,text='1',command=newwin1).place(x=75,y=50)
Button(win,text='2').place(x=75,y=75)
Button(win,text='3').place(x=75,y=100)
Button(win,text='4',command=exit).place(x=75,y=125)


l1=Label(wcol,text='Objective: Type the color of the word and not the word itself').place(x=60,y=30)
l2=Label(wcol,text='Press Enter to start').place(x=180,y=50)
l3=Label(wcol,text='Time:')
l3.place(x=210,y=70)
l4=Label(wcol,text='Score: ')
l4.place(x=200,y=90)
lc=Label(wcol,font=('Helvetica',60))
lc.pack()
lc.place(x=200,y=150)
e=Entry(wcol,width=10)
e.focus_set()
e.place(x=200,y=240)
#deadbutton=Button(wcol,text='Quit',command=wcol.destroy()).place(x=100,y=100)
wcol.bind('<Return>',startGame)
win.bind('<Return>',startGame)
e.focus_set()

br=Button(rps,text='Rock',image=rockphoto,command=rock)
br.place(x=100,y=130)
bp=Button(rps,text='Paper',image=paperphoto,command=paper)
bp.place(x=100,y=160)
bs=Button(rps,text='Scissor',image=scissorphoto,command=scissor)
bs.place(x=100,y=200)
rb=Button(rps,text='Reset',command=resetbutton)
rb.place(x=30,y=240)

userchoice=Label(rps,text='Your Choice: ')
userchoice.place(x=10,y=80)
compchoice=Label(rps,text="Computer's Choice: ")
compchoice.place(x=140,y=80)
userscorel=Label(rps,text='Your Score: ')
userscorel.place(x=10,y=210)
compscorel=Label(rps,text="Computer's Score: ")
compscorel.place(x=150,y=210)
statusl=Label(rps,text='')
statusl.place(x=120,y=250 )
userchoicepic=Label(rps)
userchoicepic.place(x=100,y=80)
compchoicepic=Label(rps)
compchoicepic.place(x=270,y=80)

win.mainloop()
wcol.mainloop()
rps.mainloop()