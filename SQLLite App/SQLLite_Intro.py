import sqlite3

# Create a connection object
conn = sqlite3.connect('myDb2.db')

# Create a cursor object
curr = conn.cursor()

# Create a table
curr.execute("""CREATE TABLE users(id integer, name text, age integer)""")

# Insert a record into table
curr.execute("INSERT INTO users values (101, 'Abhinav', 40)")
curr.execute("INSERT INTO users values (102, 'Jaivant', 10)")

# Commit changes
conn.commit()


# Reading from table
curr1 = conn.cursor()

# Read data into a cursor using a Select query
curr1.execute("SELECT * FROM users")

# Transfer data from Cursor to a Python Tuples
records = curr1.fetchall()

# Iterate of Tuples and print them out
for record in records:
	print(record)