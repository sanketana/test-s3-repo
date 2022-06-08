from tkinter import *
import tkinter.messagebox as msg

digits=[1,2,3,4,5,6,7,8,9]
mark=''
count=50
panels=['panel']*10

#def tttprog():

win=Tk()
win.title('Tic-Tac-Toe')
Label(win,text='Player 1 : X').grid(row=5,column=5)
Label(win,text='Player 2 : O').grid(row=5,column=6)

def winner(panels,sign):
	return ((panels[1]==panels[2]==panels[3]==sign) 
		or (panels[1] == panels[4] == panels[7]== sign) 
		or (panels[1] == panels[5] == panels[9] == sign) 
		or (panels[2] == panels[5] == panels[8] == sign) 
		or (panels[3] == panels[6] == panels[9] == sign) 
		or (panels[3] == panels[5] == panels[7] == sign) 
		or (panels[4] == panels[5]== panels[6] == sign) 
		or (panels[7] == panels[8] == panels[9] == sign))

def checker(digit):
	global count, mark, digits
	if digit==1 and digit in digits:
		digits.remove(digit)
		if count%2==0:
			mark='X'
			panels[digit]=mark
		elif count%2!=0:
			mark='O'
			panels[digit]=mark
		b1.config(text=mark)
		count+=1
		sign=mark

		if (win(panels, sign) and sign=='X'):
			msg.showinfo("Result", "Player1 wins")
			root.destroy()
		elif (win(panels, sign) and sign=='O'):
			msg.showinfo("Result", "Player2 wins")
			root.destroy()
	if digit==2 and digit in digits:
		digits.remove(digit)
		if count%2==0:
			mark='X'
			panels[digit]=mark
		elif count%2!=0:
			mark='O'
			panels[digit]=mark
		b2.config(text=mark)
		count+=1
		sign=mark

		if (win(panels, sign) and sign=='X'):
			msg.showinfo("Result", "Player1 wins")
			root.destroy()
		elif (win(panels, sign) and sign=='O'):
			msg.showinfo("Result", "Player2 wins")
			root.destroy()

b1=Button(win,width=15,height=7,command=lambda:checker(1))
b1.grid(row=2,column=5)
b2=Button(win,width=15,height=7,font=50,command=lambda:checker(2))
b2.grid(row=2,column=6)
b3=Button(win,width=15,height=7,font=50,command=lambda:checker(3))
b3.grid(row=2,column=7)
b4=Button(win,width=15,height=7,font=50,command=lambda:checker(4))
b4.grid(row=3,column=5)
b5=Button(win,width=15,height=7,font=50,command=lambda:checker(5))
b5.grid(row=3,column=6)
b6=Button(win,width=15,height=7,font=50,command=lambda:checker(6))
b6.grid(row=3,column=7)
b7=Button(win,width=15,height=7,font=50,command=lambda:checker(7))
b7.grid(row=4,column=5)
b8=Button(win,width=15,height=7,font=50,command=lambda:checker(8))
b8.grid(row=4,column=6)
b9=Button(win,width=15,height=7,font=50,command=lambda:checker(9))
b9.grid(row=4,column=7)

win.mainloop()
