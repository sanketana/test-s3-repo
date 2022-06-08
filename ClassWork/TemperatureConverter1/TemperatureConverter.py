import tkinter as tk

window = tk.Tk()

label1 = tk.Label(window, text="Temperature Converter")
label2 = tk.Label(window, text="Celcius")
label3 = tk.Label(window, text="Fahrenhiet")
ent1 = tk.Entry(window)
btn1 = tk.Button(window, text="Convert")
ent2 = tk.Entry(window)


label1.grid(row=1, column=2)
label2.grid(row=2, column=1)
label3.grid(row=2, column=3)
ent1.grid(row=3, column=1)
btn1.grid(row=3, column=2)
ent2.grid(row=3, column=3)

window.mainloop()