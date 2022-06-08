from tkinter import *
import tkinter.messagebox as msg
import random
from PIL import Image,ImageTk

userscore=compscore=0
uc=cc=''
def rpsprog():

	

	rps=Tk()
	rps.geometry('300x300')
	rps.title('Rock Paper Scissors')

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

	rps.mainloop()