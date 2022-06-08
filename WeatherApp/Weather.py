import tkinter as tk


window = tk.Tk()

#window.configure(bg='white')
#window.geometry("600x600")

button1 = tk.Button(window, text="button1", width=10, height=7)
button2 = tk.Button(window, text="button2", width=10, height=7)
button3 = tk.Button(window, text="button3", width=10, height=7)
button4 = tk.Button(window, text="button4", width=10, height=7)
button5 = tk.Button(window, text="button5", width=10, height=7)
button6 = tk.Button(window, text="button6", width=10, height=7)
button7 = tk.Button(window, text="button7", width=10, height=7)
button8 = tk.Button(window, text="button8", width=10, height=7)
button9 = tk.Button(window, text="button9", width=10, height=7)

button1.grid(row=1, column=1)
button2.grid(row=1, column=2)
button3.grid(row=1, column=3)

button4.grid(row=2, column=1)
button5.grid(row=2, column=2)
button6.grid(row=2, column=3)

button7.grid(row=3, column=1)
button8.grid(row=3, column=2)
button9.grid(row=3, column=3)



