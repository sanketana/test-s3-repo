import tkinter as tk

window = tk.Tk()
window.title("Calorify by Prateek")
window.geometry("500x200")

# Create global widgets
global lbl_enter_age, ent_age, btn_submit, lbl_suggested_intake, btn_proceed

# Frame for Screen 1
frm_screen1 = tk.Frame(window)

# Frame for Screen 2
frm_screen2 = tk.Frame(window)

# Defining handleSubmit
def handleSubmit():
	# write the code for finding correct calorie intake, using if else
	# Based on the if-else, change the text of the label "lbl suggeted intake"
	# here is how you do it: lbl_suggested_intake.configure(text = "Suggested claories")
	lbl_suggested_intake.configure(text = "100 Calories")

def handleProceed():
	# write the code to go to next screen
	frm_screen1.pack_forget()
	frm_screen2.pack()	

def handleCalculate():
	# Calculate the calories based on which checkboxes are selected
	# add them up and update the below variable
	calculated_calories = 250
	calculated_calories_text = str(calculated_calories) + " Calories"
	lbl_calculated_calories.configure(text = calculated_calories_text)

# Widgets for Screen 1 
lbl_enter_age = tk.Label(frm_screen1, text="Enter Your Age: ")
ent_age = tk.Entry(frm_screen1)
btn_submit = tk.Button(frm_screen1, text="Enter", command=handleSubmit)
lbl_suggested_intake = tk.Label(frm_screen1, text="Suggested Intake")
btn_proceed = tk.Button(frm_screen1, text="Proceed", command=handleProceed)

# Widgets for Screen 2
chk_pizza = tk.Checkbutton(frm_screen2, text="Pizza")
chk_burger = tk.Checkbutton(frm_screen2, text="Burger")
lbl_calculated_calories = tk.Label(frm_screen2)
btn_calculate = tk.Button(frm_screen2, text="Calculate", command=handleCalculate)


# Placing Screen 1 Widgets
lbl_enter_age.grid(row=1, column=1)
ent_age.grid(row=2, column=1)
btn_submit.grid(row=3, column=1)
lbl_suggested_intake.grid(row=4, column=1)
btn_proceed.grid(row=5, column=1)

# Placing Screen 2 Widgets
chk_pizza.grid(row=1, column=1)
chk_burger.grid(row=1, column=2)
lbl_calculated_calories.grid(row=2, column=1)
btn_calculate.grid(row=2, column=2)

# Showing Screen1
frm_screen1.pack()

# Event Loop
window.mainloop()