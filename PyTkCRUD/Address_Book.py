from tkinter import *
import tkinter.messagebox as mb
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mvemjsunp234$"
)

connector = mydb
cursor = mydb.cursor()

# Initializing the GUI window
root = Tk()
root.title('Contact Book')
root.geometry('700x550')
root.resizable(0, 0)

# Color and font variables
lf_bg = 'Gray70'
cf_bg = 'Gray57'
rf_bg = 'Gray35'
frame_font = ('Garamond', 14)

# Creating Widgets

# Header
heading_label = Label(root, text='CONTACT BOOK', font=("Noto Sans CJK TC", 15, "bold"), bg="Black", fg="White")

# Left, Center and Right Frames
left_frame = Frame(root, bg=lf_bg)
center_frame = Frame(root, bg=cf_bg)
right_frame = Frame(root, bg=rf_bg)


# Creating the StringVar variables
name_strvar = StringVar()
phone_strvar = StringVar()
email_strvar = StringVar()
search_strvar = StringVar()

# Left Frame Components
Label(left_frame, text='Name', bg=lf_bg, font=frame_font).place(relx=0.3, rely=0.05)

name_entry = Entry(left_frame, width=15, font=("Verdana", 11), textvariable=name_strvar)
name_entry.place(relx=0.1, rely=0.1)

Label(left_frame, text='Phone no.', bg=lf_bg, font=frame_font).place(relx=0.23, rely=0.2)

phone_entry = Entry(left_frame, width=15, font=("Verdana", 11), textvariable=phone_strvar)
phone_entry.place(relx=0.1, rely=0.25)

Label(left_frame, text='Email', bg=lf_bg, font=frame_font).place(relx=0.3, rely=0.35)

email_entry = Entry(left_frame, width=15, font=("Verdana", 11), textvariable=email_strvar)
email_entry.place(relx=0.1, rely=0.4)

Label(left_frame, text='Address', bg=lf_bg, font=frame_font).place(relx=0.28, rely=0.5)

address_entry = Text(left_frame, width=15, font=("Verdana", 11), height=5)
address_entry.place(relx=0.1, rely=0.55)


def list_contacts():
    global cursor
    cursor.execute('SELECT NAME FROM ADDRESS_BOOK.CONTACTS')
    fetch = cursor.fetchall()
    for data in fetch:
        listbox.insert(END, data)

def clear_fields():
    global name_strvar, phone_strvar, email_strvar, address_entry, listbox
    listbox.selection_clear(0, END)
    name_strvar.set('')
    phone_strvar.set('')
    email_strvar.set('')
    address_entry.delete(1.0, END)

def submit_record():
    global name_strvar, email_strvar, phone_strvar, address_entry
    global cursor
    name, email, phone, address = name_strvar.get(), email_strvar.get(), phone_strvar.get(), address_entry.get(1.0, END)
    if name=='' or email=='' or phone=='' or address=='':
        mb.showerror('Error!', "Please fill all the fields!")
    else:
        cursor.execute(
        "INSERT INTO ADDRESS_BOOK.CONTACTS (NAME, EMAIL, PHONE_NUMBER, ADDRESS) VALUES (%s,%s,%s,%s)", (name, email, phone, address))
        connector.commit()
        mb.showinfo('Contact added', 'We have stored the contact successfully!')
        listbox.delete(0, END)
        list_contacts()
        clear_fields()

def view_record():
    global name_strvar, phone_strvar, email_strvar, address_entry, listbox, cursor
    queryString = "SELECT * FROM ADDRESS_BOOK.CONTACTS WHERE NAME='" + listbox.get(ACTIVE) + "'"
    cursor.execute(queryString)
    values = cursor.fetchall()[0]
    name_strvar.set(values[1]); phone_strvar.set(values[3]); email_strvar.set(values[2])
    address_entry.delete(1.0, END)
    address_entry.insert(END, values[4])

def clear_fields():
    global name_strvar, phone_strvar, email_strvar, address_entry, listbox
    listbox.selection_clear(0, END)
    name_strvar.set('')
    phone_strvar.set('')
    email_strvar.set('')
    address_entry.delete(1.0, END)

def search():
   global connector
   query = str(search_strvar.get())
   if query != '':
       listbox.delete(0, END)
       cursor.execute('SELECT * FROM ADDRESS_BOOK.CONTACTS WHERE NAME LIKE %s', ('%'+query+'%', ))
       check = cursor.fetchall()
       for data in check:
         listbox.insert(END, data[1])    

def delete_record():
    global listbox, connector, cursor
    if not listbox.get(ACTIVE):
        mb.showerror("No item selected", "You have not selected any item!")
    cursor.execute('DELETE FROM ADDRESS_BOOK.CONTACTS WHERE NAME=%s', (listbox.get(ACTIVE)))
    connector.commit()
    mb.showinfo('Contact deleted', 'The desired contact has been deleted')
    listbox.delete(0, END)
    list_contacts()

def delete_all_records():
    cursor.execute('DELETE FROM ADDRESS_BOOK.CONTACTS')
    connector.commit()
    mb.showinfo("All records deleted", "All the records in your contact book have been deleted")
    listbox.delete(0, END)
    list_contacts()

# Middle Frame Components
search_entry = Entry(center_frame, width=18, font=("Verdana", 12), textvariable=search_strvar).place(relx=0.13, rely=0.04)
Button(center_frame, text='Search', font=frame_font, width=15, command=search).place(relx=0.13, rely=0.1)
Button(center_frame, text='Add Record', font=frame_font, width=15, command=submit_record).place(relx=0.13, rely=0.2)
Button(center_frame, text='View Record', font=frame_font, width=15, command=view_record).place(relx=0.13, rely=0.3)
Button(center_frame, text='Clear Fields', font=frame_font, width=15, command=clear_fields).place(relx=0.13, rely=0.4)
Button(center_frame, text='Delete Record', font=frame_font, width=15, command=delete_record).place(relx=0.13, rely=0.5)
Button(center_frame, text='Delete All Records', font=frame_font, width=15, command=delete_all_records).place(relx=0.13, rely=0.6)

# Right Frame Components
Label(right_frame, text='Saved Contacts', font=("Noto Sans CJK TC", 14), bg=rf_bg).place(relx=0.25, rely=0.05)
listbox = Listbox(right_frame, selectbackground='SkyBlue', bg='Gainsboro', fg='Black', font=('Helvetica', 12), height=20, width=25)
scroller = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
scroller.place(relx=0.93, rely=0, relheight=1)
listbox.config(yscrollcommand=scroller.set)
listbox.place(relx=0.1, rely=0.15)

# Placing Widgets
heading_label.pack(side=TOP, fill=X)
left_frame.place(relx=0, relheight=1, y=30, relwidth=0.3)
center_frame.place(relx=0.3, relheight=1, y=30, relwidth=0.3)
right_frame.place(relx=0.6, relheight=1, y=30, relwidth=0.4)



