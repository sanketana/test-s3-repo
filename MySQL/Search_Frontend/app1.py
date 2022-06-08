import mysql.connector
from tkinter import *
from tkinter import ttk

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mvemjsunp234$"
)

root = Tk()
root.geometry("1200x700+0+0")
root.title("My MovieDb Search")

# Function to Refresh Treeview
def refresh(): 
	mycursor = mydb.cursor()
	# Convert to upper case and append leading and trailing % for fuzzy search
	query_filter = "'%" + searchbox.get().upper() + "%'"
	sql_query = f"select film_id, title, description, release_year, language_id, rental_rate, length, rating from sakila.film where title like {query_filter} or description like {query_filter}"
	mycursor.execute(sql_query)
	myresult = mycursor.fetchall()	

	# Clear the Tree View
	for i in tree.get_children():
   		tree.delete(i)
	root.update()

	# Populate the Tree View
	for row in myresult: 
		tree.insert('', END, values=row)	

# List columns
columns = ('film_id', 'title', 'description', 'release_year', 'language_id', 'rental_rate', 'length', 'rating')

# Create a Frame
frame = Frame(root)

# Create a header label
headerlabel = Label(frame, text="My MovieDb Search", font=("Helvetica", "24"))

# Create a Search Text box and set default value
searchbox = Entry(frame)

# Create a Search button
searchbutton = Button(frame, text="Search", command=refresh)

# Create a Treeview
tree = ttk.Treeview(frame, columns=columns, show='headings', height=30)

# Create a horizontal scrollbar
hsb = Scrollbar(frame, orient=HORIZONTAL)

# Define headings of each column
tree.heading('film_id', text='FILM ID')
tree.heading('title', text='TITLE')
tree.heading('description', text='DESCRIPTION')
tree.heading('release_year', text='RELEASE YEAR')
tree.heading('language_id', text='LANGUAGE ID')
tree.heading('rental_rate', text='RENTAL RATE')
tree.heading('length', text='LENGTH')
tree.heading('rating', text='RATING')



# Geometry Managers
headerlabel.pack()
searchbox.pack()
searchbutton.pack()
tree.pack(side=TOP)
hsb.pack(side=BOTTOM, fill=X)
frame.pack()

# Linking Scrollbar and Treeview together
tree.config(xscrollcommand=hsb.set)
hsb.config(command=tree.xview)

# Calling Refresh function when loading screen
refresh()

root.mainloop()