import tkinter as tk
import csv

filename = 'data.csv'

window = tk.Tk()
window.title("Address Book")

def handleSave():
	# do some stuff here
	with open(filename, 'a') as file:
		writer = csv.writer(file)
		writer.writerow([ent_account.get(), ent_name.get()])
	file.close()


lbl_account = tk.Label(window, text="Scratch Account")
ent_account = tk.Entry(window)

lbl_name = tk.Label(window, text="Name")
ent_name = tk.Entry(window)

btn_read = tk.Button(window, text="Read")
btn_save = tk.Button(window, text="Save", command=handleSave)

txt_output = tk.Text(window)

lbl_account.grid(row=1, column=1)
ent_account.grid(row=1, column=2)
lbl_name.grid(row=2, column=1)
ent_name.grid(row=2, column=2)
btn_read.grid(row=3, column=1)
btn_save.grid(row=3, column=2)
txt_output.grid(row=4, column=1)

window.mainloop()