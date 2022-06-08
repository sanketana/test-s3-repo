import tkinter as tk
from tkinter import messagebox


def handle_submit():
	str_name = ent_name.get()
	messagebox.showinfo(title="Info", message=f"Hello! {str_name}")

window = tk.Tk()	

frm_name = tk.Frame(master=window)
lbl_name = tk.Label(master=frm_name, text="Full Name: ")
btn_submit = tk.Button(master=window, text="Submit", command=handle_submit)
ent_name = tk.Entry(master=frm_name)

lbl_name.pack(side=tk.LEFT)
ent_name.pack(side=tk.LEFT)
frm_name.pack()
btn_submit.pack()

window.mainloop()