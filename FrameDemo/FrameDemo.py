from tkinter import *

window = Tk()
window.title('Frame Demo App')
window.geometry('600x400')

# Login button event handler
def login():
	frm_login.pack_forget()
	frm_main.pack()
	lbl_greetings['text'] = f'Hello Mr. {ent_username.get()}!'


# First Screen
frm_login = Frame(window)
lbl_username = Label(frm_login, text='Username')
ent_username = Entry(frm_login)
lbl_password = Label(frm_login, text='Password')
ent_password = Entry(frm_login, show='*')
btn_login = Button(frm_login, text='Login', command=login)


# Second Screen
frm_main = Frame(window)
lbl_greetings = Label(frm_main, text='')

# Packing 1st Screen
lbl_username.pack()
ent_username.pack()
lbl_password.pack()
ent_password.pack()
btn_login.pack()


# Packing 2nd Screen
lbl_greetings.pack()

# Open first screen
frm_login.pack()

window.mainloop()