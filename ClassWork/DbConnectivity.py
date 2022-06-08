import sqlite3

conn = sqlite3.connect('myDb.db')

curr = conn.cursor()

#curr.execute('CREATE TABLE IF NOT EXISTS user(id integer, name text, age integer)')

#curr.execute("INSERT INTO user values(101, 'Abhinav', 40)")
#curr.execute("INSERT INTO user values(102, 'Advait', 8)")

#curr.execute("DELETE FROM user WHERE name == 'Abhinav' ")

curr.execute("UPDATE user set name = 'Siddhant' WHERE  name == 'Advait' ")

curr.execute("SELECT * FROM user")



records = curr.fetchall()

for record in records:
	print(record)


conn.commit()