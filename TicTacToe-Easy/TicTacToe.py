from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic Tac Toe by Abhinav')
#root.iconbitmap('logo.ico')

global b1, b2, b3, b4, b5, b6, b7, b8, b9
global count
count = 0
player = 'X' 

def button_click(b):
	global player, count
	if b["text"] == " " and player == "X":
		b["text"] = "O"
		player = "O"
		count = count + 1		
		check_if_won()
	elif b["text"] == " " and player == "O":
		b["text"] = "X"
		player = "X"
		count = count + 1
		check_if_won()
	else:
		messagebox.showerror("Tic Tic Toe", "That box has already been selected. Choose another one...")


def check_if_won():
	global winner
	somone_won = False

	if b1["text"] == b2["text"] and b2["text"] == b3["text"]:
			winner = True


		if b1["text"] == 'X':
			messagebox.showinfo("Winner", "X Wins!")
			winner = True
		elif b1["text"] == 'O':
			winner = True
			messagebox.showinfo("Winner", "O Wins!")

	elif b4["text"] == b5["text"] and b5["text"] == b6["text"]:
		if b4["text"] == 'X':
			winner = True
			messagebox.showinfo("Winner", "X Wins!")
		elif b4["text"] == 'O':
			winner = True
			messagebox.showinfo("Winner", "O Wins!")

	#Check if tie
	if count == 9 and winner == False:
		messagebox.showinfo("Tic Tac Toe", "It's A Tie!\nNo One Wins!")



b1 = Button(root, text=" ", height=4, width=5, command=lambda: button_click(b1))
b2 = Button(root, text=" ", height=4, width=5, command=lambda: button_click(b2))
b3 = Button(root, text=" ", height=4, width=5, command=lambda: button_click(b3))
b4 = Button(root, text=" ", height=4, width=5, command=lambda: button_click(b4))
b5 = Button(root, text=" ", height=4, width=5, command=lambda: button_click(b5))
b6 = Button(root, text=" ", height=4, width=5, command=lambda: button_click(b6))
b7 = Button(root, text=" ", height=4, width=5, command=lambda: button_click(b7))
b8 = Button(root, text=" ", height=4, width=5, command=lambda: button_click(b8))
b9 = Button(root, text=" ", height=4, width=5, command=lambda: button_click(b9))

b1.grid(row=1, column = 1)
b2.grid(row=1, column = 2)
b3.grid(row=1, column = 3)
b4.grid(row=2, column = 1)
b5.grid(row=2, column = 2)
b6.grid(row=2, column = 3)
b7.grid(row=3, column = 1)
b8.grid(row=3, column = 2)
b9.grid(row=3, column = 3)

root.mainloop()