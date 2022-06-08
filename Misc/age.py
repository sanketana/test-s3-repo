import datetime
import tkinter as tk
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry


window = tk.Tk()

#image = Image.open('image.png')
#image.thumbnail((200, 500), Image.ANTIALIAS)
#photo = ImageTk.PhotoImage(image)
#label_image = tk.Label(image=photo)

label_name = tk.Label(text = "Name")
entry_name = tk.Entry()

label_year = tk.Label(text = "Date of Birth")
dt_dob = DateEntry()



text_output = tk.Text(window, height=10, width=25)

def calculate_age():
	date_of_birth = dt_dob.get_date()
	current_date = datetime.date.today()

	age = current_date - date_of_birth
	age_days = age.days
	age_years = int(age_days / 365)
	age_months = int((age_days % 365) / 30)

	nm = entry_name.get()
	msg = f'Hey {nm}, Your age is {age_years} years and {age_months} months!'	
	text_output.insert(tk.END, msg)


my_button = tk.Button(window, text="Calculate Age", command=calculate_age)


#label_image.grid(column=2, row=1)

label_name.grid(column=1, row=2)
entry_name.grid(column=2, row=2)
label_year.grid(column=1, row=3)
dt_dob.grid(column=2, row=3)
my_button.grid(column=2, row=4)
text_output.grid(column=2, row=5)

window.mainloop()
