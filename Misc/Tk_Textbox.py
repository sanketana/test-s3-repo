from tkinter import *

window = Tk()


def eventHandler():
	label1['text'] = 'Hello Mr. ' + entry1.get()

entry1 = Entry(window)
button1 = Button(window, text='Click Me!', padx = 2, pady = 2, command=eventHandler)
label1 = Label(window, text='')

#placing button on window

#Method# 1 - Using pack
#button1.pack()


#Method# 2 - Using Grid
entry1.grid(row=0, column=1)
button1.grid(row=1, column=1)
label1.grid(row=2, column=1)

window.mainloop()