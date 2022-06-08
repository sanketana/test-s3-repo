from tkinter import *

window = Tk()
window.geometry('300x300')

lbl1 = Label(window, text="I am a label with widget padx/y!", padx=20, pady=20, bg='white', fg='black')
btn1 = Button(window, text="Click Me!")
lbl2 = Label(window, text="I am a label with pack ipadx/y!", bg='white', fg='black')
lbl3 = Label(window, text="I am a label with pack padx/y!", bg='white', fg='black')


lbl1.pack(fill=X)
btn1.pack()
lbl2.pack(ipadx=30, ipady=30)
lbl3.pack(padx=50, pady=50)


window.mainloop()


# TODO
# how to use fill in y direction