import mysql.connector
from tkinter import *
from tkinter import ttk

mydb = mysql.connector.connect(host="localhost", user="root", password="mvemjsunp234$")

mycursor = mydb.cursor()

mycursor.execute("SELECT FILM_ID, TITLE, DESCRIPTION, RELEASE_YEAR, LANGUAGE_ID, RENTAL_RATE, LENGTH, RATING FROM SAKILA.FILM")

myresult = mycursor.fetchall()




root = Tk()
root.geometry("1200x700+0+0")	

columns = ('FILM_ID', 'TITLE', 'DESCRIPTION', 'RELEASE_YEAR', 'LANGUAGE_ID', 'RENTAL_RATE', 'LENGTH', 'RATING')

frame = Frame(root)

tree = ttk.Treeview(frame, columns=columns, show='headings', height=30)
tree.heading('FILM_ID', text='Film Id')
tree.heading('TITLE', text='Name')
tree.heading('DESCRIPTION', text='Description')
tree.heading('RELEASE_YEAR', text='Release Year')
tree.heading('LANGUAGE_ID', text='Language')
tree.heading('RENTAL_RATE', text='Rental Rate')
tree.heading('LENGTH', text='Length')
tree.heading('RATING', text='Rating')

hsb = Scrollbar(frame, orient=HORIZONTAL)

for row in myresult: 
	tree.insert('', END, values=row)

tree.pack(side=TOP)
hsb.pack(side=BOTTOM, fill=X)

tree.config(xscrollcommand=hsb.set)
hsb.config(command=tree.xview)

frame.pack()


root.mainloop()