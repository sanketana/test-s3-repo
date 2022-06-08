from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Tic Tac Toe")

#global nextTurn
nextTurn = 'X'
count = 0

def disable_all_buttons():
	btn1.config(state=DISABLED)
	btn2.config(state=DISABLED)
	btn3.config(state=DISABLED)
	btn4.config(state=DISABLED)
	btn5.config(state=DISABLED)
	btn6.config(state=DISABLED)
	btn7.config(state=DISABLED)
	btn8.config(state=DISABLED)
	btn9.config(state=DISABLED)

def checkIfWon():

	# First row same
	if (btn1['text'] == btn2['text'] and btn2['text'] == btn3['text'] and btn1['text'] != ' '):
		disable_all_buttons()
		messagebox.showinfo("You Win", f"{btn1['text']} has won!")
	# Second row same
	elif (btn4['text'] == btn5['text'] and btn5['text'] == btn6['text'] and btn4['text'] != ' '):
		disable_all_buttons()		
		messagebox.showinfo("You Win", f"{btn4['text']} has won!")
	# Third row same
	elif (btn7['text'] == btn8['text'] and btn8['text'] == btn9['text'] and btn7['text'] != ' '):
		disable_all_buttons()		
		messagebox.showinfo("You Win", f"{btn7['text']} has won!")
	# First column same
	elif (btn1['text'] == btn4['text'] and btn4['text'] == btn7['text'] and btn1['text'] != ' '):
		disable_all_buttons()		
		messagebox.showinfo("You Win", f"{btn1['text']} has won!")
	# Second column same
	elif (btn2['text'] == btn5['text'] and btn5['text'] == btn8['text'] and btn2['text'] != ' '):
		disable_all_buttons()		
		messagebox.showinfo("You Win", f"{btn2['text']} has won!")
	# Third column same
	elif (btn3['text'] == btn6['text'] and btn6['text'] == btn9['text'] and btn3['text'] != ' '):
		disable_all_buttons()		
		messagebox.showinfo("You Win", f"{btn3['text']} has won!")
	# Top Left to Bottom Right diagonal
	elif (btn1['text'] == btn5['text'] and btn5['text'] == btn9['text'] and btn1['text'] != ' '):
		disable_all_buttons()		
		messagebox.showinfo("You Win", f"{btn1['text']} has won!")
	# Top Right to Bottom Left diagonal
	elif (btn3['text'] == btn5['text'] and btn5['text'] == btn7['text'] and btn3['text'] != ' '):
		disable_all_buttons()		
		messagebox.showinfo("You Win", f"{btn3['text']} has won!")
	else:
		if (count == 9):
			disable_all_buttons()			
			messagebox.showinfo("Tie", "It's a Tie!!")



def click(b):
	global nextTurn, count

	if nextTurn == 'X' and b['text'] == ' ':
		b['text'] = 'X'
		nextTurn = 'O'
		count += 1
		checkIfWon()
	elif nextTurn == 'O' and b['text'] == ' ':
		b['text'] = 'O'
		nextTurn = 'X'	
		count += 1		
		checkIfWon()	


# Creating buttons
btn1 = Button(window, height=3, width=6, text = " ", command= lambda: click(btn1))
btn2 = Button(window, height=3, width=6, text = " ", command= lambda: click(btn2))
btn3 = Button(window, height=3, width=6, text = " ", command= lambda: click(btn3))
btn4 = Button(window, height=3, width=6, text = " ", command= lambda: click(btn4))
btn5 = Button(window, height=3, width=6, text = " ", command= lambda: click(btn5))
btn6 = Button(window, height=3, width=6, text = " ", command= lambda: click(btn6))
btn7 = Button(window, height=3, width=6, text = " ", command= lambda: click(btn7))
btn8 = Button(window, height=3, width=6, text = " ", command= lambda: click(btn8))
btn9 = Button(window, height=3, width=6, text = " ", command= lambda: click(btn9))


# Grid it
btn1.grid(row=1, column=1)
btn2.grid(row=1, column=2)
btn3.grid(row=1, column=3)
btn4.grid(row=2, column=1)
btn5.grid(row=2, column=2)
btn6.grid(row=2, column=3)
btn7.grid(row=3, column=1)
btn8.grid(row=3, column=2)
btn9.grid(row=3, column=3)

window.mainloop()