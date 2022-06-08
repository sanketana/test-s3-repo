import tkinter as tk

window = tk.Tk()

btn1 = tk.Button(window, text="Click Me", height=7, width=10)
btn2 = tk.Button(window, text="Click Me", height=7, width=10)
btn3 = tk.Button(window, text="Click Me", height=7, width=10)
btn4 = tk.Button(window, text="Click Me", height=7, width=10)
btn5 = tk.Button(window, text="Click Me", height=7, width=10)
btn6 = tk.Button(window, text="Click Me", height=7, width=10)
btn7 = tk.Button(window, text="Click Me", height=7, width=10)
btn8 = tk.Button(window, text="Click Me", height=7, width=10)
btn9 = tk.Button(window, text="Click Me", height=7, width=10)

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