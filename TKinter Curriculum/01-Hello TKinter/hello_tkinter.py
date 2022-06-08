import tkinter as tk

root = tk.Tk()

root.geometry("300x200")

b1 = tk.Label(root, text="Hello TKinter!")

b1.grid(row=1, column=1)

root.mainloop()