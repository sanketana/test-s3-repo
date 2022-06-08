import datetime
import tkinter as tk
from PIL import Image, ImageTk


window = tk.Tk()

image = Image.open('image.png')
image.thumbnail((200, 500), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)

label_name = tk.Label(text = "Name")
entry_name = tk.Entry()

label_year = tk.Label(text = "Year")
entry_year = tk.Entry()

label_month = tk.Label(text = "Month")
entry_month = tk.Entry()

label_day = tk.Label(text = "Day")
entry_day = tk.Entry()

text_output = tk.Text(window, height=10, width=25)

def calculate_age():
	year_of_birth = int(entry_year.get())
	month_of_birth = int(entry_month.get())
	day_of_birth = int(entry_day.get())

	date_of_birth = datetime.date(year_of_birth, month_of_birth, day_of_birth)
	current_date = datetime.date.today()

	age = current_date - date_of_birth

	nm = entry_name.get()
	msg = f'Hey {nm}, Your age is {age.days} days '	
	text_output.insert(tk.END, msg)


my_button = tk.Button(window, text="Calculate Age", command=calculate_age)


label_image.grid(column=2, row=1)

label_name.grid(column=1, row=2)
entry_name.grid(column=2, row=2)
label_year.grid(column=1, row=3)
entry_year.grid(column=2, row=3)
label_month.grid(column=1, row=4)
entry_month.grid(column=2, row=4)
label_day.grid(column=1, row=5)
entry_day.grid(column=2, row=5)
my_button.grid(column=2, row=6)
text_output.grid(column=2, row=7)

window.mainloop()