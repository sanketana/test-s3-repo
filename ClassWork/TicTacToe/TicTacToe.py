import tkinter as tk

window = tk.Tk()
window.title("Tic Tac Toe")

global turn
turn = 'X'

btn1 = tk.Button(window, height=7, width=10)
btn1.grid(row=1, column=1)
btn2 = tk.Button(window, height=7, width=10).grid(row=1, column=2)
btn3 = tk.Button(window, height=7, width=10).grid(row=1, column=3)

btn4 = tk.Button(window, height=7, width=10).grid(row=2, column=1)
btn5 = tk.Button(window, height=7, width=10).grid(row=2, column=2)
btn6 = tk.Button(window, height=7, width=10).grid(row=2, column=3)

btn7 = tk.Button(window, height=7, width=10).grid(row=3, column=1)
btn8 = tk.Button(window, height=7, width=10).grid(row=3, column=2)
btn9 = tk.Button(window, height=7, width=10).grid(row=3, column=3)
#btn1.grid(row=1, column=1)

def btn1_clicked(event):
	btn1.config(text=turn)



btn1.bind('<Button>', btn1_clicked)

window.mainloop()