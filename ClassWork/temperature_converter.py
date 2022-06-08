from tkinter import *

window = Tk()


#Function to convert and update text boxes
def convert():
	#get the value from f
	celcius_value = int(ent_celcius.get())

	#convert it
	fahrenheit_value = round((celcius_value * (9/5) ) + 32, 1)



	#set the c
	ent_fahrenheit.delete(0, END)
	ent_fahrenheit.insert(0, fahrenheit_value)


# Create Widgets
lbl_title = Label(window, text='Temperature Converter')
lbl_celcius = Label(window, text='Celcius')
lbl_fahrenheit = Label(window, text='Fahreheit')
ent_celcius = Entry(window)
ent_fahrenheit = Entry(window)
btn_convert = Button(window, text='Convert', command=convert)

# Grid the Widgets
lbl_title.grid(row=1, column=2)
lbl_celcius.grid(row=2, column=1)
lbl_fahrenheit.grid(row=2, column=3)
ent_celcius.grid(row=3, column=1)
ent_fahrenheit.grid(row=3, column=3)
btn_convert.grid(row=3, column=2)

window.mainloop()