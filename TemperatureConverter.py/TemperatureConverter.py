import tkinter as tk


window = tk.Tk()

lbl_title = tk.Label(window, text="Temperature Converter")
lbl_celcius = tk.Label(window, text="Celcius")
lbl_Fahrenheit = tk.Label(window, text="Fahrenheit")
ent_celcius = tk.Entry(window)
ent_Fahrenheit = tk.Entry(window)

def handle_submit():
	celcius_val = ent_celcius.get()
	fahrenheit_val = (float(celcius_val) * (9/5)) + 32
	ent_Fahrenheit.delete(0, 10)
	ent_Fahrenheit.insert(0, fahrenheit_val)


btn_convert = tk.Button(window, text = "Convert", command=handle_submit)


lbl_title.grid(row=1, column=2)
lbl_celcius.grid(row=2, column=1)
ent_celcius.grid(row=3, column=1)
btn_convert.grid(row=3, column=2)
lbl_Fahrenheit.grid(row=2, column=3)
ent_Fahrenheit.grid(row=3, column=3)

window.mainloop()