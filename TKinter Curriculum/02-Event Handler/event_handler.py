import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.geometry("300x200")

def button_click():
	messagebox.showinfo("Info", "Hello TKinter")

b1 = tk.Button(root, text="Click Me!", command=button_click)

b1.grid(row=1, column=1)

root.mainloop()