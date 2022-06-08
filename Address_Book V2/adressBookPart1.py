#--------------------------------------
# Author      :   Younes Derfoufi
# Company     :   CRMEF OUJDA
# ------------------------------------
# -*- coding: utf-8 -*-
from tkinter import ttk
#import tkinter as tk
from tkinter import *
from tkinter import filedialog 
import os
#from PIL import Image, ImageTk
import sqlite3  

   
root = Tk()
root.title("Address Book")
root.geometry("550x480")
#root.configure(bg = "#eaeaea")

# Add Title
lblTitle = Label(root , text = "Address Book" , font = ("Arial" , 21) , bg="darkblue" , fg = "white" )
lblTitle.place(x=0 , y=0 , width=250)

# Search area
lbSearchByName = Label(root , text = "Search by name :"  , bg="darkblue" , fg = "white" )
lbSearchByName.place(x=250 , y=0 , width=120)
entrySearchByName = Entry(root)
entrySearchByName.place(x=380 , y=0 , width=160)

lbSearchByPhone = Label(root , text = "Search by name :"  , bg="darkblue" , fg = "white" )
lbSearchByPhone.place(x=250 , y=20 , width=120)
entrySearchByPhone = Entry(root)
entrySearchByPhone.place(x=380 , y=20 , width=160)



# Label & Entry name
lblName = Label(root , text = "Name & surname:" ,  bg="black" , fg = "yellow")
lblName.place(x=5 , y = 50 , width = 125)

entryName = Entry(root)
entryName.place(x = 140,  y =50 , width=400)


# Label & Entry Phone
lblPhone = Label(root , text = "Phone Number:" , bg="black" , fg = "yellow")
lblPhone.place(x=5 , y=80 ,  width = 125 )
entryPhone = Entry(root)
entryPhone.place(x = 140,  y =80 , width=400)


# Label & Entry Photo
lblPhoto = Label(root , text = "Photo:" , bg="black" , fg = "yellow")
lblPhoto.place(x=5 , y=110 ,  width = 125 )
bPhoto = Button(root , text = "Browse" , bg="darkblue" , fg = "yellow" )
bPhoto.place(x= 480 ,  y = 110 , height = 25)
entryPhoto = Entry(root)
entryPhoto.place(x = 140,  y =110 , width=320)

# More Info
lblMore = Label(root , text = "More Info:" , bg="black" , fg = "yellow")
lblMore.place(x=5 , y=140 ,  width = 125 )
entryMore = Entry(root)
entryMore.place(x = 140,  y =140 , width=400)

# Command Button
bAdd = Button(root , text = "Add Customer" , bg="darkblue" , fg = "yellow")
bAdd.place(x= 5 ,  y = 170 , width = 255)

bDelete = Button(root , text = "Delete Selected" , bg="darkblue" , fg = "yellow")
bDelete.place(x= 5 ,  y = 205 , width = 255)

bEdit = Button(root , text = "Edit Selected" , bg="darkblue" , fg = "yellow" )
bEdit.place(x= 5 ,  y = 240 , width = 255)

bSort= Button(root , text = "Sort by name" , bg="darkblue" , fg = "yellow" )
bSort.place(x= 5 ,  y = 275 , width = 255)

bExit= Button(root , text = "Exit App" , bg="darkblue" , fg = "yellow" )
bExit.place(x= 5 ,  y = 310 , width = 255)

# Load Image
  

# Add Treeview




root.mainloop()