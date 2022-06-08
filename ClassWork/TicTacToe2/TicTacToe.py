import tkinter as tk

global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9
global turn
turn = "X"

window = tk.Tk()


def b_click(btn):

	btn["text"] = turn

	if (turn == "X"):
		turn = "O"
	else:
		turn = "X"


btn1 = tk.Button(window, height=3, width=6, command=lambda: b_click(btn1))
btn2 = tk.Button(window, height=3, width=6, command=lambda: b_click(btn2))
btn3 = tk.Button(window, height=3, width=6, command=lambda: b_click(btn3))
btn4 = tk.Button(window, height=3, width=6, command=lambda: b_click(btn4))
btn5 = tk.Button(window, height=3, width=6, command=lambda: b_click(btn5))
btn6 = tk.Button(window, height=3, width=6, command=lambda: b_click(btn6))
btn7 = tk.Button(window, height=3, width=6, command=lambda: b_click(btn7))
btn8 = tk.Button(window, height=3, width=6, command=lambda: b_click(btn8))
btn9 = tk.Button(window, height=3, width=6, command=lambda: b_click(btn9))

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