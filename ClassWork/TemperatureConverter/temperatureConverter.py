import tkinter as tk

window = tk.Tk()

lbl_title = tk.Label(window, text="Temperature Converter")
ent_celcius = tk.Entry(window)
ent_fahrenheit = tk.Entry(window)
btn_convert = tk.Button(window, text="Convert")

lbl_title.grid(row=1, column=2)
ent_celcius.grid(row=2, column=1)
ent_fahrenheit.grid(row=2, column=3)
btn_convert.grid(row=2, column=2)

window.mainloop()