import tkinter as tk

window = tk.Tk()

l1 = tk.Label(window, text="label")
b1 = tk.Button(window, text="Click me")

l1.grid(row = 1, column=1)
b1.grid(row = 1, column=2)