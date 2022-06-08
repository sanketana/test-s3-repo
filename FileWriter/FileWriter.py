import tkinter as tk
import csv

global lbl_account, ent_account, lbl_name, ent_name, lbl_age, ent_age, btn_save, txt_output
filename = 'data1.csv'

window = tk.Tk()
window.title("Address Book")

lbl_account = tk.Label(window, text="Scratch Account")
ent_account = tk.Entry(window)

lbl_name = tk.Label(window, text="Full Name")
ent_name = tk.Entry(window)

lbl_age = tk.Label(window, text="Age")
ent_age = tk.Entry(window)

txt_output = tk.Text(window)


def handleSave():
	with open(filename, 'a') as file:
		writer = csv.writer(file)
		writer.writerow([ent_account.get(), ent_name.get(), ent_age.get()])
	file.close()

def handleRead():
	file = open(filename, 'r')
	stuff = file.read()

	txt_output.insert(tk.END, stuff)
	file.close()


btn_save = tk.Button(window, text="Save", command=handleSave)
btn_read = tk.Button(window, text="Read", command=handleRead)

lbl_account.grid(row=1, column=1)
ent_account.grid(row=1, column=2)
lbl_name.grid(row=2, column=1)
ent_name.grid(row=2, column=2)
lbl_age.grid(row=3, column=1)
ent_age.grid(row=3, column=2)
btn_read.grid(row=4, column=1)
btn_save.grid(row=4, column=2)
txt_output.grid(row=5, column=1)


window.mainloop()