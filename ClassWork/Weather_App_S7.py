import pyowm
import tkinter as tk


#Creating Parent Window
window = tk.Tk()
window.title("My Weather App")


#Creating Widgets (Label, Textbox and Buttons)
lbl_title = tk.Label(window, text="My Weather App")
lbl_search = tk.Label(window, text="City Name (eg: Delhi, IN) ")
ent_place = tk.Entry(window)
lbl_result = tk.Label(window, text="")


#Search Button
btn_submit = tk.Button(window, text="Get Current Weather")

#Place Widgets on Window
lbl_title.grid(row=1, column=2)
lbl_search.grid(row=2, column=1)
ent_place.grid(row=2, column=2)
btn_submit.grid(row=2, column=3)
lbl_result.grid(row=3, column=2)

#Event Loop
window.mainloop()